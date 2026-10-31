"""Only files written whole by a generator are marked linguist-generated (I01).

GitHub collapses a linguist-generated file's diff in a pull request. That is
right for the READMEs, the pattern pages and the figures, and wrong for a
hand-written doc that merely carries generated marker blocks: its prose would
be hidden from the reviewer who is meant to read it.
"""

from __future__ import annotations

import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def attribute(*paths: str) -> dict[str, str]:
    out = subprocess.run(
        ["git", "check-attr", "linguist-generated", "--", *paths],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return {line.split(": ")[0]: line.split(": ")[-1] for line in out.splitlines()}


def tracked(*patterns: str) -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "--", *patterns], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return out.split()


class GitattributesTest(unittest.TestCase):
    def test_fully_generated_files_are_marked(self):
        paths = [
            "README.md", "README.zh-CN.md", "docs/measured.md", "docs/measured.zh-CN.md",
            "docs/review-queue.md", "docs/zh-queue.md", "examples/index.json",
            "docs/benchmarks.md", "docs/benchmarks.zh-CN.md", "docs/shape.md", "docs/shape.zh-CN.md",
            *tracked("docs/by-pattern", "docs/assets"),
        ]
        self.assertGreater(len(paths), 20)
        unmarked = [path for path, value in attribute(*paths).items() if value != "set"]
        self.assertEqual(unmarked, [])

    def test_hand_written_files_with_marker_blocks_are_not(self):
        paths = [
            "docs/status.md", "docs/sources.md", "docs/patterns.md", "docs/patterns.zh-CN.md", "docs/compatibility.md",
            "llms.txt",
            "site/index.html", "examples/README.md", "skills/awesome-jev/SKILL.md", "src/awesome_jev_mcp/README.md",
            "catalog.json", "CONTRIBUTING.md", *tracked("docs/practice"),
        ]
        marked = [path for path, value in attribute(*paths).items() if value != "unspecified"]
        self.assertEqual(marked, [])


if __name__ == "__main__":
    unittest.main()
