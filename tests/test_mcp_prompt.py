"""The MCP server's wire_pattern prompt (I35), on made-up data.

src/awesome_jev_mcp/prompts.py builds the text from the catalogue, the
patterns, compat.json, the taxonomy and examples/index.json it is handed;
server.py registers it and says where the data came from. Standard library
only, like the rest of these tests: `mcp` is stubbed (test_mcp_caveats'
loader), and the examples index is built in memory from the example files
rather than read from the committed, generated examples/index.json.
"""

from __future__ import annotations

import ast
import copy
import inspect
import json
import pathlib
import sys
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "src" / "awesome_jev_mcp"
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

import build_examples_index  # noqa: E402
from awesome_jev_mcp import data, prompts  # noqa: E402
from awesome_jev_mcp.evidence_url import evidence_url  # noqa: E402
from test_mcp_caveats import load_server  # noqa: E402
from test_mcp_query import COMPAT  # noqa: E402

PATTERNS = [
    {"key": "tool-selection", "en": "Tool selection", "blurb_en": "Which tool to call next."},
    {"key": "fan-out", "en": "Fan-out", "blurb_en": "Many questions in one request."},
    {"key": "safety-gating", "en": "Safety gating", "blurb_en": "Whether to let an action through."},
]
TAXONOMY = {
    "flags": [
        {"key": "not-jev", "blurb_en": "Never calls it."},
        {"key": "shadow-mode-only", "blurb_en": "Wired in, inert."},
        {"key": "code-untested", "blurb_en": "Read, not run."},
        {"key": "single-commit", "blurb_en": "One commit."},
        {"key": "no-license", "blurb_en": "No licence."},
    ],
    "summary_sources": [
        {"key": "curated", "en": "written for this list"},
        {"key": "upstream-description", "en": "upstream description"},
        {"key": "upstream-description-stale", "en": "earlier upstream description"},
    ],
}


def row(slug: str, *, path: str = "src/main.py", read_on: str = "", kind: str = "", **fields) -> dict:
    evidence = {"path": path, "matched": ["noul"]}
    if kind:
        evidence["kind"] = kind
    if read_on:
        evidence["read_on"] = read_on
    base = {"slug": slug, "title": slug.title(), "url": f"https://github.com/o/{slug}", "summary": f"{slug} does it.",
            "kind": "project", "patterns": ["tool-selection"], "has_code": True, "evidence": evidence}
    return {**base, **fields}


ROWS = [
    row("py-top", stars=500, languages=["python"], flags=["single-commit"], read_on="2026-09-01",
        summary_source="upstream-description"),
    row("ts-one", stars=50, languages=["typescript"], path="src/b.ts"),
    row("docs-page", official=True, kind="", url="https://docs.example.com/x", languages=["python"]),
    row("shadow", stars=9999, languages=["python"], flags=["shadow-mode-only"]),
    row("clone", stars=9000, languages=["python"], flags=["not-jev"]),
    row("wire", stars=8000, languages=["python"], kind="wire-shape"),
    row("no-evidence", stars=800, languages=["python"], evidence=None),
    row("shipped", stars=10, languages=["python"], kind="example-only", flags=["no-license"],
        summary_source="upstream-description-stale"),
    *(row(f"py-{n}", stars=100 - n, languages=["python"]) for n in range(1, 6)),
]

EXAMPLES = {
    "examples": [
        {"name": "01-many", "path": "examples/01-many/main.py", "slug": "example-many",
         "url": "https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-many/main.py",
         "patterns": ["fan-out", "tool-selection"], "languages": ["python"], "flags": ["code-untested"],
         "status": "not-run", "code": "print('many')\n"},
        {"name": "02-tools", "path": "examples/02-tools/main.py", "slug": "example-tools",
         "url": "https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-tools/main.py",
         "patterns": ["tool-selection"], "languages": ["python"], "flags": ["code-untested"],
         "status": "not-run", "code": 'DOC = """has ````four```` backticks"""\nprint("tools")\n\n'},
        {"name": "03-ts", "path": "examples/03-ts/main.ts", "slug": "example-ts",
         "url": "https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-ts/main.ts",
         "patterns": ["fan-out"], "languages": ["typescript"], "status": "not-recorded", "code": "console.log(1)\n"},
    ]
}


def text(pattern: str = "tool-selection", *, examples=EXAMPLES, **kwargs) -> str:
    return prompts.wire_pattern_text(ROWS, PATTERNS, COMPAT, TAXONOMY, examples, pattern=pattern,
                                     data="DATA", served="SERVED", **kwargs)


def section(body: str, title: str) -> str:
    return body.split(f"## {title}\n", 1)[1].split("\n## ", 1)[0].split("\n---\n", 1)[0]


class ShapeTest(unittest.TestCase):
    def test_sections_come_in_order_and_the_data_line_last(self):
        body = text(language="python", surface="cloud")
        heads = [line for line in body.splitlines() if line.startswith(("# Wiring", "## ", "---", "Data: "))]
        self.assertEqual(heads, ["# Wiring Jev for Tool selection (`tool-selection`)", "## The surface",
                                 "## Worked examples", "## Skeleton", "---", "Data: DATA"])
        self.assertIn("\nWhich tool to call next.\n", body)

    def test_it_links_the_patterns_when_not_to_use_section(self):
        self.assertIn("https://github.com/kydlikebtc/awesome-jev/blob/main/docs/patterns.md#tool-selection", text())
        # Not every section of docs/patterns.md has a "When not to" paragraph
        # (human-escalation, the triage patterns and content-scoring have a
        # note instead), so the prompt sends the agent to the section, not to a
        # paragraph it may not find.
        self.assertIn("where the section has one", text())
        self.assertIn("Read the pattern's section of docs/patterns.md first", text())

    def test_an_unknown_pattern_names_the_valid_ones_and_nothing_else(self):
        body = text("nope")
        self.assertIn("no decision pattern 'nope'. Valid keys: fan-out, safety-gating, tool-selection.", body)
        self.assertNotIn("## ", body)
        self.assertTrue(body.endswith("Data: DATA"))

    def test_arguments_are_tidied(self):
        self.assertEqual(text(" tool-selection ", language=" Python ", surface=" Cloud "),
                         text("tool-selection", language="python", surface="Cloud"))

    def test_the_data_it_is_handed_is_not_changed(self):
        rows, examples, taxonomy = copy.deepcopy(ROWS), copy.deepcopy(EXAMPLES), copy.deepcopy(TAXONOMY)
        prompts.wire_pattern_text(rows, PATTERNS, COMPAT, taxonomy, examples, pattern="tool-selection",
                                  language="python", surface="cloud")
        self.assertEqual((rows, examples, taxonomy), (ROWS, EXAMPLES, TAXONOMY))


class SurfaceTest(unittest.TestCase):
    def test_a_named_surface_gets_its_compat_fields(self):
        part = section(text(surface="cloud"), "The surface")
        self.assertIn("### Cloud Workers", part)
        self.assertIn("- model: @cf/acme/jev-9.1", part)
        self.assertIn("- endpoint: env.AI.run()", part)
        self.assertIn("- env: binding", part)
        self.assertIn("as of 2031-01-01", part)
        self.assertIn("`noul` answers carry no confidence field", part)
        self.assertNotIn("Gate Router", part)
        self.assertIn(" on Cloud Workers from the material above", text(surface="cloud"))

    def test_chinese_fields_are_left_to_compatibility(self):
        compat = {**COMPAT, "platforms": [{**COMPAT["platforms"][2], "notes": "Wrapped.", "notes_zh": "包在里面。"}]}
        body = prompts.wire_pattern_text(ROWS, PATTERNS, compat, TAXONOMY, EXAMPLES, pattern="tool-selection",
                                         surface="cloud")
        part = section(body, "The surface")
        self.assertIn("- notes: Wrapped.", part)
        self.assertNotIn("notes_zh", part)
        self.assertNotIn("包在里面", body)

    def test_which_rows_stand_for_the_surface_is_left_to_compatibility(self):
        part = section(text(surface="gate"), "The surface")
        self.assertIn("### Gate Router", part)
        self.assertIn("- id: gate-router", part)
        self.assertNotIn("catalog_platforms", part)
        self.assertNotIn("granularity", part)

    def test_a_fragment_can_name_several(self):
        part = section(text(surface="r"), "The surface")
        self.assertIn("### Vendor API", part)
        self.assertIn("### Gate Router", part)
        self.assertIn("### Cloud Workers", part)

    def test_no_surface_or_an_unknown_one_lists_them_all(self):
        for asked, opening in (("", "No surface named."), ("zzz", "No surface matches 'zzz'.")):
            with self.subTest(surface=asked):
                part = section(text(surface=asked), "The surface")
                self.assertTrue(part.strip().startswith(opening), part)
                self.assertIn("Vendor API, Gate Router, Cloud Workers, Docs only", part)
                self.assertNotIn("###", part)
        self.assertIn("Wire the `tool-selection` decision from the material above", text())


class RowsTest(unittest.TestCase):
    def test_only_linked_examples_of_calling_jev_in_catalogue_order(self):
        found, in_language = prompts.cited_rows(ROWS, "tool-selection")
        self.assertTrue(in_language)
        self.assertEqual([e["slug"] for e in found],
                         ["py-top", "py-1", "py-2", "py-3", "py-4", "py-5", "ts-one", "shipped"])

    def test_the_language_asked_for_comes_first_else_every_language_is_said(self):
        self.assertEqual([e["slug"] for e in prompts.cited_rows(ROWS, "tool-selection", "typescript")[0]], ["ts-one"])
        found, in_language = prompts.cited_rows(ROWS, "tool-selection", "rust")
        self.assertFalse(in_language)
        self.assertEqual(len(found), 8)
        part = section(text(language="rust"), "Worked examples")
        self.assertIn("No cited `tool-selection` row lists rust; these are in other languages.", part)

    def test_five_rows_at_most_with_the_count_they_come_from(self):
        part = section(text(language="python"), "Worked examples")
        self.assertIn("5 of the 7 `tool-selection` rows in python that cite", part)
        numbered = [line for line in part.splitlines() if line[:2] in {f"{n}." for n in range(1, 10)}]
        self.assertEqual(len(numbered), 5)
        self.assertNotIn("py-5", part)
        self.assertIn("Nothing here has been executed", part)

    def test_each_row_links_its_cited_file_as_the_site_does_and_dates_only_a_reading(self):
        part = section(text(), "Worked examples")
        top = next(e for e in ROWS if e["slug"] == "py-top")
        self.assertIn(f"   Call site: [src/main.py]({evidence_url(top)}), read by a person on 2026-09-01", part)
        self.assertIn("https://github.com/o/py-top/blob/HEAD/src/main.py", part)
        self.assertIn("   Call site: [src/b.ts](https://github.com/o/ts-one/blob/HEAD/src/b.ts), no reading date recorded",
                      section(text(language="typescript"), "Worked examples"))
        self.assertNotIn("verified", part.lower())

    def test_whose_words_the_summary_is_and_the_caveats_travel(self):
        part = section(text(), "Worked examples")
        self.assertIn("py-top does it. (upstream description)", part)
        self.assertIn("   Caveats: `single-commit`", part)
        # Said once, before the rows: their text is data, not instructions.
        self.assertEqual(part.count(prompts.TEXT_NOTE), 1)
        self.assertLess(part.index(prompts.TEXT_NOTE), part.index("py-top does it."))
        body = text(language="python")
        rest = prompts.wire_pattern_text([e for e in ROWS if e["slug"] in {"shipped"}], PATTERNS, COMPAT,
                                         TAXONOMY, None, pattern="tool-selection")
        self.assertIn("shipped does it. (earlier upstream description)", rest)
        self.assertIn("   Example the project ships: [src/main.py]", rest)
        self.assertIn("- `no-license`: No licence.", rest)
        self.assertIn("What those caveats mean:\n- `single-commit`: One commit.\n", body)
        self.assertNotIn("no-license", body, "only the caveats of the rows shown are explained")

    def test_a_negative_result_says_so_however_its_row_records_it(self):
        # I34: a benchmark says it through its measurement's direction, any
        # other row through the negative-result flag; the prompt marks both.
        rows = [
            {**row("lost-bench", stars=30), "kind": "benchmark", "measurement": {"task": "t", "direction": "unfavourable"}},
            row("dropped", stars=20, flags=["negative-result"], notes="Recall fell; removed."),
            {**row("mixed-bench", stars=10), "kind": "benchmark", "measurement": {"task": "t", "direction": "mixed"}},
        ]
        part = section(prompts.wire_pattern_text(rows, PATTERNS, COMPAT, TAXONOMY, None, pattern="tool-selection"),
                       "Worked examples")
        marked = ("   Negative result: its own author measured Jev for this use and concluded against it "
                  "(author-stated, not reproduced here)")
        blocks = {}
        for line in part.splitlines():
            if line[:3] in {"1. ", "2. ", "3. "}:
                slug = line.split("(`", 1)[1].split("`", 1)[0]
                blocks[slug] = []
            elif blocks and line.startswith("   "):
                blocks[slug].append(line)
        self.assertEqual(set(blocks), {"lost-bench", "dropped", "mixed-bench"})
        for slug, lines in blocks.items():
            with self.subTest(slug=slug):
                self.assertIs(marked in lines, slug != "mixed-bench")

    def test_a_pattern_without_a_cited_row_says_so(self):
        part = section(text("safety-gating"), "Worked examples")
        self.assertIn("No catalogued `safety-gating` row cites the file its code was read in", part)


class SkeletonTest(unittest.TestCase):
    def test_the_example_that_lists_the_pattern_first_is_inlined_under_a_never_executed_header(self):
        part = section(text(language="python"), "Skeleton")
        self.assertIn("examples/02-tools/main.py, catalogued as `example-tools`; the examples index was served SERVED.",
                      part)
        lines = part.splitlines()
        opening = next(i for i, line in enumerate(lines) if line.startswith("`````"))
        self.assertEqual(lines[opening], "`````python", "the fence outlasts the code's own backticks")
        header = []
        for line in lines[opening + 1:]:
            if not line.startswith("# "):
                break
            header.append(line)
        said = " ".join(line[2:] for line in header)
        self.assertTrue(said.startswith("awesome-jev: never executed. Its catalogue row carries code-untested: "
                                        "Read, not run."), said)
        self.assertIn("Source: https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-tools/main.py", said)
        self.assertTrue(all(len(line) <= 80 for line in header[:-1]))
        code = "\n".join(lines[opening + 1 + len(header):]).split("\n`````", 1)[0]
        self.assertEqual(code, EXAMPLES["examples"][1]["code"].rstrip("\n"))
        self.assertIn("Also for `tool-selection`: examples/01-many/main.py.", part)

    def test_the_rows_other_caveats_travel_with_its_code(self):
        flagged = {"examples": [{**EXAMPLES["examples"][1], "flags": ["code-untested", "single-commit", "made-up"]}]}
        part = section(text(examples=flagged), "Skeleton")
        said = " ".join(line[2:] for line in part.splitlines() if line.startswith("# "))
        self.assertIn("carries code-untested: Read, not run.", said)
        self.assertIn("It also carries single-commit: One commit.", said)
        self.assertIn("It also carries made-up.", said, "a flag the taxonomy lacks still travels as its key")
        plain = section(text(), "Skeleton")
        self.assertNotIn("also carries", plain)

    def test_without_a_language_the_examples_own_sets_the_fence_and_the_comment(self):
        only_ts = {"examples": [EXAMPLES["examples"][2]]}
        part = section(text("fan-out", examples=only_ts), "Skeleton")
        self.assertIn("```typescript\n// awesome-jev: the catalogue records no run of this file.", part)

    def test_another_language_gets_its_own_comment_and_what_the_index_records(self):
        part = section(text("fan-out", language="typescript"), "Skeleton")
        self.assertIn("```typescript\n// awesome-jev: the catalogue records no run of this file.", part)
        self.assertIn("console.log(1)", part)

    def test_no_skeleton_in_the_language_names_the_ones_there_are(self):
        part = section(text("fan-out", language="rust"), "Skeleton")
        self.assertIn("No skeleton for `fan-out` in rust. This repository's examples for it: "
                      "examples/01-many/main.py (python), examples/03-ts/main.ts (typescript).", part)
        self.assertNotIn("```", part)

    def test_no_example_or_no_index_is_said_plainly(self):
        self.assertIn("This repository ships no example for `safety-gating`", section(text("safety-gating"), "Skeleton"))
        part = section(text(examples=None), "Skeleton")
        self.assertIn("No examples index could be read (SERVED)", part)

    def test_the_real_index_has_a_skeleton_for_each_examples_patterns(self):
        # Built in memory from catalog.json and examples/, never read from the generated file.
        catalog = json.loads((ROOT / "catalog.json").read_text())
        index, _ = build_examples_index.build(catalog)
        self.assertTrue(index["examples"])
        for example in index["examples"]:
            for key in example["patterns"]:
                chosen, mine = prompts.pick_skeleton(index, key, example["languages"][0])
                with self.subTest(example=example["name"], pattern=key):
                    self.assertIn(example, mine)
                    self.assertIsNotNone(chosen)


class StandaloneTest(unittest.TestCase):
    def imports(self, name: str) -> tuple[set[str], set[str]]:
        tree = ast.parse((PACKAGE / name).read_text())
        absolute = {a.name.split(".")[0] for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
        absolute |= {n.module.split(".")[0] for n in ast.walk(tree)
                     if isinstance(n, ast.ImportFrom) and n.level == 0 and n.module}
        relative = {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.level}
        return absolute, relative

    def test_the_prompt_needs_only_the_standard_library(self):
        absolute, relative = self.imports("prompts.py")
        self.assertEqual(absolute - sys.stdlib_module_names, set())
        self.assertEqual(relative, {"evidence_url", "query"})

    def test_the_link_rule_stands_alone_so_scripts_can_load_it_by_path(self):
        absolute, relative = self.imports("evidence_url.py")
        self.assertEqual(absolute - sys.stdlib_module_names, set())
        self.assertEqual(relative, set())
        import evidence_url as shim  # scripts/evidence_url.py

        self.assertEqual(shim.SOURCE, PACKAGE / "evidence_url.py")
        self.assertEqual(pathlib.Path(shim.evidence_url.__code__.co_filename), PACKAGE / "evidence_url.py")

    def test_the_index_the_server_reads_is_the_one_the_generator_writes(self):
        self.assertEqual(data.EXAMPLES, build_examples_index.OUT)


class RegistrationTest(unittest.TestCase):
    """server.py registers the prompt and hands it the loaded data."""

    @classmethod
    def setUpClass(cls):
        cls.server = load_server()
        catalog = json.loads((ROOT / "catalog.json").read_text())
        cls.index, _ = build_examples_index.build(catalog)

    def test_one_prompt_with_its_arguments(self):
        registered = self.server.mcp.prompts
        self.assertEqual(sorted(registered), ["wire_pattern"])
        params = inspect.signature(registered["wire_pattern"]["fn"]).parameters
        self.assertEqual({n: p.default for n, p in params.items()},
                         {"pattern": inspect.Parameter.empty, "language": "", "surface": ""})
        self.assertGreater(len(inspect.getdoc(self.server.wire_pattern) or ""), 200)

    def test_it_answers_with_prompts_on_the_loaded_data(self):
        s = self.server
        with mock.patch.object(s, "_examples", return_value=(self.index, "in memory")):
            for args in ({"pattern": "tool-selection", "language": "python", "surface": "cloudflare"},
                         {"pattern": "retry-control"}, {"pattern": "zzz"}):
                with self.subTest(**args):
                    expected = prompts.wire_pattern_text(
                        s.CATALOG, s.PATTERNS, s.COMPAT, s.TAXONOMY, self.index, data=s.PROVENANCE.line(),
                        served="in memory", **{"language": "", "surface": "", **args})
                    self.assertEqual(s.wire_pattern(**args), expected)

    def test_the_index_is_read_once_and_only_when_asked_for(self):
        s = load_server()
        self.assertEqual(s._examples.cache_info().misses, 0, "starting the server read the examples index")
        with mock.patch.object(s, "load_examples", return_value=(self.index, "counted")) as loader:
            s.wire_pattern("tool-selection")
            s.wire_pattern("fan-out", "python")
        self.assertEqual(loader.call_count, 1)
        s._examples.cache_clear()


class PublishSmokeTest(unittest.TestCase):
    def test_the_smoke_step_expects_every_registered_prompt_and_the_bundled_index(self):
        tree = ast.parse((PACKAGE / "server.py").read_text())
        names = sorted(
            node.name for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and any(isinstance(d, ast.Call) and isinstance(d.func, ast.Attribute) and d.func.attr == "prompt"
                    for d in node.decorator_list)
        )
        self.assertEqual(names, ["wire_pattern"])
        workflow = (ROOT / ".github" / "workflows" / "publish.yml").read_text()
        self.assertIn(f"assert prompts == {json.dumps(names)}, prompts", workflow)
        self.assertIn("asyncio.run(server.mcp.get_prompt(", workflow)
        self.assertIn("data._read_dir(data.BUNDLED, (data.EXAMPLES,))", workflow)


if __name__ == "__main__":
    unittest.main()
