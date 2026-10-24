#!/usr/bin/env python3
"""Say when a scheduled workflow has stopped doing its job.

Each weekly job here reports through an issue or a commit — claims through its
issue, metadata through its commit and its digest, discover through its queue,
links (since 2026-10-24) through its issue. A job that stops running, or fails
before it reports, says nothing at all, and nothing noticed: links failed on
each of its first four Mondays (2026-09-28 to 2026-10-19), and the only sign
was a red cross on the Actions page. GitHub also turns a public repository's
schedules off after 60 days without activity, which looks the same: silence.

So once a day this asks the Actions API about every workflow under
.github/workflows that has a `schedule:` trigger (this one aside) and reports
one when

- it is not `active`: disabled by hand, or by GitHub for inactivity; or
- no run of it, scheduled or dispatched, has succeeded in the last MAX_DAYS
  days: a week, and a day of slack for GitHub starting scheduled runs late.

A workflow is found by its file, so a new scheduled job is watched from its
first day without editing anything here. Only a successful run counts: one
that went red, was cancelled or is still queued says nothing about whether the
job can do its work.

`--markdown FILE` writes the issue body watchdog.yml keeps. It quotes dates,
never "N days ago", so the body changes only when the facts do and the
workflow can leave an unchanged issue alone.

Exit codes: 0 every scheduled workflow is healthy, 1 at least one is not, 2 the
Actions API could not be read, so nothing was judged.

Usage:
  python3 scripts/watchdog.py
  python3 scripts/watchdog.py --markdown /tmp/body.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _github  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKFLOWS = ROOT / ".github" / "workflows"
# This workflow runs the check; it cannot report its own silence.
OWN = "watchdog.yml"
MAX_DAYS = 8
SCHEDULE = re.compile(r"^  schedule:\s*$", re.MULTILINE)


def scheduled(directory: pathlib.Path = WORKFLOWS) -> list[str]:
    """File names of the workflows with a `schedule:` trigger, this one aside."""
    return [
        path.name
        for path in sorted(directory.glob("*.yml"))
        if path.name != OWN and SCHEDULE.search(path.read_text(encoding="utf-8"))
    ]


def when(run: dict) -> dt.datetime:
    return dt.datetime.fromisoformat(run["created_at"].replace("Z", "+00:00"))


def day(run: dict | None) -> str:
    return when(run).date().isoformat() if run else "never"


class Unreadable(Exception):
    """The Actions API gave no usable answer about a workflow."""


def look(name: str, repo: str) -> dict:
    """What the Actions API says about one workflow file: its state and page,
    its newest run of any outcome and its newest successful run (or None)."""
    base = f"/repos/{repo}/actions/workflows/{name}"
    workflow = _github.api_get(base)
    latest = _github.api_get(f"{base}/runs?per_page=1")
    success = _github.api_get(f"{base}/runs?per_page=1&status=success")
    for answer in (workflow, latest, success):
        if not isinstance(answer, dict) or answer.get("blocked"):
            raise Unreadable(f"{name}: the Actions API did not answer")
    return {
        "name": name,
        "state": workflow.get("state", "unknown"),
        # Its Actions page, where its runs are listed and "Run workflow" is.
        "url": f"https://github.com/{repo}/actions/workflows/{name}",
        "latest": (latest.get("workflow_runs") or [None])[0],
        "success": (success.get("workflow_runs") or [None])[0],
    }


def problem(seen: dict, now: dt.datetime) -> str | None:
    """Why this workflow needs a person, or None when it is healthy."""
    if seen["state"] != "active":
        if seen["state"] == "disabled_inactivity":
            return ("GitHub turned its schedule off after 60 days without repository activity; "
                    "enable it on its Actions page")
        return f"it is {seen['state'].replace('_', ' ')}; enable it on its Actions page"
    if seen["success"] is None:
        return "no run of it has ever succeeded"
    age = (now - when(seen["success"])).total_seconds() / 86_400
    if age > MAX_DAYS:
        return f"no run of it has succeeded in the last {MAX_DAYS} days"
    return None


def run_cell(run: dict | None) -> str:
    if not run:
        return "none"
    outcome = run.get("conclusion") or run.get("status") or "unknown"
    return f"{day(run)}, {outcome} ([run]({run.get('html_url', '')}))"


def table(found: list[tuple[dict, str | None]]) -> list[str]:
    """One row per scheduled workflow, the ones that need a person first."""
    rows = [item for item in found if item[1]] + [item for item in found if not item[1]]
    lines = ["| Workflow | Last success | Newest run | Needs |", "| --- | --- | --- | --- |"]
    for seen, why in rows:
        name = seen["name"].removesuffix(".yml")
        lines.append(
            f"| [{name}]({seen['url']}) | {day(seen['success'])} | {run_cell(seen['latest'])} | {why or 'nothing'} |"
        )
    return lines


def markdown(found: list[tuple[dict, str | None]]) -> str:
    """The issue body watchdog.yml keeps."""
    broken = sum(1 for _, why in found if why)
    return "\n".join([
        "A daily check found a scheduled workflow that has stopped doing its job. Each one",
        "reports through an issue or a commit, so one that stops running or fails before it",
        "reports says nothing; this issue is how that silence is heard.",
        "",
        *table(found),
        "",
        "Open the newest run, fix what stopped it, then run the workflow again from its",
        "Actions page (Run workflow). This issue closes itself on the first day every",
        f"scheduled workflow has succeeded within {MAX_DAYS} days, and its description",
        "is rewritten whenever what it says changes.",
        "",
        f"<!-- Written by scripts/watchdog.py; {broken} of {len(found)} need a person. -->",
        "",
    ])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--markdown", default="", metavar="FILE", help="write the issue body here")
    args = parser.parse_args(argv)

    # Actions sets GITHUB_REPOSITORY, so a fork watches its own runs.
    repo = os.environ.get("GITHUB_REPOSITORY") or _github.SELF
    now = dt.datetime.now(dt.timezone.utc)
    names = scheduled()
    try:
        found = [(seen, problem(seen, now)) for seen in (look(name, repo) for name in names)]
    except (Unreadable, _github.RateLimited) as exc:
        print(f"::error title=Watchdog could not read the Actions API::{exc}")
        return 2

    for seen, why in found:
        print(f"  {'ok  ' if not why else 'STOP'} {seen['name']:<16} last success {day(seen['success'])}"
              + (f": {why}" if why else ""))
    broken = sum(1 for _, why in found if why)
    body = markdown(found)
    if args.markdown:
        pathlib.Path(args.markdown).write_text(body, encoding="utf-8")
    _github.step_summary("## Scheduled workflows\n\n" + "\n".join(table(found)))
    print(f"watchdog: {len(found)} scheduled workflow(s), {broken} need a person")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
