#!/usr/bin/env python3
"""GitHub's facts about each candidate still to read: `.discover/facts.json`.

The discovery queue (scripts/queue_sync.py) listed its candidates by the day a
script last read them, then by name, so the top of the issue was whichever
repositories the sibling lists happened to cite first, and hundreds of
candidates came with nothing to say which deserved a person's hour. The weekly
refresh already reads stars, commit counts and last pushes for every
catalogued repository. Since 2026-10-24 it reads the same for every candidate
still to read, and this file keeps them:

  stars     stargazers
  commits   commits on the default branch (0 for an empty repository)
  pushed    the day of the last push
  readme    whether a README sits at the top of the default branch's tree
  archived  whether its owner archived it
  name      owner/name as GitHub now gives it, only when that differs
  missing   true, alone, when GitHub found no such repository

queue_sync.py orders the candidates to read by them (most stars first, then
most commits, then the latest push) and parks the weakest: a candidate with at
least PARK_AT of the weak facts in WEAK, or one GitHub no longer finds.
Parked is not declined. Nothing is decided about a parked candidate: it stays
in the issue under its own heading, anyone may still read it, and the first
refresh that finds it stronger puts it back among those to read. A person's
decision is still only a row in catalog.json or a line in docs/declined.txt.

The facts are GitHub's figures, read with batched GraphQL queries like the
refresh's own (scripts/refresh_metadata.py), owners and names passed as
variables. Nothing a candidate's owner wrote is kept: the files at the top of
its tree are only tested for a README. Every entry is checked on the way in,
as .discover/seen.json's are, and the file is written one repository per line
in name order, so a week's diff is what moved. A candidate GraphQL did not
answer this week keeps last week's facts; one no longer to read is dropped.

Usage:
  GITHUB_TOKEN=... python3 scripts/discover_facts.py   # read them, rewrite the file
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

from _github import RateLimited, graphql_request, log_usage, token  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATH = ROOT / ".discover" / "facts.json"
# discover_seen.SLUG: the owner and name GitHub links carry, lower-cased.
SLUG = re.compile(r"[a-z0-9][\w.-]*/[\w.-]+")
# Repositories per query. The refresh's fifty took 4.5 s on average with the
# commit count (GitHub stops a query at 10 s); this one lists each root tree
# too, so it asks for half as many at a time.
BATCH = 25
FIELDS = (
    "nameWithOwner stargazerCount isArchived pushedAt "
    "defaultBranchRef { target { ... on Commit { history { totalCount } tree { entries { name type } } } } }"
)
README = re.compile(r"readme(?:[._-][\w.-]+)?", re.IGNORECASE)

# What parks a candidate: each is a reason a person's hour is better spent
# elsewhere first, none is a reason to decline it.
WEAK = {
    "one commit or none": lambda facts: facts["commits"] <= 1,
    "no star": lambda facts: facts["stars"] == 0,
    "no README": lambda facts: not facts["readme"],
}
PARK_AT = 2
MISSING = "GitHub finds no such repository"

ABOUT = [
    "GitHub's figures, not anyone's verdict: what the weekly refresh read about each repository still to read in the discovery queue.",
    "stars; commits on the default branch; pushed, the day of the last push; readme, whether one sits at the top of the tree; archived;",
    "name, only when GitHub now gives the repository another owner/name; missing, alone, when GitHub found no such repository.",
    f"scripts/queue_sync.py orders the queue by them and parks a candidate with {PARK_AT} or more of: "
    + ", ".join(WEAK) + ". Parked is not declined.",
    "A person's decision is a row in catalog.json or a line in docs/declined.txt, never an entry here.",
    "Written by scripts/discover_facts.py, run and committed by .github/workflows/metadata.yml.",
]


def problem(slug: object, entry: object) -> str:
    """Why an entry is not a candidate's facts, or "" when it is."""
    if not isinstance(slug, str) or not SLUG.fullmatch(slug) or slug != slug.lower():
        return "not a lower-case owner/name"
    if entry == {"missing": True}:
        return ""
    if not isinstance(entry, dict):
        return "not an object"
    for key in ("stars", "commits"):
        if not isinstance(entry.get(key), int) or isinstance(entry.get(key), bool) or entry[key] < 0:
            return f"{key} is not a count"
    for key in ("readme", "archived"):
        if not isinstance(entry.get(key), bool):
            return f"{key} is not true or false"
    pushed = entry.get("pushed")
    try:
        if dt.date.fromisoformat(pushed).isoformat() != pushed:
            raise ValueError
    except (TypeError, ValueError):
        return "pushed is not YYYY-MM-DD"
    name = entry.get("name")
    if name is not None and (not isinstance(name, str) or not SLUG.fullmatch(name) or name != name.lower()):
        return "name is not a lower-case owner/name"
    if set(entry) - {"stars", "commits", "pushed", "readme", "archived", "name"}:
        return "has a key this file does not know"
    return ""


def parse(data: object) -> tuple[dict[str, dict], list[str]]:
    """The facts in a loaded file, and one message per entry left out."""
    if not isinstance(data, dict) or not isinstance(data.get("facts"), dict):
        return {}, ['not a facts file: expected {"about": [...], "facts": {...}}']
    kept: dict[str, dict] = {}
    dropped: list[str] = []
    for slug, entry in data["facts"].items():
        why = problem(slug, entry)
        if why:
            dropped.append(f"{str(slug)[:80]!r}: {why}")
        else:
            kept[slug] = dict(entry)
    return kept, dropped


def load(path: pathlib.Path | str = PATH) -> tuple[dict[str, dict], list[str]]:
    """parse() of a file. A missing file is an empty one: every candidate is
    then unmeasured, and the queue lists them as it did before 2026-10-24."""
    path = pathlib.Path(path)
    if not path.exists():
        return {}, []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        return {}, [f"unreadable: {exc}"]
    return parse(data)


def report_dropped(where: str, dropped: list[str]) -> None:
    """A GitHub warning naming how many entries were left out, then the first
    few; the rest of the file is still used."""
    if not dropped:
        return
    n = len(dropped)
    print(
        f"::warning title=Discovery facts left out::{where}: "
        f"{n} entr{'ies' if n != 1 else 'y'} not shaped like a candidate's facts, left out",
        file=sys.stderr,
    )
    for line in dropped[:10]:
        print(f"  {where}: {line}", file=sys.stderr)


def render(facts: dict[str, dict]) -> str:
    """The file's text: `about` first, then one repository per line in name
    order, each entry's keys sorted. Same facts, same bytes."""
    about = ",\n".join(f"    {json.dumps(line, ensure_ascii=False)}" for line in ABOUT)
    rows = ",\n".join(
        f"    {json.dumps(slug)}: " + json.dumps(facts[slug], sort_keys=True)
        for slug in sorted(facts)
    )
    lines = ["{", '  "about": [', about, "  ],"]
    lines += ['  "facts": {', rows, "  }"] if rows else ['  "facts": {}']
    return "\n".join(lines + ["}"]) + "\n"


def write(path: pathlib.Path | str, facts: dict[str, dict]) -> None:
    """render() to path in one step, so a crash never leaves half a file."""
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(render(facts))
        os.replace(tmp, path)
    except BaseException:
        pathlib.Path(tmp).unlink(missing_ok=True)
        raise


def parked(facts: dict | None) -> list[str]:
    """Why a candidate is parked, or [] when it is not. A candidate with no
    facts yet (found since the last refresh) is not parked: nothing says it
    is weak."""
    if not facts:
        return []
    if facts.get("missing"):
        return [MISSING]
    weak = [name for name, test in WEAK.items() if test(facts)]
    return weak if len(weak) >= PARK_AT else []


def rank(facts: dict | None) -> tuple:
    """Sort key, strongest first: most stars, then most commits, then the
    latest push. A candidate without facts sorts after every one with them."""
    if not facts or facts.get("missing"):
        return (1,)
    return (0, -facts["stars"], -facts["commits"], -dt.date.fromisoformat(facts["pushed"]).toordinal())


def describe(facts: dict | None, *, parked: bool = False) -> str:
    """The facts as the queue shows them beside a candidate. Nothing for one
    the refresh has not read yet, or one GitHub no longer finds (its parked
    reason says so); and on a parked line, no missing README, which the
    reason names whenever it is missing."""
    if not facts or facts.get("missing"):
        return ""
    commits = facts["commits"]
    parts = [f"★{facts['stars']}", f"{commits} commit{'s' if commits != 1 else ''}", f"last push {facts['pushed']}"]
    if not facts["readme"] and not parked:
        parts.append("no README")
    if facts["archived"]:
        parts.append("archived")
    if facts.get("name"):
        parts.append(f"now {facts['name']}")
    return " · ".join(parts)


def query_for(batch: list[str]) -> tuple[str, dict]:
    """One query for up to BATCH repositories, aliased r0, r1, …. Owners and
    names travel as variables, never pasted into the query text."""
    params, lookups, variables = [], [], {}
    for alias, repo in enumerate(batch):
        owner, name = repo.split("/", 1)
        variables[f"o{alias}"], variables[f"n{alias}"] = owner, name
        params.append(f"$o{alias}: String!, $n{alias}: String!")
        lookups.append(f"r{alias}: repository(owner: $o{alias}, name: $n{alias}) {{ {FIELDS} }}")
    return f"query({', '.join(params)}) {{ " + " ".join(lookups) + " }", variables


def from_node(repo: str, node: dict) -> dict:
    """A candidate's facts from GraphQL's names for them. An empty repository
    has no default branch, so no commits and no README."""
    target = (node.get("defaultBranchRef") or {}).get("target") or {}
    entries = (target.get("tree") or {}).get("entries") or []
    facts = {
        "stars": node["stargazerCount"],
        "commits": (target.get("history") or {}).get("totalCount") or 0,
        "pushed": (node.get("pushedAt") or "")[:10],
        "readme": any(
            isinstance(e, dict) and e.get("type") == "blob" and README.fullmatch(str(e.get("name") or ""))
            for e in entries
        ),
        "archived": bool(node.get("isArchived")),
    }
    name = str(node.get("nameWithOwner") or "").lower()
    if name and name != repo:
        facts["name"] = name
    return facts


def read(repos: list[str]) -> tuple[dict[str, dict], int]:
    """Facts for every candidate GraphQL answered, and how many it did not.
    A lookup GitHub says is NOT_FOUND is a fact too (`missing`); a failed
    query, a refused lookup or a spent budget leaves those candidates unread."""
    found: dict[str, dict] = {}
    unread = 0
    batches = [repos[start : start + BATCH] for start in range(0, len(repos), BATCH)]
    for number, batch in enumerate(batches, 1):
        try:
            answer = graphql_request(*query_for(batch))
        except RateLimited:
            answer = None
        data = (answer or {}).get("data") or {}
        absent = {
            str(e["path"][0])
            for e in (answer or {}).get("errors") or []
            if isinstance(e, dict) and e.get("type") == "NOT_FOUND" and e.get("path")
        }
        answered = 0
        for alias, repo in enumerate(batch):
            node = data.get(f"r{alias}")
            if isinstance(node, dict) and isinstance(node.get("stargazerCount"), int) and node.get("pushedAt"):
                found[repo] = from_node(repo, node)
            elif data and f"r{alias}" in absent:
                found[repo] = {"missing": True}
            else:
                unread += 1
                continue
            answered += 1
        print(f"graphql batch {number}/{len(batches)}: {answered} of {len(batch)} answered", file=sys.stderr)
    return found, unread


def main(argv: list[str] | None = None) -> int:
    import queue_sync  # it imports this module, so not at the top

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)  # tests
    args = parser.parse_args(argv)
    root = pathlib.Path(args.root)
    # Reports any entry of either file it leaves out.
    seen, catalog, retired, declined, before = queue_sync.read_files(root)
    # Under the name the sibling lists cite, so a candidate settled under the
    # name GitHub now gives it is read again, and its rename kept.
    repos = [c.repo for c in queue_sync.derive(seen, catalog, retired, declined) if c.state == "open"]
    if not token():
        print("discovery facts: no GITHUB_TOKEN, so nothing is read and last week's facts stand", file=sys.stderr)
    found, unread = read(repos) if token() else ({}, len(repos))
    # A candidate not answered keeps last week's facts; one no longer to read
    # (catalogued, declined, or re-read and found quiet) is dropped.
    facts = {repo: found.get(repo) or before[repo] for repo in repos if repo in found or repo in before}
    facts, dropped = parse({"facts": facts})
    report_dropped("this run's facts", dropped)
    write(root / ".discover" / "facts.json", facts)

    states = [c.state for c in queue_sync.derive(seen, catalog, retired, declined, facts) if c.repo in set(repos)]
    print(
        f"discovery facts: {len(found)} of {len(repos)} candidate(s) read, {unread} not answered"
        f" ({sum(1 for r in repos if r not in found and r in before)} keep last week's facts);"
        f" {states.count('open')} to read, {states.count('parked')} parked,"
        f" {len(states) - states.count('open') - states.count('parked')} settled under the name GitHub now gives"
    )
    log_usage()
    return 0


if __name__ == "__main__":
    sys.exit(main())
