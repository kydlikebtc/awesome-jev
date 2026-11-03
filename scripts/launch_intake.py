#!/usr/bin/env python3
"""Answer a launch issue, and collect a week's launches (docs/launches.md).

L10, L11 and T3 of the 2026-11-03 launch-board plan. The launch form
(.github/ISSUE_TEMPLATE/launch.yml) names a catalogued product, says whether
the person launching it made it, and gives one line about it. When such an
issue is opened or edited, launch-intake.yml runs this with `--event`, and it
writes one comment that says one of three things:

- **not launched**, and what to change: the product is not catalogued, is not
  a product (an article, an alternative, a row flagged as no example),
  launched less than 60 days before the week, or the line is out of bounds;
- **held for a person**, and why: the person says they made it and the check
  could not confirm it (L11), the repository is a fork (T3), the product has
  had no push for 60 days (T2), or the account opening the issue is younger
  than 30 days or its age cannot be read;
- **ready**: the launch as it will be written into launches/<week>.json.

A launch submitted by Thursday 23:59 UTC is for the next ISO week; later, for
the week after. The day comes from the issue's own `created_at`, so the answer
does not depend on when the check runs.

Who counts as a maker: a login in the row's `makers` (or the login in its
author.url when it names none), the repository's owner, or a public member of
the organisation that owns it. A repository's collaborator list needs that
repository's own push access, which no token here has; a maintainer confirms
anyone else by adding them to the row's `makers`.

Like draft_from_issue.py, the job that answers an issue only comments: anyone
can open one. `--collect WEEK` reads every open launch issue, assesses each the
same way, and writes the week's file (and, for a maker the check confirmed,
their login and line onto the row) into the working tree, for a person to
review in the Friday merge. It never posts anything.

The three facts the check reads from GitHub (the repository, the account's age,
an organisation's public members) need a token that can read any repository
and account, which the workflow has and the scheduled task that collects on
Fridays does not. So the comment records the facts it was given, in a hidden
line, and `--collect` assesses each issue again against today's catalogue and
weeks with the facts recorded in that issue's latest check comment, which only
github-actions[bot] can have written. `--live` reads GitHub instead. An issue
with no such comment is reported, not collected.

Usage:
  python3 scripts/launch_intake.py --event "$GITHUB_EVENT_PATH" --out comment.md
  python3 scripts/launch_intake.py --issue 81 --out comment.md
  python3 scripts/launch_intake.py --collect 2026-W47 [--live]
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
import launches as L  # noqa: E402
from draft_from_issue import fence, find_row, insert_after, one_line, parse_form, repository, ticked  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://kydlikebtc.github.io/awesome-jev/"
NEW_ENTRY = "https://github.com/kydlikebtc/awesome-jev/issues/new?template=new-entry.yml"
MARKER = "<!-- written by scripts/launch_intake.py -->"
FACTS = re.compile(r"^<!-- launch-intake-facts (\{.*\}) -->$", re.MULTILINE)
BOT = "github-actions[bot]"
LABEL = "launch"

# The form's headings, as GitHub renders an issue form.
FIELDS = {
    "Product": "product",
    "Who is launching it?": "role",
    "One line about it": "tagline",
    "The same line in Chinese (optional)": "tagline_zh",
    "Confirmation": "confirm",
}
MAKER = "I made it, or maintain it (maker)"
HUNTER = "Someone else made it (hunter)"
CONFIRMS = (
    "The product calls Jev to decide something, and its row in the catalogue says where",
    "I will not buy votes or ask accounts to vote in bulk; a launch found gamed is removed, with the reason kept",
)
# The bounds of the launch schema's tagline and tagline_zh.
TAGLINE = (3, 80)
TAGLINE_ZH = (2, 60)
# The cut-off: a launch opened by the end of Thursday (UTC) is for next week.
LAST_DAY = 3  # Monday is 0
YOUNG_DAYS = 30
SITE_SLUG = re.compile(r"(?:#|/products/)([a-z0-9]+(?:-[a-z0-9]+)*)(?:\.html)?/?$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


# --------------------------------------------------------------------------
# What GitHub is asked
# --------------------------------------------------------------------------


class Lookup:
    """The three facts the check reads from GitHub. Tests pass their own."""

    def repo(self, full_name: str) -> dict | None:
        data = _github.api_get(f"/repos/{full_name}")
        return data if isinstance(data, dict) and not data.get("blocked") else None

    def user(self, login: str) -> dict | None:
        data = _github.api_get(f"/users/{login}")
        return data if isinstance(data, dict) and not data.get("blocked") else None

    def public_member(self, org: str, login: str) -> bool:
        status, _ = _github.api_fetch(f"/orgs/{org}/public_members/{login}")
        return status == 204


class Recorder(Lookup):
    """Another lookup's answers, kept as the facts a comment records: only the
    fields the check uses, so the hidden line stays short."""

    def __init__(self, inner: Lookup):
        self.inner = inner
        self.facts: dict = {"repos": {}, "users": {}, "members": {}}

    def repo(self, full_name):
        data = self.inner.repo(full_name)
        kept = None if data is None else {
            "fork": bool(data.get("fork")),
            "parent": {"full_name": ((data.get("parent") or {}).get("full_name"))},
            "owner": {k: (data.get("owner") or {}).get(k) for k in ("login", "type")},
        }
        self.facts["repos"][full_name] = kept
        return kept

    def user(self, login):
        data = self.inner.user(login)
        kept = None if data is None else {"created_at": data.get("created_at")}
        self.facts["users"][login] = kept
        return kept

    def public_member(self, org, login):
        member = self.inner.public_member(org, login)
        self.facts["members"][f"{org}/{login}"] = member
        return member


class Recorded(Lookup):
    """Answers from the facts a check comment recorded. A fact it did not
    record reads as unreadable, which holds the launch for a person."""

    def __init__(self, facts: dict):
        self.facts = facts

    def repo(self, full_name):
        return (self.facts.get("repos") or {}).get(full_name)

    def user(self, login):
        return (self.facts.get("users") or {}).get(login)

    def public_member(self, org, login):
        return (self.facts.get("members") or {}).get(f"{org}/{login}") is True


def facts_line(facts: dict) -> str:
    """The hidden line: JSON whose `>` is escaped, so no value can close the
    HTML comment it sits in."""
    return f"<!-- launch-intake-facts {json.dumps(facts, sort_keys=True).replace('>', chr(92) + 'u003e')} -->"


def recorded_facts(comments: list[dict]) -> dict | None:
    """The facts in the newest check comment, or None when there is none.
    Only a comment github-actions[bot] wrote counts: anyone can type the line."""
    for item in reversed(comments):
        if (item.get("user") or {}).get("login") != BOT or not str(item.get("body") or "").startswith(MARKER):
            continue
        match = FACTS.search(item["body"])
        if match:
            try:
                facts = json.loads(match.group(1))
            except ValueError:
                return None
            return facts if isinstance(facts, dict) else None
    return None


# --------------------------------------------------------------------------
# Reading one issue
# --------------------------------------------------------------------------


def opened_at(issue: dict) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(str(issue.get("created_at") or "").replace("Z", "+00:00"))
    except ValueError:
        return None


def target_week(opened: dt.datetime) -> str:
    """The week a launch opened at `opened` (UTC) is for."""
    day = opened.astimezone(dt.timezone.utc).date()
    monday = day - dt.timedelta(days=day.weekday())
    weeks_ahead = 1 if day.weekday() <= LAST_DAY else 2
    return L.week_of(monday + dt.timedelta(weeks=weeks_ahead))


def resolve(answer: str, catalog: list[dict]) -> dict | None:
    """The catalogued row a form answer names: a slug, the site's address of a
    row or product page, or the project's GitHub URL."""
    text = one_line(answer).strip().strip("<>`")
    by_slug = {r.get("slug"): r for r in catalog}
    if SLUG.match(text.lower()) and text.lower() in by_slug:
        return by_slug[text.lower()]
    match = SITE_SLUG.search(text)
    if text.startswith(SITE) and match and match.group(1) in by_slug:
        return by_slug[match.group(1)]
    full = repository(text)
    return find_row(catalog, full) if full else None


def confirm_maker(login: str, row: dict, repo: dict | None, lookup: Lookup) -> str | None:
    """How `login` is confirmed as one of the row's makers, or None."""
    if L.login_key(login) in {L.login_key(m) for m in L.makers_of(row)}:
        return "named as a maker on the row"
    owner = ((repo or {}).get("owner") or {})
    if L.login_key(str(owner.get("login") or "")) == L.login_key(login):
        return "owns the repository"
    if owner.get("type") == "Organization" and owner.get("login") and lookup.public_member(owner["login"], login):
        return f"a public member of {owner['login']}"
    return None


def assess(issue: dict, catalog: list[dict], all_weeks: list[dict], *, lookup: Lookup) -> dict:
    """What the check makes of one launch issue:

    {"verdict": "ready" | "held" | "refused" | "collected", "week": ..., "row": slug or None,
     "problems": [...], "holds": [...], "maker": how the maker was confirmed or None,
     "launch": the launch item, or None when refused}"""
    form = parse_form(issue.get("body") or "", FIELDS)
    login = str((issue.get("user") or {}).get("login") or "")
    opened = opened_at(issue)
    out: dict = {"verdict": "refused", "week": None, "row": None, "problems": [], "holds": [],
                 "maker": None, "launch": None}
    if not login or opened is None:
        out["problems"].append("the issue has no author or no date, so nothing can be checked")
        return out
    week = out["week"] = target_week(opened)
    monday, _ = L.week_days(week)
    for existing in all_weeks:
        for launch in existing.get("launches") or []:
            if launch.get("issue") == issue.get("number"):
                out.update(verdict="collected", week=existing["week"], row=launch.get("product"), launch=launch)
                return out

    row = resolve(form.get("product", ""), catalog)
    if row is None:
        out["problems"].append(
            "the product is not in the catalogue. Add it with the new-entry form first "
            f"({NEW_ENTRY}); it can launch once its row is in")
        return out
    slug = out["row"] = row["slug"]
    if not L.is_product(row):
        out["problems"].append(
            f"`{slug}` is a {row.get('kind')} row" + ("" if row.get("has_code") else " without code")
            + (" flagged as not an example of deciding with Jev" if set(row.get("flags") or []) & L.query.DISQUALIFYING else "")
            + f"; only {', '.join(L.BOARD_KINDS)} rows with code launch")
    for past_week, _launch in L.launched(all_weeks).get(slug, []):
        past_monday, _ = L.week_days(past_week)
        if past_week == week:
            out["problems"].append(f"`{slug}` is on {week} already")
        elif 0 <= (monday - past_monday).days < L.RELAUNCH_DAYS:
            again = past_monday + dt.timedelta(days=L.RELAUNCH_DAYS)
            out["problems"].append(f"`{slug}` launched in {past_week}; it can launch again in the week of {again}")

    tagline = one_line(form.get("tagline", ""))
    tagline_zh = one_line(form.get("tagline_zh", ""))
    if not TAGLINE[0] <= len(tagline) <= TAGLINE[1]:
        out["problems"].append(f"the line about it is {len(tagline)} characters; it takes {TAGLINE[0]} to {TAGLINE[1]}")
    if tagline_zh and not TAGLINE_ZH[0] <= len(tagline_zh) <= TAGLINE_ZH[1]:
        out["problems"].append(f"the Chinese line is {len(tagline_zh)} characters; it takes {TAGLINE_ZH[0]} to {TAGLINE_ZH[1]}")
    missing = [c for c in CONFIRMS if c not in ticked(form.get("confirm", ""))]
    if missing:
        out["problems"].append("both confirmation boxes need a tick")
    role_answer = one_line(form.get("role", ""))
    if role_answer not in (MAKER, HUNTER):
        out["problems"].append("say who is launching it: the maker or a hunter")
    if out["problems"]:
        return out

    full = _github.repo_of(row)
    repo = lookup.repo(full) if full else None
    role = "hunter"
    if role_answer == MAKER:
        how = confirm_maker(login, row, repo, lookup)
        if how:
            role, out["maker"] = "maker", how
        else:
            # Filed as a hunter's until a person confirms it: a maker launch's
            # submitter is always on the row's makers (check_launches.py).
            out["holds"].append(
                f"{login} says they made it, and the check could not confirm it (not on the row's makers, "
                "not the repository's owner, not a public member of its organisation); a maintainer who "
                "confirms it adds them to the row's `makers` and sets the role to maker")
    if full and repo is None:
        out["holds"].append(f"the repository {full} could not be read, so whether it is a fork is unknown")
    elif repo and repo.get("fork"):
        parent = ((repo.get("parent") or {}).get("full_name")) or "another repository"
        out["holds"].append(f"the repository is a fork of {parent}; a person checks it is more than a copy")
    if L.quiet(row, L.as_of(catalog)):
        out["holds"].append(f"the repository has had no push for more than {L.QUIET_DAYS} days")
    user = lookup.user(login)
    born = L.day((user or {}).get("created_at"))
    if born is None:
        out["holds"].append(f"the age of the account {login} could not be read")
    elif (opened.date() - born).days < YOUNG_DAYS:
        out["holds"].append(f"the account {login} is younger than {YOUNG_DAYS} days")

    launch: dict = {
        "product": slug,
        "issue": issue["number"],
        "submitted_by": login,
        "role": role,
        "submitted_on": opened.date().isoformat(),
        "tagline": tagline,
    }
    if tagline_zh:
        launch["tagline_zh"] = tagline_zh
    launch["status"] = "held" if out["holds"] else "scheduled"
    if out["holds"]:
        launch["reason"] = ("; ".join(out["holds"]))[:300]
    out["launch"] = launch
    out["verdict"] = "held" if out["holds"] else "ready"
    return out


# --------------------------------------------------------------------------
# The comment
# --------------------------------------------------------------------------


def comment(result: dict, facts: dict | None = None) -> str:
    lines = [MARKER] + ([facts_line(facts)] if facts is not None else []) + [""]
    week = result.get("week")
    span = ""
    if week:
        monday, sunday = L.week_days(week)
        span = f"**{week}** (Monday {monday} to Sunday {sunday}, UTC)"
    verdict = result["verdict"]
    if verdict == "collected":
        lines.append(f"This launch is on {span}. Its Discussion opens on that Monday; nothing else to do.")
    elif verdict == "refused":
        lines += ["This is an automatic check, and it cannot put the launch on the board yet:", ""]
        lines += [f"- {p}" for p in result["problems"]]
        lines += ["", "Edit the issue to fix it, and the check runs again."]
    elif verdict == "held":
        lines += [f"Held for a person, for {span}:", ""]
        lines += [f"- {h}" for h in result["holds"]]
        lines += ["", "A maintainer decides before Friday's merge. Nothing to do unless they ask."]
    else:
        maker = f" Confirmed as a maker: {result['maker']}." if result.get("maker") else ""
        lines.append(f"Ready for {span}.{maker} It reaches the board with the Friday merge, and its "
                     "Discussion opens on Monday, where a thumbs-up is a vote.")
    if result.get("launch") and verdict != "collected":
        text = json.dumps(result["launch"], ensure_ascii=False, indent=2)
        tick = fence(text)
        lines += ["", "What goes into the week's file:", "", f"{tick}json", text, tick]
    if result.get("row"):
        lines += ["", f"The product's page: {SITE}products/{result['row']}.html"]
    lines += ["", "How the board works: https://github.com/kydlikebtc/awesome-jev/blob/main/docs/launches.md", ""]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Collecting a week
# --------------------------------------------------------------------------


def collect(week: str, issues: list[dict], catalog: list[dict], all_weeks: list[dict], *,
            lookup: Lookup | Callable[[dict], Lookup | None]) -> tuple[dict, list[str], list[str]]:
    """The week's file with every open launch issue for it added, the rows a
    confirmed maker's launch fills in (their login on `makers`, their line as
    the row's `tagline` when it has none), and a line per issue saying what
    happened to it. Launches already on the file stay as they are. `lookup`
    is one Lookup for every issue, or a function giving each issue its own
    (its recorded facts), None when it has none."""
    current = next((w for w in all_weeks if w.get("week") == week), None)
    data = json.loads(json.dumps(current)) if current else {"week": week, "status": "scheduled", "launches": []}
    if data.get("status") != "scheduled":
        raise ValueError(f"{week} is {data.get('status')}; launches are added only before it opens")
    rows = {r["slug"]: r for r in catalog}
    changed: list[str] = []
    notes: list[str] = []
    for issue in sorted(issues, key=lambda i: i.get("number") or 0):
        number = issue.get("number")
        own = lookup if isinstance(lookup, Lookup) else lookup(issue)
        if own is None:
            notes.append(f"#{number}: no check comment from {BOT} to collect from; run launch-intake on it")
            continue
        result = assess(issue, catalog, all_weeks, lookup=own)
        if result["verdict"] == "collected" or result["week"] != week:
            continue
        if result["verdict"] == "refused":
            notes.append(f"#{number}: not launched ({'; '.join(result['problems'])})")
            continue
        launch = result["launch"]
        if any(x.get("product") == launch["product"] for x in data["launches"]):
            notes.append(f"#{number}: {launch['product']} is on {week} already, from an earlier issue")
            continue
        if len(data["launches"]) >= 60:
            notes.append(f"#{number}: {week} is full (60 launches); it waits for the next week")
            continue
        data["launches"].append(launch)
        notes.append(f"#{number}: {launch['product']} {launch['status']}"
                     + (f" ({launch['reason']})" if launch.get("reason") else ""))
        if result.get("maker"):
            row = rows[launch["product"]]
            before = json.dumps(row, sort_keys=True)
            known = {L.login_key(m) for m in L.makers_of(row)}
            if L.login_key(launch["submitted_by"]) not in known:
                makers = L.makers_of(row) + [launch["submitted_by"]]
                rows[launch["product"]] = row = insert_after(row, "author", "makers", makers[:10])
            if not row.get("tagline"):
                row = insert_after(row, "zh_machine" if "zh_machine" in row else "summary_zh", "tagline", launch["tagline"])
                if launch.get("tagline_zh"):
                    row = insert_after(row, "tagline", "tagline_zh", launch["tagline_zh"])
                rows[launch["product"]] = row
            if json.dumps(row, sort_keys=True) != before:
                changed.append(launch["product"])
    for i, row in enumerate(catalog):
        if row.get("slug") in changed:
            catalog[i] = rows[row["slug"]]
    return data, changed, notes


def open_issues(repo: str) -> list[dict]:
    """Every open issue labelled `launch`."""
    out: list[dict] = []
    for page in range(1, 11):
        batch = _github.api_get(f"/repos/{repo}/issues?labels={LABEL}&state=open&per_page=100&page={page}")
        if not isinstance(batch, list):
            break
        out += [i for i in batch if "pull_request" not in i]
        if len(batch) < 100:
            break
    return out


def issue_comments(repo: str, number: int) -> list[dict]:
    found = _github.api_get(f"/repos/{repo}/issues/{number}/comments?per_page=100")
    return found if isinstance(found, list) else []


def write_json(path: pathlib.Path, data, *, indent: int = 2) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=indent) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None, *, lookup: Lookup | None = None,
         issues_for: Callable[[str], list[dict]] = open_issues,
         comments_for: Callable[[str, int], list[dict]] = issue_comments) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--event", metavar="FILE", help="the `issues` event payload ($GITHUB_EVENT_PATH)")
    source.add_argument("--issue", metavar="NUMBER", help="read this issue from the API instead")
    source.add_argument("--collect", metavar="WEEK", help="write every open launch issue for WEEK into its file")
    parser.add_argument("--out", metavar="FILE", help="with --event or --issue: write the comment here")
    parser.add_argument("--live", action="store_true",
                        help="with --collect: read GitHub's facts again instead of those each check comment recorded")
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    lookup = lookup or Lookup()
    root = pathlib.Path(args.root)
    catalog_path = root / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    all_weeks = L.weeks(root / "launches")
    repo = os.environ.get("GITHUB_REPOSITORY") or _github.SELF

    if args.collect:
        week = args.collect.strip()
        if not L.WEEK.match(week):
            print(f"error: --collect takes an ISO week like 2026-W47, not {week!r}", file=sys.stderr)
            return 2
        try:
            def recorded(issue: dict) -> Lookup | None:
                facts = recorded_facts(comments_for(repo, issue["number"]))
                return Recorded(facts) if facts is not None else None

            data, changed, notes = collect(week, issues_for(repo), catalog, all_weeks,
                                           lookup=lookup if args.live else recorded)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        for note in notes:
            print(f"  {note}")
        if data["launches"] or (root / "launches" / f"{week}.json").exists():
            write_json(root / "launches" / f"{week}.json", data)
        if changed:
            write_json(catalog_path, catalog)
        print(f"{week}: {len(data['launches'])} launch(es) on file; rows filled in: {', '.join(changed) or 'none'}")
        return 0

    if not args.out:
        parser.error("--out is required with --event or --issue")
    if args.event:
        issue = json.loads(pathlib.Path(args.event).read_text(encoding="utf-8")).get("issue") or {}
    else:
        if not re.fullmatch(r"[1-9]\d{0,6}", args.issue.strip()):
            print(f"error: --issue takes an issue number, not {args.issue!r}", file=sys.stderr)
            return 2
        issue = _github.api_get(f"/repos/{repo}/issues/{args.issue.strip()}") or {}
    if not isinstance(issue.get("number"), int) or "pull_request" in issue:
        print("error: no issue to answer", file=sys.stderr)
        return 2
    recorder = Recorder(lookup)
    result = assess(issue, catalog, all_weeks, lookup=recorder)
    pathlib.Path(args.out).write_text(comment(result, recorder.facts), encoding="utf-8")
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"number={issue['number']}\n")
    print(f"issue #{issue['number']}: {result['verdict']} for {result['week']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
