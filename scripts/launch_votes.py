#!/usr/bin/env python3
"""Read the votes on a launch's GitHub Discussion (docs/launches.md; L2 of the
2026-11-03 plan).

A vote is a thumbs-up reaction on the Discussion's own post. GitHub's GraphQL
API serves a Discussion's reactions with who left each one and when
(Discussion.reactions(content: THUMBS_UP)), and the voter's account age
(User.createdAt), which is all scripts/launches.py weigh() needs. Nothing is
stored: the reader returns the votes to its caller, and the only thing this
repository keeps is the count written when a week closes (launches/*.json),
never who voted.

Run in Actions with the workflow's own token (launch-votes.yml, Run workflow);
locally it needs GITHUB_TOKEN. `--fixture` reads saved GraphQL answers instead
of the network, for the tests.

Run: python3 scripts/launch_votes.py --discussion 12
     python3 scripts/launch_votes.py --discussion 12 --week 2026-W47 --own alice,bob
     python3 scripts/launch_votes.py --fixture answers.json --week 2026-W47
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Callable, Iterable

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _github  # noqa: E402
import launches  # noqa: E402

REPOSITORY = _github.SELF
PAGE = 100
# The most pages read for one Discussion: 2,000 votes. A launch past that has
# outgrown this way of counting (docs/launches.md, "When it stops scaling").
MAX_PAGES = 20

QUERY = """
query($owner: String!, $name: String!, $number: Int!, $after: String) {
  repository(owner: $owner, name: $name) {
    discussion(number: $number) {
      number
      url
      reactions(content: THUMBS_UP, first: 100, after: $after) {
        totalCount
        pageInfo { hasNextPage endCursor }
        nodes { createdAt user { login createdAt } }
      }
    }
  }
}
"""


class ReadError(RuntimeError):
    """The votes could not be read; the message says why."""


def votes_from(pages: Iterable[dict]) -> dict:
    """The votes in a run of GraphQL answers for one Discussion:
    {"discussion", "url", "total", "votes": [{"login", "at", "account_created"}]}.
    A reaction whose user is gone (a deleted account) has no login and is left out."""
    out: dict = {"discussion": None, "url": None, "total": 0, "votes": []}
    for answer in pages:
        errors = answer.get("errors") or []
        data = answer.get("data") or {}
        discussion = (data.get("repository") or {}).get("discussion")
        if discussion is None:
            detail = "; ".join(str(e.get("message")) for e in errors) or "no such discussion"
            raise ReadError(detail)
        reactions = discussion.get("reactions") or {}
        out["discussion"] = discussion.get("number")
        out["url"] = discussion.get("url")
        out["total"] = reactions.get("totalCount") or 0
        for node in reactions.get("nodes") or []:
            user = node.get("user") or {}
            if user.get("login"):
                out["votes"].append({
                    "login": user["login"],
                    "at": node.get("createdAt"),
                    "account_created": user.get("createdAt"),
                })
    return out


def fetch_pages(number: int, repository: str = REPOSITORY,
                ask: Callable[[str, dict], dict | None] = _github.graphql_request) -> list[dict]:
    """Every page of THUMBS_UP reactions on Discussion `number`."""
    owner, name = repository.split("/", 1)
    pages: list[dict] = []
    after = None
    for _ in range(MAX_PAGES):
        answer = ask(QUERY, {"owner": owner, "name": name, "number": number, "after": after})
        if answer is None:
            raise ReadError("no answer from the GraphQL API (no token, or the request was refused)")
        pages.append(answer)
        info = ((((answer.get("data") or {}).get("repository") or {}).get("discussion") or {})
                .get("reactions") or {}).get("pageInfo") or {}
        if not info.get("hasNextPage"):
            return pages
        after = info.get("endCursor")
    raise ReadError(f"more than {MAX_PAGES * PAGE} reactions; this reader stops there")


def summary(read: dict, tally: dict | None, week: str | None) -> str:
    """The job summary: counts only, never the logins."""
    lines = [
        f"### Votes on discussion #{read['discussion']}",
        "",
        f"- {read['url']}",
        f"- thumbs-up reactions: {read['total']} ({len(read['votes'])} from accounts that still exist)",
    ]
    if tally is not None:
        lines += [
            f"- inside {week}: {tally['votes']} vote(s), counted {tally['counted']} under rules "
            f"{launches.CURRENT_RULES}, {tally['discounted']} discounted",
        ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--discussion", type=int, help="the Discussion's number")
    source.add_argument("--fixture", type=pathlib.Path, help="a JSON list of saved GraphQL answers")
    parser.add_argument("--repo", default=REPOSITORY, help="owner/name (default %(default)s)")
    parser.add_argument("--week", help="ISO week to weigh the votes for, e.g. 2026-W47")
    parser.add_argument("--own", default="", help="comma-separated logins whose votes are the product's own")
    parser.add_argument("--out", type=pathlib.Path, help="write the votes as JSON here (not into the repository)")
    args = parser.parse_args(argv)
    try:
        if args.fixture:
            pages = json.loads(args.fixture.read_text(encoding="utf-8"))
        else:
            pages = fetch_pages(args.discussion, args.repo)
        read = votes_from(pages)
    except (ReadError, _github.RateLimited, OSError, ValueError) as exc:
        print(f"launch_votes: {exc}", file=sys.stderr)
        _github.step_summary(f"### Votes not read\n\n{exc}")
        return 1
    tally = None
    if args.week:
        own = [x for x in args.own.split(",") if x]
        tally = launches.weigh(read["votes"], own=own, week=args.week)
    if args.out:
        args.out.write_text(json.dumps({**read, "tally": tally}, indent=2) + "\n", encoding="utf-8")
    text = summary(read, tally, args.week)
    print(text)
    _github.step_summary(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
