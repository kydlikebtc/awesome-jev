#!/usr/bin/env python3
"""Write docs/review-queue.md: the rows a script singles out for a person to read.

Every entry on the page is a machine signal: a path, a string or a combination
of fields matched a rule. None is a finding about the row, and nothing here is
written back into catalog.json. The one exception opens the page: since
2026-10-30, what someone read and left for a person in docs/held.txt
(scripts/held.py), listed as it stands there. Whoever reads a row records the decision in that
row, as each section says, and the row leaves the page at the next regeneration.

Lint could warn once per row instead, but dozens or hundreds of warnings on
every run is a log nobody reads. The same rules count their rows in
_stats.compute(), so docs/status.md publishes the numbers and this page names
the rows.

One section per signal. A section is a function in SECTIONS that takes the
catalogue and returns a Section; add a function there to add a signal. The
Chinese is model-written, and the page says so once at the top.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/build_review_queue.py
     python3 scripts/build_review_queue.py --check    # exit 1 if the page is stale
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.parse
from dataclasses import dataclass

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
import held  # noqa: E402
from _github import repo_of  # noqa: E402
from classify import classify_broad, suggest  # noqa: E402
from evidence_url import evidence_url  # noqa: E402
from measurements import model_read as measurements_model_read  # noqa: E402
from measurements import unread  # noqa: E402
from readme.rows import PATTERN_LABELS, anchor, esc, label, md_url, star_band, star_label  # noqa: E402
from readme.sections import INLINE_MEASURED, INLINE_PER_PATTERN, MEASURED_PLACE, START_PLACE  # noqa: E402
from readme.sections import front_page as printed_by_name  # noqa: E402
from readme.strings import EN, ZH  # noqa: E402
import thresholds  # noqa: E402
import wire  # noqa: E402

ROOT = _stats.ROOT
OUT = ROOT / "docs" / "review-queue.md"
HELD = ROOT / "docs" / "held.txt"
SITE = "https://kydlikebtc.github.io/awesome-jev/"


@dataclass(frozen=True)
class Section:
    """One machine signal and the rows it currently marks."""

    key: str  # the HTML anchor; other pages link to it, so keep it stable
    title_en: str
    title_zh: str
    about_en: str  # what the rule matches, and why that is not a verdict
    about_zh: str
    leave_en: str  # what a person records to take a row off the page
    leave_zh: str
    columns: tuple[tuple[str, str], ...]  # (en, zh) per column
    rows: tuple[tuple[str, ...], ...]  # Markdown cells, one tuple per row


def cell(text: str) -> str:
    """Outside text as an inline code cell: no backtick can close it early,
    no pipe can split the table, no newline can end the row."""
    clean = text.replace("`", "'").replace("\n", " ").replace("|", "\\|")
    return f"`{clean}`"


def row_link(entry: dict) -> str:
    slug = entry["slug"]
    return f"[{slug}]({SITE}?lang=en#{urllib.parse.quote(slug)})"


def file_link(entry: dict) -> str:
    """The cited path, linked as the READMEs and the site link it (evidence_url)."""
    path = entry["evidence"]["path"]
    url = evidence_url(entry)
    return f"[{cell(path)}]({md_url(url)})" if url else cell(path)


EVIDENCE_COLUMNS = (("Row", "行"), ("Kind", "类型"), ("Cited file", "引用的文件"), ("Matched", "匹配文本"))


def evidence_rows(catalog: list[dict], signal) -> tuple[tuple[str, ...], ...]:
    marked = sorted((e for e in catalog if signal(e)), key=lambda e: e["slug"])
    return tuple(
        (row_link(e), cell(e["kind"]), file_link(e), " ".join(cell(m) for m in e["evidence"]["matched"]))
        for e in marked
    )


def examples_dir(catalog: list[dict]) -> Section:
    return Section(
        key="examples-dir",
        title_en="Evidence read from an examples directory",
        title_zh="证据取自 examples 目录",
        about_en=(
            "The cited file sits under an `examples/` or `example/` directory and the row does not "
            "record `evidence.kind`. An SDK's examples are often its clearest call site; a project's "
            "examples can also be all it has, and say little about how it uses Jev itself. The path "
            "cannot tell which."
        ),
        about_zh=(
            "引用的文件位于 `examples/` 或 `example/` 目录下，而该行没有记录 `evidence.kind`。"
            "SDK 的示例往往就是最清楚的调用点；但一个项目的示例也可能是它仅有的调用，"
            "说明不了它自己如何使用 Jev。单凭路径无法判断是哪一种。"
        ),
        leave_en=(
            "To take a row off, read the file and set `evidence.kind`: `call-site` when it is the "
            "project's own use of Jev, `example-only` when it is only an example. Citing a better "
            "file from the project's own code instead also takes it off. A model that does either records "
            "its reading in `evidence.model_read_on`, never in `evidence.read_on`."
        ),
        leave_zh=(
            "移出方法：读这个文件，然后设置 `evidence.kind`——它就是项目自身对 Jev 的使用时设为 "
            "`call-site`，只是示例时设为 `example-only`。改为引用项目自身代码中更合适的文件，也会让它移出。"
            "由模型来做时，把阅读记在 `evidence.model_read_on`，不要记在 `evidence.read_on`。"
        ),
        columns=EVIDENCE_COLUMNS,
        rows=evidence_rows(catalog, _stats.examples_unjudged),
    )


def single_model_name(catalog: list[dict]) -> Section:
    names = ", ".join(cell(name) for name in _stats.MODEL_NAMES_AND_HOST)
    return Section(
        key="single-model-name",
        title_en="Evidence resting on one model name or the API host",
        title_zh="证据只靠一个模型名或 API 主机",
        about_en=(
            f"The only string in `evidence.matched` is one of {names}, or a pinned model version "
            "(`jev-` and a version number). Any file that configures Jev "
            "contains one of them (a settings file, a pricing table, a model list) whether or not it "
            "calls the API, so the weekly text check can keep passing after the call itself is gone."
        ),
        about_zh=(
            f"`evidence.matched` 里唯一的字符串是 {names} 之一，或一个固定的模型版本号"
            "（`jev-` 加版本号）。任何配置 Jev 的文件都会包含它们"
            "（设置文件、价格表、模型列表），不论是否真的调用 API；所以即使调用本身已经删除，"
            "每周的文本检查也可能继续通过。"
        ),
        leave_en=(
            "To take a row off, add a second string from the call itself (an import, the method "
            "called, a question type) to `evidence.matched`, then run "
            "`python3 scripts/verify_claims.py --only <slug>` to confirm the file holds every string. A "
            "model that does this records its reading in `evidence.model_read_on`, never in `evidence.read_on`."
        ),
        leave_zh=(
            "移出方法：从调用本身再取一个字符串（import、被调用的方法、问题类型）加入 "
            "`evidence.matched`，然后运行 `python3 scripts/verify_claims.py --only <slug>`，"
            "确认文件含有每一个字符串。由模型来做时，把阅读记在 `evidence.model_read_on`，不要记在 `evidence.read_on`。"
        ),
        columns=EVIDENCE_COLUMNS,
        rows=evidence_rows(catalog, _stats.single_model_name),
    )


def by_band(entries) -> list[dict]:
    """Most-starred band first, then by title: the order a person with an hour
    would read them in. The band, not the count (readme/rows.py STAR_BANDS),
    so the weekly star refresh moves a row only when it crosses a floor."""
    return sorted(entries, key=lambda e: (-star_band(e.get("stars")), e["title"].lower(), e["slug"]))


def patterns_cell(patterns) -> str:
    return " ".join(cell(p) for p in patterns)


def tool_selection_broad_words(catalog: list[dict]) -> Section:
    marked = by_band(e for e in catalog if _stats.tool_selection_broad_only(e))
    return Section(
        key="tool-selection-broad-words",
        title_en="Tool selection resting on words the keyword rules no longer count",
        title_zh="工具选择只靠关键词规则已不再计入的词",
        about_en=(
            "The row carries `tool-selection`, and the keyword rules suggest it for the row's summary "
            "and title only as they stood until 2026-09-27. They then counted \"control\", \"harness\" "
            "and \"screen\" on their own, and \"robot\", \"autonomous\" and \"drive\" with no word for "
            "deciding or acting beside them; the rules in `scripts/classify.py` no longer do. The bulk "
            "passes took the rules' patterns, so a row here may never have been read against "
            "tool-selection, or a person may have agreed with it without recording so. The rules read "
            "a project's GitHub description at discovery; the summary stands in for it here."
        ),
        about_zh=(
            "该行带有 `tool-selection`，而关键词规则只有按 2026-09-27 之前的写法才会从它的摘要和标题建议这个模式。"
            "当时的规则单凭 \"control\"、\"harness\"、\"screen\" 就算数，\"robot\"、\"autonomous\"、"
            "\"drive\" 旁边没有表示决定或动作的词也算数；`scripts/classify.py` 里现在的规则不再这样。"
            "批量收录时直接采用了规则给出的模式，所以这里的行可能从未有人对照 tool-selection 读过，"
            "也可能有人读过并同意，只是没有记录。规则在发现阶段读的是项目的 GitHub 描述；这里以摘要代替。"
        ),
        leave_en=(
            "To take a row off, read the project against [`tool-selection`](patterns.md#tool-selection). "
            "If nothing in it decides which tool or action comes next, replace `tool-selection` in "
            "`patterns` with the pattern it does show, or with `overview`. Either way, set "
            "`patterns_reviewed` to the date you read it; that alone takes off a row whose "
            "`tool-selection` was right. A model that reads it sets `patterns_model_read_on` instead, "
            "which moves the row to [Read or written by a model](#model-read)."
        ),
        leave_zh=(
            "移出方法：对照 [`tool-selection`](patterns.md#tool-selection) 阅读该项目。"
            "如果其中没有任何东西在决定下一步调用哪个工具或采取哪个动作，就把 `patterns` 里的 `tool-selection` "
            "换成它实际体现的模式，或换成 `overview`。无论哪种情况，都把阅读日期写入 `patterns_reviewed`；"
            "`tool-selection` 本来就对的行，只写这个日期也会移出。由模型阅读时改写 `patterns_model_read_on`，"
            "该行会移到[模型读过或撰写](#model-read)一节。"
        ),
        columns=(
            ("Row", "行"),
            ("Stars", "星标"),
            ("Patterns in the row", "该行的模式"),
            ("Suggested until 2026-09-27", "2026-09-27 之前的建议"),
            ("Suggested now", "现在的建议"),
        ),
        rows=tuple(
            (
                row_link(e),
                star_label(e.get("stars")),
                patterns_cell(e["patterns"]),
                patterns_cell(suggest(e, classify_broad)[1]),
                patterns_cell(suggest(e)[1]),
            )
            for e in marked
        ),
    )


def unsorted_overview(catalog: list[dict]) -> Section:
    marked = by_band(e for e in catalog if _stats.not_indexed_by_pattern(e))

    def suggestion(entry: dict) -> str:
        found = suggest(entry)[1]
        return "—" if found == [_stats.OVERVIEW] else patterns_cell(found)

    return Section(
        key="unsorted-overview",
        title_en="Overview rows with code, not yet indexed by pattern",
        title_zh="带代码、尚未按模式索引的 overview 行",
        about_en=(
            "The row is a project or a plugin with code, its only pattern is `overview`, and it records no "
            "reading against the patterns, neither a person's (`patterns_reviewed`) nor a model's "
            "(`patterns_model_read_on`). `overview` is for a row that surveys the model or the space "
            "([patterns.md](patterns.md#overview)); it is also what the keyword rules suggest when nothing "
            "matches, and the bulk passes took the rules' patterns. The READMEs, the Overview page and the "
            "site list these rows apart, as not yet indexed by pattern. The last column is only a "
            "suggestion: what the keyword rules (`scripts/classify.py`) make of the row's summary and "
            "title, and a dash when none of them matches."
        ),
        about_zh=(
            "该行是带代码的项目或插件，唯一的模式是 `overview`，且没有任何对照决策模式阅读的记录："
            "既没有人的（`patterns_reviewed`），也没有模型的（`patterns_model_read_on`）。"
            "`overview` 本是给介绍模型或整个领域的行用的（[patterns.md](patterns.md#overview)）；"
            "它也是关键词规则什么都没匹配到时给出的建议，而批量收录时直接采用了规则给出的模式。"
            "README、Overview 页面和站点把这些行单独列为“尚未按模式索引”。最后一列只是建议："
            "关键词规则（`scripts/classify.py`）根据该行摘要和标题给出的结果，没有任何规则匹配时显示为破折号。"
        ),
        leave_en=(
            "To take a row off, read the project against [the patterns](patterns.md). Put the patterns it "
            "shows in `patterns`, or keep `overview` if it surveys the space, and set `patterns_reviewed` "
            "to the date you read it. A model that reads it sets `patterns_model_read_on` instead, which "
            "moves the row to [Read or written by a model](#model-read)."
        ),
        leave_zh=(
            "移出方法：对照[决策模式](patterns.md)阅读该项目。把它体现的模式写进 `patterns`；"
            "如果它确实是在介绍整个领域，就保留 `overview`。然后把阅读日期写入 `patterns_reviewed`。"
            "由模型阅读时改写 `patterns_model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。"
        ),
        columns=(
            ("Row", "行"),
            ("Kind", "类型"),
            ("Stars", "星标"),
            ("Keyword rules suggest (a suggestion)", "关键词规则的建议（仅供参考）"),
        ),
        rows=tuple(
            (row_link(e), cell(e["kind"]), star_label(e.get("stars")), suggestion(e)) for e in marked
        ),
    )


def generic_summary(catalog: list[dict]) -> Section:
    marked = by_band(e for e in catalog if _stats.generic_summary(e))
    listed = [cell(word) for word in ("jev", "typesafe", "System One", "choice", "score", "noul", "decision", "confidence")]
    words, words_zh = ", ".join(listed), "、".join(listed)
    return Section(
        key="generic-summary",
        title_en="Rows with code whose summary names nothing about Jev",
        title_zh="带代码、摘要没有提到 Jev 的行",
        about_en=(
            "The row has code, is not TypeSafe AI's own (`official`), has no `notes`, and its English "
            f"summary contains none of {words} (in any case, also inside a longer word). Most are the "
            "project's own GitHub description (`summary_source`), which has no reason to mention Jev, "
            "so a reader of the list cannot tell what the project asks Jev to decide. The words are a "
            "floor, not a test: a summary without them may still say it, and one with them may say "
            "little. The last column links the file the row cites, as the READMEs and the pattern "
            "pages do."
        ),
        about_zh=(
            "该行带代码，不是 TypeSafe AI 自己发布的（`official`），没有 `notes`，而且英文摘要里"
            f"没有 {words_zh} 中的任何一个（不分大小写，出现在更长的词里也算）。其中多数是项目自己在 GitHub 上的描述"
            "（`summary_source`），它没有理由提到 Jev，于是读列表的人看不出这个项目让 Jev 做什么决策。"
            "这些词只是底线，不是检验：没有这些词的摘要也可能说清楚了，有这些词的也可能什么都没说。"
            "最后一列链接到该行引用的文件，与 README 和模式页面一样。"
        ),
        leave_en=(
            "To take a row off, read the cited file and write a summary that says what the project asks "
            "Jev to decide, in words that include one of those above (naming Jev is enough; the rule reads "
            "only the words), with `summary_source` set to `curated` and `summary_zh` to match (see the "
            "`summary` field rules in [CONTRIBUTING](../CONTRIBUTING.md#field-rules)); or keep the "
            "summary and add a `notes` line that says it. A summary a model writes is labelled "
            "`model-written` instead, and the row moves to [Read or written by a model](#model-read)."
        ),
        leave_zh=(
            "移出方法：读引用的文件，写一条说明该项目让 Jev 决定什么的摘要，其中要含有上面列出的某个词（写出 Jev 即可；规则只看这些词），把 `summary_source` 设为 `curated`，"
            "并相应更新 `summary_zh`（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `summary` 的字段规则）；"
            "或者保留摘要，加一行 `notes` 说明这一点。由模型撰写的摘要改标为 `model-written`，"
            "该行会移到[模型读过或撰写](#model-read)一节。"
        ),
        columns=(
            ("Row", "行"),
            ("Kind", "类型"),
            ("Stars", "星标"),
            ("Summary", "摘要"),
            ("Summary source", "摘要来源"),
            ("Cited file", "引用的文件"),
        ),
        rows=tuple(
            (
                row_link(e),
                cell(e["kind"]),
                star_label(e.get("stars")),
                esc(e["summary"]),
                cell(e["summary_source"]) if e.get("summary_source") else "—",
                file_link(e) if e.get("evidence") else "—",
            )
            for e in marked
        ),
    )


def measurement_unread(catalog: list[dict]) -> Section:
    marked = by_band(unread(catalog))
    return Section(
        key="measurement-unread",
        title_en="Benchmark measurements nobody has read against the report",
        title_zh="人和模型都还没有对照报告读过的基准测试测量",
        about_en=(
            "The row's `measurement` has neither `read_on` nor `model_read_on`: a script or a model filled "
            "in its fields from the author's README or results, and nobody has recorded reading them since. The fields index what the "
            "author reports; the direction is the author's own conclusion (author-stated, not reproduced "
            "here). The fields first filled in on 2026-09-28 were read by a model; "
            "[method.md](method.md) says how. [benchmarks.md](benchmarks.md) shows every field."
        ),
        about_zh=(
            "该行的 `measurement` 既没有 `read_on` 也没有 `model_read_on`：字段由脚本或模型根据作者的 README "
            "或结果填写，此后没有人或模型记录过核读。"
            "这些字段索引的是作者报告的内容；结论方向是作者本人的结论（作者自述，未经本仓库复现）。"
            "2026-09-28 首次填写的字段由模型阅读得出，做法见 [method.md](method.md)。"
            "全部字段见 [benchmarks.zh-CN.md](benchmarks.zh-CN.md)。"
        ),
        leave_en=(
            "To take a row off, read the author's report (the row's link, or `measurement.report`) against "
            "every field, correct or remove any the report does not state, and set `measurement.read_on` to "
            "the day you read it (see the `measurement` field rules in "
            "[CONTRIBUTING](../CONTRIBUTING.md#field-rules)). A model that reads it sets "
            "`measurement.model_read_on` instead, which moves the row to [Read or written by a model](#model-read)."
        ),
        leave_zh=(
            "移出方法：对照作者的报告（该行的链接，或 `measurement.report`）逐项核读，改正或删去报告里没有说的字段，"
            "再把 `measurement.read_on` 设为核读当天（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 "
            "`measurement` 的字段规则）。由模型核读时改写 `measurement.model_read_on`，该行会移到"
            "[模型读过或撰写](#model-read)一节。"
        ),
        columns=(
            ("Row", "行"),
            ("Stars", "星标"),
            ("Direction (author-stated, not reproduced here)", "结论方向（作者自述，未经本仓库复现）"),
            ("Report", "报告"),
        ),
        rows=tuple(
            (
                row_link(e),
                star_label(e.get("stars")),
                cell(e["measurement"]["direction"]) if e["measurement"].get("direction") else "—",
                f"[{cell(e['measurement'].get('report') or e['url'])}]({md_url(e['measurement'].get('report') or e['url'])})",
            )
            for e in marked
        ),
    )


def wire_unread(catalog: list[dict]) -> Section:
    marked = by_band(wire.unread(catalog))
    return Section(
        key="wire-unread",
        title_en="Interfaces of alternatives nobody has read in the cited files",
        title_zh="人和模型都还没有在所引文件中读过的替代实现接口",
        about_en=(
            "The row's `wire` record cites a file with neither `read_on` nor `model_read_on`: a script or a model read the "
            "project's code for its route, its yes/no spelling, where its answers come from and whether it "
            "calls Jev to compare, and no person has checked since. Every value is backed by a string in a "
            "cited file, which the weekly `claims` run re-reads; whether the strings mean what the fields say "
            "is the reading. The records first filled in on 2026-09-28 were read by a model; "
            "[method.md](method.md) says how. [compatibility.md](compatibility.md#7-compatible-interfaces-that-are-not-jev) "
            "shows every field."
        ),
        about_zh=(
            "该行的 `wire` 记录所引文件中有的既没有 `read_on` 也没有 `model_read_on`：由脚本或模型阅读项目代码，得出其路由、是/否题型的写法、"
            "答案来自哪里、是否调用 Jev 做对比，此后没有人核对过。每个值都有所引文件中的一段字符串作依据，"
            "每周的 `claims` 任务会重读这些字符串；这些字符串是否真如字段所说，则要靠人读。"
            "2026-09-28 首次填写的记录由模型阅读得出，做法见 [method.md](method.md)。"
            "全部字段见 [compatibility.md](compatibility.md#7-compatible-interfaces-that-are-not-jev)。"
        ),
        leave_en=(
            "To take a row off, read each file in `wire.source` against every field, correct or remove any "
            "field the files do not show, and set `read_on` on each source to the day you read it (see the "
            "`wire` field rules in [CONTRIBUTING](../CONTRIBUTING.md#field-rules)). A model that reads them "
            "sets `model_read_on` instead, which moves the row to [Read or written by a model](#model-read)."
        ),
        leave_zh=(
            "移出方法：对照 `wire.source` 中的每个文件逐项核读，改正或删去文件里看不出的字段，再把每个来源的 "
            "`read_on` 设为核读当天（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `wire` 的字段规则）。"
            "由模型核读时改写 `model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。"
        ),
        columns=(("Row", "行"), ("Stars", "星标"), ("Weights", "权重"), ("Cited files", "引用的文件")),
        rows=tuple(
            (
                row_link(e),
                star_label(e.get("stars")),
                cell(e["wire"]["weights"]) if e["wire"].get("weights") else "—",
                " ".join(cell(item["path"]) for item in wire.sources(e["wire"])),
            )
            for e in marked
        ),
    )


def threshold_cell(item: dict) -> str:
    """One threshold as the row records it: question type, quantity, constant."""
    return cell(f"{item.get('question_type')} {item.get('compares')} {thresholds.number(item.get('value'))}")


def thresholds_unread(catalog: list[dict]) -> Section:
    marked = by_band(thresholds.unread(catalog))
    return Section(
        key="thresholds-unread",
        title_en="Thresholds nobody has read in the cited file",
        title_zh="人和模型都还没有在所引文件中读过的阈值",
        about_en=(
            "The row's `observed_thresholds` has an item with neither `read_on` nor `model_read_on`: a script or a model read the "
            "cited file for the constants it compares a Jev answer with, and no person has checked since. "
            "Each item's `source` is a string in `evidence.matched`, which the weekly `claims` run re-reads, "
            "and its `value` is written in it; which answer the constant is compared with, and what the code "
            "does on each side, is the reading. They are what the project chose, not recommendations. The "
            "thresholds first recorded on 2026-09-28 were read by a model; [method.md](method.md) says how."
        ),
        about_zh=(
            "该行的 `observed_thresholds` 中有条目既没有 `read_on` 也没有 `model_read_on`：由脚本或模型阅读所引文件，找出其中与 Jev "
            "答案比较的常量，此后没有人核对过。每个条目的 `source` 是 `evidence.matched` 中的一段字符串，"
            "每周的 `claims` 任务会重读它，`value` 就写在其中；常量与哪个答案比较、两侧代码各做什么，则要靠人读。"
            "这些是该项目自己的选择，不是推荐值。2026-09-28 首次记录的阈值由模型阅读得出，做法见 "
            "[method.md](method.md)。"
        ),
        leave_en=(
            "To take a row off, read the cited file against every item: correct `question_type`, `compares` "
            "and `decision`, remove any item that is not a decision on a Jev answer, and set each item's "
            "`read_on` to the day you read it (see the `observed_thresholds` field rules in "
            "[CONTRIBUTING](../CONTRIBUTING.md#field-rules)). A model that reads them sets `model_read_on` "
            "instead, which moves the row to [Read or written by a model](#model-read)."
        ),
        leave_zh=(
            "移出方法：对照所引文件逐条核读，改正 `question_type`、`compares` 和 `decision`，删去不是基于 Jev "
            "答案做决定的条目，再把每个条目的 `read_on` 设为核读当天（见 "
            "[CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `observed_thresholds` 的字段规则）。"
            "由模型核读时改写 `model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。"
        ),
        columns=(("Row", "行"), ("Stars", "星标"), ("Thresholds", "阈值"), ("Cited file", "引用的文件")),
        rows=tuple(
            (
                row_link(e),
                star_label(e.get("stars")),
                " ".join(threshold_cell(item) for item in thresholds.recorded(e)),
                file_link(e),
            )
            for e in marked
        ),
    )


def model_work(entry: dict) -> list[tuple[str, str]]:
    """What a model read or wrote for the row that no person has checked since,
    as (what, when) pairs; `when` is "" for a summary, which records no date."""
    query = _stats.load_query()
    found = []
    if entry.get("patterns_model_read_on") and not entry.get("patterns_reviewed"):
        found.append(("patterns", entry["patterns_model_read_on"]))
    if query.read_by(entry.get("evidence")) == query.MODEL:
        found.append(("call site", entry["evidence"]["model_read_on"]))
        # Read in that call site, so the model's reading too (primitives_read_by).
        if query.primitives_read_by(entry) == query.MODEL:
            found.append(("question_types", ""))
    if entry in measurements_model_read([entry]):
        found.append(("measurement", entry["measurement"]["model_read_on"]))
    if entry in wire.model_read([entry]):
        days = sorted({item["model_read_on"] for item in wire.sources(entry["wire"]) if "read_on" not in item})
        found.append(("interface", ", ".join(days)))
    if entry in thresholds.model_read([entry]):
        days = sorted({item["model_read_on"] for item in thresholds.recorded(entry) if "read_on" not in item})
        found.append(("thresholds", ", ".join(days)))
    if entry.get("summary_source") == "model-written":
        found.append(("summary", ""))
    return found


def model_read(catalog: list[dict]) -> Section:
    marked = by_band(e for e in catalog if model_work(e))
    return Section(
        key="model-read",
        title_en="Read or written by a model, not yet checked by a person",
        title_zh="模型读过或撰写、尚无人核对",
        about_en=(
            "Since 2026-10-24 a model's reading is recorded apart from a person's: `patterns_model_read_on`, "
            "and `model_read_on` on the call site (`evidence`), a benchmark's `measurement`, each file of an "
            "alternative's `wire` and each threshold; a summary a model wrote is labelled `model-written`, and "
            "`question_types` on a row whose call site only a model has read is that model's reading too. "
            "Every surface shows these as a model's work, never as a person's. A row here left the lists "
            "above because a model read it, not because a person agreed: a model can misread a file in ways "
            "a person would not, so these rows are for a person to check, all of them or a sample."
        ),
        about_zh=(
            "自 2026-10-24 起，模型的阅读与人的阅读分开记录：`patterns_model_read_on`，以及调用点（`evidence`）、"
            "基准测试的 `measurement`、替代实现 `wire` 的每个文件和每个阈值上的 `model_read_on`；模型撰写的摘要标为 "
            "`model-written`；调用点只有模型读过的行，其 `question_types` 也是模型的阅读。"
            "所有页面都把这些显示为模型的工作，从不当作人的。这里的行离开上面各节，是因为模型读过，"
            "而不是因为有人认可：模型可能以人不会的方式读错文件，所以这些行留给人核对，全部或抽查。"
        ),
        leave_en=(
            "To take a row off, check what the model read or wrote, correct anything it got wrong, and record "
            "your own reading: `patterns_reviewed`, `evidence.read_on` (after checking `question_types` against "
            "the call site), `measurement.read_on`, or `read_on` on each file or threshold; keep or rewrite a "
            "summary and set `summary_source` to `curated`. The "
            "model's date may stay beside yours: a person's reading supersedes it everywhere it is shown."
        ),
        leave_zh=(
            "移出方法：核对模型读过或写下的内容，改正它弄错的地方，再记下你自己的阅读：`patterns_reviewed`、"
            "`evidence.read_on`（先对照调用点核对 `question_types`）、`measurement.read_on`，"
            "或每个文件、每个阈值上的 `read_on`；摘要则保留或改写，"
            "并把 `summary_source` 设为 `curated`。模型的日期可以留在你的旁边：凡是显示日期的地方，人的阅读都优先。"
        ),
        columns=(("Row", "行"), ("Stars", "星标"), ("A model's work, unchecked", "模型的工作（未经核对）")),
        rows=tuple(
            (
                row_link(e),
                star_label(e.get("stars")),
                " · ".join(f"{cell(what)} {when}".rstrip() for what, when in model_work(e)),
            )
            for e in marked
        ),
    )


def place_link(place: str) -> str:
    """Where the README prints a row (readme.sections.front_page), named and
    linked as the English README's heading for it."""
    names = {START_PLACE: EN["start_h"], MEASURED_PLACE: EN["measured_h"]}
    name = names.get(place) or label(PATTERN_LABELS, place, "en")
    return f"[{name}](../README.md#{anchor(name)})"


def gap_cell(field: str, gaps: dict[str, str], entry: dict) -> str:
    """One of _stats.front_page_gaps() as a cell, "—" when the row lacks nothing there."""
    found = gaps.get(field)
    if found is None:
        return "—"
    if found == "generic-summary":
        return f"[{cell(found)}](#generic-summary)"
    if found == "model_read_on":
        return f"[{cell(found)}](#model-read) {entry['evidence']['model_read_on']}"
    if found == "unread":
        return found
    return cell(found)


def front_page(catalog: list[dict]) -> Section:
    places: dict[str, list[str]] = {}
    rows: dict[str, dict] = {}
    for place, position, entry in printed_by_name(catalog):
        places.setdefault(entry["slug"], []).append(f"{place_link(place)} {position}")
        rows.setdefault(entry["slug"], entry)
    marked = [(entry, _stats.front_page_gaps(entry)) for entry in rows.values()]
    marked = [(entry, gaps) for entry, gaps in marked if gaps]
    start = (EN["start_h"], ZH["start_h"])
    measured = (EN["measured_h"], ZH["measured_h"])
    return Section(
        key="front-page",
        title_en="Rows the README shows, still lacking a person's summary, Chinese or reading",
        title_zh="README 展示、仍缺人写摘要、人写中文或人读所引文件的行",
        about_en=(
            f"Most readers see only the README, and of the catalogue only the rows it prints by name: the "
            f"*{start[0]}* list, the first {INLINE_MEASURED} reports under *{measured[0]}* and the first "
            f"{INLINE_PER_PATTERN} rows of each decision pattern, {len(rows)} rows in all. A row is listed here, "
            "in the order the README first prints it, while it lacks any of three things a person gives it: a "
            "summary written for this catalogue, Chinese a person wrote, and a person's reading of the file it "
            "cites. A summary lacks it when `summary_source` says it is the project's own GitHub description "
            "or a model's that no person has checked, or when any other summary names nothing about Jev (the "
            "[`generic-summary`](#generic-summary) rule); the Chinese, while `zh_machine` is set; the cited "
            "file, while `evidence` records no `read_on`. Each is a fact about who wrote or read the text, not "
            "a verdict on it: a project's own description can be clear and a machine translation right. Whether "
            "a row is filed under the right pattern is for the pattern sections below. The README orders each "
            "pattern's rows by star band, so the weekly refresh can move a row on or off this list when it "
            "crosses a band floor."
        ),
        about_zh=(
            f"大多数读者只看 README，而目录里他们看得到的只有 README 点名列出的行：“{start[1]}”列表、"
            f"“{measured[1]}”下的前 {INLINE_MEASURED} 份报告，以及每个决策模式的前 {INLINE_PER_PATTERN} 行，"
            f"共 {len(rows)} 行。这里按 README 首次列出的顺序，列出其中仍缺以下任何一项的行，三项都要由人来补："
            "为本目录撰写的摘要、人写的中文、人对所引文件的阅读。`summary_source` 表明摘要是项目自己的 GitHub 描述，"
            "或是尚无人核对的模型撰写时，摘要算缺；其他摘要没有提到 Jev 的（[`generic-summary`](#generic-summary) "
            "规则），也算缺。设置了 `zh_machine` 的中文算缺；`evidence` 没有 `read_on` 的，所引文件算缺。"
            "每一项说的都是谁写了、谁读了这些文字，不是对文字的评判：项目自己的描述可能很清楚，机翻也可能是对的。"
            "某行是否归在正确的模式下，由下面的模式各节负责。README 按星标档位排列每个模式的行，"
            "所以每周刷新让某行跨过档位下限时，它可能进入或离开这个列表。"
        ),
        leave_en=(
            "To take a row off, give it what it lacks. Write a summary that says what the project asks Jev to "
            "decide and set `summary_source` to `curated` (see the `summary` field rules in "
            "[CONTRIBUTING](../CONTRIBUTING.md#field-rules)); a model's summary takes `curated` once you have "
            "checked or rewritten it. Write the Chinese yourself and delete `zh_machine` "
            "([Claim a translation](../CONTRIBUTING.md#claim-a-translation): a model's draft keeps the flag, "
            "however carefully you corrected it). Read the cited file, check `question_types` against it and set "
            "`evidence.read_on`. A model can draft any of these, recorded as a model's work (`model-written`, "
            "`zh_machine`, `evidence.model_read_on`), and the row stays here until a person has checked it."
        ),
        leave_zh=(
            "移出方法：补上它缺的。写一条说明该项目让 Jev 决定什么的摘要，并把 `summary_source` 设为 `curated`"
            "（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `summary` 的字段规则）；"
            "模型写的摘要，经你核对或改写后再设为 `curated`。中文由你亲自撰写，并删去 `zh_machine`"
            "（见[认领翻译](../CONTRIBUTING.md#claim-a-translation)：模型起草的译文无论你改得多仔细，都保留这个标记）。"
            "读所引文件，对照它核对 `question_types`，再设置 `evidence.read_on`。模型可以起草其中任何一项，"
            "但要记为模型的工作（`model-written`、`zh_machine`、`evidence.model_read_on`），该行会留在这里，直到有人核对。"
        ),
        columns=(
            ("Row", "行"),
            ("Where the README prints it", "README 中的位置"),
            ("Summary", "摘要"),
            ("Chinese", "中文"),
            ("Cited file", "引用的文件"),
        ),
        rows=tuple(
            (
                row_link(entry),
                " · ".join(places[entry["slug"]]),
                *(gap_cell(field, gaps, entry) for field in ("summary", "summary_zh", "evidence")),
            )
            for entry, gaps in marked
        ),
    )


def needs_person(catalog: list[dict], path: pathlib.Path | None = None) -> Section:
    candidates, slugs = held.load(path or HELD)
    by_slug = {e["slug"]: e for e in catalog if isinstance(e, dict) and "slug" in e}
    by_repo = {}
    for entry in catalog:
        repo = repo_of(entry) if isinstance(entry, dict) else None
        if repo:
            by_repo.setdefault(repo.lower(), entry["slug"])
    rows = []
    for slug, reason in slugs.items():
        if slug in by_slug:
            rows.append((row_link(by_slug[slug]), "row · 目录行", esc(reason)))
        else:
            rows.append((cell(slug), "row, not in `catalog.json`: delete the line · 不在目录中，删去此行", esc(reason)))
    for repo, reason in candidates.items():
        where = f"[{repo}](https://github.com/{repo})"
        if repo in by_repo:
            rows.append((where, f"candidate, since catalogued as `{by_repo[repo]}`: delete the line · 已收录，删去此行",
                         esc(reason)))
        else:
            rows.append((where, "candidate · 候选", esc(reason)))
    return Section(
        key="needs-person",
        title_en="Held for a person: read, not settled",
        title_zh="等人看：读过、未定",
        about_en=(
            "Unlike every other section, these are not a rule's matches: someone (often a scheduled AI run) read "
            "a row or a discovery candidate, could not settle it, and wrote it into "
            "[`docs/held.txt`](held.txt) with the reason, rows first, then candidates. A held candidate waits under "
            "its own heading in the discovery issue instead of at the top of those to read. The bots' own lists "
            "are in their issues: links that died (`links`), cited files and strings that moved (`claims`, #28) and "
            "the weekly refresh's changes (`metadata`, #32)."
        ),
        about_zh=(
            "和其他各节不同，这些不是规则的命中：有人（通常是定时运行的 AI）读过某一行或某个发现候选，拿不准，"
            "把它连同原因写进了 [`docs/held.txt`](held.txt)，先列目录行，再列候选。被搁置的候选在发现 issue 里"
            "单列一节，不再排在待读的最前面。机器人自己的清单在各自的 issue 里：失效的链接（`links`）、"
            "移动了的引用文件和字符串（`claims`，#28）、每周刷新的变化（`metadata`，#32）。"
        ),
        leave_en=(
            "To take one off, decide it: change or retire the row, add the candidate's row or decline it in "
            "`docs/declined.txt`, or conclude nothing needs doing. Then delete its line in `docs/held.txt` in the "
            "same pull request."
        ),
        leave_zh=(
            "移出方法：做出决定。修改或退役该行，为候选添加一行或在 `docs/declined.txt` 中拒收它，"
            "或者认定什么都不用做。然后在同一个 pull request 里删去 `docs/held.txt` 中的对应行。"
        ),
        columns=(("Held", "搁置项"), ("What", "类型"), ("Reason given", "原因")),
        rows=tuple(rows),
    )


def experimental(catalog: list[dict]) -> Section:
    marked = sorted((e for e in catalog if e.get("experimental_seen")), key=lambda e: e["slug"])
    return Section(
        key="experimental",
        title_en="Cited file shows an experimental Jev feature",
        title_zh="所引文件出现 Jev 的实验性功能",
        about_en=(
            "The weekly refresh found the request shape of one of Jev's experimental features in the file the "
            "row cites (`experimental_seen`, scripts/verify_claims.py): a Box question (Jev 1.14), or the "
            "images or long-context opt-in header. A text signal about that file, not a reading: it does not "
            "say the code uses the feature. Box is not one of the three primitives the catalogue counts, "
            "filters and picks between, so nothing else shows these rows apart."
        ),
        about_zh=(
            "每周刷新在该行引用的文件里发现了 Jev 某项实验性功能的请求结构（`experimental_seen`，"
            "scripts/verify_claims.py）：Box 问题（Jev 1.14），或图像、长上下文的启用请求头。"
            "这是关于该文件的文本信号，不是阅读结论，不说明代码确实使用了该功能。Box 不在目录统计、"
            "筛选和选择器所覆盖的三个原语之内，因此其他地方都不会单独列出这些行。"
        ),
        leave_en=(
            "Nothing takes a row off but the file: the signal goes when the file no longer shows the shape. "
            "Read it to say in `notes` what the project does with the feature; when Box leaves the "
            "experimental tier, this list is where its rows are."
        ),
        leave_zh=(
            "只有文件本身能让行移出：文件里不再出现该结构时，信号就会消失。读过之后，可以在 `notes` "
            "里写明项目如何使用该功能；Box 结束实验阶段时，它的行就在这张表里。"
        ),
        columns=(("Row", "行"), ("Kind", "类型"), ("Cited file", "引用的文件"), ("Shows", "出现")),
        rows=tuple(
            (row_link(e), cell(e["kind"]), file_link(e), " ".join(cell(x) for x in e["experimental_seen"]))
            for e in marked
        ),
    )


SECTIONS = (
    needs_person, front_page, examples_dir, single_model_name, tool_selection_broad_words, unsorted_overview, generic_summary,
    measurement_unread, wire_unread, thresholds_unread, model_read, experimental,
)

HEADER = (
    "<!-- Written by scripts/build_review_queue.py from catalog.json and docs/held.txt. "
    "Edit those, not this file. -->"
)
PROVENANCE = (
    "<sub>The Chinese on this page is model-written and has not been reviewed by a person. · "
    "本页中文由模型撰写（机翻），未经人工审校。</sub>"
)
INTRO_EN = (
    "Rows a script has singled out for a person to read. Each entry is a machine signal (a path, "
    "a string or a combination of fields matched a rule), not a finding about the row, and nothing on this page is written "
    "into `catalog.json`. Whoever reads a row records the decision in it, as each section says, and "
    "the row leaves this page when it is next regenerated. [status.md](status.md) publishes the "
    "counts."
)
INTRO_ZH = (
    "脚本挑出、需要人来读的行。每一项都是机器信号（某个路径、字符串或字段组合命中了规则），"
    "不是对该行的结论，本页内容也不会写回 `catalog.json`。读过某一行的人按各节所说把判断记进该行，"
    "下次重新生成时它就会离开本页。数量见 [status.md](status.md)。"
)


def table(columns: tuple[tuple[str, str], ...], rows) -> list[str]:
    head = " | ".join(f"{en} · {zh}" for en, zh in columns)
    return [f"| {head} |", "|" + "|".join(" --- " for _ in columns) + "|"] + [
        "| " + " | ".join(cells) + " |" for cells in rows
    ]


def render(catalog: list[dict]) -> str:
    sections = [build(catalog) for build in SECTIONS]
    out = [HEADER, "", "# Review queue · 复核队列", "", PROVENANCE, "", INTRO_EN, "", INTRO_ZH, ""]
    out += table(
        (("Signal", "信号"), ("Rows", "行数")),
        [(f"[{s.title_en} · {s.title_zh}](#{s.key})", str(len(s.rows))) for s in sections],
    )
    for s in sections:
        out += ["", f'<a id="{s.key}"></a>', "", f"## {s.title_en} · {s.title_zh}", ""]
        out += [s.about_en, "", s.about_zh, "", s.leave_en, "", s.leave_zh, ""]
        out += table(s.columns, s.rows) if s.rows else ["Nothing is on this list. · 此列表为空。"]
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="exit 1 instead of writing a stale page")
    args = parser.parse_args(argv)

    catalog = json.loads((ROOT / "catalog.json").read_text())
    text = render(catalog)
    counts = ", ".join(f"{build.__name__}: {len(build(catalog).rows)}" for build in SECTIONS)
    rel = OUT.relative_to(ROOT)
    current = OUT.read_text() if OUT.exists() else None
    if text == current:
        print(f"{rel} is current ({counts})")
        return 0
    if args.check:
        print(f"error: {rel} is stale; run python3 scripts/build_review_queue.py ({counts})", file=sys.stderr)
        return 1
    OUT.write_text(text)
    print(f"wrote {rel} ({counts})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
