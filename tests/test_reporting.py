"""Regression checks for catalogue reporting; no network or live API calls."""

from __future__ import annotations

import pathlib
import tempfile
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

import _stats
import assemble_site
import build_docs
import build_readme
import lint_docs
from readme import sections


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

    def test_sweep_coverage_counts_the_rows_that_share_the_newest_date(self):
        # max(checked) alone said 2026-09-24 while 67 rows still carried the
        # 23rd; how many rows share the newest date is the other half of it.
        def row(slug, checked, status):
            return {"slug": slug, "kind": "project", "patterns": [], "checked": checked, "link_status": status}

        rows = [
            row("a", "2026-09-24", 200),
            row("b", "2026-09-24", 200),
            row("c", "2026-09-23", 200),
            row("d", "2026-09-25", 403),  # a date without a 2xx is not a successful check
            row("e", None, None),
            row("f", "2026-09-24", 404),  # nor on the newest date
        ]
        schema = {"properties": {"kind": {"enum": ["project"]}}}
        with patch.object(_stats, "load", return_value=(rows, [], [], {"platforms": []}, schema)):
            stats = _stats.compute()
        self.assertEqual((stats["last_sweep"], stats["sweep_coverage"]), ("2026-09-24", 2))
        self.assertIn("| Rows whose latest successful check is on that date | 2 of 6 |", build_docs.shape_block(stats))
        self.assertEqual(build_docs.inline_values(stats)["sweep_coverage"], 2)
        with patch.object(_stats, "load", return_value=([row("e", None, None)], [], [], {"platforms": []}, schema)):
            never = _stats.compute()
        self.assertEqual((never["last_sweep"], never["sweep_coverage"]), ("never", 0))

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
        # One count per evidence.kind (I18); a record without kind is a call site.
        self.assertEqual(stats["call_site_rows"], 1)
        self.assertEqual(stats["wire_shape_rows"], 0)
        self.assertEqual(stats["example_only_rows"], 0)
        self.assertEqual(stats["link_ok"], 0)
        self.assertEqual(stats["last_sweep"], "never")

        with patch.object(_stats, "compute", return_value=stats), patch.object(sections, "START_HERE", []):
            english = build_readme.render([entry], [], build_readme.EN)
            chinese = build_readme.render([entry], [], build_readme.ZH)
        self.assertIn("1 call-site citation records", english)
        self.assertIn("**not latest CI passes**", english)
        self.assertIn("including entries without `code-untested`", english)
        self.assertIn("不是最新 CI 通过数", chinese)
        self.assertIn("没有 `code-untested` 标签也不代表已测试", chinese)
        self.assertIn("`recommendation`", english)
        self.assertNotIn("verified examples", _stats.pitch_public(stats))
        self.assertNotIn("verified examples", assemble_site.meta_block(stats))


class ReadmePreviewTests(unittest.TestCase):
    def test_style_only_change_invalidates_the_preview_url(self):
        paths = [
            "site/index.html", "site/catalog.css", "site/catalog-core.mjs",
            "site/favicon.svg", "site/fonts/fonts.css", "scripts/render_images.py", "scripts/_stats.py",
            "catalog.json", "collections.json", "compat.json", "patterns.json", "taxonomy.json",
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            for path in paths:
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("unchanged")
            with patch.object(sections, "ROOT", root):
                before = build_readme.preview_version()
                self.assertEqual(before, build_readme.preview_version())
                (root / "site/catalog.css").write_text("new layout")
                self.assertNotEqual(before, build_readme.preview_version())


if __name__ == "__main__":
    unittest.main()
