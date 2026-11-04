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
  * what a closed week is measured by (week_measures, gate_streak; L28)

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
import importlib.util
import json
import pathlib
import re
import sys
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUERY = ROOT / "src" / "awesome_jev_mcp" / "query.py"


def _load_query():
    """src/awesome_jev_mcp/query.py by its path, under the name site_api.py
    loads it by, so both share one module. Standard library only: the board's
    rules need nothing else from this repository (docs/launch-engine.md)."""
    name = "awesome_jev_query"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, QUERY)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


query = _load_query()
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

# A launch submitted by this day of the week (Monday is 0), 23:59 UTC, is for
# next week; later, the week after (docs/launches.md "The week").
LAST_DAY = 3

# Evidence tiers, strongest first (query.LAUNCH_TIERS, which the MCP server's
# launch tools and the site's api/v1/launches.json read too).
TIERS = query.LAUNCH_TIERS

# How votes count. A rule is never changed in place: a new one gets the next
# name, and a closed week records the one it was counted under.
#   own:       votes from the product's makers and the launch's submitter
#   young_days: an account younger than this when it voted ...
#   young:     ... counts this much
#   ring_votes, ring_share: a launch with at least ring_votes votes, at least
#              ring_share of them from such young (or unreadable) accounts, is
#              held for a person when the week closes instead of ranked (L14)
RULES = {
    "v1": {"own": 0.0, "young_days": 30, "young": 0.5, "ring_votes": 10, "ring_share": 0.5},
}
CURRENT_RULES = "v1"

BADGES = ("week-1", "week-2", "week-3")

# When the board moves from one a week to one a day (L16 of the 2026-11-03
# plan): after DAILY_WEEKS closed weeks in a row with at least DAILY_LAUNCHES
# launches on the board each. Until then a day's board would be nearly empty.
DAILY_WEEKS = 4
DAILY_LAUNCHES = 20

# What the 2026-11-03 plan measures the board by (its "指标" and gate G2;
# L28). The north star: launches a week with at least NORTH_STAR_VOTES
# counted votes. G2: GATE_WEEKS closed weeks in a row, each with at least
# GATE_LAUNCHES launches on the board and GATE_VOTERS accounts whose vote
# counted. The weeks keep only the counts (voters, returning_voters,
# tier_at_open), never who voted.
NORTH_STAR_VOTES = 5
GATE_WEEKS = 4
GATE_LAUNCHES = 10
GATE_VOTERS = 50
READ = ("person", "model")

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
    """The evidence tier the board shows for a row (TIERS; query.launch_tier)."""
    return query.launch_tier(row)


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


def week_for(day: dt.date) -> str:
    """The week a launch submitted on `day` (UTC) is for: next week through
    LAST_DAY, the week after from then on."""
    monday = day - dt.timedelta(days=day.weekday())
    return week_of(monday + dt.timedelta(weeks=1 if day.weekday() <= LAST_DAY else 2))


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


def counted_voters(votes: list[dict], *, own: Iterable[str], week: str, rules: str = CURRENT_RULES) -> set[str]:
    """The lower-case logins whose vote on one launch counted for something
    under `rules`, taken as weigh() takes them: cast inside the week, once per
    login. Only the close uses them, to count a week's accounts; no file
    keeps them."""
    rule = RULES[rules]
    monday, sunday = week_days(week)
    mine = {login_key(x) for x in own}
    seen: set[str] = set()
    out: set[str] = set()
    for vote in sorted(votes, key=lambda v: (str(v.get("at")), str(v.get("login")))):
        login = login_key(str(vote.get("login") or ""))
        cast = day(vote.get("at"))
        if not login or login in seen or not cast or not monday <= cast <= sunday:
            continue
        seen.add(login)
        if login in mine:
            weight = rule["own"]
        else:
            born = day(vote.get("account_created"))
            weight = rule["young"] if born is None or (cast - born).days < rule["young_days"] else 1.0
        if weight > 0:
            out.add(login)
    return out


def young_votes(votes: list[dict], *, own: Iterable[str], week: str, rules: str = CURRENT_RULES) -> tuple[int, int]:
    """(votes from accounts younger than the rule allows or of unreadable age,
    votes) among those weigh() counts, the product's own left out of both."""
    rule = RULES[rules]
    monday, sunday = week_days(week)
    mine = {login_key(x) for x in own}
    seen: set[str] = set()
    young = n = 0
    for vote in sorted(votes, key=lambda v: (str(v.get("at")), str(v.get("login")))):
        login = login_key(str(vote.get("login") or ""))
        cast = day(vote.get("at"))
        if not login or login in seen or not cast or not monday <= cast <= sunday:
            continue
        seen.add(login)
        if login in mine:
            continue
        n += 1
        born = day(vote.get("account_created"))
        if born is None or (cast - born).days < rule["young_days"]:
            young += 1
    return young, n


def ring(votes: list[dict], *, own: Iterable[str], week: str, rules: str = CURRENT_RULES) -> str | None:
    """Why a launch's votes look like a ring of new accounts, or None (L14).
    A heuristic: it holds the launch for a person, who decides."""
    rule = RULES[rules]
    young, n = young_votes(votes, own=own, week=week, rules=rules)
    if n >= rule["ring_votes"] and young >= rule["ring_share"] * n:
        return (f"{young} of {n} votes came from accounts younger than {rule['young_days']} days "
                "or of unknown age; held for a person before it ranks")
    return None


def shuffled(launch_list: list[dict], week: str) -> list[dict]:
    """A running week's launches in an order fixed by the week and the slugs,
    so no launch sits on top because it came first and two builds agree. The
    board and the order the vote posts are created in both use it, and so do
    the MCP server and api/v1/launches.json (query.launch_order)."""
    return query.launch_order(launch_list, week)


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


def hunters(all_weeks: list[dict]) -> list[tuple[str, int, int]]:
    """(login, launches, top three) for everyone who launched someone else's
    product in a closed week, most launches first, then most placings, then by
    login (L21). A launch that was held or removed is not counted."""
    shown: dict[str, str] = {}
    counts: dict[str, list[int]] = {}
    for week in all_weeks:
        if week.get("status") != "closed":
            continue
        for launch in week.get("launches") or []:
            if launch.get("status") != "scheduled" or launch.get("role") != "hunter":
                continue
            key = login_key(str(launch.get("submitted_by") or ""))
            if not key:
                continue
            shown.setdefault(key, launch["submitted_by"])
            tally = counts.setdefault(key, [0, 0])
            tally[0] += 1
            tally[1] += 1 if (launch.get("result") or {}).get("badges") else 0
    return sorted(((shown[k], n, top) for k, (n, top) in counts.items()), key=lambda h: (-h[1], -h[2], login_key(h[0])))


def on_board(week: dict) -> list[dict]:
    """A week's launches on the board: neither held nor removed."""
    return [x for x in week.get("launches") or [] if x.get("status") == "scheduled"]


def _streak(all_weeks: list[dict], test) -> int:
    """How many closed weeks in a row, ending with the newest closed one, pass
    `test`. A week with no file breaks the run like one that fails."""
    closed = sorted((w for w in all_weeks if w.get("status") == "closed" and WEEK.match(str(w.get("week")))),
                    key=lambda w: w["week"], reverse=True)
    streak, expected = 0, None
    for week in closed:
        monday, _ = week_days(week["week"])
        if expected is not None and monday != expected:
            break
        if not test(week):
            break
        streak += 1
        expected = monday - dt.timedelta(days=7)
    return streak


def daily_streak(all_weeks: list[dict]) -> int:
    """How many closed weeks in a row, ending with the newest closed one, had
    at least DAILY_LAUNCHES launches on the board. A week with no file breaks
    the run like a short one. DAILY_WEEKS of them means the daily board is due
    (L16)."""
    return _streak(all_weeks, lambda w: len(on_board(w)) >= DAILY_LAUNCHES)


def gate_streak(all_weeks: list[dict]) -> int:
    """How many closed weeks in a row, ending with the newest closed one, had
    at least GATE_LAUNCHES launches on the board and GATE_VOTERS accounts
    whose vote counted (G2 of the 2026-11-03 plan, met at GATE_WEEKS). A week
    closed before the close counted its accounts fails it."""
    return _streak(all_weeks, lambda w: len(on_board(w)) >= GATE_LAUNCHES
                   and int(w.get("voters") or 0) >= GATE_VOTERS)


def week_measures(week: dict) -> dict:
    """What a closed week is measured by (L28): its launches on the board; the
    accounts whose vote counted, and how many of them also voted the week
    before, as the close counted them (None when it did not); how many
    launches reached NORTH_STAR_VOTES counted votes (the plan's north star);
    how many launches a person or a model had read when they opened, of
    those whose tier at opening is on file; and the votes cast on the board
    and how many of them counted for less than one."""
    on = on_board(week)
    known = [x for x in on if x.get("tier_at_open") in TIERS]
    results = [x.get("result") or {} for x in on]
    return {
        "week": week.get("week"),
        "launches": len(on),
        "voters": week.get("voters"),
        "returning_voters": week.get("returning_voters"),
        "north_star": sum(1 for r in results if float(r.get("counted") or 0) >= NORTH_STAR_VOTES),
        "read_at_open": sum(1 for x in known if x["tier_at_open"] in READ),
        "tier_known": len(known),
        "votes": sum(int(r.get("votes") or 0) for r in results),
        "discounted": sum(int(r.get("discounted") or 0) for r in results),
    }


def relaunch_from(week: str) -> dt.date:
    """The first Monday a product launched in `week` may launch again: at
    least RELAUNCH_DAYS after that week's Monday."""
    monday, _ = week_days(week)
    return monday + dt.timedelta(days=-(-RELAUNCH_DAYS // 7) * 7)


def launch_again(history: list[tuple[str, dict]], weeks_by_id: dict[str, dict],
                 today: dt.date | None) -> tuple[str, dt.date | None]:
    """Whether a product with these launches (launched(), oldest first) can
    launch again: ("now", None) when it never launched, or its last week
    closed and a launch submitted `today` would be for a week at least
    RELAUNCH_DAYS on; ("from", Monday) when its last week closed too recently;
    ("on", None) while its last week is still on the board. With no `today`
    the rule cannot be read, so a closed last week counts as "now": the check
    on the issue says if it is early."""
    if not history:
        return "now", None
    last = history[-1][0]
    if (weeks_by_id.get(last) or {}).get("status") != "closed":
        return "on", None
    again = relaunch_from(last)
    if today is not None and week_days(week_for(today))[0] < again:
        return "from", again
    return "now", None


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
