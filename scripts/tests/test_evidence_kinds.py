"""What a cited file shows is recorded and counted apart, and machine signals go to a page (I18).

`evidence` used to be one kind of record and one published number: 1,121
"call-site" citations, 52 of which were files of `kind: alternative` projects
that by definition are not built on Jev. `evidence.kind` now says what a cited file
shows (call-site, wire-shape, example-only), lint requires `wire-shape` on
every alternative, and _stats publishes one count per kind.

Two weaker signals are machine judgements, not facts: a cited file under an
examples directory, and a citation resting on one model name. They are counted
in _stats and listed in docs/review-queue.md rather than warned about per row,
and nothing about them is written into catalog.json.
"""

from __future__ import annotations

import contextlib
import copy
import io
import json
import pathlib
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import _github  # noqa: E402
import _stats  # noqa: E402
import build_readme  # noqa: E402
import build_review_queue as queue  # noqa: E402
import lint_docs  # noqa: E402
import regenerate  # noqa: E402
from readme import sections  # noqa: E402


def entry(slug: str, *, kind: str = "project", url: str | None = None, **evidence) -> dict:
    row = {
        "slug": slug,
        "title": slug,
        "summary": "s",
        "summary_zh": "s",
        "url": url or f"https://github.com/someone/{slug}",
        "kind": kind,
        "patterns": ["tool-selection"],
        "sources": [],
        "license": "CC0-1.0",
    }
    if evidence:
        # Read by a person, so that only the signals under test list the row:
        # the README front-page section lists a cited file nobody has read.
        row["evidence"] = {"read_on": "2026-09-01", **evidence}
    return row


ROWS = [
    entry("plain", path="src/app.py", matched=["system_one", "typesafe_sdk"]),
    entry("marked", path="src/app.py", matched=["system_one"], kind_="call-site"),
    entry("alt", kind="alternative", path="server.py", matched=["/v1/systemone"], kind_="wire-shape"),
    entry("sample", path="examples/demo.py", matched=["system_one", "Choice"]),
    entry("sample-judged", path="examples/demo.py", matched=["system_one", "Choice"], kind_="example-only"),
    entry("nested-sample", path="sdk/example/run.ts", matched=["jev-latest"]),
    entry("lookalike", path="my_examples/run.py", matched=["jev-latest", "choice"]),
    entry("host-only", path="config.py", matched=["api.typesafe.ai"]),
    entry("none"),
]
for row in ROWS:
    if "evidence" in row and "kind_" in row["evidence"]:
        row["evidence"]["kind"] = row["evidence"].pop("kind_")


def compute(rows: list[dict]) -> dict:
    patterns = [{"key": "tool-selection"}]
    schema = {"properties": {"kind": {"enum": ["project", "alternative"]}}}
    with patch.object(_stats, "load", return_value=(rows, [], patterns, {"platforms": []}, schema)):
        return _stats.compute()


class KindTest(unittest.TestCase):
    def test_a_record_without_kind_is_a_call_site(self):
        kinds = {row["slug"]: _stats.evidence_kind(row) for row in ROWS}
        self.assertEqual(kinds["plain"], "call-site")
        self.assertEqual(kinds["marked"], "call-site")
        self.assertEqual(kinds["alt"], "wire-shape")
        self.assertEqual(kinds["sample-judged"], "example-only")
        self.assertIsNone(kinds["none"])

    def test_one_count_per_kind_and_they_add_up(self):
        stats = compute(ROWS)
        self.assertEqual(stats["call_site_rows"], 6)
        self.assertEqual(stats["wire_shape_rows"], 1)
        self.assertEqual(stats["example_only_rows"], 1)
        self.assertNotIn("evidence_rows", stats)
        cited = sum(1 for row in ROWS if row.get("evidence"))
        self.assertEqual(stats["call_site_rows"] + stats["wire_shape_rows"] + stats["example_only_rows"], cited)

    def test_the_kinds_are_the_schemas(self):
        schema = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
        self.assertEqual(
            tuple(schema["properties"]["evidence"]["properties"]["kind"]["enum"]), _stats.EVIDENCE_KINDS
        )


class SignalTest(unittest.TestCase):
    def test_examples_directory_until_someone_records_a_kind(self):
        marked = {row["slug"] for row in ROWS if _stats.examples_unjudged(row)}
        # A recorded kind is the decision; a directory merely named *examples is not one.
        self.assertEqual(marked, {"sample", "nested-sample"})

    def test_one_model_name_or_the_host_alone(self):
        marked = {row["slug"] for row in ROWS if _stats.single_model_name(row)}
        self.assertEqual(marked, {"nested-sample", "host-only"})
        self.assertFalse(_stats.single_model_name(entry("x", path="a.py", matched=["system_one"])))
        self.assertFalse(_stats.single_model_name(entry("x", path="a.py", matched=["jev-latest", "choice"])))

    def test_counts_match_the_signals(self):
        stats = compute(ROWS)
        self.assertEqual(stats["review_examples_dir"], 2)
        self.assertEqual(stats["review_single_model_name"], 2)

    def test_the_model_names_are_ones_discovery_treats_as_jev_signals(self):
        # verify_claims --discover scores a file by these; a name here that it
        # does not know would be a signal nothing else in the repository uses.
        self.assertTrue(set(_stats.MODEL_NAMES_AND_HOST) <= set(_github.strong()))
        # A pinned version counts for both, whichever version it is.
        for version in _github.version_signals():
            if _github.VERSION.fullmatch(version):
                self.assertTrue(_stats.PINNED_MODEL_VERSION.fullmatch(version))
        self.assertEqual(_github.strong_signals("jev-9.9"), ["jev-9.9"])
        self.assertTrue(_stats.single_model_name(entry("x", path="a.py", matched=["jev-9.9"])))
        self.assertTrue(_stats.single_model_name(entry("x", path="a.py", matched=["jev-9.9.1"])))
        self.assertFalse(_stats.single_model_name(entry("x", path="a.py", matched=["jev-2048"])))


class RealCatalogueTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "catalog.json").read_text())
        cls.stats = _stats.compute()

    def test_every_alternative_citation_is_wire_shape(self):
        wrong = [
            e["slug"]
            for e in self.catalog
            if e["kind"] == "alternative" and e.get("evidence") and e["evidence"].get("kind") != "wire-shape"
        ]
        self.assertEqual(wrong, [])

    def test_wire_shape_is_never_described_as_a_file_without_a_jev_call(self):
        # An alternative's cited file is often a baseline script that sends the
        # real Jev the same request (NanoJev's own notes say so), so a wire-shape
        # citation is "not a Jev integration", never "not a Jev call".
        calls_jev = [
            e["slug"]
            for e in self.catalog
            if (e.get("evidence") or {}).get("kind") == "wire-shape"
            and {"api.typesafe.ai", "typesafe-ai/jev"} & set(e["evidence"]["matched"])
        ]
        self.assertTrue(calls_jev)
        site = (ROOT / "site" / "index.html").read_text()
        wire_label = [line for line in site.splitlines() if "cite_wire_shape:" in line]
        self.assertEqual(len(wire_label), 2)
        surfaces = {
            "README": build_readme.EN["verified_recheck"] + build_readme.ZH["verified_recheck"],
            "site": "\n".join(wire_label),
            "status": (ROOT / "docs" / "status.md").read_text(),
            "llms": (ROOT / "llms.txt").read_text(),
            "schema": (ROOT / "schema" / "entry.schema.json").read_text(),
        }
        for name, text in surfaces.items():
            for phrase in ("not a Jev call", "without using Jev", "rather than using Jev", "并非调用 Jev", "并未使用 Jev"):
                with self.subTest(surface=name, phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_published_counts_add_up_to_the_cited_rows(self):
        cited = sum(1 for e in self.catalog if e.get("evidence"))
        s = self.stats
        self.assertEqual(s["call_site_rows"] + s["wire_shape_rows"] + s["example_only_rows"], cited)

    def test_the_page_counts_what_status_publishes(self):
        # Rendered, not compared with the committed page: CI runs the unit
        # tests before it regenerates, and a pull request that re-files a row
        # (docs/review-queue.md lists pattern signals too) leaves the page to
        # the bot. The `generated` step of scripts/check.py judges the file.
        text = queue.render(self.catalog)
        for key, stat in (("examples-dir", "review_examples_dir"), ("single-model-name", "review_single_model_name")):
            with self.subTest(key=key):
                self.assertIn(f"](#{key}) | {self.stats[stat]} |", text)


class ReviewQueuePageTest(unittest.TestCase):
    def test_sections_are_bilingual_and_uniquely_anchored(self):
        built = [build(ROWS) for build in queue.SECTIONS]
        self.assertEqual(len({s.key for s in built}), len(built))
        cjk = re.compile(r"[㐀-鿿]")
        for s in built:
            with self.subTest(section=s.key):
                self.assertRegex(s.key, r"^[a-z0-9-]+$")
                for en, zh in ((s.title_en, s.title_zh), (s.about_en, s.about_zh), (s.leave_en, s.leave_zh)):
                    self.assertTrue(en.strip())
                    self.assertRegex(zh, cjk)
                for en, zh in s.columns:
                    self.assertTrue(en and cjk.search(zh))
                for cells in s.rows:
                    self.assertEqual(len(cells), len(s.columns))

    def test_page_lists_each_marked_row_under_its_signal(self):
        text = queue.render(ROWS)
        examples, names = text.split('<a id="single-model-name"></a>')
        self.assertIn("#sample)", examples)
        self.assertIn("#nested-sample)", examples)
        self.assertNotIn("#sample-judged)", examples)
        self.assertIn("#host-only)", names)
        self.assertIn("#nested-sample)", names)
        self.assertNotIn("#plain)", text)
        self.assertIn("model-written", text.split("\n\n")[2])
        self.assertIn("机翻", text.split("\n\n")[2])

    def test_an_empty_signal_says_so(self):
        # docs/held.txt is not this fixture's: with nothing held, every section is empty.
        with patch.object(queue, "HELD", pathlib.Path(tempfile.gettempdir()) / "no-held.txt"):
            text = queue.render([entry("plain", path="src/app.py", matched=["system_one", "typesafe_sdk"])])
        self.assertEqual(text.count("Nothing is on this list. · 此列表为空。"), len(queue.SECTIONS))

    def test_outside_text_cannot_break_the_table(self):
        hostile = entry("hostile", path="examples/a|b`c.py", matched=["x|y", "`z`\nw"])
        text = queue.render([hostile])
        line = next(l for l in text.splitlines() if "#hostile)" in l)
        self.assertEqual(len(re.findall(r"(?<!\\)\|", line)), len(queue.EVIDENCE_COLUMNS) + 1, line)
        self.assertNotIn("\n`z`", text)
        self.assertIn("examples/a%7Cb%60c.py", line)

    def test_nothing_on_the_page_moves_with_stars_or_dates(self):
        rows = copy.deepcopy(ROWS)
        before = queue.render(rows)
        for row in rows:
            row["stars"] = 12345
            row["checked"] = "2026-09-28"
            if row.get("evidence"):
                row["evidence"]["read_on"] = "2026-09-28"
        self.assertEqual(queue.render(rows), before)

    def test_check_mode_reports_a_stale_page_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            page = pathlib.Path(tmp) / "docs" / "review-queue.md"
            page.parent.mkdir()
            page.write_text("old\n")
            (pathlib.Path(tmp) / "catalog.json").write_text("[]\n")
            with patch.object(queue, "ROOT", pathlib.Path(tmp)), patch.object(queue, "OUT", page), patch.object(
                queue, "render", return_value="new\n"
            ), contextlib.redirect_stderr(io.StringIO()) as err, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(queue.main(["--check"]), 1)
                self.assertIn("docs/review-queue.md is stale", err.getvalue())
                self.assertEqual(page.read_text(), "old\n")
                self.assertEqual(queue.main([]), 0)
            self.assertEqual(page.read_text(), "new\n")


class WiringTest(unittest.TestCase):
    def test_regenerate_runs_it_and_owns_its_output(self):
        self.assertIn("build_review_queue.py", [script for script, _ in regenerate.GENERATORS])
        self.assertIn("docs/review-queue.md", regenerate.OUTPUTS)

    def test_lint_docs_treats_it_as_generated_and_its_quotes_as_quotes(self):
        self.assertTrue(lint_docs.generated("docs/review-queue.md"))
        self.assertIn("docs/review-queue.md", lint_docs.QUOTES_UPSTREAM)
        # The page does quote strings that are not compat.json model strings.
        text = (ROOT / "docs" / "review-queue.md").read_text()
        self.assertTrue(lint_docs.check_vendor_facts("docs/review-queue.md", text, lint_docs.vendor_facts()))

    def test_readme_prints_every_kind_and_marks_the_model_written_chinese(self):
        stats = {**_stats.compute(), "call_site_rows": 7001, "wire_shape_rows": 7002, "example_only_rows": 7003}
        catalog = json.loads((ROOT / "catalog.json").read_text())
        retired = json.loads((ROOT / "retired.json").read_text())
        with patch.object(_stats, "compute", return_value=stats):
            english = build_readme.render(catalog, retired, build_readme.EN)
            chinese = build_readme.render(catalog, retired, build_readme.ZH)
        for text in (english, chinese):
            for number in ("7001", "7002", "7003"):
                self.assertIn(number, text)
            self.assertIn("(docs/review-queue.md)", text)
        line = next(l for l in chinese.splitlines() if "7001" in l and "调用点文本复查" in l)
        self.assertTrue(line.endswith(" <sub>(机翻)</sub>"), line)
        self.assertNotIn("机翻", next(l for l in english.splitlines() if "7001" in l and "Call-site" in l))
        self.assertIn("verified_recheck", sections.ZH_MACHINE)


if __name__ == "__main__":
    unittest.main()
