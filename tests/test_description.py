"""The public pitch is rounded, and its drift is reported rather than failed (I07).

The GitHub repository description is the one published sentence CI cannot
rewrite: editing it needs admin rights no workflow token has. It used to quote
the exact entry count, so every merged row turned `main` red until someone ran
`gh repo edit` by hand; then the count floored to the hundred, which still
changed about weekly. Since 2026-11-05 it states no count, shared with the
site's og:description, and a separate push-only workflow files an issue
carrying the exact command instead of failing lint. No network here.
"""

from __future__ import annotations

import contextlib
import io
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import _stats
import assemble_site
import check_description


class PublicCountTest(unittest.TestCase):
    def test_floors_to_the_hundred_with_a_plus(self):
        for entries, shown in ((1207, "1,200+"), (1200, "1,200+"), (1199, "1,100+"), (805, "800+"), (100, "100+")):
            with self.subTest(entries=entries):
                self.assertEqual(_stats.public_count(entries), shown)

    def test_a_small_catalogue_is_stated_exactly(self):
        # Flooring 42 to "0+" would be true and useless.
        self.assertEqual(_stats.public_count(42), "42")

    def test_next_change_is_the_next_hundred(self):
        self.assertEqual(_stats.next_public_change(1207), 1300)
        self.assertEqual(_stats.next_public_change(1299), 1300)
        self.assertEqual(_stats.next_public_change(1300), 1400)
        self.assertEqual(_stats.next_public_change(42), 43)

    def test_the_pitch_states_no_count(self):
        # Since 2026-11-05: a count, even floored, changed weekly and waited for an admin.
        pitches = {_stats.pitch_public({"entries": n}) for n in (42, 1201, 1299, 1300, 99999)}
        self.assertEqual(len(pitches), 1)
        pitch = pitches.pop()
        self.assertTrue(pitch.startswith("Public resources for Jev"), pitch)
        self.assertNotRegex(pitch, r"\d{2,}")
        self.assertNotIn("verified examples", pitch)

    def test_site_meta_description_is_the_same_rounded_sentence(self):
        meta = assemble_site.meta_block({"entries": 1207})
        pitch = _stats.pitch_public({"entries": 1207}).replace("'", "&#x27;")
        self.assertIn(f'<meta name="description" content="{pitch}" />', meta)
        self.assertIn(f'<meta property="og:description" content="{pitch}" />', meta)


class EditCommandTest(unittest.TestCase):
    def test_command_is_paste_ready(self):
        pitch = _stats.pitch_public({"entries": 1207})
        command = check_description.edit_command(pitch)
        self.assertTrue(command.startswith(f'gh repo edit {check_description.SELF} --description "'))
        self.assertIn("TypeSafe AI's", command)
        # Round-trips through a real shell to exactly the pitch.
        out = subprocess.run(
            ["bash", "-c", command.replace(f"gh repo edit {check_description.SELF} --description ", "printf %s ", 1)],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        self.assertEqual(out, pitch)

    def test_shell_specials_are_escaped(self):
        command = check_description.edit_command('a "b" $HOME `x` \\')
        out = subprocess.run(
            ["bash", "-c", command.replace(f"gh repo edit {check_description.SELF} --description ", "printf %s ", 1)],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        self.assertEqual(out, 'a "b" $HOME `x` \\')


class CheckDescriptionTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        self.output = self.dir / "output"
        self.summary = self.dir / "summary"
        self.report = self.dir / "report.md"
        self.expected = _stats.pitch_public({"entries": 1207})

    def run_check(self, published, argv=(), has_token=True):
        env = {"GITHUB_OUTPUT": str(self.output), "GITHUB_STEP_SUMMARY": str(self.summary)}
        out = io.StringIO()
        with patch.dict(os.environ, env), patch.object(
            check_description._stats, "compute", return_value={"entries": 1207}
        ), patch.object(check_description, "token", return_value="t" if has_token else ""), patch.object(
            check_description, "api_get", return_value=published
        ), patch.object(check_description, "report_social_preview"), contextlib.redirect_stdout(out):
            code = check_description.main(list(argv))
        return code, out.getvalue()

    def status(self):
        return self.output.read_text() if self.output.exists() else ""

    def test_match_passes_and_reports_match(self):
        code, out = self.run_check({"description": self.expected}, ["--report", str(self.report)])
        self.assertEqual(code, 0)
        self.assertIn("status=match", self.status())
        self.assertFalse(self.report.exists())
        self.assertIn("the pitch states no count", out)

    def test_adding_rows_is_never_drift(self):
        code, _ = self.run_check({"description": _stats.pitch_public({"entries": 4321})})
        self.assertEqual(code, 0)

    def test_drift_for_a_person_exits_non_zero_with_the_command(self):
        code, out = self.run_check({"description": "1207 public resources for Jev"})
        self.assertEqual(code, 1)
        self.assertIn(check_description.edit_command(self.expected), out)
        self.assertIn("status=drift", self.status())

    def test_drift_in_ci_warns_writes_the_issue_and_stays_green(self):
        code, out = self.run_check({"description": "1207 public resources for Jev"}, ["--report", str(self.report)])
        self.assertEqual(code, 0)
        self.assertIn("::warning", out)
        self.assertIn("status=drift", self.status())
        body = self.report.read_text()
        self.assertIn(check_description.edit_command(self.expected), body)
        self.assertIn("1207 public resources for Jev", body)
        self.assertIn(self.expected, body)
        self.assertIn(check_description.edit_command(self.expected), self.summary.read_text())

    def test_stale_report_from_an_earlier_run_is_removed(self):
        self.report.write_text("old")
        self.run_check({"description": self.expected}, ["--report", str(self.report)])
        self.assertFalse(self.report.exists())

    def test_no_token_or_no_answer_is_skipped_never_drift(self):
        code, out = self.run_check(None, ["--report", str(self.report)], has_token=False)
        self.assertEqual(code, 0)
        self.assertIn("skipped", out)
        self.assertIn(self.expected, out)
        self.assertIn("status=skipped", self.status())
        self.output.unlink()
        code, _ = self.run_check(None, ["--report", str(self.report)])
        self.assertEqual(code, 0)
        self.assertIn("status=skipped", self.status())
        self.assertFalse(self.report.exists())

    def test_a_refused_read_is_skipped_never_drift(self):
        # _github.api_get returns this for a 403 that names no rate limit.
        blocked = {"blocked": True, "status": 403, "message": "Resource not accessible by integration"}
        code, out = self.run_check(blocked, ["--report", str(self.report)])
        self.assertEqual(code, 0)
        self.assertIn("skipped", out)
        self.assertIn("status=skipped", self.status())
        self.assertFalse(self.report.exists())


class WorkflowWiringTest(unittest.TestCase):
    """Lint's checks stay read-only and never check what they cannot fix.
    (Its one write-scoped job, `regenerate`, is covered by
    scripts/tests/test_check_generated.py.)"""

    def test_lint_no_longer_checks_the_live_description(self):
        lint = (ROOT / ".github/workflows/lint.yml").read_text()
        self.assertNotIn("check_description", lint)
        self.assertNotIn("issues: write", lint)
        self.assertIn("permissions:\n  contents: read\n", lint)

    def test_description_workflow_is_push_only_and_may_file_issues(self):
        text = (ROOT / ".github/workflows/description.yml").read_text()
        self.assertIn("python3 scripts/check_description.py --report", text)
        self.assertIn("permissions:\n  contents: read\n  issues: write\n", text)
        self.assertIn("  push:\n    branches: [main]\n", text)
        self.assertIn("  workflow_dispatch:\n", text)
        self.assertNotIn("pull_request", text)
        self.assertIn("--label description", text)
        # A dispatch from a branch must not open or close the issue.
        self.assertIn("    if: github.ref == 'refs/heads/main'\n", text)
        # No event payload reaches a shell.
        self.assertNotIn("github.event", text.split("\non:")[1])

    def test_counts_previews_the_description(self):
        out = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "counts.py")], capture_output=True, text=True, check=True
        ).stdout
        entries = len(__import__("json").loads((ROOT / "catalog.json").read_text()))
        self.assertIn(_stats.pitch_public({"entries": entries}), out)
        self.assertIn("it states no count", out)


class IssueStepsTest(unittest.TestCase):
    """The two issue steps of description.yml, run under bash with a stub `gh`.

    Every push to main reaches them while the description is stale, so they
    must file one issue, stay quiet while the fix is unchanged, speak up when
    it changes, and close the issue on the first match. Nothing reaches GitHub.
    """

    WORKFLOW = ROOT / ".github" / "workflows" / "description.yml"
    STUB = "\n".join(
        [
            "#!/usr/bin/env bash",
            'printf "%s\\n" "$*" >> "$GH_LOG"',
            'case "$1 $2" in',
            '  "issue list") printf "%s\\n" "$GH_EXISTING" ;;',
            '  "issue view") printf "%s\\n" "$GH_SEEN"; exit "${GH_VIEW_EXIT:-0}" ;;',
            "esac",
            "",
        ]
    )

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        stub = self.dir / "gh"
        stub.write_text(self.STUB)
        stub.chmod(0o755)
        self.log = self.dir / "gh.log"
        self.report = self.dir / "description.md"
        self.expected = _stats.pitch_public({"entries": 1207})
        self.fix = check_description.edit_command(self.expected)
        self.report.write_text(check_description.issue_body("1207 public resources", self.expected, 1207) + "\n")

    def step(self, name: str) -> str:
        """The run: block of the named step, dedented."""
        lines = self.WORKFLOW.read_text().splitlines()
        start = lines.index(f"      - name: {name}")
        run = next(i for i in range(start, len(lines)) if lines[i] == "        run: |")
        body = []
        for line in lines[run + 1 :]:
            if line.strip() and not line.startswith(" " * 10):
                break
            body.append(line[10:])
        return "\n".join(body).replace("/tmp/description.md", str(self.report))

    def run_step(self, name: str, existing: str = "", seen: str = "", view_exit: int = 0):
        env = {
            **os.environ,
            "PATH": f"{self.dir}{os.pathsep}{os.environ['PATH']}",
            "GH_LOG": str(self.log),
            "GH_EXISTING": existing,
            "GH_SEEN": seen,
            "GH_VIEW_EXIT": str(view_exit),
        }
        # The shell GitHub runs a `run:` block in.
        done = subprocess.run(
            ["bash", "--noprofile", "--norc", "-eo", "pipefail", "-c", self.step(name)],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(done.returncode, 0, done.stderr)
        calls = self.log.read_text().splitlines() if self.log.exists() else []
        return calls, done.stdout

    def verbs(self, calls):
        return [" ".join(c.split()[:2]) for c in calls]

    def test_first_drift_files_one_labelled_issue(self):
        calls, _ = self.run_step("Open or update the description issue")
        self.assertEqual(self.verbs(calls), ["label create", "issue list", "issue create"])
        self.assertIn("--label description", calls[-1])
        self.assertIn(str(self.report), calls[-1])

    def test_unchanged_drift_does_not_comment_again(self):
        # GitHub may hand bodies back with CRLF line endings.
        seen = (self.report.read_text()).replace("\n", "\r\n")
        calls, out = self.run_step("Open or update the description issue", existing="7", seen=seen)
        self.assertEqual(self.verbs(calls), ["label create", "issue list", "issue view"])
        self.assertIn("#7 already carries this command", out)

    def test_a_changed_fix_is_commented(self):
        # The fix an earlier wording asked for (before 2026-11-05 the pitch carried a count).
        stale = check_description.issue_body("x", "1,100+ public resources for Jev, TypeSafe AI's System One", 1107)
        self.assertNotIn(self.fix, stale)
        calls, _ = self.run_step("Open or update the description issue", existing="7", seen=stale)
        self.assertEqual(self.verbs(calls), ["label create", "issue list", "issue view", "issue comment"])
        self.assertTrue(calls[-1].startswith("issue comment 7 --body-file"), calls[-1])

    def test_an_unreadable_issue_is_commented_rather_than_skipped(self):
        calls, _ = self.run_step("Open or update the description issue", existing="7", view_exit=1)
        self.assertEqual(self.verbs(calls)[-1], "issue comment")

    def test_a_match_closes_the_open_issue_and_nothing_else(self):
        calls, _ = self.run_step("Close the description issue once it matches", existing="7")
        self.assertEqual(self.verbs(calls), ["issue list", "issue close"])
        self.assertTrue(calls[-1].startswith("issue close 7"), calls[-1])
        self.log.unlink()
        calls, _ = self.run_step("Close the description issue once it matches")
        self.assertEqual(self.verbs(calls), ["issue list"])


if __name__ == "__main__":
    unittest.main()
