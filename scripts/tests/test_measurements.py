"""A benchmark row's `measurement` and the page that sets them side by side (I44).

A kind: benchmark row may carry `measurement`: what its own author measured,
indexed field by field from the author's report. These tests pin the schema
and taxonomy to each other, every rule scripts/measurements.py keeps (through
lint, as a pull request meets them), the counts _stats publishes, and the
generated docs/benchmarks.md pair: every rendering of a direction says it is
author-stated and not reproduced here, and nothing on the page depends on the
catalogue's file order or on a star count moving inside its band. Pages are
rendered in memory, never read from the committed files: pull-request CI runs
these tests before it regenerates anything.
"""

from __future__ import annotations

import copy
import datetime as dt
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats
import build_benchmarks
import build_review_queue
import lint
import measurements
import regenerate
from readme import rows as readme_rows
from readme.strings import EN, ZH, ZH_MACHINE
from test_star_bands import LABELS as STAR_LABELS, moved_within_bands

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
TAXONOMY = json.loads((ROOT / "taxonomy.json").read_text())
PATTERNS = json.loads((ROOT / "patterns.json").read_text())["patterns"]
COMPAT = json.loads((ROOT / "compat.json").read_text())
CATALOG = json.loads((ROOT / "catalog.json").read_text())
TODAY = dt.date(2026, 9, 28)
QUALIFIERS = {"en": "author-stated, not reproduced here", "zh": "作者自述，未经本仓库复现"}

MEASURED = {
    "slug": "bench-row",
    "title": "Bench row",
    "summary": "A benchmark.",
    "summary_zh": "一个基准测试。",
    "url": "https://github.com/someone/bench-row",
    "kind": "benchmark",
    "patterns": ["search-ranking"],
    "stars": 12,
    "has_code": False,
    "measurement": {
        "task": "Rerank search results",
        "datasets": ["SciFact"],
        "comparators": ["Cohere Rerank 4 Pro"],
        "metrics": ["ranking", "latency"],
        "n": 300,
        "model_string": "jev-latest",
        "as_of": "2026-09-17",
        "direction": "mixed",
    },
    "first_seen": "2026-09-20",
    "sources": [{"catalog": "maintainer submission", "url": "https://github.com/kydlikebtc/awesome-jev"}],
    "license": "CC0-1.0",
}


def with_measurement(**changes) -> dict:
    """MEASURED with its measurement changed; a value of None removes that field."""
    out = copy.deepcopy(MEASURED)
    for key, value in changes.items():
        if value is None:
            out["measurement"].pop(key, None)
        else:
            out["measurement"][key] = value
    return out


def problems(entry: dict) -> list[str]:
    return measurements.row_problems(entry, TODAY)


class SchemaAndTaxonomyTest(unittest.TestCase):
    def test_directions_and_metrics_have_one_label_each(self):
        measurement = SCHEMA["properties"]["measurement"]["properties"]
        self.assertEqual(
            [d["key"] for d in TAXONOMY["measurement_directions"]], measurement["direction"]["enum"]
        )
        self.assertEqual([m["key"] for m in TAXONOMY["measurement_metrics"]], measurement["metrics"]["items"]["enum"])
        # The server and the site read the same four directions.
        self.assertEqual(list(measurements.load_query().DIRECTIONS), measurement["direction"]["enum"])
        core = (ROOT / "site" / "catalog-core.mjs").read_text()
        self.assertIn('export const DIRECTIONS = ["favourable", "mixed", "unfavourable", "inconclusive"];', core)

    def test_a_direction_or_metric_without_a_label_fails_lint(self):
        for path in (("direction",), ("metrics", "items")):
            with self.subTest(path=path):
                schema = copy.deepcopy(SCHEMA)
                node = schema["properties"]["measurement"]["properties"]
                for step in path:
                    node = node[step]
                node["enum"].append("brand-new")
                errors, _ = lint.check_taxonomy(schema, TAXONOMY)
                self.assertEqual(len(errors), 1, errors)
                self.assertIn("'brand-new' but it has no label", errors[0])

    def test_the_chinese_labels_say_a_model_wrote_them(self):
        for group in ("measurement_directions", "measurement_metrics"):
            for item in TAXONOMY[group]:
                with self.subTest(key=item["key"]):
                    self.assertIs(item.get("zh_machine"), True)

    def test_only_a_task_is_required_and_nothing_else_is_accepted(self):
        schema = SCHEMA["properties"]["measurement"]
        self.assertEqual(schema["required"], ["task"])
        self.assertIs(schema["additionalProperties"], False)
        self.assertIn("author-stated, not reproduced here", schema["properties"]["direction"]["description"].lower())
        bad = with_measurement(verdict="good")
        errors, _ = lint.validate(bad, SCHEMA, "catalog.json[0]")
        self.assertEqual(errors, ("catalog.json[0].measurement: unknown field 'verdict'",))


class RuleTest(unittest.TestCase):
    """scripts/measurements.py, one broken rule at a time, and lint's wiring of it."""

    def test_a_complete_row_passes(self):
        self.assertEqual(problems(MEASURED), [])
        self.assertEqual(measurements.row_problems({"slug": "x", "kind": "project"}, TODAY), [])

    def test_only_a_benchmark_may_carry_one(self):
        (found,) = problems({**MEASURED, "kind": "project"})
        self.assertIn("kind is 'project'", found)

    def test_a_measurement_is_dated_by_as_of_or_published(self):
        (found,) = problems(with_measurement(as_of=None))
        self.assertIn("no as_of and no published date", found)
        self.assertEqual(problems({**with_measurement(as_of=None), "published": "2026-09-17"}), [])

    def test_dates_are_real_and_not_in_the_future(self):
        for field in ("as_of", "read_on"):
            with self.subTest(field=field):
                (found,) = problems(with_measurement(**{field: "2026-02-30"}))
                self.assertEqual(found, f"measurement.{field} is not a valid date")
                (found,) = problems(with_measurement(**{field: "2026-09-29"}))
                self.assertEqual(found, f"measurement.{field} 2026-09-29 is in the future")
        self.assertEqual(problems(with_measurement(read_on="2026-09-28")), [])

    def test_nobody_reads_a_report_before_the_measurement(self):
        (found,) = problems(with_measurement(read_on="2026-09-16"))
        self.assertIn("read_on 2026-09-16 is before as_of 2026-09-17", found)
        self.assertEqual(problems(with_measurement(read_on="2026-09-17")), [])

    def test_lint_reports_row_problems_on_the_row(self):
        errors, _ = lint.check_entry_invariants({**MEASURED, "kind": "project"}, "catalog.json[4]", retired=False, today=TODAY)
        self.assertEqual(len([e for e in errors if "measurement" in e]), 1, errors)
        self.assertTrue(any(e.startswith("catalog.json[4]: bench-row: has a measurement") for e in errors), errors)

    def test_a_model_string_compat_json_does_not_list_is_an_error(self):
        for string in ("typesafe/jev-1", "jev-1.13", "gpt-6"):
            with self.subTest(string=string):
                (where, message), = measurements.model_problems([with_measurement(model_string=string)], [], COMPAT)
                self.assertEqual(where, "catalog.json[0]")
                self.assertIn(f"measurement.model_string {string!r} is not a string compat.json lists", message)
        for string in measurements.accepted_strings(COMPAT):
            with self.subTest(listed=string):
                self.assertEqual(measurements.model_problems([with_measurement(model_string=string)], [], COMPAT), [])
        (where, _), = measurements.model_problems([], [with_measurement(model_string="gpt-6")], COMPAT)
        self.assertEqual(where, "retired.json[0]")

    def test_compat_json_is_read_only_when_a_row_records_a_model_string(self):
        self.assertEqual(measurements.model_problems([with_measurement(model_string=None)], [], {}), [])

    def test_check_all_runs_the_model_string_rule(self):
        errors, _ = lint.check_all(SCHEMA, [with_measurement(model_string="gpt-6")], [])
        self.assertTrue(any("measurement.model_string 'gpt-6'" in e for e in errors), errors)


class RealCatalogueTest(unittest.TestCase):
    def test_every_measurement_is_on_a_benchmark_and_follows_the_rules(self):
        # The live catalogue can contain measurements newer than the fixtures.
        today = dt.date.today()
        measured = measurements.measured(CATALOG)
        self.assertGreaterEqual(len(measured), 20)
        for entry in measured:
            with self.subTest(slug=entry["slug"]):
                self.assertEqual(entry["kind"], "benchmark")
                self.assertEqual(measurements.row_problems(entry, today), [])
        self.assertEqual(measurements.model_problems(CATALOG, [], COMPAT), [])

    def test_the_model_read_backfill_claims_no_reading(self):
        # The fields first filled in on 2026-09-28 were read by a model, so no
        # row claims a person's reading (read_on) for them. When this test was
        # written, unread() meant "no read_on". Since 2026-10-24 a model that
        # reads a report records measurement.model_read_on instead, which
        # unread() also leaves out: that row moves to the review queue's model
        # section and is still nobody's reading but a model's.
        query = measurements.load_query()
        measured = measurements.measured(CATALOG)
        by_a_person = [e["slug"] for e in measured if query.read_by(query.measurement_of(e)) == query.PERSON]
        self.assertEqual(by_a_person, [])
        self.assertEqual(len(measurements.unread(CATALOG)) + len(measurements.model_read(CATALOG)), len(measured))

    def test_a_model_reading_of_a_report_is_not_a_persons(self):
        read = with_measurement(model_read_on="2026-09-20")
        self.assertEqual(measurements.unread([read]), [])
        self.assertEqual(measurements.model_read([read]), [read])
        self.assertEqual(measurements.unread([MEASURED]), [MEASURED])
        self.assertEqual(measurements.model_read([MEASURED]), [])

    def test_stats_count_what_the_rows_hold(self):
        stats = _stats.compute()
        self.assertEqual(stats["measured_rows"], len(measurements.measured(CATALOG)))
        self.assertEqual(stats["review_measurement_unread"], len(measurements.unread(CATALOG)))
        directions = stats["measurement_directions"]
        self.assertEqual(list(directions)[:4], ["favourable", "mixed", "unfavourable", "inconclusive"])
        self.assertEqual(sum(directions.values()), stats["measured_rows"])


class BenchmarksPageTest(unittest.TestCase):
    def render(self, catalog=None, lang="en") -> str:
        return build_benchmarks.render(CATALOG if catalog is None else catalog, PATTERNS, TAXONOMY, lang)

    def test_every_direction_shown_says_whose_it_is(self):
        for lang in ("en", "zh"):
            with self.subTest(lang=lang):
                page = self.render(lang=lang)
                labels = {d["en" if lang == "en" else "zh"] for d in TAXONOMY["measurement_directions"]}
                matrix_head = next(line for line in page.splitlines() if line.startswith("| Pattern") or line.startswith("| 模式"))
                for label in labels:
                    self.assertIn(f"{label} ({QUALIFIERS[lang]})", matrix_head)
                table_head = [line for line in page.splitlines() if line.startswith("| Row |") or line.startswith("| 行 |")]
                self.assertEqual(len(table_head), 1)
                self.assertIn(QUALIFIERS[lang], table_head[0])

    def test_the_chinese_page_says_a_model_wrote_it(self):
        page = self.render(lang="zh")
        self.assertIn("本页的中文说明由模型撰写（机翻）", page)
        self.assertNotIn("机翻", self.render(lang="en"))

    def test_every_measured_row_its_comparators_and_datasets_are_listed(self):
        page = self.render()
        for entry in measurements.measured(CATALOG):
            with self.subTest(slug=entry["slug"]):
                self.assertIn(f"#{entry['slug']})", page)
                for name in entry["measurement"].get("comparators", []) + entry["measurement"].get("datasets", []):
                    self.assertIn(f"| {readme_rows.esc(name)} |", page)

    def test_file_order_and_stars_within_a_band_change_nothing(self):
        for lang in ("en", "zh"):
            with self.subTest(lang=lang):
                page = self.render(lang=lang)
                self.assertEqual(self.render(list(reversed(CATALOG)), lang), page)
                for how in ("low", "high", "random"):
                    self.assertEqual(self.render(moved_within_bands(CATALOG, how), lang), page)

    def star_cells(self, page: str) -> list[str]:
        """The Stars cell of each row in the table of every measured report."""
        lines = page.splitlines()
        head = next(i for i, line in enumerate(lines) if line.startswith(("| Row |", "| 行 |")))
        cells = []
        for line in lines[head + 2 :]:
            if not line.startswith("| "):
                break
            cells.append(line.split(" | ")[1])
        return cells

    def test_no_exact_star_count_and_no_age(self):
        # The Stars column is read cell by cell, against the band labels. A
        # search of the whole page for "| 24 |" also matched jev-dspy-lab's n
        # of 24, and failed the weekly refresh of 2026-10-07 when
        # jev-benchmarks reached 24 stars; the copy below pins that case.
        colliding = copy.deepcopy(CATALOG)
        rows = measurements.measured(colliding)
        rows[0]["stars"] = next(e["measurement"]["n"] for e in rows if (e["measurement"].get("n") or 0) >= 10)
        for catalog in (CATALOG, colliding):
            for lang in ("en", "zh"):
                with self.subTest(lang=lang, colliding=catalog is colliding):
                    cells = self.star_cells(self.render(catalog, lang))
                    self.assertEqual(len(cells), len(measurements.measured(catalog)))
                    self.assertLessEqual(set(cells), {*STAR_LABELS, "—"})
        page = self.render()
        for word in ("days ago", "today", "yesterday", "weeks ago"):
            self.assertNotIn(word, page.lower())

    def test_a_catalogue_without_measurements_says_so(self):
        bare = [{k: v for k, v in e.items() if k != "measurement"} for e in CATALOG]
        self.assertIn("No benchmark row carries a measurement yet.", self.render(bare))

    def test_registered_as_a_generator_and_generated_output(self):
        self.assertIn("build_benchmarks.py", [script for script, _ in regenerate.GENERATORS])
        for path in ("docs/benchmarks.md", "docs/benchmarks.zh-CN.md"):
            with self.subTest(path=path):
                self.assertIn(path, regenerate.OUTPUTS)
                self.assertIn(f"/{path} linguist-generated", (ROOT / ".gitattributes").read_text())
        import lint_docs

        self.assertTrue(lint_docs.generated("docs/benchmarks.md"))
        self.assertTrue(lint_docs.generated("docs/benchmarks.zh-CN.md"))


class ReviewQueueTest(unittest.TestCase):
    def test_unread_measurements_are_listed_and_a_reading_takes_one_off(self):
        section = build_review_queue.measurement_unread([MEASURED])
        self.assertEqual(section.key, "measurement-unread")
        self.assertEqual(len(section.rows), 1)
        self.assertIn("`mixed`", section.rows[0][2])
        read = with_measurement(read_on="2026-09-28")
        self.assertEqual(build_review_queue.measurement_unread([read]).rows, ())
        self.assertIn(build_review_queue.measurement_unread, build_review_queue.SECTIONS)


class RowRenderingTest(unittest.TestCase):
    """README and pattern-page rows show the author's direction, with whose it is."""

    def test_a_direction_bit_on_every_row_that_records_one(self):
        for strings, lang in ((EN, "en"), (ZH, "zh")):
            with self.subTest(lang=lang):
                bit = readme_rows.direction_bit(MEASURED, strings)
                self.assertIn(QUALIFIERS[lang], bit)
                label = next(d["en" if lang == "en" else "zh"] for d in TAXONOMY["measurement_directions"] if d["key"] == "mixed")
                self.assertIn(label, bit)
                self.assertIn(bit, "\n".join(readme_rows.entry_list([MEASURED], strings)))
                self.assertEqual(readme_rows.direction_bit(with_measurement(direction=None), strings), "")

    def test_the_note_explains_it_and_is_marked_where_a_model_wrote_it(self):
        self.assertIn("direction_note", ZH_MACHINE)
        self.assertTrue(readme_rows.direction_note(ZH, docs="docs/").endswith(" <sub>(机翻)</sub>"))
        en = readme_rows.direction_note(EN, docs="../")
        self.assertIn("](../benchmarks.md)", en)
        self.assertIn("author-stated, not reproduced here", en)


if __name__ == "__main__":
    unittest.main()
