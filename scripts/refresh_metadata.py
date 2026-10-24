#!/usr/bin/env python3
"""Refresh the repository facts in catalog.json from the GitHub API.

Star counts, licences and archive status go stale the moment they are written,
and a catalog full of six-month-old numbers is the failure mode every abandoned
awesome list shares. This script re-reads them.

It touches ONLY facts a machine can check:

  stars          <- stargazers_count
  repo_license   <- license.spdx_id, or "unknown" when none is declared
  archived flag  <- the repository's own archived field
  no-license flag<- whether a licence is declared
  summary_source <- whether summary is the repository's own description
  repo_created_at<- created_at: when the repository was created
  repo_pushed_at <- pushed_at: when anything was last pushed to it
  repo_commits   <- how many commits its default branch has
  single-commit flag <- whether that count is exactly one

Summaries, notes, patterns and question_types are human judgements and are
never touched. summary_source records a comparison, not a judgement: the
summary is identical to the description GitHub serves (letter case, runs of
whitespace and one final full stop aside) or it is not. See
summary_source_for() for the rules; the one it never breaks is that only a
person writes `curated`. `archived` follows GitHub's own flag rather than a
no-push-in-N-days heuristic, because the catalog's whole stance is to state
checkable facts rather than guesses — the cost is missing projects that are
quietly unmaintained without being formally archived. The same stance covers
the dates and the commit count: they are recorded as GitHub states them, so a
reader can judge upkeep, and nothing here turns them into a verdict. Only the
`single-commit` flag follows from them, and it restates the count exactly.

Usage:
  python3 scripts/refresh_metadata.py            # report drift, change nothing
  python3 scripts/refresh_metadata.py --write    # apply it
  python3 scripts/refresh_metadata.py --json     # machine-readable report
  python3 scripts/refresh_metadata.py --via rest # one REST request per row
  python3 scripts/refresh_metadata.py --compare  # read both ways, list differences
  python3 scripts/refresh_metadata.py --only-field summary_source --write
                                                 # apply one kind of change, nothing else

Facts are read with batched GraphQL queries, fifty repositories each; a
row GraphQL cannot answer is read over REST, which also remains the whole path
with `--via rest`. `--compare` showed the two give the same facts before the
weekly job switched. A blocked repository, or a GitHub budget that runs out,
costs the rows involved, never the run: whatever was read is still written, and
the digest says what was not.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _github import (  # noqa: E402
    SELF,
    RateLimited,
    api_get,
    api_response,
    graphql_request,
    last_page,
    log_usage,
    repo_of,
    step_summary,
    usage_lines,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
WORKERS = 6

# Repositories per GraphQL query. Each is one aliased `repository` lookup, and
# a query of fifty costs one point of the GraphQL budget, so the whole
# catalogue is about two dozen requests where REST needs two per repository.
# It was a hundred until 2026-09-27, when the commit count joined the query:
# counting each default branch's history took a query of a hundred 9-10 s
# (measured over the whole catalogue that day), at GitHub's 10-second limit
# for a GraphQL request; fifty took 4.5 s on average and under 7 s at most.
BATCH = 50
FIELDS = (
    "nameWithOwner url stargazerCount isArchived licenseInfo { spdxId } description "
    "createdAt pushedAt defaultBranchRef { target { ... on Commit { history { totalCount } } } }"
)

# summary_source values (schema/entry.schema.json). The refresh writes the two
# upstream ones; CURATED is a person's statement that they wrote the text and
# MODEL_WRITTEN (since 2026-10-24) the same of a model, and the refresh leaves
# both be.
CURATED = "curated"
MODEL_WRITTEN = "model-written"
WRITTEN_HERE = (CURATED, MODEL_WRITTEN)
UPSTREAM = "upstream-description"
UPSTREAM_STALE = "upstream-description-stale"

# The kinds of change diff_for() proposes, in the order it proposes them.
# --only-field applies a subset and leaves every other one unwritten.
CHANGE_FIELDS = (
    "stars", "repo_license", "renamed", "flags", "summary_source",
    "repo_created_at", "repo_pushed_at", "repo_commits",
)

# The three repository facts GitHub states and the row records as stated, each
# placed after the first of these keys the row has, so a row reads stars,
# repo_license, repo_created_at, repo_pushed_at, repo_commits.
REPO_FACTS = {
    "repo_created_at": ("created_at", ("repo_license", "stars")),
    "repo_pushed_at": ("pushed_at", ("repo_created_at", "repo_license", "stars")),
    "repo_commits": ("commits", ("repo_pushed_at", "repo_created_at", "repo_license", "stars")),
}

# `single-commit` says what repo_commits says when it is 1, and lint.py holds
# the two to agreeing, so a change to the flag is applied with the count:
# `--only-field repo_commits` carries it and `--only-field flags` does not.
SINGLE_COMMIT = "single-commit"

# SELF is imported from _github: rows pointing at this repository are its own
# runnable examples, and stamping them with this repo's own star count would be
# both meaningless and circular.


def facts(entry: dict, repo: str, *, stars: int, spdx: str, archived: bool,
          full_name: str | None, html_url: str | None, description: str | None,
          created_at: str | None = None, pushed_at: str | None = None,
          commits: int | None = None) -> dict:
    return {
        "slug": entry["slug"],
        "repo": repo,
        "state": "ok",
        "stars": stars,
        "repo_license": spdx,
        "archived": archived,
        # GitHub follows a renamed or transferred repository with a redirect,
        # so the old URL keeps answering 200 and no link check ever notices.
        # The canonical name is the fact; the catalogue should hold it.
        "full_name": full_name or repo,
        "html_url": html_url,
        # The repository's own one-line description, as GitHub serves it; None
        # when it has none. Compared with the row's summary, never copied in.
        "description": description or None,
        # When the repository was created and when anything was last pushed to
        # any branch, as GitHub states them (UTC, to the second). None when
        # GitHub gave none; a row then keeps what it had.
        "created_at": timestamp(created_at),
        "pushed_at": timestamp(pushed_at),
        # Commits on the default branch. None when not counted: an empty
        # repository has no default branch to count, and a rate limit or a
        # refused count leaves the row's previous figure standing.
        "commits": commits if isinstance(commits, int) and commits > 0 else None,
    }


def timestamp(value: object) -> str | None:
    """GitHub's `2026-09-17T09:21:47Z`, or None for anything not in that form,
    so the REST and GraphQL spellings of a date always compare equal."""
    if isinstance(value, str) and TIMESTAMP.fullmatch(value):
        return value
    return None


TIMESTAMP = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")


def from_rest(entry: dict, repo: str, data: dict, commits: int | None = None) -> dict:
    """Facts from `/repos/{repo}`, plus the commit count, which that answer does
    not carry: rest_commits() asks for it separately."""
    # GitHub reports NOASSERTION for a LICENSE file it cannot identify — custom
    # or modified terms — which is different from having none at all, so it is
    # kept as-is. Only a repository with no licence file becomes "unknown".
    spdx = ((data.get("license") or {}).get("spdx_id") or "").strip() or "unknown"
    return facts(
        entry, repo, stars=data["stargazers_count"], spdx=spdx,
        archived=bool(data.get("archived")), full_name=data.get("full_name"),
        html_url=data.get("html_url"), description=data.get("description"),
        created_at=data.get("created_at"), pushed_at=data.get("pushed_at"),
        commits=commits,
    )


def from_graphql(entry: dict, repo: str, node: dict) -> dict:
    """The same facts from GraphQL's names for them. `repository(owner, name)`
    follows renames like REST's redirect; licenseInfo is null where REST's
    licence is, and spdxId is NOASSERTION where REST's spdx_id is."""
    spdx = ((node.get("licenseInfo") or {}).get("spdxId") or "").strip() or "unknown"
    # An empty repository has no default branch: defaultBranchRef is null.
    target = (node.get("defaultBranchRef") or {}).get("target") or {}
    return facts(
        entry, repo, stars=node["stargazerCount"], spdx=spdx,
        archived=bool(node.get("isArchived")), full_name=node.get("nameWithOwner"),
        html_url=node.get("url"), description=node.get("description"),
        created_at=node.get("createdAt"), pushed_at=node.get("pushedAt"),
        commits=(target.get("history") or {}).get("totalCount"),
    )


def outcome(entry: dict, repo: str, state: str, detail: str = "") -> dict:
    return {"slug": entry["slug"], "repo": repo, "state": state, "detail": detail}


def rest_commits(repo: str) -> int | None:
    """Commits on the default branch over REST: one commit per page, so the
    page number of the `Link` header's rel="last" is the count; without that
    link, the commits on the one page are. None when GitHub did not say — an
    empty repository answers 409, a blocked one 403 — or the budget is spent:
    the count is one more request, and losing it must not cost the row's
    other facts."""
    try:
        status, data, head = api_response(f"/repos/{repo}/commits?per_page=1")
    except RateLimited:
        return None
    if not 200 <= status < 300 or not isinstance(data, list):
        return None
    return last_page((head or {}).get("Link")) or len(data) or None


def fetch(entry: dict) -> dict | None:
    """Current facts for one row over REST, or None when the row names no GitHub
    repository. Any other failure is a state, never an exception: a blocked
    repository or a spent budget costs this row, not the run. Two requests:
    the repository, then its commit count."""
    repo = repo_of(entry)
    if not repo:
        return None
    try:
        data = api_get(f"/repos/{repo}")
    except RateLimited as exc:
        return outcome(entry, repo, "skipped", exc.detail)
    if isinstance(data, dict) and data.get("blocked"):
        return outcome(entry, repo, "blocked", f"HTTP {data['status']}: {data.get('message') or 'no reason given'}")
    if not isinstance(data, dict) or "stargazers_count" not in data:
        return outcome(entry, repo, "gone")
    # A renamed repository is counted under the name GitHub now gives it.
    return from_rest(entry, repo, data, rest_commits(data.get("full_name") or repo))


def query_for(batch: list[tuple[str, int]]) -> tuple[str, dict]:
    """One query for up to BATCH repositories, aliased r0, r1, …. Owners and
    names travel as variables, never pasted into the query text."""
    params, lookups, variables = [], [], {}
    for alias, (repo, _) in enumerate(batch):
        owner, name = repo.split("/", 1)
        variables[f"o{alias}"] = owner
        variables[f"n{alias}"] = name
        params.append(f"$o{alias}: String!, $n{alias}: String!")
        lookups.append(f"r{alias}: repository(owner: $o{alias}, name: $n{alias}) {{ {FIELDS} }}")
    query = (
        f"query({', '.join(params)}) {{ rateLimit {{ cost remaining }} "
        + " ".join(lookups)
        + " }"
    )
    return query, variables


def fetch_graphql(rows: list[dict]) -> tuple[list[dict | None], list[int]]:
    """Facts for every row GraphQL answers, and the positions it did not.

    Only an alias that came back with its fields counts. Not found, blocked,
    a failed query or a spent GraphQL budget all leave the row to REST, whose
    answer — gone, blocked, skipped — is the one this script has always given."""
    results: list[dict | None] = [None] * len(rows)
    left: list[int] = []
    todo = [(repo_of(entry), position) for position, entry in enumerate(rows)]
    batches = [todo[start : start + BATCH] for start in range(0, len(todo), BATCH)]
    for number, batch in enumerate(batches, 1):
        try:
            answer = graphql_request(*query_for(batch))
        except RateLimited:
            answer = None
        data = (answer or {}).get("data") or {}
        cost = data.get("rateLimit") or {}
        answered = 0
        for alias, (repo, position) in enumerate(batch):
            node = data.get(f"r{alias}")
            if isinstance(node, dict) and isinstance(node.get("stargazerCount"), int):
                results[position] = from_graphql(rows[position], repo, node)
                answered += 1
            else:
                left.append(position)
        print(
            f"graphql batch {number}/{len(batches)}: {answered} of {len(batch)} answered"
            + (f", cost {cost.get('cost')}, {cost.get('remaining')} points left" if cost else ", no answer"),
            file=sys.stderr,
        )
    return results, left


def fetch_all(rows: list[dict], *, via: str = "graphql") -> list[dict | None]:
    """Facts for every row: GraphQL in batches, REST for whatever it left."""
    if via == "graphql":
        results, left = fetch_graphql(rows)
    else:
        results, left = [None] * len(rows), list(range(len(rows)))
    if left:
        if via == "graphql":
            print(f"reading {len(left)} row(s) over REST", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            for position, fresh in zip(left, pool.map(fetch, [rows[i] for i in left])):
                results[position] = fresh
    return results


COMPARED = (
    "state", "stars", "repo_license", "archived", "full_name", "html_url", "description",
    "created_at", "pushed_at", "commits",
)


def compare(rows: list[dict]) -> list[str]:
    """Read every row both ways and name each fact the two disagree on. Nothing
    is written; this is how the GraphQL path was shown to match REST."""
    rest = fetch_all(rows, via="rest")
    graph, _ = fetch_graphql(rows)
    differences = []
    for entry, a, b in zip(rows, rest, graph):
        if a is None or b is None:
            continue  # GraphQL did not answer: the refresh reads this row over REST anyway
        for key in COMPARED:
            if a.get(key) != b.get(key):
                differences.append(f"{entry['slug']} ({a['repo']}): {key} rest={a.get(key)} graphql={b.get(key)}")
    return differences


def same_text(text: str | None) -> str:
    """The form in which a summary and a description are compared: letter case,
    runs of whitespace and one final full stop do not make two texts different.
    Nothing else is forgiven — a summary cut short, or with one word changed, is
    not the description."""
    text = " ".join((text or "").split())
    if text.endswith((".", "\u3002")):
        text = text[:-1].rstrip()
    return text.casefold()


def summary_source_for(entry: dict, description: str | None) -> str | None:
    """The summary_source this row should now carry, or None to leave it alone.

      identical to the description        -> upstream-description
      was upstream-description, differs   -> upstream-description-stale
      curated or model-written            -> left alone, whatever GitHub says
      anything else that differs          -> left alone (unlabelled stays so)

    A repository without a description matches nothing. Nothing here can
    produce `curated`: that is a person saying they wrote the text, which no
    comparison can know, and `model-written` says the same of a model. Stale
    is not undone by drifting further; only a description that matches again
    (or a person) changes it.
    """
    summary = entry.get("summary")
    current = entry.get("summary_source")
    if not isinstance(summary, str) or current in WRITTEN_HERE:
        return None
    wanted = same_text(description)
    if wanted and same_text(summary) == wanted:
        return UPSTREAM if current != UPSTREAM else None
    if current == UPSTREAM:
        return UPSTREAM_STALE
    return None


def diff_for(entry: dict, fresh: dict) -> list[tuple[str, object, object]]:
    """Field-level changes this row would take. Empty means nothing moved."""
    changes: list[tuple[str, object, object]] = []

    if entry.get("stars") is not None and entry["stars"] != fresh["stars"]:
        changes.append(("stars", entry["stars"], fresh["stars"]))
    elif entry.get("stars") is None:
        changes.append(("stars", None, fresh["stars"]))

    if entry.get("repo_license") != fresh["repo_license"]:
        changes.append(
            ("repo_license", entry.get("repo_license"), fresh["repo_license"])
        )

    if fresh.get("full_name") and fresh["full_name"].lower() != fresh["repo"].lower():
        changes.append(("renamed", fresh["repo"], fresh["full_name"]))

    flags = set(entry.get("flags", []))
    # Both flags are two-way: a project that gets archived gains the flag, and
    # one that is un-archived or gains a licence loses it. A flag that only
    # ever accumulates would slowly stop meaning anything.
    if fresh["archived"] and "archived" not in flags:
        changes.append(("flags", "archived", "add"))
    if not fresh["archived"] and "archived" in flags:
        changes.append(("flags", "archived", "remove"))

    # `no-license` means no LICENSE file at all, which is exactly repo_license
    # "unknown" — the same definition lint.py enforces. This used to count
    # NOASSERTION as unlicensed too, so a row that correctly moved to NOASSERTION
    # kept telling readers there was no licence: 28 rows, vercel/ai among them.
    unlicensed = fresh["repo_license"] == "unknown"
    if unlicensed and "no-license" not in flags:
        changes.append(("flags", "no-license", "add"))
    if not unlicensed and "no-license" in flags:
        changes.append(("flags", "no-license", "remove"))

    source = summary_source_for(entry, fresh.get("description"))
    if source:
        changes.append(("summary_source", entry.get("summary_source"), source))

    # GitHub's dates and commit count, recorded as it states them. A fact
    # GitHub did not give this time (None) leaves the row's value alone.
    for field, (key, _) in REPO_FACTS.items():
        value = fresh.get(key)
        if value is not None and entry.get(field) != value:
            changes.append((field, entry.get(field), value))

    # Two-way like `archived`: one commit gains the flag, a second loses it.
    # An uncounted repository changes nothing.
    commits = fresh.get("commits")
    if commits == 1 and SINGLE_COMMIT not in flags:
        changes.append(("flags", SINGLE_COMMIT, "add"))
    if commits is not None and commits > 1 and SINGLE_COMMIT in flags:
        changes.append(("flags", SINGLE_COMMIT, "remove"))

    return changes


def change_kind(change: tuple[str, object, object]) -> str:
    """The CHANGE_FIELDS name --only-field selects a change by: its field,
    except that the single-commit flag goes with repo_commits, which it
    restates."""
    field, what, _ = change
    return "repo_commits" if field == "flags" and what == SINGLE_COMMIT else field


def put_after(entry: dict, key: str, value: object, after: str) -> None:
    """Set entry[key], placing a new key right after `after` so a row reads
    summary, summary_source, summary_zh. Mutates in place, as apply() does:
    the row stays the same object inside the catalogue list."""
    if key in entry or after not in entry:
        entry[key] = value
        return
    items = list(entry.items())
    entry.clear()
    for name, current in items:
        entry[name] = current
        if name == after:
            entry[key] = value


def apply(entry: dict, fresh: dict, changes: list[tuple[str, object, object]]) -> None:
    for field, a, b in changes:
        if field == "stars":
            entry["stars"] = b
        elif field == "repo_license":
            entry["repo_license"] = b
        elif field == "renamed":
            # Rewrite whichever of url / repo points at the old name, keeping
            # any path inside the repository (a /blob/ link stays a /blob/ link).
            for key in ("url", "repo"):
                value = entry.get(key, "")
                prefix = f"https://github.com/{a}"
                if value.lower().startswith(prefix.lower()):
                    entry[key] = f"https://github.com/{b}" + value[len(prefix) :]
        elif field == "flags":
            flags = entry.setdefault("flags", [])
            if b == "add" and a not in flags:
                flags.append(a)
            elif b == "remove" and a in flags:
                flags.remove(a)
            if not flags:
                entry.pop("flags", None)
        elif field == "summary_source":
            put_after(entry, "summary_source", b, "summary")
        elif field in REPO_FACTS:
            anchors = REPO_FACTS[field][1]
            put_after(entry, field, b, next((key for key in anchors if key in entry), anchors[-1]))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="apply the changes")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--only",
        default="",
        help="only refresh rows whose slug contains this substring",
    )
    parser.add_argument(
        "--digest",
        default="",
        help="also write a Markdown summary to this path, for an issue body",
    )
    parser.add_argument(
        "--via",
        choices=("graphql", "rest"),
        default="graphql",
        help="graphql (default): batched, REST for what it leaves; rest: one request per row",
    )
    parser.add_argument(
        "--compare",
        action="store_true",
        help="read the rows both ways and list any fact they disagree on; writes nothing",
    )
    parser.add_argument(
        "--only-field",
        action="append",
        choices=CHANGE_FIELDS,
        default=[],
        metavar="FIELD",
        help=(
            "report and apply only this kind of change (repeatable): "
            + ", ".join(CHANGE_FIELDS)
            + ". Every other change is left out of the report and unwritten. The "
            "single-commit flag goes with repo_commits, not with flags."
        ),
    )
    args = parser.parse_args()
    only_fields = set(args.only_field)
    if only_fields:
        print(f"only these changes: {', '.join(sorted(only_fields))}; every other one is left as it is", file=sys.stderr)

    catalog = json.loads(CATALOG.read_text())
    rows = [
        e
        for e in catalog
        if repo_of(e) and repo_of(e) != SELF and args.only in e["slug"]
    ]
    print(f"refreshing {len(rows)} row(s) with a GitHub repository\n", file=sys.stderr)

    if args.compare:
        differences = compare(rows)
        for line in differences:
            print(f"  {line}")
        print(f"\n{len(differences)} difference(s) between REST and GraphQL across {len(rows)} row(s)")
        log_usage()
        return 1 if differences else 0

    # Nothing below raises for one row or for a spent budget: every row comes
    # back with a state, so the rows that were read are always written.
    results = fetch_all(rows, via=args.via)

    report: list[dict] = []
    gone: list[str] = []
    blocked: list[dict] = []
    skipped: list[str] = []
    for entry, fresh in zip(rows, results):
        if fresh is None:
            continue
        if fresh["state"] == "skipped":
            skipped.append(entry["slug"])
            continue
        if fresh["state"] == "blocked":
            blocked.append(fresh)
            continue
        if fresh["state"] == "gone":
            gone.append(f"{entry['slug']} ({fresh['repo']})")
            continue
        changes = diff_for(entry, fresh)
        if only_fields:
            changes = [change for change in changes if change_kind(change) in only_fields]
        if not changes:
            continue
        report.append(
            {
                "slug": entry["slug"],
                "repo": fresh["repo"],
                "changes": [{"field": f, "from": a, "to": b} for f, a, b in changes],
            }
        )
        if args.write:
            apply(entry, fresh, changes)

    if args.write and report:
        CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")

    if args.digest:
        pathlib.Path(args.digest).write_text(
            digest(report, gone, len(rows), blocked=blocked, skipped=len(skipped))
        )

    tally = (
        f"checked {len(rows) - len(skipped)} of {len(rows)} row(s): "
        f"{len(skipped)} skipped (GitHub API budget), {len(blocked)} blocked, "
        f"{len(gone)} did not resolve"
    )
    step_summary(
        "## Repository facts\n\n"
        + f"- {tally}\n"
        + f"- {'applied' if args.write else 'would change'} {len(report)} row(s)\n"
        + "".join(f"- {line}\n" for line in usage_lines())
    )

    if args.json:
        print(
            json.dumps(
                {
                    "changed": report,
                    "unreachable": gone,
                    "blocked": [{"slug": b["slug"], "repo": b["repo"], "detail": b["detail"]} for b in blocked],
                    "skipped": skipped,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        log_usage()
        return 0

    for item in report:
        print(f"  {item['slug']}")
        for change in item["changes"]:
            if change["field"] == "flags":
                print(f"      flag {change['to']}: {change['from']}")
            else:
                print(f"      {change['field']}: {change['from']} -> {change['to']}")
    if gone:
        print(
            f"\n  {len(gone)} repository(ies) did not resolve — deleted, renamed or private:"
        )
        for item in gone:
            print(f"      {item}")
        print(
            "  These need a person: a rename is fixable, a deletion means retiring the row."
        )
    if blocked:
        print(f"\n  {len(blocked)} repository(ies) GitHub refuses to serve:")
        for item in blocked:
            print(f"      {item['slug']} ({item['repo']}) {item['detail']}")
    if skipped:
        print(
            f"\n  {len(skipped)} row(s) not re-read: the GitHub API budget ran out. "
            "They keep their previous facts."
        )

    verb = "applied" if args.write else "would change"
    print(f"\n{tally}")
    print(f"{verb} {len(report)} row(s) of {len(rows)}")
    if report and not args.write:
        print("Run with --write to apply.")
    log_usage()
    return 0


def digest(
    report: list[dict],
    gone: list[str],
    checked: int,
    *,
    blocked: list[dict] | None = None,
    skipped: int = 0,
) -> str:
    """What a person needs from a weekly refresh, in a form that fits an issue.

    Stars move on most rows every week; listing each one produced a report far
    past GitHub's 65,536-character issue body limit, so the notice for a
    refresh would have failed to post. Star-only changes are counted, and so
    are a last push or a commit count moving and a creation date recorded for
    the first time: routine() says which. Anything else — a licence changing,
    a project archived, a flag gained or lost, a repository gone or blocked,
    rows the API budget left unread — is the reason a person reads this at all.
    Unread rows are counted, not listed: on a bad week that is most of them.
    """
    blocked = blocked or []
    stars_only = [r for r in report if {c["field"] for c in r["changes"]} == {"stars"}]
    # A summary found identical to its repository's description is labelled,
    # counted and not listed: the first run labelled hundreds. A summary whose
    # description has since changed is listed; a person may want to reread it.
    labelled = [r for r in report if any(labels_upstream(c) for c in r["changes"])]
    activity = [r for r in report if any(c["field"] in REPO_FACTS and routine(c) for c in r["changes"])]
    notable = [r for r in report if not all(routine(c) for c in r["changes"])]
    read = f"{checked - skipped} of {checked}" if skipped else f"{checked}"
    lines = [
        f"Re-read {read} repositories: {len(report)} rows changed, "
        f"{len(stars_only)} of them stars only.",
        "",
    ]
    if labelled:
        lines += [
            f"{len(labelled)} summaries are now labelled `{UPSTREAM}`: each is identical to its "
            "repository's own GitHub description.",
            "",
        ]
    if activity:
        lines += [
            f"{len(activity)} rows record a new last push, commit count or first creation date "
            "(`repo_pushed_at`, `repo_commits`, `repo_created_at`), as GitHub states them.",
            "",
        ]
    if notable or blocked:
        lines += ["**Worth a look before merging:**", ""]
        for item in notable:
            parts = [
                f"{c['field']} {c['from']} → {c['to']}"
                if c["field"] != "flags"
                else f"flag `{c['from']}` {c['to']}"
                for c in item["changes"]
                if not routine(c)
            ]
            lines.append(f"- `{item['slug']}` ({item['repo']}): " + "; ".join(parts))
        for item in blocked:
            lines.append(
                f"- `{item['slug']}` ({item['repo']}): GitHub refuses to serve it ({item['detail']})"
            )
        lines.append("")
    if gone:
        lines += [
            f"**{len(gone)} repositories did not resolve** — deleted, renamed or "
            "private. A rename is fixable; a deletion means retiring the row with a "
            "notes line saying why.",
            "",
        ]
        lines += [f"- {item}" for item in gone]
        lines.append("")
    if skipped:
        lines += [
            f"**{skipped} repositories were not re-read** — the GitHub API budget ran "
            "out before they were reached. They keep their previous facts; the run's "
            "summary says what was spent.",
            "",
        ]
    if not notable and not gone and not blocked and not skipped and not labelled and not activity:
        lines += ["Nothing but star counts moved.", ""]
    return "\n".join(lines)


def labels_upstream(change: dict) -> bool:
    """A change that only records a summary matching its repository's description."""
    return change["field"] == "summary_source" and change["to"] == UPSTREAM


def routine(change: dict) -> bool:
    """A change the digest counts rather than lists: stars, a label recording a
    match, a last push or commit count moving, a creation date recorded for the
    first time. A creation date that changes is listed: GitHub keeps a
    repository's creation date through renames and transfers, so a new one
    usually means another repository now answers to that name."""
    field = change["field"]
    if field in ("stars", "repo_pushed_at", "repo_commits") or labels_upstream(change):
        return True
    return field == "repo_created_at" and change["from"] is None


if __name__ == "__main__":
    sys.exit(main())
