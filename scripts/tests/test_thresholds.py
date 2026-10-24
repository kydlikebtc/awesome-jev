"""observed_thresholds: the constants a cited file compares a Jev answer with (I26).

SKILL.md and examples/README.md said one catalogued system's thresholds ranged
"from 0.3 to 0.9", a number typed from one row's notes that nothing re-derived.
The catalogue now records, per row, each constant as the cited file writes it,
standing on a string in evidence.matched that the weekly claims run re-reads;
_stats counts them per primitive and quantity, build_docs writes the ranges into
both files, and lint_docs rejects a range typed anywhere else.

Nothing here reads a committed generated file: build_docs.render() and the
review queue render in memory, since a sources-only pull request runs these
tests before regenerating.
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import _stats  # noqa: E402
import build_assets  # noqa: E402
import build_docs  # noqa: E402
import build_review_queue  # noqa: E402
import lint  # noqa: E402
import lint_docs  # noqa: E402
import regenerate  # noqa: E402
import thresholds  # noqa: E402

TODAY = dt.date(2026, 9, 28)
SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
CATALOG = json.loads((ROOT / "catalog.json").read_text())
SKILL = "skills/awesome-jev/SKILL.md"
EXAMPLES_README = "examples/README.md"


def item(**changes) -> dict:
    out = {
        "question_type": "noul",
        "compares": "probability",
        "value": 0.55,
        "decision": "at or above: highlight the line",
        "source": "HIT_THRESHOLD = 0.55",
    }
    out.update(changes)
    return {k: v for k, v in out.items() if v is not None}


def entry(slug: str = "demo", items=None, matched=None, **extra) -> dict:
    items = [item()] if items is None else items
    return {
        "slug": slug,
        "title": slug.title(),
        "url": f"https://github.com/someone/{slug}",
        "stars": 3,
        "evidence": {
            "path": "src/config.ts",
            "matched": matched if matched is not None else ["api.typesafe.ai", *{i["source"] for i in items}],
        },
        "observed_thresholds": items,
        **extra,
    }


class RuleTest(unittest.TestCase):
    """thresholds.row_problems, one rule at a time."""

    def problems(self, row: dict) -> list[str]:
        return thresholds.row_problems(row, TODAY)

    def test_a_well_formed_row_and_a_row_without_the_field_pass(self):
        self.assertEqual(self.problems(entry()), [])
        self.assertEqual(self.problems({"slug": "plain"}), [])

    def test_the_value_may_be_spelled_as_the_file_spells_it(self):
        for source, value in (
            ("FLAG_THRESHOLD = 0.70", 0.7), ("p >= .5", 0.5), ("review_priority >= 2.0", 2.0),
            ("threshold: 1", 1), ("{ floor: 0.55, act: 0.7 }", 0.7),
        ):
            with self.subTest(source=source):
                self.assertTrue(thresholds.written_in(value, source))
        for source, value in (("jev-1.13", 0.13), ("p_2 >= x", 2), ("HIT_THRESHOLD", 0.55), ("0.555", 0.55)):
            with self.subTest(absent=source):
                self.assertFalse(thresholds.written_in(value, source))
        self.assertFalse(thresholds.written_in(True, "x = 1"))

    def test_each_rule_names_what_is_wrong(self):
        cases = (
            ({"evidence": None}, "has observed_thresholds but no evidence"),
            ({"flags": ["not-jev"]}, "is flagged not-jev"),
            ({"url": "https://github.com/kydlikebtc/awesome-jev"}, "cites this repository's own file"),
            ({"repo": "https://github.com/KydLikeBTC/Awesome-Jev"}, "cites this repository's own file"),
        )
        for changes, fragment in cases:
            with self.subTest(fragment=fragment):
                row = {**entry(), **changes}
                if changes.get("evidence", 1) is None:
                    row.pop("evidence")
                found = self.problems(row)
                self.assertEqual(len(found), 1, found)
                self.assertIn(fragment, found[0])

    def test_each_item_rule_names_the_item(self):
        cases = (
            (entry(matched=["api.typesafe.ai"]), "observed_thresholds[0].source 'HIT_THRESHOLD = 0.55' is not one of"),
            (entry(items=[item(value=0.6)]), "observed_thresholds[0].value 0.6 is not written in its source"),
            (entry(items=[item(compares="confidence")]), "a noul answer carries no confidence"),
            (entry(items=[item(question_type="choice", compares="score")]), "a choice answer carries no score"),
            (entry(items=[item(source="X = 1.5", value=1.5)]), "value 1.5: a probability is at most 1"),
            (entry(items=[item(read_on="2026-02-30")]), "read_on is not a valid date"),
            (entry(items=[item(read_on="2026-09-29")]), "read_on 2026-09-29 is in the future"),
        )
        for row, fragment in cases:
            with self.subTest(fragment=fragment):
                found = self.problems(row)
                self.assertEqual(len(found), 1, found)
                self.assertIn(fragment, found[0])
        # The second item is named by its own index.
        two = entry(items=[item(), item(value=0.9, source="HIT = 0.8")], matched=["HIT_THRESHOLD = 0.55", "HIT = 0.8"])
        self.assertEqual(len(self.problems(two)), 1)
        self.assertIn("observed_thresholds[1].value 0.9", self.problems(two)[0])

    def test_a_score_value_lives_on_its_levels_scale(self):
        row = entry(items=[item(question_type="score", compares="score", value=2.0, source="RELEVANT_SCORE = 2.0")])
        self.assertEqual(self.problems(row), [])
        self.assertEqual(self.problems(entry(items=[item(read_on="2026-09-28")])), [])

    def test_lint_runs_the_rules_on_every_row_retired_ones_too(self):
        bad = entry(matched=["api.typesafe.ai"])
        for retired in (False, True):
            with self.subTest(retired=retired):
                errors, _ = lint.check_entry_invariants(bad, "catalog.json[0]", retired=retired, today=TODAY)
                self.assertTrue(any("demo: observed_thresholds[0].source" in e for e in errors), errors)


class AnswerShapeTest(unittest.TestCase):
    def test_the_answers_agree_with_the_primitives_figure(self):
        # thresholds.ANSWERS restates which answers carry a confidence; the
        # README figure (build_assets.PRIMS) says it too. Hold the two together.
        notes = {name: note_en for name, _, _, _, note_en, _ in build_assets.PRIMS}
        self.assertEqual(set(notes), set(thresholds.ANSWERS))
        for name, carried in thresholds.ANSWERS.items():
            with self.subTest(primitive=name):
                says_confidence = "confidence" in notes[name] and "no confidence" not in notes[name]
                self.assertEqual("confidence" in carried, says_confidence)
                self.assertIn("probability", carried)

    def test_the_schema_is_the_module_s_vocabulary(self):
        props = list(SCHEMA["properties"])
        self.assertEqual(props[props.index("primitives_seen") + 1], "observed_thresholds")
        field = SCHEMA["properties"]["observed_thresholds"]
        fields = field["items"]["properties"]
        self.assertEqual(tuple(fields["question_type"]["enum"]), thresholds.QUESTION_TYPES)
        self.assertEqual(fields["question_type"]["enum"], SCHEMA["properties"]["question_types"]["items"]["enum"])
        self.assertEqual(tuple(fields["compares"]["enum"]), thresholds.COMPARES)
        self.assertEqual(set(field["items"]["required"]), {"question_type", "compares", "value", "decision", "source"})
        self.assertEqual(field["maxItems"], SCHEMA["properties"]["evidence"]["properties"]["matched"]["maxItems"])
        for word in ("not a recommendation", "evidence.matched"):
            self.assertIn(word, field["description"])
        self.assertNotIn("verified", field["description"].lower())


class StatsTest(unittest.TestCase):
    def catalogue(self) -> list[dict]:
        return [
            entry("a", items=[item(value=0.3, source="LOW = 0.3"), item(value=0.9, source="HIGH = 0.9")]),
            entry("b", items=[item(question_type="choice", compares="confidence", value=0.6, source="c >= 0.6", read_on="2026-09-20")]),
            entry("c", items=[item(value=0.5, source="p >= 0.5")]),
            {"slug": "d", "title": "D", "url": "https://github.com/someone/d"},
        ]

    def test_ranges_never_mix_a_probability_with_a_confidence(self):
        ranges = thresholds.ranges(self.catalogue())
        self.assertEqual(list(ranges), ["choice confidence", "noul probability"])
        self.assertEqual(ranges["noul probability"], {"rows": 2, "thresholds": 3, "low": 0.3, "high": 0.9})
        self.assertEqual(ranges["choice confidence"], {"rows": 1, "thresholds": 1, "low": 0.6, "high": 0.6})
        self.assertEqual(thresholds.ranges(list(reversed(self.catalogue()))), ranges)

    def test_rows_unread_and_sources(self):
        catalogue = self.catalogue()
        self.assertEqual([e["slug"] for e in thresholds.rows(catalogue)], ["a", "b", "c"])
        self.assertEqual([e["slug"] for e in thresholds.unread(catalogue)], ["a", "c"])
        self.assertEqual(thresholds.sources(catalogue[0]), {"LOW = 0.3", "HIGH = 0.9"})

    def test_compute_counts_the_real_catalogue_by_the_module(self):
        s = _stats.compute()
        self.assertEqual(s["threshold_rows"], len(thresholds.rows(CATALOG)))
        self.assertEqual(s["thresholds_recorded"], sum(len(thresholds.recorded(e)) for e in CATALOG))
        self.assertEqual(s["threshold_ranges"], thresholds.ranges(CATALOG))
        self.assertEqual(s["review_thresholds_unread"], len(thresholds.unread(CATALOG)))

    def test_a_threshold_source_is_not_a_second_string_for_the_call(self):
        # The single-model-name signal asks what the call-site claim rests on.
        row = entry(items=[item()], matched=["jev-latest", "HIT_THRESHOLD = 0.55"])
        self.assertTrue(_stats.single_model_name(row))
        self.assertFalse(_stats.single_model_name({**row, "observed_thresholds": []}))

    def test_numbers_print_as_the_file_would(self):
        self.assertEqual([thresholds.number(v) for v in (0.55, 0.9, 2.0, 0.05, None)], ["0.55", "0.9", "2", "0.05", "—"])


class RealCatalogueTest(unittest.TestCase):
    def test_every_recorded_threshold_keeps_every_rule(self):
        for row in thresholds.rows(CATALOG):
            with self.subTest(slug=row["slug"]):
                self.assertEqual(thresholds.row_problems(row, dt.date.today()), [])
                self.assertEqual(lint.validate(row, SCHEMA, row["slug"]), lint.Findings())

    def test_the_field_sits_right_after_the_signal_or_the_evidence(self):
        for row in thresholds.rows(CATALOG):
            with self.subTest(slug=row["slug"]):
                keys = list(row)
                before = keys[keys.index("observed_thresholds") - 1]
                self.assertEqual(before, "primitives_seen" if "primitives_seen" in row else "evidence")

    def test_decisions_say_which_side_of_the_constant(self):
        for row in thresholds.rows(CATALOG):
            for found in thresholds.recorded(row):
                with self.subTest(slug=row["slug"], source=found["source"]):
                    self.assertRegex(found["decision"], r"^(at or above|above|below|at or below)\b")


class DocsTest(unittest.TestCase):
    """SKILL.md and examples/README.md state the ranges as generated values."""

    def rendered(self) -> dict[str, str]:
        return {str(path.relative_to(ROOT)): text for path, text in build_docs.render().items()}

    def test_both_files_are_filled_by_build_docs_and_staged_by_the_bots(self):
        rendered = self.rendered()
        for rel in (SKILL, EXAMPLES_README):
            with self.subTest(rel=rel):
                self.assertIn(rel, rendered)
                self.assertIn(rel, regenerate.OUTPUTS)
        add = next(
            line for line in (ROOT / ".github" / "workflows" / "metadata.yml").read_text().splitlines() if "git add" in line
        )
        self.assertIn(SKILL, add.split())
        self.assertIn(EXAMPLES_README, add.split())

    def test_the_ranges_come_from_the_stats(self):
        s = _stats.compute()
        values = build_docs.inline_values(s)
        noul, choice = s["threshold_ranges"]["noul probability"], s["threshold_ranges"]["choice confidence"]
        self.assertEqual(values["threshold_noul_low"], thresholds.number(noul["low"]))
        self.assertEqual(values["threshold_noul_high"], thresholds.number(noul["high"]))
        self.assertEqual(values["threshold_choice_low"], thresholds.number(choice["low"]))
        self.assertEqual(values["threshold_choice_high"], thresholds.number(choice["high"]))
        rendered = self.rendered()
        for rel in (SKILL, EXAMPLES_README):
            text = rendered[rel]
            with self.subTest(rel=rel):
                for key in ("threshold_rows", "threshold_noul_low", "threshold_noul_high",
                            "threshold_choice_low", "threshold_choice_high", "thresholds_unread"):
                    self.assertIn(f"<!--n:{key}-->{values[key]}<!--/n-->", text)
                self.assertIn("not recommendations", text)
                # The count is of rows recording a threshold so far, not of every
                # row whose cited file compares one (the reading was a first pass).
                self.assertIn("a first reading, not every row whose file has one", " ".join(text.split()))
                self.assertEqual(lint_docs.check_decimal_ranges(rel, text), [])
                self.assertEqual(lint_docs.check_leading_markers(rel, text), [])

    def test_llms_txt_counts_the_rows_recorded_so_far(self):
        text = " ".join(self.rendered()["llms.txt"].split())
        self.assertIn("<!--n:threshold_rows-->", text)
        self.assertIn("a first reading, not every row whose file has one", text)

    def test_an_empty_group_prints_a_dash_not_none(self):
        s = {**_stats.compute(), "threshold_ranges": {}}
        values = build_docs.threshold_values(s)
        self.assertEqual(values["threshold_noul_low"], "—")
        self.assertEqual(values["threshold_choice_rows"], 0)

    def test_the_examples_keep_their_constants_and_say_what_they_are(self):
        four = (ROOT / "examples" / "04-tool-selection" / "main.py").read_text()
        self.assertIn("needs.noul < 0.5", four)
        self.assertIn("tool.confidence < 0.6", four)
        self.assertIn("unverified starting points", four)
        two = (ROOT / "examples" / "02-confidence-gate" / "main.py").read_text()
        self.assertEqual(lint_docs.DECIMAL_RANGE.findall(two), [])


class DecimalRangeTest(unittest.TestCase):
    def test_a_typed_range_is_rejected_and_a_generated_one_is_not(self):
        for text in (
            "ranging from 0.3 to 0.9.", "ranging from 0.3 to 0.9. A threshold", "cut at 0.55–0.8 here", "from .3 - .9", "阈值从 0.3 到 0.9 不等", "0.2 ~ 1.0",
        ):
            with self.subTest(text=text):
                self.assertEqual(len(lint_docs.check_decimal_ranges("x.md", text)), 1)
        for text in (
            "from <!--n:threshold_noul_low-->0.2<!--/n--> to <!--n:threshold_noul_high-->0.9<!--/n-->",
            "2–10 levels", "jev-1.13 to jev-1.14", "two options at 0.45/0.44", "a 0.9 threshold", "v0.1.0 to 0.2.0",
            "0.1 to 0.2.0", "0.3 to 0.9x",
            "<!-- shape:start -->\n0.3 to 0.9\n<!-- shape:end -->",
        ):
            with self.subTest(text=text):
                self.assertEqual(lint_docs.check_decimal_ranges("x.md", text), [])
        found = lint_docs.check_decimal_ranges("x.md", "line one\nranging from 0.3 to 0.9\n")
        self.assertTrue(found[0].startswith("x.md:2: typed decimal range '0.3 to 0.9'"), found)

    def test_main_reads_hand_written_docs_but_not_the_dated_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "docs").mkdir()
            (root / "notes.md").write_text("Thresholds range from 0.3 to 0.9.\n")
            (root / "llms.txt").write_text("from 0.4 to 0.8\n")
            (root / "docs" / "method.md").write_text("In 2026 the notes said 0.3 to 0.9.\n")
            files = ["notes.md", "llms.txt", "docs/method.md"]
            with (
                mock.patch.object(lint_docs, "ROOT", root),
                mock.patch.object(lint_docs, "hand_written_files", return_value=files),
                mock.patch.object(lint_docs, "fact_file_list", return_value=[]),
                mock.patch.object(lint_docs, "load_compat", return_value={}),
                mock.patch.object(lint_docs, "vendor_problems", return_value=[]),
                mock.patch.object(lint_docs, "check_pattern_docs", return_value=[]),
                mock.patch.object(lint_docs, "check_cjk_fallback", return_value=[]),
                mock.patch.object(lint_docs, "check_site_origin", return_value=[]),
                mock.patch("sys.stderr") as err,
            ):
                self.assertEqual(lint_docs.main([]), 1)
            printed = "".join(str(call.args[0]) for call in err.write.call_args_list)
            self.assertIn("notes.md:1: typed decimal range", printed)
            self.assertIn("llms.txt:1: typed decimal range", printed)
            self.assertNotIn("docs/method.md", printed)


class ReviewQueueTest(unittest.TestCase):
    def test_rows_no_person_read_are_listed_most_starred_band_first(self):
        catalogue = [
            entry("small", items=[item()], stars=3),
            entry("read", items=[item(read_on="2026-09-20")], stars=5000),
            entry("big", items=[item(), item(question_type="choice", compares="confidence", value=0.8, source="C = 0.8")], stars=2000),
        ]
        section = build_review_queue.thresholds_unread(catalogue)
        self.assertEqual(section.key, "thresholds-unread")
        self.assertIn(build_review_queue.thresholds_unread, build_review_queue.SECTIONS)
        slugs = [cells[0].split("]")[0].strip("[") for cells in section.rows]
        self.assertEqual(slugs, ["big", "small"])
        self.assertIn("`noul probability 0.55` `choice confidence 0.8`", section.rows[0][2])
        self.assertEqual(len(section.columns), len(section.rows[0]))
        self.assertIn("not recommendations", section.about_en)
        self.assertIn("不是推荐值", section.about_zh)


if __name__ == "__main__":
    unittest.main()
