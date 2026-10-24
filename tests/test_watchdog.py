"""The watchdog (A4, 2026-10-24): scripts/watchdog.py's verdicts on each
scheduled workflow, and watchdog.yml's issue step, run as GitHub runs it
(`bash -e`, no pipefail) with a stub `gh` on PATH. Also the links workflow,
which since the same day reports dead links through an issue and goes red only
when the sweep crashes. No network."""

from __future__ import annotations

import contextlib
import datetime as dt
import io
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

import watchdog  # noqa: E402
from test_discover_workflow import GH_STUB  # noqa: E402
from test_weekly_jobs import run_block, step_lines  # noqa: E402

NOW = dt.datetime(2026, 10, 24, 8, tzinfo=dt.timezone.utc)


def event_values(text: str) -> list[str]:
    """Lines outside comments that name a `github.event` value."""
    return [line for line in text.splitlines() if "github.event" in line and not line.lstrip().startswith("#")]


def run(days_ago: float, conclusion: str = "success") -> dict:
    created = (NOW - dt.timedelta(days=days_ago)).isoformat().replace("+00:00", "Z")
    return {"created_at": created, "conclusion": conclusion, "status": "completed", "html_url": "https://x/run"}


def seen(name="links.yml", state="active", latest=None, success=None) -> dict:
    return {"name": name, "state": state, "url": f"https://github.com/o/r/actions/workflows/{name}",
            "latest": latest, "success": success}


class VerdictTest(unittest.TestCase):
    def test_the_scheduled_workflows_are_found_by_their_files(self):
        names = watchdog.scheduled()
        for name in ("claims.yml", "discover.yml", "links.yml", "metadata.yml"):
            self.assertIn(name, names)
        self.assertNotIn("watchdog.yml", names, "it cannot report its own silence")
        self.assertNotIn("lint.yml", names)
        self.assertIn("  schedule:\n", (WORKFLOWS / "watchdog.yml").read_text())

    def test_a_recent_success_is_healthy_whatever_came_after(self):
        self.assertIsNone(watchdog.problem(seen(latest=run(1, "failure"), success=run(7.9)), NOW))

    def test_what_needs_a_person(self):
        cases = {
            "no run of it has ever succeeded": seen(latest=run(5, "failure")),
            "no run of it has succeeded in the last 8 days": seen(latest=run(1, "failure"), success=run(8.1)),
            "after 60 days without repository activity": seen(state="disabled_inactivity", success=run(1)),
            "it is disabled manually": seen(state="disabled_manually", success=run(1)),
        }
        for words, item in cases.items():
            with self.subTest(words=words):
                self.assertIn(words, watchdog.problem(item, NOW))

    def test_the_body_quotes_dates_not_ages(self):
        found = [(seen("claims.yml", success=run(4), latest=run(4)), None),
                 (seen(latest=run(5, "failure")), "no run of it has ever succeeded")]
        body = watchdog.markdown(found)
        rows = [line for line in body.splitlines() if line.startswith("| [")]
        self.assertTrue(rows[0].startswith("| [links]("), "the one that needs a person comes first")
        self.assertIn("| never | 2026-10-19, failure ([run](https://x/run)) | no run of it has ever succeeded |", rows[0])
        self.assertIn("| 2026-10-20 |", rows[1])
        self.assertNotIn("days ago", body)
        self.assertIn("1 of 2 need a person", body)


class MainTest(unittest.TestCase):
    def run_main(self, answers: dict[str, dict]) -> tuple[int, str, str]:
        with tempfile.TemporaryDirectory() as tmp:
            body = pathlib.Path(tmp) / "body.md"
            out = io.StringIO()

            def look(name, repo):
                if isinstance(answers[name], BaseException):
                    raise answers[name]
                return answers[name]

            with mock.patch.object(watchdog, "scheduled", return_value=sorted(answers)), \
                 mock.patch.object(watchdog, "look", look), \
                 mock.patch.object(watchdog.dt, "datetime", wraps=dt.datetime) as clock, \
                 mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}), \
                 contextlib.redirect_stdout(out):
                clock.now.return_value = NOW
                code = watchdog.main(["--markdown", str(body)])
            return code, out.getvalue(), body.read_text() if body.exists() else ""

    def test_healthy_is_exit_0(self):
        code, out, body = self.run_main({"claims.yml": seen("claims.yml", success=run(2), latest=run(2))})
        self.assertEqual(code, 0)
        self.assertTrue(out.rstrip().endswith("watchdog: 1 scheduled workflow(s), 0 need a person"))
        self.assertIn("| nothing |", body)

    def test_a_stopped_workflow_is_exit_1(self):
        code, out, _ = self.run_main({
            "claims.yml": seen("claims.yml", success=run(2), latest=run(2)),
            "links.yml": seen(latest=run(5, "failure")),
        })
        self.assertEqual(code, 1)
        self.assertIn("STOP links.yml", out)

    def test_an_unreadable_api_judges_nothing(self):
        code, out, body = self.run_main({"links.yml": watchdog.Unreadable("links.yml: no answer")})
        self.assertEqual(code, 2)
        self.assertIn("::error title=Watchdog could not read the Actions API::", out)
        self.assertEqual(body, "")


class IssueStepTest(unittest.TestCase):
    NAME = "Open, rewrite or close the watchdog issue"

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        stub = self.dir / "bin" / "gh"
        stub.parent.mkdir()
        stub.write_text(GH_STUB)
        stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
        self.log = self.dir / "gh.log"
        self.lines = step_lines((WORKFLOWS / "watchdog.yml").read_text(), self.NAME)
        self.script = run_block(self.lines).replace("/tmp/", f"{self.dir}/")

    def run_step(self, code: str, existing: str = "", current: str = "") -> list[str]:
        (self.dir / "body.md").write_text("the body\n")
        self.log.write_text("")
        env = {**os.environ, "PATH": f"{self.dir / 'bin'}{os.pathsep}{os.environ['PATH']}",
               "STUB_LOG": str(self.log), "STUB_EXISTING": existing, "STUB_MISSING": "",
               "STUB_CURRENT": current, "CODE": code}
        done = subprocess.run(["bash", "--noprofile", "--norc", "-e", "-c", self.script],
                              cwd=self.dir, env=env, capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        return [line for line in self.log.read_text().splitlines()
                if not line.startswith(("label create", "issue list"))]

    def test_a_stopped_workflow_opens_one_issue(self):
        calls = self.run_step("1")
        self.assertEqual(len(calls), 1)
        self.assertTrue(calls[0].startswith("issue create --title A scheduled workflow has stopped succeeding --label watchdog"))

    def test_an_open_issue_is_rewritten_only_when_it_would_change(self):
        self.assertEqual(self.run_step("1", existing="40", current="an older body"),
                         ["issue view 40 --json body --jq .body", f"issue edit 40 --body-file {self.dir}/body.md"])
        self.assertEqual(self.run_step("1", existing="40", current="the body\r"),
                         ["issue view 40 --json body --jq .body"])

    def test_health_closes_the_issue_and_is_otherwise_quiet(self):
        closed = self.run_step("0", existing="40")
        self.assertEqual(len(closed), 1)
        self.assertTrue(closed[0].startswith("issue close 40 --comment"))
        self.assertEqual(self.run_step("0"), [])

    def test_no_event_value_reaches_the_shell(self):
        text = (WORKFLOWS / "watchdog.yml").read_text()
        self.assertEqual(event_values(text), [])
        self.assertIn("  actions: read\n", text)
        self.assertNotIn("contents: write", text)


LINKS_STUB = """#!/bin/bash
# Plays check_links.py --markdown FILE: STUB_EXIT is its exit code;
# STUB_REPORT=no crashes before the counts, as a traceback would.
[ "$1 $2" = "scripts/check_links.py --markdown" ] || { echo "unexpected: $*" >&2; exit 9; }
if [ "$STUB_REPORT" = "no" ]; then
  echo "Traceback (most recent call last):" >&2
  exit "$STUB_EXIT"
fi
echo "### Dead links (1)" > "$3"
echo "refused: 0 of 1 GitHub URLs (0%), 0 of 0 on other hosts (-)"
echo "links: 1 checked: 0 answered 2xx, 0 redirected, 0 refused, 1 dead"
exit "$STUB_EXIT"
"""


class LinksWorkflowTest(unittest.TestCase):
    """links.yml: the sweep's alarms reach an issue, and only a crash is red."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        (self.dir / "bin").mkdir()
        for name, body in (("python3", LINKS_STUB), ("gh", GH_STUB)):
            stub = self.dir / "bin" / name
            stub.write_text(body)
            stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
        self.text = (WORKFLOWS / "links.yml").read_text()

    def run_step(self, name: str, **env: str) -> subprocess.CompletedProcess:
        script = run_block(step_lines(self.text, name)).replace("/tmp/", f"{self.dir}/")
        full = {**os.environ, "PATH": f"{self.dir / 'bin'}{os.pathsep}{os.environ['PATH']}",
                "GITHUB_OUTPUT": str(self.dir / "output"), "STUB_LOG": str(self.dir / "gh.log"),
                "STUB_EXISTING": "", "STUB_MISSING": "", "STUB_CURRENT": "", **env}
        (self.dir / "output").write_text("")
        (self.dir / "gh.log").write_text("")
        return subprocess.run(["bash", "--noprofile", "--norc", "-e", "-c", script],
                              cwd=self.dir, env=full, capture_output=True, text=True)

    def test_the_sweep_has_a_token_and_writes_the_body(self):
        lines = step_lines(self.text, "Sweep links")
        self.assertIn("          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}", lines)
        self.assertIn("check_links.py --markdown /tmp/body.md", run_block(lines))
        self.assertIn("  issues: write\n", self.text)
        self.assertNotIn("contents: write", self.text)
        self.assertEqual(event_values(self.text), [])

    def test_alarms_are_handed_to_the_issue_and_the_run_stays_green(self):
        for code in ("0", "1", "3"):
            with self.subTest(exit=code):
                done = self.run_step("Sweep links", STUB_EXIT=code, STUB_REPORT="yes")
                self.assertEqual(done.returncode, 0, done.stderr)
                self.assertIn("links: 1 checked", done.stdout)
                self.assertEqual((self.dir / "output").read_text(), f"code={code}\n")

    def test_a_crash_before_the_counts_is_red(self):
        done = self.run_step("Sweep links", STUB_EXIT="1", STUB_REPORT="no")
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("::error title=Link sweep stopped::", done.stdout)

    def test_the_issue_step_runs_on_either_alarm(self):
        lines = step_lines(self.text, "Open or update the links issue")
        condition = next(line for line in lines if line.strip().startswith("if:"))
        self.assertEqual(condition.strip(),
                         "if: steps.sweep.outputs.code == '1' || steps.sweep.outputs.code == '3'")

    def test_the_issue_is_opened_once_then_commented_on(self):
        (self.dir / "body.md").write_text("### Dead links (1)\n")
        name = "Open or update the links issue"
        self.assertEqual(self.run_step(name).returncode, 0)
        calls = [c for c in (self.dir / "gh.log").read_text().splitlines() if c.startswith("issue")]
        self.assertTrue(calls[-1].startswith("issue create --title Dead links found by the weekly sweep --label links"))
        self.assertEqual(self.run_step(name, STUB_EXISTING="41").returncode, 0)
        calls = [c for c in (self.dir / "gh.log").read_text().splitlines() if c.startswith("issue")]
        self.assertEqual(calls[-1], f"issue comment 41 --body-file {self.dir}/body.md")


if __name__ == "__main__":
    unittest.main()
