"""What the MCP server says about a benchmark's measurement (I44).

A kind: benchmark row may carry `measurement`: what its own author measured,
indexed from the author's report. search_examples filters on who a benchmark
compared Jev with, on which dataset, and on the direction its author states;
every answer that shows a direction says it is author-stated and not
reproduced here. Tested on made-up rows through query.py, as
tests/test_mcp_query.py tests the rest.
"""

from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from awesome_jev_mcp import query  # noqa: E402

PATTERNS = [{"key": "search-ranking", "en": "Search & ranking", "blurb_en": "Which result first."}]


def row(slug: str, **fields) -> dict:
    base = {"slug": slug, "title": slug, "url": f"https://github.com/o/{slug}", "summary": "s",
            "kind": "benchmark", "patterns": ["search-ranking"], "has_code": True}
    return {**base, **fields}


ROWS = [
    row("rerank", stars=50, measurement={"task": "Rerank", "datasets": ["SciFact", "NFCorpus"],
                                         "comparators": ["Cohere Rerank 4 Pro"], "direction": "mixed"}),
    row("memory", stars=40, measurement={"task": "Recall", "datasets": ["LongMemEval"],
                                         "comparators": ["local cross-encoder"], "direction": "unfavourable"}),
    row("undirected", stars=30, measurement={"task": "Classify", "comparators": ["GPT-6 Astra"]}),
    row("plain", stars=20),
]


def slugs(answer: dict) -> list[str]:
    return [r["slug"] for r in answer["results"]]


class MeasurementAnswerTest(unittest.TestCase):
    def search(self, **filters) -> dict:
        return query.search(ROWS, PATTERNS, **filters)

    def test_a_measured_row_carries_its_measurement_and_whose_direction_it_is(self):
        results = {r["slug"]: r for r in self.search()["results"]}
        self.assertEqual(results["rerank"]["measurement"]["direction_note"], "author-stated, not reproduced here")
        self.assertEqual(results["rerank"]["measurement"]["task"], "Rerank")
        self.assertNotIn("direction_note", results["undirected"]["measurement"])
        self.assertNotIn("measurement", results["plain"])
        # The row as filed is not changed by showing it.
        self.assertNotIn("direction_note", ROWS[0]["measurement"])

    def test_the_answer_says_what_the_fields_are_only_when_a_measured_row_is_shown(self):
        self.assertEqual(self.search()["measurement_note"], query.MEASUREMENT_NOTE)
        self.assertIn("not reproduced here", query.MEASUREMENT_NOTE)
        self.assertNotIn("measurement_note", self.search(query="plain"))

    def test_comparator_and_dataset_match_a_fragment_ignoring_case(self):
        self.assertEqual(slugs(self.search(comparator="cohere")), ["rerank"])
        self.assertEqual(slugs(self.search(comparator=" CROSS-encoder ")), ["memory"])
        self.assertEqual(slugs(self.search(dataset="longmem")), ["memory"])
        self.assertEqual(slugs(self.search(dataset="nfcorpus")), ["rerank"])
        self.assertEqual(self.search(dataset="BEIR")["total_matching"], 0)
        # A blank filter filters nothing.
        self.assertEqual(self.search(comparator="  ")["total_matching"], len(ROWS))

    def test_direction_matches_exactly_and_an_unknown_one_lists_the_valid_ones(self):
        self.assertEqual(slugs(self.search(direction="unfavourable")), ["memory"])
        self.assertEqual(slugs(self.search(direction="mixed")), ["rerank"])
        wrong = self.search(direction="negative")
        self.assertEqual(wrong["valid_directions"], list(query.DIRECTIONS))
        self.assertIn("not a verdict", wrong["hint"])

    def test_get_example_marks_the_direction_too(self):
        answer = query.find_example(ROWS, "memory")
        self.assertEqual(answer["measurement"]["direction_note"], query.DIRECTION_NOTE)
        self.assertEqual(query.find_example(ROWS, "plain"), {**ROWS[3], "text_note": query.TEXT_NOTE})

    def test_independent_report_is_a_benchmark_without_the_vendor_flag(self):
        self.assertTrue(query.is_independent_report(ROWS[0]))
        self.assertFalse(query.is_independent_report({**ROWS[0], "flags": ["vendor-reported"]}))
        self.assertFalse(query.is_independent_report({**ROWS[0], "kind": "project"}))


if __name__ == "__main__":
    unittest.main()
