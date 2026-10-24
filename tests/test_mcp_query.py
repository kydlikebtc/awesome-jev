"""What the MCP server's tools answer, tested on a handful of rows (I33).

src/awesome_jev_mcp/query.py holds every decision the five tools make — which
rows count as examples, which caveats travel, the order, the model-string
check — as functions over the data they are handed. It is standard library
only, so these tests import it directly: no `mcp`, no network, no catalogue
file. The last class checks that server.py hands its tools' arguments and data
to these functions unchanged, through the stubbed loader in
test_mcp_caveats.py.
"""

from __future__ import annotations

import ast
import copy
import inspect
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "src" / "awesome_jev_mcp"
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "src"))

from awesome_jev_mcp import query  # noqa: E402
from test_mcp_caveats import load_server  # noqa: E402

PATTERNS = [
    {"key": "tool-selection", "en": "Tool selection", "blurb_en": "Which tool to call next."},
    {"key": "safety-gating", "en": "Safety gating", "blurb_en": "Whether to let an action through."},
    {"key": "human-escalation", "en": "Human escalation", "blurb_en": "When to ask a person."},
    {"key": "overview", "en": "Overview", "blurb_en": "Surveys the space."},
]


def row(slug: str, **fields) -> dict:
    base = {
        "slug": slug,
        "title": slug.title(),
        "url": f"https://github.com/o/{slug}",
        "summary": f"{slug} summary",
        "kind": "project",
        "patterns": ["tool-selection"],
    }
    return {**base, **fields}


ROWS = [
    row("router", title="Router", has_code=True, stars=40, languages=["python"], question_types=["choice"],
        platforms=["typesafe-api"], flags=["vendor-reported", "single-commit"], notes="Routes by cost."),
    row("gate", title="gate", has_code=True, stars=400, patterns=["tool-selection", "safety-gating"],
        languages=["typescript"], platforms=["cloudflare-workers-ai"]),
    row("vendor-docs", title="Vendor docs", kind="official-docs", official=True, patterns=["overview"]),
    row("clone", title="Clone", kind="alternative", has_code=True, stars=4000, flags=["not-jev"]),
    row("dry-run", title="Dry run", has_code=True, stars=90, flags=["shadow-mode-only"], primitives_seen=["noul"]),
]

# A made-up compat.json: its strings are fixtures, not claims about any vendor.
# Vendor API and Gate Router both stand for rows recording typesafe-api, so
# both are coarse; Cloud Workers alone for cloudflare-workers-ai.
COMPAT = {
    "as_of": "2031-01-01",
    "platforms": [
        {"id": "vendor-api", "name": "Vendor API", "official": True, "model": "acme-latest (default) · jev-9.1.0",
         "endpoint": "POST /v1/decide", "env": "ACME_KEY", "catalog_platforms": ["typesafe-api"],
         "granularity": "coarse"},
        {"id": "gate-router", "name": "Gate Router", "model": "acme/jev-9.1 · ~acme/jev", "endpoint": "POST /gate/v1",
         "env": "GATE_KEY", "catalog_platforms": ["gate-router", "typesafe-api"], "granularity": "coarse"},
        {"id": "cloud-workers", "name": "Cloud Workers", "model": "@cf/acme/jev-9.1", "endpoint": "env.AI.run()",
         "env": "binding", "catalog_platforms": ["cloudflare-workers-ai"]},
        {"id": "docs-only", "name": "Docs only", "model": "—", "endpoint": "—", "env": "—", "catalog_platforms": []},
    ],
    "limits": [{"k": "choice options", "n": {"max": 3}}],
    "not_model_strings": [{"s": "acme/jev-9", "why": "Nobody documents it."}],
}


def slugs(result: dict) -> list[str]:
    return [r["slug"] for r in result["results"]]


class SearchTest(unittest.TestCase):
    def search(self, rows=ROWS, **filters) -> dict:
        return query.search(rows, PATTERNS, **filters)

    def test_rows_that_are_not_examples_are_left_out_unless_asked_for(self):
        self.assertEqual(slugs(self.search()), ["vendor-docs", "gate", "router"])
        self.assertEqual(slugs(self.search(include_non_jev=True)), ["vendor-docs", "clone", "gate", "dry-run", "router"])
        self.assertEqual(query.DISQUALIFYING, {"not-jev", "shadow-mode-only"})
        # Each disqualifying flag on its own is enough.
        for flag in sorted(query.DISQUALIFYING):
            with self.subTest(flag=flag):
                lone = [row("only", has_code=True, flags=["vendor-reported", flag])]
                self.assertEqual(self.search(lone)["total_matching"], 0)
                self.assertEqual(slugs(self.search(lone, include_non_jev=True)), ["only"])

    def test_caveats_are_exactly_the_rows_flags(self):
        by_slug = {r["slug"]: r for r in ROWS}
        results = self.search(include_non_jev=True, limit=50)["results"]
        self.assertEqual(len(results), len(ROWS))
        for result in results:
            with self.subTest(slug=result["slug"]):
                flags = by_slug[result["slug"]].get("flags")
                if flags:
                    self.assertEqual(result["caveats"], flags)
                else:
                    self.assertNotIn("caveats", result)

    def test_limit_is_clamped_between_one_and_fifty(self):
        many = [row(f"r{i:02}", has_code=True) for i in range(60)]
        for limit, returned in ((-3, 1), (0, 1), (1, 1), ("5", 5), (50, 50), (51, 50), (1000, 50)):
            with self.subTest(limit=limit):
                result = self.search(many, limit=limit)
                self.assertEqual(result["total_matching"], 60)
                self.assertEqual(result["returned"], returned)
                self.assertEqual(len(result["results"]), returned)
        self.assertEqual(self.search(limit=50)["returned"], 3, "returned counts rows, not the limit")

    def test_an_unknown_pattern_lists_the_valid_ones(self):
        self.assertEqual(
            self.search(pattern="nope"),
            {
                "error": "unknown pattern 'nope'",
                "valid_patterns": ["human-escalation", "overview", "safety-gating", "tool-selection"],
                "hint": "call list_patterns() for what each one means",
            },
        )

    def test_filters(self):
        cases = [
            ({"pattern": "safety-gating"}, ["gate"]),
            ({"pattern": "human-escalation"}, []),
            ({"kind": "official-docs"}, ["vendor-docs"]),
            ({"kind": "docs"}, []),
            ({"language": "python"}, ["router"]),
            ({"language": "py"}, []),
            ({"question_type": "choice"}, ["router"]),
            # primitives_seen is a script's text signal, never a person's reading.
            ({"question_type": "noul", "include_non_jev": True}, []),
            # A value rows record, whole; PlatformTest covers surfaces and fragments.
            ({"platform": "cloudflare-workers-ai"}, ["gate"]),
            ({"platform": " TYPESAFE-API "}, ["router"]),
            ({"official_only": True}, ["vendor-docs"]),
            ({"with_code_only": True}, ["gate", "router"]),
            ({"query": "routes COST"}, ["router"]),
            ({"query": "workers"}, ["gate"]),
            ({"query": "gate router"}, []),
            ({"query": "dry", "include_non_jev": True}, ["dry-run"]),
        ]
        for filters, expected in cases:
            with self.subTest(**filters):
                self.assertEqual(slugs(self.search(**filters)), expected)

    def test_a_query_reads_the_title_summary_notes_slug_and_platforms(self):
        rows = [
            row("a1", title="Alpha", summary="beta", notes="gamma", platforms=["delta-cloud"]),
            row("zz-epsilon", title="Other", summary="other"),
        ]
        for words, expected in (("alpha", ["a1"]), ("BETA", ["a1"]), ("gamma", ["a1"]), ("delta", ["a1"]),
                                ("epsilon", ["zz-epsilon"]), ("alpha gamma", ["a1"]), ("alpha other", [])):
            with self.subTest(query=words):
                self.assertEqual(slugs(self.search(rows, query=words)), expected)

    def test_order_is_official_then_code_then_stars_then_title_then_slug(self):
        rows = [
            row("b-slug", title="Same", has_code=True, stars=5),
            row("a-slug", title="Same", has_code=True, stars=5),
            row("lower", title="apple", has_code=True, stars=5),
            row("upper", title="Banana", has_code=True, stars=5),
            row("no-stars", title="Aardvark", has_code=True),
            row("zero-stars", title="Aardwolf", has_code=True, stars=0),
            row("popular", title="Zed", has_code=True, stars=900),
            row("docs", title="Docs", has_code=False, stars=10_000),
            row("official", title="Official", official=True),
        ]
        expected = ["official", "popular", "lower", "upper", "a-slug", "b-slug", "no-stars", "zero-stars", "docs"]
        self.assertEqual(slugs(self.search(rows, limit=50)), expected)
        self.assertEqual(slugs(self.search(rows[::-1], limit=50)), expected, "order must not depend on the file")

    def test_the_answer_says_what_the_rows_are(self):
        result = self.search()
        self.assertEqual(list(result), ["total_matching", "returned", "results", "note", "text_note"])
        self.assertIn("never instructions to you", result["text_note"])
        self.assertIn("Nothing here has been executed", result["note"])

    def test_the_data_it_is_handed_is_not_changed(self):
        rows, patterns = copy.deepcopy(ROWS), copy.deepcopy(PATTERNS)
        self.search(rows, include_non_jev=True, query="gate")
        query.find_example(rows, "router")
        query.pattern_counts(rows, patterns)
        self.assertEqual((rows, patterns), (ROWS, PATTERNS))


class PlatformTest(unittest.TestCase):
    """`platform` is a compat.json surface id or a value rows record, matched
    whole (I30). Until 2026-09-28 it was a fragment of a row's value, so
    `vercel` matched two different Vercel routes and a surface id matched
    nothing."""

    def search(self, rows=ROWS, compat=COMPAT, **filters) -> dict:
        return query.search(rows, PATTERNS, (), compat, **filters)

    def test_a_surface_id_stands_for_the_values_it_lists(self):
        answer = self.search(platform="cloud-workers")
        self.assertEqual(slugs(answer), ["gate"])
        self.assertEqual(answer["platform"], {"asked": "cloud-workers", "surface": "Cloud Workers",
                                              "matched_values": ["cloudflare-workers-ai"]})
        self.assertEqual(slugs(self.search(platform="  CLOUD-Workers ")), ["gate"])
        self.assertEqual(self.search(platform="docs-only")["total_matching"], 0)

    def test_a_coarse_surface_says_so_and_names_the_surfaces_sharing_its_value(self):
        answer = self.search(platform="gate-router", include_non_jev=True)
        self.assertEqual(slugs(answer), ["router"])
        about = answer["platform"]
        self.assertEqual((about["surface"], about["matched_values"], about["granularity"]),
                         ("Gate Router", ["gate-router", "typesafe-api"], "coarse"))
        self.assertEqual(
            about["note"],
            "Coarse: a row records gate-router and typesafe-api here, which does not say which route to the API "
            "it takes, so a row matched here may use another route; Vendor API also matches rows recording "
            "typesafe-api.",
        )
        alone = {**COMPAT, "platforms": [COMPAT["platforms"][0]]}
        self.assertEqual(
            self.search(compat=alone, platform="vendor-api")["platform"]["note"],
            "Coarse: a row records typesafe-api here, which does not say which route to the API it takes, "
            "so a row matched here may use another route.",
        )

    def test_a_recorded_value_names_the_surfaces_listing_it(self):
        about = self.search(platform="typesafe-api")["platform"]
        self.assertEqual(about["matched_values"], ["typesafe-api"])
        self.assertEqual(about["surfaces"], ["vendor-api", "gate-router"])
        self.assertEqual(about["granularity"], "coarse")
        self.assertIn("compat.json lists typesafe-api for Vendor API and Gate Router", about["note"])
        exact = self.search(platform="cloudflare-workers-ai")["platform"]
        self.assertEqual(exact, {"asked": "cloudflare-workers-ai", "matched_values": ["cloudflare-workers-ai"],
                                 "surfaces": ["cloud-workers"]})
        self.assertEqual(self.search(platform="gate-router")["platform"]["surface"], "Gate Router",
                         "an id that is also a value means the surface")

    def test_a_fragment_is_refused_with_what_would_match(self):
        for asked in ("cloud", "TYPESAFE", "workers-ai", "Cloud Workers"):
            with self.subTest(platform=asked):
                self.assertEqual(
                    self.search(platform=asked),
                    {
                        "error": f"unknown platform {asked!r}",
                        "surfaces": ["vendor-api", "gate-router", "cloud-workers", "docs-only"],
                        "recorded_values": ["cloudflare-workers-ai", "typesafe-api"],
                        "hint": "a surface id from compatibility(), or a value rows record in `platforms`, "
                        "matched whole",
                    },
                )

    def test_a_value_is_known_whatever_the_other_filters_keep(self):
        answer = self.search(platform="cloudflare-workers-ai", language="python")
        self.assertEqual((answer["total_matching"], answer["platform"]["matched_values"]),
                         (0, ["cloudflare-workers-ai"]))
        # A value a surface lists is known before any row records it.
        listed = {**COMPAT, "platforms": [*COMPAT["platforms"],
                                          {"id": "edge", "name": "Edge", "catalog_platforms": ["edge-fn"]}]}
        answer = self.search(compat=listed, platform="edge-fn")
        self.assertEqual((answer["total_matching"], answer["platform"]),
                         (0, {"asked": "edge-fn", "matched_values": ["edge-fn"], "surfaces": ["edge"]}))
        self.assertIn("error", self.search(platform="edge-fn"))

    def test_a_row_recording_two_of_a_surfaces_values_is_matched_once(self):
        rows = [row("both", has_code=True, platforms=["typesafe-api", "gate-router"])]
        self.assertEqual(slugs(self.search(rows, platform="gate-router")), ["both"])
        self.assertEqual(query.platform_rows(rows * 1, ["typesafe-api", "gate-router"]), rows)

    def test_without_compat_json_a_recorded_value_still_matches(self):
        self.assertEqual(slugs(query.search(ROWS, PATTERNS, platform="typesafe-api")), ["router"])
        self.assertIn("error", query.search(ROWS, PATTERNS, platform="cloud-workers"))

    def test_the_answer_puts_platform_after_the_note_and_before_the_glossary(self):
        flags = [{"key": "vendor-reported", "blurb_en": "v"}, {"key": "single-commit", "blurb_en": "s"}]
        answer = query.search(ROWS, PATTERNS, flags, COMPAT, platform="typesafe-api")
        self.assertEqual(
            list(answer), ["total_matching", "returned", "results", "note", "text_note", "platform", "caveat_glossary"]
        )
        self.assertNotIn("platform", self.search())

    def test_the_real_compat_json_resolves_every_surface_and_refuses_a_fragment(self):
        compat = json.loads((ROOT / "compat.json").read_text())
        rows = json.loads((ROOT / "catalog.json").read_text())
        for platform in compat["platforms"]:
            with self.subTest(surface=platform["id"]):
                answer = query.search(rows, PATTERNS, (), compat, platform=platform["id"], include_non_jev=True)
                self.assertNotIn("error", answer)
                self.assertEqual(answer["total_matching"],
                                 len(query.platform_rows(rows, platform["catalog_platforms"])))
                self.assertEqual("granularity" in answer["platform"], platform.get("granularity") == "coarse")
        refused = query.search(rows, PATTERNS, (), compat, platform="vercel")
        self.assertIn("vercel-ai-gateway", refused["recorded_values"])
        self.assertIn("vercel-compat", refused["surfaces"])


class CompactTest(unittest.TestCase):
    def test_a_full_row_keeps_its_fields_in_order(self):
        entry = row(
            "full", has_code=True, summary_source="curated", patterns_reviewed="2026-09-27",
            question_types=["choice"], languages=["python"], platforms=["typesafe-api"], stars=0,
            repo_license="MIT", repo_created_at="2026-01-01T00:00:00Z", repo_pushed_at="2026-02-01T00:00:00Z",
            repo_commits=3, official=True, flags=["vendor-reported"], notes="n",
            evidence={"path": "x.py", "matched": ["noul"]}, primitives_seen=["noul"], sources=[{"catalog": "a/b"}],
        )
        compact = query.compact(entry)
        self.assertEqual(
            list(compact),
            ["slug", "title", "url", "summary", "kind", "patterns", "summary_source", "patterns_reviewed",
             "question_types", "languages", "platforms", "stars", "repo_license", "repo_created_at",
             "repo_pushed_at", "repo_commits", "official", "caveats", "note"],
        )
        self.assertEqual(compact["stars"], 0, "a zero is a count, not an absence")
        self.assertEqual(compact["caveats"], ["vendor-reported"])
        self.assertEqual(compact["note"], "n")

    def test_a_bare_row_gets_only_the_core_fields(self):
        entry = row("bare", official=False, flags=[], notes="", stars=None, has_code=True)
        self.assertEqual(list(query.compact(entry)), ["slug", "title", "url", "summary", "kind", "patterns"])


class FindExampleTest(unittest.TestCase):
    def test_a_known_slug_returns_the_whole_row(self):
        self.assertEqual(query.find_example(ROWS, "router"), {**ROWS[0], "text_note": query.TEXT_NOTE})

    def test_an_unknown_slug_suggests_up_to_five_sorted_slugs(self):
        many = [row(f"r{i:02}") for i in range(60)][::-1]
        answer = query.find_example(many, "R0")
        self.assertEqual(answer["did_you_mean"], ["r00", "r01", "r02", "r03", "r04"])
        self.assertEqual(answer["error"], "no entry with slug 'R0'")
        self.assertEqual(query.find_example(ROWS, "e")["did_you_mean"], ["clone", "gate", "router", "vendor-docs"])
        self.assertIsNone(query.find_example(ROWS, "zzz")["did_you_mean"])
        self.assertEqual(query.find_example(ROWS, "zzz")["hint"], "use search_examples() to find a slug")


class PatternCountsTest(unittest.TestCase):
    def test_every_pattern_in_taxonomy_order_with_its_count(self):
        rows = ROWS + [row("stray", patterns=["not-in-the-taxonomy"])]
        answer = query.pattern_counts(rows, PATTERNS)
        self.assertEqual(
            [(p["key"], p["name"], p["examples"]) for p in answer["patterns"]],
            [("tool-selection", "Tool selection", 4), ("safety-gating", "Safety gating", 1),
             ("human-escalation", "Human escalation", 0), ("overview", "Overview", 1)],
        )
        self.assertEqual(answer["patterns"][0]["description"], "Which tool to call next.")
        self.assertIn("never a security boundary", answer["note"])


class CompatLookupTest(unittest.TestCase):
    def test_every_surface_by_default(self):
        answer = query.compat_lookup(COMPAT)
        self.assertEqual(list(answer), ["as_of", "surfaces", "limits", "warning"])
        self.assertEqual(answer["surfaces"], COMPAT["platforms"])
        self.assertEqual((answer["as_of"], answer["limits"]), ("2031-01-01", COMPAT["limits"]))
        self.assertIn("`noul`", answer["warning"])

    def test_a_fragment_matches_names_ignoring_case(self):
        self.assertEqual([p["name"] for p in query.compat_lookup(COMPAT, "cloud")["surfaces"]], ["Cloud Workers"])
        self.assertEqual([p["name"] for p in query.compat_lookup(COMPAT, "ROUTER")["surfaces"]], ["Gate Router"])

    def test_no_match_names_every_surface(self):
        self.assertEqual(
            query.compat_lookup(COMPAT, "zzz"),
            {"error": "no surface matching 'zzz'", "known_surfaces": [p["name"] for p in COMPAT["platforms"]]},
        )

    def test_an_id_matches_whole(self):
        self.assertEqual([p["name"] for p in query.compat_lookup(COMPAT, " Gate-Router ")["surfaces"]], ["Gate Router"])
        self.assertIn("error", query.compat_lookup(COMPAT, "gate-rou"))

    def test_handed_the_rows_each_surface_counts_its_catalogued_examples(self):
        rows = ROWS + [row("both", platforms=["typesafe-api", "gate-router"])]
        answer = query.compat_lookup(COMPAT, "", rows)
        self.assertEqual(list(answer), ["as_of", "surfaces", "limits", "warning", "catalogued_examples_note"])
        examples = {p["id"]: p["catalogued_examples"] for p in answer["surfaces"]}
        self.assertEqual({k: v["rows"] for k, v in examples.items()},
                         {"vendor-api": 2, "gate-router": 2, "cloud-workers": 1, "docs-only": 0})
        self.assertEqual(examples["cloud-workers"], {"rows": 1, "search": {"platform": "cloud-workers"}})
        self.assertEqual(examples["vendor-api"]["note"], query.coarse_note(COMPAT, COMPAT["platforms"][0]))
        # Every other field is compat.json's, untouched.
        self.assertEqual([{k: v for k, v in p.items() if k != "catalogued_examples"} for p in answer["surfaces"]],
                         COMPAT["platforms"])
        self.assertIn("caveated rows included", answer["catalogued_examples_note"])
        # The count is what search_examples(platform=<id>) finds, not_examples included.
        for platform in COMPAT["platforms"]:
            with self.subTest(surface=platform["id"]):
                found = query.search(rows, PATTERNS, (), COMPAT, platform=platform["id"], include_non_jev=True)
                self.assertEqual(found["total_matching"], examples[platform["id"]]["rows"])


class ModelStringTest(unittest.TestCase):
    EVERY = ["@cf/acme/jev-9.1", "acme-latest", "acme/jev-9.1", "jev-9.1.0", "~acme/jev"]

    def test_a_listed_string_names_its_surfaces(self):
        answer = query.model_string_check(COMPAT, "  acme/jev-9.1  ")
        self.assertEqual(
            answer,
            {"model": "acme/jev-9.1", "valid": True, "surfaces": [
                {"surface": "Gate Router", "accepts": ["acme/jev-9.1", "~acme/jev"],
                 "endpoint": "POST /gate/v1", "env": "GATE_KEY"}]},
        )

    def test_a_remark_in_the_cell_is_not_part_of_the_string(self):
        self.assertEqual(query.accepted(COMPAT["platforms"][0]), ["acme-latest", "jev-9.1.0"])
        self.assertEqual(query.accepted(COMPAT["platforms"][3]), [])
        self.assertEqual(query.accepted({"model": "a ·  · b"}), ["a", "b"])
        self.assertIs(query.model_string_check(COMPAT, "acme-latest")["valid"], True)
        self.assertIs(query.model_string_check(COMPAT, "acme-latest (default)")["valid"], False)

    def test_a_prefix_of_a_real_string_is_not_valid_but_is_named(self):
        for needle, near in (("acme/jev-9", ["acme/jev-9.1"]), ("acme/jev-9.1.0", ["acme/jev-9.1"]),
                             ("x", None), ("", None)):
            with self.subTest(needle=needle):
                answer = query.model_string_check(COMPAT, needle)
                self.assertIs(answer["valid"], False)
                self.assertEqual(answer["close_but_wrong"], near)
                self.assertEqual(answer["valid_strings"], self.EVERY)
                # A string compat.json refutes gives its own reason (I30).
                reason = "Nobody documents it." if needle == "acme/jev-9" else (
                    "matches no model string on any documented surface")
                self.assertEqual(answer["reason"], reason)

    def test_the_hint_is_built_from_compat_json_alone(self):
        self.assertEqual(
            query.model_hint(COMPAT),
            "The versioned id is jev-9.1.0, with aliases acme-latest. Gateways and SDKs rename it: "
            "acme/jev-9.1 or ~acme/jev on Gate Router; @cf/acme/jev-9.1 on Cloud Workers. "
            "`acme/jev-9`: Nobody documents it. Pin a version rather than an alias once you have tuned any threshold.",
        )
        self.assertEqual(query.model_string_check(COMPAT, "nope")["hint"], query.model_hint(COMPAT))
        bare = {"platforms": [{"name": "Only", "model": "one · two", "endpoint": "e", "env": "k"}]}
        self.assertEqual(
            query.model_hint(bare),
            "Gateways and SDKs rename it: one or two on Only. "
            "Pin a version rather than an alias once you have tuned any threshold.",
        )
        # Surfaces taking the same strings are named together, in compat.json's
        # order; an alias with a digit in it is still an alias.
        shared = {"platforms": [
            {"name": "Own", "official": True, "model": "acme2-latest · jev-9.1 (pinned)", "endpoint": "e", "env": "k"},
            {"name": "Beta", "model": "x · y", "endpoint": "e", "env": "k"},
            {"name": "Alpha", "model": "x ·  · y", "endpoint": "e", "env": "k"},
            {"name": "Gamma", "model": "z · jev-9.1", "endpoint": "e", "env": "k"},
        ]}
        self.assertEqual(
            query.model_hint(shared),
            "The versioned id is jev-9.1, with aliases acme2-latest. "
            "Gateways and SDKs rename it: x or y on Beta and Alpha; z on Gamma. "
            "Pin a version rather than an alias once you have tuned any threshold.",
        )

    def test_the_fabrication_is_refused_against_the_real_compat_json(self):
        compat = json.loads((ROOT / "compat.json").read_text())
        every = sorted({m for p in compat["platforms"] for m in query.accepted(p)})
        fabricated = "typesafe/jev-1"
        answer = query.model_string_check(compat, fabricated)
        self.assertIs(answer["valid"], False)
        near = [m for m in every if m.startswith(fabricated) or fabricated.startswith(m)]
        self.assertTrue(near, "the real strings no longer start with the fabrication; the prefix trap is untested")
        self.assertEqual(answer["close_but_wrong"], near)
        for model in every:
            with self.subTest(model=model):
                self.assertIs(query.model_string_check(compat, model)["valid"], True)


class StandaloneTest(unittest.TestCase):
    def test_query_imports_only_the_standard_library(self):
        tree = ast.parse((PACKAGE / "query.py").read_text())
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported |= {alias.name.split(".")[0] for alias in node.names}
            elif isinstance(node, ast.ImportFrom):
                self.assertEqual(node.level, 0, "query.py must not import the package's data or server modules")
                imported.add(node.module.split(".")[0])
        self.assertEqual(imported - set(sys.stdlib_module_names), set())

    def test_query_holds_no_catalogue_of_its_own(self):
        for name in ("CATALOG", "COMPAT", "PATTERNS", "PROVENANCE"):
            self.assertFalse(hasattr(query, name), name)

    def test_importing_it_needs_no_mcp_and_reaches_no_network(self):
        code = (
            "import sys, urllib.request\n"
            "urllib.request.urlopen = None\n"
            "import awesome_jev_mcp.query\n"
            "assert 'mcp' not in sys.modules and 'awesome_jev_mcp.server' not in sys.modules\n"
        )
        done = subprocess.run([sys.executable, "-c", code], cwd=ROOT / "src", capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)


class ServerWiringTest(unittest.TestCase):
    """server.py registers the tools and adds the `data` line; the answers are
    query.py's, on the data the server loaded."""

    @classmethod
    def setUpClass(cls):
        cls.server = load_server()
        cls.line = cls.server.PROVENANCE.line()

    def stamped(self, answer: dict) -> dict:
        return {**answer, "data": self.line}

    def test_search_examples_passes_every_argument_through(self):
        params = inspect.signature(self.server.search_examples).parameters
        wanted = {name: p.default for name, p in inspect.signature(query.search).parameters.items()
                  if p.kind is p.KEYWORD_ONLY}
        self.assertEqual({name: p.default for name, p in params.items()}, wanted)
        # A value per argument that changes the answer on the real catalogue.
        changed = {"pattern": "safety-gating", "kind": "project", "language": "python", "question_type": "choice",
                   "platform": "langchain", "comparator": "Cohere", "dataset": "LongMemEval",
                   "direction": "unfavourable", "outcome": "negative", "query": "router", "official_only": True, "with_code_only": True,
                   "include_non_jev": True, "limit": 3}
        s = self.server
        default = query.search(s.CATALOG, s.PATTERNS, s.FLAGS, s.COMPAT)
        for name, value in changed.items():
            with self.subTest(argument=name):
                expected = query.search(s.CATALOG, s.PATTERNS, s.FLAGS, s.COMPAT, **{name: value})
                self.assertNotEqual(expected, default, "this value does not exercise the argument")
                self.assertEqual(self.server.search_examples(**{name: value}), self.stamped(expected))

    def test_the_other_tools_answer_with_query_on_the_loaded_data(self):
        s = self.server
        slug = s.CATALOG[0]["slug"]
        # Padded or upper-cased arguments too, so a server that tidied them
        # before handing them over would answer differently from query.py.
        for asked in (slug, "zzz-none", f" {slug.upper()} "):
            with self.subTest(slug=asked):
                self.assertEqual(s.get_example(asked), self.stamped(query.find_example(s.CATALOG, asked, s.FLAGS)))
        self.assertEqual(s.list_patterns(), self.stamped(query.pattern_counts(s.CATALOG, s.PATTERNS)))
        for surface in ("", "cloudflare", "zzz", " Cloudflare ", "vercel-compat"):
            with self.subTest(surface=surface):
                self.assertEqual(s.compatibility(surface),
                                 self.stamped(query.compat_lookup(s.COMPAT, surface, s.CATALOG)))
        for model in ("typesafe/jev-1", "jev-latest", "", "  JEV-Latest  "):
            with self.subTest(model=model):
                self.assertEqual(s.check_model_string(model), self.stamped(query.model_string_check(s.COMPAT, model)))

    def test_every_tool_keeps_its_description(self):
        for name in ("search_examples", "get_example", "list_patterns", "compatibility", "check_model_string"):
            with self.subTest(tool=name):
                self.assertGreater(len(inspect.getdoc(getattr(self.server, name)) or ""), 80)


class PublishSmokeTest(unittest.TestCase):
    """CI never installs `mcp`, so only publish's smoke step sees the real SDK
    register the tools; its list must be every tool server.py defines."""

    def test_the_smoke_step_expects_every_registered_tool(self):
        tree = ast.parse((PACKAGE / "server.py").read_text())
        tools = sorted(
            node.name for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and any(isinstance(d, ast.Name) and d.id == "tool" for d in node.decorator_list)
        )
        self.assertIn("search_examples", tools)
        workflow = (ROOT / ".github" / "workflows" / "publish.yml").read_text()
        self.assertIn(f"assert tools == {json.dumps(tools)}, tools", workflow)
        self.assertIn("asyncio.run(server.mcp.list_tools())", workflow)


if __name__ == "__main__":
    unittest.main()
