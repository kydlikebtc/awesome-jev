#!/usr/bin/env python3
"""Open a launch week, and close the one before it (docs/launches.md).

L12, L13 and L14 of the 2026-11-03 launch-board plan. launch-week.yml runs
`--monday` early every Monday (UTC):

- **close** last week, if it is open: read each launch's thumbs-up votes from
  its Discussion (launch_votes.py), weigh them under the current rules
  (launches.weigh), hold any launch whose votes look like a ring of new
  accounts for a person (launches.ring, L14), rank the rest (launches.rank,
  with badges for the top three), and write the results, `closed_on` and
  `rules` into launches/<week>.json;
- **open** this week, if it is scheduled: for each launch on the board, find or
  create its vote post in the Discussion category named `Launches`, write the
  post's number, and mark the week open.

Only counts are written, never who voted. A post is found again by a marker in
its body before one is created, so a run that stopped halfway can simply run
again; a mutation is sent once and never retried (_github.graphql_mutation).

Nothing happens when there is nothing to do: no file for the week, or a week
already opened or closed. Turning Discussions on and adding the `Launches`
category (maintainers only) is the owner's; until then opening a week with
launches on it fails, and says so.

`--probe` (launch-probe.yml, by hand) starts one discussion in the category
and deletes it at once: the check that the workflow's own token may post in a
category only maintainers can start discussions in, before a Monday needs it.

Usage:
  python3 scripts/launch_week.py --monday                # what launch-week.yml runs
  python3 scripts/launch_week.py --probe                 # what launch-probe.yml runs
  python3 scripts/launch_week.py --open 2026-W47
  python3 scripts/launch_week.py --close 2026-W46 [--on 2026-11-23]   # or count it again
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
from typing import Callable

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _github  # noqa: E402
import launch_votes  # noqa: E402
import launches as L  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = L.query.SITE
DOCS = L.query.LAUNCHES_DOC
CATEGORY = "Launches"
MAX_PAGES = 10

REPO_QUERY = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    id
    hasDiscussionsEnabled
    discussionCategories(first: 50) { nodes { id name } }
  }
}
"""

POSTS_QUERY = """
query($owner: String!, $name: String!, $category: ID!, $after: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $after, categoryId: $category) {
      pageInfo { hasNextPage endCursor }
      nodes { number body author { login } }
    }
  }
}
"""

CREATE = """
mutation($repository: ID!, $category: ID!, $title: String!, $body: String!) {
  createDiscussion(input: {repositoryId: $repository, categoryId: $category, title: $title, body: $body}) {
    discussion { id number url }
  }
}
"""

DELETE = """
mutation($id: ID!) {
  deleteDiscussion(input: {id: $id}) {
    discussion { number }
  }
}
"""

PROBE_TITLE = "Probe: can the launch-week workflow post here? (deleted at once)"
PROBE_BODY = (
    "launch-probe.yml started this discussion to check that the workflow's own token may start one in "
    "the `Launches` category, and deletes it straight away. If you can still read it, the deletion "
    "failed: a maintainer can delete it by hand. How the board works: " + DOCS
)

Ask = Callable[[str, dict], "dict | None"]


class WeekError(Exception):
    """Something only a person can fix; the message says what."""


def marker(week: str, slug: str) -> str:
    return f"<!-- launch {week} {slug} -->"


MARKER = re.compile(r"<!-- launch (\d{4}-W\d{2}) ([a-z0-9-]+) -->")
SPECIAL = re.compile(r"([\\`*_{}\[\]<>()#+!|~])")


def plain(text: str) -> str:
    """User text made inert in Markdown: no formatting, no link, no @mention."""
    return SPECIAL.sub(r"\\\1", " ".join(str(text).split())).replace("@", "@​")


TIER_TEXT = {
    "person": "a person read the call site",
    "model": "a model read the call site",
    "file": "a script matched a Jev call in the cited file",
    "none": "no call site is cited yet",
}


def post(week: str, launch: dict, row: dict) -> tuple[str, str]:
    """The title and body of a launch's vote post."""
    monday, sunday = L.week_days(week)
    title = f"{row.get('title') or launch['product']} · {launch['tagline']}"[:250]
    lines = [
        marker(week, launch["product"]),
        f"**{plain(launch['tagline'])}**",
    ]
    if launch.get("tagline_zh"):
        lines += ["", plain(launch["tagline_zh"])]
    lines += [
        "",
        f"- Its page: {SITE}products/{launch['product']}.html",
        f"- Code: {row.get('repo') or row.get('url')}",
        f"- Evidence: {TIER_TEXT[L.tier(row)]}",
        f"- Launched by its {launch['role']}, {launch['submitted_by']} (#{launch['issue']})",
        "",
        f"**A thumbs-up on this post is a vote.** Votes cast from Monday {monday} to Sunday {sunday} (UTC) "
        "count, one per account. The maker's and the submitter's own count for nothing, and an account "
        "younger than 30 days counts half (rules v1). When the week closes, the counts are written to the "
        "repository; who voted is not.",
        "",
        "Votes and the catalogue's evidence are shown apart and never added together. A rank is a count "
        f"of votes, not this catalogue's recommendation, and nothing here is affiliated with TypeSafe AI. "
        f"How the board works: {DOCS}",
        "",
    ]
    return title, "\n".join(lines)


def load_week(root: pathlib.Path, week: str) -> dict | None:
    path = root / "launches" / f"{week}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def save_week(root: pathlib.Path, data: dict) -> None:
    path = root / "launches" / f"{data['week']}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rows_by_slug(root: pathlib.Path) -> dict[str, dict]:
    return {r["slug"]: r for r in json.loads((root / "catalog.json").read_text(encoding="utf-8"))}


# --------------------------------------------------------------------------
# Opening
# --------------------------------------------------------------------------


def category(repository: str, ask: Ask) -> tuple[str, str]:
    """(repository id, the Launches category's id)."""
    owner, name = repository.split("/", 1)
    answer = ask(REPO_QUERY, {"owner": owner, "name": name}) or {}
    repo = (answer.get("data") or {}).get("repository")
    if not repo:
        raise WeekError(f"could not read {repository} over GraphQL")
    if not repo.get("hasDiscussionsEnabled"):
        raise WeekError(f"Discussions are off in {repository}; the owner turns them on (MAINTAINING.md)")
    for node in (repo.get("discussionCategories") or {}).get("nodes") or []:
        if node.get("name") == CATEGORY:
            return repo["id"], node["id"]
    raise WeekError(f"{repository} has no Discussion category named {CATEGORY!r}; the owner adds one "
                    "in which only maintainers can start a discussion (MAINTAINING.md)")


# Who may have made a vote post: the workflow's token, or the owner running
# this by hand. A post anyone else started is never taken for one, marker or
# not, so the category stays safe even in a format anyone can post in.
POSTERS = {"github-actions", "github-actions[bot]"}


def existing_posts(repository: str, category_id: str, ask: Ask) -> dict[tuple[str, str], int]:
    """The vote posts already in the category, by (week, slug): posts with a
    launch marker started by POSTERS or the repository's owner."""
    owner, name = repository.split("/", 1)
    posters = POSTERS | {owner.lower()}
    found: dict[tuple[str, str], int] = {}
    after = None
    for _ in range(MAX_PAGES):
        answer = ask(POSTS_QUERY, {"owner": owner, "name": name, "category": category_id, "after": after}) or {}
        page = ((answer.get("data") or {}).get("repository") or {}).get("discussions")
        if page is None:
            raise WeekError("could not list the Launches category's discussions")
        for node in page.get("nodes") or []:
            match = MARKER.search(node.get("body") or "")
            author = str(((node.get("author") or {}).get("login")) or "").lower()
            if match and author in posters:
                found.setdefault((match.group(1), match.group(2)), node["number"])
        if not (page.get("pageInfo") or {}).get("hasNextPage"):
            break
        after = page["pageInfo"].get("endCursor")
    return found


def open_week(data: dict, rows: dict[str, dict], *, repository: str, ask: Ask, mutate: Ask) -> list[str]:
    """Give each launch on the board its vote post and mark the week open.
    Returns a line per launch."""
    if data.get("status") != "scheduled":
        raise WeekError(f"{data['week']} is {data.get('status')}, not scheduled")
    week = data["week"]
    on = [x for x in data["launches"] if x.get("status") == "scheduled"]
    notes: list[str] = []
    if on:
        repo_id, category_id = category(repository, ask)
        posts = existing_posts(repository, category_id, ask)
        for launch in L.shuffled(on, week):
            if launch.get("discussion"):
                notes.append(f"{launch['product']}: post #{launch['discussion']} on file")
                continue
            number = posts.get((week, launch["product"]))
            if number is None:
                title, body = post(week, launch, rows[launch["product"]])
                answer = mutate(CREATE, {"repository": repo_id, "category": category_id, "title": title, "body": body})
                created = (((answer or {}).get("data") or {}).get("createDiscussion") or {}).get("discussion")
                if not created:
                    # Write what was opened so far; the next run finds this one if it was made after all.
                    raise WeekError(f"could not create the post for {launch['product']}: {_errors(answer)}")
                number = created["number"]
                notes.append(f"{launch['product']}: post #{number} created")
            else:
                notes.append(f"{launch['product']}: post #{number} found")
            launch["discussion"] = number
    data["status"] = "open"
    return notes


def _errors(answer: dict | None) -> str:
    return "; ".join(str(e.get("message")) for e in (answer or {}).get("errors") or []) or "no answer"


def probe(repository: str, *, ask: Ask, mutate: Ask) -> list[str]:
    """Start a discussion in the Launches category and delete it: whether the
    token running this may post vote posts there. Raises WeekError when it may
    not, or when the post it made could not be deleted."""
    repo_id, category_id = category(repository, ask)
    answer = mutate(CREATE, {"repository": repo_id, "category": category_id, "title": PROBE_TITLE, "body": PROBE_BODY})
    made = (((answer or {}).get("data") or {}).get("createDiscussion") or {}).get("discussion")
    if not made:
        raise WeekError(
            f"could not start a discussion in the {CATEGORY} category ({_errors(answer)}). If it is in "
            "Announcement format, the workflow's token may not count as a maintainer there; MAINTAINING.md "
            "says what to do"
        )
    gone = mutate(DELETE, {"id": made["id"]})
    if not (((gone or {}).get("data") or {}).get("deleteDiscussion") or {}).get("discussion"):
        raise WeekError(
            f"started #{made['number']} in {CATEGORY}, so posting works, but could not delete it "
            f"({_errors(gone)}); a maintainer deletes it by hand: {made.get('url')}"
        )
    return [f"started and deleted #{made['number']}: this token can post vote posts in the {CATEGORY} category"]


# --------------------------------------------------------------------------
# Closing
# --------------------------------------------------------------------------


def close_week(data: dict, rows: dict[str, dict], *, on: dt.date,
               read: Callable[[int], list[dict]]) -> list[str]:
    """Count, check and rank an open week's launches, and mark it closed.
    A closed week is counted again the same way, after a person changed a
    launch's status (MAINTAINING.md). `read(number)` is a Discussion's votes.
    Returns a line per launch."""
    week = data["week"]
    if data.get("status") not in ("open", "closed"):
        raise WeekError(f"{week} is {data.get('status')}; only an open or closed week is counted")
    _, sunday = L.week_days(week)
    if on <= sunday:
        raise WeekError(f"{week} runs until Sunday {sunday}; it closes after that")
    notes: list[str] = []
    for launch in data["launches"]:
        if launch.get("status") != "scheduled":
            launch.pop("result", None)
            continue
        row = rows.get(launch["product"], {})
        own = L.makers_of(row) + [launch["submitted_by"]]
        votes = read(launch["discussion"]) if launch.get("discussion") else []
        # A person who read the votes and let the launch stand has the last word.
        why = None if launch.get("cleared_by") else L.ring(votes, own=own, week=week)
        if why:
            launch["status"], launch["reason"] = "held", why
            launch.pop("result", None)
            notes.append(f"{launch['product']}: held ({why})")
            continue
        launch["result"] = {**L.weigh(votes, own=own, week=week), "rank": 1}
    ordered = L.rank(data["launches"], rows)
    for launch in ordered:
        r = launch["result"]
        badge = f", {r['badges'][0]}" if r.get("badges") else ""
        notes.append(f"{launch['product']}: rank {r['rank']}, {r['votes']} votes, {r['counted']} counted, "
                     f"{r['discounted']} discounted{badge}")
    data["status"] = "closed"
    data["closed_on"] = on.isoformat()
    data["rules"] = L.CURRENT_RULES
    # Keys in the schema's order, so the file reads the same way every week.
    for key in ("closed_on", "rules", "launches"):
        data[key] = data.pop(key)
    return notes


def votes_reader(repository: str, ask: Ask) -> Callable[[int], list[dict]]:
    def read(number: int) -> list[dict]:
        return launch_votes.votes_from(launch_votes.fetch_pages(number, repository=repository, ask=ask))["votes"]
    return read


# --------------------------------------------------------------------------
# Monday
# --------------------------------------------------------------------------


def monday(root: pathlib.Path, today: dt.date, *, repository: str, ask: Ask, mutate: Ask) -> list[str]:
    """Close last week if it is open and open this week if it is scheduled.
    Writes each file it changed and returns what it did."""
    rows = rows_by_slug(root)
    this, last = L.week_of(today), L.week_of(today - dt.timedelta(days=7))
    done: list[str] = []
    before = load_week(root, last)
    if before and before.get("status") == "open":
        notes = close_week(before, rows, on=today, read=votes_reader(repository, ask))
        save_week(root, before)
        done += [f"closed {last}"] + [f"  {n}" for n in notes]
    current = load_week(root, this)
    if current and current.get("status") == "scheduled":
        try:
            notes = open_week(current, rows, repository=repository, ask=ask, mutate=mutate)
        finally:
            save_week(root, current)  # what was opened so far, even when a post failed
        done += [f"opened {this}"] + [f"  {n}" for n in notes]
    return done or [f"nothing to do: no open week {last} to close, no scheduled week {this} to open"]


def main(argv: list[str] | None = None, *, ask: Ask = _github.graphql_request,
         mutate: Ask = _github.graphql_mutation) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--monday", action="store_true", help="close last week and open this one, as needed")
    action.add_argument("--open", metavar="WEEK", help="open a scheduled week")
    action.add_argument("--close", metavar="WEEK", help="close an open week, or count a closed one again")
    action.add_argument("--probe", action="store_true",
                        help="start a discussion in the Launches category and delete it (launch-probe.yml)")
    parser.add_argument("--on", metavar="DAY", help="today, UTC (default: the clock)")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY") or _github.SELF)
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    root = pathlib.Path(args.root)
    today = L.day(args.on) if args.on else dt.datetime.now(dt.timezone.utc).date()
    if today is None:
        parser.error(f"--on takes a day like 2026-11-23, not {args.on!r}")
    week = args.open or args.close
    if week and not L.WEEK.match(week):
        parser.error(f"not an ISO week: {week!r}")
    try:
        if args.probe:
            done = probe(args.repo, ask=ask, mutate=mutate)
        elif args.monday:
            done = monday(root, today, repository=args.repo, ask=ask, mutate=mutate)
        else:
            data = load_week(root, week)
            if data is None:
                raise WeekError(f"there is no launches/{week}.json")
            rows = rows_by_slug(root)
            if args.open:
                try:
                    notes = open_week(data, rows, repository=args.repo, ask=ask, mutate=mutate)
                finally:
                    save_week(root, data)  # the posts made so far, even when one failed
            else:
                # Written only once every launch is counted: a half-counted week is never kept.
                notes = close_week(data, rows, on=today, read=votes_reader(args.repo, ask))
                save_week(root, data)
            done = [f"{'opened' if args.open else 'closed'} {week}"] + [f"  {n}" for n in notes]
    except (WeekError, launch_votes.ReadError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        _github.step_summary(f"### Launch week\n\nStopped: {exc}\n")
        return 1
    print("\n".join(done))
    _github.step_summary("### Launch week\n\n" + "\n".join(f"- {line.strip()}" for line in done) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
