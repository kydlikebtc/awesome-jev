"""The weekly GitHub-reading workflows (links, metadata, claims) as I10 left
them: the sweep has a token, metadata no longer swallows the sweep's counts
with `|| true`, the logs are kept, and the notice fires on what the refresh
digest says. Shell steps run as GitHub runs them — `bash -e`, no pipefail — with
a stub python3 on PATH. No network."""

from __future__ import annotations

import os
import pathlib
import re
import stat
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
sys.path.insert(0, str(ROOT / "scripts"))

import refresh_metadata  # noqa: E402


def step_lines(text: str, name: str) -> list[str]:
    """Every line of one step, from its `- name:` to the next step."""
    lines = text.splitlines()
    start = lines.index(f"      - name: {name}")
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("      - ") or lines[i].startswith("      # ")),
        len(lines),
    )
    return lines[start:end]


def run_block(lines: list[str]) -> str:
    """The step's `run: |` body, dedented."""
    at = lines.index("        run: |")
    return "\n".join(line[10:] for line in lines[at + 1 :] if line.startswith(" " * 10) or not line.strip())


STUB = """#!/bin/bash
# Plays check_links.py: STUB_EXIT is its exit code; STUB_REPORT=no crashes
# before the counts, as a traceback would.
if [ "$STUB_REPORT" = "no" ]; then
  echo "Traceback (most recent call last):" >&2
  exit "$STUB_EXIT"
fi
echo "  ok   200  some-row"
echo "refused: 0 of 1 GitHub URLs (0%), 0 of 0 on other hosts (-)"
echo "links: 1 checked: 1 answered 2xx (stamped), 0 redirected, 0 refused, 0 dead"
exit "$STUB_EXIT"
"""


# links.yml itself, which since 2026-10-24 reports through an issue, is
# tested in tests/test_watchdog.py beside the watchdog that watches it.


class MetadataStampTest(unittest.TestCase):
    NAME = "Stamp every link that still answers"

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        stub = self.dir / "bin" / "python3"
        stub.parent.mkdir()
        stub.write_text(STUB)
        stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
        text = (WORKFLOWS / "metadata.yml").read_text()
        self.lines = step_lines(text, self.NAME)
        self.script = run_block(self.lines).replace("/tmp/", f"{self.dir}/")

    def run_step(self, exit_code: int, report: bool = True) -> subprocess.CompletedProcess:
        env = {
            **os.environ,
            "PATH": f"{self.dir / 'bin'}{os.pathsep}{os.environ['PATH']}",
            "STUB_EXIT": str(exit_code),
            "STUB_REPORT": "yes" if report else "no",
        }
        return subprocess.run(
            ["bash", "--noprofile", "--norc", "-e", "-c", self.script],
            cwd=self.dir, env=env, capture_output=True, text=True,
        )

    def test_counts_are_no_longer_swallowed(self):
        body = "\n".join(self.lines)
        self.assertIn("check_links.py --write", body)
        self.assertNotIn("|| true", body)
        self.assertNotIn("tail -5", body)

    def test_alarms_do_not_stop_the_refresh_and_their_counts_are_shown(self):
        for code in (0, 1, 3):
            with self.subTest(exit=code):
                done = self.run_step(code)
                self.assertEqual(done.returncode, 0, done.stderr)
                self.assertIn("links: 1 checked", done.stdout)
                self.assertIn(f"check_links.py exit {code}", done.stdout)

    def test_a_crash_before_the_counts_fails_the_step(self):
        for code in (1, 2):
            with self.subTest(exit=code):
                done = self.run_step(code, report=False)
                self.assertNotEqual(done.returncode, 0)
                self.assertIn("::error title=Link sweep stopped::", done.stdout)


class MetadataLogsTest(unittest.TestCase):
    def test_logs_are_kept_even_when_a_step_fails(self):
        text = (WORKFLOWS / "metadata.yml").read_text()
        lines = step_lines(text, "Keep the sweep and refresh logs")
        body = "\n".join(lines)
        self.assertIn("        if: always()", lines)
        self.assertIn("        uses: actions/upload-artifact@v7", lines)
        for path in ("/tmp/links.log", "/tmp/refresh.log", "/tmp/signals.log", "/tmp/sources.log", "/tmp/digest.md"):
            self.assertIn(f"            {path}", lines, path)
        self.assertIn("if-no-files-found: ignore", body)
        order = [text.index(f"      - name: {name}") for name in (
            "Refresh stars, licences and archive status",
            "Keep the sweep and refresh logs",
            "Rebuild everything generated from those facts, and commit it here",
        )]
        self.assertEqual(order, sorted(order))

    def test_the_notice_fires_on_what_the_digest_says(self):
        text = (WORKFLOWS / "metadata.yml").read_text()
        grep = next(line for line in text.splitlines() if "grep -qE" in line and "digest.md" in line)
        pattern = grep.split('"')[1]
        quiet = refresh_metadata.digest([], [], 3)
        blocked = refresh_metadata.digest(
            [], [], 3, blocked=[{"slug": "s", "repo": "a/b", "detail": "HTTP 403: blocked"}]
        )
        skipped = refresh_metadata.digest([], [], 3, skipped=2)
        gone = refresh_metadata.digest([], ["s (a/b)"], 3)
        self.assertIsNone(re.search(pattern, quiet), "stars alone land silently")
        for name, body in (("blocked", blocked), ("skipped", skipped), ("gone", gone)):
            with self.subTest(case=name):
                self.assertIsNotNone(re.search(pattern, body), body)


SIGNALS_STUB = """#!/bin/bash
# Plays verify_claims.py --write-signals: STUB_EXIT is its exit code.
[ "$1 $2" = "scripts/verify_claims.py --write-signals" ] || { echo "unexpected: $*" >&2; exit 9; }
echo "  + some-row: choice, noul"
echo "wrote catalog.json"
echo "primitive text signals: 1 row(s) with evidence; 1 added, 0 changed, 0 removed, 0 unchanged; 0 not read"
exit "$STUB_EXIT"
"""


class MetadataSignalsTest(unittest.TestCase):
    """I14: the weekly run records primitives_seen after the refresh and before
    the commit, and a crash there never costs the week's refresh."""

    NAME = "Record the primitive text signals in each cited file"

    def setUp(self):
        self.text = (WORKFLOWS / "metadata.yml").read_text()
        self.lines = step_lines(self.text, self.NAME)

    def test_it_runs_between_the_refresh_and_the_commit(self):
        order = [self.text.index(f"      - name: {name}") for name in (
            "Refresh stars, licences and archive status",
            self.NAME,
            "Keep the sweep and refresh logs",
            "Rebuild everything generated from those facts, and commit it here",
        )]
        self.assertEqual(order, sorted(order))
        self.assertIn("        continue-on-error: true", self.lines)
        self.assertIn("          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}", self.lines)
        commit = run_block(step_lines(self.text, "Rebuild everything generated from those facts, and commit it here"))
        self.assertIn("git add -A catalog.json ", commit)

    def run_step(self, exit_code: int) -> subprocess.CompletedProcess:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        folder = pathlib.Path(tmp.name)
        stub = folder / "bin" / "python3"
        stub.parent.mkdir()
        stub.write_text(SIGNALS_STUB)
        stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
        script = run_block(self.lines).replace("/tmp/", f"{folder}/")
        env = {**os.environ, "PATH": f"{folder / 'bin'}{os.pathsep}{os.environ['PATH']}", "STUB_EXIT": str(exit_code)}
        return subprocess.run(
            ["bash", "--noprofile", "--norc", "-e", "-c", script],
            cwd=folder, env=env, capture_output=True, text=True,
        )

    def test_the_counts_end_the_log_and_the_exit_code_is_kept(self):
        for code in (0, 1):
            with self.subTest(exit=code):
                done = self.run_step(code)
                self.assertEqual(done.returncode, code, done.stderr)
                self.assertEqual(done.stdout.strip().splitlines()[-1][:22], "primitive text signals")

    def test_claims_stays_read_only_and_never_writes_signals(self):
        claims = (WORKFLOWS / "claims.yml").read_text()
        self.assertIn("  contents: read\n", claims)
        self.assertNotIn("contents: write", claims)
        self.assertNotIn("--write-signals", claims)


SOURCES_STUB = """#!/bin/bash
# Plays attribute_sources.py --write --digest FILE: STUB_EXIT is its exit code.
[ "$1 $2 $3" = "scripts/attribute_sources.py --write --digest" ] || { echo "unexpected: $*" >&2; exit 9; }
[ -n "$4" ] || { echo "no digest file" >&2; exit 9; }
echo "  ~ some-row: +someone/awesome-jev"
echo "sibling-list citations: 1 of 2 row(s) changed (1 added, 0 removed); read 52 of 52 list(s)"
exit "$STUB_EXIT"
"""


class MetadataSourcesTest(unittest.TestCase):
    """I16: the weekly run records which sibling directories link each row's
    repository after the refresh (whose digest it appends to) and before the
    commit, needs no token, and a crash there never costs the week's refresh."""

    NAME = "Record which sibling directories link each repository"

    def setUp(self):
        self.text = (WORKFLOWS / "metadata.yml").read_text()
        self.lines = step_lines(self.text, self.NAME)

    def test_it_runs_after_the_digest_is_written_and_before_the_commit(self):
        order = [self.text.index(f"      - name: {name}") for name in (
            "Refresh stars, licences and archive status",
            "Record the primitive text signals in each cited file",
            self.NAME,
            "Keep the sweep and refresh logs",
            "Rebuild everything generated from those facts, and commit it here",
        )]
        self.assertEqual(order, sorted(order))
        self.assertIn("        continue-on-error: true", self.lines)
        self.assertNotIn("GITHUB_TOKEN", "\n".join(self.lines), "the raw host needs no token")
        self.assertIn("--digest /tmp/digest.md", run_block(self.lines))

    def run_step(self, exit_code: int) -> subprocess.CompletedProcess:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        folder = pathlib.Path(tmp.name)
        stub = folder / "bin" / "python3"
        stub.parent.mkdir()
        stub.write_text(SOURCES_STUB)
        stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
        script = run_block(self.lines).replace("/tmp/", f"{folder}/")
        env = {**os.environ, "PATH": f"{folder / 'bin'}{os.pathsep}{os.environ['PATH']}", "STUB_EXIT": str(exit_code)}
        return subprocess.run(
            ["bash", "--noprofile", "--norc", "-e", "-c", script],
            cwd=folder, env=env, capture_output=True, text=True,
        )

    def test_the_counts_end_the_log_and_the_exit_code_is_kept(self):
        for code in (0, 1):
            with self.subTest(exit=code):
                done = self.run_step(code)
                self.assertEqual(done.returncode, code, done.stderr)
                self.assertTrue(done.stdout.strip().splitlines()[-1].startswith("sibling-list citations: "))


class ClaimsWorkflowTest(unittest.TestCase):
    def test_the_budget_comment_quotes_the_documented_limit(self):
        text = (WORKFLOWS / "claims.yml").read_text()
        self.assertNotIn("5000", text)
        self.assertIn("1,000 REST", text)


if __name__ == "__main__":
    unittest.main()
