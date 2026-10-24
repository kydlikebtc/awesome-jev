# Document triage

<sub>[awesome-jev](../../README.md) · [中文](document-triage.zh-CN.md)</sub>

_Classify and route incoming documents, invoices and forms._

Every catalogued example of this decision — 21 of them. The same rows, with caveats, are in [the index](../../README.md#document-triage); [the site](https://kydlikebtc.github.io/awesome-jev/?p=document-triage&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#document-triage): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 0 · call site 20 · wire shape 0 · example only 0 · independent reports 2 · negative results 0 · no file cited 1. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

The catalogue files nothing TypeSafe AI publishes under this pattern.

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[docjev](https://github.com/jerryjliu/docjev)** — A very fast document classifier/splitter using Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · jerryjliu · `Py` · call site [`src/jev_docs/engines/jev.py`](https://github.com/jerryjliu/docjev/blob/HEAD/src/jev_docs/engines/jev.py), read 2026-09-22</sub>

- **[formanator](https://github.com/timrogers/formanator)** — Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) clients, with support for AI-powered receipt analysis with an LLM or Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · timrogers · `Rs` · call site [`src/typesafe.rs`](https://github.com/timrogers/formanator/blob/HEAD/src/typesafe.rs), read 2026-09-22</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · kyotofin · `TS` · call site [`src/backend.ts`](https://github.com/kyotofin/tax-doc-classifier/blob/HEAD/src/backend.ts), read 2026-09-22</sub>

- **[doc-router](https://github.com/misbahsy/doc-router)** — A Document OCR Router to help route pages based on content. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · misbahsy · `Rs` · call site [`crates/doc-router-jev/src/wire.rs`](https://github.com/misbahsy/doc-router/blob/HEAD/crates/doc-router-jev/src/wire.rs), read 2026-09-22</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)** — Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。 <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · zaious · `Py` · call site [`scripts/common/jev_client.py`](https://github.com/Zaious/jev-capability-atlas/blob/HEAD/scripts/common/jev_client.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Local-first, SQLite receipts, zero dependencies. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · romiluz13 · `Py` · call site [`jevmory/cli.py`](https://github.com/romiluz13/jevmory/blob/HEAD/jevmory/cli.py), read 2026-09-22</sub>

- **[pdf-race](https://github.com/goodrahstar/pdf-race)** — Docling → Jev vs Docling → Gemini 3.8 Flash vs Gemini reading the PDF: same documents, one clock, scored against arXiv's own metadata <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · goodrahstar · `JS` · call site [`lib/lanes.mjs`](https://github.com/goodrahstar/pdf-race/blob/HEAD/lib/lanes.mjs), read 2026-09-24</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)** — Agent skill that spots bounded-judgment steps, tries a typed decision model (TypeSafe's Jev) first, and documents every attempt <sub>(upstream description)</sub>
  <sub>`Plugin` · harrymunro · `Py` · call site [`skills/decision-first/scripts/ask.py`](https://github.com/harrymunro/decision-first/blob/HEAD/skills/decision-first/scripts/ask.py), read 2026-09-22</sub>

- **[jev-boe-demo](https://github.com/Tatuck/jev-boe-demo)** — Daily demo applying TypeSafe's Jev model to Spain's official gazette (BOE). <sub>(upstream description)</sub>
  <sub>`Project` · tatuck · `TS` · call site [`pipeline/analyze.ts`](https://github.com/Tatuck/jev-boe-demo/blob/HEAD/pipeline/analyze.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-builder](https://github.com/collapseindex/jev-builder)** — A browser form for building requests to TypeSafe's Jev: pick a template, fill in the blanks, copy the request. No JSON, no install, runs locally. <sub>(upstream description)</sub>
  <sub>`Project` · collapseindex · `JS` · call site [`jev-builder-core.js`](https://github.com/collapseindex/jev-builder/blob/HEAD/jev-builder-core.js), read 2026-09-22</sub>

- **[jev-decision-lab](https://github.com/jlov7/jev-decision-lab)** — A local lab for seeing what TypeSafe's Jev judgment model does on realistic business cases: typed answers, probabilities, policy in code, receipts. <sub>(upstream description)</sub>
  <sub>`Project` · jlov7 · `Py` · call site [`jev_lab/adapters.py`](https://github.com/jlov7/jev-decision-lab/blob/HEAD/jev_lab/adapters.py), read 2026-09-22</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model. <sub>(upstream description)</sub>
  <sub>`Project` · charlyhno-eng · `TS` · call site [`server/classification-cache.ts`](https://github.com/Charlyhno-eng/jev-document-classification/blob/HEAD/server/classification-cache.ts), read 2026-09-22</sub>

- **[jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction)** — Parsing the PDF and extracting the relevant information <sub>(upstream description)</sub>
  <sub>`Project` · abhishekmamdapure · `Py` · call site [`backend/main.py`](https://github.com/abhishekmamdapure/jev-information-extraction/blob/HEAD/backend/main.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-layer](https://github.com/typakon4/jev-layer)** — Portable System-1 decision layer for agent harnesses with host-owned routing, receipts, replay, and fail-open integrations. <sub>(upstream description)</sub>
  <sub>`Integration` · typakon4 · `JS` · call site [`src/providers/typesafe.mjs`](https://github.com/typakon4/jev-layer/blob/HEAD/src/providers/typesafe.mjs), read 2026-09-22</sub>

- **[jev-organize](https://github.com/nexibeo/jev-organize)** — Throw in a pile of company files and get them classified and organized by department, type, sensitivity, date, counterparty and PII, with an index for AI agents. Powered by TypeSafe's Jev on OpenRouter (17¢ per 1,000 files). Zero-dependency Node CLI + Claude skill + Codex agent. <sub>(upstream description)</sub>
  <sub>`Plugin` · nexibeo · `JS` · call site [`skills/jev-organize/scripts/src/jev.mjs`](https://github.com/nexibeo/jev-organize/blob/HEAD/skills/jev-organize/scripts/src/jev.mjs), read 2026-09-24</sub>

- **[jev-report](https://github.com/HackSing/jev-report)** — 发明 RLHF 的人，这次做了个不会说话的模型：Jev 独立研究报告。52 页 PDF + 50 条中文实测复现包 + 143 条可回溯数据表 <sub>(upstream description)</sub>
  <sub>`Project` · hacksing · `Py` · call site [`figs.py`](https://github.com/HackSing/jev-report/blob/HEAD/figs.py), read 2026-09-22</sub>

- **[jev-score](https://github.com/a-Fig/jev-score)** — Local-first document evaluation workspaces powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · a-fig · `JS` · call site [`src/jev.mjs`](https://github.com/a-Fig/jev-score/blob/HEAD/src/jev.mjs), read 2026-09-22</sub>

- **[last-exit](https://github.com/0x963D/last-exit)** — A cyberpunk border encounter powered by TypeSafe Jev. Bluff the guard. Inspect the receipts. <sub>(upstream description)</sub>
  <sub>`Project` · 0x963d · `JS` · call site [`lib/hosted.mjs`](https://github.com/0x963D/last-exit/blob/HEAD/lib/hosted.mjs), read 2026-09-22</sub>

- **[Quicksilver](https://github.com/UditAkhourii/quicksilver)** — Claude Code skill that hands relevance calls to Jev: one noul per file, log line or ticket ('which of these files handle auth?'), asked in parallel and sorted by probability, so Claude gets a shortlist with confidences instead of reading everything.
  <sub>`Plugin` · uditakhourii · `JS` · `noul` · call site [`skills/quicksilver/scripts/qs.mjs`](https://github.com/UditAkhourii/quicksilver/blob/HEAD/skills/quicksilver/scripts/qs.mjs)</sub>

- **[tiab-review-plugin](https://github.com/youkiti/tiab-review-plugin)** — A Chrome extension that speeds up title-and-abstract screening for systematic reviews, published on the Chrome Web Store.
  <sub>`Plugin` · youkiti · `TS` · call site [`src/lib/providers/typesafe.ts`](https://github.com/youkiti/tiab-review-plugin/blob/HEAD/src/lib/providers/typesafe.ts), read 2026-09-24</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified claims`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
