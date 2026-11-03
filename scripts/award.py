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

Votes order a shortlist; the evidence decides who may be on it. The award
itself is a person's choice from the shortlist, written with its reasons in
docs/award/<year>.md. This script never writes that file, and never picks.

Run:
  python3 scripts/award.py --year 2027        # the shortlists, as Markdown
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


def render(year: int, lists: dict[str, list[dict]], patterns: list[dict]) -> str:
    first, last = year_days(year)
    lines = [
        f"# Decision award {year}: shortlists",
        "",
        f"The launch board's year from {first} to {last}, drawn up by `scripts/award.py --year {year}` from the "
        "closed launch weeks on file. One shortlist per decision pattern: products a person or a model read the "
        "call site of, each at its best week, by rank and then counted votes. The award is a person's choice from "
        "a shortlist, with reasons; a place here is not a recommendation.",
        "",
    ]
    for p in patterns:
        lines += [f"## {p['en']} (`{p['key']}`)", ""]
        entries = lists.get(p["key"]) or []
        if not entries:
            lines += ["No eligible launch this year.", ""]
            continue
        for i, e in enumerate(entries, start=1):
            lines.append(
                f"{i}. [{e['title']}]({launches.query.SITE}products/"
                f"{e['product']}.html): #{e['rank']} in {e['week']}, {e['votes']} votes, {e['counted']} counted; "
                f"evidence: {e['evidence']}"
            )
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--year", type=int, required=True, help=f"the award year, from {FIRST_YEAR}")
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.year < FIRST_YEAR:
        parser.error(f"the first award year is {FIRST_YEAR}")
    root = pathlib.Path(args.root)
    catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    patterns = json.loads((root / "patterns.json").read_text(encoding="utf-8"))["patterns"]
    all_weeks = launches.weeks(root / "launches")
    print(render(args.year, shortlists(args.year, all_weeks, catalog, patterns), patterns))
    return 0


if __name__ == "__main__":
    sys.exit(main())
