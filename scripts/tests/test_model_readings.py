"""A model's reading, recorded apart from a person's (C2, since 2026-10-24).

`read_on` and `patterns_reviewed` date a person's reading. `model_read_on`
(on `evidence`, `measurement`, each `wire.source` item and each
`observed_thresholds` item) and `patterns_model_read_on` date a model's, and
`summary_source: model-written` marks a summary a model wrote. These tests pin
the one rule every surface follows (the MCP package's query.py reading()), the
helpers that sort each record into read by a person, only by a model, or by
nobody, the review queue's section for a model's work, and what the surfaces
print: never a model's reading as a person's, and a person's wherever both
are recorded. Rows are made up, apart from the last class; nothing here reads
a generated file.
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import _stats  # noqa: E402
import build_benchmarks  # noqa: E402
import build_compat  # noqa: E402
import build_review_queue  # noqa: E402
import measurements  # noqa: E402
import thresholds  # noqa: E402
import wire  # noqa: E402
from platform_values import load_query  # noqa: E402
from readme import rows as readme_rows  # noqa: E402
from readme.strings import EN, ZH  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
CATALOG = json.loads((ROOT / "catalog.json").read_text())
QUERY = load_query()

PERSON_DAY, MODEL_DAY = "2026-10-24", "2026-10-20"
MEASUREMENT = {"task": "Route tickets", "as_of": "2026-10-01"}
THRESHOLD = {"question_type": "noul", "compares": "probability", "value": 0.5, "decision": "at or above: act",
             "source": "P = 0.5"}


def row(slug: str, **fields) -> dict:
    base = {"slug": slug, "title": slug.title(), "url": f"https://github.com/o/{slug}", "kind": "project",
            "patterns": ["tool-selection"], "summary": f"{slug} does it.", "stars": 50}
    return {**base, **fields}


def evidence(**reading) -> dict:
    return {"path": "src/main.py", "matched": ["jev"], **reading}


def slugs(entries) -> list[str]:
    return [e["slug"] for e in entries]


class OneRuleTest(unittest.TestCase):
    def test_a_persons_reading_supersedes_a_models(self):
        self.assertEqual(QUERY.reading({"read_on": PERSON_DAY, "model_read_on": MODEL_DAY}), (QUERY.PERSON, PERSON_DAY))
        self.assertEqual(QUERY.reading({"model_read_on": MODEL_DAY}), (QUERY.MODEL, MODEL_DAY))
        for nothing in ({}, None, PERSON_DAY, ["read_on"], {"read_on": ""}):
            with self.subTest(record=nothing):
                self.assertIsNone(QUERY.reading(nothing))
                self.assertIsNone(QUERY.read_by(nothing))
        model = row("p", patterns_model_read_on=MODEL_DAY)
        self.assertEqual(QUERY.patterns_reading(model), (QUERY.MODEL, MODEL_DAY))
        both = row("p", patterns_reviewed=PERSON_DAY, patterns_model_read_on=MODEL_DAY)
        self.assertEqual(QUERY.patterns_reading(both), (QUERY.PERSON, PERSON_DAY))

    def test_every_record_that_takes_a_persons_reading_takes_a_models(self):
        props = SCHEMA["properties"]
        records = {
            "evidence": props["evidence"]["properties"],
            "measurement": props["measurement"]["properties"],
            "wire.source": props["wire"]["properties"]["source"]["items"]["properties"],
            "observed_thresholds": props["observed_thresholds"]["items"]["properties"],
        }
        for name, fields in records.items():
            with self.subTest(record=name):
                self.assertEqual(fields[QUERY.MODEL_READ_ON]["pattern"], fields[QUERY.READ_ON]["pattern"])
                self.assertIn("model_read_on", fields[QUERY.READ_ON]["description"])
        self.assertEqual(props[QUERY.PATTERNS_MODEL_READ]["pattern"], props[QUERY.PATTERNS_READ]["pattern"])
        self.assertIn("model-written", props["summary_source"]["enum"])
        # The scripts that check the dates name the same two fields.
        self.assertEqual(wire.READINGS, (QUERY.READ_ON, QUERY.MODEL_READ_ON))
        self.assertEqual(thresholds.READINGS, {QUERY.READ_ON, QUERY.MODEL_READ_ON})
        self.assertEqual(measurements.DATED[1:], (QUERY.READ_ON, QUERY.MODEL_READ_ON))

    def test_primitives_are_the_reading_of_whoever_read_the_call_site(self):
        named = ["noul"]
        model = row("m", question_types=named, evidence=evidence(model_read_on=MODEL_DAY))
        self.assertEqual(QUERY.primitives_read_by(model), QUERY.MODEL)
        both = row("p", question_types=named, evidence=evidence(read_on=PERSON_DAY, model_read_on=MODEL_DAY))
        self.assertEqual(QUERY.primitives_read_by(both), QUERY.PERSON)
        # What the field has meant from the start: a person's.
        self.assertEqual(QUERY.primitives_read_by(row("undated", question_types=named, evidence=evidence())), QUERY.PERSON)
        self.assertEqual(QUERY.primitives_read_by(row("uncited", question_types=named)), QUERY.PERSON)
        self.assertIsNone(QUERY.primitives_read_by(row("none", evidence=evidence(model_read_on=MODEL_DAY))))


class SortingTest(unittest.TestCase):
    """Each record is read by a person, only by a model, or by nobody: in one list, never two."""

    def test_measurements(self):
        rows = [
            row("nobody", kind="benchmark", measurement=dict(MEASUREMENT)),
            row("model", kind="benchmark", measurement={**MEASUREMENT, "model_read_on": MODEL_DAY}),
            row("person", kind="benchmark", measurement={**MEASUREMENT, "read_on": PERSON_DAY}),
            row("both", kind="benchmark", measurement={**MEASUREMENT, "read_on": PERSON_DAY, "model_read_on": MODEL_DAY}),
        ]
        self.assertEqual(slugs(measurements.unread(rows)), ["nobody"])
        self.assertEqual(slugs(measurements.model_read(rows)), ["model"])

    def test_a_model_cannot_read_a_report_before_the_measurement_either(self):
        early = row("early", kind="benchmark", measurement={**MEASUREMENT, "model_read_on": "2026-09-30"})
        (found,) = measurements.row_problems(early, dt.date(2026, 10, 24))
        self.assertIn("measurement.model_read_on 2026-09-30 is before as_of 2026-10-01", found)
        (found,) = measurements.row_problems(row("late", kind="benchmark", measurement={
            **MEASUREMENT, "model_read_on": "2026-10-25"}), dt.date(2026, 10, 24))
        self.assertEqual(found, "measurement.model_read_on 2026-10-25 is in the future")

    def test_thresholds(self):
        rows = [
            row("nobody", observed_thresholds=[dict(THRESHOLD)]),
            row("model", observed_thresholds=[{**THRESHOLD, "model_read_on": MODEL_DAY}]),
            row("half", observed_thresholds=[{**THRESHOLD, "model_read_on": MODEL_DAY}, dict(THRESHOLD)]),
            row("mixed", observed_thresholds=[{**THRESHOLD, "model_read_on": MODEL_DAY}, {**THRESHOLD, "read_on": PERSON_DAY}]),
            row("person", observed_thresholds=[{**THRESHOLD, "read_on": PERSON_DAY}]),
            row("none"),
        ]
        self.assertEqual(slugs(thresholds.unread(rows)), ["nobody", "half"])
        self.assertEqual(slugs(thresholds.model_read(rows)), ["model", "mixed"])

    def test_wire(self):
        def alt(slug, *items):
            return row(slug, kind="alternative", wire={"weights": "open", "source": [
                {"path": f"{i}.py", "matched": ["x"], **item} for i, item in enumerate(items)]})

        rows = [
            alt("nobody", {}),
            alt("model", {"model_read_on": MODEL_DAY}),
            alt("half", {"model_read_on": MODEL_DAY}, {}),
            alt("mixed", {"read_on": PERSON_DAY}, {"model_read_on": MODEL_DAY}),
            alt("person", {"read_on": PERSON_DAY}),
        ]
        self.assertEqual(slugs(wire.unread(rows)), ["nobody", "half"])
        self.assertEqual(slugs(wire.model_read(rows)), ["model", "mixed"])

    def test_patterns_and_the_not_yet_indexed_list(self):
        unplaced = row("u", patterns=["overview"], has_code=True)
        self.assertTrue(_stats.not_indexed_by_pattern(unplaced))
        self.assertFalse(_stats.not_indexed_by_pattern({**unplaced, "patterns_model_read_on": MODEL_DAY}))
        self.assertFalse(_stats.patterns_match_rules({**unplaced, "patterns_model_read_on": MODEL_DAY}))

    def test_the_counts_take_a_record_off_once_a_person_reads_it(self):
        rows = [
            row("a", patterns_model_read_on=MODEL_DAY, evidence=evidence(model_read_on=MODEL_DAY)),
            row("b", patterns_model_read_on=MODEL_DAY, patterns_reviewed=PERSON_DAY,
                evidence=evidence(model_read_on=MODEL_DAY, read_on=PERSON_DAY)),
            row("c", kind="benchmark", measurement={**MEASUREMENT, "model_read_on": MODEL_DAY}),
        ]
        self.assertEqual(_stats.model_read_counts(rows),
                         {"patterns": 1, "evidence": 1, "measurement": 1, "wire": 0, "thresholds": 0})


class ReviewQueueTest(unittest.TestCase):
    def test_a_models_work_waits_in_its_own_section_in_band_order(self):
        catalog = [
            row("small", stars=5, summary_source="model-written"),
            row("big", stars=5000, question_types=["noul"], evidence=evidence(model_read_on=MODEL_DAY),
                patterns_model_read_on=MODEL_DAY),
            row("checked", stars=900, evidence=evidence(model_read_on=MODEL_DAY, read_on=PERSON_DAY),
                summary_source="curated", patterns_model_read_on=MODEL_DAY, patterns_reviewed=PERSON_DAY),
            row("bench", stars=100, kind="benchmark", measurement={**MEASUREMENT, "model_read_on": MODEL_DAY}),
        ]
        section = build_review_queue.model_read(catalog)
        self.assertEqual(section.key, "model-read")
        self.assertEqual([r[0].split("]")[0] for r in section.rows], ["[big", "[bench", "[small"])
        self.assertEqual(section.rows[0][2],
                         f"`patterns` {MODEL_DAY} · `call site` {MODEL_DAY} · `question_types`")
        self.assertEqual(section.rows[1][2], f"`measurement` {MODEL_DAY}")
        self.assertEqual(section.rows[2][2], "`summary`")
        self.assertIs(build_review_queue.SECTIONS[-1], build_review_queue.model_read)

    def test_a_model_read_record_leaves_the_unread_sections(self):
        model = row("bench", kind="benchmark", measurement={**MEASUREMENT, "model_read_on": MODEL_DAY},
                    observed_thresholds=[{**THRESHOLD, "model_read_on": MODEL_DAY}])
        self.assertEqual(build_review_queue.measurement_unread([model]).rows, ())
        self.assertEqual(build_review_queue.thresholds_unread([model]).rows, ())
        self.assertEqual(len(build_review_queue.model_read([model]).rows), 1)

    def test_how_to_take_a_row_off_names_the_persons_fields(self):
        section = build_review_queue.model_read([])
        for field in ("patterns_reviewed", "evidence.read_on", "measurement.read_on", "`curated`"):
            self.assertIn(field, section.leave_en)
            self.assertIn(field, section.leave_zh)


class SurfaceTest(unittest.TestCase):
    """Where a date is printed, whose reading it is goes with it."""

    def test_a_readme_row_says_a_model_read_the_call_site(self):
        model = row("m", evidence=evidence(model_read_on=MODEL_DAY))
        self.assertTrue(readme_rows.call_site(model, EN).endswith(f", read by a model {MODEL_DAY}"))
        self.assertTrue(readme_rows.call_site(model, ZH).endswith(f"，{MODEL_DAY} 模型阅读"))
        both = row("p", evidence=evidence(model_read_on=MODEL_DAY, read_on=PERSON_DAY))
        self.assertTrue(readme_rows.call_site(both, EN).endswith(f", read {PERSON_DAY}"))
        self.assertNotIn(MODEL_DAY, readme_rows.call_site(both, EN))

    def test_the_compatibility_table_says_whose_reading_in_words(self):
        def read_in(*items):
            record = {"source": [{"path": f"{i}.py", "matched": ["x"], **item} for i, item in enumerate(items)]}
            return build_compat.read_in(row("a", kind="alternative"), record)

        self.assertTrue(read_in({"read_on": PERSON_DAY}).endswith(f"(read by a person on {PERSON_DAY})"))
        self.assertTrue(read_in({"model_read_on": MODEL_DAY}).endswith(
            f"(read by a model on {MODEL_DAY}, not yet checked by a person)"))
        self.assertTrue(read_in({"read_on": PERSON_DAY}, {"model_read_on": MODEL_DAY}).endswith(
            f"(partly read by a person on {PERSON_DAY}, the rest by a model on {MODEL_DAY})"))
        self.assertTrue(read_in({"model_read_on": MODEL_DAY}, {}).endswith("(not yet read by a person)"))

    def test_the_benchmark_pages_mark_a_models_date(self):
        model = {**MEASUREMENT, "model_read_on": MODEL_DAY}
        self.assertEqual(build_benchmarks.read_cell(model, "en"), f"{MODEL_DAY} *(model)*")
        self.assertEqual(build_benchmarks.read_cell(model, "zh"), f"{MODEL_DAY} *（模型）*")
        self.assertEqual(build_benchmarks.read_cell({**model, "read_on": PERSON_DAY}, "en"), PERSON_DAY)
        self.assertEqual(build_benchmarks.read_cell(MEASUREMENT, "en"), "—")
        catalog = [
            row("m", kind="benchmark", measurement=model),
            row("p", kind="benchmark", measurement={**MEASUREMENT, "read_on": PERSON_DAY}),
            row("n", kind="benchmark", measurement=dict(MEASUREMENT)),
        ]
        patterns = json.loads((ROOT / "patterns.json").read_text())["patterns"]
        taxonomy = json.loads((ROOT / "taxonomy.json").read_text())
        page = build_benchmarks.render(catalog, patterns, taxonomy, "en")
        self.assertIn("Of those, a person has read **1** against their report (`measurement.read_on`) and only "
                      "a model **1** (`measurement.model_read_on`); a script or a model filled in the other **1**",
                      page)
        self.assertIn(f"| {MODEL_DAY} *(model)* |", page)

    def test_an_agent_is_told_whose_reading_it_gets(self):
        model = row("m", question_types=["noul"], evidence=evidence(model_read_on=MODEL_DAY),
                    patterns_model_read_on=MODEL_DAY, summary_source="model-written")
        out = QUERY.compact(model)
        self.assertEqual(out["patterns_model_read_on"], MODEL_DAY)
        self.assertNotIn("patterns_reviewed", out)
        self.assertEqual(out["question_types_read_by"], QUERY.MODEL)
        self.assertEqual(out["summary_source"], "model-written")
        person = row("p", question_types=["noul"], evidence=evidence(read_on=PERSON_DAY))
        self.assertNotIn("question_types_read_by", QUERY.compact(person))
        self.assertIn("model-written by a model", QUERY.TEXT_NOTE)


class RealCatalogueTest(unittest.TestCase):
    SAID = re.compile(r"by an AI assistant that read the README and the cited file on (\d{4}-\d{2}-\d{2})")

    def test_rows_whose_notes_say_a_model_read_them_record_it_as_a_models(self):
        drafted = [(e, m.group(1)) for e in CATALOG if (m := self.SAID.search(e.get("notes") or ""))]
        self.assertGreaterEqual(len(drafted), 42)
        for entry, day in drafted:
            with self.subTest(slug=entry["slug"]):
                # Until a person reads it, and records that, it is a model's.
                if "read_on" not in entry["evidence"]:
                    self.assertEqual(entry["evidence"].get("model_read_on"), day)
                self.assertIn(entry.get("summary_source"), ("model-written", "curated"))

    def test_every_model_reading_is_a_real_past_date(self):
        today = dt.date.today()
        for entry in CATALOG:
            for record in (entry.get("evidence"), QUERY.measurement_of(entry), *thresholds.recorded(entry),
                           *wire.sources(wire.wire_of(entry) or {})):
                if isinstance(record, dict) and "model_read_on" in record:
                    with self.subTest(slug=entry["slug"]):
                        self.assertLessEqual(dt.date.fromisoformat(record["model_read_on"]), today)


if __name__ == "__main__":
    unittest.main()
