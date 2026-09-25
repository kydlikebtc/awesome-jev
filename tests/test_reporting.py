"""Regression checks for catalogue reporting; no network or live API calls."""

from __future__ import annotations

import pathlib
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

import _stats
import build_docs
import build_readme
import lint_docs


class CoverageReportingTests(unittest.TestCase):
    def test_coverage_changes_when_first_entry_arrives(self):
        counts = {"retry-control": 6, "recommendation": 0}
        before = {"by_pattern": counts}
        self.assertIn("`recommendation`", build_readme.coverage_note(before, "en"))
        self.assertIn("未收录不代表", build_readme.coverage_note(before, "zh"))

        after = {"by_pattern": {**counts, "recommendation": 1}}
        self.assertIn("All 2 patterns", build_readme.coverage_note(after, "en"))
        self.assertNotIn("no entries", build_readme.coverage_note(after, "en"))
        self.assertIn("全部 2 个模式", build_readme.coverage_note(after, "zh"))

    def test_empty_taxonomy_does_not_claim_complete_coverage(self):
        empty = {"by_pattern": {}}
        self.assertIn("not reported", build_readme.coverage_note(empty, "en"))
        self.assertIn("暂不报告", build_readme.coverage_note(empty, "zh"))

    def test_empty_kind_does_not_imply_empty_patterns(self):
        stats = {
            "by_pattern": {"recommendation": 1},
            "entries": 1,
            "empty_kinds": ["case-study"],
        }
        patterns = [{"key": "recommendation", "blurb_en": "Recommend from a shortlist."}]
        rendered = build_docs.gaps_block(stats, patterns)
        self.assertIn("Every pattern has at least one entry", rendered)
        self.assertIn("**`case-study`**", rendered)
        self.assertNotIn("nobody has published", rendered)
        self.assertNotIn("No entries yet", rendered)

    def test_handwritten_gap_counts_are_rejected_in_both_languages(self):
        for text in ("Two patterns have no examples yet.", "有两个模式目前没有例子。"):
            with self.subTest(text=text):
                self.assertTrue(lint_docs.check_bare_counts("docs/example.md", text))
                generated = "<!-- gaps:start -->\n" + text + "\n<!-- gaps:end -->"
                self.assertEqual(lint_docs.check_bare_counts("docs/example.md", generated), [])


class VerificationReportingTests(unittest.TestCase):
    def test_success_status_requires_a_date(self):
        self.assertFalse(_stats.link_ok({"link_status": 200}))
        self.assertFalse(_stats.link_ok({"checked": "2026-09-24", "link_status": 403}))
        self.assertTrue(_stats.link_ok({"checked": "2026-09-22", "link_status": 200}))

    def test_citation_without_check_result_is_reported_only_as_a_record(self):
        entry = {
            "slug": "example",
            "title": "Example",
            "url": "https://example.com/repo",
            "summary": "A cited implementation, not a runtime test.",
            "summary_zh": "有调用点记录，未经运行测试。",
            "kind": "project",
            "patterns": ["tool-selection"],
            "license": "CC0-1.0",
            "evidence": {"path": "main.py", "matched": ["system_one"], "read_on": "2026-09-01"},
        }
        patterns = [{"key": "tool-selection"}, {"key": "recommendation"}]
        schema = {"properties": {"kind": {"enum": ["project", "case-study"]}}}
        # There is deliberately no CI result or runtime record in this fixture.
        with patch.object(_stats, "load", return_value=([entry], [], patterns, {"platforms": []}, schema)):
            stats = _stats.compute()
        self.assertEqual(stats["evidence_rows"], 1)
        self.assertEqual(stats["link_ok"], 0)
        self.assertEqual(stats["last_sweep"], "never")

        with patch.object(_stats, "compute", return_value=stats), patch.object(build_readme, "START_HERE", []):
            english = build_readme.render([entry], [], build_readme.EN, "2026-09-24")
            chinese = build_readme.render([entry], [], build_readme.ZH, "2026-09-24")
        self.assertIn("evidence%20recorded-1", english)
        self.assertIn("**not latest CI passes**", english)
        self.assertIn("including entries without `code-untested`", english)
        self.assertIn("不是最新 CI 通过数", chinese)
        self.assertIn("没有 `code-untested` 标签也不代表已测试", chinese)
        self.assertIn("`recommendation`", english)
        self.assertNotIn("verified examples", _stats.pitch(stats))
        self.assertNotIn("verified examples", build_docs.meta_block(stats))


if __name__ == "__main__":
    unittest.main()
