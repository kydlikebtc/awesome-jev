#!/usr/bin/env python3
"""The launch board's rules, in one place (docs/launches.md; since 2026-11-03).

The catalogue stays the full index. The board is a layer over it: once a week a
product's maker (or a hunter) launches a catalogued row, people vote with a
thumbs-up on the launch's GitHub Discussion, and the week closes with a rank.
Votes say how many people cared; the evidence the catalogue already records
says whether the product calls Jev. The two are shown side by side and never
added into one score, so a rank is never read as the catalogue's endorsement.

Everything the site, the vote reader and the checks decide about the board is
decided here, so the three cannot drift apart:

  * which rows can be on it (eligible), and which are quiet (inactive, T2)
  * the evidence tier a launch shows (tier), read from the same fields the
    other surfaces read (query.reading, query.evidence_kind)
  * who a row's makers are (makers_of)
  * the ISO weeks the board runs in (week_of, week_days)
  * how votes are weighted and a week is ranked (weigh, rank; RULES)

What launches/*.json and makers/*.json may hold, beyond what the schemas can
say, is checked by scripts/check_launches.py with these rules. It lives apart
so that the site build, which imports this module, does not import lint.py.

Dates come from the data, never from the clock: the newest day the catalogue
records stands for "now" (as_of), so two builds of the same files write the
same bytes, as the plain pages already promise (site_pages.py).

Stdlib only, like the rest of scripts/.

Run: python3 scripts/launches.py --new            # the rows the board lists this week
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
from typing import Iterable

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from site_api import query  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LAUNCH_DIR = ROOT / "launches"
MAKER_DIR = ROOT / "makers"
LAUNCH_SCHEMA = ROOT / "schema" / "launch.schema.json"
MAKER_SCHEMA = ROOT / "schema" / "maker.schema.json"

# The kinds a product can be. Articles, videos, tutorials, benchmarks and the
# rest stay in the catalogue; they are not launched.
BOARD_KINDS = ("project", "plugin", "sdk", "integration")

# A row whose repository has seen no push in this many days before as_of() is
# quiet (T2 of the 2026-10-30 plan): it stays catalogued and keeps its page,
# but the board does not list it as new.
QUIET_DAYS = 60

# A product launches at most once in this many days.
RELAUNCH_DAYS = 60

# Evidence tiers, strongest first: a person read the call site; only a model
# did; a script found Jev's request or answer in the cited file and nobody has
# read it; no file is cited.
TIERS = ("person", "model", "file", "none")

# How votes count. A rule is never changed in place: a new one gets the next
# name, and a closed week records the one it was counted under.
#   own:       votes from the product's makers and the launch's submitter
#   young_days: an account younger than this when it voted ...
#   young:     ... counts this much
RULES = {
    "v1": {"own": 0.0, "young_days": 30, "young": 0.5},
}
CURRENT_RULES = "v1"

BADGES = ("week-1", "week-2", "week-3")

LOGIN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")
GITHUB_PROFILE = re.compile(r"^https://github\.com/([A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?)/?$")
WEEK = re.compile(r"^(\d{4})-W(\d{2})$")
DAY = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# --------------------------------------------------------------------------
# Rows
# --------------------------------------------------------------------------


def is_product(row: dict) -> bool:
    """A row that can be launched: a project, plugin, SDK or integration with
    code, that is an example of deciding with Jev (no not-jev or
    shadow-mode-only flag)."""
    return (
        row.get("kind") in BOARD_KINDS
        and bool(row.get("has_code"))
        and not set(row.get("flags") or []) & query.DISQUALIFYING
    )


def tier(row: dict) -> str:
    """The evidence tier the board shows for a row (TIERS)."""
    if query.evidence_kind(row) is None:
        return "none"
    return query.read_by(row.get("evidence")) or "file"


def day(value: object) -> dt.date | None:
    """The date at the start of an ISO date or timestamp string, or None."""
    if isinstance(value, str) and DAY.match(value[:10]):
        try:
            return dt.date.fromisoformat(value[:10])
        except ValueError:
            return None
    return None


def as_of(catalog: Iterable[dict]) -> dt.date | None:
    """The newest day the catalogue records (a row's first_seen or the day its
    link was checked): what the board treats as today."""
    days = [d for row in catalog for d in (day(row.get("first_seen")), day(row.get("checked"))) if d]
    return max(days) if days else None


def quiet(row: dict, today: dt.date | None) -> bool:
    """True when the row's repository has had no push for QUIET_DAYS before
    `today`. A row with no recorded push date is not called quiet."""
    pushed = day(row.get("repo_pushed_at"))
    return bool(pushed and today and (today - pushed).days > QUIET_DAYS)


def makers_of(row: dict) -> list[str]:
    """The GitHub logins whose maker page lists a row: its `makers`, or else the
    login in author.url when that is a GitHub profile."""
    if row.get("makers"):
        return list(row["makers"])
    match = GITHUB_PROFILE.match(str((row.get("author") or {}).get("url") or ""))
    return [match.group(1)] if match else []


def login_key(login: str) -> str:
    """GitHub logins are case-insensitive; pages and files use lower case."""
    return login.lower()


# --------------------------------------------------------------------------
# Weeks
# --------------------------------------------------------------------------


def week_of(date: dt.date) -> str:
    year, week, _ = date.isocalendar()
    return f"{year}-W{week:02d}"


def week_days(week: str) -> tuple[dt.date, dt.date]:
    """Monday and Sunday of an ISO week id."""
    match = WEEK.match(week)
    if not match:
        raise ValueError(f"not an ISO week: {week!r}")
    monday = dt.date.fromisocalendar(int(match.group(1)), int(match.group(2)), 1)
    return monday, monday + dt.timedelta(days=6)


def new_this_week(catalog: list[dict]) -> tuple[str | None, list[dict]]:
    """The newest ISO week any product entered the catalogue, and the products
    first seen in it that are not quiet, strongest evidence first, then by
    stars and title. This is what the board lists before any launch has been
    voted on, and it is an order, not a ranking."""
    today = as_of(catalog)
    products = [r for r in catalog if is_product(r) and day(r.get("first_seen"))]
    if not products:
        return None, []
    newest = week_of(max(day(r["first_seen"]) for r in products))
    rows = [r for r in products if week_of(day(r["first_seen"])) == newest and not quiet(r, today)]
    return newest, sorted(rows, key=lambda r: (TIERS.index(tier(r)), *query.sort_key(r)))


# --------------------------------------------------------------------------
# Votes
# --------------------------------------------------------------------------


def weigh(votes: list[dict], *, own: Iterable[str], week: str, rules: str = CURRENT_RULES) -> dict:
    """Count one launch's votes under `rules`.

    A vote is {"login", "at", "account_created"} (timestamps, as the Discussion
    reader writes them). Only votes cast inside the week count at all; a login
    counts once. `own` are the logins whose votes are the product's own (its
    makers and the submitter)."""
    rule = RULES[rules]
    monday, sunday = week_days(week)
    mine = {login_key(x) for x in own}
    seen: set[str] = set()
    counted = 0.0
    n = discounted = 0
    for vote in sorted(votes, key=lambda v: (str(v.get("at")), str(v.get("login")))):
        login = str(vote.get("login") or "")
        cast = day(vote.get("at"))
        if not login or login_key(login) in seen or not cast or not monday <= cast <= sunday:
            continue
        seen.add(login_key(login))
        n += 1
        weight = 1.0
        if login_key(login) in mine:
            weight = rule["own"]
        else:
            born = day(vote.get("account_created"))
            if born is None or (cast - born).days < rule["young_days"]:
                weight = rule["young"]
        if weight < 1:
            discounted += 1
        counted += weight
    return {"votes": n, "counted": round(counted, 2), "discounted": discounted}


def rank(launches: list[dict], catalog: dict[str, dict]) -> list[dict]:
    """Rank the scheduled launches of a week by their counted votes; ties go to
    the stronger evidence, then the earlier submission, then the slug. Each
    launch needs `result` with `counted`; returns them in order with `rank`
    and, for the top three with a vote counted, a badge."""
    on_board = [x for x in launches if x.get("status") == "scheduled"]

    def key(x: dict) -> tuple:
        row = catalog.get(x["product"], {})
        return (-x["result"]["counted"], TIERS.index(tier(row)), x["submitted_on"], x["product"])

    ordered = sorted(on_board, key=key)
    for place, launch in enumerate(ordered, start=1):
        launch["result"]["rank"] = place
        badges = [BADGES[place - 1]] if place <= len(BADGES) and launch["result"]["counted"] > 0 else []
        if badges:
            launch["result"]["badges"] = badges
        else:
            launch["result"].pop("badges", None)
    return ordered


# --------------------------------------------------------------------------
# Files
# --------------------------------------------------------------------------


def load_dir(directory: pathlib.Path) -> dict[str, object]:
    """Every *.json file directly in `directory`, by name without .json; a file
    that does not parse is kept as the error text."""
    out: dict[str, object] = {}
    if not directory.is_dir():
        return out
    for path in sorted(directory.glob("*.json")):
        try:
            out[path.stem] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            out[path.stem] = f"does not parse: {exc}"
    return out


def weeks(directory: pathlib.Path = LAUNCH_DIR) -> list[dict]:
    """The launch weeks on file that parse, oldest first."""
    found = load_dir(directory)
    return [found[k] for k in sorted(found) if isinstance(found[k], dict)]


def makers(directory: pathlib.Path = MAKER_DIR) -> dict[str, dict]:
    """The maker profiles on file that parse, by lower-case login."""
    return {login_key(k): v for k, v in load_dir(directory).items() if isinstance(v, dict)}


def launched(all_weeks: list[dict]) -> dict[str, list[tuple[str, dict]]]:
    """For each product slug, its launches on the board (week, launch), oldest
    first. Held and removed launches are not shown anywhere but the file."""
    out: dict[str, list[tuple[str, dict]]] = {}
    for week in sorted(all_weeks, key=lambda w: str(w.get("week"))):
        for launch in week.get("launches") or []:
            if launch.get("status") == "scheduled":
                out.setdefault(launch["product"], []).append((week["week"], launch))
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--new", action="store_true", help="print the products the board lists this week")
    parser.parse_args(argv)
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    week, rows = new_this_week(catalog)
    print(f"{week}: {len(rows)} product(s)")
    for row in rows:
        print(f"  {tier(row):6} ★{row.get('stars') or 0:<5} {row['slug']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
