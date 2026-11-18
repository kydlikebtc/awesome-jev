"""Negative results: one predicate, one place to record each, first on every list (I34).

A negative result is a row whose own author measured Jev for its use and
concluded against it. A kind: benchmark row says so only in its
measurement's direction (unfavourable, I44); any other row carries the
negative-result flag, which lint keeps off benchmarks and requires to come with
notes saying where the conclusion can be read. Every surface derives
"negative" from either through query.is_negative_result(), and the site's
isNegativeResult() is held to it on scripts/tests/negative_cases.json (read by
scripts/test_catalog_core.mjs too). The README's "Measured, not claimed",
docs/measured.md and docs/status.md list them first, in band order, never the
file's. Pages render in memory: CI runs these tests before it regenerates.
"""

from __future__ import annotations

import copy
import datetime as dt
import json
import pathlib
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats
import build_docs
import build_readme
import lint
import measurements
from readme import pages, rows, sections, strings
from test_star_bands import moved_within_bands

ROOT = pathlib.Path(__file__).resolve().parents[2]
CASES = json.loads((pathlib.Path(__file__).resolve().parent / "negative_cases.json").read_text())["cases"]
CATALOG = json.loads((ROOT / "catalog.json").read_text())
RETIRED = json.loads((ROOT / "retired.json").read_text())
SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
TAXONOMY = json.loads((ROOT / "taxonomy.json").read_text())
QUERY = measurements.load_query()
TODAY = dt.date(2026, 9, 28)

PLUGIN = {
    "slug": "dropped-use",
    "title": "Dropped use",
    "summary": "A plugin.",
    "summary_zh": "一个插件。",
    "url": "https://github.com/someone/dropped-use",
    "kind": "plugin",
    "patterns": ["context-compaction"],
    "has_code": False,
    "flags": ["negative-result"],
    "notes": "Its author measured handoff recall and removed the Jev step.",
    "first_seen": "2026-09-20",
    "sources": [{"catalog": "maintainer submission", "url": "https://github.com/kydlikebtc/awesome-jev"}],
    "license": "CC0-1.0",
}


def flag_problems(entry: dict) -> list[str]:
    return measurements.negative_flag_problems(entry)


class PredicateTest(unittest.TestCase):
    def test_the_shared_cases(self):
        self.assertGreaterEqual(len(CASES), 10)
        for case in CASES:
            with self.subTest(case=case["name"]):
                self.assertIs(QUERY.is_negative_result(case["entry"]), case["negative"])
                self.assertIs(QUERY.is_independent_report(case["entry"]), case["independent"])
                self.assertIs(rows.is_negative(case["entry"]), case["negative"])

    def test_one_flag_and_one_direction_name_it(self):
        self.assertEqual(QUERY.NEGATIVE_FLAG, measurements.NEGATIVE_FLAG)
        self.assertIn(QUERY.NEGATIVE_FLAG, SCHEMA["properties"]["flags"]["items"]["enum"])
        self.assertIn(QUERY.NEGATIVE_DIRECTION, QUERY.DIRECTIONS)
        (label,) = [f for f in TAXONOMY["flags"] if f["key"] == QUERY.NEGATIVE_FLAG]
        self.assertEqual((label["en"], label["zh"]), ("measured, not adopted", "实测后未采用"))
        self.assertIs(label["zh_machine"], True)
        self.assertIn("not reproduced here", label["blurb_en"])
        core = (ROOT / "site" / "catalog-core.mjs").read_text()
        self.assertIn('export const NEGATIVE_FLAG = "negative-result";', core)
        self.assertIn('export const NEGATIVE_DIRECTION = "unfavourable";', core)


class FlagRuleTest(unittest.TestCase):
    def test_a_flagged_row_with_a_sourced_note_passes(self):
        for notes in (
            "Removed in PR #1165.",
            "See https://example.org/writeup for why it was dropped.",
            "Handoffs written this way had worse recall than the raw transcript.",
            "Tied the old labeller on 413 headlines, so the author kept it in shadow; see issue 44.",
        ):
            with self.subTest(notes=notes):
                self.assertEqual(flag_problems({**PLUGIN, "notes": notes}), [])
        self.assertEqual(flag_problems({**PLUGIN, "flags": ["no-license"], "notes": ""}), [])

    def test_never_on_a_benchmark(self):
        (found,) = flag_problems({**PLUGIN, "kind": "benchmark"})
        self.assertIn("kind is 'benchmark'", found)
        self.assertIn("measurement.direction", found)

    def test_it_needs_notes_that_say_where_the_conclusion_is(self):
        for notes in (None, "", "   "):
            with self.subTest(notes=notes):
                entry = {**PLUGIN, "notes": notes} if notes is not None else {k: v for k, v in PLUGIN.items() if k != "notes"}
                (found,) = flag_problems(entry)
                self.assertIn("notes is empty", found)
        (found,) = flag_problems({**PLUGIN, "notes": "The author did not like it."})
        self.assertIn("names no link, pull request or issue number, or measurement", found)

    def test_lint_reports_it_on_the_row(self):
        errors, _ = lint.check_entry_invariants({**PLUGIN, "kind": "benchmark"}, "catalog.json[3]", retired=False, today=TODAY)
        self.assertEqual([e for e in errors if "negative-result" in e],
                         [e for e in errors if e.startswith("catalog.json[3]: dropped-use: flagged negative-result")])
        self.assertEqual(len([e for e in errors if "negative-result" in e]), 1, errors)
        errors, _ = lint.check_entry_invariants(PLUGIN, "catalog.json[3]", retired=False, today=TODAY)
        self.assertEqual(errors, ())


class RealCatalogueTest(unittest.TestCase):
    def test_the_flag_sits_only_on_rows_that_are_not_benchmarks_and_says_why(self):
        flagged = [e for e in CATALOG if QUERY.NEGATIVE_FLAG in (e.get("flags") or [])]
        self.assertTrue(flagged)
        for entry in flagged:
            with self.subTest(slug=entry["slug"]):
                self.assertNotEqual(entry["kind"], "benchmark")
                self.assertEqual(flag_problems(entry), [])

    def test_the_negative_results_the_rows_record(self):
        self.assertEqual(
            sorted(e["slug"] for e in measurements.negative(CATALOG)),
            ["hermes-agent-jev-evaluation", "hermes-jev-skills", "jev-skill-router",
             "jevkit-bragamat", "no-mistakes-review-context", "worldmonitor-shadow-mode"],
        )
        self.assertEqual(_stats.compute()["negative_results"], len(measurements.negative(CATALOG)))


class ReadmeTest(unittest.TestCase):
    @mock.patch.object(sections, "START_HERE", [])
    def render(self, catalog, pack=strings.EN) -> str:
        readme = build_readme.render(copy.deepcopy(catalog), copy.deepcopy(RETIRED), pack)
        start = readme.index(f"\n## {pack['measured_h']}\n")
        return readme[start: readme.index("\n## ", start + 1)]

    def test_negative_results_come_first_under_their_heading_in_both_languages(self):
        negatives = sorted(measurements.negative(CATALOG), key=rows.sort_key)
        for pack in (strings.EN, strings.ZH):
            with self.subTest(lang=pack["lang_code"]):
                text = self.render(CATALOG, pack)
                head, tail = text.split(f"\n### {pack['others_h']}\n")
                self.assertIn(f"\n### {pack['negative_h']}\n", head)
                for entry in negatives:
                    self.assertIn(f"**[{rows.esc(entry['title'])}]({entry['url']})**", head)
                note = rows.marked(pack, "negative_note", site=rows.negatives_link(pack["lang_code"]))
                self.assertIn(note, head)
        self.assertIn("negative_note", strings.ZH_MACHINE)
        self.assertTrue(rows.marked(strings.ZH, "negative_note", site="").endswith(" <sub>(机翻)</sub>"))
        self.assertIn("not reproduced here", strings.EN["negative_note"])

    def test_file_order_and_stars_within_a_band_change_nothing(self):
        expected = self.render(CATALOG)
        self.assertEqual(self.render(list(reversed(CATALOG))), expected)
        for how in ("low", "high"):
            self.assertEqual(self.render(moved_within_bands(CATALOG, how)), expected)

    def test_negative_results_count_towards_the_limit_and_are_cut_at_it(self):
        many = [
            {**PLUGIN, "slug": f"neg-{i:02d}", "title": f"neg {i:02d}", "url": f"https://github.com/o/neg-{i:02d}"}
            for i in range(sections.INLINE_MEASURED + 3)
        ]
        negatives, picks, others = sections.measured_selection(many + [e for e in CATALOG if rows.is_measured(e)], [])
        self.assertEqual(len(negatives), sections.INLINE_MEASURED)
        self.assertEqual((picks, others), ([], []))
        few = many[:2]
        negatives, picks, others = sections.measured_selection(
            few + [e for e in CATALOG if rows.is_measured(e) and not rows.is_negative(e)], rows.collection_slugs("measured")
        )
        self.assertEqual(len(negatives) + len(picks) + len(others), sections.INLINE_MEASURED)
        self.assertEqual(len(negatives), 2)

    def test_without_negative_results_there_is_no_heading(self):
        positive = [e for e in CATALOG if not rows.is_negative(e)]
        text = self.render(positive)
        self.assertNotIn(strings.EN["negative_h"], text)
        self.assertNotIn(strings.EN["others_h"], text)


class MeasuredPageTest(unittest.TestCase):
    def test_the_page_puts_them_first_and_ignores_file_order(self):
        measured = [e for e in CATALOG if rows.is_measured(e)]
        for pack in (strings.EN, strings.ZH):
            with self.subTest(lang=pack["lang_code"]):
                page = pages.render_measured_page(measured, pack)
                self.assertLess(page.index(pack["negative_h"]), page.index(pack["others_h"]))
                self.assertEqual(pages.render_measured_page(list(reversed(measured)), pack), page)


class StatusBlockTest(unittest.TestCase):
    def test_every_negative_result_is_listed_with_whose_conclusion_it_is(self):
        block = build_docs.negative_block(CATALOG)
        lines = block.splitlines()
        self.assertEqual(len(lines), len(measurements.negative(CATALOG)))
        for line in lines:
            self.assertTrue(line.endswith("author-stated, not reproduced here."), line)
        self.assertIn("flagged `negative-result`", block)
        self.assertIn("direction is `unfavourable`", block)
        # Caveat flags travel with the row: a result kept in shadow says so here too.
        for entry in measurements.negative(CATALOG):
            (line,) = [line for line in lines if f"#{entry['slug']})" in line]
            for flag in entry.get("flags") or []:
                if flag != "negative-result":
                    self.assertIn(f"`{flag}`", line, entry["slug"])
        shadow = build_docs.negative_block([{**PLUGIN, "flags": ["no-license", "negative-result", "shadow-mode-only"]}])
        self.assertIn("(`plugin`; caveats: `shadow-mode-only`, `no-license`)", shadow)
        self.assertEqual(build_docs.negative_block(list(reversed(CATALOG))), block)
        self.assertEqual(build_docs.negative_block(moved_within_bands(CATALOG, "high")), block)
        self.assertEqual(build_docs.negative_block([]), "No row records a negative result yet.")
        # Inside one band the title decides, whatever the counts.
        same_band = [
            {**PLUGIN, "slug": "zeta", "title": "zeta", "stars": 150},
            {**PLUGIN, "slug": "alpha", "title": "alpha", "stars": 900},
            {**PLUGIN, "slug": "mid", "title": "mid", "stars": 120},
        ]
        order = [line.split("](")[0] for line in build_docs.negative_block(same_band).splitlines()]
        self.assertEqual(order, ["- [alpha", "- [mid", "- [zeta"])

    def test_status_md_carries_the_block_and_the_count(self):
        rendered = build_docs.render()[ROOT / "docs" / "status.md"]
        self.assertIn("<!-- negative:start -->\n" + build_docs.negative_block(CATALOG) + "\n<!-- negative:end -->", rendered)
        self.assertIn("### Negative results", rendered)
        self.assertIn(f"| {_stats.compute()['negative_results']} |", rendered)


class SiteTest(unittest.TestCase):
    def test_the_page_shows_a_badge_and_a_toggle_from_the_shared_predicate(self):
        page = (ROOT / "site" / "index.html").read_text()
        self.assertIn("isNegativeResult } from \"./catalog-core.mjs\"", page)
        self.assertIn('["neg", "t_neg", ""]', page)
        self.assertIn("isNegativeResult(e) ?", page)
        self.assertIn("not reproduced here", page[page.index("negative_about:"):][:400])


if __name__ == "__main__":
    unittest.main()
