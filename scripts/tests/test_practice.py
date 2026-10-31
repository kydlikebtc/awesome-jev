"""The practice reviews (K1, 2026-10-31): docs/practice/ pages whose prose a
model wrote and says so, and whose tables build_practice.py refills from
catalog.json. A recommended row must stay under its pattern and cite a file
someone read. No network."""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import build_docs  # noqa: E402
import build_practice  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]


class PracticeTest(unittest.TestCase):
    def test_every_page_renders_from_the_catalogue(self):
        # Rendered, not compared with the committed pages: like every other
        # generated file, a page may lag the catalogue until regenerate.py
        # runs on main (check_generated.py judges that, not this test).
        pages = build_practice.render()
        self.assertEqual({p.name for p in pages}, {f"{key}.md" for key in build_practice.PAGES} | {"README.md"})
        for path, text in pages.items():
            blocks = ("pages",) if path.name == "README.md" else ("readings", "primitives", "thresholds", "measured", "read")
            for block in blocks:
                body = text.split(f"<!-- {block}:start -->")[1].split(f"<!-- {block}:end -->")[0]
                self.assertTrue(body.strip(), f"{path.name}: {block} is empty")

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
        def row(slug: str, pattern: str, **evidence: str) -> dict:
            return {"slug": slug, "kind": "project", "patterns": [pattern], "url": f"https://github.com/o/{slug}",
                    "evidence": {"path": "a.py", "matched": ["y"], **evidence}}

        catalog = [row("read", "tool-selection", read_on="2026-09-22"), row("elsewhere", "content-scoring",
                   read_on="2026-09-22"), row("unread", "tool-selection")]
        self.assertIn("read by a person, 2026-09-22", build_practice.read_block("tool-selection", ("read",), catalog))
        with self.assertRaisesRegex(SystemExit, "not filed under tool-selection"):
            build_practice.read_block("tool-selection", ("elsewhere",), catalog)
        with self.assertRaisesRegex(SystemExit, "not in catalog.json"):
            build_practice.read_block("tool-selection", ("no-such-row",), catalog)
        with self.assertRaisesRegex(SystemExit, "cites no file anyone has read"):
            build_practice.read_block("tool-selection", ("unread",), catalog)

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
