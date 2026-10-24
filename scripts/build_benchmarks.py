#!/usr/bin/env python3
"""Write docs/benchmarks.md and docs/benchmarks.zh-CN.md from the benchmark rows' measurements.

A kind: benchmark row may carry `measurement`: what its own author measured,
indexed field by field from the author's report (schema/entry.schema.json,
scripts/measurements.py). These pages put those fields side by side: which
decision patterns have a measured report and in which direction its author
says it went, which comparators and datasets were used, and every measured row
with the columns a reader needs to tell a one-afternoon script from a larger
study (independent or vendor-reported, raw data published, stars as a band,
caveat flags).

Nothing on either page was measured or re-run here. Every direction is the
author's own conclusion, and every place a page shows one says so:
author-stated, not reproduced here. A row whose measurement has no `read_on`
was filled in by a script or a model; one with a `model_read_on` (since
2026-10-24) a model has read against the report since, and its date is marked
as a model's wherever the pages show it. The pages count both kinds and
docs/review-queue.md lists them for a person to read.

Every number is derived from catalog.json when the pages are written; stars
are printed and sorted as bands (readme.rows.STAR_BANDS), so a count that moves
inside its band changes nothing here, and no row's place depends on its
position in the file. The Chinese page's prose is model-written and says so at
the top; task, dataset and comparator names are recorded in English and shown
as recorded on both pages.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/build_benchmarks.py
     python3 scripts/build_benchmarks.py --check    # exit 1 if a page is stale
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from platform_values import load_query  # noqa: E402
from readme.rows import FLAG_LABELS, FLAG_ORDER, esc, label, md_url, sort_key, star_label  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://kydlikebtc.github.io/awesome-jev/"
PAGES = {"en": "benchmarks.md", "zh": "benchmarks.zh-CN.md"}
HEADER = "<!-- Written by scripts/build_benchmarks.py from catalog.json. Edit that, not this file. -->"

TEXT = {
    "en": {
        "title": "Benchmarks, indexed",
        "nav": "[awesome-jev](../README.md) · [中文](benchmarks.zh-CN.md)",
        "provenance": "",
        "qualifier": "author-stated, not reproduced here",
        "intro": (
            "Every `kind: benchmark` row that carries a `measurement`: what its own author measured, indexed "
            "field by field from the author's report. This repository measured and re-ran none of it. A "
            "**direction** is the author's own conclusion about Jev for that task, author-stated and not "
            "reproduced here, and is left blank where the author states none in words. Task, dataset and "
            "comparator names are recorded as the author names them."
        ),
        "counts": (
            "**{benchmarks}** benchmark rows; **{measured}** carry a measurement. Of those, a person has read "
            "**{read}** against their report (`measurement.read_on`) and only a model **{model}** "
            "(`measurement.model_read_on`); a script or a model filled in the other **{unread}** and nobody has "
            "read them back. The review queue lists [the unread rows](review-queue.md#measurement-unread) and "
            "[those only a model has read](review-queue.md#model-read). How the fields were first filled in: "
            "[docs/method.md](method.md). Field rules: [CONTRIBUTING](../CONTRIBUTING.md#field-rules)."
        ),
        "matrix_h": "Direction by decision pattern",
        "matrix_intro": (
            "Benchmark rows per decision pattern, by the direction their authors state. A row filed under "
            "several patterns counts under each."
        ),
        "pattern": "Pattern",
        "none_stated": "none stated",
        "unmeasured": "no measurement recorded",
        "comparators_h": "By comparator",
        "comparators_intro": "What authors compared Jev with, as each names it, and the rows that did.",
        "comparator": "Comparator",
        "datasets_h": "By dataset",
        "datasets_intro": "Named datasets and benchmark suites the measurements used, as each author names them.",
        "dataset": "Dataset",
        "rows": "Rows",
        "table_h": "Every measured report",
        "table_intro": (
            "Rows by star band, then title. **Independent** is yes unless the row is flagged vendor-reported. "
            "**Raw data**: yes when the author publishes per-item results or raw responses, no when the "
            "author says only aggregates are published, — when neither is established. **Pre-registered**: "
            "yes when the author states the protocol or set was fixed before the run. **Taken** is the "
            "measurement's `as_of`, else the row's publication date. **Read** is the day a person read the "
            "report against the fields; a date marked *(model)* is a model's reading, not yet checked by a person."
        ),
        "cols": ("Row", "Stars", "Independent", "Raw data", "Pre-registered", "Caveats", "Task", "Metrics", "n",
                 "Model string", "Taken", "Direction ({q})", "Read"),
        "model_read": "{date} *(model)*",
        "yes": "yes", "no": "no", "report": "report", "nothing": "No benchmark row carries a measurement yet.",
        "footer": "Generated by `scripts/build_benchmarks.py` from `catalog.json`; edit the catalogue, not this page.",
    },
    "zh": {
        "title": "基准测试索引",
        "nav": "[awesome-jev](../README.zh-CN.md) · [English](benchmarks.md)",
        "provenance": (
            "> 本页的中文说明由模型撰写（机翻），未经人工审校。任务、数据集和对比对象的名称按作者的叫法以英文记录，"
            "两种语言的页面上都原样显示。"
        ),
        "qualifier": "作者自述，未经本仓库复现",
        "intro": (
            "所有带 `measurement` 的 `kind: benchmark` 行：作者本人测了什么，按作者的报告逐项索引。"
            "这些测量本仓库一项都没有做过或重跑过。**结论方向**是作者本人对 Jev 在该任务上的结论，"
            "属作者自述、未经本仓库复现；作者没有用文字说明结论的，这一栏留空。"
        ),
        "counts": (
            "共 **{benchmarks}** 条基准测试行；其中 **{measured}** 条带测量字段。这些行里，**{read}** 条已由人对照报告核读"
            "（`measurement.read_on`），**{model}** 条只有模型读过（`measurement.model_read_on`）；其余 **{unread}** 条"
            "由脚本或模型填写，还没有人或模型读回核对。复核队列列出了[未读的行](review-queue.md#measurement-unread)和"
            "[只有模型读过的行](review-queue.md#model-read)。"
            "这些字段最初如何填写：[docs/method.md](method.md)。字段规则：[CONTRIBUTING](../CONTRIBUTING.md#field-rules)。"
        ),
        "matrix_h": "按决策模式看结论方向",
        "matrix_intro": "每个决策模式下的基准测试行数，按作者自述的结论方向分列。归入多个模式的行在每个模式下各计一次。",
        "pattern": "模式",
        "none_stated": "作者未说明",
        "unmeasured": "尚无测量字段",
        "comparators_h": "按对比对象",
        "comparators_intro": "作者拿 Jev 与什么对比（按作者的叫法），以及做了这种对比的行。",
        "comparator": "对比对象",
        "datasets_h": "按数据集",
        "datasets_intro": "测量用到的有名称的数据集和基准套件，按作者的叫法。",
        "dataset": "数据集",
        "rows": "行",
        "table_h": "全部带测量的报告",
        "table_intro": (
            "按 star 区间、再按标题排序。**独立**：除非该行带 vendor-reported 标记，否则为「是」。"
            "**原始数据**：作者公开逐条结果或原始响应为「是」，作者说明只公开汇总为「否」，两者都无法确认为「—」。"
            "**预注册**：作者说明方案或数据集在运行前已固定为「是」。"
            "**测量日期**取测量的 `as_of`，没有则取该行的发布日期。"
            "**核读**是人对照报告核读字段的日期；标 *（模型）* 的日期是模型的阅读，尚无人核对。"
        ),
        "cols": ("行", "星标", "独立", "原始数据", "预注册", "警示", "任务", "指标", "n", "模型字符串", "测量日期",
                 "结论方向（{q}）", "核读"),
        "model_read": "{date} *（模型）*",
        "yes": "是", "no": "否", "report": "报告", "nothing": "目前还没有基准测试行带测量字段。",
        "footer": "由 `scripts/build_benchmarks.py` 根据 `catalog.json` 生成；请修改目录数据，不要改本页。",
    },
}


def _labels(group: list[dict], lang: str) -> dict[str, str]:
    return {item["key"]: item["zh" if lang == "zh" else "en"] for item in group}


def row_link(entry: dict, lang: str) -> str:
    return f"[{esc(entry['title'])}]({SITE}?lang={lang}#{urllib.parse.quote(entry['slug'])})"


def _table(head: list[str], rows: list[list[str]]) -> list[str]:
    return ["| " + " | ".join(head) + " |", "|" + "|".join(" --- " for _ in head) + "|"] + [
        "| " + " | ".join(cells) + " |" for cells in rows
    ]


def matrix(benchmarks: list[dict], patterns: list[dict], taxonomy: dict, lang: str) -> list[str]:
    """Benchmark rows per pattern (those with any), by their authors' stated direction."""
    query = load_query()
    text = TEXT[lang]
    directions = [d["key"] for d in taxonomy["measurement_directions"]]
    names = _labels(taxonomy["measurement_directions"], lang)
    head = [text["pattern"]] + [f"{names[d]} ({text['qualifier']})" for d in directions]
    head += [text["none_stated"], text["unmeasured"]]
    rows = []
    for pattern in patterns:
        under = [e for e in benchmarks if pattern["key"] in e["patterns"]]
        if not under:
            continue
        measured = [query.measurement_of(e) for e in under if query.measurement_of(e)]
        cells = [sum(1 for m in measured if m.get("direction") == d) for d in directions]
        cells += [sum(1 for m in measured if "direction" not in m), len(under) - len(measured)]
        rows.append([pattern["zh" if lang == "zh" else "en"]] + [str(c) if c else "·" for c in cells])
    return _table(head, rows)


def by_name(measured: list[dict], field: str, name_head: str, lang: str) -> list[str]:
    """One line per name `field` (comparators or datasets) holds, most-used first, then by name."""
    query = load_query()
    rows: dict[str, list[dict]] = {}
    for entry in measured:
        for name in query.measurement_of(entry).get(field) or []:
            rows.setdefault(name, []).append(entry)
    order = sorted(rows, key=lambda name: (-len(rows[name]), name.casefold(), name))
    return _table(
        [name_head, TEXT[lang]["rows"]],
        [[esc(name), ", ".join(row_link(e, lang) for e in sorted(rows[name], key=sort_key))] for name in order],
    )


def report_row(entry: dict, lang: str, taxonomy: dict) -> list[str]:
    query = load_query()
    text = TEXT[lang]
    m = query.measurement_of(entry)
    yes_no = {True: text["yes"], False: text["no"]}
    flags = [f"`{label(FLAG_LABELS, f, lang)}`" for f in FLAG_ORDER if f in (entry.get("flags") or [])]
    metrics = _labels(taxonomy["measurement_metrics"], lang)
    task = esc(m["task"]) + (f" · [{text['report']}]({md_url(m['report'])})" if m.get("report") else "")
    return [
        row_link(entry, lang),
        star_label(entry.get("stars")) or "—",
        yes_no[query.is_independent_report(entry)],
        yes_no.get(m.get("raw_data"), "—"),
        yes_no.get(m.get("preregistered"), "—"),
        " ".join(flags) or "—",
        task,
        ", ".join(metrics[k] for k in m.get("metrics") or []) or "—",
        str(m["n"]) if "n" in m else "—",
        f"`{m['model_string']}`" if m.get("model_string") else "—",
        m.get("as_of") or entry.get("published") or "—",
        _labels(taxonomy["measurement_directions"], lang)[m["direction"]] if "direction" in m else "—",
        read_cell(m, lang),
    ]


def read_cell(measurement: dict, lang: str) -> str:
    """The day a person read the report, else a model's day marked as a model's, else a dash."""
    query = load_query()
    found = query.reading(measurement)
    if found is None:
        return "—"
    who, date = found
    return date if who == query.PERSON else TEXT[lang]["model_read"].format(date=date)


def readings(measured: list[dict]) -> dict[str, int]:
    """How many measured rows a person has read, only a model, and nobody."""
    query = load_query()
    who = [query.read_by(query.measurement_of(e)) for e in measured]
    return {"read": who.count(query.PERSON), "model": who.count(query.MODEL), "unread": who.count(None)}


def render(catalog: list[dict], patterns: list[dict], taxonomy: dict, lang: str) -> str:
    query = load_query()
    text = TEXT[lang]
    benchmarks = [e for e in catalog if e.get("kind") == query.BENCHMARK]
    measured = sorted((e for e in benchmarks if query.measurement_of(e)), key=sort_key)
    out = [HEADER, "", f"# {text['title']}", "", f"<sub>{text['nav']}</sub>", ""]
    if text["provenance"]:
        out += [text["provenance"], ""]
    counts = text["counts"].format(benchmarks=len(benchmarks), measured=len(measured), **readings(measured))
    out += [text["intro"], "", counts, ""]
    if not measured:
        return "\n".join(out + [text["nothing"], "", "---", "", text["footer"], ""])
    out += [f"## {text['matrix_h']}", "", text["matrix_intro"], ""] + matrix(benchmarks, patterns, taxonomy, lang)
    out += ["", f"## {text['comparators_h']}", "", text["comparators_intro"], ""]
    out += by_name(measured, "comparators", text["comparator"], lang)
    out += ["", f"## {text['datasets_h']}", "", text["datasets_intro"], ""]
    out += by_name(measured, "datasets", text["dataset"], lang)
    out += ["", f"## {text['table_h']}", "", text["table_intro"], ""]
    head = list(text["cols"])
    head[-2] = head[-2].format(q=text["qualifier"])
    out += _table(head, [report_row(e, lang, taxonomy) for e in measured])
    return "\n".join(out + ["", "---", "", text["footer"], ""])


def load() -> tuple[list[dict], list[dict], dict]:
    catalog = json.loads((ROOT / "catalog.json").read_text())
    patterns = json.loads((ROOT / "patterns.json").read_text())["patterns"]
    taxonomy = json.loads((ROOT / "taxonomy.json").read_text())
    return catalog, patterns, taxonomy


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="exit 1 instead of writing a stale page")
    args = parser.parse_args(argv)
    catalog, patterns, taxonomy = load()
    query = load_query()
    measured = [e for e in catalog if query.measurement_of(e)]
    counts = readings(measured)
    summary = (
        f"{len(measured)} measured benchmark row(s): {counts['read']} read by a person, "
        f"{counts['model']} only by a model, {counts['unread']} by nobody"
    )
    stale = []
    for lang, name in PAGES.items():
        path = DOCS / name
        text = render(catalog, patterns, taxonomy, lang)
        if path.exists() and path.read_text() == text:
            continue
        stale.append(name)
        if not args.check:
            path.write_text(text)
    if args.check and stale:
        print(f"error: docs/{' and docs/'.join(stale)} stale; run python3 scripts/build_benchmarks.py ({summary})",
              file=sys.stderr)
        return 1
    print((f"wrote docs/{' and docs/'.join(stale)}" if stale else "docs/benchmarks*.md are current") + f" ({summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
