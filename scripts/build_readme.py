#!/usr/bin/env python3
"""Generate README.md and README.zh-CN.md from catalog.json.

catalog.json is the only place a fact is edited. Both READMEs are build
artifacts, and CI fails if they drift from the catalog, so there is no way to
hand-patch one language and leave the other stale.

Layout logic lives in render() exactly once. The two languages differ only by
the string pack passed in, which is what keeps them structurally identical
instead of slowly diverging.

Readability rules this file enforces, learned the hard way:

* Long `notes` prose only appears in the curated sections, where there are few
  rows and the note *is* the point. In the big pattern tables it would make
  every row several lines tall and destroy scanning, so those carry short flag
  pills instead and the full note lives in catalog.json and on the site.
* One index, not two. The coverage histogram doubles as the table of contents,
  so there is no separate link list repeating the same eighteen counts.
* Anything that is really a table is rendered as a table, not as prose or as a
  comma-separated wall of links.

Run: python3 scripts/build_readme.py
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
PATTERNS_FILE = ROOT / "patterns.json"
RETIRED = ROOT / "retired.json"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _stats  # noqa: E402
from _github import SELF as REPO  # noqa: E402

REPO_URL = f"https://github.com/{REPO}"
RAW = f"https://raw.githubusercontent.com/{REPO}/main"
SITE = "https://kydlikebtc.github.io/awesome-jev/"


# The taxonomy lives in patterns.json so build_readme, build_assets and the MCP
# server all read one copy. Three embedded copies was three chances to drift.
_PATTERNS = json.loads(PATTERNS_FILE.read_text())["patterns"]
PATTERN_ORDER = [p["key"] for p in _PATTERNS]
PATTERN_LABELS = {
    p["key"]: (p["en"], p["zh"], p["blurb_en"], p["blurb_zh"]) for p in _PATTERNS
}

# Kind and flag labels live in taxonomy.json, which the site also reads at
# runtime. Two embedded copies had already drifted on three flag labels.
_TAXONOMY = json.loads((ROOT / "taxonomy.json").read_text())
KIND_ORDER = [k["key"] for k in _TAXONOMY["kinds"]]
FLAG_ORDER = [f["key"] for f in _TAXONOMY["flags"]]
KIND_LABELS = {
    k["key"]: (k["en"], k["zh"], k["blurb_en"], k["blurb_zh"]) for k in _TAXONOMY["kinds"]
}
FLAG_LABELS = {
    f["key"]: (f["en"], f["zh"], f["blurb_en"], f["blurb_zh"]) for f in _TAXONOMY["flags"]
}

# The handful of rows a newcomer should open, in reading order. Curated by hand
# because "most starred" is not the same as "read this first" — the limitations
# page has no stars at all and is the most useful page in the docs.
START_HERE = [
    "typesafe-quickstart",
    "typesafe-jaggedness",
    "example-three-primitives",
    "fast-jev-compaction",
    "ai-cookbook-jev-track",
    "hermes-agent-jev-evaluation",
]

# The README shows this many rows per pattern and links to a page with the rest.
#
# It used to show every row, collapsing long sections behind <details>. That
# kept the scroll short but not the file: at 805 entries the README was 323 KB,
# 92% of it this one section, with every multi-pattern row printed once per
# pattern. Collapsing hides rows from the eye, not from the download, the
# renderer or anyone reading the raw file.
#
# Ten is enough to show what a pattern looks like in practice, in the same
# order the site and the MCP server use — official first, then code, then
# stars — so all three surfaces agree on what comes first. Each pattern also
# gets its own generated page, which is a URL worth having for its own sake:
# "every safety-gating example" can now be linked to.
INLINE_PER_PATTERN = 10
PAGES_DIR = ROOT / "docs" / "by-pattern"

# The three primitives, rendered as a table rather than described in a
# paragraph. Every fact here is from the official API reference.
PRIMITIVES = [
    {
        "glyph": "◆",
        "name": "choice",
        "returns_en": "one option, plus `probabilities` and `confidence`",
        "returns_zh": "一个选项，附带 `probabilities` 和 `confidence`",
        "limit_en": "up to **255** options",
        "limit_zh": "最多 **255** 个选项",
        "for_en": "pick a tool, a route, a label",
        "for_zh": "选工具、选分支、选标签",
    },
    {
        "glyph": "▮",
        "name": "score",
        "returns_en": "a number, plus `legend`, `probabilities` and `confidence`",
        "returns_zh": "一个数值，附带 `legend`、`probabilities` 和 `confidence`",
        "limit_en": "**2–10** ordered levels, 0-indexed",
        "limit_zh": "**2–10** 个有序级别，从 0 开始",
        "for_en": "rank quality, risk, urgency",
        "for_zh": "给质量、风险、紧急度排序",
    },
    {
        "glyph": "◐",
        "name": "noul",
        "returns_en": "a 0–1 probability in `.noul` — **and no `confidence`**",
        "returns_zh": "`.noul` 里一个 0–1 概率 —— **且不带 `confidence`**",
        "limit_en": 'not called "binary" or "boolean"',
        "limit_zh": "它不叫 binary，也不叫 boolean",
        "for_en": "gate an action, keep or drop an item",
        "for_zh": "拦一个动作、留或弃一个条目",
    },
]

EN = {
    "lang_code": "en",
    "other_readme": "README.zh-CN.md",
    "other_name": "中文",
    "site_label": "Searchable site",
    "collection_first": "First call",
    "collection_build": "Adapt a project",
    "collection_measured": "Independent reports",
    "tagline": (
        "Public resources for Jev — TypeSafe AI's System One decision model — "
        "indexed by the decision it makes, not by the blog that mentioned it."
    ),
    "generated": "This file is generated from catalog.json. Edit the catalog, then run `python3 scripts/build_readme.py`.",
    "badge_note": "Counts describe saved link and evidence records, not current CI passes or runtime tests.",
    "shot_alt": "The awesome-jev site: a coverage histogram down the left acting as the pattern filter, dense entry cards on the right",
    "shot_cap": 'Filter by clicking a bar. Two more views: <a href="https://kydlikebtc.github.io/awesome-jev/?view=prims">primitives</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat">compatibility</a>. Every filter and entry is a shareable URL.',
    # ---- what this is ----
    "about_h": "What this is",
    "about_rows": [
        (
            "**Jev** is a decision model from TypeSafe AI. It does not write text — you hand it "
            "state plus typed questions and it returns typed answers with calibrated confidence, "
            "fast and cheap enough to sit in an agent's inner loop.",
        ),
        (
            "**This repo** indexes public examples of using it, organised by the *decision* being "
            "made. The resource you read this week is disposable; the decision pattern is not.",
        ),
        (
            "**How to assess it:** every row names its source. Call-site citations, primitive "
            "claims and caveats are recorded where available, so you can inspect what was read "
            "and what remains untested.",
        ),
    ],
    "about_not": (
        "Not the product, not an SDK, not affiliated with TypeSafe AI, and not a recommendation. "
        "Inclusion is a source record, not a runtime or performance endorsement. "
        "See [what is verified](#what-is-verified-and-what-is-not)."
    ),
    # ---- primitives ----
    "prims_h": "What Jev returns",
    "prims_intro": (
        "Three primitives. Every pattern below is built out of them, and the asymmetry in the last "
        "row is the single most common source of bugs."
    ),
    "th_prim": "Primitive",
    "th_returns": "Returns",
    "th_limit": "Limits",
    "th_for": "Used for",
    "prims_after": (
        "Input is **text only** — string, JSON object, or array of text. Context is **64k** tokens "
        "per request, **32k** for the state plus the longest question. Output tokens are free. "
        "There are no published weights, so it cannot be run locally. "
        "Full cross-platform differences: [`docs/compatibility.md`](docs/compatibility.md)."
    ),
    # ---- sections ----
    "l_patterns": "Patterns",
    "l_compat": "Compatibility",
    "l_vetting": "Vetting",
    "cov_alt": "Horizontal bar chart of how many catalog examples exist for each of the eighteen decision patterns",
    "prim_alt": "Three panels describing the choice, score and noul primitives and what each returns",
    "start_h": "Start here",
    "start_intro": 'Six things in reading order. Hand-picked, because "most starred" is not the same as "read this first".',
    "th_why_read": "Why this one",
    "coverage_h": "Coverage",
    "coverage_intro": (
        "Every decision pattern, sized by how many entries this catalogue contains. This doubles as the index — "
        "the names link to the sections below. A zero is a research gap, not a rendering bug."
    ),
    "measured_h": "Measured, not claimed",
    "measured_intro": (
        "Independent measurement reports in the catalogue, including **negative results** that "
        "help explain where an approach fails. These are the original authors' measurements; "
        "this repository has not independently reproduced them. Check each report's dataset, "
        "method and model version before comparing results."
    ),
    "patterns_h": "By decision pattern",
    "patterns_intro": (
        "The primary index. Each heading is a decision an agent has to make; the rows are examples "
        "of making it. Caveats appear as short tags — the full note for each row is in "
        "[`catalog.json`](catalog.json) and on [the site]({site})."
    ),
    "kinds_h": "By resource kind",
    "kinds_intro": "The same rows grouped by what you will find when you open the link.",
    "th_find": "What you will find",
    "repo_h": "Also in this repo",
    "repo_intro": "The parts that are not the catalog.",
    "th_file": "File",
    "th_what": "What it is",
    "verified_h": "What is verified, and what is not",
    "stat_rechecked": "evidence recorded",
    "verified_recheck": (
        "**Call-site text checks** — {n} rows record a file and matching strings in `evidence`. "
        "The weekly [claims job](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) "
        "checks that those strings remain on the default branch and reports missing text or files. "
        "This count measures recorded evidence, **not latest CI passes**. A text match does not "
        "prove that a call executes, the API is compatible, or the result is correct."
    ),
    "verified_yes": (
        "**Link checks** — {link_ok} rows carry an HTTP 2xx response and a `checked` date; "
        "{link_unstamped} carry no dated success record. Dates vary by row and a past success "
        "does not guarantee availability today. Stars and licences are repository metadata snapshots."
    ),
    "verified_read": (
        "**Source and code review** — `evidence.path` cites the file read, `evidence.read_on` "
        "records the reported review date, and `evidence_none` explains missing file evidence. "
        "Reading a call site is separate from running it. Summaries include source descriptions "
        "and machine translations; see the [method and its limits](docs/method.md)."
    ),
    "verified_no": (
        "**Runtime and performance not independently tested here** — treat every catalogue entry "
        "as untested by this repository, including entries without `code-untested`. Linked "
        "benchmarks describe their authors' measurements; this catalogue has not reproduced them. "
        "Repository build checks and package smoke tests do not exercise those integrations or "
        "the live Jev API, and inclusion is not a security review."
    ),
    "verified_flags_h": "What the tags mean",
    "th_tag": "Tag",
    "th_means": "Means",
    "data_h": "Machine-readable data",
    "data_intro": "One entry per example, validated against a JSON Schema on every push.",
    "contrib_h": "Contributing and licence",
    "contrib_body": (
        "Corrections take priority over additions — a wrong row costs more than a missing one. "
        "See [CONTRIBUTING.md](CONTRIBUTING.md); the bar is *could a reader act on this row without "
        "opening the link?*"
    ),
    "license_body": (
        "Code in `scripts/`, `site/` and `examples/` is [MIT](LICENSE-MIT). Catalog metadata is "
        "[CC0-1.0](LICENSE-CC0), with a per-row `license` field. Linked works keep their own "
        "licences — `repo_license` records what each declares."
    ),
    # ---- table headers ----
    "th_example": "Example",
    "th_shows": "What it shows",
    "th_kind": "Kind",
    "th_code": "Code",
    "th_caveats": "Caveats",
    "th_pattern": "Pattern",
    "th_count": "Examples",
    "no_entries": "_No entries yet._",
    "retired_h": "Retired links",
    "retired_intro": "Links that stopped resolving, kept so a dead reference stays searchable instead of vanishing.",
    "th_why": "Why",
    "pattern_more": "**{shown} of {n}** shown · [all {n} on one page →]({page}) · [filter on the site]({site})",
    "pattern_all": "All {n} shown · [on its own page]({page}) · [filter on the site]({site})",
    "page_intro": (
        "Every catalogued example of this decision — {n} of them, official first, then rows "
        "with code, then by stars. The same rows, with caveats, are in [the index]({readme}); "
        "[the site]({site}) can filter them further by language, primitive and kind."
    ),
    "page_other_lang": "[中文]({other})",
    "page_footer": (
        "<sub>Generated from `catalog.json` by `scripts/build_readme.py`. "
        "Edit the catalogue, not this file — CI fails if the two disagree.</sub>"
    ),
    "gap": "no examples yet",
    # ---- stats ----
    "stat_entries": "entries",
    "stat_with_code": "with code",
    "stat_official": "official",
    "stat_verified": "dated 2xx",
    "stat_patterns": "patterns",
    "stat_retired": "retired",
}

ZH = {
    "lang_code": "zh",
    "other_readme": "README.md",
    "other_name": "English",
    "site_label": "可搜索站点",
    "collection_first": "第一次调用",
    "collection_build": "改造现有项目",
    "collection_measured": "独立测量报告",
    "tagline": (
        "Jev（TypeSafe AI 的 System One 决策模型）公开资源索引 —— "
        "按它做的**决策**归类，而不是按提到它的博客归类。"
    ),
    "generated": "本文件由 catalog.json 生成。请修改目录数据后运行 `python3 scripts/build_readme.py`。",
    "badge_note": "数字统计已保存的链接与证据记录，不代表当前 CI 通过数或运行测试结果。",
    "shot_alt": "awesome-jev 站点：左侧覆盖度直方图兼作模式筛选器，右侧是密集的条目卡片",
    "shot_cap": '点击条形即可筛选。另有两个视图：<a href="https://kydlikebtc.github.io/awesome-jev/?view=prims&lang=zh">三个原语</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat&lang=zh">兼容性矩阵</a>。每个筛选条件和每个条目都是可分享的 URL。',
    "about_h": "这是什么",
    "about_rows": [
        (
            "**Jev** 是 TypeSafe AI 的决策模型。它不生成文本 —— 你给它状态和类型化问题，"
            "它返回带校准置信度的类型化答案，快且便宜到可以放进智能体的内层循环。",
        ),
        (
            "**本仓库**收集它的公开使用例子，按所做的**决策**组织。"
            "你这周读的那篇资料是一次性的，决策模式不是。",
        ),
        (
            "**如何判断可信度：**每一行都写明来源；有依据时记录调用点、原语声明和注意事项，"
            "方便你查看读过什么，以及哪些部分仍未实测。",
        ),
    ],
    "about_not": (
        "不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。"
        "收录是一份来源记录，不代表运行验证或性能背书。"
        "详见[哪些经过核实](#哪些经过核实哪些没有)。"
    ),
    "prims_h": "Jev 返回什么",
    "prims_intro": "三个原语。下面所有模式都由它们构成，而最后一行那个不对称是最常见的 bug 来源。",
    "th_prim": "原语",
    "th_returns": "返回",
    "th_limit": "限制",
    "th_for": "用来",
    "prims_after": (
        "输入**仅支持文本** —— 字符串、JSON 对象、或文本数组。上下文每次请求 **64k** token，"
        "其中 state 加最长的那个问题占 **32k**。输出 token 免费。"
        "权重未公开，因此无法本地运行。"
        "跨平台差异全表见 [`docs/compatibility.md`](docs/compatibility.md)。"
    ),
    "l_patterns": "决策模式",
    "l_compat": "兼容性",
    "l_vetting": "核查指南",
    "cov_alt": "十八个决策模式各有多少个目录条目的横向条形图",
    "prim_alt": "三个面板，分别说明 choice、score、noul 三个原语各自返回什么",
    "start_h": "从这里开始",
    "start_intro": "六条，按阅读顺序。手工挑选 —— 因为「star 最多」和「该先读哪个」不是一回事。",
    "th_why_read": "为什么是它",
    "coverage_h": "覆盖度",
    "coverage_intro": (
        "全部决策模式，按本目录的收录数量排列长度。这张表同时就是索引 —— 名称链接到下面对应章节。"
        "数字为 0 的是待补的研究缺口，不是渲染 bug。"
    ),
    "measured_h": "实测，而非宣称",
    "measured_intro": (
        "本目录收录的独立测量报告，包括有助于理解适用边界的**负面结果**。这些是原作者的测量，"
        "本仓库没有独立复现。比较结果前，请分别查看数据集、测试方法和模型版本。"
    ),
    "patterns_h": "按决策模式",
    "patterns_intro": (
        "主索引。每个标题是智能体必须做的一个决策；下面的行是做这个决策的例子。"
        "警示以短标记呈现 —— 每行的完整备注在 [`catalog.json`](catalog.json) 和[站点]({site})里。"
    ),
    "kinds_h": "按资源形态",
    "kinds_intro": "同样这些行，按你点开链接后会看到什么来分组。",
    "th_find": "点开会看到",
    "repo_h": "本仓库还有什么",
    "repo_intro": "除目录数据之外的部分。",
    "th_file": "文件",
    "th_what": "是什么",
    "verified_h": "哪些经过核实，哪些没有",
    "stat_rechecked": "已记录证据",
    "verified_recheck": (
        "**调用点文本复查** —— 有 {n} 行通过 `evidence` 记录了文件和匹配字符串。"
        "每周 [claims 任务](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) "
        "检查这些字符串是否仍在默认分支，发现文本或文件缺失时报告。"
        "这个数字是已记录的证据数量，**不是最新 CI 通过数**。文本匹配不能证明调用实际执行、"
        "API 兼容或结果正确。"
    ),
    "verified_yes": (
        "**链接检查** —— 有 {link_ok} 行记录了 HTTP 2xx 响应和 `checked` 日期，"
        "另有 {link_unstamped} 行没有带日期的成功记录。检查日期因条目而异，过去成功不保证今天仍可访问。"
        "star 数和许可证也是仓库元数据的快照。"
    ),
    "verified_read": (
        "**来源与代码阅读** —— `evidence.path` 指向所读文件，`evidence.read_on` 记录声明的阅读日期，"
        "`evidence_none` 解释缺少文件证据的原因。阅读调用点与运行代码是两件事。"
        "摘要包含源项目描述与机翻，详见[方法与局限](docs/method.md)。"
    ),
    "verified_no": (
        "**本仓库未独立验证运行与性能** —— 所有目录条目默认都未经本仓库实测，没有 "
        "`code-untested` 标签也不代表已测试。被收录的基准是原作者的测量，本目录没有独立复现。"
        "仓库构建检查与安装包冒烟测试不运行这些集成，也不调用 Jev 在线 API；收录亦不代表安全审计。"
    ),
    "verified_flags_h": "这些标记是什么意思",
    "th_tag": "标记",
    "th_means": "含义",
    "data_h": "机器可读数据",
    "data_intro": "每个例子一条记录，每次推送都按 JSON Schema 校验。",
    "contrib_h": "参与贡献与许可",
    "contrib_body": (
        "纠错优先于新增 —— 一个错的条目比一个缺失的条目代价更大。"
        "详见 [CONTRIBUTING.md](CONTRIBUTING.md)；收录标准是：*读者不点开链接，能否据此行动？*"
    ),
    "license_body": (
        "`scripts/`、`site/`、`examples/` 中的代码采用 [MIT](LICENSE-MIT)。"
        "目录元数据采用 [CC0-1.0](LICENSE-CC0)，并带逐行 `license` 字段。"
        "被链接的作品各自保留原许可 —— `repo_license` 记录了各自声明的内容。"
    ),
    "th_example": "例子",
    "th_shows": "展示了什么",
    "th_kind": "形态",
    "th_code": "代码",
    "th_caveats": "警示",
    "th_pattern": "模式",
    "th_count": "例子数",
    "no_entries": "_暂无条目。_",
    "retired_h": "已退休的链接",
    "retired_intro": "已无法访问的链接。保留下来，让失效的引用仍可被搜索到，而不是凭空消失。",
    "th_why": "原因",
    "pattern_more": "已显示 **{shown} / {n}** 条 · [在单独页面查看全部 {n} 条 →]({page}) · [在站点上筛选]({site})",
    "pattern_all": "已显示全部 {n} 条 · [单独页面]({page}) · [在站点上筛选]({site})",
    "page_intro": (
        "这个决策的全部已收录例子 —— 共 {n} 条，官方优先，其次是含代码的，再按 star 排序。"
        "同样这些行及其警示也在[索引]({readme})里；[站点]({site})还能按语言、原语和形态进一步筛选。"
    ),
    "page_other_lang": "[English]({other})",
    "page_footer": (
        "<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。"
        "请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>"
    ),
    "gap": "暂无例子",
    "stat_entries": "条目",
    "stat_with_code": "含代码",
    "stat_official": "官方",
    "stat_verified": "带日期的2xx",
    "stat_patterns": "覆盖模式",
    "stat_retired": "已退休",
}


LANG_LABELS = {
    "python": "Py",
    "typescript": "TS",
    "javascript": "JS",
    "go": "Go",
    "rust": "Rs",
    "shell": "sh",
    "java": "Java",
    "ruby": "Rb",
    "php": "PHP",
    "csharp": "C#",
    "elixir": "Ex",
    "lua": "Lua",
    "swift": "Swift",
    "kotlin": "Kt",
    "haskell": "Hs",
    "c": "C",
    "cpp": "C++",
}

# The non-catalog parts of the repo, so navigation is a table rather than a
# scattering of inline links the reader has to hunt for.
REPO_FILES = [
    (
        "docs/patterns.md",
        "Every pattern defined, each with an explicit *when NOT to use this*.",
        "逐个定义每个模式，并明确写出**什么时候不该用它**。",
    ),
    (
        "docs/compatibility.md",
        "Model string, field names, request shape, endpoint and env var differ per platform. This is that table.",
        "模型串、字段名、请求结构、端点、环境变量 —— 每个平台都不一样。这就是那张对照表。",
    ),
    (
        "docs/vetting.md",
        "What to check before trusting a row, and the one mistake most people make.",
        "信任一个条目之前该检查什么，以及大多数人会犯的那一个错。",
    ),
    (
        "docs/status.md",
        "What week one of this ecosystem actually looked like, gaps included.",
        "这个生态第一周的真实样貌，包括缺口。",
    ),
    (
        "docs/method.md",
        "How the catalog was built, what was excluded, and where it is weakest.",
        "目录是如何建起来的、排除了什么、以及它最弱的地方在哪。",
    ),
    (
        "docs/sources.md",
        "Where every row came from, and the licence position.",
        "每一行的来源，以及许可状况。",
    ),
    (
        "examples/",
        "Four runnable examples. One deliberately leaves the threshold policy to you.",
        "四个可运行样例。其中一个刻意把阈值策略留给你写。",
    ),
    (
        "schema/entry.schema.json",
        "What a catalog entry may contain.",
        "一条目录记录允许包含什么。",
    ),
    (
        ".claude-plugin/",
        "Install the skill and the MCP server together in Claude Code: `/plugin marketplace add kydlikebtc/awesome-jev`, then `/plugin install awesome-jev@awesome-jev`.",
        "在 Claude Code 里一次装好技能和 MCP server：先 `/plugin marketplace add kydlikebtc/awesome-jev`，再 `/plugin install awesome-jev@awesome-jev`。",
    ),
    (
        "src/awesome_jev_mcp/",
        "An MCP server, so an agent can query the catalogue instead of reading it. Caveats travel with every result, and so does how current the data is.",
        "一个 MCP server —— 让智能体可以查询目录而不是阅读它。每条结果都带着它的警示，也带着数据有多新。",
    ),
    (
        "skills/awesome-jev/",
        "An agent skill: the facts that generated Jev code most often gets wrong, and the design rules worth following.",
        "一份 agent 技能：生成的 Jev 代码最常搞错的那些事实，以及值得遵循的设计规则。",
    ),
    (
        "scripts/verify_claims.py",
        "Re-reads every cited call site weekly, so a primitive claim is checkable rather than asserted.",
        "每周重读每一处被引用的调用点 —— 让原语声明可核实，而不只是被断言。",
    ),
    (
        "scripts/refresh_metadata.py",
        "Re-reads stars, licences and archive status from the GitHub API and opens a PR.",
        "从 GitHub API 重新读取 star、许可证与归档状态，并开 PR。",
    ),
]


def esc(text: str) -> str:
    """Escape what would break a markdown table cell."""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def bar(count: int, peak: int, width: int = 16) -> str:
    """A proportional bar from block characters.

    The coverage index is the site's histogram rendered in markdown, so the two
    surfaces tell the same story. Eighths give sub-character resolution, which
    matters when the long tail is 1 or 2 rows against a peak of 53.
    """
    if count <= 0:
        return ""
    units = count / peak * width
    full = int(units)
    eighths = " ▏▎▍▌▋▊▉"  # index 0..7
    step = round((units - full) * 8)
    # A remainder just under 1 rounds to 8, which is past the end of the ramp.
    # That is a whole block, so carry it rather than indexing off the string —
    # this only fires at particular count/peak ratios, so it sat latent until
    # the catalog grew past 400 rows.
    if step >= 8:
        full += 1
        step = 0
    return ("█" * full + (eighths[step] if step else "")) or "▏"


def anchor(text: str) -> str:
    """GitHub's heading-to-anchor rule, enough of it for our headings."""
    slug = text.lower()
    slug = "".join(ch for ch in slug if ch.isalnum() or ch in " -_\u4e00-\u9fff")
    return slug.strip().replace(" ", "-")


def label(mapping: dict, key: str, lang: str, *, field: int = 0) -> str:
    entry = mapping.get(key)
    if entry is None:
        raise KeyError(
            f"no display label for {key!r}. Add it to build_readme.py when you add a schema enum value."
        )
    index = field + (1 if lang == "zh" else 0)
    if index >= len(entry):
        raise KeyError(f"label {key!r} has no field {field} for language {lang!r}")
    return entry[index]


def summary_of(entry: dict, lang: str) -> str:
    text = entry["summary_zh"] if lang == "zh" else entry["summary"]
    if lang == "zh" and entry.get("zh_machine"):
        text += " <sub>(机翻)</sub>"
    return esc(text)


def flags_of(entry: dict, lang: str) -> str:
    tags = [
        f"`{label(FLAG_LABELS, flag, lang)}`"
        for flag in FLAG_ORDER
        if flag in entry.get("flags", [])
    ]
    return " ".join(tags) if tags else "—"


def sort_key(entry: dict) -> tuple:
    """Official first, then rows with code, then stars, then title."""
    return (
        not entry.get("official", False),
        not entry.get("has_code", False),
        -(entry.get("stars") or 0),
        entry["title"].lower(),
    )


def entry_list(entries: list[dict], strings: dict, *, notes: bool = False) -> list[str]:
    """Render rows as a list rather than a table.

    Tables lose here. GitHub sizes columns by content, so with 148 rows the
    title column gets squeezed until names wrap onto three lines while the
    summary column hogs the width — measured at a 61px median row height and a
    46px title column. A list has no columns to fight over: one line of title
    and summary, one dim line of signals, and long titles simply wrap normally.

    `notes=True` adds the full note as a third line, for the curated sections
    where there are a handful of rows and the note is why the row is there.
    """
    lang = strings["lang_code"]
    if not entries:
        return [strings["no_entries"], ""]

    lines = []
    for entry in sorted(entries, key=sort_key):
        head = f"- **[{esc(entry['title'])}]({entry['url']})**"
        if entry.get("official"):
            head += " ⭐"
        lines.append(f"{head} — {summary_of(entry, lang)}")

        # Signals go on a dim second line: kind, popularity, author, language,
        # primitives, then caveats last so they read as the final word.
        bits = [f"`{label(KIND_LABELS, entry['kind'], lang)}`"]
        if entry.get("stars") is not None:
            bits.append(f"★{entry['stars']:,}")
        if entry.get("author"):
            bits.append(esc(entry["author"]["name"]))
        for item in entry.get("languages", []):
            bits.append(f"`{LANG_LABELS.get(item, item)}`")
        for item in entry.get("question_types", []):
            bits.append(f"`{item}`")
        flags = [
            f"`{label(FLAG_LABELS, flag, lang)}`"
            for flag in FLAG_ORDER
            if flag in entry.get("flags", [])
        ]
        if flags:
            bits.append("⚠ " + " ".join(flags))
        lines.append(f"  <sub>{' · '.join(bits)}</sub>")

        if notes:
            note = entry.get("notes_zh" if lang == "zh" else "notes")
            if note:
                lines.append(f"  <sub>{esc(note)}</sub>")
        lines.append("")
    return lines


def group_by_pattern(catalog: list[dict]) -> dict[str, list[dict]]:
    """Rows per pattern, each list already in display order."""
    by_pattern: dict[str, list[dict]] = {key: [] for key in PATTERN_ORDER}
    for entry in catalog:
        for pattern in entry["patterns"]:
            by_pattern[pattern].append(entry)
    return {key: sorted(rows, key=sort_key) for key, rows in by_pattern.items()}


def page_name(key: str, lang: str) -> str:
    """File name of a pattern's page, mirroring README.md / README.zh-CN.md."""
    return f"{key}.zh-CN.md" if lang == "zh" else f"{key}.md"


def site_link(key: str, lang: str) -> str:
    # The site reads ?p= for the pattern filter and ?lang= for the language, so a
    # reader who came from the Chinese README lands on the Chinese site.
    return f"{SITE}?p={key}&lang={lang}"


def render_page(key: str, rows: list[dict], strings: dict) -> str:
    """One pattern's complete list, as its own linkable page."""
    lang = strings["lang_code"]
    name = label(PATTERN_LABELS, key, lang)
    readme = "README.zh-CN.md" if lang == "zh" else "README.md"
    other = page_name(key, "en" if lang == "zh" else "zh")

    out = [
        f"# {name}",
        "",
        f"<sub>[awesome-jev](../../{readme}) · "
        f"{strings['page_other_lang'].format(other=other)}</sub>",
        "",
        f"_{label(PATTERN_LABELS, key, lang, field=2)}_",
        "",
        strings["page_intro"].format(
            n=len(rows),
            readme=f"../../{readme}#{anchor(name)}",
            site=site_link(key, lang),
        ),
        "",
    ]
    out.extend(entry_list(rows, strings))
    out += ["---", "", strings["page_footer"], ""]
    return "\n".join(out)


def coverage_note(stats: dict, lang: str) -> str:
    """Describe current catalogue coverage without inferring ecosystem absence."""
    missing = [key for key, count in stats["by_pattern"].items() if count == 0]
    total = len(stats["by_pattern"])
    if lang == "zh":
        if missing:
            statement = (
                f"本目录有 {len(missing)} 个模式尚未收录条目："
                + "、".join(f"`{key}`" for key in missing)
                + "。未收录不代表其他地方没有公开案例。"
            )
        elif total:
            statement = f"全部 {total} 个模式均已收录条目。覆盖不代表已运行验证或各模式成熟度相同。"
        else:
            statement = "尚未配置决策模式，因此暂不报告覆盖率。"
        return statement + " 详见 [`docs/status.md`](docs/status.md)。"
    if missing:
        statement = (
            f"{len(missing)} patterns have no entries in this catalogue: "
            + ", ".join(f"`{key}`" for key in missing)
            + ". Absence here does not establish absence elsewhere."
        )
    elif total:
        statement = f"All {total} patterns have at least one catalogue entry. Coverage does not imply runtime testing or equal maturity."
    else:
        statement = "No decision patterns are configured, so coverage is not reported yet."
    return statement + " See [`docs/status.md`](docs/status.md)."


def render(catalog: list[dict], retired: list[dict], strings: dict, today: str) -> str:
    lang = strings["lang_code"]
    out: list[str] = []
    add = out.append

    by_pattern = group_by_pattern(catalog)
    by_kind: dict[str, list[dict]] = {key: [] for key in KIND_ORDER}
    for entry in catalog:
        by_kind[entry["kind"]].append(entry)
    by_slug = {entry["slug"]: entry for entry in catalog}

    live_patterns = [key for key in PATTERN_ORDER if by_pattern[key]]
    live_kinds = [key for key in KIND_ORDER if by_kind[key]]
    # Counted in _stats so the badges, docs/status.md, llms.txt and the site's
    # meta tags all use one definition of "with code" or dated link records.
    stats = _stats.compute()
    with_code, official = stats["with_code"], stats["official"]
    link_records = stats["link_ok"]
    # Recorded citations are not the result of the latest scheduled check.
    evidence_records = stats["evidence_rows"]

    # ---- header ----
    add("<!--")
    add(f"  {strings['generated']}")
    add("-->")
    add("")
    add('<div align="center">')
    add("")
    add('# <img src="site/favicon.svg" width="36" height="36" alt=""> awesome-jev')
    add("")
    add("<sub>Jev Decision Atlas</sub>")
    add("")
    add(f"**{strings['tagline']}**")
    add("")
    add(
        f"[![lint]({REPO_URL}/actions/workflows/lint.yml/badge.svg)]({REPO_URL}/actions/workflows/lint.yml) "
        f"[![links]({REPO_URL}/actions/workflows/links.yml/badge.svg)]({REPO_URL}/actions/workflows/links.yml) "
        f"[![entries](https://img.shields.io/badge/{strings['stat_entries']}-{len(catalog)}-f5a524?style=flat-square)]({SITE}) "
        f"[![dated HTTP 2xx records](https://img.shields.io/badge/{strings['stat_verified'].replace(' ', '%20').replace('-', '--')}-{link_records}-4ec97a?style=flat-square)]({SITE}) "
        f"[![evidence records](https://img.shields.io/badge/{strings['stat_rechecked'].replace(' ', '%20')}-{evidence_records}-a9b3c0?style=flat-square)]({REPO_URL}/actions/workflows/claims.yml) "
        "[![data](https://img.shields.io/badge/data-CC0--1.0-8b949e?style=flat-square)](LICENSE-CC0) "
        "[![code](https://img.shields.io/badge/code-MIT-8b949e?style=flat-square)](LICENSE-MIT)"
    )
    add("")
    add(f"<sub>{strings['badge_note']}</sub>")
    add("")
    add(
        f"[{strings['site_label']}]({SITE}) &nbsp;·&nbsp; "
        f"[{strings['other_name']}]({strings['other_readme']}) &nbsp;·&nbsp; "
        f"[{strings['l_patterns']}](docs/patterns.md) &nbsp;·&nbsp; "
        f"[{strings['l_compat']}](docs/compatibility.md) &nbsp;·&nbsp; "
        f"[{strings['l_vetting']}](docs/vetting.md)"
    )
    add("")
    add(
        f"[{strings['collection_first']}]({SITE}?collection=first-call&lang={lang}) &nbsp;·&nbsp; "
        f"[{strings['collection_build']}]({SITE}?collection=build&lang={lang}) &nbsp;·&nbsp; "
        f"[{strings['collection_measured']}]({SITE}?collection=measured&lang={lang})"
    )
    add("")
    # Rendered from the live site on every Pages deploy (render_images.py) and
    # never committed, so it cannot show a number the catalogue has moved past.
    # GitHub proxies README images through a cache; the query string changes
    # whenever the data does, so a new render is actually fetched.
    shot = "site-zh.png" if lang == "zh" else "site-en.png"
    version = f"{stats['entries']}-{stats['last_sweep']}"
    add(
        f'<a href="{SITE}"><img src="{SITE}img/{shot}?v={version}" '
        f'alt="{strings["shot_alt"]}" width="760"></a>'
    )
    add("")
    add(f"<sub>{strings['shot_cap']}</sub>")
    add("")
    add("</div>")
    add("")
    add("---")
    add("")

    # ---- what this is ----
    add(f"## {strings['about_h']}")
    add("")
    for (line,) in strings["about_rows"]:
        add(f"- {line}")
    add("")
    add(f"> ⚠️ {strings['about_not']}")
    add("")

    # ---- primitives, as a generated figure ----
    add(f"## {strings['prims_h']}")
    add("")
    add(strings["prims_intro"])
    add("")
    add("<picture>")
    add(
        f'  <source media="(prefers-color-scheme: dark)" '
        f'srcset="docs/assets/primitives-{lang}-dark.svg">'
    )
    add(
        f'  <img src="docs/assets/primitives-{lang}-light.svg" '
        f'alt="{strings["prim_alt"]}" width="660">'
    )
    add("</picture>")
    add("")
    add(strings["prims_after"])
    add("")

    # ---- start here ----
    add(f"## {strings['start_h']}")
    add("")
    add(strings["start_intro"])
    add("")
    for index, slug in enumerate(START_HERE, 1):
        entry = by_slug.get(slug)
        if entry is None:
            raise KeyError(
                f"START_HERE names {slug!r}, which is not in catalog.json. Update the list in "
                "build_readme.py when a curated row is renamed or removed."
            )
        why = entry.get("notes_zh" if lang == "zh" else "notes") or summary_of(
            entry, lang
        )
        # An ordered list: a table squeezed the title column until names wrapped.
        add(f"{index}. **[{esc(entry['title'])}]({entry['url']})**")
        add(f"   <sub>{esc(why)}</sub>")
        add("")

    # ---- coverage: a generated figure, not block characters ----
    add(f"## {strings['coverage_h']}")
    add("")
    add(strings["coverage_intro"])
    add("")
    add("<picture>")
    add(
        f'  <source media="(prefers-color-scheme: dark)" '
        f'srcset="docs/assets/coverage-{lang}-dark.svg">'
    )
    add(
        f'  <img src="docs/assets/coverage-{lang}-light.svg" '
        f'alt="{strings["cov_alt"]}" width="100%">'
    )
    add("</picture>")
    add("")
    add(coverage_note(stats, lang))
    add("")

    # ---- measured results: the differentiator, surfaced early ----
    measured = [
        entry
        for entry in catalog
        if entry["kind"] == "benchmark"
        and "vendor-reported" not in entry.get("flags", [])
    ]
    if measured:
        add(f"## {strings['measured_h']}")
        add("")
        add(strings["measured_intro"])
        add("")
        out.extend(entry_list(measured, strings, notes=True))

    # ---- by pattern ----
    add(f"## {strings['patterns_h']}")
    add("")
    add(strings["patterns_intro"].replace("{site}", SITE))
    add("")
    for key in live_patterns:
        name = label(PATTERN_LABELS, key, lang)
        blurb = label(PATTERN_LABELS, key, lang, field=2)
        rows = by_pattern[key]
        add(f"### {name}")
        add("")
        add(f"_{blurb}_")
        add("")
        out.extend(entry_list(rows[:INLINE_PER_PATTERN], strings))
        more = "pattern_more" if len(rows) > INLINE_PER_PATTERN else "pattern_all"
        add(
            strings[more].format(
                shown=min(len(rows), INLINE_PER_PATTERN),
                n=len(rows),
                page=f"docs/by-pattern/{page_name(key, lang)}",
                site=site_link(key, lang),
            )
        )
        add("")

    # ---- by kind, as a table with its own bars ----
    add(f"## {strings['kinds_h']}")
    add("")
    add(strings["kinds_intro"])
    add("")
    kind_peak = max((len(by_kind[key]) for key in KIND_ORDER), default=1) or 1
    add(
        f"| {strings['th_kind'] if 'th_kind' in strings else 'Kind'} | {strings['th_count']} | {strings['th_find']} |"
    )
    add("| --- | :-- | --- |")
    for key in live_kinds:
        count = len(by_kind[key])
        add(
            f"| **{label(KIND_LABELS, key, lang)}** | `{count:>2}` {bar(count, kind_peak)} "
            f"| {esc(label(KIND_LABELS, key, lang, field=2))} |"
        )
    add("")

    # ---- the rest of the repo ----
    add(f"## {strings['repo_h']}")
    add("")
    add(strings["repo_intro"])
    add("")
    add(f"| {strings['th_file']} | {strings['th_what']} |")
    add("| --- | --- |")
    for path, what_en, what_zh in REPO_FILES:
        add(f"| [`{path}`]({path}) | {esc(what_zh if lang == 'zh' else what_en)} |")
    add("")

    # ---- verification ----
    add(f"## {strings['verified_h']}")
    add("")
    add(f"- 🔗 {strings['verified_yes'].format(**stats)}")
    add(f"- 📖 {strings['verified_read']}")
    add(f"- 🔁 {strings['verified_recheck'].replace('{n}', str(evidence_records))}")
    add(f"- ❌ {strings['verified_no']}")
    add("")
    add(f"### {strings['verified_flags_h']}")
    add("")
    used_flags = [
        flag for flag in FLAG_ORDER if any(flag in e.get("flags", []) for e in catalog)
    ]
    add(f"| {strings['th_tag']} | {strings['th_means']} |")
    add("| --- | --- |")
    for flag in used_flags:
        add(
            f"| `{label(FLAG_LABELS, flag, lang)}` "
            f"| {esc(label(FLAG_LABELS, flag, lang, field=2))} |"
        )
    add("")

    if retired:
        add(f"### {strings['retired_h']}")
        add("")
        add(strings["retired_intro"])
        add("")
        add(f"| {strings['th_example']} | {strings['th_why']} |")
        add("| --- | --- |")
        for entry in sorted(retired, key=lambda item: item["title"].lower()):
            why = entry.get("notes_zh" if lang == "zh" else "notes") or "—"
            status = entry.get("link_status")
            add(
                f"| {esc(entry['title'])} | {esc(why)}{f' `HTTP {status}`' if status else ''} |"
            )
        add("")

    # ---- data ----
    add(f"## {strings['data_h']}")
    add("")
    add(strings["data_intro"])
    add("")
    add(f"| {strings['th_file']} | {strings['th_what']} |")
    add("| --- | --- |")
    add(
        f"| [`catalog.json`]({RAW}/catalog.json) | {len(catalog)} {strings['stat_entries']} |"
    )
    add(
        f"| [`retired.json`]({RAW}/retired.json) | {len(retired)} {strings['stat_retired']} |"
    )
    add(
        f"| [`compat.json`]({RAW}/compat.json) | The platform matrix behind `docs/compatibility.md` |"
    )
    add(
        f"| [`patterns.json`]({RAW}/patterns.json) | The decision taxonomy both generators and the MCP server read |"
    )
    add(
        f"| [`schema/entry.schema.json`]({RAW}/schema/entry.schema.json) | One entry's shape |"
    )
    add(f"| [`llms.txt`]({RAW}/llms.txt) | For agents, with the caveats spelled out |")
    add("")

    # ---- contributing + licence ----
    add(f"## {strings['contrib_h']}")
    add("")
    add(strings["contrib_body"])
    add("")
    add(strings["license_body"])
    add("")

    return "\n".join(out)


def write_pattern_pages(catalog: list[dict]) -> list[pathlib.Path]:
    """Write one page per live pattern per language, and remove any others.

    docs/by-pattern/ belongs to this script and nothing else, so a page for a
    pattern that no longer has entries is deleted rather than left behind. A
    stale page would still be served, still be linked from somewhere, and still
    look authoritative — the same failure as a hand-written count left at 148.
    """
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for key, rows in group_by_pattern(catalog).items():
        if not rows:
            continue
        for strings in (EN, ZH):
            path = PAGES_DIR / page_name(key, strings["lang_code"])
            path.write_text(render_page(key, rows, strings))
            written.append(path)
    for path in PAGES_DIR.glob("*.md"):
        if path not in written:
            path.unlink()
            print(f"removed {path.relative_to(ROOT)}: its pattern has no entries")
    return written


def main() -> int:
    catalog = json.loads(CATALOG.read_text())
    retired = json.loads(RETIRED.read_text())
    today = dt.date.today().isoformat()

    try:
        (ROOT / "README.md").write_text(render(catalog, retired, EN, today))
        (ROOT / "README.zh-CN.md").write_text(render(catalog, retired, ZH, today))
        pages = write_pattern_pages(catalog)
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    counts = Counter(pattern for entry in catalog for pattern in entry["patterns"])
    print(f"wrote README.md and README.zh-CN.md from {len(catalog)} entries")
    print(f"wrote {len(pages)} pattern pages under {PAGES_DIR.relative_to(ROOT)}/")
    if counts:
        print(
            "  top patterns: " + ", ".join(f"{k} {v}" for k, v in counts.most_common(5))
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
