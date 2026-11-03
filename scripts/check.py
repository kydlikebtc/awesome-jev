#!/usr/bin/env python3
"""Run every check CI runs, in CI's order, with one command (I08).

The same checks used to be listed four times: lint.yml's steps, the commands in
CONTRIBUTING.md, the pull-request template's checklist and metadata.yml's
pre-push chain. The lists had drifted apart. Running CONTRIBUTING's commands
could pass while CI failed, because the unit tests, the node tests, the site
data and the curated collections were checked only in lint.yml, and the weekly
metadata refresh pushed to main after four of the checks. STEPS below is now
the one list: lint.yml's catalog job runs `check.py --ci`, its regenerate job
and metadata.yml run `check.py --ci --quick` before they push, and
CONTRIBUTING and the pull-request template name `check.py --fix`.
scripts/tests/test_check.py fails when lint.yml runs a script this list does
not cover.

Each step is one command, run from the repository root, in order. It records
its kind (fix: rewrites a source into canonical form, only with --fix;
generate: rewrites derived files, as CI does before validating them; verify;
report), the lint.yml job that runs it, and anything it needs besides Python:
node, chrome or the network. Every step runs even after an earlier one failed,
so one run shows every problem; only a step whose prerequisite failed is
skipped.

A step whose tool is missing (no node, no Chrome) is reported as skipped, and
the run can still pass. Under --ci it fails instead: CI must never pass by not
checking. A step that needs the network reports an unreachable service itself
(check_release.py says `skipped`).

Generated files are judged by check_generated.py, and the verdict depends on
the mode:
  default     strict: every generated file committed and current, as a
              dispatched lint run checks.
  --fix       as CI judges a pull request, against --base (default
              origin/main): generated files may be left out, but any the
              branch changed must be exactly what the generators write.
  --base REV  that pull-request verdict, without --fix.
  --ci        by $GITHUB_EVENT_NAME, as lint.yml always has: pull_request
              compares the merge commit's two parents, push hands drift to
              the regenerate job, anything else is strict.

The same base, where a mode has one, goes to lint.py as --base: it then also
warns about a row the change adds whose machine-translated Chinese drops a
number from the English. A pull request in CI compares with HEAD^1, --fix and
--base with that base; every other run has no base and gives no such warning,
so the rows already filed are never warned about run after run
(docs/zh-queue.md lists those).

Stdlib only, like the rest of scripts/.

Run: python3 scripts/check.py           # every check, strict about generated files
     python3 scripts/check.py --fix     # sort the catalogue first; judge as a pull request
     python3 scripts/check.py --quick   # skip the preview images (Chrome), PyPI and the review card (network)
     python3 scripts/check.py --list    # every step in order, and whether this mode runs it
     python3 scripts/check.py --only lint,lint-docs   # just these; --skip NAME,... leaves some out
     python3 scripts/check.py --ci      # lint.yml: log groups, annotations, a step summary
"""

from __future__ import annotations

import argparse
import dataclasses
import os
import pathlib
import shutil
import subprocess
import sys
import time
from typing import Callable, Iterable, TextIO

SCRIPTS = pathlib.Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

KINDS = ("fix", "generate", "verify", "report")
NEEDS = ("", "node", "chrome", "network")
# The lint.yml job that runs a step; "" for a step no workflow runs (--fix only).
CI_JOB = "catalog"
JOBS = (CI_JOB, "release", "review", "")
DEFAULT_BASE = "origin/main"
COMMAND = "python3 scripts/check.py"

JSON_FILES = (
    "catalog.json",
    "retired.json",
    "compat.json",
    "patterns.json",
    "taxonomy.json",
    "collections.json",
    "picker.json",
    "schema/entry.schema.json",
    "schema/launch.schema.json",
    "schema/maker.schema.json",
)
JSON_CHECK = (
    "import json\n"
    f"for path in {JSON_FILES!r}:\n"
    "    json.load(open(path, encoding='utf-8'))\n"
    "    print(f'  ok {path}')\n"
)


@dataclasses.dataclass(frozen=True)
class Step:
    name: str  # short and unique; --only, --skip and the log use it
    title: str  # what passing it shows
    argv: tuple[str, ...]  # "python3" first is replaced by the interpreter running this
    kind: str = "verify"
    job: str = CI_JOB
    needs: str = ""
    after: tuple[str, ...] = ()  # skipped when one of these failed in the same run
    verdict: bool = False  # check_generated.py: its arguments depend on the mode
    base: bool = False  # takes --base REV when the mode has a base to compare with
    shown: str = ""  # how the command is printed, when argv is unreadable

    def display(self, extra: Iterable[str] = ()) -> str:
        return self.shown or " ".join((*self.argv, *extra))


STEPS = (
    Step(
        "sort", "catalog.json and retired.json are in slug order",
        ("python3", "scripts/sort_catalog.py"), kind="fix", job="",
    ),
    Step(
        "json", "JSON is parseable", ("python3", "-c", JSON_CHECK),
        shown="python3 -c 'json.load' each of " + ", ".join(JSON_FILES),
    ),
    Step(
        "lint", "Entries are valid against the schema and each other", ("python3", "scripts/lint.py"), base=True,
    ),
    Step("collections", "Curated entry points resolve", ("python3", "scripts/check_collections.py")),
    Step(
        "launches", "Launch weeks and maker profiles keep the board's rules",
        ("python3", "scripts/check_launches.py"),
    ),
    # Before regenerating, as in CI: no test may assume the committed
    # generated files are current, because a pull request may leave them stale.
    Step(
        "unittest-scripts", "Regression tests in scripts/tests",
        ("python3", "-m", "unittest", "discover", "-s", "scripts/tests"),
    ),
    Step("unittest-tests", "Regression tests in tests", ("python3", "-m", "unittest", "discover", "-s", "tests")),
    Step(
        "node", "Catalog filtering and sorting regression checks",
        ("node", "--test", "scripts/test_catalog_core.mjs"), needs="node",
    ),
    Step("assemble", "Site data assembles", ("python3", "scripts/assemble_site.py"), kind="generate"),
    Step(
        "site-data", "Assembled site data is complete and current",
        ("python3", "scripts/check_site_data.py"), after=("assemble",),
    ),
    Step(
        "render", "Preview images render with the current catalogue",
        ("python3", "scripts/render_images.py"), kind="generate", needs="chrome", after=("assemble",),
    ),
    # Every run validates the regenerated tree, not whatever generated files
    # happen to be committed; the generated step judges those.
    Step(
        "regenerate", "Every generated file is regenerated from the sources",
        ("python3", "scripts/regenerate.py"), kind="generate",
    ),
    # Run after regenerating, these also prove each generator idempotent. A
    # generator that wrote something different on every run would have lint's
    # regenerate job commit on every push.
    Step(
        "compat", "compatibility.md is in sync with compat.json",
        ("python3", "scripts/build_compat.py", "--check"), after=("regenerate",),
    ),
    # status.md, sources.md, llms.txt and the site's meta tags all froze at the
    # first build's 148 entries because nothing regenerated them. (The meta
    # tags are now written at deploy; check_site_data guards them.)
    Step(
        "docs", "Generated numbers in the docs are current",
        ("python3", "scripts/build_docs.py", "--check"), after=("regenerate",),
    ),
    # And no new hand-written count can creep back in beside them; every model
    # string or limit stated anywhere agrees with compat.json.
    Step(
        "lint-docs", "Docs carry no stale numbers and agree with compat.json",
        ("python3", "scripts/lint_docs.py"), after=("regenerate",),
    ),
    Step(
        "covers", "README covers fit and are current",
        ("python3", "scripts/build_readme_cover.py", "--check"), after=("regenerate",),
    ),
    Step(
        "generated", "Generated files are current, or left for the bot",
        ("python3", "scripts/check_generated.py"), verdict=True, after=("regenerate",),
    ),
    Step("counts", "Catalog stats, and the description they imply", ("python3", "scripts/counts.py"), kind="report"),
    # Its own lint.yml job, on a push to main only: the network must not
    # decide whether a pull request passes.
    Step(
        "release", "pyproject.toml, plugin.json and PyPI agree",
        ("python3", "scripts/check_release.py"), job="release", needs="network",
    ),
    # lint.yml's `review` job, on a pull request only, runs the base branch's
    # copy of this script against the pull request's catalogue. Locally it
    # reviews this branch against origin/main. Advisory: it reports and
    # exits 0 whatever it finds.
    Step(
        "review", "Review card for the rows this branch adds or changes (advisory)",
        ("python3", "scripts/review_pr.py"), kind="report", job="review", needs="network",
    ),
)
BY_NAME = {step.name: step for step in STEPS}

# Scripts a lint.yml `run:` block may invoke without being a step here, and
# why. scripts/tests/test_check.py holds lint.yml to STEPS plus this.
NOT_STEPS = {
    "scripts/check.py": "the runner itself",
}


@dataclasses.dataclass(frozen=True)
class Options:
    fix: bool = False
    ci: bool = False
    quick: bool = False
    base: str | None = None
    only: frozenset[str] = frozenset()
    skip: frozenset[str] = frozenset()


@dataclasses.dataclass(frozen=True)
class Result:
    step: Step
    status: str  # ok | failed | skipped
    detail: str = ""
    seconds: float = 0.0


def excluded(step: Step, opts: Options) -> str | None:
    """Why this mode leaves the step out altogether; None if it belongs to it."""
    if step.kind == "fix" and not opts.fix:
        return "only with --fix"
    if opts.ci and step.job != CI_JOB:
        return f"lint.yml runs it in its `{step.job}` job" if step.job else "no workflow runs it"
    if opts.only and step.name not in opts.only:
        return "not named by --only"
    return None


def skipped(step: Step, opts: Options) -> str | None:
    """Why a step this mode includes is not run, decided before any tool is looked for."""
    if step.name in opts.skip:
        return "named by --skip"
    if opts.quick and step.needs in ("chrome", "network"):
        return f"--quick skips steps that need {step.needs}"
    return None


def missing_tool(need: str) -> str | None:
    """Why the tool a step needs is absent, or None. The network is not probed:
    the step that needs it reports an unreachable service itself."""
    if need == "node":
        return None if shutil.which("node") else "node is not on PATH"
    if need == "chrome":
        try:
            import render_images  # the one place that knows where Chrome may be

            render_images.find_chrome()
        except SystemExit:
            return "no Chrome found (set CHROME to a Chrome or Chromium binary)"
        except Exception as exc:  # a broken render_images.py: run the step, which fails on it
            print(f"    could not look for Chrome ({type(exc).__name__}: {exc}); running the step", flush=True)
    return None


def is_commit(rev: str) -> bool:
    done = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}"], cwd=ROOT, capture_output=True
    )
    return done.returncode == 0


def generated_args(
    opts: Options, event: str, commit_exists: Callable[[str], bool] = is_commit
) -> tuple[list[str] | None, str]:
    """check_generated.py's arguments for this mode and what they mean, or
    None and why there is nothing to compare with."""
    if opts.ci:
        if event == "pull_request":
            return ["pr", "--base", "HEAD^1", "--head", "HEAD^2"], "judged as a pull request (HEAD^2 against HEAD^1)"
        if event == "push":
            return ["push"], "a push to main: drift is reported for the regenerate job, not failed"
        return ["strict"], f"strict ({event or 'no event'}): any drift fails"
    base = opts.base or (DEFAULT_BASE if opts.fix else None)
    if base is None:
        return ["strict"], "strict: every one committed and current"
    if not commit_exists(base):
        return None, f"{base} is not a commit in this clone; fetch it, or pass --base <remote>/main"
    return ["pr", "--base", base], f"judged as CI judges a pull request against {base}"


def base_args(
    opts: Options, event: str, commit_exists: Callable[[str], bool] = is_commit
) -> tuple[list[str], str]:
    """--base REV for a step that compares this tree with a base (lint's
    warnings about new rows), and what that base is; no arguments when this
    mode has none, which leaves those warnings out rather than failing."""
    if opts.ci:
        if event == "pull_request":
            return ["--base", "HEAD^1"], "rows the pull request adds are those not in HEAD^1"
        return [], f"no base ({event or 'no event'}): nothing is compared as a new row"
    base = opts.base or (DEFAULT_BASE if opts.fix else None)
    if base is None:
        return [], "no base (--fix or --base gives one): nothing is compared as a new row"
    if not commit_exists(base):
        return [], f"{base} is not a commit in this clone: nothing is compared as a new row"
    return ["--base", base], f"rows this tree adds are those not in {base}"


def execute(argv: list[str]) -> int:
    env = {**os.environ, "PYTHONUNBUFFERED": "1"}
    return subprocess.run(argv, cwd=ROOT, env=env).returncode


def interpreter(argv: Iterable[str]) -> list[str]:
    argv = list(argv)
    return [sys.executable, *argv[1:]] if argv and argv[0] == "python3" else argv


def escape(text: str, prop: bool = False) -> str:
    """For a GitHub workflow command: its message, or (prop) a property value."""
    text = text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    return text.replace(":", "%3A").replace(",", "%2C") if prop else text


class Runner:
    """Runs the steps a mode includes, in order, and remembers each result."""

    def __init__(
        self,
        opts: Options,
        *,
        event: str = "",
        execute: Callable[[list[str]], int] = execute,
        missing: Callable[[str], str | None] = missing_tool,
        commit_exists: Callable[[str], bool] = is_commit,
        out: TextIO | None = None,
        clock: Callable[[], float] = time.monotonic,
    ):
        self.opts, self.event, self.execute = opts, event, execute
        self.missing, self.commit_exists, self.clock = missing, commit_exists, clock
        self.out = out or sys.stdout
        self.results: list[Result] = []

    def say(self, text: str) -> None:
        print(text, file=self.out, flush=True)

    def failed(self, name: str) -> bool:
        return any(r.step.name == name and r.status == "failed" for r in self.results)

    def why_not(self, step: Step) -> tuple[str | None, str | None, list[str]]:
        """(reason to skip, reason it fails without running, extra arguments)."""
        reason = skipped(step, self.opts)
        if reason:
            return reason, None, []
        broken = [name for name in step.after if self.failed(name)]
        if broken:
            return f"{', '.join(broken)} failed", None, []
        extra: list[str] = []
        if step.base:
            extra, meaning = base_args(self.opts, self.event, self.commit_exists)
            self.say(f"    {step.name} — {meaning}")
        if step.verdict:
            args, meaning = generated_args(self.opts, self.event, self.commit_exists)
            if args is None:
                return meaning, None, []
            extra = args
            self.say(f"    generated files — {meaning}")
        absent = self.missing(step.needs) if step.needs else None
        if absent:
            return (None, absent, []) if self.opts.ci else (absent, None, [])
        return None, None, extra

    def run(self, steps: Iterable[Step] = STEPS) -> list[Result]:
        plan = [step for step in steps if excluded(step, self.opts) is None]
        for index, step in enumerate(plan, 1):
            header = f"[{index}/{len(plan)}] {step.name} — {step.title}"
            self.say(f"::group::{header}" if self.opts.ci else f"\n==> {header}")
            reason, fatal, extra = self.why_not(step)
            if reason:
                self.results.append(Result(step, "skipped", reason))
                self.say(f"    skipped: {reason}")
            elif fatal:
                self.results.append(Result(step, "failed", fatal))
                self.say(f"    FAILED: {fatal}")
            else:
                self.say(f"    $ {step.display(extra)}")
                started = self.clock()
                code = self.execute(interpreter((*step.argv, *extra)))
                seconds = self.clock() - started
                status = "ok" if code == 0 else "failed"
                detail = "" if code == 0 else f"exit {code}: {step.display(extra)}"
                self.results.append(Result(step, status, detail, seconds))
                self.say(f"    {'ok' if code == 0 else f'FAILED (exit {code})'} in {seconds:.1f} s")
            if self.opts.ci:
                self.say("::endgroup::")
                last = self.results[-1]
                if last.status == "failed":
                    self.say(
                        f"::error title={escape(f'Check failed ({step.name})', prop=True)}::"
                        + escape(f"{step.title}: {last.detail}. Rerun it alone: {COMMAND} --only {step.name}")
                    )
        return self.results


def tally(results: list[Result]) -> str:
    counts = {status: sum(r.status == status for r in results) for status in ("ok", "failed", "skipped")}
    return f"{len(results)} steps: {counts['ok']} passed, {counts['failed']} failed, {counts['skipped']} skipped"


def report(results: list[Result], seconds: float, out: TextIO) -> None:
    print(f"\ncheck.py: {tally(results)}, in {seconds:.1f} s", file=out)
    for r in results:
        label = {"ok": "ok", "failed": "FAILED", "skipped": "skipped"}[r.status]
        tail = f"{r.seconds:.1f} s" if r.status == "ok" else r.detail
        print(f"  {label:<8} {r.step.name:<17} {tail}", file=out)
    failed = [r.step.name for r in results if r.status == "failed"]
    not_run = [f"{r.step.name} ({r.detail})" for r in results if r.status == "skipped"]
    if failed:
        print(f"FAILED: {', '.join(failed)}. Rerun one alone: {COMMAND} --only {failed[0]}", file=out)
    elif not results:
        print("No step ran.", file=out)
    elif not_run:
        # A skipped check did not pass; name it rather than say "All checks passed".
        print(f"No check failed. Not run, so not passed: {'; '.join(not_run)}.", file=out)
    else:
        print("All checks passed.", file=out)
    out.flush()


def summary_markdown(results: list[Result], seconds: float, flags: str) -> str:
    lines = [
        "## Checks",
        "",
        f"`{COMMAND} {flags}`: {tally(results)}, in {seconds:.0f} s. "
        f"Run them locally with `{COMMAND}`; `--only NAME` reruns one step.",
        "",
        "| # | Step | Result | Detail |",
        "| --- | --- | --- | --- |",
    ]
    for index, r in enumerate(results, 1):
        detail = (f"{r.seconds:.1f} s" if r.status == "ok" else r.detail).replace("|", "\\|")
        mark = "**failed**" if r.status == "failed" else r.status
        lines.append(f"| {index} | `{r.step.name}` {r.step.title} | {mark} | {detail} |")
    return "\n".join(lines) + "\n"


def verdict_shown(opts: Options, event: str) -> list[str]:
    """check_generated.py's arguments as --list shows them."""
    if opts.ci and not event:
        return ["{pr --base HEAD^1 --head HEAD^2 | push | strict}", "by $GITHUB_EVENT_NAME"]
    args, _ = generated_args(opts, event, lambda _rev: True)
    return args or []


def list_steps(opts: Options, out: TextIO) -> None:
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    for index, step in enumerate(STEPS, 1):
        why = excluded(step, opts) or skipped(step, opts)
        extra = verdict_shown(opts, event) if step.verdict else []
        print(
            f"{index:>2}  {step.name:<17} {step.kind:<8} needs {step.needs or '-':<7} "
            f"lint.yml job {step.job or '-':<8} {'not run: ' + why if why else 'runs'}",
            file=out,
        )
        print(f"      {step.display(extra)}", file=out)


def names(values: Iterable[str] | None, parser: argparse.ArgumentParser) -> frozenset[str]:
    """Step names from repeatable, comma-separated --only/--skip values."""
    chosen = frozenset(name.strip() for value in values or () for name in value.split(",") if name.strip())
    unknown = sorted(chosen - set(BY_NAME))
    if unknown:
        parser.error(f"unknown step {', '.join(unknown)}; the steps are {', '.join(BY_NAME)}")
    return chosen


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--fix", action="store_true",
        help="first sort catalog.json and retired.json, then judge generated files as CI judges a pull request",
    )
    parser.add_argument(
        "--ci", action="store_true",
        help="lint.yml: log groups, annotations and a step summary; generated files judged by "
        "$GITHUB_EVENT_NAME; a missing node or Chrome fails",
    )
    parser.add_argument("--quick", action="store_true", help="skip the steps that need Chrome or the network")
    parser.add_argument(
        "--base", metavar="REV",
        help=f"judge generated files as CI judges a pull request against REV, and have lint warn about "
        f"machine-translated rows added since REV that drop a number (--fix: {DEFAULT_BASE})",
    )
    # Repeatable, so a wrapper's --skip and the caller's add up instead of one
    # replacing the other.
    parser.add_argument(
        "--only", metavar="NAME,...", action="append", help="run only these steps (names from --list; repeatable)"
    )
    parser.add_argument("--skip", metavar="NAME,...", action="append", help="leave these steps out (repeatable)")
    parser.add_argument("--list", action="store_true", help="print every step and whether this mode runs it")
    args = parser.parse_args(argv)
    if args.ci and (args.fix or args.base):
        parser.error("--ci judges generated files by event; it takes neither --fix nor --base")
    opts = Options(
        fix=args.fix, ci=args.ci, quick=args.quick, base=args.base,
        only=names(args.only, parser), skip=names(args.skip, parser),
    )
    if args.list:
        list_steps(opts, sys.stdout)
        return 0
    if not any(excluded(step, opts) is None for step in STEPS):
        print("error: this mode selects no step; see --list", file=sys.stderr)
        return 2

    started = time.monotonic()
    results = Runner(opts, event=os.environ.get("GITHUB_EVENT_NAME", "")).run()
    seconds = time.monotonic() - started
    report(results, seconds, sys.stdout)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if opts.ci and summary:
        flags = " ".join(arg for arg in (argv if argv is not None else sys.argv[1:]))
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(summary_markdown(results, seconds, flags))
    return 1 if any(r.status == "failed" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
