#!/usr/bin/env python3
"""Write docs/shape.md and docs/shape.zh-CN.md: the catalogue's shape as a dataset.

Which languages the rows record, how they reach Jev, star bands by kind,
languages by decision pattern, which patterns are filed together and how the
rows spread over their authors. Every number comes from _stats.shape(), the
one definition counts.py prints too, computed from catalog.json, compat.json,
patterns.json and the entry schema when the pages are written.

The pages describe what this catalogue holds: what the sibling directories
and this repository's discovery found and a person filed. That is not the
ecosystem at large, and each section says what its count can and cannot show.
Stars are printed as bands (readme.rows.STAR_BANDS), a popularity signal and
not a quality verdict, so a count moving inside its band changes nothing here.
No author is named. The Chinese page's prose is model-written and says so at
the top.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/build_shape.py
     python3 scripts/build_shape.py --check    # exit 1 if a page is stale
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from dataclasses import dataclass

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
import snapshot_stats  # noqa: E402
from readme.rows import STAR_BANDS, page_name  # noqa: E402

ROOT = _stats.ROOT
DOCS = ROOT / "docs"
PAGES = {"en": "shape.md", "zh": "shape.zh-CN.md"}
HEADER = (
    "<!-- Written by scripts/build_shape.py from catalog.json, compat.json, patterns.json, the entry schema "
    "and history/. Edit those, not this file. -->"
)
# The trend table needs this many snapshots before it is shown (fewer is not a
# trend), and shows at most the newest TREND_SHOWN of them.
TREND_MIN = 3
TREND_SHOWN = 12

TEXT = {
    "en": {
        "title": "The catalogue's shape",
        "nav": "[awesome-jev](../README.md) · [中文](shape.zh-CN.md)",
        "provenance": "",
        "intro": (
            "Counts that describe this catalogue as a dataset, regenerated from `catalog.json` whenever it "
            "changes; the newest link check behind them is dated **{last_sweep}**. They describe what the "
            "catalogue holds, which is what reached it through the sibling directories, this repository's "
            "discovery and its contributors, not the ecosystem at large. A star band is a popularity signal, not a quality "
            "verdict, and nothing here was run or reproduced by this repository. `python3 scripts/counts.py` "
            "prints the same numbers as text; the headline figures are on [the status page](status.md)."
        ),
        "evidence_h": "Evidence by decision pattern",
        "evidence_intro": (
            "What the catalogue records about the rows filed under each pattern: reports counted, not a "
            "verdict. A row counts in every column that applies and under every pattern it is filed under. "
            "**Official documentation** is TypeSafe AI's own documentation pages (`kind: official-docs`). "
            "**Call site**, **wire shape** and **example only** count rows citing a file, by what "
            "`evidence.kind` records it shows: where the project calls Jev; a file speaking Jev's request "
            "shape rather than building on Jev; only an example the project ships. **Independent reports** "
            "are benchmark rows not flagged `vendor-reported`: their authors' measurements, not reproduced by "
            "this repository. **Negative results** are rows whose own author measured Jev for the use and "
            "concluded against it (author-stated; [listed on the status page](status.md#negative-results)). "
            "**No file cited** counts rows with no `evidence` (`evidence_none` may say why). The MCP server's "
            "`list_patterns` and each pattern's page give the same numbers."
        ),
        "overview_reports": (
            "{n} independent reports are filed under `overview` and no other pattern, so this table cannot "
            "count them for the decision they measured until a person files them under it."
        ),
        "ladder_cols": (
            "Rows", "Official documentation", "Call site", "Wire shape", "Example only", "Independent reports",
            "Negative results", "No file cited",
        ),
        "languages_h": "Languages",
        "languages_intro": (
            "Rows recording each language (`languages`; a row may record several). {none} rows record none."
        ),
        "language": "Language",
        "rows": "Rows",
        "platforms_h": "How rows reach Jev",
        "platforms_intro": (
            "`platforms` records how a row reaches Jev. Discovery does not tag it: "
            "`scripts/discover_candidates.py` and the drafts it writes leave the field to the person adding a "
            "row, and `typesafe-api` is what a row records when nobody named another route. So the first group "
            "below counts that default at least as much as a finding: a row that reaches Jev through a "
            "pass-through may record `typesafe-api` alone ([compatibility](compatibility.md)). Each row counts "
            "in exactly one group."
        ),
        "group": "Group",
        "tiers": {
            "typesafe-api-only": "`typesafe-api` and nothing else",
            "compat-surface": (
                "At least one value another surface in [the compatibility table](compatibility.md) stands for "
                "(a gateway, SDK or framework), and not `self-hosted`"
            ),
            "no-surface": (
                "Besides `typesafe-api`, only values no compatibility surface stands for (a host, tool or "
                "framework the example runs in, or a route that table does not describe), and not `self-hosted`"
            ),
            "self-hosted": "`self-hosted`, whatever else is recorded",
            "none": "No value recorded",
        },
        "values_intro": "Every value rows record, with the compatibility surfaces that stand for it:",
        "value": "Value",
        "surfaces": "Compatibility surface",
        "licences_h": "Licences",
        "licences": (
            "The licences the linked repositories declare are counted on [the sources page](sources.md#licences), "
            "beside what this repository's own licence covers."
        ),
        "stars_h": "Stars by kind",
        "stars_intro": (
            "Rows of each kind per star band, from GitHub's count at the last weekly refresh; a row without a "
            "repository has no count. The median is the band of the middle row (the lower of two). A band is "
            "a popularity signal, not a quality verdict, and says nothing about upkeep."
        ),
        "kind": "Kind",
        "with_stars": "With a star count",
        "under": "under {floor}",
        "median": "Median band",
        "by_pattern_h": "Languages by decision pattern",
        "by_pattern_intro": (
            "Rows per pattern recording each of the {n} most recorded languages; the rest share one column. A "
            "row recording two languages counts in both, and a row filed under two patterns counts in both."
        ),
        "pattern": "Pattern",
        "other_languages": "Other languages",
        "no_language": "None recorded",
        "pairs_h": "Patterns filed together",
        "pairs_intro": (
            "{multi} rows are filed under more than one pattern. The {n} pairs most often filed on the same row:"
        ),
        "pair": "Patterns",
        "authors_h": "Authors",
        "authors": (
            "{rows} rows name an author; they name {authors} different ones, compared by display name without "
            "regard to case. {one} of them have one row here, {two} two, and {many} three or more; the most any "
            "one author has is {most}. No author is named on this page: it shows how concentrated the "
            "catalogue is, not who contributes to it."
        ),
        "trend_h": "Over time",
        "trend_none": (
            "No snapshot yet. Each weekly refresh (`.github/workflows/metadata.yml`) writes the catalogue's counts "
            "to `history/<date>.json`, and a table of how they moved appears here from the third snapshot."
        ),
        "trend_few": (
            "Collecting since {first}: {n} in `history/` so far, one per weekly refresh. A table of how the "
            "counts moved appears here from the third."
        ),
        "snapshots": ("snapshot", "snapshots"),
        "trend_intro": (
            "The catalogue's counts at each weekly refresh, from the snapshots in `history/` (generated data, never "
            "a source): {n} since {first}, the newest {shown} shown. A count is what was catalogued on that day, "
            "not how the ecosystem grew; a dash is a count that snapshot did not record. Candidates to read is the "
            "discovery queue's \"To read\" (issue #14), recorded since 2026-10-30: when it grows, drafting is behind "
            "discovery."
        ),
        "trend_cols": (
            "Snapshot", "Entries", "With code", "Rows citing a call site", "Independent reports", "Negative results",
            "Alternatives", "No licence declared", "Candidates to read",
        ),
        "footer": (
            "Generated by `scripts/build_shape.py` from `catalog.json`, `compat.json`, `patterns.json`, the "
            "entry schema and the snapshots in `history/`; edit those, not this page."
        ),
    },
    "zh": {
        "title": "目录的形状",
        "nav": "[awesome-jev](../README.zh-CN.md) · [English](shape.md)",
        "provenance": "> 本页中文说明由模型撰写（机翻），未经人工审校。",
        "intro": (
            "把本目录当作一个数据集来描述的计数，每当 `catalog.json` 变化就重新生成；其背后最新一次链接检查的日期是 "
            "**{last_sweep}**。这些数字描述的是目录收录了什么——即经由兄弟目录、本仓库的发现流程和贡献者进入目录的内容——"
            "而不是整个生态。star 区间是热度信号，不是质量结论；这里的一切都没有被本仓库运行或复现。"
            "`python3 scripts/counts.py` 以文本形式打印同样的数字；主要数字见[状态页](status.md)。"
        ),
        "evidence_h": "按决策模式看证据",
        "evidence_intro": (
            "目录对归入每个模式的行记录了什么：只是计数，不是结论。一行在所有适用的列里都计数，归入几个模式就在几个模式下计数。"
            "**官方文档**是 TypeSafe AI 自己的文档页（`kind: official-docs`）。**调用点**、**接口形态**和**仅示例**"
            "按 `evidence.kind` 记录的文件内容，统计引用了文件的行：项目调用 Jev 的位置；只采用了 Jev 的请求结构、"
            "并非基于 Jev 构建的文件；项目附带的示例。**独立报告**是没有标 `vendor-reported` 的基准测试行："
            "测量是其作者的，未经本仓库复现。**负面结果**是作者本人为该用途测过 Jev、并得出不利于它的结论的行"
            "（作者自述；[在状态页列出](status.md#negative-results)）。**未引用文件**统计没有 `evidence` 的行"
            "（`evidence_none` 可能说明了原因）。MCP server 的 `list_patterns` 和每个模式的页面给出同样的数字。"
        ),
        "overview_reports": (
            "有 {n} 份独立报告只归入了 `overview`、没有归入任何其他模式，所以在有人把它们归入所测的决策之前，"
            "这张表无法把它们计入那个决策。"
        ),
        "ladder_cols": ("行数", "官方文档", "调用点", "接口形态", "仅示例", "独立报告", "负面结果", "未引用文件"),
        "languages_h": "语言",
        "languages_intro": "记录了每种语言的行数（`languages`；一行可以记录多种语言）。有 {none} 行没有记录语言。",
        "language": "语言",
        "rows": "行数",
        "platforms_h": "各行如何接入 Jev",
        "platforms_intro": (
            "`platforms` 记录一行如何接入 Jev。发现流程不会标注它：`scripts/discover_candidates.py` 及其生成的草稿"
            "都把这个字段留给添加该行的人，而没有人写明其他路径时，一行记录的就是 `typesafe-api`。"
            "所以下面第一组的数字至少同样反映了这个默认值，而不只是发现：经由透传接入 Jev 的行也可能只记录 "
            "`typesafe-api`（见[兼容性](compatibility.md)）。每行恰好计入一组。"
        ),
        "group": "分组",
        "tiers": {
            "typesafe-api-only": "只有 `typesafe-api`",
            "compat-surface": "至少有一个值对应[兼容性表](compatibility.md)中的其他接入面（网关、SDK 或框架），且不含 `self-hosted`",
            "no-surface": (
                "除 `typesafe-api` 外只记录没有任何兼容性接入面对应的值（示例运行所在的主机、工具或框架，"
                "或该表未描述的路径），且不含 `self-hosted`"
            ),
            "self-hosted": "含 `self-hosted`，无论还记录了什么",
            "none": "未记录任何值",
        },
        "values_intro": "各行记录的每个值，以及对应它的兼容性接入面：",
        "value": "值",
        "surfaces": "兼容性接入面",
        "licences_h": "许可证",
        "licences": "被链接仓库声明的许可证统计在[来源页](sources.md#licences)，旁边说明了本仓库自身许可覆盖的范围。",
        "stars_h": "按类型看 star",
        "stars_intro": (
            "每种类型在各 star 区间的行数，取自最近一次每周刷新时 GitHub 的计数；没有仓库的行没有计数。"
            "中位数是居中那一行所在的区间（两行居中时取较低者）。区间是热度信号，不是质量结论，也不说明是否有人维护。"
        ),
        "kind": "类型",
        "with_stars": "有 star 计数",
        "under": "不足 {floor}",
        "median": "中位区间",
        "by_pattern_h": "按决策模式看语言",
        "by_pattern_intro": (
            "每个模式下记录了最常见的 {n} 种语言各自的行数；其余语言合为一列。记录两种语言的行在两列都计数，"
            "归入两个模式的行在两个模式下都计数。"
        ),
        "pattern": "模式",
        "other_languages": "其他语言",
        "no_language": "未记录",
        "pairs_h": "一起归档的模式",
        "pairs_intro": "有 {multi} 行归入了不止一个模式。最常出现在同一行上的 {n} 对模式：",
        "pair": "模式",
        "authors_h": "作者",
        "authors": (
            "有 {rows} 行写明了作者，共 {authors} 位不同的作者（按显示名比较，不区分大小写）。其中 {one} 位在本目录只有一行，"
            "{two} 位有两行，{many} 位有三行或更多；单个作者最多有 {most} 行。本页不列出任何作者的名字："
            "它显示的是目录的集中程度，而不是谁在贡献。"
        ),
        "trend_h": "随时间的变化",
        "trend_none": (
            "还没有快照。每次每周刷新（`.github/workflows/metadata.yml`）都会把目录的计数写入 `history/<日期>.json`，"
            "从第三份快照起，这里会出现一张计数变化表。"
        ),
        "trend_few": "自 {first} 起开始收集：`history/` 中目前有 {n}，每次每周刷新一份。从第三份起，这里会出现一张计数变化表。",
        "snapshots": ("1 份快照", "{n} 份快照"),
        "trend_intro": (
            "每次每周刷新时目录的计数，取自 `history/` 中的快照（生成的数据，从不作为数据源）：自 {first} 起共 {n} 份，"
            "显示最新的 {shown} 份。计数反映的是当天目录收录了什么，而不是生态增长了多少；短横表示该快照没有记录这项计数。"
            "待读候选是发现队列（issue #14）的「待读」数，自 2026-10-30 起记录：它增长说明起草跟不上发现。"
        ),
        "trend_cols": ("快照", "条目", "含代码", "引用调用点的行", "独立报告", "负面结果", "替代实现", "未声明许可证", "待读候选"),
        "footer": (
            "由 `scripts/build_shape.py` 根据 `catalog.json`、`compat.json`、`patterns.json`、条目 schema 与 `history/` "
            "中的快照生成；请修改这些文件，不要改本页。"
        ),
    },
}


@dataclass(frozen=True)
class Inputs:
    """What the pages are built from."""

    catalog: list
    patterns: list
    compat: dict
    schema: dict
    taxonomy: dict
    history: tuple = ()  # (date, snapshot) pairs, oldest first: snapshot_stats.load_history()


def load() -> Inputs:
    catalog, _retired, patterns, compat, schema = _stats.load()
    taxonomy = json.loads((ROOT / "taxonomy.json").read_text())
    return Inputs(catalog, patterns, compat, schema, taxonomy, tuple(snapshot_stats.load_history()))


def table(head: list[str], rows: list[list]) -> list[str]:
    cells = [[str(c).replace("|", "\\|") for c in row] for row in rows]
    return ["| " + " | ".join(head) + " |", "|" + "|".join(" --- " for _ in head) + "|"] + [
        "| " + " | ".join(row) + " |" for row in cells
    ]


def band_names(lang: str) -> list[str]:
    """Column names for star band 0 (under the first floor) and each band."""
    return [TEXT[lang]["under"].format(floor=STAR_BANDS[0][0]), *(name for _, name in STAR_BANDS)]


def pattern_name(patterns: list[dict], key: str, lang: str) -> str:
    name = next((p["zh" if lang == "zh" else "en"] for p in patterns if p["key"] == key), key)
    return f"[{name}](by-pattern/{page_name(key, lang)})"


def evidence_section(shape: dict, patterns: list[dict], lang: str) -> list[str]:
    """The pattern x evidence matrix (_stats.evidence_ladder, the MCP server's own definition)."""
    text = TEXT[lang]
    rows = [
        [pattern_name(patterns, key, lang), *ladder.values()] for key, ladder in shape["evidence_by_pattern"].items()
    ]
    out = [f"## {text['evidence_h']}", "", text["evidence_intro"], ""]
    out += table([text["pattern"], *text["ladder_cols"]], rows)
    if shape["overview_only_reports"]:
        out += ["", text["overview_reports"].format(n=shape["overview_only_reports"])]
    return out


def languages_section(shape: dict, lang: str) -> list[str]:
    text = TEXT[lang]
    out = [f"## {text['languages_h']}", "", text["languages_intro"].format(none=shape["rows_without_language"]), ""]
    return out + table([text["language"], text["rows"]], [[f"`{k}`", n] for k, n in shape["languages"].items()])


def platforms_section(shape: dict, compat: dict, lang: str) -> list[str]:
    text = TEXT[lang]
    out = [f"## {text['platforms_h']}", "", text["platforms_intro"], ""]
    out += table([text["group"], text["rows"]], [[text["tiers"][k], n] for k, n in shape["platform_tiers"].items()])
    claimed: dict[str, list[str]] = {}
    for surface in compat["platforms"]:
        for value in surface.get("catalog_platforms") or []:
            claimed.setdefault(value, []).append(f"`{surface['id']}`")
    out += ["", text["values_intro"], ""]
    rows = [[f"`{value}`", ", ".join(claimed.get(value, [])) or "—", n] for value, n in shape["platforms"].items()]
    return out + table([text["value"], text["surfaces"], text["rows"]], rows)


def stars_section(shape: dict, taxonomy: dict, lang: str) -> list[str]:
    text = TEXT[lang]
    kinds = {k["key"]: k["zh" if lang == "zh" else "en"] for k in taxonomy["kinds"]}
    bands = band_names(lang)
    rows = []
    for kind, row in shape["stars_by_kind"].items():
        if not row["rows"]:
            continue
        median = "—" if row["median_band"] is None else bands[row["median_band"]]
        rows.append([f"{kinds.get(kind, kind)} (`{kind}`)", row["rows"], row["with_stars"], *row["bands"], median])
    head = [text["kind"], text["rows"], text["with_stars"], *bands, text["median"]]
    return [f"## {text['stars_h']}", "", text["stars_intro"], ""] + table(head, rows)


def by_pattern_section(shape: dict, patterns: list[dict], lang: str) -> list[str]:
    text = TEXT[lang]
    top = shape["top_languages"]
    rows = []
    for key, langs in shape["languages_by_pattern"].items():
        other = sum(n for name, n in langs.items() if name not in top)
        rows.append([pattern_name(patterns, key, lang), *(langs.get(name, 0) for name in top), other])
    head = [text["pattern"], *(f"`{name}`" for name in top), text["other_languages"]]
    intro = text["by_pattern_intro"].format(n=len(top))
    return [f"## {text['by_pattern_h']}", "", intro, ""] + table(head, rows)


def pairs_section(shape: dict, patterns: list[dict], lang: str) -> list[str]:
    text = TEXT[lang]
    pairs = shape["pattern_pairs"]
    intro = text["pairs_intro"].format(multi=shape["multi_pattern_rows"], n=len(pairs))
    rows = [[f"{pattern_name(patterns, a, lang)} + {pattern_name(patterns, b, lang)}", n] for a, b, n in pairs]
    return [f"## {text['pairs_h']}", "", intro, ""] + table([text["pair"], text["rows"]], rows)


def authors_section(shape: dict, lang: str) -> list[str]:
    text = TEXT[lang]
    a = shape["authors"]
    body = text["authors"].format(
        rows=a["rows_naming_an_author"], authors=a["authors"], one=a["one_row"], two=a["two_rows"],
        many=a["three_or_more_rows"], most=a["most_rows_by_one_author"],
    )
    return [f"## {text['authors_h']}", "", body]


def snapshot_count(n: int, lang: str) -> str:
    one, many = TEXT[lang]["snapshots"]
    if lang == "zh":
        return (one if n == 1 else many).format(n=n)
    return f"{n} {one if n == 1 else many}"


def trend_cells(snapshot: dict) -> list:
    """One snapshot's line: its date and the counts it recorded (— if it did not)."""
    stats, kinds = snapshot.get("stats") or {}, (snapshot.get("counts") or {}).get("kinds") or {}
    values = [stats.get(key) for key in (
        "entries", "with_code", "call_site_rows", "independent_reports", "negative_results",
    )]
    # The discovery queue's "To read", recorded since 2026-10-30.
    values += [kinds.get("alternative"), stats.get("no_licence"), (snapshot.get("queue") or {}).get("open")]
    return [snapshot["date"], *("—" if v is None else v for v in values)]


def trend_section(history: tuple, lang: str) -> list[str]:
    """How the counts moved across the history/ snapshots, once there are
    TREND_MIN of them; until then, since when and how many. Absolute dates
    only: the page must not change because a day passed."""
    text = TEXT[lang]
    out = [f"## {text['trend_h']}", ""]
    if not history:
        return out + [text["trend_none"]]
    first, n = history[0][0], len(history)
    if n < TREND_MIN:
        return out + [text["trend_few"].format(first=first, n=snapshot_count(n, lang))]
    shown = history[-TREND_SHOWN:]
    out += [text["trend_intro"].format(n=n, first=first, shown=len(shown)), ""]
    return out + table(list(text["trend_cols"]), [trend_cells(snapshot) for _, snapshot in shown])


def render(inputs: Inputs, lang: str) -> str:
    text = TEXT[lang]
    shape = _stats.shape(inputs.catalog, inputs.patterns, inputs.compat, inputs.schema)
    out = [HEADER, "", f"# {text['title']}", "", f"<sub>{text['nav']}</sub>", ""]
    if text["provenance"]:
        out += [text["provenance"], ""]
    out += [text["intro"].format(last_sweep=_stats.newest_check(inputs.catalog)), ""]
    for section in (
        evidence_section(shape, inputs.patterns, lang),
        languages_section(shape, lang),
        platforms_section(shape, inputs.compat, lang),
        [f"## {text['licences_h']}", "", text["licences"]],
        stars_section(shape, inputs.taxonomy, lang),
        by_pattern_section(shape, inputs.patterns, lang),
        pairs_section(shape, inputs.patterns, lang),
        authors_section(shape, lang),
        trend_section(inputs.history, lang),
    ):
        out += section + [""]
    return "\n".join(out + ["---", "", text["footer"], ""])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="exit 1 instead of writing a stale page")
    args = parser.parse_args(argv)
    inputs = load()
    shape = _stats.shape(inputs.catalog, inputs.patterns, inputs.compat, inputs.schema)
    summary = (
        f"{shape['entries']} rows, {len(shape['languages'])} languages, {len(shape['platforms'])} platform values, "
        f"{shape['authors']['authors']} authors, {len(inputs.history)} snapshot(s) in history/"
    )
    stale = []
    for lang, name in PAGES.items():
        path = DOCS / name
        page = render(inputs, lang)
        if path.exists() and path.read_text() == page:
            continue
        stale.append(name)
        if not args.check:
            path.write_text(page)
    if args.check and stale:
        print(f"error: docs/{' and docs/'.join(stale)} stale; run python3 scripts/build_shape.py ({summary})",
              file=sys.stderr)
        return 1
    print((f"wrote docs/{' and docs/'.join(stale)}" if stale else "docs/shape*.md are current") + f" ({summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
