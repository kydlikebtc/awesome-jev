"""The reader-facing sentences the READMEs and pattern pages print.

EN and ZH are one pack per language with the same keys; render() and
render_page() take a pack, which is what keeps the two READMEs structurally
identical instead of slowly diverging. The two tables below are bilingual rows
rather than packs because each row pairs a path with its description.

A few short labels (the reading-map summary, back links, the maintenance-check
captions, the caveat label in rows.py) are still chosen inline by language, and
coverage_note() in sections.py writes its own EN and zh sentences.
"""

from __future__ import annotations

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
    "shot_alt": "Searchable Jev catalogue with curated paths, filters, dated source evidence and entry cards",
    "shot_cap": 'Filter by clicking a bar. Two more views: <a href="https://kydlikebtc.github.io/awesome-jev/?view=prims">primitives</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat">compatibility</a>. Every filter and entry is a shareable URL. Also as plain pages: <a href="https://kydlikebtc.github.io/awesome-jev/patterns/">one per pattern</a> · <a href="https://kydlikebtc.github.io/awesome-jev/new.html">what\'s new each week</a> (<a href="https://kydlikebtc.github.io/awesome-jev/feed.xml">Atom feed</a>). Products with code also launch on <a href="https://kydlikebtc.github.io/awesome-jev/launches.html">the weekly launch board</a> (<a href="docs/launches.md">how it works</a>).',
    # ---- what this is ----
    "about_h": "What this is",
    "about_rows": [
        (
            "**Jev** is a decision model from TypeSafe AI. It does not write text — you hand it "
            "state plus typed questions and it returns typed answers with calibrated confidence, "
            "fast and cheap enough to sit in an agent's inner loop.",
        ),
        (
            "**This repo** is a launch board over a catalogue. The board above: products built on Jev, "
            "launched by their makers once a week and voted on. Under it, the Jev Decision Atlas: every "
            "public example of using Jev this index can find, organised by the *decision* being made, "
            "which outlives any one resource. A launch needs its row; a row never needs a launch.",
        ),
        (
            "**How to assess it:** every row names its source, and call-site citations, primitive "
            "claims and caveats are recorded where available. On the board the same record sits beside "
            "the votes, so you can see what was read before you trust a rank.",
        ),
    ],
    "about_not": (
        "Not the product, not an SDK, not affiliated with TypeSafe AI, and not a recommendation. "
        "Inclusion is a source record and a rank is a count of votes; neither is a runtime or "
        "performance endorsement. See [what is verified](#what-is-verified-and-what-is-not)."
    ),
    # ---- the launch board (scripts/readme/board.py) ----
    "chip_board": "Launch board ↗",
    "chip_launch": "Launch a product",
    "footer_brand": "**awesome-jev Launches** · over the Jev Decision Atlas",
    "board_h": "This week's launches",
    "board_intro": (
        "Products built on Jev, launched by their makers once a week, or hunted by anyone who found one. "
        "People vote with a thumbs-up on each launch's post in [Discussions]({discussions}); the week closes "
        "on Sunday 23:59 UTC with a rank. Votes say how many people cared; the evidence beside each launch "
        "says who read the code that calls Jev. The two are never added together, and a rank is not this "
        "catalogue's recommendation. [The board]({board}) has every week, a page per product and per maker, "
        "and the rising list."
    ),
    "board_running_h": "▲ This week: {week}",
    "board_running_note": (
        "In a shuffled order and without counts until the week closes, so nobody votes for whatever is on top."
    ),
    "board_next_h": "Next week: {week}",
    "board_next_note": (
        "Filed for next week, in no particular order. Their vote posts open on Monday {monday}."
    ),
    "board_closed_h": "🏆 Last week: {week}",
    "board_closed_more": (
        "Every launch of {week}, with the votes discounted and why: [the week's page]({page}) · "
        "[results feed]({feed})"
    ),
    "board_empty": (
        "No launch is on the board yet. A launch submitted by Thursday 23:59 UTC is filed on Friday and opens "
        "the next Monday: [launch a product]({form}), yours or one you found, such as those rising below."
    ),
    "board_rising_h": "★ Rising: {start} to {end}",
    "board_rising_note": (
        "The {shown} products whose GitHub stars grew fastest between the two latest weekly refreshes, at least "
        "{n} stars gained, by the gain as a share of the stars before; the first {listed} here. Stars are "
        "GitHub's count, a popularity signal, not a verdict, and nothing is awarded for rising. "
        "[All {shown} on the board]({board})."
    ),
    "board_rising_none": "No product gained {n} stars between the two latest weekly refreshes.",
    "board_stars": "{before} → {after} stars ({share})",
    "board_launch_it": "Launch it ↗",
    "board_again": "can launch again from {day}",
    "board_on": "on the board in {week}",
    "board_vote": "Vote ↗",
    "board_votes": "{votes} votes, {counted} counted",
    "board_ring": "most from new accounts, which counted for nothing",
    "board_maker": "launched by its maker {who}",
    "board_hunter": "hunted by {who}",
    "tiers": {
        "person": "👤 a person read the call site",
        "model": "🤖 a model read the call site, no person yet",
        "file": "🔍 text match only, nobody has read it",
        "none": "no file cited",
    },
    "launch_h": "Launch your product",
    "launch_intro": (
        "Anything built on Jev with public code can launch: a project, plugin, SDK or integration whose row "
        "is in the catalogue ([add the row]({entry}) first if it is not). Makers launch their own; anyone can "
        "hunt one they found. Nobody waits for a maintainer: every case has a rule, and the check on your "
        "issue says what it settled."
    ),
    "th_step": "Step",
    "th_when": "When",
    "th_what_happens": "What happens",
    "launch_steps": [
        (
            "🚀 Launch", "by Thursday 23:59 UTC",
            "Open the [launch form]({form}), or *Launch it* on the product's page, which fills it in. A check "
            "answers the issue at once: ready for next week, or what to change.",
        ),
        (
            "▲ Vote", "Monday to Sunday",
            "The week opens on Monday with a post per launch in [Discussions]({discussions}). A vote is a "
            "thumbs-up on the post: one per account, a maker's own count for nothing, and an account under "
            "30 days old counts half.",
        ),
        (
            "🏆 Results", "the next Monday",
            "The votes are counted, the week is ranked, the top three get their place on their badge, and "
            "each launch's issue hears its result. A product can launch again after 60 days.",
        ),
    ],
    "launch_badge": (
        "Every product has a badge that keeps itself up to date: *listed*, then *launching*, then *vote this "
        "week*, then its place in a top three. One line in your README, never changed again:"
    ),
    "launch_badge_live": "as it reads today for `{slug}`",
    "launch_more": (
        "The rules in full: [how votes count]({rules}) · [the board]({board}) · [each week's results as a "
        "feed]({feed}) · [JSON for agents]({api}) and the MCP server's `launch_board` and `top_launches` "
        "tools · [run the same board in your own repository]({engine})."
    ),
    "launch_rules_anchor": "how-votes-count-rules-v2",
    # ---- primitives ----
    "prims_h": "What Jev returns",
    "prims_intro": (
        "Three core primitives: Choice, Score and Noul. The patterns below use these; "
        "Noul returns a probability without a separate confidence field. "
        "Jev 1.14 also adds experimental [Box](https://docs.typesafe.ai/primitives/box): "
        "one bounding box and confidence per question, with no 'not found' answer. "
        "Box requires an image and the images opt-in described below."
    ),
    "th_prim": "Primitive",
    "th_returns": "Returns",
    "th_limit": "Limits",
    "th_for": "Used for",
    "prims_layers": (
        "Under each primitive, two counts that are never added together: rows whose `question_types` "
        "records a person reading the code call it, and rows where only a text signal shows it — the "
        "weekly refresh found its request or answer shape in the one file the row cites "
        "(`primitives_seen`), which does not show that the code calls it. "
        "See [what is verified](#what-is-verified-and-what-is-not)."
    ),
    "prims_after": (
        "Input is text or structured JSON by default. On the native API, Jev 1.13 and 1.14 also accept "
        "experimental [PNG/JPEG images](https://docs.typesafe.ai/images) with "
        "`TypeSafe-Danger-Zone-Images: true`; audio and video are unsupported. "
        "Default context is **64k** tokens per request, **32k** for the state plus the longest question. "
        "The experimental `TypeSafe-Danger-Zone-Long-Context: true` header raises both limits to "
        "**262k**, with lower speed and accuracy ([models](https://docs.typesafe.ai/models)). "
        "Output tokens are free. "
        "As checked on 2026-11-05, native `jev-latest` and `jev-preview` both point to `jev-1.14.0`, "
        "and there is no separate preview build; both pinned IDs (`jev-1.14.0`, `jev-1.13.0`) are "
        "accepted. "
        "There are no published weights, so it cannot be run locally. "
        "Full cross-platform differences: [`docs/compatibility.md`](docs/compatibility.md)."
    ),
    "picker_intro": (
        "Which primitive fits a decision? The figure below arranges TypeSafe's own guidance as a decision "
        "list: read down and stop at the first yes. The order and the wording are this repository's; every "
        "step cites the page it follows, listed under the figure. It is the vendor's design guidance with "
        "its sources, not a recommendation of any row here."
    ),
    "picker_sources": (
        "Beside each primitive, the rows filed under the pattern named there, counted as the figure above "
        "counts them: read by a person, or text signal only. The steps live in [`picker.json`](picker.json), "
        "which the site's primitives view reads too. Sources, numbered as in the figure: {sources}."
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
        "Every decision pattern, sized by how many entries this catalogue contains. "
        "Use the pattern index below the chart to jump to a section. A zero is a research gap, not a rendering bug."
    ),
    "measured_h": "Measured, not claimed",
    "measured_intro": (
        "Independent measurement reports in the catalogue, including **negative results** that "
        "help explain where an approach fails. These are the original authors' measurements; "
        "this repository has not independently reproduced them. Check each report's dataset, "
        "method and model version before comparing results."
    ),
    "measured_more": (
        "**{shown} of {n}** shown: first the picks of the curated [independent reports]({path}) path, "
        "in its order, then the first of the others in list order · [all {n} on one page, with every "
        "note →]({page}) · [filter on the site]({site})"
    ),
    "measured_more_negative": (
        "**{shown} of {n}** shown: the negative results first, then the picks of the curated "
        "[independent reports]({path}) path, in its order, then the first of the others in list order · "
        "[all {n} on one page, with every note →]({page}) · [filter on the site]({site})"
    ),
    "negative_h": "Negative results first",
    "negative_note": (
        "Rows whose own author measured Jev for the use and concluded against it: a benchmark whose "
        "measurement's direction is *unfavourable*, or another row flagged *measured, not adopted*. "
        "Author-stated, not reproduced here. Read them before the positive examples; "
        "[the site lists them]({site})."
    ),
    "others_h": "Other independent reports",
    "measured_page_intro": (
        "Every independent measurement report and negative result in the catalogue — {n} rows — with every "
        "note and caveat tag, the negative results first. [The README]({readme}) shows those, then the picks "
        "of the curated [independent reports]({path}) path and the first few others; [the site]({site}) lists "
        "the same rows and can filter them further."
    ),
    "patterns_h": "By decision pattern",
    "patterns_intro": (
        "The primary index. Each heading is a decision an agent has to make; the rows are examples "
        "of making it. Caveats appear as short tags — the full note for each row is in "
        "[`catalog.json`](catalog.json) and on [the site]({site})."
    ),
    "stars_note": (
        "★ gives a repository's GitHub stars as a band — {bands}; rows with no repository or "
        "under {floor} stars show no band. Rows run official first, then with code, then by band, "
        "then by title. A band is a popularity signal, not a quality verdict; the exact count, "
        "as last read from GitHub, is in [`catalog.json`]({catalog}) and on [the site]({site})."
    ),
    "list_sep": ", ",
    "list_and": " and ",
    "call_site": "call site",
    "cited_file": "cited file",
    "read_on": ", read {date}",
    "model_read_on": ", read by a model {date}",
    "direction_bit": "author's conclusion: {direction} (author-stated, not reproduced here)",
    "direction_note": (
        "*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they "
        "measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from "
        "the author's report: author-stated, not reproduced here, and absent where the author states none "
        "in words. [{page}]({page_link}) sets every benchmark's measurement side by side."
    ),
    "call_site_note": (
        "A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the "
        "repository's default branch; the date after it is the day a person last read that file "
        "(`evidence.read_on`) or, where it says *read by a model*, the day a model did "
        "(`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for "
        "a file that shows the project speaking Jev's request shape rather than building on Jev, or "
        "only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the "
        "file as it is now, which may differ from what was read, and stops resolving once the file "
        "moves; the weekly claims check reports that."
    ),
    "kinds_h": "By resource kind",
    "kinds_intro": "The same rows grouped by what you will find when you open the link.",
    "th_find": "What you will find",
    "repo_h": "Also in this repo",
    "repo_intro": "The parts that are not the catalog.",
    "repo_skill_division": (
        "`skills/awesome-jev/` complements TypeSafe's own agent skill, [typesafe-ai/skills]({url}) "
        "([its row]({row})), rather than replacing it: for the API contract and for designing questions, "
        "that skill and the live docs it reads are the reference; this one adds what the public ecosystem "
        "shows — worked examples and their caveats, platform differences, and independent and negative results."
    ),
    "th_file": "File",
    "th_what": "What it is",
    "verified_h": "What is verified, and what is not",
    "stat_rechecked": "evidence recorded",
    "verified_recheck": (
        "**Call-site text checks** — {call_site} rows record in `evidence` a file where the project "
        "calls Jev, and strings matched in it. Another {wire_shape} record a file that shows a project "
        "speaking Jev's request shape rather than building on Jev (every `alternative`, whether it "
        "serves that shape or sends Jev the same request to compare, and adapters backed by other "
        "models), and {example_only} only an example the project ships; `evidence.kind` says "
        "which. The weekly [claims job](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) "
        "checks that those strings remain on the default branch and reports missing text or files. "
        "These counts measure recorded evidence, **not latest CI passes**. A text match does not "
        "prove that a call executes, the API is compatible, or the result is correct. Citations a "
        "script marks for a person to re-read are listed in the [review queue](docs/review-queue.md)."
    ),
    "verified_yes": (
        "**Link checks** — {link_ok} rows carry an HTTP 2xx response and a `checked` date; "
        "{link_unstamped} carry no dated success record. Dates vary by row and a past success "
        "does not guarantee availability today. Stars and licences are repository metadata snapshots."
    ),
    "verified_read": (
        "**Source and code review** — `evidence.path` cites the file read, `evidence.read_on` "
        "records the reported review date, `evidence.model_read_on` a model's reading, shown apart, and "
        "`evidence_none` explains missing file evidence. "
        "Reading a call site is separate from running it. Summaries include source descriptions "
        "and machine translations; see the [method and its limits](docs/method.md)."
    ),
    "verified_summaries": (
        "**Whose words the summaries are** — {upstream} summaries are the linked project's own GitHub "
        "description, word for word, and are marked *({upstream_mark})*; {stale} are marked "
        "*({stale_mark})*: taken from one that no longer reads the same. Those words are their "
        "authors'. {curated} summaries are marked as written for this catalogue by a person, {model} "
        "were written for it by a model and are marked *({model_mark})*, and {unlabelled} carry no record "
        "either way. The weekly refresh compares each summary with its repository's description and labels "
        "a match; only a person marks a summary as a person's."
    ),
    "verified_translations": (
        "**Who wrote the Chinese** — {hand} of {entries} rows have a Chinese summary a person wrote; a "
        "model translated the other {machine}, and each of those carries `zh_machine` and is marked "
        "*(机翻)* in the Chinese README, on the Chinese pattern pages and in the site's Chinese view. "
        "The [translation queue](docs/zh-queue.md) lists machine translations for a person to replace: "
        "every one on the most-starred rows, then, most-starred first, others flagged by at least one of "
        "three text signals a script computes (much shorter than the English, a number from the English "
        "missing, mostly ASCII). A signal is a comparison, not a "
        "verdict on a translation, and no row in the READMEs, the pattern pages or the site shows one. "
        "To take some, see "
        "[Claim a translation](CONTRIBUTING.md#claim-a-translation); only a translation of your own "
        "takes `zh_machine` off."
    ),
    "verified_primitives": (
        "**Which primitives** — {read} rows name in `question_types` the primitives a person read the "
        "code calling, and {model} more the primitives a model read there, on rows whose call site only a "
        "model has read (`evidence.model_read_on`). Apart from those, {signal} rows carry `primitives_seen`, "
        "a machine text signal: "
        "the weekly refresh found a primitive's request or answer shape (`\"type\": \"choice\"`, "
        "`Noul(`, `.noul`) in the one file the row cites. A shape in a file is not a call, and "
        "{signal_only} of those rows carry no `question_types`, so the signal is all that is recorded "
        "about their primitives. No filter, count or rule here reads the signal as a primitive claim."
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
    "license_summaries": (
        "Summaries marked *({upstream_mark})* or *({stale_mark})* are the linked projects' own words, "
        "which that dedication does not cover ([sources and licences](docs/sources.md#licences))."
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
    "unindexed_h": "Not yet indexed by pattern",
    "unindexed_readme": (
        "**{n}** of these rows are projects or plugins with code. `overview` is also where the keyword "
        "rules put a description they could not place, and nobody has recorded reading these rows against "
        "the patterns (`patterns_reviewed`), so they are listed apart: [at the end of the Overview "
        "page]({page}), [on the site]({site}), and in the [review queue]({queue}) with the rules' suggestion."
    ),
    "unindexed_page": (
        "Projects and plugins with code, {n} of them, whose only pattern is `overview` and whose rows record "
        "no `patterns_reviewed`. `overview` is also where the keyword rules put a description they could not "
        "place, so these rows may never have been placed at all. A row leaves this list when a person gives "
        "it a pattern, or reads it against [the patterns]({patterns}) and records the date in "
        "`patterns_reviewed`. The [review queue]({queue}) lists them with the rules' suggestion."
    ),
    "page_intro": (
        "Every catalogued example of this decision — {n} of them. The same rows, with caveats, "
        "are in [the index]({readme}); [the site]({site}) can filter them further by language, "
        "primitive and kind."
    ),
    "pattern_evidence": (
        "Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than "
        "once): official documentation {official_docs} · call site {call_site} · wire shape {wire_shape} · "
        "example only {example_only} · independent reports {independent_reports} · negative results "
        "{negative_results} · no file cited {no_file_cited}. “Independent” = a benchmark not flagged "
        "vendor-reported, not reproduced by this repository. [Every pattern side by side]({shape})."
    ),
    "design_link": (
        "Design notes for this decision are in [docs/patterns.md]({page}): what it decides and which "
        "primitive shapes it, and, where one is written, when not to use a decision model for it."
    ),
    "design_link_overview": (
        "What `overview` means in this catalogue, and why a project with code filed only under it counts "
        "as not yet indexed by pattern: [docs/patterns.md]({page})."
    ),
    "official_h": "Official material",
    "official_intro": (
        "What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also "
        "listed below, with its summary."
    ),
    "official_none": "The catalogue files nothing TypeSafe AI publishes under this pattern.",
    "examples_h": "Examples in this repository",
    "examples_intro": (
        "Code under this repository's [`examples/`]({dir}) filed under this pattern. Each is also listed "
        "below, with its summary; [the examples' README]({readme}) says how far they have been checked."
    ),
    "examples_none": "This repository ships no example of this pattern; [`examples/`]({dir}) has the ones it does.",
    "list_h": "The full list",
    "page_other_lang": "[中文]({other})",
    "page_footer": (
        "<sub>Generated from `catalog.json` by `scripts/build_readme.py`. "
        "Edit the catalogue, not this file.</sub>"
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
    "shot_alt": "可搜索的 Jev 目录：精选路径、筛选排序、带日期的来源证据与条目卡片",
    "shot_cap": '点击条形即可筛选。另有两个视图：<a href="https://kydlikebtc.github.io/awesome-jev/?view=prims&lang=zh">三个原语</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat&lang=zh">兼容性矩阵</a>。每个筛选条件和每个条目都是可分享的 URL。也有静态页面：<a href="https://kydlikebtc.github.io/awesome-jev/patterns/">每个模式一页</a> · <a href="https://kydlikebtc.github.io/awesome-jev/new.zh.html">每周新增与退役</a>（<a href="https://kydlikebtc.github.io/awesome-jev/feed.zh.xml">Atom 订阅</a>）。有代码的产品还可以上<a href="https://kydlikebtc.github.io/awesome-jev/launches.zh.html">每周发布榜</a>（<a href="docs/launches.zh-CN.md">规则说明</a>）。',
    "about_h": "这是什么",
    "about_rows": [
        (
            "**Jev** 是 TypeSafe AI 的决策模型。它不生成文本 —— 你给它状态和类型化问题，"
            "它返回带校准置信度的类型化答案，快且便宜到可以放进智能体的内层循环。",
        ),
        (
            "**本仓库**是目录之上的一个发布榜。上面的榜：用 Jev 做的产品，由 Maker 每周发布一次、大家投票。"
            "榜的下面是 Jev 决策图谱：这个索引能找到的每一个 Jev 公开用例，按所做的**决策**组织 —— "
            "资料会过时，决策模式不会。发布需要先有条目；条目不需要发布。",
        ),
        (
            "**如何判断可信度：**每一行都写明来源；有依据时记录调用点、原语声明和注意事项。"
            "榜上同一份记录就放在票数旁边，信一个名次之前先看看读过什么。",
        ),
    ],
    "about_not": (
        "不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。"
        "收录是一份来源记录，名次只是票数的计数；两者都不代表运行验证或性能背书。"
        "详见[哪些经过核实](#哪些经过核实哪些没有)。"
    ),
    # ---- 发布榜（scripts/readme/board.py）----
    "chip_board": "发布榜 ↗",
    "chip_launch": "发布产品",
    "footer_brand": "**awesome-jev 发布榜** · 建在 Jev 决策图谱之上",
    "board_h": "本周发布榜",
    "board_intro": (
        "用 Jev 做出来的产品，由 Maker 每周发布一次，任何人也可以推荐（hunt）自己发现的产品。"
        "大家在每个 Launch 的 [Discussions]({discussions}) 帖子上点赞投票，每周日 23:59 UTC 收榜、排名。"
        "票数说明有多少人关心；每个 Launch 旁边的证据说明谁读过它调用 Jev 的代码。两者从不相加，"
        "名次也不是本目录的推荐。[发布榜]({board})上有每一周、每个产品和每位 Maker 的页面，以及上升榜。"
    ),
    "board_running_h": "▲ 本周：{week}",
    "board_running_note": "收榜前按随机顺序展示、不显示票数，免得大家都投最上面那个。",
    "board_next_h": "下周：{week}",
    "board_next_note": "已登记、下周上榜的 Launch，不分先后。投票帖在 {monday}（周一）开放。",
    "board_closed_h": "🏆 上周：{week}",
    "board_closed_more": "{week} 的全部 Launch、被折算的票和原因：[当周页面]({page}) · [结果订阅]({feed})",
    "board_empty": (
        "榜上还没有 Launch。周四 23:59 UTC 前提交的 Launch 周五登记、下周一开榜："
        "[发布一个产品]({form})，自己做的或你发现的都行，比如下面上升最快的这些。"
    ),
    "board_rising_h": "★ 上升最快：{start} 至 {end}",
    "board_rising_note": (
        "最近两次每周刷新之间，GitHub 星标涨得最快的 {shown} 个产品：至少涨了 {n} 个，按涨幅占原有星标的比例排序，"
        "这里列前 {listed} 个。星标是 GitHub 的计数，是热度信号，不是评价；上升不会得到任何奖励。"
        "[发布榜上的全部 {shown} 个]({board})。"
    ),
    "board_rising_none": "最近两次每周刷新之间，没有产品的星标涨到 {n} 个。",
    "board_stars": "{before} → {after} 星（{share}）",
    "board_launch_it": "发布它 ↗",
    "board_again": "{day} 起可再次发布",
    "board_on": "{week} 在榜",
    "board_vote": "投票 ↗",
    "board_votes": "{votes} 票，计 {counted} 票",
    "board_ring": "多数票来自新账号，这些票不计",
    "board_maker": "Maker {who} 发布",
    "board_hunter": "{who} 推荐",
    "tiers": {
        "person": "👤 有人读过调用点",
        "model": "🤖 模型读过调用点，尚无人复核",
        "file": "🔍 仅文本匹配，还没有人读过",
        "none": "没有引用文件",
    },
    "launch_h": "发布你的产品",
    "launch_intro": (
        "任何用 Jev 做的、代码公开的东西都可以发布：项目、插件、SDK 或集成，只要它的条目在目录里"
        "（没有就先[添加条目]({entry})）。Maker 发布自己的产品；任何人都可以推荐自己发现的产品。"
        "没有一步需要等维护者：每种情况都有规则，issue 上的检查会告诉你它的判定。"
    ),
    "th_step": "步骤",
    "th_when": "时间",
    "th_what_happens": "会发生什么",
    "launch_steps": [
        (
            "🚀 发布", "周四 23:59 UTC 前",
            "打开[发布表单]({form})，或在产品页点「发布它」，表单会自动填好。检查会立刻在 issue 上回复："
            "下周上榜，或者需要改什么。",
        ),
        (
            "▲ 投票", "周一到周日",
            "周一开榜，每个 Launch 在 [Discussions]({discussions}) 里有一个帖子。投票就是在帖子上点赞："
            "每个账号一票，Maker 自己的票不计，注册不满 30 天的账号算半票。",
        ),
        (
            "🏆 结果", "下周一",
            "计票、排名，前三名的徽章显示名次，每个 Launch 的 issue 都会收到结果。60 天后可以再次发布。",
        ),
    ],
    "launch_badge": (
        "每个产品都有一枚自动更新的徽章：已收录，然后是发布中、本周投票，再到前三名的名次。"
        "在你的 README 里放一行，之后不用再改："
    ),
    "launch_badge_live": "`{slug}` 今天的样子",
    "launch_more": (
        "完整规则：[怎么计票]({rules}) · [发布榜]({board}) · [每周结果订阅]({feed}) · [给智能体的 JSON]({api}) "
        "以及 MCP 服务器的 `launch_board`、`top_launches` 工具 · [在你自己的仓库里跑同一套发布榜]({engine})。"
    ),
    "launch_rules_anchor": "怎么计票规则-v2",
    "prims_h": "Jev 返回什么",
    "prims_intro": (
        "三个核心原语：Choice、Score 和 Noul。下面的模式使用它们；Noul 返回概率，没有单独的 confidence 字段。"
        "Jev 1.14 还新增了实验性 [Box](https://docs.typesafe.ai/primitives/box)：每个问题返回一个边界框和置信度，"
        "没有「未找到」答案。Box 需要图像，并须按下文显式启用图像功能。"
    ),
    "th_prim": "原语",
    "th_returns": "返回",
    "th_limit": "限制",
    "th_for": "用来",
    "prims_layers": (
        "每个原语下方有两个互不相加的数：先是 `question_types` 记录了有人读过代码、确认调用该原语的行数；"
        "再是只有文本信号的行数 —— 每周刷新在该行所引的那一个文件中找到了它的请求或回答结构"
        "（`primitives_seen`），这并不表明代码调用了它。见[哪些经过核实](#哪些经过核实哪些没有)。"
    ),
    "prims_after": (
        "默认输入为文本或结构化 JSON。原生 API 的 Jev 1.13 和 1.14 也支持实验性 "
        "[PNG/JPEG 图像](https://docs.typesafe.ai/images)，须发送 `TypeSafe-Danger-Zone-Images: true`；"
        "不支持音频和视频。默认每次请求 **64k** token，其中 state 加最长问题最多 **32k**。"
        "实验性请求头 `TypeSafe-Danger-Zone-Long-Context: true` 将两项限制均提高到 **262k**，"
        "但速度和准确率会降低（见[模型文档](https://docs.typesafe.ai/models)）。输出 token 免费。"
        "截至 2026-11-05，原生 `jev-latest` 和 `jev-preview` 都指向 `jev-1.14.0`，目前没有单独的预览版；"
        "两个固定版本 ID（`jev-1.14.0`、`jev-1.13.0`）均可用。"
        "权重未公开，因此无法本地运行。"
        "跨平台差异全表见 [`docs/compatibility.md`](docs/compatibility.md)。"
    ),
    "picker_intro": (
        "某个决策该用哪个原语？下图把 TypeSafe 官方的指引排成一张判断清单：自上而下，遇到第一个「是」即停。"
        "顺序与措辞出自本仓库；每一步都注明所依据的页面，列在图下。"
        "这是厂商附有来源的设计指引，不是对本目录任何条目的推荐。"
    ),
    "picker_sources": (
        "每个原语旁是归入所列模式的行数，计法同上图：人读确认，或仅文本信号。"
        "这些步骤存于 [`picker.json`](picker.json)，网站的原语页也读取它。来源（编号同图中）：{sources}。"
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
        "全部决策模式，按本目录的收录数量排列长度。图表下方的场景索引可跳转到对应章节。"
        "数字为 0 的是待补的研究缺口，不是渲染 bug。"
    ),
    "measured_h": "实测，而非宣称",
    "measured_intro": (
        "本目录收录的独立测量报告，包括有助于理解适用边界的**负面结果**。这些是原作者的测量，"
        "本仓库没有独立复现。比较结果前，请分别查看数据集、测试方法和模型版本。"
    ),
    "measured_more": (
        "已显示 **{shown} / {n}** 条：先是精选路径[独立测量报告]({path})选出的条目，按该路径的顺序，"
        "再按列表顺序补上其余条目中靠前的几条 · [在单独页面查看全部 {n} 条及全部备注 →]({page}) · "
        "[在站点上筛选]({site})"
    ),
    "measured_more_negative": (
        "已显示 **{shown} / {n}** 条：先是负面结果，再是精选路径[独立测量报告]({path})选出的条目，按该路径的顺序，"
        "再按列表顺序补上其余条目中靠前的几条 · [在单独页面查看全部 {n} 条及全部备注 →]({page}) · "
        "[在站点上筛选]({site})"
    ),
    "negative_h": "负面结果优先",
    "negative_note": (
        "作者本人针对这一用途测量过 Jev 并得出不采用结论的行：基准测试的测量结论为*不利*，或其他行带有"
        "*实测后未采用*标记。作者自述，未经本仓库复现。请先读它们，再看正面例子；[站点也列出了它们]({site})。"
    ),
    "others_h": "其他独立测量报告",
    "measured_page_intro": (
        "本目录收录的全部独立测量报告和负面结果 —— 共 {n} 条，附全部备注和警示标记，负面结果排在最前。"
        "[README]({readme}) 先显示负面结果，再显示精选路径[独立测量报告]({path})选出的条目和其余条目中靠前的几条；"
        "[站点]({site})列出同样这些条目，并可进一步筛选。"
    ),
    "patterns_h": "按决策模式",
    "patterns_intro": (
        "主索引。每个标题是智能体必须做的一个决策；下面的行是做这个决策的例子。"
        "警示以短标记呈现 —— 每行的完整备注在 [`catalog.json`](catalog.json) 和[站点]({site})里。"
    ),
    "stars_note": (
        "★ 以区间给出仓库的 GitHub star 数 —— {bands}；没有仓库或不足 {floor} 星的行不标区间。"
        "排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；"
        "最近一次从 GitHub 读到的精确数字在 [`catalog.json`]({catalog}) 和[站点]({site})上。"
    ),
    "list_sep": "、",
    "list_and": "、",
    "call_site": "调用点",
    "cited_file": "引用文件",
    "read_on": "，{date} 阅读",
    "model_read_on": "，{date} 模型阅读",
    "direction_bit": "作者结论：{direction}（作者自述，未经本仓库复现）",
    "direction_note": (
        "*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、"
        "不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。"
        "[{page}]({page_link}) 把每条基准测试的测量字段并列展示。"
    ),
    "call_site_note": (
        "*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；"
        "其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，"
        "则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。"
        "*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，"
        "或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，"
        "可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。"
    ),
    "kinds_h": "按资源形态",
    "kinds_intro": "同样这些行，按你点开链接后会看到什么来分组。",
    "th_find": "点开会看到",
    "repo_h": "本仓库还有什么",
    "repo_intro": "除目录数据之外的部分。",
    "repo_skill_division": (
        "`skills/awesome-jev/` 是对 TypeSafe 官方智能体技能 [typesafe-ai/skills]({url})（[目录条目]({row})）"
        "的补充，而非替代：API 契约与问题设计以官方技能及其所读的实时文档为准；本技能补充公开生态里能看到的东西"
        "——实际示例及其警示、各平台差异，以及独立测量与负面结果。"
    ),
    "th_file": "文件",
    "th_what": "是什么",
    "verified_h": "哪些经过核实，哪些没有",
    "stat_rechecked": "已记录证据",
    "verified_recheck": (
        "**调用点文本复查** —— 有 {call_site} 行通过 `evidence` 记录了项目调用 Jev 的文件及其中匹配的字符串。"
        "另有 {wire_shape} 行记录的文件只表明项目采用了 Jev 的请求结构、并非基于 Jev 构建"
        "（所有 `alternative`——无论是自己提供这种结构，还是向 Jev 发送同样的请求作对比——"
        "以及由其他模型支撑的适配器），{example_only} 行记录的只是项目附带的示例；"
        "`evidence.kind` 标明属于哪一种。"
        "每周 [claims 任务](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) "
        "检查这些字符串是否仍在默认分支，发现文本或文件缺失时报告。"
        "这些数字是已记录的证据数量，**不是最新 CI 通过数**。文本匹配不能证明调用实际执行、"
        "API 兼容或结果正确。脚本标出、需要人重读的引用列在[复核队列](docs/review-queue.md)。"
    ),
    "verified_yes": (
        "**链接检查** —— 有 {link_ok} 行记录了 HTTP 2xx 响应和 `checked` 日期，"
        "另有 {link_unstamped} 行没有带日期的成功记录。检查日期因条目而异，过去成功不保证今天仍可访问。"
        "star 数和许可证也是仓库元数据的快照。"
    ),
    "verified_read": (
        "**来源与代码阅读** —— `evidence.path` 指向所读文件，`evidence.read_on` 记录声明的阅读日期，"
        "`evidence.model_read_on` 记录模型的阅读、单独显示，`evidence_none` 解释缺少文件证据的原因。阅读调用点与运行代码是两件事。"
        "摘要包含源项目描述与机翻，详见[方法与局限](docs/method.md)。"
    ),
    "verified_summaries": (
        "**摘要是谁的文字** —— {upstream} 条摘要的英文原文就是被链接项目自己在 GitHub 上的描述，"
        "逐字相同，这些行标为 *({upstream_mark})*；{stale} 条标为 *({stale_mark})*：英文取自项目描述，"
        "但两者已不再相同。这些文字出自项目作者，中文摘要是其译文。{curated} 条摘要标明由人为本目录撰写，"
        "{model} 条由模型为本目录撰写并标为 *({model_mark})*，{unlabelled} 条未作记录。"
        "每周刷新会把每条英文摘要与其仓库描述比对并标出相同者；只有人才能把摘要标为人写的。"
    ),
    "verified_translations": (
        "**中文是谁写的** —— {entries} 行中有 {hand} 行的中文摘要由人撰写；其余 {machine} 行由模型翻译，"
        "带有 `zh_machine`，并在中文 README、中文模式页面和站点的中文视图中逐条标为 *(机翻)*。"
        "[翻译队列](docs/zh-queue.md)列出等待有人替换的机翻：先是星标最高各行的全部机翻，再按星标从高到低"
        "列出被脚本计算的三项文本信号（比英文短得多、缺少英文里的数字、大部分是 ASCII 字符）中至少一项标出的"
        "其他机翻。信号只是对照比较，不是对译文的结论，"
        "README、模式页面和站点上的各行都不显示信号。认领方法见[认领翻译](CONTRIBUTING.md#claim-a-translation)；"
        "只有你自己写的译文才能去掉 `zh_machine`。"
    ),
    "verified_primitives": (
        "**用了哪些原语** —— 有 {read} 行在 `question_types` 中记录了有人读代码时确认调用的原语；"
        "另有 {model} 行记录的是模型读代码时确认的原语，这些行的调用点只有模型读过（`evidence.model_read_on`）。"
        "此外还有 {signal} 行带 `primitives_seen`，这是机器文本信号：每周刷新在该行所引的那一个文件中"
        "找到了某个原语的请求或回答结构（`\"type\": \"choice\"`、`Noul(`、`.noul`）。"
        "文件里出现这种结构不等于调用；其中 {signal_only} 行没有 `question_types`，"
        "这个信号就是关于它们所用原语的全部记录。本目录的筛选、计数和规则都不会把它当作原语声明。"
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
    "license_summaries": (
        "标有 *({upstream_mark})* 或 *({stale_mark})* 的摘要是被链接项目自己的文字（中文为其译文），"
        "不在上述 CC0 声明之内（见[来源与许可](docs/sources.md#licences)）。"
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
    "unindexed_h": "尚未按模式索引",
    "unindexed_readme": (
        "其中 **{n}** 行是带代码的项目或插件。`overview` 也是关键词规则无法归类时给出的默认值，"
        "而这些行没有任何人对照决策模式阅读过的记录（`patterns_reviewed`），因此单独列出："
        "见 [Overview 页面末尾]({page})、[站点]({site})，以及附有规则建议的[复核队列]({queue})。"
    ),
    "unindexed_page": (
        "带代码的项目或插件，共 {n} 行：唯一的模式是 `overview`，且没有记录 `patterns_reviewed`。"
        "`overview` 也是关键词规则无法归类时给出的默认值，所以这些行可能从未被归类。"
        "有人为某行指定模式，或对照[决策模式]({patterns})读过它并把日期记入 `patterns_reviewed` 后，"
        "该行就会离开此列表。[复核队列]({queue})列出了它们以及规则给出的建议。"
    ),
    "page_intro": (
        "这个决策的全部已收录例子 —— 共 {n} 条。"
        "同样这些行及其警示也在[索引]({readme})里；[站点]({site})还能按语言、原语和形态进一步筛选。"
    ),
    "pattern_evidence": (
        "本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 {official_docs} · "
        "调用点 {call_site} · 接口形态 {wire_shape} · 仅示例 {example_only} · "
        "独立报告 {independent_reports} · 负面结果 {negative_results} · 未引用文件 {no_file_cited}。"
        "“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照]({shape})。"
    ),
    "design_link": (
        "这个决策的设计说明见 [docs/patterns.zh-CN.md]({page})：它决定什么、用哪种原语来建模，"
        "以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版]({en})译写，以英文版为准。"
    ),
    "design_link_overview": (
        "`overview` 在本目录里是什么意思、为什么只归在它下面的带代码项目算作尚未按模式索引，"
        "见 [docs/patterns.zh-CN.md]({page})（由模型从[英文版]({en})译写，以英文版为准）。"
    ),
    "official_h": "官方材料",
    "official_intro": (
        "TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。"
        "每一条在下文也都列出，附有摘要。"
    ),
    "official_none": "目录里没有归在这个模式下的 TypeSafe AI 官方材料。",
    "examples_h": "本仓库的示例",
    "examples_intro": (
        "本仓库 [`examples/`]({dir}) 里归在这个模式下的代码。每一条在下文也都列出，附有摘要；"
        "[示例的 README]({readme}) 说明了它们核验到了哪一步。"
    ),
    "examples_none": "本仓库没有这个模式的示例；已有的示例见 [`examples/`]({dir})。",
    "list_h": "完整列表",
    "page_other_lang": "[English]({other})",
    "page_footer": (
        "<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。"
        "请修改目录，不要改这个文件。</sub>"
    ),
    "gap": "暂无例子",
    "stat_entries": "条目",
    "stat_with_code": "含代码",
    "stat_official": "官方",
    "stat_verified": "带日期的2xx",
    "stat_patterns": "覆盖模式",
    "stat_retired": "已退休",
}

# ZH keys whose Chinese a model wrote rather than a person: the same disclosure
# `zh_machine` makes for a catalogue row, and rendered the same way, with
# "(机翻)" after it. A person who rewrites one removes its key from here.
ZH_MACHINE = frozenset(
    {
        "stars_note", "verified_recheck", "verified_read", "verified_summaries", "license_summaries", "unindexed_readme",
        "unindexed_page", "prims_intro", "prims_after", "prims_layers", "verified_primitives", "verified_translations",
        "call_site_note", "measured_more", "measured_page_intro", "repo_skill_division", "direction_note",
        "measured_more_negative", "negative_note", "pattern_evidence", "design_link", "design_link_overview",
        "official_intro", "official_none", "examples_intro", "examples_none", "picker_intro", "picker_sources",
        # The launch board's sections (2026-11-05): about_rows is marked line
        # by line in sections.what_this_is, launch_steps under its table.
        "about_rows", "about_not", "board_intro", "board_running_note", "board_next_note", "board_closed_more",
        "board_empty", "board_rising_note", "board_rising_none", "launch_intro", "launch_steps", "launch_badge",
        "launch_more",
    }
)

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
        "docs/shape.md",
        "The catalogue as a dataset: languages, how rows reach Jev, star bands by kind, languages by pattern.",
        "把目录当作数据集来看：语言、如何接入 Jev、各类型的 star 区间、各模式用的语言。 <sub>(机翻)</sub>",
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

# A REPO_FILES path the Chinese README links in its Chinese version instead.
REPO_FILES_ZH = {"docs/shape.md": "docs/shape.zh-CN.md", "docs/patterns.md": "docs/patterns.zh-CN.md"}

# The data files listed under "Machine-readable data", after catalog.json and
# retired.json, whose rows carry live counts and are written in sections.py.
DATA_FILES = [
    ("compat.json", "The platform matrix behind `docs/compatibility.md`", "`docs/compatibility.md` 使用的平台兼容性数据"),
    ("patterns.json", "The decision taxonomy both generators and the MCP server read", "生成器与 MCP server 共用的决策模式分类"),
    ("collections.json", "Bilingual editorial paths, selection reasons and limitations", "双语精选路径、推荐理由与使用限制"),
    ("schema/entry.schema.json", "One entry's shape", "每条目录记录的字段规范"),
    ("llms.txt", "For agents, with the caveats spelled out", "供智能体读取的目录说明，明确附带限制"),
]
