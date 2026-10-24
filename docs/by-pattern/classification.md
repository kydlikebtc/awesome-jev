# Classification

<sub>[awesome-jev](../../README.md) · [中文](classification.zh-CN.md)</sub>

_Put an item into a taxonomy, including deep hierarchies walked with probabilities._

Every catalogued example of this decision — 126 of them. The same rows, with caveats, are in [the index](../../README.md#classification); [the site](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#classification): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 4 · call site 116 · wire shape 1 · example only 0 · independent reports 11 · negative results 1 · no file cited 9. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) <sub>`Official docs` · `Py` · `score`</sub>
- [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) <sub>`Official docs` · `Py`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — Walks deep patent, retail, biomedical and source-code taxonomies with a parallel beam search over Choice probabilities.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block.
  <sub>`Official docs` · `Py`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★10k+ · `TS` · `choice` · `noul` · call site [`apps/web/utils/decision-model/typesafe.ts`](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/typesafe.ts), read 2026-09-22</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.
  <sub>`Project` · ★10k+ · Vercel Labs · `TS` · `choice` · call site [`apps/web/lib/jev/compose.ts`](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts), read 2026-09-22</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.
  <sub>`Benchmark` · ★10k+ · `TS` · `choice` · call site [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js), read 2026-09-22 · author's conclusion: unfavourable (author-stated, not reproduced here) · ⚠ `shadow mode`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · call site [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql), read 2026-09-22</sub>

- **[332_lab-jev-chat](https://github.com/Liyucheng1997/332_lab-jev-chat)** — A Windows WeChat assistant: Jev judges the intent of each incoming message and DeepSeek suggests replies.
  <sub>`Project` · ★100+ · liyucheng1997 · `Kt` · call site [`windows/jev_windows/jev_api.py`](https://github.com/Liyucheng1997/332_lab-jev-chat/blob/HEAD/windows/jev_windows/jev_api.py), read 2026-09-24</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends.
  <sub>`Project` · ★100+ · `TS` · `choice` · call site [`src/search.ts`](https://github.com/ellipsis-dev/blink/blob/HEAD/src/search.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)** — Zero-shot text classification over plain HTTP — no API key, no account. One Cloudflare Worker, a CLI, and an MCP server. https://classifier.dev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · mrmps · `TS` · call site [`src/jev.ts`](https://github.com/mrmps/classifier-dev/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — A very fast document classifier/splitter using Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · jerryjliu · `Py` · call site [`src/jev_docs/engines/jev.py`](https://github.com/jerryjliu/docjev/blob/HEAD/src/jev_docs/engines/jev.py), read 2026-09-22</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)** — An introduction to Jev with hands-on tests: Choice, Score and Noul turn natural language into typed judgements for classification, scoring and routing, compared with DeepSeek on comment labelling, speed and results, with CSV import, replay and offline reports.
  <sub>`Benchmark` · ★100+ · nanmicoder · `JS` · call site [`src/backends/jev.mjs`](https://github.com/NanmiCoder/jev-arena/blob/HEAD/src/backends/jev.mjs), read 2026-09-24</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts), read 2026-09-22</sub>

- **[Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis)** — An on-demand crypto market terminal: pick a coin and a tweet sample, and Jev turns market data, funding rates and social sentiment into a Buy, Sell, Hold or Take Profit decision card. It never places trades.
  <sub>`Project` · ★100+ · brainstormity · `Py` · call site [`app/services/typesafe_service.py`](https://github.com/brainstormity/Jev-X-Sentiment-Analysis/blob/HEAD/app/services/typesafe_service.py), read 2026-09-24</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js), read 2026-09-22</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy.
  <sub>`Project` · ★100+ · `TS` · `choice` · `score` · call site [`engine/jev-service.ts`](https://github.com/irfndi/prism-liquidity-agent/blob/HEAD/engine/jev-service.ts), read 2026-09-22</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — Automate your job: local-first AI task hub. Email, Teams, Slack & reports -> one timeline -> AI triage -> your coding agents (Claude Code, Codex, Gemini) do the work, you approve. <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★100+ · ldbumble · `Py` · call site [`taskuary/jev.py`](https://github.com/ldbumble/taskuary/blob/HEAD/taskuary/jev.py), read 2026-09-22</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · kyotofin · `TS` · call site [`src/backend.ts`](https://github.com/kyotofin/tax-doc-classifier/blob/HEAD/src/backend.ts), read 2026-09-22</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — A browser extension that removes page clutter, with reusable template rules.
  <sub>`Project` · ★100+ · kitze · `TS` · call site [`lib/jev.ts`](https://github.com/kitze/unclutter/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — Detect youtube sponsor segment with live audio and transcript powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · trungdq88 · `JS` · call site [`extension/lib/jev.js`](https://github.com/trungdq88/youtube-sponsor-detection/blob/HEAD/extension/lib/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★10+ · 24601 · `Py` · call site [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md), read 2026-09-24</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · devanshbatham · `Rs` · call site [`src/jev.rs`](https://github.com/devanshbatham/commit-miner/blob/HEAD/src/jev.rs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness — Jev-powered risk classification & evidence-gated auto-approval. Fail-closed by construction. dsh 生态第一个 System-1 决策插件 <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · asktheway · `TS` · call site [`scripts/smoke.mjs`](https://github.com/AskTheWay/dsh-jev-interceptor/blob/HEAD/scripts/smoke.mjs), read 2026-09-24</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scoring, and semantic predicates from SQL. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · prasanthj · `C++` · call site [`benchmarks/live.py`](https://github.com/prasanthj/duckdb-jev/blob/HEAD/benchmarks/live.py), read 2026-09-22</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — Software, by reflex. A sentence becomes a call of a small program, chosen by Jev, TypeSafe AI's classifier, and run only when it is sure enough. Reflexes are recipes anyone can write, share and improve. A CLI you talk to, a package manager for reflexes from git, and a TypeScript SDK.
  <sub>`Project` · ★10+ · evoke-build · `Rs` · call site [`crates/evoke-adapters/src/systemone.rs`](https://github.com/evoke-build/evoke/blob/HEAD/crates/evoke-adapters/src/systemone.rs), read 2026-09-24</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — A Home Assistant integration: typed answers about the house as sensors, noul, choice and score actions for automations, and a conversation agent.
  <sub>`Integration` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · call site [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py), read 2026-09-30 · ⚠ `AI-written` `self-submitted`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and safe orchestration. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · forvela · `JS` · call site [`src/decision.js`](https://github.com/forvela/jev-agent-browser/blob/HEAD/src/decision.js), read 2026-09-22</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · smkrv · `TS` · call site [`src/client.ts`](https://github.com/smkrv/jev-calibrate/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and OpenCode: typed classify, check, score, rank, and ask, plus one-command setup. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · francoischastel · `TS` · call site [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts), read 2026-09-22</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · goodrahstar · `JS` · call site [`lib/racers.mjs`](https://github.com/goodrahstar/jev-column-race/blob/HEAD/lib/racers.mjs), read 2026-09-22</sub>

- **[jev-gmail-ai-spam-filter-and-labeling](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling)** — Self-hosted AI email classifier for Gmail powered by Jev. Create custom labels, organize your inbox, and filter spam with confidence and cost controls. <sub>(earlier upstream description)</sub>
  <sub>`Project` · ★10+ · ilyamk · `JS` · call site [`CODE.gs`](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling/blob/HEAD/CODE.gs), read 2026-09-24</sub>

- **[jev-guard](https://github.com/klauswg/jev-guard)** — Real-time risk triage gateway for exchange deposits and withdrawals — Jev (TypeSafe System One) handles triage only; adjudication stays in deterministic code. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · klauswg · `Java` · call site [`src/main/java/com/jevguard/eval/EvalRunner.java`](https://github.com/klauswg/jev-guard/blob/HEAD/src/main/java/com/jevguard/eval/EvalRunner.java), read 2026-09-24</sub>

- **[jev-ids](https://github.com/jev-sec/jev-ids)** — Blazing-Fast Token-Efficient Intrusion Detection System (IDS) based on TypeSafe's Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jev-ids · `Py` · call site [`jev_ids/detectors/jev.py`](https://github.com/jev-sec/jev-ids/blob/HEAD/jev_ids/detectors/jev.py), read 2026-09-24</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · parth-kp · `Py` · call site [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py), read 2026-09-22</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — An MCP server exposing classify, score, check, match and screen to any agent.
  <sub>`Plugin` · ★10+ · blakestone-x · `Py` · call site [`jev_mcp/client.py`](https://github.com/blakestone-x/jev-mcp/blob/HEAD/jev_mcp/client.py), read 2026-09-22</sub>

- **[jev-poly-crypto-demo](https://github.com/frankda/jev-poly-crypto-demo)** — A research tool for Polymarket's five-minute BTC Up/Down markets: live market data becomes Jev class scores, independent logic decides, and a dashboard shows it. Paper trading only; it never connects a wallet.
  <sub>`Project` · ★10+ · frankda · `TS` · call site [`scripts/check-jev.ts`](https://github.com/frankda/jev-poly-crypto-demo/blob/HEAD/scripts/check-jev.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · kbhuw · `JS` · call site [`dist/server.mjs`](https://github.com/kbhuw/jev-sift/blob/HEAD/dist/server.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · reachjalil · `TS` · call site [`benchmarks/run.mjs`](https://github.com/reachjalil/jev-tree/blob/HEAD/benchmarks/run.mjs), read 2026-09-22</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — Answers one question over a pile of text — tickets, reviews, logs — by packing many items into each request, and reports 32x the throughput of one request per item at 41% lower cost.
  <sub>`Project` · ★10+ · collapseindex · `Py` · call site [`src/jev_ultralightspeed/_settings.py`](https://github.com/collapseindex/jev-ultralightspeed/blob/HEAD/src/jev_ultralightspeed/_settings.py), read 2026-09-24 · ⚠ `unverified claims`</sub>

- **[JevBystander](https://github.com/Nisaka520/JevBystander)** — An Android accessibility reader for WeChat: it only reads the screen and pops three toasts — intent, emotion, urgency, a suggestion — and never writes or sends a reply. No third-party dependencies; an 861 KB APK.
  <sub>`Project` · ★10+ · nisaka520 · `Kt` · call site [`app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt`](https://github.com/Nisaka520/JevBystander/blob/HEAD/app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt), read 2026-09-24</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-language questions and full probabilities using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ktaletsk · `Py` · call site [`src/jevframe/_engine.py`](https://github.com/ktaletsk/jevframe/blob/HEAD/src/jevframe/_engine.py), read 2026-09-22</sub>

- **[JevIntent](https://github.com/Nisaka520/JevIntent)** — A WeChat plugin (FkWeChat): long-press a message to analyse its intent, emotion and a suggested reply stance, shown only as a local hint the sender never sees.
  <sub>`Project` · ★10+ · nisaka520 · `Java` · call site [`main.java`](https://github.com/Nisaka520/JevIntent/blob/HEAD/main.java), read 2026-09-24</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · reachjalil · `JS` · call site [`benchmarks/pager/run-jev-v2.mjs`](https://github.com/reachjalil/jevlogs/blob/HEAD/benchmarks/pager/run-jev-v2.mjs), read 2026-09-22</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — grep for what code does: one Noul per code chunk, diff hunk or CSV row, printed as file:line hits with probabilities. --diff gates a PR in CI on a rule written in English (exit 0 match / 1 clean / 2 error); --tests lists the test files a diff can affect.
  <sub>`Project` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · call site [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts), read 2026-09-23 · ⚠ `unverified claims` `self-submitted`</sub>

- **[lkclean](https://github.com/stefw/lkclean)** — Chrome extension that cleans up your LinkedIn feed: hides engagement bait, self-promo and off-topic posts using Jev, TypeSafe AI's typed classification model — and explains every decision. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · stefw · `TS` · call site [`src/jev.ts`](https://github.com/stefw/lkclean/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — A local, offline System One server compatible with TypeSafe's Jev API. It answers typed yes/no, category and score questions with small open models. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · amithgc · `Py` · call site [`src/local_jev/ui/app.js`](https://github.com/amithgc/local-jev/blob/HEAD/src/local_jev/ui/app.js), read 2026-09-22</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · giuliosmall · `C` · call site [`sql/typesafe.sql`](https://github.com/giuliosmall/pg_typesafe/blob/HEAD/sql/typesafe.sql), read 2026-09-22</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines.
  <sub>`Plugin` · ★10+ · `Py` · `sh` · `choice` · `score` · `noul` · call site [`src/reflex_guard/providers/typesafe.py`](https://github.com/sharziki/semdecide/blob/HEAD/src/reflex_guard/providers/typesafe.py), read 2026-09-22</sub>

- **[sharp](https://github.com/tshmieldev/sharp)** — Filter your X.com feed with Jev or any LLM <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · tshmieldev · `TS` · call site [`src/common/settings.ts`](https://github.com/tshmieldev/sharp/blob/HEAD/src/common/settings.ts), read 2026-09-24</sub>

- **[sift](https://github.com/bohutang/sift)** — Chrome extension that labels every post on X (Substance · Humor · Chit-chat · Promo · Junk · AI-written) with TypeSafe Jev, and hides the ones you don't want. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · bohutang · `JS` · call site [`background.js`](https://github.com/bohutang/sift/blob/HEAD/background.js), read 2026-09-22</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — A Chrome extension that asks whether a DOM element is an advert.
  <sub>`Project` · ★10+ · realzachi · `JS` · call site [`src/typesafe.js`](https://github.com/realZachi/typesafe-adblock/blob/HEAD/src/typesafe.js), read 2026-09-22 · ⚠ `one commit`</sub>

- **[wechat-jev-assistant](https://github.com/yushen100/wechat-jev-assistant)** — A Windows WeChat conversation assistant: reads chats locally, redacts them, has TypeSafe Jev judge them, and keeps an encrypted history.
  <sub>`Project` · ★10+ · yushen100 · `Py` · call site [`src/wechat_jev/typesafe_client.py`](https://github.com/yushen100/wechat-jev-assistant/blob/HEAD/src/wechat_jev/typesafe_client.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · oso95 · `TS` · call site [`src/shared/jev.ts`](https://github.com/oso95/x-scanner/blob/HEAD/src/shared/jev.ts), read 2026-09-22</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server: a decision layer for coding agents, built on TypeSafe Jev (System One model). Ship gates, risk checks, file triage that keeps files out of context, and a safe headless browser, with calibrated confidence. For Claude Code, Codex, Cursor. <sub>(upstream description)</sub>
  <sub>`Plugin` · abhishekswe · `TS` · call site [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts), read 2026-09-22</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — AGI JEV Detection — local AI agent monitor: chain-level malicious-agent detection (TypeSafe Jev + Sentinel), escalate-only L1–L5 containment, Neo4j forensics, AngryRobot dashboard. HackSpain 2026. <sub>(upstream description)</sub>
  <sub>`Project` · carlosedm10 · `Py` · call site [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — Classify an artist's discography by theme, mood, and lyrical complexity with Jev (TypeSafe AI), and view it as a colorful terminal dashboard <sub>(upstream description)</sub>
  <sub>`Project` · lirantal · `JS` · call site [`src/jev.ts`](https://github.com/lirantal/discoprint/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrated probabilities (noul/choice/score) for routing/triage/guardrail judgments, no text generation. 把 TypeSafe Jev 决策模型注册为 DSH agent 工具 <sub>(upstream description)</sub>
  <sub>`Plugin` · nanami-0713 · `JS` · call site [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[DuoMind](https://github.com/j1s4nn/duomind)** — OpenAI-compatible local server that pairs a small llama.cpp model with Jev: 18 decision points before, during and after generation (needs reasoning, safety, format, should stop, needs retry) steer the local model. Prompts go to TypeSafe; generation stays local. <sub>(written by a model)</sub>
  <sub>`Project` · j1s4nn · `Py` · `noul` · `choice` · call site [`src/duomind/jev_client.py`](https://github.com/j1s4nn/duomind/blob/HEAD/src/duomind/jev_client.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — This repository contains a GitHub issue classifier built on Jev, TypeSafe AI's System One model. It labels every new issue with typed values and calibrated confidence in milliseconds, labelling what it is sure about and escalating what it is not. Three guardrail layers guard every write, and a
  <sub>`Project` · kalyanm45 · `Py` · call site [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[grev](https://github.com/aurorainfra/grev)** — Unix filters that ask questions instead of matching patterns: `grev 'is a vegan meal' menu.txt` keeps the lines Jev says yes to, with related tools that use a choice's confidence or a path score. Pins jev-1.13.0 because thresholds are tuned per model version. <sub>(written by a model)</sub>
  <sub>`Project` · aurorainfra · `Go` · call site [`internal/jev/price.go`](https://github.com/aurorainfra/grev/blob/HEAD/internal/jev/price.go), read by a model 2026-10-24</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — A text-moderation demo: one systemOne call screens seven Noul hazards and one severity Score in parallel, and the verdict is computed in code from policy thresholds.
  <sub>`Project` · norbertbodziony · `TS` · call site [`app/api/moderate/route.ts`](https://github.com/NorbertBodziony/guard-jev/blob/HEAD/app/api/moderate/route.ts), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[himalaya-jev-mail-classify](https://github.com/initrd/himalaya-jev-mail-classify)** — Label and prioritise Gmail with a language model. Reads mail through himalaya, classifies each thread with Jev (TypeSafe) over OpenRouter, and applies Gmail labels and colours. Dry run by default, idempotent, no state file. <sub>(upstream description)</sub>
  <sub>`Project` · initrd · `Py` · call site [`mail_classify.py`](https://github.com/initrd/himalaya-jev-mail-classify/blob/HEAD/mail_classify.py), read 2026-09-24</sub>

- **[hunch](https://github.com/steven-shoemaker/hunch)** — Ask Jev over columns of data: closed-set questions, cached and joined back. <sub>(upstream description)</sub>
  <sub>`Project` · steven-shoemaker · `Py` · call site [`src/hunch/client.py`](https://github.com/steven-shoemaker/hunch/blob/HEAD/src/hunch/client.py), read 2026-09-24</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — Issue triage that stays quiet when it isn't sure. Calibrated labels, spam and duplicate detection — with abstention. <sub>(upstream description)</sub>
  <sub>`Project` · emreozyoruk · `JS` · call site [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.
  <sub>`Project` · Really Artificial · `JS` · `choice` · `score` · `noul` · call site [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs), read 2026-09-22 · ⚠ `AI-written`</sub>

- **[Jev Playwright](https://github.com/arthurfiorette/jev-playwright)** — Playwright reporter that asks Jev which existing end-to-end tests a code change could affect and skips the clearly unrelated ones before any browser starts. Sends changed paths, patches and test bodies by default; its README warns it can miss affected tests. <sub>(written by a model)</sub>
  <sub>`Project` · arthurfiorette · `TS` · call site [`src/config.ts`](https://github.com/arthurfiorette/jev-playwright/blob/HEAD/src/config.ts), read by a model 2026-10-24</sub>

- **[JEV Sees](https://github.com/CharlesFeng0314/JEV_sees)** — Gives Jev vision: local Florence-2 and CLIP models find the objects in an image, video or RGB-D frame and keep their IDs across frames, then Jev answers a choice, noul or score about each relevant object (bus colour, pedestrian risk, animal motion). <sub>(written by a model)</sub>
  <sub>`Project` · charlesfeng0314 · `Py` · `choice` · `noul` · `score` · call site [`jev_sees/session.py`](https://github.com/CharlesFeng0314/JEV_sees/blob/HEAD/jev_sees/session.py), read by a model 2026-10-24</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能 <sub>(upstream description)</sub>
  <sub>`Plugin` · yuyang2230 · `Py` · call site [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py), read 2026-09-22</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on. <sub>(upstream description)</sub>
  <sub>`Benchmark` · themsquared · `Py` · call site [`bench.py`](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py), read 2026-09-24</sub>

- **[jev-chess](https://github.com/hemanth/jev-chess)** — Chess moves, evaluations, persona opponents, and game classification with TypeSafe AI System One <sub>(upstream description)</sub>
  <sub>`Project` · hemanth · `TS` · call site [`src/typeSafeClient.ts`](https://github.com/hemanth/jev-chess/blob/HEAD/src/typeSafeClient.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-clean](https://github.com/Kunyanli230/jev-clean)** — decision-first data cleaning system powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · kunyanli230 · `Py` · call site [`src/idac/typesafe_client.py`](https://github.com/Kunyanli230/jev-clean/blob/HEAD/src/idac/typesafe_client.py), read 2026-09-24</sub>

- **[Jev-Code-Reviewer](https://github.com/egma-ai/jev-code-reviewer)** — Local reviewer for coding agents' pull requests: each change is classified P0, P1 or P2 by Jev choices against a written priority policy, and only P0 changes are shown by default. Posts nothing to GitHub. <sub>(written by a model)</sub>
  <sub>`Project` · egma-ai · `JS` · `choice` · call site [`src/providers.mjs`](https://github.com/egma-ai/jev-code-reviewer/blob/HEAD/src/providers.mjs), read by a model 2026-10-24</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model. <sub>(upstream description)</sub>
  <sub>`Project` · charlyhno-eng · `TS` · call site [`server/classification-cache.ts`](https://github.com/Charlyhno-eng/jev-document-classification/blob/HEAD/server/classification-cache.ts), read 2026-09-22</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels <sub>(upstream description)</sub>
  <sub>`Project` · inanna-malick · `Hs` · call site [`scripts/curate-fixtures.py`](https://github.com/inanna-malick/jev-dsl/blob/HEAD/scripts/curate-fixtures.py), read 2026-09-22</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost
  <sub>`Benchmark` · 4esv · `Py` · call site [`evaljev/runners.py`](https://github.com/4esv/jev-eval/blob/HEAD/evaljev/runners.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-eval](https://github.com/onlyoneaman/jev-eval)** — TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts <sub>(upstream description)</sub>
  <sub>`Benchmark` · onlyoneaman · `TS` · call site [`jev_eval/backends.py`](https://github.com/onlyoneaman/jev-eval/blob/HEAD/jev_eval/backends.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies. <sub>(upstream description)</sub>
  <sub>`Project` · foadsf · `Py` · call site [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/HEAD/jev.py), read 2026-09-22</sub>

- **[jev-issue-radar](https://github.com/Patrick-SCH03/jev-issue-radar)** — GitHub issue triage with side-by-side evidence. Try the public sample without setup, or run the local app with TypeSafe Jev via OpenRouter. <sub>(upstream description)</sub>
  <sub>`Project` · patrick-sch03 · `JS` · call site [`lib/jev.mjs`](https://github.com/Patrick-SCH03/jev-issue-radar/blob/HEAD/lib/jev.mjs), read 2026-09-22</sub>

- **[jev-labeler-action](https://github.com/yamadashy/jev-labeler-action)** — Zero-config AI issue labeling with TypeSafe's Jev. No generated text. Unofficial. <sub>(upstream description)</sub>
  <sub>`Project` · yamadashy · `TS` · call site [`src/jev/client.ts`](https://github.com/yamadashy/jev-labeler-action/blob/HEAD/src/jev/client.ts), read 2026-09-24</sub>

- **[jev-linkedin-slop-filter](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter)** — Slams a BAIT, CORP or BRAG stamp onto LinkedIn engagement-bait, judged live by Jev (TypeSafe System One). <sub>(upstream description)</sub>
  <sub>`Project` · arpit-khandelwal · `JS` · call site [`server/jev.js`](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter/blob/HEAD/server/jev.js), read 2026-09-24</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed. <sub>(upstream description)</sub>
  <sub>`Project` · jyatesdotdev · `Py` · call site [`logtriage/cli.py`](https://github.com/jyatesdotdev/jev-logtriage/blob/HEAD/logtriage/cli.py), read 2026-09-22</sub>

- **[jev-mail](https://github.com/muhammedilyasy/jev-mail)** — Chrome extension that triages Gmail with TypeSafe's Jev model: category, priority, spam % and reply % on every email. <sub>(upstream description)</sub>
  <sub>`Plugin` · muhammedilyasy · `JS` · call site [`src/common/jev.js`](https://github.com/muhammedilyasy/jev-mail/blob/HEAD/src/common/jev.js), read 2026-09-24</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — MCP server for Jev (TypeSafe System One): the three official question types — choice, score, noul — plus batch classify. Calibrated probabilities, ~0.5s, <$0.001/call. <sub>(upstream description)</sub>
  <sub>`Plugin` · wangkuangkuang · `Py` · call site [`src/jev_mcp_server/config.py`](https://github.com/wangkuangkuang/jev-mcp-server/blob/HEAD/src/jev_mcp_server/config.py), read 2026-09-22</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no d
  <sub>`Project` · ddfeyes · `Py` · call site [`src/jev_mode/client.py`](https://github.com/ddfeyes/jev-mode/blob/HEAD/src/jev_mode/client.py), read 2026-09-22</sub>

- **[jev-organize](https://github.com/nexibeo/jev-organize)** — Throw in a pile of company files and get them classified and organized by department, type, sensitivity, date, counterparty and PII, with an index for AI agents. Powered by TypeSafe's Jev on OpenRouter (17¢ per 1,000 files). Zero-dependency Node CLI + Claude skill + Codex agent. <sub>(upstream description)</sub>
  <sub>`Plugin` · nexibeo · `JS` · call site [`skills/jev-organize/scripts/src/jev.mjs`](https://github.com/nexibeo/jev-organize/blob/HEAD/skills/jev-organize/scripts/src/jev.mjs), read 2026-09-24</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent. <sub>(upstream description)</sub>
  <sub>`Plugin` · krw82 · `TS` · call site [`src/jev/client.ts`](https://github.com/krw82/jev-playwright-mcp/blob/HEAD/src/jev/client.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-pr-labeler](https://github.com/1jehuang/jev-pr-labeler)** — Semantic GitHub PR labels using Jev's typed decisions, with conceptual scope instead of line counts <sub>(upstream description)</sub>
  <sub>`Project` · 1jehuang · `Py` · call site [`jev_labeler/classifier.py`](https://github.com/1jehuang/jev-pr-labeler/blob/HEAD/jev_labeler/classifier.py), read 2026-09-24</sub>

- **[jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline)** — Daily research monitor for standing questions: deterministic Python owns the loop, TypeSafe Jev screens sources per question, Qwen writes the notes (pilot) <sub>(earlier upstream description)</sub>
  <sub>`Project` · shimo4228 · `Py` · call site [`src/jev_research_pipeline/jev/core.py`](https://github.com/shimo4228/jev-research-pipeline/blob/HEAD/src/jev_research_pipeline/jev/core.py), read 2026-09-24</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Plugin` · vicente-md · `Java` · call site [`src/main/java/ai/jev/resilience/client/dto/JevRequest.java`](https://github.com/Vicente-MD/jev-resilience/blob/HEAD/src/main/java/ai/jev/resilience/client/dto/JevRequest.java), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model. <sub>(upstream description)</sub>
  <sub>`Project` · fatwang2 · `JS` · call site [`src/jev.mjs`](https://github.com/fatwang2/jev-review-action/blob/HEAD/src/jev.mjs), read 2026-09-22</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets <sub>(upstream description)</sub>
  <sub>`Benchmark` · teyhouse · `Py` · call site [`main.py`](https://github.com/teyhouse/jev-secret-detection/blob/HEAD/main.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-skip](https://github.com/valentynkit/jev-skip)** — Skips video sponsor segments by reading the captions and deciding at watch time.
  <sub>`Project` · valentynkit · `TS` · call site [`lib/jev.ts`](https://github.com/valentynkit/jev-skip/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[jev-slop-guard](https://github.com/davertor/jev-slop-guard)** — Jev Slop Guard — a Chrome extension that scores and stamps AI slop on your X and LinkedIn feeds as you scroll <sub>(upstream description)</sub>
  <sub>`Plugin` · davertor · `JS` · call site [`lib/jev.ts`](https://github.com/davertor/jev-slop-guard/blob/HEAD/lib/jev.ts), read 2026-09-24</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next <sub>(upstream description)</sub>
  <sub>`Benchmark` · sypherin · `Py` · call site [`jev_client.py`](https://github.com/sypherin/jev-trace-classifier/blob/HEAD/jev_client.py), read 2026-09-22</sub>

- **[jev-triage](https://github.com/cephalization/jev-triage)** — Uses typeful jev, zero sync to pull and sync large repositories for issue triage <sub>(earlier upstream description)</sub>
  <sub>`Project` · cephalization · `TS` · call site [`apps/api/src/worker/typesafe.ts`](https://github.com/cephalization/jev-triage/blob/HEAD/apps/api/src/worker/typesafe.ts), read 2026-09-22</sub>

- **[Jevatar](https://github.com/AppChainAI/Jevatar)** — An AI companion that replies only with facial expressions. Jev (TypeSafe System One) judges your message and picks 1 of 14 moods; blobatar morphs its face. React + Vite + Bun. <sub>(upstream description)</sub>
  <sub>`Project` · appchainai · `TS` · call site [`server.ts`](https://github.com/AppChainAI/Jevatar/blob/HEAD/server.ts), read 2026-09-24</sub>

- **[jevbench](https://github.com/GautamTalksDev/jevbench)** — Preregistered, bias-corrected test of TypeSafe Jev's calibration under human disagreement (ChaosNLI, 100 labels per item) <sub>(upstream description)</sub>
  <sub>`Benchmark` · Gautam Khosla · `Py` · `choice` · `noul` · call site [`jevbench/clients/jev.py`](https://github.com/GautamTalksDev/jevbench/blob/HEAD/jevbench/clients/jev.py) · author's conclusion: mixed (author-stated, not reproduced here) · ⚠ `AI-written` `self-submitted`</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — Text extraction with Jev: field extraction, PII detection and exact quotes, built on TypeSafe's Jev. <sub>(upstream description)</sub>
  <sub>`Project` · jkrup · `JS` · call site [`src/client.mjs`](https://github.com/jkrup/jeveryword/blob/HEAD/src/client.mjs), read 2026-09-22</sub>

- **[JevEye](https://github.com/Adityakhalkar/JevEye)** — Ask Jev about an image. A CNN reports what it sees with a calibrated confidence or an abstention; Jev judges what it means. <sub>(upstream description)</sub>
  <sub>`Project` · adityakhalkar · `TS` · call site [`src/lib/jev.ts`](https://github.com/Adityakhalkar/JevEye/blob/HEAD/src/lib/jev.ts), read 2026-09-24</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you own. Discord/Telegram/Reddit bots, CLI, Python, npm, HTTP API, MCP. <sub>(upstream description)</sub>
  <sub>`Plugin` · ohernandezdev · `Py` · call site [`jevmod/judge.py`](https://github.com/ohernandezdev/jevmod/blob/HEAD/jevmod/judge.py), read 2026-09-24</sub>

- **[Jevstiller](https://github.com/tomerglick57/Jevstiller)** — Proxy in front of a repeated Jev classification call: it forwards to Jev at first, trains a small local model on Jev's own answers and probabilities, and answers locally once it agrees with Jev on held-out traffic. The author reports 61.7% of Banking77 answered locally at 99.4% agreement. <sub>(written by a model)</sub>
  <sub>`Project` · tomerglick57 · `Py` · `choice` · `noul` · call site [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/HEAD/jevstiller/teachers/jev.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[JevT++](https://github.com/wiatrM/jevtpp)** — C++20 library that turns runtime text, JSON or objects into enums, booleans and scores through compile-time schemas, with full distributions and explicit abstention. Runs local Laya models in-process (ONNX Runtime or ggml) or Jev through an opt-in remote backend; latency metrics and a Mario demo. <sub>(written by a model)</sub>
  <sub>`SDK` · wiatrm · `C++` · call site [`include/jevt/remote.hpp`](https://github.com/wiatrM/jevtpp/blob/HEAD/include/jevt/remote.hpp), read by a model 2026-10-24</sub>

- **[jevticktrouter](https://github.com/GhrezaKh74/JevTicktRouter)** — A .NET 10 and React 19 application for fast, structured AI-powered ticket triage using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ghrezakh74 · `C#` · call site [`backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs`](https://github.com/GhrezaKh74/JevTicktRouter/blob/HEAD/backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevtriage](https://github.com/sathariels/jevtriage)** — GitHub Action + CLI: triage PRs with TypeSafe Jev (ready / needs review / risky) with confidence gates and jevcheck-friendly contracts. <sub>(upstream description)</sub>
  <sub>`Project` · sathariels · `Py` · call site [`src/jevtriage/client.py`](https://github.com/sathariels/jevtriage/blob/HEAD/src/jevtriage/client.py), read 2026-09-24</sub>

- **[jlink](https://github.com/keltokhy/jlink)** — Record linkage for economists: write the match rule in plain English, get a probability per pair, audit it, cite it. Python, CLI, Stata and R. <sub>(upstream description)</sub>
  <sub>`Project` · keltokhy · `Py` · call site [`bench/local_models.py`](https://github.com/keltokhy/jlink/blob/HEAD/bench/local_models.py), read 2026-09-24</sub>

- **[metis](https://github.com/Ayush0054/metis)** — Metis: automatic GitHub issue triage powered by TypeSafe AI Jev. A reusable GitHub Action. <sub>(upstream description)</sub>
  <sub>`Project` · ayush0054 · `Py` · call site [`src/metis_triage/_triage.py`](https://github.com/Ayush0054/metis/blob/HEAD/src/metis_triage/_triage.py), read 2026-09-22</sub>

- **[mysql-ailike](https://github.com/maayanlevy/mysql-ailike)** — Natural-language row filtering for MySQL, powered by TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Plugin` · maayanlevy · `C++` · call site [`src/typesafe.h`](https://github.com/maayanlevy/mysql-ailike/blob/HEAD/src/typesafe.h), read 2026-09-24</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — n8n community node for Jev by TypeSafe AI: classify, score and check text with calibrated probabilities. Parallel requests and multi-item batching. <sub>(upstream description)</sub>
  <sub>`Project` · khmuhtadin · `TS` · call site [`nodes/JevClassification/JevClassification.node.ts`](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/HEAD/nodes/JevClassification/JevClassification.node.ts), read 2026-09-22</sub>

- **[notiq](https://github.com/chengyongru/notiq)** — Native Android notification filtering with natural-language rules, powered by Jev or self-hosted FastJev. <sub>(upstream description)</sub>
  <sub>`Project` · chengyongru · `Kt` · call site [`app/src/main/java/dev/notiq/data/Settings.kt`](https://github.com/chengyongru/notiq/blob/HEAD/app/src/main/java/dev/notiq/data/Settings.kt), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — Jev-powered model-judged permission gate for OMP (TypeSafe System One) <sub>(upstream description)</sub>
  <sub>`Project` · strml · `TS` · call site [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts), read 2026-09-22 · ⚠ `archived`</sub>

- **[one-system](https://github.com/rawwerks/one-system)** — Use local and hosted classifiers aka decision models aka Jev-like models, all through a single TypeSafe API <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · rawwerks · `TS` · cited file [`examples/public_release_review.py`](https://github.com/rawwerks/one-system/blob/HEAD/examples/public_release_review.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — Detect semantic stagnation in AI agent loops <sub>(upstream description)</sub>
  <sub>`Project` · ashutoshvjti · `TS` · call site [`experiments/jev-client.ts`](https://github.com/AshutoshVJTI/progressgate/blob/HEAD/experiments/jev-client.ts), read 2026-09-22</sub>

- **[pulselane](https://github.com/ndolinschi/pulselane)** — PulseLane — clinic triage decisions via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/pulselane/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[tab-bouncer](https://github.com/MANISH007700/tab-bouncer)** — Chrome extension that closes the tabs you don't need, judged by TypeSafe's Jev in one call. Tell it what you're doing; it shows the rest the door. <sub>(upstream description)</sub>
  <sub>`Plugin` · manish007700 · `JS` · call site [`judge.js`](https://github.com/MANISH007700/tab-bouncer/blob/HEAD/judge.js), read 2026-09-24</sub>

- **[triagedy](https://github.com/m0rphtail/triagedy)** — Alert triage as a UNIX filter: JSONL security alerts in, typed decisions out. Runs on TypeSafe Jev or a local model; policy routing stays in code. <sub>(upstream description)</sub>
  <sub>`Project` · m0rphtail · `Rs` · call site [`src/backends/jev.rs`](https://github.com/m0rphtail/triagedy/blob/HEAD/src/backends/jev.rs), read 2026-09-22</sub>

- **[twitter-jev-guard](https://github.com/qs-lll/twitter-jev-guard)** — Uses TypeSafe Jev to spot low-quality, spam and advertising posts on the X/Twitter timeline and stamps a conspicuous translucent watermark over their text.
  <sub>`Plugin` · qs-lll · `JS` · call site [`extension/background.js`](https://github.com/qs-lll/twitter-jev-guard/blob/HEAD/extension/background.js), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — Diffusion-style pixel art out of a general classifier (TypeSafe Jev): 256 parallel pixel questions + refinement passes <sub>(upstream description)</sub>
  <sub>`Project` · wizhill05 · `TS` · call site [`fix_synthesizer.py`](https://github.com/Wizhill05/typesafe-image-diffusion/blob/HEAD/fix_synthesizer.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — Three composable judgment pipelines on TypeSafe's Jev: support-ticket triage, observability alert triage, and a deploy-risk gate. <sub>(upstream description)</sub>
  <sub>`Project` · shivam2003-dev · `Py` · call site [`src/triage/mock.py`](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/HEAD/src/triage/mock.py), read 2026-09-22</sub>

- **[vibecheck](https://github.com/jlowin/vibecheck)** — Python library that turns System One calls into plain values: check (yes/no), classify (one option), label (every option that applies) and score, with thresholds, an unsure answer and batching of several questions about the same data. Works against TypeSafe or any compatible server. <sub>(written by a model)</sub>
  <sub>`SDK` · jlowin · `Py` · `noul` · call site [`src/vibecheck/backends.py`](https://github.com/jlowin/vibecheck/blob/HEAD/src/vibecheck/backends.py), read by a model 2026-10-24</sub>

- **[watfile](https://github.com/jexp/watfile)** — Text/PDF - File categorization and sorting with Typesafe AI Jev or local calibrated decision model <sub>(upstream description)</sub>
  <sub>`Project` · jexp · `Py` · call site [`src/watfile/classifier/jev.py`](https://github.com/jexp/watfile/blob/HEAD/src/watfile/classifier/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.
  <sub>`Benchmark` · ★100+ · ⚠ `no licence` `unverified claims`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.
  <sub>`Benchmark` · Lindfors</sub>

- **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)** — An ML engineer's walkthrough from the classification-task angle, which is the framing closest to what the model actually does.
  <sub>`Video` · Sam Witteveen</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified claims`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.
  <sub>`Benchmark` · Near Here</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
