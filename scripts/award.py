#!/usr/bin/env python3
"""The year's decision award: one shortlist per decision pattern (L23 of the
2026-11-03 launch-board plan, docs/launches.md).

Jev entered early access on 2026-09-15, so the board's year runs from
15 September to the 14th of the next September, and the first award falls on
Jev's first anniversary, 2027-09-15. For each pattern in patterns.json this
draws up a shortlist from that year's closed launch weeks:

- the weeks whose Sunday falls inside the year;
- the launches still on the board (not held, not removed);
- only products whose call site a person or a model read (evidence tier
  `person` or `model`): an award for the decision a product makes needs
  someone to have read the code that makes it;
- each product once per pattern it is filed under, at its best week: the best
  rank, then the most counted votes, then the later week;
- the first SHORTLIST of them.

Votes order a shortlist; the evidence decides who may be on it. The award is
the first of each shortlist, by that same order, and the file says so for each
pattern: no person picks (2026-11-05, when the owner asked that no step of the
board wait for one). award.yml runs `--due` on the 15th of each month; on or
after the anniversary it writes docs/award/<year>.md, once, and pushes it.

Run:
  python3 scripts/award.py --year 2027           # the shortlists and the awards, as Markdown
  python3 scripts/award.py --year 2027 --write   # the same, into docs/award/2027.md
  python3 scripts/award.py --due                 # --write for the year just ended, if due and not written
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import launches  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Jev's early access began on 15 September 2026; each award year ends the day
# before the anniversary.
ANNIVERSARY = (9, 15)
FIRST_YEAR = 2027
SHORTLIST = 3
ELIGIBLE = ("person", "model")


def year_days(year: int) -> tuple[dt.date, dt.date]:
    """The first and last day of award year `year` (the one ending in it)."""
    month, day = ANNIVERSARY
    return dt.date(year - 1, month, day), dt.date(year, month, day) - dt.timedelta(days=1)


def shortlists(year: int, all_weeks: list[dict], catalog: list[dict], patterns: list[dict]) -> dict[str, list[dict]]:
    """{pattern key: up to SHORTLIST entries}, in patterns.json's order. Each
    entry: product, title, week, rank, votes, counted, evidence."""
    first, last = year_days(year)
    rows = {r["slug"]: r for r in catalog}
    best: dict[tuple[str, str], tuple[tuple, dict]] = {}
    for week in all_weeks:
        if week.get("status") != "closed" or not launches.WEEK.match(str(week.get("week"))):
            continue
        _, sunday = launches.week_days(week["week"])
        if not first <= sunday <= last:
            continue
        for launch in week.get("launches") or []:
            result = launch.get("result") or {}
            row = rows.get(launch.get("product"))
            if launch.get("status") != "scheduled" or not result.get("rank") or row is None:
                continue
            if not launches.is_product(row) or launches.tier(row) not in ELIGIBLE:
                continue
            order = (result["rank"], -float(result.get("counted") or 0), -sunday.toordinal())
            entry = {
                "product": row["slug"],
                "title": row.get("title") or row["slug"],
                "week": week["week"],
                "rank": result["rank"],
                "votes": result.get("votes", 0),
                "counted": result.get("counted", 0),
                "evidence": launches.tier(row),
            }
            for key in row.get("patterns") or []:
                if (key, row["slug"]) not in best or order < best[(key, row["slug"])][0]:
                    best[(key, row["slug"])] = (order, entry)
    out: dict[str, list[dict]] = {}
    for p in patterns:
        found = sorted(((o, e) for (k, _), (o, e) in best.items() if k == p["key"]), key=lambda x: (x[0], x[1]["product"]))
        out[p["key"]] = [e for _, e in found[:SHORTLIST]]
    return out


READER = {"person": "a person", "model": "a model"}


def render(year: int, lists: dict[str, list[dict]], patterns: list[dict]) -> str:
    first, last = year_days(year)
    lines = [
        f"# Decision award {year}",
        "",
        f"The launch board's year from {first} to {last}, drawn up by `scripts/award.py --year {year}` from the "
        "closed launch weeks on file. One shortlist per decision pattern: products a person or a model read the "
        "call site of, each at its best week, by rank and then counted votes. The award is the first of each "
        "shortlist, by that order; no person picks it. A place here is a count of votes among products whose code "
        "someone read, not this catalogue's recommendation.",
        "",
    ]
    for p in patterns:
        lines += [f"## {p['en']} (`{p['key']}`)", ""]
        entries = lists.get(p["key"]) or []
        if not entries:
            lines += ["No eligible launch this year, so no award.", ""]
            continue
        top = entries[0]
        lines += [
            f"**Award: [{top['title']}]({launches.query.SITE}products/{top['product']}.html).** "
            f"Its best week was {top['week']}, where it placed #{top['rank']} with {top['counted']} counted votes, "
            f"the best of the products filed under this pattern; {READER[top['evidence']]} read its call site.",
            "",
            "Shortlist:",
            "",
        ]
        for i, e in enumerate(entries, start=1):
            lines.append(
                f"{i}. [{e['title']}]({launches.query.SITE}products/"
                f"{e['product']}.html): #{e['rank']} in {e['week']}, {e['votes']} votes, {e['counted']} counted; "
                f"evidence: {e['evidence']}"
            )
        lines.append("")
    return "\n".join(lines)


def due_year(today: dt.date) -> int | None:
    """The award year whose anniversary has passed by `today` (the year just
    ended), or None before the first."""
    month, day = ANNIVERSARY
    year = today.year if (today.month, today.day) >= (month, day) else today.year - 1
    return year if year >= FIRST_YEAR else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--year", type=int, help=f"the award year, from {FIRST_YEAR}")
    which.add_argument("--due", action="store_true",
                       help="write the award for the year just ended, if its anniversary has passed and it is not written")
    parser.add_argument("--write", action="store_true", help="with --year: write docs/award/<year>.md")
    parser.add_argument("--on", metavar="DAY", help="today, for --due (default: the clock, UTC)")
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    root = pathlib.Path(args.root)
    if args.due:
        today = launches.day(args.on) if args.on else dt.datetime.now(dt.timezone.utc).date()
        if today is None:
            parser.error(f"--on takes a day like 2027-09-15, not {args.on!r}")
        year = due_year(today)
        if year is None or (root / "docs" / "award" / f"{year}.md").exists():
            print(f"no award is due on {today}" + (f": {year}'s is written" if year else ""))
            return 0
        args.year, args.write = year, True
    if args.year < FIRST_YEAR:
        parser.error(f"the first award year is {FIRST_YEAR}")
    catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    patterns = json.loads((root / "patterns.json").read_text(encoding="utf-8"))["patterns"]
    all_weeks = launches.weeks(root / "launches")
    text = render(args.year, shortlists(args.year, all_weeks, catalog, patterns), patterns)
    if args.write:
        path = root / "docs" / "award" / f"{args.year}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
        print(f"wrote {path.relative_to(root)}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
