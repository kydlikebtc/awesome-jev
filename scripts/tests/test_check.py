"""scripts/check.py is the one list of the checks CI runs (I08).

lint.yml, metadata.yml, CONTRIBUTING.md and the pull-request template each used
to carry their own list of checks, and the lists drifted. These tests hold
lint.yml to check.py's STEPS: every script a lint.yml `run:` block invokes is a
step, or is named in NOT_STEPS with a reason. They also check how each mode
chooses, skips and reports steps, with a fake runner so nothing heavy runs, and
that the workflows and the contributor docs name check.py. No network.
"""

from __future__ import annotations

import io
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import check  # noqa: E402

WORKFLOWS = ROOT / ".github" / "workflows"
LINT = WORKFLOWS / "lint.yml"
METADATA = WORKFLOWS / "metadata.yml"
SCRIPT = re.compile(r"\bscripts/[\w./-]+\.(?:py|mjs)\b")
UNITTEST = re.compile(r"-m unittest discover -s (\S+)")


def run_blocks(text: str) -> dict[str, list[str]]:
    """Each job's `run:` commands, inline or block scalar, keyed by job id,
    with shell comments dropped so prose cannot satisfy or fail a test."""
    jobs: dict[str, list[str]] = {}
    job = None
    lines = text.split("\n")
    index = lines.index("jobs:") + 1
    while index < len(lines):
        line = lines[index]
        header = re.fullmatch(r"  ([\w-]+):", line)
        if header:
            job = header.group(1)
            jobs[job] = []
        found = re.match(r"^\s+(?:- )?run: ?(.*)$", line)
        if found and job:
            column = line.index("run:")
            index += 1
            if found.group(1).strip() not in ("|", "|-", ">", ">-"):
                jobs[job].append(found.group(1))
                continue
            body = []
            while index < len(lines) and (
                not lines[index].strip() or len(lines[index]) - len(lines[index].lstrip()) > column
            ):
                if not lines[index].lstrip().startswith("#"):
                    body.append(lines[index].strip())
                index += 1
            jobs[job].append("\n".join(body).strip())
            continue
        index += 1
    return jobs


def invoked(command: str) -> set[str]:
    """The scripts and test directories a shell command runs."""
    return set(SCRIPT.findall(command)) | {f"unittest:{d}" for d in UNITTEST.findall(command)}


def covered(steps=check.STEPS) -> set[str]:
    return set().union(*(invoked(" ".join(step.argv)) for step in steps))


def uncovered(text: str) -> list[tuple[str, str]]:
    """(job, script) for every script a workflow runs that check.py does not know."""
    known = covered() | set(check.NOT_STEPS)
    return sorted(
        (job, key)
        for job, commands in run_blocks(text).items()
        for command in commands
        for key in invoked(command)
        if key not in known
    )


class LintIsCoveredTest(unittest.TestCase):
    def setUp(self):
        self.text = LINT.read_text()
        self.jobs = run_blocks(self.text)

    def test_every_script_lint_runs_is_a_step(self):
        self.assertEqual(
            uncovered(self.text), [],
            "lint.yml runs scripts that scripts/check.py does not list: add each to STEPS, "
            "or to NOT_STEPS with the reason",
        )

    def test_the_parser_finds_what_a_new_step_would_add(self):
        # Otherwise the test above could pass by reading nothing.
        self.assertEqual(set(self.jobs), {"catalog", "regenerate", "release", "review"})
        added = self.text.replace(
            "        run: python3 scripts/check.py --ci\n",
            "        run: python3 scripts/check.py --ci\n\n"
            "      - name: new\n        run: |\n          # scripts/in_a_comment.py\n"
            "          python3 scripts/new_check.py --flag\n"
            "          python3 -m unittest discover -s newtests\n\n"
            "      - run: node --test scripts/new.mjs\n",
        )
        self.assertEqual(
            uncovered(added),
            [("catalog", "scripts/new.mjs"), ("catalog", "scripts/new_check.py"), ("catalog", "unittest:newtests")],
        )

    def test_no_inline_python_in_lint(self):
        # An inline check is a check the list cannot see; it belongs in STEPS.
        for job, commands in self.jobs.items():
            for command in commands:
                self.assertNotIn("python3 -c", command, job)

    def test_not_steps_are_real_and_explained(self):
        for script, reason in check.NOT_STEPS.items():
            with self.subTest(script=script):
                self.assertTrue((ROOT / script).exists())
                self.assertTrue(reason.strip())
                self.assertNotIn(script, covered())

    def test_the_catalog_job_runs_check_py_and_nothing_else(self):
        self.assertEqual(self.jobs["catalog"], ["python3 scripts/check.py --ci"])
        catalog = self.text.split("\n  catalog:\n", 1)[1].split("\n  regenerate:\n", 1)[0]
        self.assertIn("    name: Validate catalog and generated READMEs\n", catalog)
        self.assertIn("      drift: ${{ steps.generated.outputs.drift }}\n", catalog)
        # --ci fails without node, so the job must set it up before running.
        self.assertLess(catalog.index("uses: actions/setup-node@"), catalog.index("scripts/check.py --ci"))

    def test_the_regenerate_job_runs_the_same_list(self):
        self.assertIn("python3 scripts/check.py --ci --quick", self.jobs["regenerate"])
        regenerate = self.text.split("\n  regenerate:\n", 1)[1].split("\n  # ", 1)[0]
        self.assertLess(regenerate.index("uses: actions/setup-node@"), regenerate.index("scripts/check.py --ci"))

    def test_a_step_for_another_job_is_run_by_that_job(self):
        # By its script: the review job runs the base branch's copy of it, from
        # another directory and with CI's arguments (scripts/review_pr.py).
        for step in check.STEPS:
            if step.job in ("", check.CI_JOB):
                continue
            with self.subTest(step=step.name):
                ran = set().union(*(invoked(command) for command in self.jobs[step.job]))
                self.assertTrue(invoked(step.display()) <= ran, (step.display(), self.jobs[step.job]))


class MetadataTest(unittest.TestCase):
    def test_it_runs_every_check_on_its_commit_before_pushing(self):
        text = METADATA.read_text()
        check_at = text.index("run: python3 scripts/check.py --ci --quick\n")
        self.assertLess(text.index("git commit -q"), check_at)
        self.assertLess(check_at, text.index("git push -q origin HEAD:main"))
        self.assertIn("        if: steps.commit.outputs.changed == 'true'\n", text)
        self.assertLess(text.index("uses: actions/setup-node@"), check_at)
        # No hand-kept chain of checks beside it.
        commands = "\n".join(c for cs in run_blocks(text).values() for c in cs)
        for script in ("lint.py", "lint_docs.py", "build_compat.py", "build_docs.py"):
            self.assertNotIn(f"scripts/{script}", commands)


def step_script(text: str, name: str) -> str:
    """The `run: |` block of a workflow step, dedented."""
    lines = text.splitlines()
    start = lines.index(f"      - name: {name}")
    run = next(i for i in range(start, len(lines)) if lines[i] == "        run: |")
    body = []
    for line in lines[run + 1 :]:
        if line.strip() and not line.startswith(" " * 10):
            break
        body.append(line[10:])
    return "\n".join(body)


class MetadataStepsTest(unittest.TestCase):
    """metadata.yml's commit and push steps, run as GitHub runs them (`bash -e`,
    no pipefail) in throwaway clones of a bare origin. check.py runs between
    them; here only the shell around it is exercised."""

    COMMIT = "Rebuild everything generated from those facts, and commit it here"
    PUSH = "Push to main, or fall back to a branch if main moved"
    GIT = ["git", "-c", "user.name=test", "-c", "user.email=test@example.invalid"]
    REGENERATE = (
        "import pathlib\n"
        "root = pathlib.Path(__file__).resolve().parent.parent\n"
        "(root / 'README.md').write_text('generated from ' + (root / 'catalog.json').read_text())\n"
    )

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        self.env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
        text = METADATA.read_text()
        # The steps write their notes to /tmp; keep the test's own.
        self.commit_step = step_script(text, self.COMMIT).replace("/tmp/", f"{self.dir}/")
        self.push_step = step_script(text, self.PUSH)
        (self.dir / "digest.md").write_text("3 stars moved\n")
        seed = self.dir / "seed"
        files = {
            "catalog.json": "v1\n", "README.md": "generated from v1\n", "README.zh-CN.md": "zh\n",
            "docs/status.md": "status\n", "llms.txt": "llms\n", "scripts/regenerate.py": self.REGENERATE,
            ".discover/seen.json": "{}\n", "examples/index.json": "{}\n", "history/README.md": "# history/\n",
            "examples/README.md": "examples\n", "skills/awesome-jev/SKILL.md": "skill\n",
        }
        for rel, body in files.items():
            (seed / rel).parent.mkdir(parents=True, exist_ok=True)
            (seed / rel).write_text(body)
        self.git(seed.parent, "init", "-q", "-b", "main", str(seed))
        self.git(seed, "add", "-A")
        self.git(seed, "commit", "-q", "-m", "base")
        self.origin = self.dir / "origin.git"
        self.git(self.dir, "clone", "-q", "--bare", str(seed), str(self.origin))
        self.work = self.dir / "work"
        self.git(self.dir, "clone", "-q", str(self.origin), str(self.work))
        self.output = self.dir / "output.txt"

    def git(self, cwd: pathlib.Path, *args: str) -> str:
        return subprocess.run(
            [*self.GIT, *args], cwd=cwd, env=self.env, capture_output=True, text=True, check=True
        ).stdout

    def bash(self, script: str, **env: str) -> subprocess.CompletedProcess:
        self.output.write_text("")
        return subprocess.run(
            ["bash", "--noprofile", "--norc", "-e", "-c", script], cwd=self.work,
            env={**self.env, "GITHUB_OUTPUT": str(self.output), **env}, capture_output=True, text=True,
        )

    def outputs(self) -> dict[str, str]:
        return dict(line.split("=", 1) for line in self.output.read_text().splitlines() if line)

    def origin_log(self, ref: str = "main") -> list[str]:
        return self.git(self.origin, "log", "--format=%an|%s", ref).splitlines()

    def test_nothing_changed_commits_and_pushes_nothing(self):
        done = self.bash(self.commit_step)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(self.outputs(), {"changed": "false"})
        done = self.bash(self.push_step, CHANGED="false")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(self.outputs(), {"landed": "none"})
        self.assertEqual(len(self.origin_log()), 1)

    def test_commits_the_refresh_and_what_it_regenerates_then_pushes(self):
        (self.work / "catalog.json").write_text("v2\n")
        (self.work / "stray.txt").write_text("never committed by the bot\n")
        done = self.bash(self.commit_step)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(self.outputs(), {"changed": "true"})
        self.assertEqual(len(self.origin_log()), 1, "nothing is pushed before the checks run")
        head = self.git(self.work, "log", "-1", "--format=%an|%s|%b", "HEAD").strip()
        self.assertEqual(head, "github-actions[bot]|chore: weekly refresh of link status and repository facts|3 stars moved")
        files = self.git(self.work, "show", "--name-only", "--format=", "HEAD").split()
        self.assertEqual(sorted(files), ["README.md", "catalog.json"])

        done = self.bash(self.push_step, CHANGED="true")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(self.outputs(), {"landed": "main"})
        self.assertEqual(self.origin_log()[0], "github-actions[bot]|chore: weekly refresh of link status and repository facts")

    def test_commits_the_discovery_verdicts_it_took_in(self):
        # The step before this one merged discover.yml's artifact (I05).
        (self.work / ".discover" / "seen.json").write_text('{"verdicts": {}}\n')
        done = self.bash(self.commit_step)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(self.outputs(), {"changed": "true"})
        files = self.git(self.work, "show", "--name-only", "--format=", "HEAD").split()
        self.assertEqual(files, [".discover/seen.json"])

    def test_commits_the_snapshot_the_step_before_it_wrote(self):
        # "Keep a dated snapshot of the catalogue's counts" wrote it (I46).
        (self.work / "history" / "2026-10-07.json").write_text("{}\n")
        done = self.bash(self.commit_step)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(self.outputs(), {"changed": "true"})
        files = self.git(self.work, "show", "--name-only", "--format=", "HEAD").split()
        self.assertEqual(files, ["history/2026-10-07.json"])

    def test_falls_back_to_a_branch_rather_than_forcing(self):
        (self.work / "catalog.json").write_text("v2\n")
        self.assertEqual(self.bash(self.commit_step).returncode, 0)
        other = self.dir / "other"
        self.git(self.dir, "clone", "-q", str(self.origin), str(other))
        (other / "catalog.json").write_text("a conflicting edit\n")
        self.git(other, "commit", "-q", "-am", "someone else")
        self.git(other, "push", "-q", "origin", "HEAD:main")
        before = self.origin_log()

        done = self.bash(self.push_step, CHANGED="true")
        self.assertEqual(done.returncode, 0, done.stderr)
        landed = self.outputs()["landed"]
        self.assertTrue(landed.startswith("metadata/refresh-"), landed)
        self.assertEqual(self.origin_log(), before)
        self.assertEqual(self.origin_log(landed)[0].split("|")[0], "github-actions[bot]")


class ContributorDocsTest(unittest.TestCase):
    def test_contributing_and_the_template_name_the_one_command(self):
        for path in ("CONTRIBUTING.md", ".github/PULL_REQUEST_TEMPLATE.md"):
            with self.subTest(path=path):
                text = (ROOT / path).read_text(encoding="utf-8")
                self.assertTrue("python3 scripts/check.py --fix" in text, f"{path} does not name check.py --fix")
                self.assertFalse("python3 scripts/sort_catalog.py && python3 scripts/lint.py" in text, path)


class StepsTest(unittest.TestCase):
    def test_steps_are_well_formed(self):
        names = [step.name for step in check.STEPS]
        self.assertEqual(len(names), len(set(names)))
        for position, step in enumerate(check.STEPS):
            with self.subTest(step=step.name):
                self.assertRegex(step.name, r"^[a-z][a-z-]*$")
                self.assertIn(step.kind, check.KINDS)
                self.assertIn(step.needs, check.NEEDS)
                self.assertIn(step.job, check.JOBS)
                self.assertEqual(step.kind == "fix", step.job == "", "only a fix step runs in no workflow")
                for before in step.after:
                    self.assertIn(before, names[:position])
                for script in SCRIPT.findall(" ".join(step.argv)):
                    self.assertTrue((ROOT / script).exists(), script)
        for path in check.JSON_FILES:
            self.assertTrue((ROOT / path).exists(), path)

    def test_order(self):
        names = [step.name for step in check.STEPS]
        self.assertEqual([s.name for s in check.STEPS if s.verdict], ["generated"])
        # Unit tests before regenerating, as in CI: none may rely on committed
        # generated files being current, since a pull request may leave them stale.
        for tests in ("unittest-scripts", "unittest-tests"):
            self.assertLess(names.index(tests), names.index("regenerate"))
        for later in ("compat", "docs", "lint-docs", "covers", "generated"):
            self.assertLess(names.index("regenerate"), names.index(later))
            self.assertIn("regenerate", check.BY_NAME[later].after)
        self.assertEqual(names[0], "sort")


def planned(opts: check.Options) -> dict[str, str]:
    """Each step's fate under opts, as --list reports it."""
    return {
        step.name: (check.excluded(step, opts) and "excluded") or (check.skipped(step, opts) and "skipped") or "runs"
        for step in check.STEPS
    }


class ModeTest(unittest.TestCase):
    def test_default_runs_everything_but_the_fixer(self):
        fates = planned(check.Options())
        self.assertEqual(fates.pop("sort"), "excluded")
        self.assertEqual(set(fates.values()), {"runs"})

    def test_ci_runs_the_catalog_job(self):
        fates = planned(check.Options(ci=True))
        self.assertEqual({n for n, f in fates.items() if f != "runs"}, {"sort", "release", "review"})

    def test_quick_skips_chrome_and_network(self):
        fates = planned(check.Options(quick=True))
        self.assertEqual({n for n, f in fates.items() if f == "skipped"}, {"render", "release", "review"})

    def test_fix_sorts_first(self):
        self.assertEqual(planned(check.Options(fix=True))["sort"], "runs")

    def test_only_and_skip(self):
        fates = planned(check.Options(only=frozenset({"lint", "render"}), skip=frozenset({"render"})))
        self.assertEqual({n for n, f in fates.items() if f != "excluded"}, {"lint", "render"})
        self.assertEqual(fates["render"], "skipped")

    def test_generated_verdict_by_mode(self):
        exists = lambda rev: True  # noqa: E731
        absent = lambda rev: False  # noqa: E731
        self.assertEqual(check.generated_args(check.Options(), "", exists)[0], ["strict"])
        self.assertEqual(check.generated_args(check.Options(), "pull_request", exists)[0], ["strict"])
        self.assertEqual(
            check.generated_args(check.Options(fix=True), "", exists)[0], ["pr", "--base", "origin/main"]
        )
        self.assertEqual(
            check.generated_args(check.Options(base="upstream/main"), "", exists)[0], ["pr", "--base", "upstream/main"]
        )
        args, why = check.generated_args(check.Options(fix=True), "", absent)
        self.assertIsNone(args)
        self.assertIn("--base", why)


class FakeRun:
    """A Runner whose commands never run: each returns the code set for it."""

    def __init__(self, opts: check.Options, codes=None, missing=None, commit_exists=None, event=""):
        self.calls: list[list[str]] = []
        self.asked: list[str] = []
        self.codes = codes or {}
        self.out = io.StringIO()

        def execute(argv):
            self.calls.append(argv)
            return next((code for key, code in self.codes.items() if key in argv), 0)

        def ask(need):
            self.asked.append(need)
            return (missing or {}).get(need)

        ticks = iter(range(1000))
        self.results = check.Runner(
            opts, event=event, execute=execute, missing=ask,
            commit_exists=commit_exists or (lambda rev: True), out=self.out, clock=lambda: next(ticks),
        ).run()

    def status(self) -> dict[str, str]:
        return {r.step.name: r.status for r in self.results}

    def detail(self, name: str) -> str:
        return next(r.detail for r in self.results if r.step.name == name)


class RunnerTest(unittest.TestCase):
    def test_every_step_runs_in_order(self):
        run = FakeRun(check.Options())
        expected = [s for s in check.STEPS if check.excluded(s, check.Options()) is None]
        self.assertEqual([r.step for r in run.results], expected)
        self.assertEqual(set(run.status().values()), {"ok"})
        self.assertEqual(len(run.calls), len(expected))
        self.assertEqual(run.calls[1], [sys.executable, "scripts/lint.py"])
        self.assertIn(["node", "--test", "scripts/test_catalog_core.mjs"], run.calls)
        self.assertIn([sys.executable, "scripts/check_generated.py", "strict"], run.calls)

    def test_a_failure_does_not_stop_the_run_but_skips_what_needs_it(self):
        run = FakeRun(check.Options(), codes={"scripts/lint.py": 1, "scripts/regenerate.py": 2})
        status = run.status()
        self.assertEqual(status["lint"], "failed")
        self.assertEqual(status["regenerate"], "failed")
        self.assertEqual(run.detail("regenerate"), "exit 2: python3 scripts/regenerate.py")
        for later in ("compat", "docs", "lint-docs", "covers", "generated"):
            self.assertEqual(status[later], "skipped")
            self.assertEqual(run.detail(later), "regenerate failed")
        self.assertEqual(status["counts"], "ok")
        self.assertEqual(status["collections"], "ok")

    def test_a_missing_tool_is_skipped_locally(self):
        run = FakeRun(check.Options(), missing={"node": "node is not on PATH"})
        self.assertEqual(run.status()["node"], "skipped")
        self.assertEqual(run.detail("node"), "node is not on PATH")
        self.assertNotIn(["node", "--test", "scripts/test_catalog_core.mjs"], run.calls)

    def test_a_missing_tool_fails_in_ci(self):
        run = FakeRun(check.Options(ci=True), missing={"chrome": "no Chrome found"}, event="push")
        self.assertEqual(run.status()["render"], "failed")
        self.assertIn("::error title=Check failed (render)::", run.out.getvalue())

    def test_quick_never_looks_for_chrome(self):
        run = FakeRun(check.Options(quick=True))
        self.assertNotIn("chrome", run.asked)
        self.assertEqual(run.status()["render"], "skipped")
        self.assertEqual(run.status()["release"], "skipped")

    def test_ci_groups_annotates_and_judges_by_event(self):
        run = FakeRun(check.Options(ci=True), codes={"scripts/lint.py": 1}, event="pull_request")
        out = run.out.getvalue()
        self.assertEqual(out.count("::group::"), out.count("::endgroup::"))
        self.assertIn("::group::[2/17] lint — ", out)
        self.assertIn("::error title=Check failed (lint)::", out)
        self.assertIn("Rerun it alone: python3 scripts/check.py --only lint", out)
        self.assertIn(
            [sys.executable, "scripts/check_generated.py", "pr", "--base", "HEAD^1", "--head", "HEAD^2"], run.calls
        )
        self.assertNotIn("release", run.status())

    def test_fix_sorts_then_judges_as_a_pull_request(self):
        run = FakeRun(check.Options(fix=True))
        self.assertEqual(run.calls[0], [sys.executable, "scripts/sort_catalog.py"])
        self.assertIn([sys.executable, "scripts/check_generated.py", "pr", "--base", "origin/main"], run.calls)

    def test_fix_without_a_base_to_compare_with_skips_only_that_verdict(self):
        run = FakeRun(check.Options(fix=True), commit_exists=lambda rev: False)
        self.assertEqual(run.status()["generated"], "skipped")
        self.assertIn("pass --base", run.detail("generated"))
        self.assertEqual(run.status()["regenerate"], "ok")

    def test_the_summary_table(self):
        run = FakeRun(check.Options(ci=True), codes={"scripts/lint.py": 1})
        table = check.summary_markdown(run.results, 12.0, "--ci")
        self.assertIn("## Checks", table)
        self.assertIn("| 2 | `lint` ", table)
        self.assertIn("| **failed** | exit 1: python3 scripts/lint.py |", table)

    def test_a_skipped_check_is_not_reported_as_passed(self):
        run = FakeRun(check.Options(), missing={"node": "node is not on PATH"})
        out = io.StringIO()
        check.report(run.results, 1.0, out)
        self.assertNotIn("All checks passed", out.getvalue())
        self.assertIn("No check failed. Not run, so not passed: node (node is not on PATH).", out.getvalue())
        out = io.StringIO()
        check.report(FakeRun(check.Options()).results, 1.0, out)
        self.assertIn("All checks passed.", out.getvalue())

    def test_a_broken_render_script_is_run_not_skipped(self):
        # If render_images.py cannot even be imported, the step must run and
        # fail on it, not be skipped as "no Chrome" nor crash the whole run.
        from unittest.mock import patch

        with patch.dict(sys.modules, {"render_images": None}), patch("sys.stdout", io.StringIO()):
            self.assertIsNone(check.missing_tool("chrome"))

    def test_escape(self):
        self.assertEqual(check.escape("a: b, c%\nd"), "a: b, c%25%0Ad")
        self.assertEqual(check.escape("a: b, c", prop=True), "a%3A b%2C c")


class CommandLineTest(unittest.TestCase):
    def check_py(self, *args: str, **env: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check.py"), *args],
            cwd=ROOT, capture_output=True, text=True, env={**os.environ, **env}, timeout=120,
        )

    def test_list_names_every_step(self):
        done = self.check_py("--list")
        self.assertEqual(done.returncode, 0, done.stderr)
        for step in check.STEPS:
            self.assertRegex(done.stdout, rf"\b{re.escape(step.name)}\b")
        self.assertIn("not run: only with --fix", done.stdout)

    def test_bad_arguments(self):
        self.assertEqual(self.check_py("--ci", "--fix").returncode, 2)
        self.assertEqual(self.check_py("--ci", "--base", "main").returncode, 2)
        done = self.check_py("--only", "nosuch")
        self.assertEqual(done.returncode, 2)
        self.assertIn("the steps are sort, json, lint", done.stderr)
        done = self.check_py("--ci", "--only", "sort")
        self.assertEqual(done.returncode, 2)
        self.assertIn("selects no step", done.stderr)

    def test_only_and_skip_add_up_when_repeated(self):
        # .claude/check.sh passes --skip render and then the caller's arguments.
        done = self.check_py("--list", "--skip", "render", "--skip", "release,counts")
        self.assertEqual(done.returncode, 0, done.stderr)
        for name in ("render", "release", "counts"):
            self.assertRegex(done.stdout, rf"\b{name}\b.*not run: named by --skip")
        done = self.check_py("--list", "--only", "lint", "--only", "json")
        self.assertEqual(len(re.findall(r"\bruns$", done.stdout, re.M)), 2, done.stdout)

    def test_one_real_step_in_ci_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary = pathlib.Path(tmp) / "summary.md"
            done = self.check_py("--ci", "--only", "json", GITHUB_STEP_SUMMARY=str(summary))
            self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
            self.assertIn("::group::[1/1] json", done.stdout)
            self.assertIn("  ok catalog.json", done.stdout)
            self.assertIn("All checks passed.", done.stdout)
            self.assertIn("| 1 | `json` JSON is parseable | ok |", summary.read_text())


if __name__ == "__main__":
    unittest.main()
