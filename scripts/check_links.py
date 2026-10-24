#!/usr/bin/env python3
"""Sweep every catalog URL and report which ones stopped resolving.

Read-only by default: it prints a report and exits non-zero when something is
dead, so a scheduled run opens a visible red build rather than silently
rewriting the catalog. Pass --write to stamp `checked` and `link_status` on the
rows that answered.

A refusal (401/403/429) is not a dead link, but a sweep where many are refused
has checked little. Refusals are counted for GitHub and for other hosts apart —
one is our token's budget, the other mostly Cloudflare-style bot walls — and
when more than REFUSAL_ALARM of either group refused, the sweep exits 3 and says
it was rate limited or blocked rather than looking like a quiet week. Every
count, and the GitHub budget spent, goes to the job summary.

Exit codes: 0 fine, 1 dead links, 3 too many refusals to trust a group.

A dead link is never deleted by this script. Moving a row to retired.json is a
judgement call — the row needs a `notes` line saying why — so a person does it.

`--markdown FILE` also writes the rows a person has to look at as an issue
body: the dead links, the redirects, and, when a group's refusals passed the
alarm, the refused links. links.yml keeps one issue open with it (since
2026-10-24): before that a red run on the Actions page was the sweep's only
signal, and it was red on each of its first four Mondays without anyone
being told.

Usage:
  python3 scripts/check_links.py               # report only
  python3 scripts/check_links.py --write       # also update checked/link_status
  python3 scripts/check_links.py --only youtube.com
  python3 scripts/check_links.py --markdown /tmp/body.md   # and write the issue body
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _github  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"

TIMEOUT = 20
WORKERS = 8

# The host refused *us*: not evidence the page is gone.
REFUSED = (401, 403, 429)
# More refused than this share of one group, and that group's sweep says more
# about the runner than the links. A share, not a count, so it keeps its
# meaning as the catalogue grows; judged per group so a week of Cloudflare walls
# cannot pass for GitHub rate-limiting us, or the reverse.
REFUSAL_ALARM = 0.20
# A share of a handful of URLs (a --only run) says nothing.
REFUSAL_MIN_GROUP = 20
GROUPS = ("GitHub", "other hosts")

# A bare repository root and nothing else. A /blob/ or /tree/ path must not
# match: see github_repo_status for why.
GITHUB_ROOT = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+?)/?$")

# A plain urllib request gets 403'd by a lot of CDNs. Look like a browser.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# Hosts that answer HEAD with a lie. Ask for GET on these.
GET_ONLY = (
    "medium.com",
    "youtube.com",
    "youtu.be",
    "x.com",
    "twitter.com",
    "forbes.com",
)


def github_repo_status(url: str) -> tuple[int, str] | None:
    """Check a GitHub repo root through the API. None means "not applicable".

    github.com's HTML answers 429 after a few dozen unauthenticated requests,
    so on an 800-row sweep most GitHub rows came back BLOK and never got
    stamped — the checker was rate-limiting itself into uselessness. The API
    with a token has a budget of its own (GitHub documents 1,000 requests an
    hour per repository for the workflow token); _github waits out a rate
    limit once, and after that a row is reported refused (429), not sent to
    github.com's HTML to collect another 429 there.

    Only a bare repo root qualifies. A /blob/ path still goes through HTTP,
    because /repos/{owner}/{name} answering 200 says nothing about whether
    that file still exists, and quietly swapping in the weaker check would
    make the sweep claim more than it verified.
    """
    if not _github.token():
        return None
    match = GITHUB_ROOT.match(url)
    if not match:
        return None

    try:
        status, _ = _github.api_fetch(f"/repos/{match.group(1)}/{match.group(2)}")
    except _github.RateLimited as exc:
        return 429, f"not checked: {exc}"
    if 200 <= status < 300:
        return status, ""
    # 404 here is real: the repo is gone or went private. Anything else
    # is about us, not the repo, so fall back to the HTML request.
    if status == 404:
        return 404, "repository not found via API"
    return None


def fetch_status(url: str) -> tuple[int, str]:
    """Return (status, note). Status 0 means the request never completed."""
    via_api = github_repo_status(url)
    if via_api is not None:
        return via_api

    method = "GET" if any(host in url for host in GET_ONLY) else "HEAD"

    for attempt in (method, "GET"):
        request = urllib.request.Request(url, headers=HEADERS, method=attempt)
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return response.status, ""
        except urllib.error.HTTPError as exc:
            # 405 means the host dislikes HEAD, not that the page is gone.
            if attempt == "HEAD" and exc.code in (403, 405, 400, 501):
                continue
            return exc.code, exc.reason or ""
        except urllib.error.URLError as exc:
            if attempt == "HEAD":
                continue
            return 0, str(exc.reason)
        except Exception as exc:  # noqa: BLE001 - a sweep must not die on one row
            if attempt == "HEAD":
                continue
            return 0, exc.__class__.__name__
    return 0, "unreachable"


def group_of(url: str) -> str:
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    return GROUPS[0] if host in ("github.com", "www.github.com") else GROUPS[1]


def pct(part: int, whole: int) -> str:
    return f"{part / whole:.0%}" if whole else "-"


def alarms(shares: dict[str, tuple[int, int]]) -> list[str]:
    """One sentence per group whose (refused, checked) is past the alarm."""
    out = []
    for name, (refused, total) in shares.items():
        if total >= REFUSAL_MIN_GROUP and refused > REFUSAL_ALARM * total:
            where = "GitHub URLs" if name == GROUPS[0] else "URLs on other hosts"
            out.append(
                f"{refused} of {total} {where} refused this checker "
                f"({pct(refused, total)} > {REFUSAL_ALARM:.0%}): that is rate limiting or "
                "blocking of this runner, not dead links. Rows that answered were "
                "stamped; the refused ones keep their previous date."
            )
    return out


def summary_markdown(counts: dict[str, dict[str, int]], shares, warnings: list[str], write: bool) -> str:
    stamped = " (stamped)" if write else ""
    lines = [
        "## Link sweep",
        "",
        "| | GitHub | Other hosts | All |",
        "| --- | ---: | ---: | ---: |",
    ]
    for label, key in (
        ("Checked", "checked"),
        (f"Answered 2xx{stamped}", "alive"),
        ("Redirected", "moved"),
        ("Refused (401/403/429)", "refused"),
        ("Dead", "dead"),
    ):
        gh, other = counts[GROUPS[0]][key], counts[GROUPS[1]][key]
        if key == "refused":
            cells = [f"{gh} ({pct(*shares[GROUPS[0]])})", f"{other} ({pct(*shares[GROUPS[1]])})"]
        else:
            cells = [str(gh), str(other)]
        lines.append(f"| {label} | {cells[0]} | {cells[1]} | {gh + other} |")
    lines.append("")
    lines += [f"- **{warning}**" for warning in warnings]
    lines += [f"- {line}" for line in _github.usage_lines()]
    return "\n".join(lines)


# One issue comment stays well under GitHub's 65,536-character limit.
ISSUE_ROWS = 150


def cell(text: object) -> str:
    """Text for one cell of a Markdown table: one line, no column breaks."""
    return " ".join(str(text).split()).replace("|", "\\|")


def issue_table(items: list[tuple], heading: str, advice: str) -> list[str]:
    """One section of the issue: a heading with its count, what to do, and a
    row per link (slug, HTTP status, URL, and the note, when there is one)."""
    lines = [f"### {heading} ({len(items)})", "", advice, "", "| Row | HTTP | URL |", "| --- | ---: | --- |"]
    for entry, status, *note in items[:ISSUE_ROWS]:
        why = f" ({cell(note[0])})" if note and note[0] else ""
        lines.append(f"| `{entry['slug']}` | {status or '---'} | <{cell(entry['url'])}>{why} |")
    if len(items) > ISSUE_ROWS:
        lines.append(f"\n…and {len(items) - ISSUE_ROWS} more, in the run's log.")
    return lines + [""]


def issue_markdown(dead: list, moved: list, blocked: list, warnings: list[str], counts: str) -> str:
    """The issue body links.yml posts: the rows a person has to act on, by
    what they have to do. The refused links are listed only when a group's
    refusals passed the alarm, since a handful refuse every week."""
    lines = [
        "A scheduled link sweep found links that need a person: a link that no longer",
        "resolves, a redirect, or a sweep refused so often that it checked little.",
        "",
    ]
    if dead:
        lines += issue_table(
            dead,
            "Dead links",
            "Open each one first: a site that is down for a day looks the same. A link that "
            "is gone moves its row to `retired.json` with a `notes` line saying why; a "
            "script never retires one.",
        )
    if moved:
        lines += issue_table(moved, "Redirects", "Update each row's `url` to where it now leads.")
    if warnings:
        lines += [f"**{warning}**" for warning in warnings] + [""]
        lines += issue_table(
            blocked,
            "Refused",
            "Not evidence that a page is gone: open them in a browser, and do not retire a "
            "row on a 401, 403 or 429 alone.",
        )
    lines += ["```", counts, "```", ""]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write", action="store_true", help="stamp checked/link_status on live rows"
    )
    parser.add_argument(
        "--only", default="", help="only check URLs containing this substring"
    )
    parser.add_argument(
        "--markdown", default="", metavar="FILE",
        help="also write the dead links, redirects and (past the alarm) refused links as an issue body",
    )
    args = parser.parse_args(argv)

    catalog = json.loads(CATALOG.read_text())
    targets = [entry for entry in catalog if args.only in entry["url"]]
    if not targets:
        print("nothing to check")
        _github.step_summary("## Link sweep\n\nNo catalogue URL matched; nothing was checked.")
        print("links: 0 checked")
        return 0

    print(f"checking {len(targets)} url(s) with {WORKERS} workers\n")
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(lambda entry: fetch_status(entry["url"]), targets))

    today = dt.date.today().isoformat()
    dead: list[tuple[dict, int, str]] = []
    moved: list[tuple[dict, int]] = []
    blocked: list[tuple[dict, int, str]] = []
    counts = {name: dict.fromkeys(("checked", "alive", "moved", "refused", "dead"), 0) for name in GROUPS}

    for entry, (status, note) in zip(targets, results):
        alive = 200 <= status < 300
        redirected = 300 <= status < 400
        # 401/403/429 mean the host refused *us*, which is not evidence the page
        # is gone. Forbes, Medium and anything behind Cloudflare answer this way
        # to every scripted request. Retiring those rows would be factually
        # wrong, so they are reported separately for a human to eyeball.
        refused = status in REFUSED

        if alive:
            mark = "ok  "
        elif redirected:
            mark = "--> "
        elif refused:
            mark = "BLOK"
        else:
            mark = "DEAD"
        detail = f" {note}" if note else ""
        print(f"  {mark} {status or '---'}  {entry['slug']}{detail}")

        tally = counts[group_of(entry["url"])]
        tally["checked"] += 1
        if alive:
            tally["alive"] += 1
            if args.write:
                entry["checked"] = today
                entry["link_status"] = status
        elif redirected:
            tally["moved"] += 1
            moved.append((entry, status))
        elif refused:
            tally["refused"] += 1
            blocked.append((entry, status, note))
        else:
            tally["dead"] += 1
            dead.append((entry, status, note))

    alive_total = len(targets) - len(dead) - len(moved) - len(blocked)
    if args.write:
        CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")
        print(f"\nstamped checked={today} on {alive_total} row(s)")

    print_lists(blocked, moved, dead)

    shares = {name: (tally["refused"], tally["checked"]) for name, tally in counts.items()}
    warnings = alarms(shares)
    for warning in warnings:
        print(f"\n{warning}")
    if not dead and not warnings:
        print("\nall links resolved")

    _github.step_summary(summary_markdown(counts, shares, warnings, args.write))
    _github.log_usage()
    # The last two lines are the counts, so a log's tail always carries them.
    (gh, gh_total), (other, other_total) = shares[GROUPS[0]], shares[GROUPS[1]]
    refusals = (
        f"refused: {gh} of {gh_total} GitHub URLs ({pct(gh, gh_total)}), "
        f"{other} of {other_total} on other hosts ({pct(other, other_total)})"
    )
    counts = (
        f"links: {len(targets)} checked: {alive_total} answered 2xx"
        + (" (stamped)" if args.write else "")
        + f", {len(moved)} redirected, {len(blocked)} refused, {len(dead)} dead"
    )
    if args.markdown:
        pathlib.Path(args.markdown).write_text(
            issue_markdown(dead, moved, blocked, warnings, f"{refusals}\n{counts}"), encoding="utf-8"
        )
    print(f"\n{refusals}")
    print(counts)
    if dead:
        return 1
    return 3 if warnings else 0


def print_lists(blocked: list, moved: list, dead: list) -> None:
    """The rows a person has to look at, by what they have to do."""
    if blocked:
        print(
            f"\n{len(blocked)} link(s) refused this checker but are probably fine. "
            "Open each in a browser; do NOT retire on a 403 alone:"
        )
        for entry, status, note in blocked:
            print(f"  {entry['slug']}  HTTP {status}  {entry['url']}  {note}")

    if moved:
        print(f"\n{len(moved)} redirect(s) — update `url` to the destination:")
        for entry, status in moved:
            print(f"  {entry['slug']}  HTTP {status}  {entry['url']}")

    if dead:
        print(
            f"\n{len(dead)} dead link(s). Move each to retired.json with a notes line saying why:"
        )
        for entry, status, note in dead:
            print(f"  {entry['slug']}  HTTP {status or '---'}  {entry['url']}  {note}")


if __name__ == "__main__":
    sys.exit(main())
