#!/usr/bin/env python3
"""Keep this repository's GitHub traffic in history/traffic/, one file per weekly refresh.

The catalogue reaches readers through several doors: the README in two
languages, the site, the MCP server, the skill and plugin, llms.txt and the
site's api/v1. Until 2026-10-24 nothing said which of them anyone uses. GitHub
counts what happens on the repository itself (views and unique visitors,
clones, the ten referrers and ten paths it sees most) but keeps only the last
14 days, and the workflow token cannot read them: the four endpoints need a
fine-grained token with the "Administration" repository permission (read).

With such a token in TRAFFIC_TOKEN, this writes history/traffic/<UTC date>.json
holding the four answers as GitHub gave them, under a header saying what each
is. metadata.yml runs it weekly, so successive 14-day windows overlap and no
day is lost; whoever reads them de-duplicates by day. Without the token it says
so and writes nothing, exiting 0: the secret is optional, and the refresh must
not fail for want of it. A token GitHub refuses, or an endpoint that does not
answer, exits 1 without writing anything, and the step does not stop the
refresh (continue-on-error).

This adds no counter of its own: the site and the MCP server still collect
nothing about their readers (SECURITY.md). The numbers are GitHub's own, the
same any maintainer sees on the repository's Insights page; once committed
here they are public, like every file in history/.

Stdlib only, like the rest of scripts/.

Run: TRAFFIC_TOKEN=... python3 scripts/snapshot_traffic.py
     TRAFFIC_TOKEN=... python3 scripts/snapshot_traffic.py --date 2026-10-28
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _github  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIR = pathlib.Path("history") / "traffic"
SOURCE = "scripts/snapshot_traffic.py, run by .github/workflows/metadata.yml"
# What the file holds, endpoint by endpoint (docs.github.com/en/rest/metrics/traffic).
ENDPOINTS = {
    "views": "traffic/views?per=day",
    "clones": "traffic/clones?per=day",
    "referrers": "traffic/popular/referrers",
    "paths": "traffic/popular/paths",
}
ABOUT = [
    "Generated, never edited by hand: GitHub's own traffic figures for this repository as the weekly refresh "
    "read them, each covering the 14 days before `date`. Successive files overlap; count a day once.",
    "views and clones: totals, unique visitors, and one item per day (UTC). referrers: the ten sites GitHub saw "
    "send the most visitors. paths: the ten pages of the repository viewed most.",
    "No counter of this repository's own: the site and the MCP server collect nothing about their readers.",
]


def fetch(path: str, token: str) -> tuple[int, object]:
    """(HTTP status, parsed JSON body) for a GET with `token`; status 0 means
    no answer at all."""
    request = urllib.request.Request(
        f"{_github.API}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-jev",
            "Authorization": f"Bearer {token}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, json.loads(response.read() or b"null")
    except urllib.error.HTTPError as exc:
        return exc.code, None
    except (urllib.error.URLError, TimeoutError, ValueError):
        return 0, None


def read_traffic(repo: str, token: str) -> tuple[dict, list[str]]:
    """The four answers by name, and a line for each endpoint that gave none."""
    found: dict = {}
    failed: list[str] = []
    for name, endpoint in ENDPOINTS.items():
        status, body = fetch(f"/repos/{repo}/{endpoint}", token)
        if status == 200 and body is not None:
            found[name] = body
        else:
            why = {0: "no answer", 401: "token refused", 403: "token lacks Administration: read",
                   404: "repository not found for this token"}.get(status, f"HTTP {status}")
            failed.append(f"{name}: {why}")
    return found, failed


def summary(found: dict) -> str:
    """One line for the log and the step summary."""
    views, clones = found.get("views") or {}, found.get("clones") or {}
    top = ", ".join(f"{r.get('referrer')} {r.get('count')}" for r in (found.get("referrers") or [])[:3])
    return (
        f"traffic over 14 days: {views.get('count', 0)} views ({views.get('uniques', 0)} unique), "
        f"{clones.get('count', 0)} clones ({clones.get('uniques', 0)} unique)"
        + (f"; top referrers: {top}" if top else "")
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--date", help="the file's date (default: today, UTC)")
    args = parser.parse_args(argv)

    token = os.environ.get("TRAFFIC_TOKEN", "").strip()
    if not token:
        print("traffic: no TRAFFIC_TOKEN, so nothing is kept this week (docs/method.md says how to add one)")
        return 0
    # Actions sets GITHUB_REPOSITORY, so a fork keeps its own.
    repo = os.environ.get("GITHUB_REPOSITORY") or _github.SELF
    date = args.date or dt.datetime.now(dt.timezone.utc).date().isoformat()
    dt.date.fromisoformat(date)

    found, failed = read_traffic(repo, token)
    if failed:
        print(f"::error title=Traffic snapshot not kept::{'; '.join(failed)}")
        return 1
    snapshot = {"generated": SOURCE, "about": ABOUT, "date": date, "repository": repo, **found}
    path = ROOT / DIR / f"{date}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    line = summary(found)
    _github.step_summary(f"## Traffic\n\n{line}; kept in `{DIR.as_posix()}/{date}.json`.")
    print(f"{line}\nwrote {DIR.as_posix()}/{date}.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
