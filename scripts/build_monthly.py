#!/usr/bin/env python3
"""Write one month's ecosystem report: docs/monthly/<YYYY-MM>.md (D1).

The site's "what's new" page and its feeds list rows as they arrive, week by
week. Nothing said what a month added up to: how the catalogue grew, what kinds
of project and which languages and platforms the new rows brought, which
measurements arrived, and which new rows people were starring. This writes that
page once a month, for the month before, from

  * the weekly snapshots in history/ (scripts/snapshot_stats.py): the counts at
    the newest snapshot before the month began and at the newest one inside it;
  * catalog.json and retired.json: the rows whose `first_seen` falls in the
    month, and the rows retired in it (the date their notes give);
  * the end snapshot's star counts, so the "most starred" list is the month's,
    not today's;
  * the start and end snapshots' star counts again, for the products that rose
    fastest over the month (launches.rising, the rule the board's rising list
    uses; L29 of the launch plan's third round);
  * launches/*.json: the launch weeks whose Sunday falls in the month and that
    have closed, each with its top three (L17 of the 2026-11-03 launch-board
    plan, docs/launches.md). Votes stay apart from the evidence here too.

A report is dated and written once: running it again for a month that has a
report refuses unless --force, and regenerate.py never rewrites one, since a
month's figures do not change when the catalogue does later. docs/monthly/
README.md, the index, is rewritten each time. Stars are GitHub's count at the
snapshot, a popularity signal, not a verdict on a project.

The weekly upkeep writes the report on the first Thursday of a month
(MAINTAINING.md). Whether it is announced anywhere is the owner's decision.

Run: python3 scripts/build_monthly.py --month 2026-10
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import pathlib
import re
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import launches  # noqa: E402
import snapshot_stats  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIR = ROOT / "docs" / "monthly"
SITE = "https://kydlikebtc.github.io/awesome-jev/"
MONTH = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
RETIRED_ON = re.compile(r"^Retired (\d{4}-\d{2}-\d{2})")
TOP = 5
STARRED = 10
NEGATIVE = "negative-result"

# (stats key, English, Chinese): the snapshot counts the growth table compares.
GROWTH = (
    ("entries", "Rows", "条目"),
    ("with_code", "With code", "含代码"),
    ("call_site_rows", "Citing a file where the project calls Jev", "引用调用点的行"),
    ("wire_shape_rows", "Citing a file that speaks Jev's request shape", "引用请求结构文件的行"),
    ("independent_reports", "Independent reports", "独立报告"),
    ("negative_results", "Negative results", "负面结果"),
    ("overview_unindexed", "Overview rows with code, not yet indexed by pattern", "带代码、未按模式索引的 overview 行"),
)
HEADER = (
    "<!-- Written once by scripts/build_monthly.py from history/, catalog.json and retired.json. "
    "A dated report: never regenerated or edited by hand. -->"
)


def month_bounds(month: str) -> tuple[str, str]:
    """(first day, first day of the next month), as ISO dates."""
    year, number = (int(part) for part in month.split("-"))
    start = dt.date(year, number, 1)
    end = dt.date(year + (number == 12), number % 12 + 1, 1)
    return start.isoformat(), end.isoformat()


def in_month(date: str | None, month: str) -> bool:
    return bool(date) and str(date)[:7] == month


def snapshots_for(history: list[tuple[str, dict]], month: str) -> tuple[dict | None, dict | None]:
    """(start, end): the newest snapshot before the month began, else the first
    inside it; and the newest inside it. None where there is none."""
    first, _ = month_bounds(month)
    before = [s for d, s in history if d < first]
    inside = [s for d, s in history if in_month(d, month)]
    start = before[-1] if before else (inside[0] if inside else None)
    return start, (inside[-1] if inside else None)


def retired_on(entry: dict) -> str | None:
    match = RETIRED_ON.match(entry.get("notes") or "")
    return match.group(1) if match else None


def row_link(slug: str) -> str:
    return f"[{slug}]({SITE}?lang=en#{urllib.parse.quote(slug)})"


def number(value) -> str:
    return "—" if value is None else str(value)


def change(old, new) -> str:
    if not isinstance(old, int) or not isinstance(new, int):
        return "—"
    return f"{new - old:+d}"


def tally(values) -> list[tuple[str, int]]:
    return sorted(collections.Counter(values).items(), key=lambda kv: (-kv[1], kv[0]))


def growth_table(start: dict, end: dict) -> list[str]:
    lines = [
        f"| Count · 计数 | {start['date']} | {end['date']} | Change · 变化 |",
        "| --- | ---: | ---: | ---: |",
    ]
    rows = [(key, en, zh, start["stats"].get(key), end["stats"].get(key)) for key, en, zh in GROWTH]
    rows.append((
        "queue", "Discovery candidates to read (issue #14)", "发现队列待读候选",
        (start.get("queue") or {}).get("open"), (end.get("queue") or {}).get("open"),
    ))
    for _, en, zh, old, new in rows:
        lines.append(f"| {en} · {zh} | {number(old)} | {number(new)} | {change(old, new)} |")
    return lines


def tally_table(title: tuple[str, str], counted: list[tuple[str, int]]) -> list[str]:
    if not counted:
        return []
    head = f"| {title[0]} · {title[1]} | Rows · 行数 |"
    shown = counted[:TOP]
    rest = sum(n for _, n in counted[TOP:])
    lines = [head, "| --- | ---: |"] + [f"| `{name}` | {n} |" for name, n in shown]
    if rest:
        lines.append(f"| others · 其他 | {rest} |")
    return lines + [""]


def entry_line(entry: dict, stars: int | None) -> list[str]:
    star = f" · ★{stars}" if isinstance(stars, int) else ""
    out = [f"- {row_link(entry['slug'])} · `{entry.get('kind', '?')}`{star}: {entry.get('summary', '').strip()}"]
    if entry.get("summary_zh"):
        out.append(f"  {entry['summary_zh'].strip()}")
    return out


def plain(text: str) -> str:
    """A maker's line, inert in Markdown: no link, no formatting, no @mention."""
    return re.sub(r"([\\`*_{}\[\]<>()#+!|~])", r"\\\1", " ".join(str(text).split())).replace("@", "@\u200b")


def measured(week: dict) -> str:
    """A closed week's measures (L28) as one line: the plan's demand, north
    star and trust numbers, each only when the close recorded it."""
    m = launches.week_measures(week)
    parts = []
    if m["voters"] is not None:
        back = "" if m["returning_voters"] is None else f" ({m['returning_voters']} the week before too)"
        parts.append(f"{m['voters']} accounts voted{back}")
    parts.append(f"{m['north_star']} with at least {launches.NORTH_STAR_VOTES} counted votes")
    if m["tier_known"]:
        parts.append(f"{m['read_at_open']} of {m['tier_known']} read by a person or a model before opening")
    if m["votes"]:
        parts.append(f"{m['discounted']} of {m['votes']} votes counted for less than one")
    return "Measured: " + "; ".join(parts) + "."


def launch_section(month: str, launch_weeks: list[dict], catalog: list[dict]) -> list[str]:
    """The month's closed launch weeks, by their Sunday, each with its top three."""
    rows = {e["slug"]: e for e in catalog}
    closed = [w for w in launch_weeks if w.get("status") == "closed"
              and launches.week_days(w["week"])[1].isoformat()[:7] == month]
    out = [f"## Launches · 发布榜: {len(closed)}", ""]
    if not closed:
        return out + ["No launch week closed this month. · 本月没有收榜的周。"]
    out += [
        "The top three of each week that ended in the month, by counted votes (docs/launches.md). A rank is a "
        "count of votes, not this catalogue's recommendation; the evidence is the catalogue's own record. · "
        "当月结束的每一周的前三名，按计入的票数排序。名次只是票数的排序，不是本目录的推荐；证据来自目录自己的记录。",
        "",
    ]
    streak = launches.gate_streak(launch_weeks)
    out += [
        f"Weeks in a row, ending with the newest closed one, with at least {launches.GATE_LAUNCHES} launches on "
        f"the board and {launches.GATE_VOTERS} accounts whose vote counted: {streak}. The board aims for "
        f"{launches.GATE_WEEKS} in a row. · 截至最新收榜的一周，连续每周至少 {launches.GATE_LAUNCHES} 个 Launch 在榜、"
        f"至少 {launches.GATE_VOTERS} 个账号的票被计入：{streak} 周。目标是连续 {launches.GATE_WEEKS} 周。",
        "",
    ]
    for week in sorted(closed, key=lambda w: w["week"]):
        on = [x for x in week.get("launches") or [] if x.get("status") == "scheduled" and x.get("result")]
        removed = sum(1 for x in week.get("launches") or [] if x.get("status") == "removed")
        page = f"{SITE}weeks/{week['week']}.html"
        out.append(f"### [{week['week']}]({page}): {len(on)} launches, rules {week.get('rules', '?')}"
                   + (f", {removed} removed" if removed else ""))
        out.append("")
        out.append(measured(week))
        out.append("")
        for x in sorted(on, key=lambda x: x["result"]["rank"])[:3]:
            r = x["result"]
            tier = launches.tier(rows.get(x["product"], {}))
            page_of = f"[{x['product']}]({SITE}products/{urllib.parse.quote(x['product'])}.html)"
            out.append(f"{r['rank']}. {page_of}: {plain(x['tagline'])} · {r['votes']} votes, "
                       f"{r['counted']} counted · evidence: {tier}")
        out.append("")
    return out


def rising_section(start: dict, end: dict, catalog: list[dict]) -> list[str]:
    """The products whose stars rose fastest from the month's first snapshot
    to its last, by the board's rule (launches.rising)."""
    risen = launches.rising(catalog, start, end)
    out = [
        f"## Rising · 上升最快: {len(risen)}",
        "",
        f"The products whose GitHub stars grew fastest from the {start['date']} snapshot to the {end['date']} one: "
        f"at least {launches.RISING_MIN} stars gained, in order of the gain as a share of the stars before "
        "(docs/launches.md). A popularity signal, not a verdict. · "
        f"从 {start['date']} 到 {end['date']} 的快照之间 GitHub 星标涨得最快的产品：至少涨了 {launches.RISING_MIN} 个，"
        "按涨幅占原有星标的比例排序。热度信号，不是评价。",
        "",
    ]
    for item in risen:
        e = item["row"]
        page = f"[{e['slug']}]({SITE}products/{urllib.parse.quote(e['slug'])}.html)"
        out.append(f"- {page} · +{item['gained']} ★ ({item['before']} → {item['after']}, "
                   f"{launches.share(item['gained'], item['before'])}): {e.get('summary', '').strip()}")
    if not risen:
        out.append("None. · 无。")
    return out


def render(month: str, history: list[tuple[str, dict]], catalog: list[dict], retired: list[dict],
           *, written: str, launch_weeks: list[dict] = ()) -> str:
    start, end = snapshots_for(history, month)
    if end is None:
        raise ValueError(f"history/ has no snapshot dated in {month}: run this after the month's last weekly refresh")
    added = sorted((e for e in catalog + retired if in_month(e.get("first_seen"), month)), key=lambda e: e["slug"])
    gone = sorted((e for e in retired if in_month(retired_on(e), month)), key=lambda e: e["slug"])
    stars = {r["slug"]: r.get("stars") for r in end.get("rows", [])}
    measured = [e for e in added if e.get("measurement")]
    negative = [e for e in added if NEGATIVE in (e.get("flags") or [])]
    starred = sorted(
        (e for e in added if isinstance(stars.get(e["slug"]), int)),
        key=lambda e: (-stars[e["slug"]], e["slug"]),
    )[:STARRED]

    out = [HEADER, "", f"# {month}: the month in the catalogue · {month} 月度报告", ""]
    out += [
        f"Written on {written} from the weekly snapshots of {start['date']} and {end['date']} and the rows "
        f"`first_seen` in {month}. A count is what the catalogue held, not how the ecosystem grew; a dash is a "
        "count that snapshot did not record. Rows added counts every row first seen in the month, those "
        "after the last snapshot included; the most-starred list has only the rows that snapshot held.",
        "",
        f"写于 {written}，依据 {start['date']} 与 {end['date']} 的每周快照，以及 `first_seen` 落在 {month} 的条目。"
        "计数反映的是目录收录了什么，而不是生态增长了多少；短横表示该快照没有记录这项计数。"
        "新增条目包括当月所有首次收录的行（含最后一份快照之后的）；星标榜只含该快照里已有的行。",
        "",
        "## Counts · 计数",
        "",
        *growth_table(start, end),
        "",
        f"## Rows added · 新增条目: {len(added)}",
        "",
    ]
    if added:
        out += tally_table(("Kind", "类型"), tally(e.get("kind", "?") for e in added))
        out += tally_table(("Language", "语言"), tally(l for e in added for l in e.get("languages") or []))
        out += tally_table(("Platform", "平台"), tally(p for e in added for p in e.get("platforms") or []))
        read_by = collections.Counter(
            "person" if (e.get("evidence") or {}).get("read_on")
            else "model" if (e.get("evidence") or {}).get("model_read_on")
            else "script"
            for e in added
        )
        out += [
            f"Who read the cited file · 谁读过引用文件: a person {read_by['person']} · a model {read_by['model']} · "
            f"neither (a script's match only) {read_by['script']}. 人 {read_by['person']} · 模型 {read_by['model']} · "
            f"都没有（只有脚本匹配）{read_by['script']}。",
            "",
        ]
    out += [f"## Most starred of the new rows · 新增条目中星标最多的: {len(starred)}", ""]
    out += [
        f"By GitHub stars at the {end['date']} snapshot: a popularity signal, not a verdict. · "
        f"按 {end['date']} 快照时 GitHub 的星标数排序：热度信号，不是评价。",
        "",
    ]
    for e in starred:
        out += entry_line(e, stars[e["slug"]])
    if not starred:
        out.append("None. · 无。")
    out += [""] + rising_section(start, end, catalog)
    out += ["", f"## Measurements and negative results · 测量与负面结果: {len(measured)} · {len(negative)}", ""]
    for e in sorted({e["slug"]: e for e in measured + negative}.values(), key=lambda e: e["slug"]):
        out += entry_line(e, stars.get(e["slug"]))
    if not measured and not negative:
        out.append("None this month. · 本月没有。")
    out += ["", f"## Retired · 退役: {len(gone)}", ""]
    for e in gone:
        out.append(f"- `{e['slug']}`: {(e.get('notes') or '').split('. ')[0].strip()}.")
    if not gone:
        out.append("None this month. · 本月没有。")
    out += [""] + launch_section(month, list(launch_weeks), catalog)
    return "\n".join(out).rstrip("\n") + "\n"


def index(directory: pathlib.Path) -> str:
    months = sorted((p.stem for p in directory.glob("*.md") if MONTH.match(p.stem)), reverse=True)
    lines = [
        "<!-- Rewritten by scripts/build_monthly.py whenever it writes a report. -->",
        "",
        "# Monthly reports · 月度报告",
        "",
        "One page per month, written once in the first week of the next from the weekly snapshots in "
        "`history/` and the rows that arrived (`scripts/build_monthly.py`). · 每月一页，在下个月第一周根据 "
        "`history/` 的每周快照和当月新增的条目写成一次（`scripts/build_monthly.py`）。",
        "",
    ]
    return "\n".join(lines + [f"- [{m}]({m}.md)" for m in months]) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--month", required=True, help="YYYY-MM")
    parser.add_argument("--force", action="store_true", help="rewrite a report that exists")
    parser.add_argument("--dir", type=pathlib.Path, default=DIR, help=argparse.SUPPRESS)
    parser.add_argument("--history", type=pathlib.Path, default=ROOT / snapshot_stats.DIR, help=argparse.SUPPRESS)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if not MONTH.match(args.month):
        print(f"error: --month {args.month!r} is not YYYY-MM", file=sys.stderr)
        return 2
    path = args.dir / f"{args.month}.md"
    if path.exists() and not args.force:
        print(f"error: {path} exists; a month's report is written once (--force rewrites it)", file=sys.stderr)
        return 1
    catalog = json.loads((args.root / "catalog.json").read_text(encoding="utf-8"))
    retired = json.loads((args.root / "retired.json").read_text(encoding="utf-8"))
    try:
        text = render(args.month, snapshot_stats.load_history(args.history), catalog, retired,
                      written=dt.datetime.now(dt.timezone.utc).date().isoformat(),
                      launch_weeks=launches.weeks(args.root / "launches"))
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    args.dir.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    (args.dir / "README.md").write_text(index(args.dir), encoding="utf-8")
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
