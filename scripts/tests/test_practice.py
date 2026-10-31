"""The practice reviews (K1, 2026-10-31): docs/practice/ pages whose prose a
model wrote and says so, and whose tables build_practice.py refills from
catalog.json. A recommended row must stay under its pattern and cite a file
someone read. No network."""

from __future__ import annotations

import contextlib
import io
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import _stats  # noqa: E402
import build_docs  # noqa: E402
import build_practice  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]


class PracticeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = _stats.load()[0]

    def test_the_committed_pages_are_current(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(build_practice.main(["--check"]), 0)

    def test_every_page_says_a_model_wrote_it(self):
        for key in build_practice.PAGES:
            text = (ROOT / "docs" / "practice" / f"{key}.md").read_text(encoding="utf-8")
            self.assertRegex(text, r"\*\*Written by a model on \d{4}-\d{2}-\d{2}\*\*", key)
            self.assertIn("由模型于", text, key)
            self.assertIn("## 要点（中文）", text, key)

    def test_each_recommended_row_is_named_in_the_prose(self):
        for key, picks in build_practice.PAGES.items():
            text = (ROOT / "docs" / "practice" / f"{key}.md").read_text(encoding="utf-8")
            prose = text.split("<!-- read:end -->")[1]
            for slug in picks:
                self.assertIn(f"**{slug}, `", prose, f"{key}: say why {slug} is worth reading")

    def test_a_pick_must_stay_under_its_pattern_and_be_read(self):
        with self.assertRaisesRegex(SystemExit, "not filed under tool-selection"):
            build_practice.read_block("tool-selection", ("gptcache",), self.catalog)
        with self.assertRaisesRegex(SystemExit, "not in catalog.json"):
            build_practice.read_block("tool-selection", ("no-such-row",), self.catalog)
        unread = [{"slug": "x", "kind": "project", "patterns": ["tool-selection"], "url": "https://github.com/o/x",
                   "evidence": {"path": "a.py", "matched": ["y"]}}]
        with self.assertRaisesRegex(SystemExit, "cites no file anyone has read"):
            build_practice.read_block("tool-selection", ("x",), unread)

    def test_the_patterns_page_links_only_written_reviews(self):
        self.assertIn("(practice/safety-gating.md)", build_docs.catalogued_block("safety-gating", 3, "en"))
        self.assertIn("(practice/safety-gating.md)", build_docs.catalogued_block("safety-gating", 3, "zh"))
        self.assertNotIn("practice/", build_docs.catalogued_block("recommendation", 3, "en"))

    def test_thresholds_are_listed_with_who_read_them(self):
        rows = [{"slug": "t", "kind": "project", "patterns": ["safety-gating"],
                 "observed_thresholds": [{"question_type": "noul", "compares": "probability", "value": 0.7,
                                          "decision": "at or above: deny", "source": "p >= 0.7",
                                          "model_read_on": "2026-10-28"}]}]
        block = build_practice.thresholds_block(rows)
        self.assertIn("| `noul` | probability | 0.7 | at or above: deny | a model, 2026-10-28 |", block)
        self.assertEqual(build_practice.thresholds_block([]), "None recorded on this pattern's rows.")


if __name__ == "__main__":
    unittest.main()
