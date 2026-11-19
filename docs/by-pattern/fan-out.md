# Speculative fan-out

<sub>[awesome-jev](../../README.md) · [中文](fan-out.zh-CN.md)</sub>

_Pack many questions — including speculative ones — into one request and let code pick what mattered._

Every catalogued example of this decision — 54 of them. The same rows, with caveats, are in [the index](../../README.md#speculative-fan-out); [the site](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#fan-out): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 3 · call site 45 · wire shape 1 · example only 1 · independent reports 2 · negative results 0 · no file cited 7. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) <sub>`Official docs` · `Py`</sub>
- [Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) <sub>`Official docs` · `Py`</sub>
- [Quickstart](https://docs.typesafe.ai/introduction/quickstart) <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

## Examples in this repository

Code under this repository's [`examples/`](../../examples/) filed under this pattern. Each is also listed below, with its summary; [the examples' README](../../examples/README.md) says how far they have been checked.

- [Example: speculative fan-out](../../examples/03-fan-out/main.py) <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>
- [Example: three primitives in one request](../../examples/01-three-primitives/main.py) <sub>`Snippet` · `Py` · `choice` · `score` · `noul` · ⚠ `code untested`</sub>

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

- **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐ — A 13-question regulatory briefing over one long article, showing that batching every question into one call is far cheaper and faster with no change in answers.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐ — Pack many questions, including ones you may not need, into a single request and let your code decide afterwards what was relevant.
  <sub>`Official docs` · `Py`</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.
  <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★100k+ · `Py` · `choice` · `score` · `noul` · call site [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py), read 2026-09-22</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed.
  <sub>`Project` · ★10k+ · Browser Use · `Py` · `choice` · call site [`jev_ultrafast/model.py`](https://github.com/browser-use/jev-ultrafast/blob/HEAD/jev_ultrafast/model.py), read 2026-09-22 · ⚠ `vendor numbers`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction.
  <sub>`Project` · ★10k+ · `Go` · `noul` · call site [`backend/internal/pkg/typesafe/client.go`](https://github.com/Wei-Shaw/sub2api/blob/HEAD/backend/internal/pkg/typesafe/client.go), read 2026-09-22</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py), read 2026-09-22</sub>

- **[dasheng](https://github.com/wquguru/dasheng)** — Read-aloud trainer for English: a streaming ASR model transcribes, alignment picks the words that differ, and Jev judges only those, a noul on whether it is the same word, a choice of error type, and a 1–5 score of whether the sentence kept its meaning. Pronunciation is not scored. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · wquguru · `JS` · call site [`lib/jev.js`](https://github.com/wquguru/dasheng/blob/HEAD/lib/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Hey Jev](https://github.com/henryklunaris/hey-jev)** — macOS voice assistant: local Whisper transcribes a command, then one Jev request asks every question at once (category, compound or not, target, app, action, volume level) as `choice`, `noul` and `score` questions; code runs the action through AppleScript, and only general questions reach an LLM. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · henryklunaris · `Py` · `choice` · `noul` · `score` · call site [`siri.py`](https://github.com/henryklunaris/hey-jev/blob/HEAD/siri.py), read by a model 2026-10-29 · ⚠ `no licence` `3rd-party key`</sub>

- **[jev-chat-windows](https://github.com/jev-chat/jev-chat-windows)** — 微信（Windows 4.x）旁挂的回复辅助：窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动
  <sub>`Project` · ★100+ · jev-chat · `Py` · call site [`core/jev_client.py`](https://github.com/jev-chat/jev-chat-windows/blob/HEAD/core/jev_client.py), read 2026-09-22</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.
  <sub>`Project` · ★100+ · `TS` · `choice` · `noul` · call site [`apps/server/src/jev/client.ts`](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts), read 2026-09-22</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — Not Jev: a toolkit that synthesizes decision data, trains and calibrates small candidate scorers (JevForge-0.8B) and serves them behind a Jev-compatible API, first for picking the next click or form control on a web page. Its benchmark sends the same held-out choice, noul and score questions to Jev. <sub>(written by a model)</sub>
  <sub>`Jev-like alternative` · ★100+ · zwlijay · `Py` · cited file [`jevforge/bench_jev.py`](https://github.com/zwliJay/jev-forge/blob/HEAD/jevforge/bench_jev.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[jev-voice](https://github.com/kevinbadi/jev-voice)** — Voice control for the Mac: whisper.cpp transcribes locally, then one ~250 ms Jev request turns the command into an action and arguments picked from candidates code built, such as installed apps. Multi-step tasks run an agent loop on the Accessibility tree, capped at 40 actions and 80 Jev calls. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · kevinbadi · `Py` · call site [`jev_voice/config.py`](https://github.com/kevinbadi/jev-voice/blob/HEAD/jev_voice/config.py), read 2026-09-22</sub>

- **[VideoJev](https://github.com/MCG-NJU/VideoJev)** — Open System One video models that score temporal candidates and multiple-choice options for several queries over one shared video prefix, then return intervals, answers, and candidate probabilities without text generation.
  <sub>`Jev-like alternative` · ★100+ · Yuhan Zhu and collaborators · `Py` · ⚠ `not Jev itself` `code untested` `self-submitted`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scoring, and semantic predicates from SQL. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · prasanthj · `C++` · call site [`benchmarks/live.py`](https://github.com/prasanthj/duckdb-jev/blob/HEAD/benchmarks/live.py), read 2026-09-22</sub>

- **[jev-datafusion](https://github.com/parable-work/jev-datafusion)** — Rust crate that registers Jev as SQL functions in Apache DataFusion: noul, choice, score and a multi-question ask run per row, so one query can score every ticket or route a year of email at warehouse scale. Works with TypeSafe, OpenRouter or any /v1/systemone endpoint. <sub>(written by a model)</sub>
  <sub>`Integration` · ★10+ · parable-work · `Rs` · `noul` · `choice` · `score` · call site [`src/provider.rs`](https://github.com/parable-work/jev-datafusion/blob/HEAD/src/provider.rs), read by a model 2026-11-03</sub>

- **[jev-rules](https://github.com/EliaAlberti/jev-rules)** — Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · eliaalberti · `JS` · call site [`plugins/jev-rules/hooks/lib/jev.mjs`](https://github.com/EliaAlberti/jev-rules/blob/HEAD/plugins/jev-rules/hooks/lib/jev.mjs), read 2026-09-22</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · kbhuw · `JS` · call site [`dist/server.mjs`](https://github.com/kbhuw/jev-sift/blob/HEAD/dist/server.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-trades](https://github.com/zadescoxp/Jev-Trades)** — Trading bot with the all new TypeSafe AI's first system one model named as Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · zadescoxp · `Py` · call site [`pipeline/paper_trader.py`](https://github.com/zadescoxp/Jev-Trades/blob/HEAD/pipeline/paper_trader.py), read 2026-09-22</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · reachjalil · `TS` · call site [`benchmarks/run.mjs`](https://github.com/reachjalil/jev-tree/blob/HEAD/benchmarks/run.mjs), read 2026-09-22</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — Answers one question over a pile of text — tickets, reviews, logs — by packing many items into each request, and reports 32x the throughput of one request per item at 41% lower cost.
  <sub>`Project` · ★10+ · collapseindex · `Py` · call site [`src/jev_ultralightspeed/_settings.py`](https://github.com/collapseindex/jev-ultralightspeed/blob/HEAD/src/jev_ultralightspeed/_settings.py), read 2026-09-24 · ⚠ `unverified claims`</sub>

- **[Jevaro](https://github.com/columnar-tech/jevaro)** — Python batching proxy that asks Jev the same questions about many states in one client request, either concurrently or packed several to a call, and streams the answers back in input order as Apache Arrow, with Python and JavaScript readers for pandas, Polars or DuckDB. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · columnar-tech · `Py` · `JS` · `choice` · `noul` · `score` · call site [`jevaro-server/src/jevaro_server/app.py`](https://github.com/columnar-tech/jevaro/blob/HEAD/jevaro-server/src/jevaro_server/app.py), read by a model 2026-11-02</sub>

- **[jevcrawl](https://github.com/RayenMlayeh/jevcrawl)** — MCP server and CLI that crawls a website for an agent's question. Per page, one Jev request asks a `noul` for every text block (does it help answer the goal?) and two for every link (leads to the answer, or to a section about it); a last `noul` asks whether the kept excerpts fully answer the goal. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · RayenMlayeh · `Py` · `noul` · call site [`jevcrawl/decide/questions.py`](https://github.com/RayenMlayeh/jevcrawl/blob/HEAD/jevcrawl/decide/questions.py), read by a model 2026-10-28 · ⚠ `vendor numbers`</sub>

- **[JevGPT: Thinking Fast and Slow in Autonomous Research](https://github.com/sunyasheng/JevGPT)** — Research agent from arXiv 2610.18272. GPT-5.5 plans searches and writes the answer; in BrowseComp-Plus QA, Jev answers a Choice over numbered source lines (where is the answer) and a Noul (does the region address it) per document region and query, in parallel. GPT gets the original lines.
  <sub>`Project` · ★10+ · sunyasheng · `TS` · `Py` · `choice` · `noul` · call site [`runtime/pi-serini/src/extensions/jev_find_v1.ts`](https://github.com/sunyasheng/JevGPT/blob/HEAD/runtime/pi-serini/src/extensions/jev_find_v1.ts) · ⚠ `3rd-party key` `unverified claims` `self-submitted`</sub>

- **[jevocks](https://github.com/unicodeveloper/jevocks)** — Everyday Stocks Status with Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · unicodeveloper · `TS` · call site [`src/lib/classify.ts`](https://github.com/unicodeveloper/jevocks/blob/HEAD/src/lib/classify.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — A browser 1v1 FPS where every decision tick judges movement, view angle, aim, fire and jump.
  <sub>`Project` · ★10+ · `TS` · `choice` · call site [`server/src/jev.ts`](https://github.com/emrickgarrett/OneVOneJev/blob/HEAD/server/src/jev.ts), read 2026-09-22 · ⚠ `code untested` `no licence`</sub>

- **[pi-typesafe](https://github.com/DevMortimer/pi-typesafe)** — TypeSafe decisions for Pi: batched evaluation tool, terminal playground, and typed API for extension authors <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · devmortimer · `TS` · call site [`src/client.ts`](https://github.com/DevMortimer/pi-typesafe/blob/HEAD/src/client.ts), read 2026-09-24</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — Jev-powered, rule-based grader for text files. Runs every rule against every line in parallel. No skimming, no missed lines. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · lukstei · `TS` · call site [`src/providers/jev.ts`](https://github.com/lukstei/slop-grader/blob/HEAD/src/providers/jev.ts), read 2026-09-22</sub>

- **[system-one](https://github.com/sgoedecke/system-one)** — Batched single-token choice inference for open language models, compatible with TypeSafe <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · sgoedecke · `Py` · call site [`system_one/inference.py`](https://github.com/sgoedecke/system-one/blob/HEAD/system_one/inference.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails.
  <sub>`Tutorial` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[anofox-decide](https://github.com/DataZooDE/anofox-decide)** — DuckDB extension that asks decision models from SQL: noul, choice and score functions run over table rows concurrently, and decide_answers sends several questions about one text in a single request. Jev on TypeSafe is one of its remote providers. <sub>(written by a model)</sub>
  <sub>`Plugin` · DataZooDE · `C++` · `noul` · `choice` · `score` · call site [`src/decide_remote.cpp`](https://github.com/DataZooDE/anofox-decide/blob/HEAD/src/decide_remote.cpp), read by a model 2026-11-17</sub>

- **[CloakBrowser Agent](https://github.com/CloakHQ/CloakBrowser-Agent)** — Browser agent in which Jev decides every step in one request: a choice of operation plus a choice of target element for each possible operation, while the CloakBrowser stealth Chromium carries it out with human-like input; it runs as an MCP server, a CLI or a library. <sub>(written by a model)</sub>
  <sub>`Project` · CloakHQ · `Py` · `choice` · call site [`cloak_agent/model.py`](https://github.com/CloakHQ/CloakBrowser-Agent/blob/HEAD/cloak_agent/model.py), read by a model 2026-11-11</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — Asks for an operation plus a target for each operation it might have picked, so a browser step never needs a second round trip.
  <sub>`Snippet` · `Py` · `choice` · `noul` · call site [`examples/03-fan-out/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/03-fan-out/main.py), read 2026-09-22 · ⚠ `code untested`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — A minimal first call asking a choice, a score and a noul together, annotated with the asymmetries that catch people out.
  <sub>`Snippet` · `Py` · `choice` · `score` · `noul` · call site [`examples/01-three-primitives/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/01-three-primitives/main.py), read 2026-09-22 · ⚠ `code untested`</sub>

- **[jackalope](https://github.com/Jackalope-Dev/jackalope)** — A desktop workspace for coding agents, parallel Git worktrees, and code review. <sub>(upstream description)</sub>
  <sub>`Project` · jackalope-dev · `Rs` · call site [`apps/desktop/src-tauri/src/commands/jev.rs`](https://github.com/Jackalope-Dev/jackalope/blob/HEAD/apps/desktop/src-tauri/src/commands/jev.rs), read 2026-09-22</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding and REST samples asking a noul, a choice and a score in one call, with the full response including per-answer confidence.
  <sub>`Integration` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench)** — Measured: asking TypeSafe Jev N questions in one call bills the state once. 2,976 real requests, raw data, exact billing check. <sub>(upstream description)</sub>
  <sub>`Benchmark` · blowxian · `Py` · call site [`bench.py`](https://github.com/blowxian/jev-fanout-bench/blob/HEAD/bench.py), read 2026-09-24</sub>

- **[jev-guardrails](https://github.com/deepansh-saxena/jev-guardrails)** — Mock carrier support agent whose guardrails are built twice on the same 25 rules and thresholds, an LLM judge and Jev, then measured on 51 labelled cases. Jev answers in one request a noul per rule, choices of scope and desk, and allow, confirm or block for each tool call. <sub>(written by a model)</sub>
  <sub>`Benchmark` · deepansh-saxena · `Py` · `noul` · `choice` · call site [`tlife_agent/guardrails/backends/jev_backend.py`](https://github.com/deepansh-saxena/jev-guardrails/blob/HEAD/tlife_agent/guardrails/backends/jev_backend.py), read by a model 2026-11-19 · ⚠ `no licence`</sub>

- **[jev-mcp-router](https://github.com/ini8labs/jev-mcp-router)** — MCP gateway between an agent and its MCP servers: for each request it asks Jev one noul per server and per tool, in one request, and the LLM sees only the handful of tools Jev said yes to, instead of every tool schema. <sub>(written by a model)</sub>
  <sub>`Project` · ini8labs · `Py` · `noul` · call site [`jevmcp/jev.py`](https://github.com/ini8labs/jev-mcp-router/blob/HEAD/jevmcp/jev.py), read by a model 2026-11-16 · ⚠ `vendor numbers`</sub>

- **[jev-pr-judge](https://github.com/juanegido/jev-pr-judge)** — Typed verdicts on pull requests with TypeSafe System One (Jev): one parallel call, policy in code, usable as a GitHub Action <sub>(upstream description)</sub>
  <sub>`Project` · juanegido · `TS` · call site [`dist/action/index.js`](https://github.com/juanegido/jev-pr-judge/blob/HEAD/dist/action/index.js), read 2026-09-24</sub>

- **[jev-riffs](https://github.com/hazlema/jev-riffs)** — Music pattern ripper: code turns a MIDI melody into semitone intervals and mines repeating units, then one batched request asks Jev to score each candidate's significance as a motif (a score per candidate). A web UI draws the piano roll and plays each motif. <sub>(written by a model)</sub>
  <sub>`Project` · hazlema · `TS` · `score` · call site [`src/rip.ts`](https://github.com/hazlema/jev-riffs/blob/HEAD/src/rip.ts), read by a model 2026-11-16</sub>

- **[jev-switchboard](https://github.com/ZIJIAN004/jev-switchboard)** — A JEV-gated semantic communication layer for parallel coding agents. <sub>(upstream description)</sub>
  <sub>`Project` · zijian004 · `JS` · call site [`src/jev.mjs`](https://github.com/ZIJIAN004/jev-switchboard/blob/HEAD/src/jev.mjs), read 2026-09-22</sub>

- **[jevswiftsdk](https://github.com/NSStudent/JevSwiftSDK)** — Independent, unofficial and dependency-free Swift SDK for the System One API: choice, noul and score questions typed as Swift values, such as a choice over an enum, named batches answered in one call with every answer checked, retries with a policy and cancellation. iOS 15+, macOS 12+ and Linux. <sub>(written by a model)</sub>
  <sub>`SDK` · nsstudent · `Swift` · call site [`Sources/JevSwiftSDK/Configuration.swift`](https://github.com/NSStudent/JevSwiftSDK/blob/HEAD/Sources/JevSwiftSDK/Configuration.swift), read 2026-09-22</sub>

- **[JevTools](https://github.com/RileyCarney/JevTools)** — A local dashboard and CLI demo for Jev: it scores a product review with a six-question fan-out (scores, nouls and a choice) into a composite, classifies topics (choice) and runs custom decisions, logging every request and answer to a local SQLite file. <sub>(written by a model)</sub>
  <sub>`Project` · RileyCarney · `Py` · `choice` · `noul` · `score` · call site [`jev_demo.py`](https://github.com/RileyCarney/JevTools/blob/HEAD/jev_demo.py), read by a model 2026-11-13</sub>

- **[Mnemon](https://github.com/grivn/mnemon-memory-agent)** — Long-term memory agent that keeps raw, dated records and judges them when a question arrives: for every record its searches return, it asks Jev in one request whether the next reply should use it and whether a later message makes it no longer current (two nouls each). <sub>(written by a model)</sub>
  <sub>`Project` · grivn · `TS` · `noul` · call site [`plugins/dsh-mnemon-strategy-jev-optmem/src/judge.ts`](https://github.com/grivn/mnemon-memory-agent/blob/HEAD/plugins/dsh-mnemon-strategy-jev-optmem/src/judge.ts), read by a model 2026-11-16 · ⚠ `3rd-party key` `vendor numbers`</sub>

- **[Netizen](https://github.com/seheta/netizen)** — Simulates how Indonesian netizens react to a post before it goes live. In one request Jev answers, per persona such as ojol drivers or buzzers, whether they stop scrolling, what they do, where they stand and what their comment does, plus whether the post is sensitive and how far it spreads. <sub>(written by a model)</sub>
  <sub>`Project` · seheta · `Py` · `noul` · `choice` · `score` · call site [`spike/spike.py`](https://github.com/seheta/netizen/blob/HEAD/spike/spike.py), read by a model 2026-11-12</sub>

- **[pi-model-router](https://github.com/alexei-led/pi-model-router)** — Model router for the Pi coding agent that can ask a classifier registered in Pi, Jev 1.14 in its reference config, up to four choices in one request: whether the request starts a new task, which configured route fits the work underway, the task's goal and its phase. <sub>(written by a model)</sub>
  <sub>`Plugin` · alexei-led · `TS` · `choice` · cited file [`docs/examples/classifier-catalog.ts`](https://github.com/alexei-led/pi-model-router/blob/HEAD/docs/examples/classifier-catalog.ts), read by a model 2026-11-19</sub>

- **[psearch](https://github.com/komikat/psearch)** — Parallel web search for terminals and agents, with local Chromium and Jev-guided exploration. <sub>(upstream description)</sub>
  <sub>`Project` · komikat · `Py` · call site [`psearch.py`](https://github.com/komikat/psearch/blob/HEAD/psearch.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — Snake controlled by parallel Jev assessments, with one API call per game tick. <sub>(upstream description)</sub>
  <sub>`Project` · siroccomask · `Py` · call site [`jev_controller.py`](https://github.com/siroccomask/snake-jev/blob/HEAD/jev_controller.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[sqlite-jev](https://github.com/mgaitan/sqlite-jev)** — Batched natural-language judgments for SQLite, powered by TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · mgaitan · `C` · call site [`src/jev.c`](https://github.com/mgaitan/sqlite-jev/blob/HEAD/src/jev.c), read 2026-09-24 · ⚠ `no licence`</sub>

- **[trading-bot-jev](https://github.com/Spykoninho/trading-bot-jev)** — Crypto trend-following bot, paper trading by default, that has Jev read each news item: which asset it concerns (choice), its expected price impact (score), whether it is material or a hostile regulatory action (nouls), plus questions per source. Code turns these into a small bias and a buy veto. <sub>(written by a model)</sub>
  <sub>`Project` · Spykoninho · `TS` · `choice` · `score` · `noul` · call site [`src/brain.ts`](https://github.com/Spykoninho/trading-bot-jev/blob/HEAD/src/brain.ts), read by a model 2026-11-18 · ⚠ `vendor numbers`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — Diffusion-style pixel art out of a general classifier (TypeSafe Jev): 256 parallel pixel questions + refinement passes <sub>(upstream description)</sub>
  <sub>`Project` · wizhill05 · `TS` · call site [`fix_synthesizer.py`](https://github.com/Wizhill05/typesafe-image-diffusion/blob/HEAD/fix_synthesizer.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase)** — Next.js UI showing off TypeSafe's System One model (Jev) — parallel Noul judgments and a Choice-based citation checker, deployable to Vercel <sub>(upstream description)</sub>
  <sub>`Project` · ashadeepa · `TS` · call site [`lib/typesafe-client.ts`](https://github.com/Ashadeepa/typesafe-showcase/blob/HEAD/lib/typesafe-client.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — The richest Vercel walkthrough: single and multi-question calls, probability-threshold routing, and unit tests with a mock evaluation model.
  <sub>`Tutorial` · `TS` · `noul` · `choice` · `score`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
