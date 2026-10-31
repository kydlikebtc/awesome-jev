"""The monthly data release (D2, 2026-10-31): scripts/data_release.py's notes,
and data-release.yml's step run as GitHub runs it (`bash -e`) with stub `git`,
`python3` and `gh` on PATH. Also scripts/build_monthly.py's report (D1). No
network."""

from __future__ import annotations

import contextlib
import io
import json
import os
import pathlib
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "scripts"))

import build_monthly  # noqa: E402
import data_release  # noqa: E402
from test_weekly_jobs import run_block, step_lines  # noqa: E402

STEP = "Tag and release the month that ended"
GIT_STUB = """#!/bin/bash
echo "git $*" >> "$STUB_LOG"
case "$1 $2" in
  "rev-parse -q") [ -n "$STUB_TAGGED" ] && exit 0 || exit 1 ;;
  "tag --list") printf '%s' "$STUB_TAGS" ;;
  "rev-parse HEAD") echo abc123 ;;
esac
exit 0
"""
PYTHON_STUB = """#!/bin/bash
echo "python3 $*" >> "$STUB_LOG"
echo "the notes"
"""
GH_STUB = """#!/bin/bash
echo "gh $*" >> "$STUB_LOG"
"""


def rows(*slugs: str) -> list[dict]:
    return [{"slug": s} for s in slugs]


class NotesTest(unittest.TestCase):
    def test_what_arrived_and_what_was_retired_since_the_last_tag(self):
        text = data_release.notes(
            "catalog-2026-11", rows("a", "b", "c"), rows("old", "gone"),
            previous="catalog-2026-10", old_catalog=rows("a", "gone"), old_retired=rows("old"),
        )
        self.assertIn("**3** rows in `catalog.json` and **2** in `retired.json`", text)
        self.assertIn("**2** rows added, **1** retired", text)
        self.assertIn("Added · 新增: `b`, `c`", text)
        self.assertIn("Retired · 退役: `gone`", text)
        self.assertIn("releases/tag/catalog-2026-10", text)

    def test_the_first_release_says_so(self):
        text = data_release.notes("catalog-2026-10", rows("a"), [])
        self.assertIn("The first data release.", text)
        self.assertNotIn("Since", text)

    def test_long_lists_are_cut(self):
        many = [f"r{i:03d}" for i in range(80)]
        text = data_release.notes("catalog-2026-11", rows(*many), [], previous="catalog-2026-10",
                                  old_catalog=[], old_retired=[])
        self.assertIn(", and 20 more", text)

    def test_only_catalog_month_tags(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(data_release.main(["--tag", "awesome-jev-mcp-v0.2.0"]), 2)
            self.assertEqual(data_release.main(["--tag", "catalog-2026-13"]), 2)


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        (self.dir / "bin").mkdir()
        for name, body in (("git", GIT_STUB), ("python3", PYTHON_STUB), ("gh", GH_STUB)):
            stub = self.dir / "bin" / name
            stub.write_text(body)
            stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
        self.text = (WORKFLOWS / "data-release.yml").read_text()
        self.script = run_block(step_lines(self.text, STEP)).replace("/tmp/", f"{self.dir}/")
        self.log = self.dir / "log"

    def run_step(self, **env: str) -> list[str]:
        self.log.write_text("")
        full = {**os.environ, "PATH": f"{self.dir / 'bin'}{os.pathsep}{os.environ['PATH']}",
                "STUB_LOG": str(self.log), "STUB_TAGGED": "", "STUB_TAGS": "", **env}
        done = subprocess.run(["bash", "--noprofile", "--norc", "-e", "-c", self.script],
                              cwd=self.dir, env=full, capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        return self.log.read_text().splitlines()

    def test_the_month_that_ended_is_tagged_once(self):
        calls = self.run_step(STUB_TAGS="catalog-2026-09\ncatalog-2026-10\n")
        notes = next(c for c in calls if c.startswith("python3 "))
        self.assertRegex(notes, r"^python3 scripts/data_release.py --tag catalog-\d{4}-\d{2} --previous catalog-2026-09$")
        release = next(c for c in calls if c.startswith("gh release create"))
        self.assertIn("catalog.json retired.json schema/entry.schema.json --target abc123", release)
        self.assertIn(f"--notes-file {self.dir}/notes.md", release)

    def test_a_month_already_tagged_is_left_alone(self):
        calls = self.run_step(STUB_TAGGED="yes")
        self.assertFalse(any(c.startswith(("gh ", "python3 ")) for c in calls))

    def test_the_first_release_has_no_previous(self):
        calls = self.run_step()
        notes = next(c for c in calls if c.startswith("python3 "))
        self.assertNotIn("--previous", notes)

    def test_permissions_and_triggers(self):
        self.assertIn("  contents: write\n", self.text)
        self.assertNotIn("issues: write", self.text)
        self.assertIn('    - cron: "0 9 1 * *"\n', self.text)
        self.assertIn("fetch-depth: 0", self.text)
        self.assertEqual([l for l in self.text.splitlines() if "github.event" in l and not l.lstrip().startswith("#")], [])
        publish = (WORKFLOWS / "publish.yml").read_text()
        self.assertIn('"awesome-jev-mcp-v*"', publish, "a catalog-* tag never starts the PyPI publish")


def snapshot(date: str, entries: int, *, queue: int | None = None, stars: dict | None = None) -> dict:
    stats = {key: entries for key, _, _ in build_monthly.GROWTH}
    out = {"date": date, "stats": stats, "rows": [{"slug": s, "stars": n} for s, n in (stars or {}).items()]}
    if queue is not None:
        out["queue"] = {"open": queue}
    return out


class MonthlyTest(unittest.TestCase):
    HISTORY = [
        ("2026-10-28", snapshot("2026-10-28", 100, queue=400)),
        ("2026-11-04", snapshot("2026-11-04", 120, queue=390, stars={"big": 50})),
        ("2026-11-25", snapshot("2026-11-25", 160, queue=350, stars={"big": 90, "small": 2, "bench": 7})),
        ("2026-12-02", snapshot("2026-12-02", 170, queue=340)),
    ]
    CATALOG = [
        {"slug": "big", "kind": "project", "first_seen": "2026-11-03", "languages": ["python"],
         "platforms": ["typesafe-api"], "summary": "A big one.", "summary_zh": "大的。",
         "evidence": {"path": "a.py", "matched": ["x"], "model_read_on": "2026-11-03"}},
        {"slug": "small", "kind": "plugin", "first_seen": "2026-11-20", "languages": ["go"], "summary": "Small."},
        {"slug": "bench", "kind": "benchmark", "first_seen": "2026-11-21", "summary": "Measures.",
         "measurement": {"n": 1}, "evidence": {"path": "b.py", "matched": ["x"], "read_on": "2026-11-22"}},
        {"slug": "late", "kind": "project", "first_seen": "2026-11-29", "summary": "After the snapshot."},
        {"slug": "earlier", "kind": "project", "first_seen": "2026-10-10", "summary": "October."},
    ]
    RETIRED = [{"slug": "gone", "first_seen": "2026-09-01", "notes": "Retired 2026-11-12: the repository went away. More."}]

    def render(self) -> str:
        return build_monthly.render("2026-11", self.HISTORY, self.CATALOG, self.RETIRED, written="2026-12-03")

    def test_counts_run_from_the_snapshot_before_the_month_to_its_last(self):
        text = self.render()
        self.assertIn("| 2026-10-28 | 2026-11-25 | Change · 变化 |", text)
        self.assertIn("| Rows · 条目 | 100 | 160 | +60 |", text)
        self.assertIn("| Discovery candidates to read (issue #14) · 发现队列待读候选 | 400 | 350 | -50 |", text)

    def test_rows_added_retired_measured_and_starred(self):
        text = self.render()
        self.assertIn("## Rows added · 新增条目: 4", text)
        self.assertIn("| `project` | 2 |", text)
        self.assertIn("a person 1 · a model 1 · neither (a script's match only) 2", text)
        starred = text.split("## Most starred")[1].split("## Measurements")[0]
        self.assertLess(starred.index("#big"), starred.index("#bench"))
        self.assertIn("★90", starred, "the month's last snapshot's count, not today's")
        self.assertNotIn("#late", starred, "not in that snapshot")
        self.assertIn("  大的。", starred)
        self.assertIn("#bench", text.split("## Measurements")[1])
        self.assertIn("- `gone`: Retired 2026-11-12: the repository went away.", text)
        self.assertNotIn("#earlier", text)

    def test_written_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = pathlib.Path(tmp)
            history = folder / "history"
            history.mkdir()
            (folder / "catalog.json").write_text(json.dumps(self.CATALOG))
            (folder / "retired.json").write_text(json.dumps(self.RETIRED))
            argv = ["--month", "2026-11", "--dir", str(folder / "monthly"), "--history", str(history), "--root", str(folder)]
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()) as err:
                self.assertEqual(build_monthly.main(argv), 1, "no snapshot in the month")
                self.assertIn("no snapshot dated in 2026-11", err.getvalue())
                with mock.patch.object(build_monthly.snapshot_stats, "load_history", return_value=self.HISTORY):
                    self.assertEqual(build_monthly.main(argv), 0)
                    self.assertEqual(build_monthly.main(argv), 1, "a month's report is written once")
            self.assertIn("- [2026-11](2026-11.md)", (folder / "monthly" / "README.md").read_text())


if __name__ == "__main__":
    unittest.main()
