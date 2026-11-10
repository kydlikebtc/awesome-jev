#!/usr/bin/env python3
"""Read every product's GitHub stars once a day, for the board's rising list.

The launch board lists the products whose stars rose fastest over about a
week (launches.rising, docs/launches.md "Rising"). Until 2026-11-10 it
compared the two latest weekly refreshes in history/ (metadata.yml, on
Wednesdays), so the list on the board and in both READMEs moved once a week.
board-daily.yml runs this every day instead, and launches.readings() compares
the newest reading with the one closest to a week before it, so the list,
and the READMEs and site that show it, move every day.

It writes history/daily/<UTC date>.json:

  * a header saying it is generated, its date and what it holds;
  * `rows`: each product's slug and stars, in slug order, one line each, the
    shape rising() already reads from a weekly refresh.

A product is a row launches.is_product() accepts with a GitHub repository
(this repository's own rows aside, as in the weekly refresh). Stars come from
GitHub's GraphQL API, a hundred repositories a query: about a dozen requests
for the whole board, a point each, well inside GITHUB_TOKEN's budget. Nothing
else is read and nothing is written to catalog.json: licences, archive
status, dates and the notices they raise stay the Wednesday refresh's, and a
row's own `stars` keeps the Wednesday count.

A repository GitHub does not answer for (gone, renamed past following,
blocked) is left out of the day's reading, so it has no gain to show that day.
When fewer than half answer, nothing is written and the run fails, so a bad
day never stands in for a reading (retry.yml runs it once more). Readings
older than KEEP_DAYS are deleted: the list needs a week of them, and git's
history keeps the rest. A date before the newest reading is refused; running
twice on one day rewrites that day's file.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/daily_stars.py                  # history/daily/<today, UTC>.json
     python3 scripts/daily_stars.py --date 2026-11-10
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import launches  # noqa: E402
from _github import SELF, RateLimited, graphql_request, log_usage, repo_of, step_summary  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
DIR = launches.DAILY_DIR
FILE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.json$")
SOURCE = "scripts/daily_stars.py, run by .github/workflows/board-daily.yml"
ABOUT = [
    "Generated, never edited by hand, and not a source of truth: catalog.json is. One file per day, named by the "
    "UTC date it was read; files older than two weeks are deleted, and git's history keeps them.",
    "rows: each product's slug and its GitHub stars that day. The launch board's rising list compares the newest "
    "reading with the one closest to a week before it (scripts/launches.py, readings and rising).",
    "Stars are GitHub's count: a popularity signal, not a quality verdict.",
]
# Repositories per GraphQL query. Stars alone are cheap: a query of a hundred
# aliased lookups costs one point.
BATCH = 100
# Readings kept in history/daily/: two weeks, so a week-old reading is still
# there when a few days were missed.
KEEP_DAYS = 14
# The share of products GitHub must answer for before a reading is written.
MIN_SHARE = 0.5


def products(catalog: list[dict]) -> list[tuple[str, str]]:
    """(slug, owner/name) of every product with a GitHub repository, by slug."""
    out = []
    for row in catalog:
        repo = repo_of(row)
        if launches.is_product(row) and repo and repo.lower() != SELF.lower():
            out.append((row["slug"], repo))
    return sorted(out)


def query_for(batch: list[tuple[str, str]]) -> tuple[str, dict]:
    """One query for up to BATCH repositories, aliased r0, r1, …. Owners and
    names travel as variables, never pasted into the query text."""
    params, lookups, variables = [], [], {}
    for alias, (_, repo) in enumerate(batch):
        owner, name = repo.split("/", 1)
        variables[f"o{alias}"] = owner
        variables[f"n{alias}"] = name
        params.append(f"$o{alias}: String!, $n{alias}: String!")
        lookups.append(f"r{alias}: repository(owner: $o{alias}, name: $n{alias}) {{ stargazerCount }}")
    return f"query({', '.join(params)}) {{ rateLimit {{ cost remaining }} " + " ".join(lookups) + " }", variables


def read_stars(wanted: list[tuple[str, str]], ask=None) -> dict[str, int]:
    """slug -> stars for every product GitHub answered for. `ask` stands in
    for graphql_request in tests. A failed query or a spent budget costs its
    batch, never the run."""
    ask = graphql_request if ask is None else ask
    found: dict[str, int] = {}
    batches = [wanted[i:i + BATCH] for i in range(0, len(wanted), BATCH)]
    for number, batch in enumerate(batches, 1):
        try:
            answer = ask(*query_for(batch))
        except RateLimited:
            answer = None
        data = (answer or {}).get("data") or {}
        answered = 0
        for alias, (slug, _) in enumerate(batch):
            node = data.get(f"r{alias}")
            if isinstance(node, dict) and isinstance(node.get("stargazerCount"), int):
                found[slug] = node["stargazerCount"]
                answered += 1
        cost = data.get("rateLimit") or {}
        print(f"graphql batch {number}/{len(batches)}: {answered} of {len(batch)} answered"
              + (f", {cost.get('remaining')} points left" if cost else ", no answer"), file=sys.stderr)
    return found


def reading(date: str, stars: dict[str, int]) -> dict:
    return {
        "generated": True,
        "source": SOURCE,
        "about": ABOUT,
        "date": date,
        "rows": [{"slug": slug, "stars": stars[slug]} for slug in sorted(stars)],
    }


def render(payload: dict) -> str:
    """Indented JSON, one line per row, as history/'s weekly files are."""
    head = json.dumps({k: v for k, v in payload.items() if k != "rows"}, indent=2, ensure_ascii=False)
    rows = [json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in payload["rows"]]
    body = ",\n".join(f"    {line}" for line in rows)
    return head[:-2] + (f',\n  "rows": [\n{body}\n  ]\n}}\n' if rows else ',\n  "rows": []\n}\n')


def problems(name: str, payload: object) -> list[str]:
    """Why a file under history/daily/ is not a reading this script would write."""
    match = FILE.match(name)
    if not match:
        return [f"{name}: not named YYYY-MM-DD.json"]
    if not isinstance(payload, dict):
        return [f"{name}: not a JSON object"]
    found = []
    if payload.get("generated") is not True or payload.get("source") != SOURCE:
        found.append(f"{name}: header must say generated: true and source {SOURCE!r}")
    if payload.get("date") != match.group(1):
        found.append(f"{name}: date {payload.get('date')!r} is not the file's")
    rows = payload.get("rows")
    ok = isinstance(rows, list) and all(
        isinstance(r, dict) and set(r) == {"slug", "stars"} and isinstance(r["slug"], str)
        and isinstance(r["stars"], int) and not isinstance(r["stars"], bool) and r["stars"] >= 0
        for r in rows
    )
    slugs = [r["slug"] for r in rows] if ok else None
    if slugs is None or slugs != sorted(set(slugs)):
        found.append(f"{name}: rows must be {{slug, stars}} objects in slug order, each slug once")
    return found


def dates_in(folder: pathlib.Path) -> list[str]:
    return sorted(m.group(1) for p in folder.glob("*.json") if (m := FILE.match(p.name))) if folder.is_dir() else []


def write(path: pathlib.Path, text: str) -> None:
    """Replace the file in one step, so a crash never leaves half a reading."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".reading-", suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


def prune(folder: pathlib.Path, date: str) -> list[str]:
    """Delete the readings more than KEEP_DAYS before `date`; their names."""
    cut = (dt.date.fromisoformat(date) - dt.timedelta(days=KEEP_DAYS)).isoformat()
    gone = []
    for old in dates_in(folder):
        if old < cut:
            (folder / f"{old}.json").unlink()
            gone.append(old)
    return gone


def today() -> str:
    return dt.datetime.now(dt.timezone.utc).date().isoformat()


def main(argv: list[str] | None = None, *, ask=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--date", help="the reading's date, YYYY-MM-DD (default: today in UTC)")
    parser.add_argument("--catalog", type=pathlib.Path, default=CATALOG, help=argparse.SUPPRESS)
    parser.add_argument("--dir", type=pathlib.Path, default=DIR, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    date = args.date or today()
    try:
        dt.date.fromisoformat(date)
    except ValueError:
        print(f"error: --date {date!r} is not YYYY-MM-DD", file=sys.stderr)
        return 2
    held = dates_in(args.dir)
    if held and date < held[-1]:
        print(f"error: history/daily/ already has {held[-1]}; a reading is never dated before the newest one",
              file=sys.stderr)
        return 1
    wanted = products(json.loads(args.catalog.read_text(encoding="utf-8")))
    stars = read_stars(wanted, ask)
    if ask is None:
        log_usage()
    if len(stars) < MIN_SHARE * len(wanted):
        print(f"error: GitHub answered for {len(stars)} of {len(wanted)} products, under half; nothing written",
              file=sys.stderr)
        step_summary(f"### Daily star reading\n\nNot written: GitHub answered for {len(stars)} of "
                     f"{len(wanted)} products, under half.")
        return 1
    text = render(reading(date, stars))
    path = args.dir / f"{date}.json"
    before = path.read_text(encoding="utf-8") if path.exists() else None
    if before != text:
        write(path, text)
    gone = prune(args.dir, date)
    shown = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    line = (f"{shown}: {'unchanged' if before == text else 'rewritten' if before else 'written'}, "
            f"stars for {len(stars)} of {len(wanted)} products"
            + (f"; deleted {', '.join(gone)}" if gone else ""))
    print(line)
    step_summary(f"### Daily star reading\n\n{line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
