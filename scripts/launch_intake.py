#!/usr/bin/env python3
"""Answer a launch issue, and collect a week's launches (docs/launches.md).

L10, L11 and T3 of the 2026-11-03 launch-board plan. The launch form
(.github/ISSUE_TEMPLATE/launch.yml) names a catalogued product, says whether
the person launching it made it, and gives one line about it. When such an
issue is opened or edited, launch-intake.yml runs this with `--event`, and it
writes one comment that says one of three things:

- **not launched**, and what to change: the product is not catalogued, is not
  a product (an article, an alternative, a row flagged as no example),
  launched less than 60 days before the week, the line is out of bounds, the
  repository has had no push for 60 days (T2), or it is a fork with fewer than
  FORK_COMMITS commits of its own (T3);
- **ready**, for a week: the launch as it will be written into
  launches/<week>.json. A maker the check cannot confirm (L11) launches as a
  hunter, and an account younger than 30 days launches in the first week
  after it turns 30;
- **not read yet**: GitHub did not answer for the repository or the account,
  so the Friday filing reads it again.

Until 2026-11-05 a fork, a quiet repository, an unconfirmed maker and a young
account were held for a person. The owner asked that no step of the board
wait for one, so each now has the rule above, and nothing is held.

A launch submitted by Thursday 23:59 UTC is for the next ISO week; later, for
the week after. The day comes from the issue's own `created_at`, so the answer
does not depend on when the check runs. A launch that missed its week (it
could not be read that Friday, or no filing ran) goes on the next one.

Who counts as a maker: a login in the row's `makers` (or the login in its
author.url when it names none), the repository's owner, a public member of
the organisation that owns it, or one of its MAKER_TOP most active
contributors with at least MAKER_COMMITS commits (GitHub's public
contributors list). A repository's collaborator list needs that repository's
own push access, which no token here has.

Like draft_from_issue.py, the job that answers an issue only comments: anyone
can open one. `--collect WEEK` reads every open launch issue, assesses each the
same way, and writes the week's file (and, for a maker the check confirmed,
their login and line onto the row) into the working tree. It never posts
anything. Since L26 (2026-11-04) launch-collect.yml runs `--collect next` early
every Friday, once the week's submissions have closed, and pushes what it
wrote to `main` the way launch-week.yml does; nothing waits for a merge or a
person.

The facts the check reads from GitHub (the repository, the account's age, an
organisation's public members, the repository's top contributors and, for a
fork, how far it is ahead of its parent) need a token that can read any
repository and account. The comment records the facts it was given, in a
hidden line, and `--collect` assesses each issue again against today's
catalogue and weeks with the facts recorded in that issue's latest check
comment, which only github-actions[bot] can have written, and reads GitHub for
any fact the comment does not hold (launch-collect.yml has the token).
`--live` reads every fact from GitHub instead.

`--unread` lists the products about to launch whose call site nobody has
read (evidence tier `file` or `none`): those on a week that has not opened
and those an open launch issue names. The daily task reads them first, so a
launch opens with at least a model's reading (L28).

Usage:
  python3 scripts/launch_intake.py --event "$GITHUB_EVENT_PATH" --out comment.md
  python3 scripts/launch_intake.py --issue 81 --out comment.md
  python3 scripts/launch_intake.py --collect 2026-W47 [--live]
  python3 scripts/launch_intake.py --collect next      # the week of the coming Monday (UTC)
  python3 scripts/launch_intake.py --unread
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import urllib.parse
from typing import Callable

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _github  # noqa: E402
import launches as L  # noqa: E402
from draft_from_issue import fence, find_row, insert_after, one_line, parse_form, repository, ticked  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = L.query.SITE
NEW_ENTRY = f"{L.query.REPOSITORY_URL}/issues/new?template=new-entry.yml"
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
YOUNG_DAYS = 30
# Who else counts as a maker: one of the repository's MAKER_TOP most active
# contributors, with at least MAKER_COMMITS commits.
MAKER_TOP = 3
MAKER_COMMITS = 5
# A fork launches once it has this many commits its parent does not.
FORK_COMMITS = 10
SITE_SLUG = re.compile(r"(?:#|/products/)([a-z0-9]+(?:-[a-z0-9]+)*)(?:\.html)?/?$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


# --------------------------------------------------------------------------
# What GitHub is asked
# --------------------------------------------------------------------------


class Lookup:
    """The facts the check reads from GitHub. Tests pass their own."""

    def repo(self, full_name: str) -> dict | None:
        data = _github.api_get(f"/repos/{full_name}")
        return data if isinstance(data, dict) and not data.get("blocked") else None

    def user(self, login: str) -> dict | None:
        data = _github.api_get(f"/users/{login}")
        return data if isinstance(data, dict) and not data.get("blocked") else None

    def public_member(self, org: str, login: str) -> bool:
        status, _ = _github.api_fetch(f"/orgs/{org}/public_members/{login}")
        return status == 204

    def contributors(self, full_name: str) -> list | None:
        """[[login, commits], ...]: the repository's MAKER_TOP most active
        contributors, or None when GitHub does not say."""
        data = _github.api_get(f"/repos/{full_name}/contributors?per_page={MAKER_TOP}")
        if not isinstance(data, list):
            return None
        return [[str(c.get("login") or ""), int(c.get("contributions") or 0)] for c in data[:MAKER_TOP]
                if isinstance(c, dict)]

    def ahead(self, fork: dict) -> int | None:
        """How many commits a fork's default branch has that its parent's does
        not, or None when GitHub does not say. `fork` is the repository as
        repo() gives it."""
        parent = fork.get("parent") or {}
        owner = ((fork.get("owner") or {}).get("login")) or ""
        if not (parent.get("full_name") and parent.get("default_branch") and fork.get("default_branch") and owner):
            return None
        base, head = (urllib.parse.quote(parent["default_branch"], safe=""),
                      urllib.parse.quote(f"{owner}:{fork['default_branch']}", safe=":"))
        data = _github.api_get(f"/repos/{parent['full_name']}/compare/{base}...{head}")
        return data.get("ahead_by") if isinstance(data, dict) and isinstance(data.get("ahead_by"), int) else None


class Recorder(Lookup):
    """Another lookup's answers, kept as the facts a comment records: only the
    fields the check uses, so the hidden line stays short."""

    def __init__(self, inner: Lookup):
        self.inner = inner
        self.facts: dict = {"repos": {}, "users": {}, "members": {}, "contributors": {}, "ahead": {}}

    def repo(self, full_name):
        data = self.inner.repo(full_name)
        kept = None if data is None else {
            "fork": bool(data.get("fork")),
            "parent": {k: ((data.get("parent") or {}).get(k)) for k in ("full_name", "default_branch")},
            "owner": {k: (data.get("owner") or {}).get(k) for k in ("login", "type")},
            "default_branch": data.get("default_branch"),
            "pushed_at": data.get("pushed_at"),
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

    def contributors(self, full_name):
        found = self.inner.contributors(full_name)
        self.facts["contributors"][full_name] = found
        return found

    def ahead(self, fork):
        found = self.inner.ahead(fork)
        name = str(((fork.get("parent") or {}).get("full_name")) or "")
        self.facts["ahead"][f"{name}..{((fork.get('owner') or {}).get('login')) or ''}"] = found
        return found


class Recorded(Lookup):
    """Answers from the facts a check comment recorded. A fact it did not
    record, or recorded as unreadable, is asked of `fallback` (GitHub, in the
    workflow), and reads as unreadable when there is none."""

    def __init__(self, facts: dict, fallback: Lookup | None = None):
        self.facts = facts
        self.fallback = fallback

    def _get(self, kind: str, key: str):
        found = (self.facts.get(kind) or {}).get(key)
        return found

    def repo(self, full_name):
        found = self._get("repos", full_name)
        return found if found is not None or self.fallback is None else self.fallback.repo(full_name)

    def user(self, login):
        found = self._get("users", login)
        return found if found is not None or self.fallback is None else self.fallback.user(login)

    def public_member(self, org, login):
        found = self._get("members", f"{org}/{login}")
        if found is None and self.fallback is not None:
            return self.fallback.public_member(org, login)
        return found is True

    def contributors(self, full_name):
        found = self._get("contributors", full_name)
        return found if found is not None or self.fallback is None else self.fallback.contributors(full_name)

    def ahead(self, fork):
        name = str(((fork.get("parent") or {}).get("full_name")) or "")
        found = self._get("ahead", f"{name}..{((fork.get('owner') or {}).get('login')) or ''}")
        return found if found is not None or self.fallback is None else self.fallback.ahead(fork)


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
    return L.week_for(opened.astimezone(dt.timezone.utc).date())


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


def confirm_maker(login: str, row: dict, full: str | None, repo: dict | None, lookup: Lookup) -> str | None:
    """How `login` is confirmed as one of the row's makers, or None."""
    if L.login_key(login) in {L.login_key(m) for m in L.makers_of(row)}:
        return "named as a maker on the row"
    owner = ((repo or {}).get("owner") or {})
    if L.login_key(str(owner.get("login") or "")) == L.login_key(login):
        return "owns the repository"
    if owner.get("type") == "Organization" and owner.get("login") and lookup.public_member(owner["login"], login):
        return f"a public member of {owner['login']}"
    for name, commits in (lookup.contributors(full) or [])[:MAKER_TOP] if full else []:
        if L.login_key(str(name)) == L.login_key(login) and int(commits or 0) >= MAKER_COMMITS:
            return f"one of the repository's {MAKER_TOP} most active contributors ({commits} commits)"
    return None


def first_week_from(day: dt.date) -> str:
    """The ISO week of the first Monday on or after `day`."""
    return L.week_of(day + dt.timedelta(days=(7 - day.weekday()) % 7))


def relaunch_problems(slug: str, week: str, all_weeks: list[dict]) -> list[str]:
    monday, _ = L.week_days(week)
    out = []
    for past_week, _launch in L.launched(all_weeks).get(slug, []):
        past_monday, _ = L.week_days(past_week)
        if past_week == week:
            out.append(f"`{slug}` is on {week} already")
        elif 0 <= (monday - past_monday).days < L.RELAUNCH_DAYS:
            out.append(f"`{slug}` launched in {past_week}; it can launch again in the week of "
                       f"Monday {L.relaunch_from(past_week)}")
    return out


def assess(issue: dict, catalog: list[dict], all_weeks: list[dict], *, lookup: Lookup,
           not_before: str | None = None) -> dict:
    """What the check makes of one launch issue:

    {"verdict": "ready" | "unread" | "refused" | "collected", "week": ..., "row": slug or None,
     "problems": [...], "notes": [...], "unread": [...], "maker": how the maker was confirmed or None,
     "launch": the launch item, or None unless ready}

    Nothing is held for a person (since 2026-11-05): each case the check used
    to hold has a rule (the module's docstring). `not_before` is the week the
    Friday filing is filling: a launch whose own week has passed goes on it."""
    form = parse_form(issue.get("body") or "", FIELDS)
    login = str((issue.get("user") or {}).get("login") or "")
    opened = opened_at(issue)
    out: dict = {"verdict": "refused", "week": None, "row": None, "problems": [], "notes": [], "unread": [],
                 "maker": None, "launch": None}
    if not login or opened is None:
        out["problems"].append("the issue has no author or no date, so nothing can be checked")
        return out
    week = target_week(opened)
    if not_before and week < not_before:
        out["notes"].append(f"its own week, {week}, passed before it was filed, so it goes on {not_before}")
        week = not_before
    out["week"] = week
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
    out["problems"] += relaunch_problems(slug, week, all_weeks)

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
    if full and repo is None:
        out["unread"].append(f"the repository {full}")
    # T2: a product people can use now. GitHub's own last push when it was
    # read, so a maker who pushes and edits the issue is checked again at
    # once; the row's weekly fact otherwise.
    pushed = L.day((repo or {}).get("pushed_at")) or L.day(row.get("repo_pushed_at"))
    if pushed and (opened.date() - pushed).days > L.QUIET_DAYS:
        out["problems"].append(
            f"the repository has had no push since {pushed}, more than {L.QUIET_DAYS} days before this issue; "
            "a launch is for a product in use. After a push, edit the issue and the check runs again")
    # T3: a fork launches once it is more than a copy.
    if repo and repo.get("fork"):
        parent = ((repo.get("parent") or {}).get("full_name")) or "another repository"
        ahead = lookup.ahead(repo)
        if ahead is None:
            out["unread"].append(f"how far the fork is ahead of {parent}")
        elif ahead < FORK_COMMITS:
            out["problems"].append(
                f"the repository is a fork of {parent} with {ahead} commit(s) of its own; a fork launches once it "
                f"has {FORK_COMMITS}. If {parent} is catalogued, launch it instead")
        else:
            out["notes"].append(f"a fork of {parent} with {ahead} commits of its own")
    if out["problems"]:
        return out

    role = "hunter"
    if role_answer == MAKER:
        how = confirm_maker(login, row, full, repo, lookup)
        if how:
            role, out["maker"] = "maker", how
        else:
            out["notes"].append(
                f"{login} says they made it, and the check could not confirm it (not on the row's makers, not "
                f"the repository's owner, not a public member of its organisation, not one of its {MAKER_TOP} "
                f"most active contributors), so it launches as a hunter's. The vote post says who launched it")
    user = lookup.user(login)
    born = L.day((user or {}).get("created_at"))
    if born is None:
        out["unread"].append(f"the age of the account {login}")
    elif (opened.date() - born).days < YOUNG_DAYS:
        later = first_week_from(born + dt.timedelta(days=YOUNG_DAYS))
        if later > week:
            out["notes"].append(f"the account {login} is younger than {YOUNG_DAYS} days, so the launch waits "
                                f"for {later}, the first week after it turns {YOUNG_DAYS} days old")
            week = out["week"] = later
            out["problems"] += relaunch_problems(slug, week, all_weeks)
            if out["problems"]:
                return out
    if out["unread"]:
        out["verdict"] = "unread"
        return out

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
    launch["status"] = "scheduled"
    out["launch"] = launch
    out["verdict"] = "ready"
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
    elif verdict == "unread":
        lines += ["This is an automatic check, and GitHub did not answer for:", ""]
        lines += [f"- {u}" for u in result["unread"]]
        lines += ["", f"The filing early on Friday reads it again and puts the launch on {span} if it passes. "
                  "Nothing to do."]
    else:
        maker = f" Confirmed as a maker: {result['maker']}." if result.get("maker") else ""
        lines.append(f"Ready for {span}.{maker} It is filed on the board early on Friday, and its "
                     "Discussion opens on Monday, where a thumbs-up is a vote; the link is posted here then.")
    if result.get("notes") and verdict in ("ready", "unread"):
        lines += ["", "Settled by the board's rules, with nobody to wait for:", ""]
        lines += [f"- {n}" for n in result["notes"]]
    if result.get("launch") and verdict != "collected":
        text = json.dumps(result["launch"], ensure_ascii=False, indent=2)
        tick = fence(text)
        lines += ["", "What goes into the week's file:", "", f"{tick}json", text, tick]
    if result.get("row"):
        lines += ["", f"The product's page: {SITE}products/{result['row']}.html"]
    lines += ["", f"How the board works: {L.query.LAUNCHES_DOC}", ""]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Collecting a week
# --------------------------------------------------------------------------


def collect(week: str, issues: list[dict], catalog: list[dict], all_weeks: list[dict], *,
            lookup: Lookup | Callable[[dict], Lookup | None]) -> tuple[dict, list[str], list[str]]:
    """The week's file with every open launch issue for it added, the rows a
    confirmed maker's launch fills in (their login on `makers`, their line as
    the row's `tagline` when it has none), and a line per issue saying what
    happened to it. Launches already on the file stay as they are, and an
    issue whose own week passed unfiled goes on this one. `lookup` is one
    Lookup for every issue, or a function giving each issue its own (its
    recorded facts, GitHub for the rest), None when it has none."""
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
        result = assess(issue, catalog, all_weeks, lookup=own, not_before=week)
        if result["verdict"] == "collected" or result["week"] != week:
            continue
        if result["verdict"] == "refused":
            notes.append(f"#{number}: not launched ({'; '.join(result['problems'])})")
            continue
        if result["verdict"] == "unread":
            notes.append(f"#{number}: GitHub did not answer for {'; '.join(result['unread'])}; "
                         "the next Friday's filing tries again")
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
                     + (f" ({'; '.join(result['notes'])})" if result.get("notes") else ""))
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


def unread(catalog: list[dict], all_weeks: list[dict], issues: list[dict]) -> list[tuple[str, str, str, str, str]]:
    """(slug, tier, cited path, url, where) for each product about to launch
    whose call site neither a person nor a model has read: on a week not yet
    open (scheduled or held there), or named by an open launch issue not on
    any week yet. Each product once, in the order the board would show it
    soonest: by week, then by issue number."""
    rows = {r["slug"]: r for r in catalog}
    found: dict[str, tuple[str, str, str, str, str]] = {}

    def note(slug: str, where: str) -> None:
        row = rows.get(slug)
        if row is None or slug in found or not L.is_product(row) or L.tier(row) in L.READ:
            return
        found[slug] = (slug, L.tier(row), str((row.get("evidence") or {}).get("path") or ""),
                       str(row.get("url") or ""), where)

    filed: set[int] = set()
    for week in sorted(all_weeks, key=lambda w: str(w.get("week"))):
        for launch in week.get("launches") or []:
            if isinstance(launch.get("issue"), int):
                filed.add(launch["issue"])
            if week.get("status") == "scheduled" and launch.get("status") in ("scheduled", "held"):
                note(launch["product"], f"launches/{week['week']}.json")
    for issue in sorted(issues, key=lambda i: i.get("number") or 0):
        if issue.get("number") in filed:
            continue
        row = resolve(parse_form(issue.get("body") or "", FIELDS).get("product", ""), catalog)
        if row is not None:
            note(row["slug"], f"issue #{issue.get('number')}")
    return list(found.values())


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
    source.add_argument("--collect", metavar="WEEK",
                        help="write every open launch issue for WEEK into its file; `next`: the coming Monday's week")
    source.add_argument("--unread", action="store_true",
                        help="list the products about to launch whose call site nobody has read")
    parser.add_argument("--out", metavar="FILE", help="with --event or --issue: write the comment here")
    parser.add_argument("--live", action="store_true",
                        help="with --collect: read every fact from GitHub again, not first from each check comment")
    parser.add_argument("--on", metavar="DAY", help="today, UTC, for --collect next (default: the clock)")
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    lookup = lookup or Lookup()
    root = pathlib.Path(args.root)
    catalog_path = root / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    all_weeks = L.weeks(root / "launches")
    repo = os.environ.get("GITHUB_REPOSITORY") or _github.SELF

    if args.unread:
        found = unread(catalog, all_weeks, issues_for(repo))
        for slug, tier, path, url, where in found:
            print(f"{slug}\t{tier}\t{path or 'no file cited'}\t{url}\t{where}")
        print(f"{len(found)} product(s) about to launch with no reading of their call site", file=sys.stderr)
        return 0

    if args.collect:
        week = args.collect.strip()
        if week == "next":
            today = L.day(args.on) if args.on else dt.datetime.now(dt.timezone.utc).date()
            if today is None:
                parser.error(f"--on takes a day like 2026-11-06, not {args.on!r}")
            week = L.week_of(today + dt.timedelta(days=7 - today.weekday()))
        if not L.WEEK.match(week):
            print(f"error: --collect takes an ISO week like 2026-W47, not {week!r}", file=sys.stderr)
            return 2
        try:
            def recorded(issue: dict) -> Lookup:
                # The facts the issue's check comment recorded, and GitHub for
                # any it did not (an issue the check never answered: all of them).
                return Recorded(recorded_facts(comments_for(repo, issue["number"])) or {}, fallback=lookup)

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
