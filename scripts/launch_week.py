#!/usr/bin/env python3
"""Open a launch week, and close the one before it (docs/launches.md).

L12, L13 and L14 of the 2026-11-03 launch-board plan. launch-week.yml runs
`--monday` early every Monday (UTC):

- **close** last week, if it is open: read each launch's thumbs-up votes from
  its Discussion (launch_votes.py), weigh them under the current rules
  (launches.weigh; a launch whose votes look like a ring of new accounts
  counts those votes as nothing under v2, launches.ring, L14), rank them
  (launches.rank, with badges for the top three), and write the results,
  `closed_on` and `rules` into launches/<week>.json;
- **open** this week, if it is scheduled: for each launch on the board, find or
  create its vote post in the Discussion category named `Launches`, write the
  post's number, and mark the week open.

Only counts are written, never who voted. The close also counts the week's
accounts (L28): `voters`, the accounts whose vote counted for something on
any launch, and `returning_voters`, how many of them also voted the week
before, read again from that week's posts. Opening writes each launch's
evidence tier as it stood (`tier_at_open`), so the share of launches someone
had read before they opened can be measured.

`--tell` (launch-week.yml runs it once the files are on `main`) tells each
launch's issue (L27): when its week has opened, a comment with the vote
post's link, and the issue is closed; when the week has closed, a comment
with the result and, for the top three, the badge's README line. A comment is
found again by a marker before it is written, so a second run says nothing
twice, and a comment GitHub refuses is reported, never a failure: the files
are what count.

A post is found again by a marker in its body before one is created, so a run
that stopped halfway can simply run again; a mutation is sent once and never
retried (_github.graphql_mutation).

Nothing happens when there is nothing to do: no file for the week, or a week
already opened or closed. Turning Discussions on and adding the `Launches`
category (maintainers only) is the owner's; until then opening a week with
launches on it fails, and says so.

`--probe` (launch-probe.yml, by hand) starts one discussion in the category
and deletes it at once: the check that the workflow's own token may post in a
category only maintainers can start discussions in, before a Monday needs it.

Usage:
  python3 scripts/launch_week.py --monday                # what launch-week.yml runs
  python3 scripts/launch_week.py --tell                  # then, once the files are on main
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

ISSUE_QUERY = """
query($owner: String!, $name: String!, $number: Int!) {
  repository(owner: $owner, name: $name) {
    issue(number: $number) {
      id
      state
      comments(last: 50) { nodes { body author { login } } }
    }
  }
}
"""

COMMENT = """
mutation($subject: ID!, $body: String!) {
  addComment(input: {subjectId: $subject, body: $body}) {
    commentEdge { node { id } }
  }
}
"""

CLOSE_ISSUE = """
mutation($issue: ID!) {
  closeIssue(input: {issueId: $issue, stateReason: COMPLETED}) {
    issue { number state }
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
            # The evidence as it stood when the vote post opened (L28).
            launch.setdefault("tier_at_open", L.tier(rows[launch["product"]]))
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
            # Keys in the schema's order: the post, then the tier it opened with.
            launch["tier_at_open"] = launch.pop("tier_at_open")
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


def week_voters(data: dict, rows: dict[str, dict], read: Callable[[int], list[dict]], notes: list[str]) -> set[str]:
    """The accounts whose vote counted for something on any launch still on a
    closed week's board, read again from its posts: a week's returning voters
    are counted against the week before's. A post that cannot be read now is
    left out, and said in `notes`."""
    everyone: set[str] = set()
    for launch in L.on_board(data):
        if not launch.get("discussion"):
            continue
        row = rows.get(launch["product"], {})
        try:
            votes = read(launch["discussion"])
        except launch_votes.ReadError as exc:
            notes.append(f"{data['week']} {launch['product']}: post #{launch['discussion']} not read ({exc}); "
                         "the returning voters are counted without it")
            continue
        everyone |= L.counted_voters(votes, own=L.makers_of(row) + [launch["submitted_by"]], week=data["week"],
                                     rules=data.get("rules") or L.CURRENT_RULES)
    return everyone


def close_week(data: dict, rows: dict[str, dict], *, on: dt.date,
               read: Callable[[int], list[dict]], before: dict | None = None) -> list[str]:
    """Count, check and rank an open week's launches, and mark it closed.
    A closed week can be counted again the same way. `read(number)` is a
    Discussion's votes. `before` is the week before's file, if any: its posts
    are read again to count the returning voters. Returns a line per launch.

    Since rule v2 (2026-11-05) nothing is held for a person: a launch whose
    votes look like a ring of new accounts ranks with the rest, those votes
    counted as nothing, and its result says `ring`. Under v1 it was held."""
    week = data["week"]
    if data.get("status") not in ("open", "closed"):
        raise WeekError(f"{week} is {data.get('status')}; only an open or closed week is counted")
    _, sunday = L.week_days(week)
    if on <= sunday:
        raise WeekError(f"{week} runs until Sunday {sunday}; it closes after that")
    notes: list[str] = []
    voters: set[str] = set()
    for launch in data["launches"]:
        if launch.get("status") != "scheduled":
            launch.pop("result", None)
            continue
        row = rows.get(launch["product"], {})
        own = L.makers_of(row) + [launch["submitted_by"]]
        votes = read(launch["discussion"]) if launch.get("discussion") else []
        # Under v1 a ring was held, and a person who read the votes and let
        # the launch stand had the last word; a rule with `ring_young` (v2 on)
        # settles it in weigh() instead.
        settles = "ring_young" in L.RULES[L.CURRENT_RULES]
        why = None if launch.get("cleared_by") or settles else L.ring(votes, own=own, week=week)
        if why:
            launch["status"], launch["reason"] = "held", why
            launch.pop("result", None)
            notes.append(f"{launch['product']}: held ({why})")
            continue
        result = L.weigh(votes, own=own, week=week)
        ringed = result.pop("ring", False)
        launch["result"] = {**result, "rank": 1}
        if ringed:
            launch["result"]["ring"] = True
            notes.append(f"{launch['product']}: {L.ring(votes, own=own, week=week)}")
        voters |= L.counted_voters(votes, own=own, week=week)
    ordered = L.rank(data["launches"], rows)
    for launch in ordered:
        r = launch["result"]
        badge = f", {r['badges'][0]}" if r.get("badges") else ""
        notes.append(f"{launch['product']}: rank {r['rank']}, {r['votes']} votes, {r['counted']} counted, "
                     f"{r['discounted']} discounted{badge}")
    data["status"] = "closed"
    data["closed_on"] = on.isoformat()
    data["rules"] = L.CURRENT_RULES
    # The week's accounts (L28): counted here, in memory; only the numbers stay.
    earlier = week_voters(before, rows, read, notes) if before and before.get("status") == "closed" else set()
    data["voters"], data["returning_voters"] = len(voters), len(voters & earlier)
    notes.append(f"{data['voters']} accounts voted, {data['returning_voters']} of them the week before too")
    # Keys in the schema's order, so the file reads the same way every week.
    for key in ("closed_on", "rules", "voters", "returning_voters", "launches"):
        data[key] = data.pop(key)
    return notes


# --------------------------------------------------------------------------
# Telling each launch's issue (L27)
# --------------------------------------------------------------------------


def issue_marker(week: str, slug: str, stage: str) -> str:
    return f"<!-- launch-board {week} {slug} {stage} -->"


def opened_note(week: str, launch: dict) -> str:
    """What a launch's issue is told when its week opens."""
    monday, sunday = L.week_days(week)
    return "\n".join([
        issue_marker(week, launch["product"], "opened"),
        f"This launch is on the board for **{week}** (Monday {monday} to Sunday {sunday}, UTC). Its vote "
        f"post: {L.query.DISCUSSION}{launch['discussion']}",
        "",
        "A thumbs-up on that post is a vote, one per account (rules v1). When the week closes next Monday, "
        "the counts are written to the board and the result is posted here.",
        "",
        "Until then the product's README badge says \"vote this week\" and links to its page, where the vote "
        "post is; after the week, it shows a top-three place, if any. The line, the same for every product:",
        "",
        "```markdown",
        L.badge_line(launch["product"]),
        "```",
        "",
        f"The launch is on the board, so this issue is closed. How the board works: {DOCS}",
        "",
    ])


def closed_note(week: str, launch: dict, on_board: int, rules: str = L.CURRENT_RULES) -> str:
    """What a launch's issue is told when its week closes."""
    lines = [issue_marker(week, launch["product"], "closed")]
    result = launch.get("result")
    if launch.get("status") == "held":
        lines += [f"**{week} closed.** This launch is held for a person before it ranks: "
                  f"{launch.get('reason', '')}. A maintainer reads the votes and decides; the week's file "
                  "keeps the decision."]
    elif result:
        lines += [f"**{week} closed.** This launch placed #{result['rank']} of {on_board}, with "
                  f"{result['votes']} votes, {result['counted']} counted under rules {rules}. The week's page: "
                  f"{SITE}weeks/{week}.html"]
        if result.get("ring"):
            young = L.RULES.get(rules, L.RULES[L.CURRENT_RULES])["young_days"]
            lines += ["", f"Most of its votes came from accounts younger than {young} days or of unknown age, "
                      "which looks like a ring, so under these rules those votes counted for nothing and it "
                      "ranked by the others."]
        if result.get("badges"):
            place = result["badges"][0].split("-")[1]
            lines += ["", f"It placed in the top three, so its README badge now says \"#{place} launch of {week}\". "
                      "A README that has the line already shows it; otherwise, this is the line:", "",
                      "```markdown",
                      L.badge_line(launch["product"]),
                      "```"]
    lines += ["", f"How the board works: {DOCS}", ""]
    return "\n".join(lines)


def tell(number: int, mark: str, body: str, *, close: bool, repository: str, ask: Ask, mutate: Ask) -> str:
    """Comment `body` on issue `number` unless a comment with `mark` from
    POSTERS is there already, and close the issue when `close` and it is
    open. Returns what was done; never raises for GitHub's answers."""
    owner, name = repository.split("/", 1)
    answer = ask(ISSUE_QUERY, {"owner": owner, "name": name, "number": number}) or {}
    issue = ((answer.get("data") or {}).get("repository") or {}).get("issue")
    if not issue or not issue.get("id"):
        return f"#{number}: could not read the issue ({_errors(answer)})"
    posters = POSTERS | {owner.lower()}
    said = any(mark in str(c.get("body") or "")
               and str(((c.get("author") or {}).get("login")) or "").lower() in posters
               for c in ((issue.get("comments") or {}).get("nodes") or []))
    done: list[str] = []
    if not said:
        sent = mutate(COMMENT, {"subject": issue["id"], "body": body})
        if not ((sent or {}).get("data") or {}).get("addComment"):
            return f"#{number}: could not comment ({_errors(sent)})"
        done.append("commented")
    if close and issue.get("state") == "OPEN":
        shut = mutate(CLOSE_ISSUE, {"issue": issue["id"]})
        if not ((shut or {}).get("data") or {}).get("closeIssue"):
            return f"#{number}: {', '.join(done + ['could not close'])} ({_errors(shut)})"
        done.append("closed")
    return f"#{number}: {', '.join(done) or 'told before'}"


def tell_issues(data: dict, stage: str, *, repository: str, ask: Ask, mutate: Ask) -> list[str]:
    """Tell each launch's issue that its week opened (with the vote post, and
    close it) or closed (with the result). A launch held before its week
    opened is left to the person who decides it."""
    week = data["week"]
    notes: list[str] = []
    on_board = len(L.on_board(data))
    for launch in data["launches"]:
        number = launch.get("issue")
        if not isinstance(number, int):
            continue
        if stage == "opened" and launch.get("status") == "scheduled" and launch.get("discussion"):
            body = opened_note(week, launch)
        elif stage == "closed" and (launch.get("result") or (launch.get("status") == "held" and launch.get("discussion"))):
            body = closed_note(week, launch, on_board, data.get("rules") or L.CURRENT_RULES)
        else:
            continue
        notes.append(f"{launch['product']} " + tell(number, issue_marker(week, launch["product"], stage), body,
                                                     close=True, repository=repository, ask=ask, mutate=mutate))
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
        earlier = load_week(root, L.week_of(today - dt.timedelta(days=14)))
        notes = close_week(before, rows, on=today, read=votes_reader(repository, ask), before=earlier)
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


def tell_due(root: pathlib.Path, today: dt.date, *, repository: str, ask: Ask, mutate: Ask) -> list[str]:
    """Tell the issues of this week's launches if the week is open, and of
    last week's if it is closed (tell_issues). Each issue hears each thing
    once, so this can run after every Monday run, and again."""
    done: list[str] = []
    for week, stage in ((L.week_of(today - dt.timedelta(days=7)), "closed"), (L.week_of(today), "opened")):
        data = load_week(root, week)
        if data and data.get("status") == ("closed" if stage == "closed" else "open"):
            notes = tell_issues(data, stage, repository=repository, ask=ask, mutate=mutate)
            done += [f"told the issues of {week} that it {stage}"] + [f"  {n}" for n in notes]
    return done or ["nothing to tell: no week opened or closed this Monday"]


def main(argv: list[str] | None = None, *, ask: Ask = _github.graphql_request,
         mutate: Ask = _github.graphql_mutation) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--monday", action="store_true", help="close last week and open this one, as needed")
    action.add_argument("--open", metavar="WEEK", help="open a scheduled week")
    action.add_argument("--close", metavar="WEEK", help="close an open week, or count a closed one again")
    action.add_argument("--probe", action="store_true",
                        help="start a discussion in the Launches category and delete it (launch-probe.yml)")
    action.add_argument("--tell", action="store_true",
                        help="tell the issues of the week that opened and the week that closed (once each)")
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
        elif args.tell:
            done = tell_due(root, today, repository=args.repo, ask=ask, mutate=mutate)
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
                monday_of, _ = L.week_days(week)
                earlier = load_week(root, L.week_of(monday_of - dt.timedelta(days=7)))
                # Written only once every launch is counted: a half-counted week is never kept.
                notes = close_week(data, rows, on=today, read=votes_reader(args.repo, ask), before=earlier)
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
