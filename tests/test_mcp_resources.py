"""The MCP server's resources and caveat glossary (I35), on made-up rows.

query.py answers `awesome-jev://flags`, `awesome-jev://collections`,
`awesome-jev://collections/{id}` and `awesome-jev://patterns/{key}`, and adds
`caveat_glossary` to search_examples and get_example; server.py registers them.
CI never installs `mcp`, so the registrations are read through the stubbed
loader of test_mcp_caveats.py, which records what server.py asked the SDK to
register. Only publish.yml's smoke step asks the real SDK, and
PublishSmokeTest keeps its lists equal to server.py's.
"""

from __future__ import annotations

import ast
import copy
import inspect
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "src" / "awesome_jev_mcp"
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "src"))

from awesome_jev_mcp import query  # noqa: E402
from test_mcp_caveats import load_server  # noqa: E402
from test_mcp_query import PATTERNS, ROWS, row, slugs  # noqa: E402

# A made-up taxonomy.json `flags`, deliberately not in the order the rows use them.
FLAGS = [
    {"key": "not-jev", "en": "not Jev itself", "zh": "并非 Jev 本身", "blurb_en": "Never calls it.",
     "blurb_zh": "从不调用。"},
    {"key": "shadow-mode-only", "en": "shadow mode", "zh": "影子模式", "blurb_en": "Wired in, inert.",
     "blurb_zh": "接入但不生效。"},
    {"key": "single-commit", "en": "one commit", "zh": "单次提交", "blurb_en": "One commit.",
     "blurb_zh": "只有一次提交。", "zh_machine": True},
    {"key": "vendor-reported", "en": "vendor-reported", "zh": "厂商自报", "blurb_en": "The vendor's numbers.",
     "blurb_zh": "厂商自己的数字。"},
    {"key": "archived", "en": "archived", "zh": "已归档", "blurb_en": "Stopped.", "blurb_zh": "已停止。"},
]
TAXONOMY = {"kinds": [], "flags": FLAGS, "summary_sources": []}

COLLECTIONS = [
    {"id": "first-call", "title": "First call", "title_zh": "第一次调用", "description": "Start here.",
     "description_zh": "从这里开始。", "entries": [
         {"slug": "router", "reason": "Routes.", "reason_zh": "路由。", "caution": "Untested.", "caution_zh": "未测。"},
         {"slug": "vendor-docs", "reason": "Docs.", "reason_zh": "文档。", "caution": "Vendor.", "caution_zh": "厂商。"},
     ]},
    {"id": "measured", "title": "Measured", "title_zh": "测量", "description": "Numbers.",
     "description_zh": "数字。", "entries": [
         {"slug": "dry-run", "reason": "Inert.", "reason_zh": "不生效。", "caution": "Shadow.", "caution_zh": "影子。"},
         {"slug": "gone", "reason": "Left.", "reason_zh": "已删。", "caution": "Gone.", "caution_zh": "没了。"},
     ]},
]

RESOURCES = ["awesome-jev://collections", "awesome-jev://flags"]
TEMPLATES = ["awesome-jev://collections/{id}", "awesome-jev://patterns/{key}"]


class GlossaryTest(unittest.TestCase):
    def test_search_explains_the_flags_of_the_rows_it_returns_in_taxonomy_order(self):
        answer = query.search(ROWS, PATTERNS, FLAGS)
        self.assertEqual(slugs(answer), ["vendor-docs", "gate", "router"])
        self.assertEqual(list(answer), ["total_matching", "returned", "results", "note", "text_note", "caveat_glossary"])
        # router carries ["vendor-reported", "single-commit"]; the glossary follows taxonomy.json.
        self.assertEqual(answer["caveat_glossary"], {"single-commit": "One commit.",
                                                     "vendor-reported": "The vendor's numbers."})
        wide = query.search(ROWS, PATTERNS, FLAGS, include_non_jev=True)
        self.assertEqual(list(wide["caveat_glossary"]),
                         ["not-jev", "shadow-mode-only", "single-commit", "vendor-reported"])

    def test_the_order_is_the_taxonomys_not_the_alphabets_or_the_rows(self):
        rows = [row("late", has_code=True, flags=["archived", "vendor-reported"]),
                row("early", has_code=True, flags=["not-jev"])]
        answer = query.search(rows, PATTERNS, FLAGS, include_non_jev=True)
        self.assertEqual(list(answer["caveat_glossary"]), ["not-jev", "vendor-reported", "archived"])

    def test_rows_keep_their_bare_keys(self):
        router = next(r for r in query.search(ROWS, PATTERNS, FLAGS)["results"] if r["slug"] == "router")
        self.assertEqual(router["caveats"], ["vendor-reported", "single-commit"])

    def test_only_the_rows_returned_count(self):
        answer = query.search(ROWS, PATTERNS, FLAGS, limit=1)
        self.assertEqual(slugs(answer), ["vendor-docs"])
        self.assertNotIn("caveat_glossary", answer, "no flag in the answer, so no glossary")
        self.assertEqual(query.search(ROWS, PATTERNS, FLAGS, limit=2)["returned"], 2)

    def test_without_the_taxonomy_there_is_no_glossary(self):
        self.assertNotIn("caveat_glossary", query.search(ROWS, PATTERNS))
        self.assertEqual(query.find_example(ROWS, "router"), {**ROWS[0], "text_note": query.TEXT_NOTE})

    def test_get_example_adds_the_glossary_after_the_rows_own_fields(self):
        answer = query.find_example(ROWS, "router", FLAGS)
        self.assertEqual(list(answer), [*ROWS[0], "text_note", "caveat_glossary"])
        self.assertEqual(answer["flags"], ["vendor-reported", "single-commit"])
        self.assertEqual(list(answer["caveat_glossary"]), ["single-commit", "vendor-reported"])
        self.assertEqual(query.find_example(ROWS, "gate", FLAGS), {**ROWS[1], "text_note": query.TEXT_NOTE},
                         "a row without flags gains no glossary")
        self.assertNotIn("caveat_glossary", query.find_example(ROWS, "zzz", FLAGS))

    def test_a_flag_the_taxonomy_lacks_still_travels_as_a_key(self):
        odd = [row("odd", has_code=True, flags=["made-up", "archived"])]
        answer = query.search(odd, PATTERNS, FLAGS)
        self.assertEqual(answer["results"][0]["caveats"], ["made-up", "archived"])
        self.assertEqual(answer["caveat_glossary"], {"archived": "Stopped."})


class FlagsResourceTest(unittest.TestCase):
    def test_the_taxonomy_flags_as_written_with_the_two_that_disqualify(self):
        answer = query.flag_list(TAXONOMY)
        self.assertEqual(list(answer), ["flags", "not_examples", "note"])
        self.assertEqual(answer["flags"], FLAGS, "labels, descriptions and zh_machine pass through untouched")
        self.assertEqual(answer["not_examples"], ["not-jev", "shadow-mode-only"])
        self.assertIn("caveat_glossary", answer["note"])
        self.assertIn("zh_machine", answer["note"])


class CollectionsResourceTest(unittest.TestCase):
    def test_the_list_counts_each_path_and_names_its_resource(self):
        answer = query.collection_list(COLLECTIONS)
        first = answer["collections"][0]
        self.assertEqual(list(first), ["id", "title", "title_zh", "description", "description_zh", "entries", "uri"])
        self.assertEqual([(c["id"], c["entries"], c["uri"]) for c in answer["collections"]],
                         [("first-call", 2, "awesome-jev://collections/first-call"),
                          ("measured", 2, "awesome-jev://collections/measured")])
        self.assertIn("not a runtime certification", answer["note"])
        self.assertIn("not reproduced here", answer["note"], "a measured pick was run by its author, not by us")

    def test_one_path_in_its_own_order_with_each_row(self):
        answer = query.collection_detail(COLLECTIONS, ROWS, FLAGS, "first-call")
        self.assertEqual([e["slug"] for e in answer["entries"]], ["router", "vendor-docs"])
        router = answer["entries"][0]
        self.assertEqual(list(router), ["slug", "reason", "reason_zh", "caution", "caution_zh", "row"])
        self.assertEqual(router["row"], query.compact(ROWS[0]))
        self.assertEqual(answer["title_zh"], "第一次调用")
        self.assertEqual(list(answer)[-3:], ["note", "text_note", "caveat_glossary"])
        self.assertEqual(list(answer["caveat_glossary"]), ["single-commit", "vendor-reported"])

    def test_a_pick_is_kept_whatever_its_caveats_and_a_missing_row_is_said(self):
        answer = query.collection_detail(COLLECTIONS, ROWS, FLAGS, "measured")
        self.assertEqual(answer["entries"][0]["row"]["caveats"], ["shadow-mode-only"])
        self.assertIsNone(answer["entries"][1]["row"])
        self.assertEqual(answer["caveat_glossary"], {"shadow-mode-only": "Wired in, inert."})

    def test_an_unknown_path_lists_the_known_ones(self):
        self.assertEqual(
            query.collection_detail(COLLECTIONS, ROWS, FLAGS, "nope"),
            {"error": "no collection 'nope'", "valid_collections": ["first-call", "measured"],
             "hint": "read awesome-jev://collections"},
        )


class PatternResourceTest(unittest.TestCase):
    def test_every_row_under_the_pattern_caveats_and_all(self):
        answer = query.pattern_listing(ROWS, PATTERNS, FLAGS, "tool-selection")
        self.assertEqual(
            list(answer),
            ["pattern", "name", "description", "when_not_to_use", "examples", "not_examples", "note", "text_note",
             "entries", "caveat_glossary"],
        )
        self.assertEqual([e["slug"] for e in answer["entries"]], ["clone", "gate", "dry-run", "router"])
        self.assertEqual(answer["entries"], query.pattern_rows(ROWS, "tool-selection"))
        self.assertEqual(answer["examples"], 4)
        self.assertEqual(answer["not_examples"], ["not-jev", "shadow-mode-only"])
        self.assertEqual((answer["name"], answer["description"]), ("Tool selection", "Which tool to call next."))
        self.assertEqual(list(answer["caveat_glossary"]),
                         ["not-jev", "shadow-mode-only", "single-commit", "vendor-reported"])

    def test_it_links_the_patterns_when_not_to_use(self):
        answer = query.pattern_listing(ROWS, PATTERNS, FLAGS, "safety-gating")
        self.assertEqual(answer["when_not_to_use"],
                         "https://github.com/kydlikebtc/awesome-jev/blob/main/docs/patterns.md#safety-gating")
        # docs/patterns.md has a `## <key>` heading for every pattern (lint_docs), so the anchor exists.
        heads = re.findall(r"^## ([a-z-]+)\s*$", (ROOT / "docs" / "patterns.md").read_text(), re.M)
        for p in json.loads((ROOT / "patterns.json").read_text())["patterns"]:
            self.assertIn(p["key"], heads)

    def test_an_empty_pattern_has_no_rows_and_no_glossary(self):
        answer = query.pattern_listing(ROWS, PATTERNS, FLAGS, "human-escalation")
        self.assertEqual((answer["examples"], answer["entries"]), (0, []))
        self.assertNotIn("caveat_glossary", answer)

    def test_an_unknown_key_lists_the_valid_ones(self):
        answer = query.pattern_listing(ROWS, PATTERNS, FLAGS, "nope")
        self.assertEqual(answer["valid_patterns"], ["human-escalation", "overview", "safety-gating", "tool-selection"])
        self.assertEqual(answer["error"], "unknown pattern 'nope'")

    def test_the_rows_are_the_sites_api_rows(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import site_api  # noqa: PLC0415

        for key in ("tool-selection", "overview", "human-escalation"):
            self.assertEqual(site_api.pattern_rows(ROWS, key), query.pattern_rows(ROWS, key))
        self.assertEqual(query.pattern_rows(ROWS[::-1], "tool-selection"), query.pattern_rows(ROWS, "tool-selection"))

    def test_the_data_it_is_handed_is_not_changed(self):
        rows, flags, collections = copy.deepcopy(ROWS), copy.deepcopy(FLAGS), copy.deepcopy(COLLECTIONS)
        query.pattern_listing(rows, PATTERNS, flags, "tool-selection")
        query.collection_detail(collections, rows, flags, "first-call")
        query.collection_list(collections)
        query.find_example(rows, "router", flags)
        query.search(rows, PATTERNS, flags, include_non_jev=True)
        self.assertEqual((rows, flags, collections), (ROWS, FLAGS, COLLECTIONS))


class RegistrationTest(unittest.TestCase):
    """What server.py asks the SDK to register, through the stub that records it."""

    @classmethod
    def setUpClass(cls):
        cls.server = load_server()
        cls.line = cls.server.PROVENANCE.line()

    def test_the_four_resources_are_registered_as_json(self):
        registered = self.server.mcp.resources
        self.assertEqual(sorted(registered), sorted(RESOURCES + TEMPLATES))
        for uri, entry in registered.items():
            with self.subTest(uri=uri):
                self.assertEqual(entry["mime_type"], "application/json")
                self.assertGreater(len(inspect.getdoc(entry["fn"]) or ""), 80)

    def test_each_templates_variables_are_its_functions_parameters(self):
        # The real SDK refuses a mismatch at import; this is the same check without it.
        for uri, entry in self.server.mcp.resources.items():
            with self.subTest(uri=uri):
                self.assertEqual(set(re.findall(r"{(\w+)}", uri)), set(inspect.signature(entry["fn"]).parameters))

    def test_the_tools_are_still_the_five(self):
        self.assertEqual(sorted(self.server.mcp.tools),
                         ["check_model_string", "compatibility", "get_example", "list_patterns", "search_examples"])

    def read(self, uri: str, **params) -> dict:
        text = self.server.mcp.resources[uri]["fn"](**params)
        self.assertIsInstance(text, str)
        answer = json.loads(text)
        # Compact separators, as on the site's api/v1 files: an agent pays for every byte.
        self.assertEqual(text, json.dumps(answer, ensure_ascii=False, separators=(",", ":")))
        return answer

    def test_each_resource_answers_with_query_on_the_loaded_data_and_the_data_line(self):
        s = self.server
        self.assertEqual(self.read("awesome-jev://flags"), {**query.flag_list(s.TAXONOMY), "data": self.line})
        self.assertEqual(self.read("awesome-jev://collections"),
                         {**query.collection_list(s.COLLECTIONS), "data": self.line})
        for cid in ("first-call", "zzz"):
            with self.subTest(collection=cid):
                self.assertEqual(self.read("awesome-jev://collections/{id}", id=cid),
                                 {**query.collection_detail(s.COLLECTIONS, s.CATALOG, s.FLAGS, cid), "data": self.line})
        for key in ("safety-gating", "zzz"):
            with self.subTest(pattern=key):
                self.assertEqual(self.read("awesome-jev://patterns/{key}", key=key),
                                 {**query.pattern_listing(s.CATALOG, s.PATTERNS, s.FLAGS, key), "data": self.line})

    def test_the_tools_carry_the_glossary_from_the_loaded_taxonomy(self):
        s = self.server
        self.assertIs(s.FLAGS, s.TAXONOMY["flags"])
        answer = s.search_examples(include_non_jev=True, limit=50)
        self.assertIn("caveat_glossary", answer)
        self.assertEqual(list(answer)[-2:], ["caveat_glossary", "data"])
        seen = {flag for r in answer["results"] for flag in r.get("caveats", [])}
        self.assertEqual(set(answer["caveat_glossary"]), seen, "every flag shown is explained, and only those")
        flagged = next(e for e in s.CATALOG if e.get("flags"))
        self.assertEqual(set(s.get_example(flagged["slug"])["caveat_glossary"]), set(flagged["flags"]))

    def test_every_real_pick_and_flag_resolves(self):
        s = self.server
        for c in s.COLLECTIONS:
            with self.subTest(collection=c["id"]):
                answer = json.loads(s.collection(c["id"]))
                self.assertNotIn(None, [e["row"] for e in answer["entries"]])
        explained = {f["key"] for f in s.FLAGS}
        self.assertEqual({flag for e in s.CATALOG for flag in e.get("flags") or []} - explained, set())


def registered_uris() -> list[str]:
    """Every `@resource("…")` URI in server.py, read from its source."""
    tree = ast.parse((PACKAGE / "server.py").read_text())
    return sorted(
        d.args[0].value
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        for d in node.decorator_list
        if isinstance(d, ast.Call) and isinstance(d.func, ast.Name) and d.func.id == "resource"
    )


class PublishSmokeTest(unittest.TestCase):
    """Only publish's smoke step sees the real SDK register the resources; its
    lists must be every one server.py defines."""

    def test_the_smoke_step_expects_every_registered_resource(self):
        uris = registered_uris()
        self.assertEqual(uris, sorted(RESOURCES + TEMPLATES))
        workflow = (ROOT / ".github" / "workflows" / "publish.yml").read_text()
        static = [u for u in uris if "{" not in u]
        templates = [u for u in uris if "{" in u]
        self.assertIn(f"assert resources == {json.dumps(static)}, resources", workflow)
        self.assertIn(f"assert templates == {json.dumps(templates)}, templates", workflow)
        self.assertIn("asyncio.run(server.mcp.list_resources())", workflow)
        self.assertIn("asyncio.run(server.mcp.list_resource_templates())", workflow)
        self.assertIn("asyncio.run(server.mcp.read_resource(", workflow)


if __name__ == "__main__":
    unittest.main()
