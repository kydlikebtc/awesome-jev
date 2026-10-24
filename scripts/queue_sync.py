#!/usr/bin/env python3
"""The discovery issue's description: every candidate, and where it stands.

The weekly `discover` run posts what it found each week as a comment on one
open issue labelled `discovery`. Comments pile up, nothing in them changes
when a candidate is catalogued or declined, and ticking a box in a bot's
comment needs write access to this repository. So the issue's description is
this queue instead, rewritten by the same run from files in the repository:

  .discover/seen.json  which repositories a script found calling Jev (calls-jev)
  catalog.json         catalogued: a row's url or repo is that repository
  retired.json         catalogued, and retired since
  docs/declined.txt    a person read it and decided against it
  .discover/facts.json GitHub's figures for each candidate still to read

Nothing here is stored. Each candidate's state is derived from those files on
every run, and a person's decision only ever comes from catalog.json,
retired.json or docs/declined.txt, never from the verdict file. The same files
give the same text byte for byte, so the workflow edits the issue only when
something changed; the only dates in it are each candidate's latest read and
last push, both from those files.

Since 2026-10-24 the candidates to read are ordered by the facts the weekly
refresh keeps (scripts/discover_facts.py): most stars first, then most
commits, then the latest push, and those it has not read yet last, oldest read
first as before. A candidate weak on at least two counts (one commit or
none, no star, no README), or one GitHub no longer finds, is parked: listed
under its own heading, still open to anyone, and back among those to read
once a refresh finds it stronger. Parking decides nothing. And a candidate
catalogued, retired or declined under the name GitHub now gives it (a renamed
or transferred repository) takes that state; until the refresh has read it,
it stays to read under the name the sibling lists cite.

Usage:
  python3 scripts/queue_sync.py               # print the description
  python3 scripts/queue_sync.py --out FILE    # write it to FILE
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import datetime as dt
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import discover_facts  # noqa: E402
import discover_seen  # noqa: E402
from _github import repo_of  # noqa: E402
from discover_candidates import CLAIM_EN, CLAIM_ZH, COMMAND, inert, parse_declined  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
# The site's address (readme.rows.SITE; a test holds them equal). A row's
# permalink there is ?lang=en#<slug>.
SITE = "https://kydlikebtc.github.io/awesome-jev/"
PROPOSED = discover_seen.PROPOSED
# In the order the description lists them.
STATES = ("open", "parked", "catalogued", "retired", "declined")
# GitHub refuses an issue body over 65,536 characters. The caps start here and
# are halved until the text fits under MAX_CHARS.
MAX_CHARS = 60_000
OPEN_SHOWN = 300
DONE_SHOWN = 150

HEADER = (
    "<!-- Written by scripts/queue_sync.py from .discover/seen.json, catalog.json, "
    "retired.json and docs/declined.txt. The weekly discover run rewrites this "
    "description, so an edit here is lost. -->"
)
INTRO_EN = (
    "The discovery queue: every repository the weekly `discover` run found calling "
    "Jev, and where it stands. A ticked box was catalogued, a struck-through one "
    "declined. The state comes from `catalog.json`, `retired.json` and "
    "`docs/declined.txt`, so merging the pull request that adds the row or the "
    "decline is what ticks a box, and this description catches up at the next "
    "weekly run. Those to read come strongest first, by GitHub's figures from "
    "the weekly refresh (`.discover/facts.json`): most stars, then most commits, "
    "then the latest push; any found since then come last. A candidate weak on at "
    "least two counts (one commit or none, no star, no README) is parked below, not "
    "declined: anyone may still read it, and it comes back once a refresh finds it "
    "stronger. Each week's new candidates, with their call sites, are in the "
    "comments below."
)
# Model-written, so marked the way the README marks machine Chinese.
INTRO_ZH = (
    "发现队列：每周 `discover` 运行找到的、代码调用 Jev 的每个仓库，以及它目前的状态。"
    "打勾表示已收录，删除线表示已拒收。状态取自 `catalog.json`、`retired.json` 和 "
    "`docs/declined.txt`，所以合并添加该行或拒收它的 pull request 才会打勾，本描述在下一次"
    "每周运行时更新。待读的候选按每周刷新读到的 GitHub 数据（`.discover/facts.json`）从强到弱排列："
    "先比星标，再比提交数，再比最后推送；刷新之后才发现的排在最后。在“只有一次提交或没有提交、"
    "没有星标、没有 README”三项里至少占两项的候选放在下面的“暂缓”里，这不是拒收："
    "谁都可以照样去读，刷新发现它变强后会回到待读。每周的新候选及其调用点见下方评论。"
    "本描述里的中文（包括下面的标题和计数）都由模型写成。 <sub>(机翻)</sub>"
)
# Each list's heading, in both languages (the Chinese is model-written, as
# INTRO_ZH says).
TITLES = {
    "open": ("To read", "待读"),
    "parked": ("Parked", "暂缓"),
    "catalogued": ("Catalogued", "已收录"),
    "declined": ("Declined", "已拒收"),
    "retired": ("Catalogued and since retired", "收录后已退役"),
}


@dataclasses.dataclass(frozen=True)
class Candidate:
    repo: str  # owner/name, lower-case, as the verdict file keys it
    read_on: str  # the script's latest read of it
    state: str  # one of STATES
    rows: tuple[str, ...] = ()  # catalogue slugs, when catalogued or retired
    reason: str = ""  # the reason given, when declined; what parks it, when parked
    facts: str = ""  # GitHub's figures as the line shows them, when the refresh read it
    rank: tuple = (1,)  # discover_facts.rank(): strongest first, unread last


def rows_by_repo(rows: list) -> dict[str, tuple[str, ...]]:
    """owner/name, lower-cased, to the slugs of every row that links to it."""
    found: dict[str, set[str]] = collections.defaultdict(set)
    for row in rows:
        if not isinstance(row, dict):
            continue
        repo = repo_of(row)
        if repo and isinstance(row.get("slug"), str):
            found[repo.lower()].add(row["slug"])
    return {repo: tuple(sorted(slugs)) for repo, slugs in found.items()}


def derive(
    seen: dict[str, dict],
    catalog: list,
    retired: list,
    declined: dict[str, str],
    facts: dict[str, dict] | None = None,
) -> list[Candidate]:
    """Every repository whose verdict is calls-jev, with its state. A row in
    catalog.json wins over one in retired.json, and either over a decline,
    under the cited name or the one GitHub now gives it; what is left is to
    read, or parked when its facts are weak (discover_facts.parked())."""
    listed, gone = rows_by_repo(catalog), rows_by_repo(retired)
    facts = facts or {}
    out = []
    for repo in sorted(seen):
        entry = seen[repo]
        if entry["verdict"] != PROPOSED:
            continue
        known = facts.get(repo)
        names = (repo, known["name"]) if known and known.get("name") else (repo,)
        in_catalog = tuple(sorted({slug for name in names for slug in listed.get(name, ())}))
        in_retired = tuple(sorted({slug for name in names for slug in gone.get(name, ())}))
        decline = next((name for name in names if name in declined), None)
        if in_catalog:
            out.append(Candidate(repo, entry["on"], "catalogued", rows=in_catalog))
        elif in_retired:
            out.append(Candidate(repo, entry["on"], "retired", rows=in_retired))
        elif decline:
            out.append(Candidate(repo, entry["on"], "declined", reason=declined[decline]))
        else:
            why = discover_facts.parked(known)
            out.append(Candidate(
                repo, entry["on"], "parked" if why else "open", reason=", ".join(why),
                facts=discover_facts.describe(known, parked=bool(why)), rank=discover_facts.rank(known),
            ))
    return out


def link(repo: str) -> str:
    return f"[{repo}](https://github.com/{repo})"


def line_for(c: Candidate) -> str:
    facts = f" · {c.facts}" if c.facts else ""
    if c.state == "open":
        # The script's read, not a person's: nobody has read an open one yet.
        return f"- [ ] {link(c.repo)}{facts} · read by script {c.read_on} · `{COMMAND.format(slug=c.repo)}`"
    if c.state == "parked":
        # No box: nothing is asked of anyone, and nothing was decided.
        return (
            f"- {link(c.repo)} · parked: {c.reason}{facts} · read by script {c.read_on}"
            f" · `{COMMAND.format(slug=c.repo)}`"
        )
    if c.state == "catalogued":
        rows = ", ".join(f"[`{slug}`]({SITE}?lang=en#{slug})" for slug in c.rows)
        return f"- [x] {link(c.repo)} → {rows}"
    if c.state == "retired":
        rows = ", ".join(f"`{slug}`" for slug in c.rows)
        return f"- [x] {link(c.repo)} → {rows}, since retired (`retired.json`)"
    reason = inert(c.reason, 160) if c.reason else "no reason given"
    return f"- [x] ~~{link(c.repo)}~~ · declined: {reason}"


def more(n: int) -> list[str]:
    if not n:
        return []
    return [f"- …and {n} more, not shown to keep this description under GitHub's limit. "
            f"另有 {n} 个未列出，以免本描述超出 GitHub 的长度上限。"]


def title(state: str) -> str:
    return " · ".join(TITLES[state])


PARKED_EN = (
    "Weak on at least two counts by the latest refresh (one commit or none, no star, "
    "no README), or no longer on GitHub. Not declined: read one if you like, and the "
    "first refresh that finds it stronger moves it back to To read."
)
PARKED_ZH = (
    "按最近一次刷新，至少有两项偏弱（只有一次提交或没有提交、没有星标、没有 README），"
    "或者 GitHub 上已经找不到。这不是拒收：想读照样可以读，刷新发现它变强后会移回待读。 <sub>(机翻)</sub>"
)


def done_section(state: str, items: list[Candidate], shown: int) -> list[str]:
    if not items:
        return []
    lines = ["<details>", f"<summary>{title(state)} ({len(items)})</summary>", ""]
    if state == "parked":
        lines += [PARKED_EN, "", PARKED_ZH, ""]
    lines += [line_for(c) for c in items[:shown]] + more(len(items) - min(shown, len(items)))
    return lines + ["", "</details>", ""]


def render(candidates: list[Candidate], *, open_shown: int = OPEN_SHOWN, done_shown: int = DONE_SHOWN) -> str:
    """The description. Candidates to read and parked ones strongest first
    (the ones without facts oldest read first), the rest by name."""
    by = {state: [c for c in candidates if c.state == state] for state in STATES}
    for state in ("open", "parked"):
        by[state].sort(key=lambda c: (c.rank, c.read_on, c.repo))
    lines = [HEADER, "", INTRO_EN, "", INTRO_ZH, ""]
    lines += [
        f"**{len(by['open'])}** to read · **{len(by['parked'])}** parked · **{len(by['catalogued'])}** catalogued · "
        f"**{len(by['declined'])}** declined · **{len(by['retired'])}** catalogued and since retired",
        "",
        " · ".join(f"{TITLES[s][1]} **{len(by[s])}**" for s in ("open", "parked", "catalogued", "declined", "retired"))
        + " <sub>(机翻)</sub>",
        "",
    ]
    if by["open"]:
        lines += [CLAIM_EN, "", CLAIM_ZH, "", f"### {title('open')}", ""]
        lines += [line_for(c) for c in by["open"][:open_shown]]
        lines += more(len(by["open"]) - min(open_shown, len(by["open"]))) + [""]
    elif by["parked"]:
        lines += ["Nothing to read but the parked candidates below.", "",
                  "除了下面暂缓的候选，没有待读的。 <sub>(机翻)</sub>", ""]
    elif candidates:
        lines += ["Nothing to read: every candidate so far is catalogued or declined.", "",
                  "没有待读的候选：迄今每个候选都已收录或已拒收。 <sub>(机翻)</sub>", ""]
    else:
        lines += ["No candidate yet: `.discover/seen.json` records no repository found calling Jev.", "",
                  "还没有候选：`.discover/seen.json` 没有记录任何被发现调用 Jev 的仓库。 <sub>(机翻)</sub>", ""]
    lines += done_section("parked", by["parked"], done_shown)
    lines += done_section("catalogued", by["catalogued"], done_shown)
    lines += done_section("declined", by["declined"], done_shown)
    lines += done_section("retired", by["retired"], done_shown)
    return "\n".join(lines).rstrip("\n") + "\n"


def body(candidates: list[Candidate]) -> str:
    """render(), with the caps halved until the text fits GitHub's limit."""
    open_shown, done_shown = OPEN_SHOWN, DONE_SHOWN
    while True:
        text = render(candidates, open_shown=open_shown, done_shown=done_shown)
        if len(text) <= MAX_CHARS or not (open_shown or done_shown):
            return text
        open_shown, done_shown = open_shown // 2, done_shown // 2


def load_rows(path: pathlib.Path) -> list:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{path.name}: top level is not an array")
    return data


def read_files(root: pathlib.Path) -> tuple[dict, list, list, dict, dict]:
    """derive()'s five inputs from the files under root. Entries of the two
    script-written files that are not shaped as they should be are reported
    and left out; a catalogue that cannot be read raises."""
    catalog = load_rows(root / "catalog.json")
    retired = load_rows(root / "retired.json")
    declined_file = root / "docs" / "declined.txt"
    declined = parse_declined(declined_file.read_text(encoding="utf-8")) if declined_file.exists() else {}
    seen, dropped = discover_seen.load(root / ".discover" / "seen.json", today=dt.date.today())
    discover_seen.report_dropped(".discover/seen.json", dropped)
    facts, dropped = discover_facts.load(root / ".discover" / "facts.json")
    discover_facts.report_dropped(".discover/facts.json", dropped)
    return seen, catalog, retired, declined, facts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write the discovery issue's description.")
    parser.add_argument("--out", default="", metavar="FILE", help="write it here instead of stdout")
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)  # tests
    args = parser.parse_args(argv)
    try:
        seen, catalog, retired, declined, facts = read_files(pathlib.Path(args.root))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    candidates = derive(seen, catalog, retired, declined, facts)
    text = body(candidates)
    counts = collections.Counter(c.state for c in candidates)
    print(
        f"discovery queue: {len(candidates)} candidate(s) among {len(seen)} verdict(s): "
        + ", ".join(f"{counts[state]} {state}" for state in STATES),
        file=sys.stderr,
    )
    if args.out:
        pathlib.Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out} ({len(text)} characters)", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
