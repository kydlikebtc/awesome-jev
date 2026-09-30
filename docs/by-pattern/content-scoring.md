# Content scoring

<sub>[awesome-jev](../../README.md) · [中文](content-scoring.zh-CN.md)</sub>

_Score quality, risk or relevance on an ordered scale._

Every catalogued example of this decision — 166 of them. The same rows, with caveats, are in [the index](../../README.md#content-scoring); [the site](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#content-scoring): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 2 · call site 157 · wire shape 5 · example only 0 · independent reports 9 · negative results 1 · no file cited 4. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) <sub>`Official docs` · `Py` · `choice`</sub>
- [Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) <sub>`Official docs` · `Py` · `score`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐ — Break one broad judgement into atomic scores and combine them with weights that live in your code, not in the prompt.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★100k+ · `Py` · `choice` · `score` · `noul` · call site [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py), read 2026-09-22</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.
  <sub>`Benchmark` · ★10k+ · `TS` · `choice` · call site [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js), read 2026-09-22 · author's conclusion: unfavourable (author-stated, not reproduced here) · ⚠ `shadow mode`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py), read 2026-09-22</sub>

- **[gptcache](https://github.com/zilliztech/GPTCache)** — Semantic cache for LLMs. Fully integrated with LangChain and llama_index. <sub>(upstream description)</sub>
  <sub>`Project` · ★1k+ · zilliztech · `Py` · call site [`gptcache/similarity_evaluation/jev.py`](https://github.com/zilliztech/GPTCache/blob/HEAD/gptcache/similarity_evaluation/jev.py), read 2026-09-22</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★1k+ · `Java` · `choice` · `score` · `noul` · call site [`app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/app/src/main/java/com/jev/probe/jev/JevQuestions.kt), read 2026-09-22</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — lint text in code by jev scorerer <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · mizchi · `TS` · call site [`src/jev.ts`](https://github.com/mizchi/jev-lint/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — A local-first MCP plugin for continuous code-quality review by coding agents.
  <sub>`Plugin` · ★100+ · niazmorshed2007 · `TS` · call site [`src/jev/client.ts`](https://github.com/NiazMorshed2007/jev-review/blob/HEAD/src/jev/client.ts), read 2026-09-22</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★100+ · `TS` · `choice` · `score` · `noul` · call site [`src/review/codebase-judgments.ts`](https://github.com/devagrawal09/jev-review/blob/HEAD/src/review/codebase-judgments.ts), read 2026-09-22</sub>

- **[jev-semgrep](https://github.com/uehaj/sys1grep)** — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · uehaj · `JS` · call site [`semgrep.mjs`](https://github.com/uehaj/sys1grep/blob/HEAD/semgrep.mjs), read 2026-09-22</sub>

- **[jev-seo](https://github.com/AgriciDaniel/jev-seo)** — Live SEO audit for any website from one homepage URL, judged by Jev. PDF, XLSX and Markdown reports. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · agricidaniel · `Py` · call site [`jevseo/jev.py`](https://github.com/AgriciDaniel/jev-seo/blob/HEAD/jevseo/jev.py), read 2026-09-24</sub>

- **[jevmeter](https://github.com/ChetasLua/jevmeter)** — Scores every sentence of a video and renders the result as a live meter.
  <sub>`Project` · ★100+ · chetaslua · `Py` · call site [`jevmeter/score.py`](https://github.com/ChetasLua/jevmeter/blob/HEAD/jevmeter/score.py), read 2026-09-22</sub>

- **[killmyidea](https://github.com/monteduro/killmyidea)** — Scores a startup idea across several dimensions and returns a verdict of kill, fix or ship.
  <sub>`Project` · ★100+ · `TS` · `score` · `choice` · call site [`src/lib/typesafe.ts`](https://github.com/monteduro/killmyidea/blob/HEAD/src/lib/typesafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[llm2jev](https://github.com/Yinsongxu/LLM2Jev)** — Adapt local language models into Jev-compatible structured decision engines with Choice, Score, and Noul outputs powered by prefill-only binary inference.
  <sub>`Project` · ★100+ · yinsongxu · `Py` · call site [`src/llm2jev/server/sglang_server.py`](https://github.com/Yinsongxu/LLM2Jev/blob/HEAD/src/llm2jev/server/sglang_server.py), read 2026-09-24</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — The pipe layer of an AI nervous system: one interface connecting provider neurons to an application, across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev, not text.
  <sub>`Plugin` · ★100+ · juspay · `TS` · call site [`src/lib/providers/typesafe.ts`](https://github.com/juspay/neurolink/blob/HEAD/src/lib/providers/typesafe.ts), read 2026-09-22</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js), read 2026-09-22</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★100+ · `Py` · `sh` · `choice` · `score` · `noul` · call site [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql), read 2026-09-22</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — Code quality and coverage judgements for coding agents, in Rust.
  <sub>`Project` · ★100+ · supercorp-ai · `Rs` · call site [`crates/supercov-cli/src/quality.rs`](https://github.com/supercorp-ai/supercov/blob/HEAD/crates/supercov-cli/src/quality.rs), read 2026-09-22</sub>

- **[anydecisionmodel](https://github.com/mattt/AnyDecisionModel)** — A Swift package for typed decisions from language models (probabilities, choices, and scores), with support for local MLX models and the TypeSafe Jev API. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · mattt · `Swift` · call site [`Sources/AnyDecisionModel/Models/JevDecisionModel.swift`](https://github.com/mattt/AnyDecisionModel/blob/HEAD/Sources/AnyDecisionModel/Models/JevDecisionModel.swift), read 2026-09-22</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · marissafamularo · `JS` · call site [`src/lib/typesafe.js`](https://github.com/MarissaFamularo/citation-verifier/blob/HEAD/src/lib/typesafe.js), read 2026-09-22</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — A Home Assistant integration: typed answers about the house as sensors, noul, choice and score actions for automations, and a conversation agent.
  <sub>`Integration` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · call site [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py), read 2026-09-30 · ⚠ `AI-written` `self-submitted`</sub>

- **[hookmeter-jev](https://github.com/ehui1226/hookmeter-jev)** — ⚡ Millisecond-level Viral Hook Telemetry & Co-pilot for Social Media (Chrome Extension + JEV System 1) <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · ehui1226 · `Py` · call site [`jev_mcp_server.py`](https://github.com/ehui1226/hookmeter-jev/blob/HEAD/jev_mcp_server.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge)** — Using Jev as an evaluator. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · danielgshea · `Py` · call site [`src/evals/judges/__init__.py`](https://github.com/danielgshea/jev-as-a-judge/blob/HEAD/src/evals/judges/__init__.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · smkrv · `TS` · call site [`src/client.ts`](https://github.com/smkrv/jev-calibrate/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and OpenCode: typed classify, check, score, rank, and ask, plus one-command setup. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · francoischastel · `TS` · call site [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts), read 2026-09-22</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — Curates training data: JSONL and Parquet rows are judged on quality, relevance and risk before deciding what reaches downstream training.
  <sub>`Project` · ★10+ · `Rs` · `score` · `noul` · call site [`src/client.rs`](https://github.com/AkashPriyadarshii/jev-curate/blob/HEAD/src/client.rs), read 2026-09-22</sub>

- **[jev-dataops](https://github.com/RenaGao/jev-dataops)** — An open-source JEV-powered workbench for streaming data selection, quality evaluation, automatic LoRA training and held-out model evaluation. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · renagao · `Py` · call site [`jev_dataops/jev.py`](https://github.com/RenaGao/jev-dataops/blob/HEAD/jev_dataops/jev.py), read 2026-09-24</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered by Jev
  <sub>`Project` · ★10+ · qew7 · `Rb` · call site [`lib/jev/client.rb`](https://github.com/Qew7/jev-feels/blob/HEAD/lib/jev/client.rb), read 2026-09-22</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — An open training and inference stack for Jev-style decision models. Train models to score dynamic candidate branches from a shared prefix, with support for high-cardinality choice, calibration, and fast batched inference. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · zwlijay · `Py` · cited file [`jevforge/bench_jev.py`](https://github.com/zwliJay/jev-forge/blob/HEAD/jevforge/bench_jev.py), read 2026-09-22 · ⚠ `not Jev itself` `one commit`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — An MCP server exposing classify, score, check, match and screen to any agent.
  <sub>`Plugin` · ★10+ · blakestone-x · `Py` · call site [`jev_mcp/client.py`](https://github.com/blakestone-x/jev-mcp/blob/HEAD/jev_mcp/client.py), read 2026-09-22</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★10+ · brainstormity · `Py` · `choice` · `noul` · call site [`typesafe/__init__.py`](https://github.com/brainstormity/Jev-Moderation-Bot/blob/HEAD/typesafe/__init__.py), read 2026-09-22</sub>

- **[JEV-Paper-Radar](https://github.com/Eliot5566/JEV-Paper-Radar)** — Let Jev read every new arXiv paper each morning and surface the few you should read. Plain-English interests, calibrated probabilities, ~$0.06/day, fork and go. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · eliot5566 · `Py` · call site [`paper_radar/jev.py`](https://github.com/Eliot5566/JEV-Paper-Radar/blob/HEAD/paper_radar/jev.py), read 2026-09-24</sub>

- **[jev-rs](https://github.com/yijunyu/jev-rs)** — System One judgments (noul/choice/score) from any LLM in one prefill — a Rust, Jev-compatible /v1/systemone engine <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · yijunyu · `Rs` · call site [`src/backend/typesafe.rs`](https://github.com/yijunyu/jev-rs/blob/HEAD/src/backend/typesafe.rs), read 2026-09-22</sub>

- **[jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers)** — Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · akashpriyadarshii · `TS` · call site [`scripts/serve-laya.py`](https://github.com/AkashPriyadarshii/jev-superpowers/blob/HEAD/scripts/serve-laya.py), read 2026-09-22</sub>

- **[jev-test-filter](https://github.com/mizchi/jev-test-filter)** — Score every test against a git diff with Jev, and emit the filter arguments vitest, node:test, Playwright, cargo test and go test already understand <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · mizchi · `TS` · call site [`src/jev.ts`](https://github.com/mizchi/jev-test-filter/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-yaba-wechat](https://github.com/wuxie888/jev-yaba-wechat)** — A macOS floating assistant for replying in WeChat: it reads a message's intent and communication risk, GPT drafts several replies, Jev rates the candidates, and one click fills the chosen one in. You still decide what to send.
  <sub>`Project` · ★10+ · wuxie888 · `Py` · call site [`src/judge_jev.py`](https://github.com/wuxie888/jev-yaba-wechat/blob/HEAD/src/judge_jev.py), read 2026-09-24</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ray-hughes · `Rb` · call site [`lib/jevalyn/configuration.rb`](https://github.com/Ray-Hughes/jevalyn/blob/HEAD/lib/jevalyn/configuration.rb), read 2026-09-22</sub>

- **[jevflow](https://github.com/Mawfyy/jevflow)** — Probabilistic AI decisions as composable backend primitives — typed judgments (noul/score/choice), deterministic thresholds, and explainable workflows. Powered by TypeSafe's Jev, provider-agnostic. <sub>(upstream description)</sub>
  <sub>`Integration` · ★10+ · mawfyy · `TS` · call site [`packages/provider-jev/src/index.ts`](https://github.com/Mawfyy/jevflow/blob/HEAD/packages/provider-jev/src/index.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-language questions and full probabilities using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ktaletsk · `Py` · call site [`src/jevframe/_engine.py`](https://github.com/ktaletsk/jevframe/blob/HEAD/src/jevframe/_engine.py), read 2026-09-22</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — A chatbot built on a model that cannot generate text (TypeSafe AI's Jev, driven autoregressively) <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · bewinxed · `TS` · call site [`src/jevgpt/sampler.py`](https://github.com/Bewinxed/jevgpt/blob/HEAD/src/jevgpt/sampler.py), read 2026-09-22</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · huntedman · `TS` · call site [`src/jev-client.ts`](https://github.com/iamtoomas/JevLint/blob/HEAD/src/jev-client.ts), read 2026-09-22</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · reachjalil · `JS` · call site [`benchmarks/pager/run-jev-v2.mjs`](https://github.com/reachjalil/jevlogs/blob/HEAD/benchmarks/pager/run-jev-v2.mjs), read 2026-09-22</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Local-first, SQLite receipts, zero dependencies. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · romiluz13 · `Py` · call site [`jevmory/cli.py`](https://github.com/romiluz13/jevmory/blob/HEAD/jevmory/cli.py), read 2026-09-22</sub>

- **[JevScout](https://github.com/hqman/JevScout)** — A coding-agent skill that hunts jobs on real company sites: Chrome sees and acts, Jev scores every link and posting, and the host LLM never picks what to click.
  <sub>`Plugin` · ★10+ · hqman · `Py` · call site [`jev_job_hunter/jev.py`](https://github.com/hqman/JevScout/blob/HEAD/jev_job_hunter/jev.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jsort](https://github.com/keltokhy/jsort)** — sort by meaning: order lines along a plain-English dimension, from pairwise comparisons judged by TypeSafe's Jev model <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · keltokhy · `Py` · call site [`bench/local_models.py`](https://github.com/keltokhy/jsort/blob/HEAD/bench/local_models.py), read 2026-09-24</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — A local, offline System One server compatible with TypeSafe's Jev API. It answers typed yes/no, category and score questions with small open models. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · amithgc · `Py` · call site [`src/local_jev/ui/app.js`](https://github.com/amithgc/local-jev/blob/HEAD/src/local_jev/ui/app.js), read 2026-09-22</sub>

- **[MetaCog](https://github.com/ItIsCuthNotCup/MetaCog)** — Inference-time metacognition: a small, fast judge scores a bigger model's answers and steers its reasoning; Jev is one of the judges it can use.
  <sub>`Project` · ★10+ · itiscuthnotcup · `Py` · call site [`examples/jev_best_of_n.py`](https://github.com/ItIsCuthNotCup/MetaCog/blob/HEAD/examples/jev_best_of_n.py), read 2026-09-24</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jerryfane · `TS` · call site [`src/vendor/fast-jev/request.ts`](https://github.com/jerryfane/omp-jev-compaction/blob/HEAD/src/vendor/fast-jev/request.ts), read 2026-09-22</sub>

- **[plugins](https://github.com/cline/plugins)** — Official curated plugins for Cline CLI and extensions <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · cline · `TS` · call site [`plugins/jev-browser/src/jev-model.ts`](https://github.com/cline/plugins/blob/HEAD/plugins/jev-browser/src/jev-model.ts), read 2026-09-22</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.170→0.071). Typed decisions, runs offline, no API key, no waitlist. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · rupeshpoojary9 · `Py` · cited file [`crossbench/jev_client.py`](https://github.com/rupeshpoojary9/poorjev/blob/HEAD/crossbench/jev_client.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines.
  <sub>`Plugin` · ★10+ · `Py` · `sh` · `choice` · `score` · `noul` · call site [`src/reflex_guard/providers/typesafe.py`](https://github.com/sharziki/semdecide/blob/HEAD/src/reflex_guard/providers/typesafe.py), read 2026-09-22</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — Jev-powered, rule-based grader for text files. Runs every rule against every line in parallel. No skimming, no missed lines. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · lukstei · `TS` · call site [`src/providers/jev.ts`](https://github.com/lukstei/slop-grader/blob/HEAD/src/providers/jev.ts), read 2026-09-22</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · myc0576 · `Py` · call site [`src/smartmoney_cub_harness/jev/direct.py`](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · danrwilloughby · `TS` · call site [`src/jev.ts`](https://github.com/DanRWilloughby/snifftest/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[typed-decision-bert](https://github.com/hawkymisc/typed-decision-bert)** — Unofficial PoC: a BERT-style encoder decision engine behind a typed-decision (noul / choice / score) HTTP API. Not affiliated with TypeSafe. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · hawkymisc · `Py` · call site [`src/jevbert/api/routes.py`](https://github.com/hawkymisc/typed-decision-bert/blob/HEAD/src/jevbert/api/routes.py), read 2026-09-22</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — Screen a folder of CVs with the TypeSafe Jev decision model: typed judgments, an editable policy, free re-scoring. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · gtaras7 · `TS` · call site [`cv-screen/src/cli.ts`](https://github.com/gtaras7/typesafe-jev/blob/HEAD/cv-screen/src/cli.ts), read 2026-09-22</sub>

- **[Working-Memory-Jev](https://github.com/AustinAWay/Working-Memory-Jev)** — Passage: helps educators see where instructional text may ask a learner to hold too many ideas at once, using the real Jev API to trace active groups and changes in demand.
  <sub>`Project` · ★10+ · austinaway · `Py` · call site [`backend/jev.py`](https://github.com/AustinAWay/Working-Memory-Jev/blob/HEAD/backend/jev.py), read 2026-09-24</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · oso95 · `TS` · call site [`src/shared/jev.ts`](https://github.com/oso95/x-scanner/blob/HEAD/src/shared/jev.ts), read 2026-09-22</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · compozy · `TS` · call site [`benchmarks/jev-calibrate.ts`](https://github.com/compozy/yoshi/blob/HEAD/benchmarks/jev-calibrate.ts), read 2026-09-22</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails.
  <sub>`Tutorial` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[a0-typesafe-ai](https://github.com/3clyp50/a0-typesafe-ai)** — TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards. <sub>(upstream description)</sub>
  <sub>`Project` · 3clyp50 · `Py` · call site [`tools/typesafe_query.py`](https://github.com/3clyp50/a0-typesafe-ai/blob/HEAD/tools/typesafe_query.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[ai-provider-for-jev](https://github.com/soderlind/ai-provider-for-jev)** — Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul). <sub>(upstream description)</sub>
  <sub>`Integration` · soderlind · `PHP` · call site [`src/js/client.js`](https://github.com/soderlind/ai-provider-for-jev/blob/HEAD/src/js/client.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime. <sub>(upstream description)</sub>
  <sub>`SDK` · himomohi · `Py` · call site [`src/aside_jev/jev.py`](https://github.com/himomohi/aside-jev/blob/HEAD/src/aside_jev/jev.py), read 2026-09-22</sub>

- **[ask-jev-ai](https://github.com/waynesutton/ask-jev-ai)** — A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe's judgment model, answers yes, no, or it depends in about 100 milliseconds. Every judged ask lands on the wall in realtime, with a running count toward one million, showing cost. <sub>(upstream description)</sub>
  <sub>`Project` · waynesutton · `JS` · call site [`convex/lib/typesafe.ts`](https://github.com/waynesutton/ask-jev-ai/blob/HEAD/convex/lib/typesafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[book-aurora](https://github.com/dani1005/book-aurora)** — Jev reads a whole novel in seconds. Every passage becomes a row of colour. <sub>(upstream description)</sub>
  <sub>`Project` · dani1005 · `TS` · call site [`server/jev.ts`](https://github.com/dani1005/book-aurora/blob/HEAD/server/jev.ts), read 2026-09-24</sub>

- **[clarity-judge](https://github.com/TypeSafeAI/clarity-judge)** — Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its own verdict and confidence. <sub>(upstream description)</sub>
  <sub>`Project` · bunsdev · `TS` · call site [`lib/jevClient.ts`](https://github.com/TypeSafeAI/clarity-judge/blob/HEAD/lib/jevClient.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[claude-jev](https://github.com/buchmark/claude-jev)** — Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — calibrated probabilities instead of one more opinion. <sub>(upstream description)</sub>
  <sub>`Plugin` · buchmark · `TS` · call site [`src/infrastructure/typesafe-jev.ts`](https://github.com/buchmark/claude-jev/blob/HEAD/src/infrastructure/typesafe-jev.ts), read 2026-09-24</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop hook that checks an AI assistant's claims against what it actually read this session, using TypeSafe's Jev as the judge <sub>(upstream description)</sub>
  <sub>`Plugin` · vladyslavhontar · `Py` · call site [`stop_verify.py`](https://github.com/VladyslavHontar/clear-head/blob/HEAD/stop_verify.py), read 2026-09-22</sub>

- **[decide-mcp](https://github.com/dakdevs/decide-mcp)** — Configurable decision MCP server with AI SDK, Jev, percentage scores, and bias profile routing <sub>(upstream description)</sub>
  <sub>`SDK` · dakdevs · `TS` · call site [`src/config.ts`](https://github.com/dakdevs/decide-mcp/blob/HEAD/src/config.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)** — Agent skill that spots bounded-judgment steps, tries a typed decision model (TypeSafe's Jev) first, and documents every attempt <sub>(upstream description)</sub>
  <sub>`Plugin` · harrymunro · `Py` · call site [`skills/decision-first/scripts/ask.py`](https://github.com/harrymunro/decision-first/blob/HEAD/skills/decision-first/scripts/ask.py), read 2026-09-22</sub>

- **[deslop](https://github.com/yoichiojima-2/deslop)** — Score web pages for ads, slop, SEO and second-hand content. An agent skill built on TypeSafe Jev: four probabilities per page, no verdict, the caller sets the thresholds. <sub>(upstream description)</sub>
  <sub>`Plugin` · yoichiojima-2 · `Py` · call site [`skills/deslop/jev.py`](https://github.com/yoichiojima-2/deslop/blob/HEAD/skills/deslop/jev.py), read 2026-09-24</sub>

- **[draftpulse](https://github.com/pekth/draftpulse)** — Experimental: live X draft viral scorer powered by TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · pekth · `TS` · call site [`server/analyze.ts`](https://github.com/pekth/draftpulse/blob/HEAD/server/analyze.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[dsh-jev](https://github.com/noetion/dsh-jev)** — DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers. <sub>(upstream description)</sub>
  <sub>`Project` · noetion · `TS` · call site [`src/client.ts`](https://github.com/noetion/dsh-jev/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrated probabilities (noul/choice/score) for routing/triage/guardrail judgments, no text generation. 把 TypeSafe Jev 决策模型注册为 DSH agent 工具 <sub>(upstream description)</sub>
  <sub>`Plugin` · nanami-0713 · `JS` · call site [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — Jev-judged context compaction for DeepSeek Harness: semantic tool-result pruning + deterministic receipt compaction <sub>(upstream description)</sub>
  <sub>`Project` · yangyu666 · `JS` · call site [`jev.js`](https://github.com/yangyu666/dsh-jev-prune/blob/HEAD/jev.js), read 2026-09-22</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design. <sub>(earlier upstream description)</sub>
  <sub>`Benchmark` · xienda · `JS` · call site [`lib/index.js`](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — This repository contains a GitHub issue classifier built on Jev, TypeSafe AI's System One model. It labels every new issue with typed values and calibrated confidence in milliseconds, labelling what it is sure about and escalating what it is not. Three guardrail layers guard every write, and a
  <sub>`Project` · kalyanm45 · `Py` · call site [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev)** — Compare GPT generated language with JEV structured Noul decisions on the same input. <sub>(upstream description)</sub>
  <sub>`Project` · tanaypadar · `TS` · call site [`lib/jev.ts`](https://github.com/TanayPadar/gpt-vs-jev/blob/HEAD/lib/jev.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — Judge agent steps — ok / retry / escalate / stop via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/harnessjudge/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world. <sub>(upstream description)</sub>
  <sub>`Project` · abdelstark · `TS` · call site [`apps/server/src/jev.ts`](https://github.com/AbdelStark/heist-one/blob/HEAD/apps/server/src/jev.ts), read 2026-09-22</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — Issue triage that stays quiet when it isn't sure. Calibrated labels, spam and duplicate detection — with abstention. <sub>(upstream description)</sub>
  <sub>`Project` · emreozyoruk · `JS` · call site [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[instruct-jev](https://github.com/ctaxnagomi/instruct-jev)** — INSTRUCT_JEV - TypeSafe AI Jev / System One instruction corpus (choice/noul/score), compiled by DeckerGUI. 119 rows. Mirrored on HuggingFace. <sub>(upstream description)</sub>
  <sub>`Project` · ctaxnagomi · `Py` · call site [`DeckerGUI_JEV-CorpusDGUI/build_instruct_jev.py`](https://github.com/ctaxnagomi/instruct-jev/blob/HEAD/DeckerGUI_JEV-CorpusDGUI/build_instruct_jev.py), read 2026-09-22</sub>

- **[jev-as-quant](https://github.com/jiayylu/jev-as-quant)** — Typed System-1 decisions (Laya/Jev) as the judgment layer of a quant research stack, with Claude as System 2. Requirements → design → code → experiments. <sub>(upstream description)</sub>
  <sub>`Project` · jiayylu · `Py` · call site [`src/jevquant/engines/jev.py`](https://github.com/jiayylu/jev-as-quant/blob/HEAD/src/jevquant/engines/jev.py), read 2026-09-22</sub>

- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** — A twenty-questions guesser that keeps asking until Jev's calibrated confidence crosses a threshold — or gives up and says so <sub>(upstream description)</sub>
  <sub>`Project` · mintannn · `TS` · call site [`lib/jev.ts`](https://github.com/mintannn/jev-asks-until-sure/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[jev-builder-loop](https://github.com/rainbowpuffpuff/jev-builder-loop)** — Grok skill: Jev as a judgment sensor in a builder-agent loop (priors × probabilities → next act) <sub>(upstream description)</sub>
  <sub>`Plugin` · rainbowpuffpuff · `Py` · call site [`scripts/loop.py`](https://github.com/rainbowpuffpuff/jev-builder-loop/blob/HEAD/scripts/loop.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-carryforward](https://github.com/dharun-cohere/jev-carryforward)** — What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway. <sub>(upstream description)</sub>
  <sub>`Plugin` · dharundp6 · `TS` · call site [`src/gateway.ts`](https://github.com/dharun-cohere/jev-carryforward/blob/HEAD/src/gateway.ts), read 2026-09-22</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · nikkoxgonzales · `Py` · call site [`jev_certify/analysis.py`](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py), read 2026-09-22</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — Context compaction for Hermes sessions that never summarises: every tool call is scored by TypeSafe's Jev model, stale calls are dropped, everything kept stays verbatim. <sub>(upstream description)</sub>
  <sub>`Project` · picaye · `JS` · call site [`hermes-compact.mjs`](https://github.com/picaye/jev-compaction/blob/HEAD/hermes-compact.mjs), read 2026-09-22</sub>

- **[jev-decision-lab](https://github.com/jlov7/jev-decision-lab)** — A local lab for seeing what TypeSafe's Jev judgment model does on realistic business cases: typed answers, probabilities, policy in code, receipts. <sub>(upstream description)</sub>
  <sub>`Project` · jlov7 · `Py` · call site [`jev_lab/adapters.py`](https://github.com/jlov7/jev-decision-lab/blob/HEAD/jev_lab/adapters.py), read 2026-09-22</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels <sub>(upstream description)</sub>
  <sub>`Project` · inanna-malick · `Hs` · call site [`scripts/curate-fixtures.py`](https://github.com/inanna-malick/jev-dsl/blob/HEAD/scripts/curate-fixtures.py), read 2026-09-22</sub>

- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** — open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model. AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests. Jev evaluates state and outputs calibrated probabilities. Works with Cursor, Wind
  <sub>`Plugin` · ravinder82 · `TS` · call site [`dist/index.js`](https://github.com/Ravinder82/jev-flash-router/blob/HEAD/dist/index.js), read 2026-09-22</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves. <sub>(upstream description)</sub>
  <sub>`Plugin` · rashedint32 · `JS` · call site [`lib/jev.mjs`](https://github.com/rashedInt32/jev-gates/blob/HEAD/lib/jev.mjs), read 2026-09-22</sub>

- **[jev-hooks](https://github.com/microchipgnu/jev-hooks)** — Compose typed Jev judgments as reactive semantic state in React and backend programs <sub>(upstream description)</sub>
  <sub>`Project` · microchipgnu · `TS` · call site [`src/adapters/typesafe.ts`](https://github.com/microchipgnu/jev-hooks/blob/HEAD/src/adapters/typesafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-judgment](https://github.com/HyunjunJeon/jev-judgment)** — Agent Skill: send closed coding-agent judgments to TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · hyunjunjeon · `Py` · call site [`skills/jev-judgment/scripts/jev.py`](https://github.com/HyunjunJeon/jev-judgment/blob/HEAD/skills/jev-judgment/scripts/jev.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — Benchmark-driven Jev router and judge for cost-aware, reliable LLM coding workflows <sub>(upstream description)</sub>
  <sub>`Benchmark` · erendikmenn · `Py` · call site [`src/jev_router/providers/review.py`](https://github.com/erendikmenn/jev-llm-router-benchmark/blob/HEAD/src/jev_router/providers/review.py), read 2026-09-22</sub>

- **[jev-local](https://github.com/us/jev-local)** — Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no waitlist <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · us · `Py` · cited file [`src/jevlocal/app.py`](https://github.com/us/jev-local/blob/HEAD/src/jevlocal/app.py), read 2026-09-22 · ⚠ `not Jev itself` `no licence`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — MCP server for Jev (TypeSafe System One): the three official question types — choice, score, noul — plus batch classify. Calibrated probabilities, ~0.5s, <$0.001/call. <sub>(upstream description)</sub>
  <sub>`Plugin` · wangkuangkuang · `Py` · call site [`src/jev_mcp_server/config.py`](https://github.com/wangkuangkuang/jev-mcp-server/blob/HEAD/src/jev_mcp_server/config.py), read 2026-09-22</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no d
  <sub>`Project` · ddfeyes · `Py` · call site [`src/jev_mode/client.py`](https://github.com/ddfeyes/jev-mode/blob/HEAD/src/jev_mode/client.py), read 2026-09-22</sub>

- **[jev-model-router](https://github.com/lucianfialho/jev-model-router)** — Cost-optimized OpenRouter model router using TypeSafe's Jev, with a live full-catalog scorer instead of a hardcoded model list <sub>(upstream description)</sub>
  <sub>`Project` · lucianfialho · `Py` · call site [`src/model_router/classifier.py`](https://github.com/lucianfialho/jev-model-router/blob/HEAD/src/model_router/classifier.py), read 2026-09-22</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · scienthoon · `Py` · call site [`scripts/jev_eval.mjs`](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance. <sub>(upstream description)</sub>
  <sub>`Benchmark` · yodablocks · `Py` · call site [`harness/client.py`](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py), read 2026-09-22</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev-compatible decision endpoints <sub>(upstream description)</sub>
  <sub>`Project` · dtduc-git · `Py` · call site [`scripts/refresh.py`](https://github.com/dtduc-git/jev-packs/blob/HEAD/scripts/refresh.py), read 2026-09-22</sub>

- **[jev-paper-judge](https://github.com/JacobLinCool/jev-paper-judge)** — Feedback on your paper in seconds. <sub>(upstream description)</sub>
  <sub>`Project` · jacoblincool · `TS` · call site [`scripts/lib/typesafe.mjs`](https://github.com/JacobLinCool/jev-paper-judge/blob/HEAD/scripts/lib/typesafe.mjs), read 2026-09-22</sub>

- **[jev-rl](https://github.com/Bring-AI/jev-rl)** — JEV Reinforcement Learning: four classic games trained with JEV-powered rewards, reproducible experiments and checkpoint replays. <sub>(upstream description)</sub>
  <sub>`Project` · bring-ai · `Py` · call site [`src/jev_reward/judges.py`](https://github.com/Bring-AI/jev-rl/blob/HEAD/src/jev_reward/judges.py), read 2026-09-24</sub>

- **[jev-score](https://github.com/a-Fig/jev-score)** — Local-first document evaluation workspaces powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · a-fig · `JS` · call site [`src/jev.mjs`](https://github.com/a-Fig/jev-score/blob/HEAD/src/jev.mjs), read 2026-09-22</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring <sub>(upstream description)</sub>
  <sub>`Project` · akashpriyadarshii · `Rs` · call site [`src/jev.rs`](https://github.com/AkashPriyadarshii/jev-scout/blob/HEAD/src/jev.rs), read 2026-09-22</sub>

- **[jev-seo](https://github.com/DeployMates/jev-seo)** — Audits a business website for SEO and AI-answer-engine visibility. A deterministic crawler measures each page, then one request sends Jev a batch of narrow typed questions about it, and the answers are surfaced as probabilities in a dashboard.
  <sub>`Project` · vakandi · `TS` · `choice` · `score` · `noul` · call site [`server/src/jevClient.ts`](https://github.com/DeployMates/jev-seo/blob/HEAD/server/src/jevClient.ts), read 2026-09-30 · ⚠ `code untested` `no licence` `AI-written` `self-submitted`</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — A small second eval for shadcn-ui/lint that uses TypeSafe's Jev to judge the linter's own output. <sub>(upstream description)</sub>
  <sub>`Project` · blas0 · `JS` · call site [`run-rule-cases.mjs`](https://github.com/blas0/jev-shadcn-lint-eval/blob/HEAD/run-rule-cases.mjs), read 2026-09-22</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session. <sub>(upstream description)</sub>
  <sub>`Plugin` · shivampansuriya · `JS` · call site [`src/providers/typesafe.mjs`](https://github.com/ShivamPansuriya/jev-skill-gate/blob/HEAD/src/providers/typesafe.mjs), read 2026-09-24</sub>

- **[jev-songwriter](https://github.com/beingcognitive/jev-songwriter)** — A decision model that cannot write a single note writes songs. Code computes, Jev judges, and every call is replayable. <sub>(upstream description)</sub>
  <sub>`Project` · beingcognitive · `JS` · call site [`lib/jev.js`](https://github.com/beingcognitive/jev-songwriter/blob/HEAD/lib/jev.js), read 2026-09-22</sub>

- **[Jev-test](https://github.com/WeSecureYou/Jev-test)** — A CLI and REST API that asks Jev how exposed an occupation is to AI-driven layoffs, where it is heading, how much human accountability it needs, and how resilient it is.
  <sub>`Project` · wesecureyou · `TS` · call site [`src/services/jevClient.ts`](https://github.com/WeSecureYou/Jev-test/blob/HEAD/src/services/jevClient.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next <sub>(upstream description)</sub>
  <sub>`Benchmark` · sypherin · `Py` · call site [`jev_client.py`](https://github.com/sypherin/jev-trace-classifier/blob/HEAD/jev_client.py), read 2026-09-22</sub>

- **[jev-ui](https://github.com/etweisberg/jev-ui)** — React components that resolve which component to render, how to order a list, and whether to show an affordance — from calibrated judgments returned by TypeSafe's Jev. <sub>(upstream description)</sub>
  <sub>`Project` · etweisberg · `TS` · call site [`packages/jev-ui/src/transport/live.ts`](https://github.com/etweisberg/jev-ui/blob/HEAD/packages/jev-ui/src/transport/live.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-workbench](https://github.com/molis-ai/jev-workbench)** — Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine. <sub>(upstream description)</sub>
  <sub>`Plugin` · molis-ai · `TS` · call site [`apps/server/src/provider.ts`](https://github.com/molis-ai/jev-workbench/blob/HEAD/apps/server/src/provider.ts), read 2026-09-22</sub>

- **[jev-wrapped](https://github.com/gaborishka/jev-wrapped)** — Telegram channel X-ray: Jev judges a year of posts, you get a card. One Cloudflare Worker. <sub>(upstream description)</sub>
  <sub>`Project` · gaborishka · `JS` · call site [`shared/jev.js`](https://github.com/gaborishka/jev-wrapped/blob/HEAD/shared/jev.js), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — Jevaluate: evaluate before you trust. Field notes, runnable scripts and an agent skill for TypeSafe Jev: gated evals, a browser loop, a product walk with DeepSeek vision, a UI text judge and a first-click tree test. Co-authored with Claude Fable 5.1. <sub>(upstream description)</sub>
  <sub>`Plugin` · elshinq · `JS` · call site [`scripts/jev.mjs`](https://github.com/ElshinQ/jevaluate/blob/HEAD/scripts/jev.mjs), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jevbus](https://github.com/zkjoie/jevbus)** — A streaming event bus whose routing, subscription and consumption are decided by a probabilistic judge. The reference judge is TypeSafe AI's Jev (System One) model: send it a payload and a set of typed questions, get back calibrated probabilities instead of prose. <sub>(upstream description)</sub>
  <sub>`Project` · zkjoie · `Rs` · call site [`src/jev/http.rs`](https://github.com/zkjoie/jevbus/blob/HEAD/src/jev/http.rs), read 2026-09-22</sub>

- **[jevchess](https://github.com/choxos/jevchess)** — Jev, TypeSafe's System One model, plays chess against any OpenRouter LLM, Stockfish and you. One-page web app with live moves, Jev's move probabilities, saved games and win rates. <sub>(upstream description)</sub>
  <sub>`Project` · choxos · `JS` · call site [`docs/chess-ai.js`](https://github.com/choxos/jevchess/blob/HEAD/docs/chess-ai.js), read 2026-09-22</sub>

- **[jevmetrics](https://github.com/ishantanu/jevmetrics)** — An experimental OpenTelemetry Collector processor that asks Jev how operationally valuable each metric instrument is, from its metadata, then applies deterministic policy to decide what to keep.
  <sub>`Project` · ishantanu · `Go` · call site [`internal/evaluator/jev.go`](https://github.com/ishantanu/jevmetrics/blob/HEAD/internal/evaluator/jev.go), read 2026-09-24</sub>

- **[jevmoji](https://github.com/cheeaun/jevmoji)** — Type anything. Get related emojis scored 0–3 with Jev. <sub>(upstream description)</sub>
  <sub>`Project` · cheeaun · `JS` · call site [`js/jev-chunked.js`](https://github.com/cheeaun/jevmoji/blob/HEAD/js/jev-chunked.js), read 2026-09-24</sub>

- **[jevplay](https://github.com/ndolinschi/jevplay)** — TypeSafe Jev playground — custom Choice/Score/Noul builder with live distributions <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/jevplay/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach)** — Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improving. Runs on TypeSafe's Jev model. Zero added latency. <sub>(upstream description)</sub>
  <sub>`Plugin` · crowdlinker · `TS` · call site [`src/jev.ts`](https://github.com/CrowdLinker/JevPromptCoach/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[jevriel](https://github.com/thehan-co/jevriel)** — Give your AI JEV wings. A skill and plugin to build with TypeSafe Jev, upgrade LLM-only workflows and measure the result. <sub>(upstream description)</sub>
  <sub>`Plugin` · thehan-co · `JS` · call site [`vendor/typesafe-as-a-judge/judge.mjs`](https://github.com/thehan-co/jevriel/blob/HEAD/vendor/typesafe-as-a-judge/judge.mjs), read 2026-09-22</sub>

- **[jevseek](https://github.com/morcoan/JMP)** — JMP — Joint Model Participation. A local coding workspace where Jev routes actions and OpenAI, DeepSeek, or local models generate arguments. <sub>(upstream description)</sub>
  <sub>`Project` · morcoan · `Py` · call site [`benchmarks/compare_deliberation.py`](https://github.com/morcoan/JMP/blob/HEAD/benchmarks/compare_deliberation.py), read 2026-09-22 · ⚠ `archived`</sub>

- **[jevseo](https://github.com/epergaboni/jevseo)** — Typed SEO, AEO and GEO judgments powered by Jev, a System One decision model. Code owns the rules, the model owns the meaning. <sub>(upstream description)</sub>
  <sub>`Project` · epergaboni · `TS` · call site [`src/lib/typesafe/client.ts`](https://github.com/epergaboni/jevseo/blob/HEAD/src/lib/typesafe/client.ts), read 2026-09-22</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — Sub-100ms security gate for AI agent tool calls, powered by TypeSafe's Jev (System-1) decision model. Single-request Choice/Noul/Score evaluation, dual-factor blocking matrix, calibrated-confidence routing, fail-closed parsing, zero-config local fallback. LangChain-ready. <sub>(upstream description)</sub>
  <sub>`Project` · lgy1027 · `Py` · call site [`jevshield/client.py`](https://github.com/lgy1027/jevshield/blob/HEAD/jevshield/client.py), read 2026-09-22</sub>

- **[judging-with-typesafe](https://github.com/carlsonchik/judging-with-typesafe)** — Скилл для агентов Letta: суждения по критериям через TypeSafe System One (Jev) <sub>(upstream description)</sub>
  <sub>`Project` · carlsonchik · `Py` · call site [`skills/judging-with-typesafe/scripts/typesafe.py`](https://github.com/carlsonchik/judging-with-typesafe/blob/HEAD/skills/judging-with-typesafe/scripts/typesafe.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[leanest](https://github.com/baronunread/leanest)** — Local-first test selector using Jev judgments to determine which tests are affected by a code change <sub>(upstream description)</sub>
  <sub>`Project` · baronunread · `TS` · call site [`packages/judge/src/providers/jev.ts`](https://github.com/baronunread/leanest/blob/HEAD/packages/judge/src/providers/jev.ts), read 2026-09-22</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — A Stop hook that stops your coding agent from stopping too early. Plain-language rules, judged by jev. <sub>(upstream description)</sub>
  <sub>`Plugin` · noplan-inc · `Py` · call site [`limpet.py`](https://github.com/noplan-inc/limpet/blob/HEAD/limpet.py), read 2026-09-22</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
  <sub>`Project` · wiktorb2004 · `Py` · call site [`packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py`](https://github.com/WiktorB2004/llama-index-jev/blob/HEAD/packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py), read 2026-09-22</sub>

- **[luce](https://github.com/scienthoon/luce)** — Luce: a recipe for calibrated decision models — a sentence about your task in, a small model that answers typed questions with honest probabilities out (init → synth → train → eval → serve) <sub>(upstream description)</sub>
  <sub>`Project` · scienthoon · `Py` · call site [`scripts/jev_eval.mjs`](https://github.com/scienthoon/luce/blob/HEAD/scripts/jev_eval.mjs), read 2026-09-22</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — n8n community node for Jev by TypeSafe AI: classify, score and check text with calibrated probabilities. Parallel requests and multi-item batching. <sub>(upstream description)</sub>
  <sub>`Project` · khmuhtadin · `TS` · call site [`nodes/JevClassification/JevClassification.node.ts`](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/HEAD/nodes/JevClassification/JevClassification.node.ts), read 2026-09-22</sub>

- **[n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** — n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibrated probabilities <sub>(upstream description)</sub>
  <sub>`Project` · dommonte · `TS` · call site [`nodes/TypeSafeAi/constants.ts`](https://github.com/DomMonte/n8n-nodes-typesafe-ai/blob/HEAD/nodes/TypeSafeAi/constants.ts), read 2026-09-22</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — Jev-powered model-judged permission gate for OMP (TypeSafe System One) <sub>(upstream description)</sub>
  <sub>`Project` · strml · `TS` · call site [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts), read 2026-09-22 · ⚠ `archived`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Benchmark` · zsavage8 · `Py` · call site [`scripts/run_baseline.py`](https://github.com/zsavage8/padflow-jev-evals/blob/HEAD/scripts/run_baseline.py), read 2026-09-22</sub>

- **[pagegrade](https://github.com/kitze/pagegrade)** — Grade page sections for clarity, writing and on-page SEO. WXT + TypeSafe AI Jev. <sub>(upstream description)</sub>
  <sub>`Project` · kitze · `TS` · call site [`lib/jev.ts`](https://github.com/kitze/pagegrade/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — A Jev (TypeSafe System One) permission gate for the Pi coding agent: judges every bash / write / edit call before it runs <sub>(upstream description)</sub>
  <sub>`Project` · kurihada · `TS` · call site [`src/jev.ts`](https://github.com/kurihada/pi-jev-permit/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions. <sub>(upstream description)</sub>
  <sub>`Plugin` · legacybridge-tech · `TS` · call site [`src/client.ts`](https://github.com/legacybridge-tech/pi-typesafe-jev/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[prompt2jev](https://github.com/sumleo/prompt2jev)** — Agent skill and CLI that turn natural language, an LLM prompt, or the code that runs one into a TypeSafe Jev decision: typed state, Choice/Score/Noul questions, and a runnable script <sub>(upstream description)</sub>
  <sub>`Plugin` · sumleo · `Py` · call site [`skills/prompt2jev/scripts/prompt2jev.py`](https://github.com/sumleo/prompt2jev/blob/HEAD/skills/prompt2jev/scripts/prompt2jev.py), read 2026-09-22</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — Semantic assertions for pytest: test what your LLM app's output means, judged by TypeSafe's Jev.
  <sub>`Plugin` · allebee · `Py` · call site [`src/pytest_jev/judge.py`](https://github.com/allebee/pytest-jev/blob/HEAD/src/pytest_jev/judge.py), read 2026-09-22</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · shamazharikh · `Py` · cited file [`scripts/bench_fork.py`](https://github.com/shamazharikh/qwen-rlcd/blob/HEAD/scripts/bench_fork.py), read 2026-09-22 · ⚠ `not Jev itself` `no licence`</sub>

- **[s1-rs](https://github.com/AbdelStark/s1-rs)** — Typed System One layer for Rust (Choice/Score/Noul). <sub>(upstream description)</sub>
  <sub>`Project` · abdelstark · `Rs` · call site [`crates/s1/src/typesafe_rs.rs`](https://github.com/AbdelStark/s1-rs/blob/HEAD/crates/s1/src/typesafe_rs.rs), read 2026-09-22</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One Search: navigate and trace code with TypeSafe judgments and repository evidence <sub>(upstream description)</sub>
  <sub>`Project` · cpaczek · `TS` · call site [`src/client.ts`](https://github.com/cpaczek/s1s/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town: social-deduction party game for the living room TV, moderated by TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · tpaulshippy · `Rb` · call site [`lib/shady_town/evaluator.rb`](https://github.com/tpaulshippy/shady-town/blob/HEAD/lib/shady_town/evaluator.rb), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — Open-source Chrome extension that filters AI-generated prose and ads with Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · neddes · `JS` · call site [`background.js`](https://github.com/neddes/sloppy-jevs-extension/blob/HEAD/background.js), read 2026-09-22</sub>

- **[spendbrake](https://github.com/ndolinschi/spendbrake)** — Agent budget brake — continue / downgrade_model / stop via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/spendbrake/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[system-one-gemma](https://github.com/akash-kamat/system-one-gemma)** — Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · akash-kamat · `Py` · cited file [`system_one.py`](https://github.com/akash-kamat/system-one-gemma/blob/HEAD/system_one.py), read 2026-09-22 · ⚠ `not Jev itself` `no licence`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score / Noul questions, lint them, measure on labelled data, and put calibrated thresholds in code <sub>(upstream description)</sub>
  <sub>`Plugin` · simota · `TS` · call site [`skills/tenbin/scripts/evaluate.py`](https://github.com/simota/tenbin/blob/HEAD/skills/tenbin/scripts/evaluate.py), read 2026-09-22</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Code hook <sub>(upstream description)</sub>
  <sub>`Plugin` · riskaversetech · `TS` · call site [`src/backends/typesafe.ts`](https://github.com/RiskAverseTech/toolgate/blob/HEAD/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[transcript-scorecard](https://github.com/brandonbryant12/transcript-scorecard)** — ACME live support-call scoring demo with TypeSafe AI, Effect, SQLite, React, Vite, and Turborepo <sub>(upstream description)</sub>
  <sub>`Project` · brandonbryant12 · `TS` · call site [`apps/api/src/classifier.ts`](https://github.com/brandonbryant12/transcript-scorecard/blob/HEAD/apps/api/src/classifier.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — Judge every LLM response before the user sees it. AI SDK middleware and OpenAI-compatible proxy. <sub>(upstream description)</sub>
  <sub>`Integration` · noelzappy · `TS` · call site [`src/judge/jev.ts`](https://github.com/noelzappy/tripwire/blob/HEAD/src/judge/jev.ts), read 2026-09-22</sub>

- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** — Jev-shaped typed-decision model (state + Choice/Score/Noul questions -> calibrated probabilities, one pass) on ModernBERT / DeBERTa / LLaDA-MoE, with measured latency, accuracy, calibration and training cost <sub>(upstream description)</sub>
  <sub>`Project` · kotoba-lang · `Py` · call site [`src/typed_decisions/jev_holes.py`](https://github.com/kotoba-lang/typed-decisions/blob/HEAD/src/typed_decisions/jev_holes.py), read 2026-09-22</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — Unofficial community MCP plugin for Codex and Claude Code using TypeSafe Jev for bounded routing, ranking, extraction, verification, and escalation <sub>(upstream description)</sub>
  <sub>`Plugin` · e-fl · `JS` · call site [`server/judge.mjs`](https://github.com/E-FL/typesafe-as-a-judge/blob/HEAD/server/judge.mjs), read 2026-09-22</sub>

- **[typesafe-cli](https://github.com/y0usaf/typesafe-cli)** — Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose <sub>(upstream description)</sub>
  <sub>`Project` · y0usaf · `TS` · call site [`src/cli.ts`](https://github.com/y0usaf/typesafe-cli/blob/HEAD/src/cli.ts), read 2026-09-22</sub>

- **[typesafe-demo-mcp](https://github.com/bestagentkits/typesafe-demo-mcp)** — MCP server exposing TypeSafe System One judgments (noul, choice, score) as agent tools <sub>(upstream description)</sub>
  <sub>`Plugin` · bestagentkits · `TS` · call site [`src/typesafe.ts`](https://github.com/bestagentkits/typesafe-demo-mcp/blob/HEAD/src/typesafe.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[typesafe-jev-bridge](https://github.com/RevocGG/typesafe-jev-bridge)** — Use the TypeSafe Jev decision model (System One) anywhere: zero-dependency OpenAI-compatible bridge for 9Router, Claude Code, Cursor, Cline & any OpenAI SDK. Typed yes/no, choice & score judgments via CLI or HTTP. <sub>(upstream description)</sub>
  <sub>`SDK` · revocgg · `JS` · call site [`typesafe-bridge/demo.py`](https://github.com/RevocGG/typesafe-jev-bridge/blob/HEAD/typesafe-bridge/demo.py), read 2026-09-22</sub>

- **[typesafe-local](https://github.com/aabolfazl/typesafe-local)** — Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon. <sub>(upstream description)</sub>
  <sub>`Project` · aabolfazl · `Py` · call site [`ots/server.py`](https://github.com/aabolfazl/typesafe-local/blob/HEAD/ots/server.py), read 2026-09-22</sub>

- **[typesafe-oracles](https://github.com/trophee-bot/typesafe-oracles)** — Evaluating TypeSafe's System One primitives (Choice/Score/Noul) — where a typed oracle beats an LLM call
  <sub>`Project` · trophee-bot · `JS` · call site [`probes/run-arms.mjs`](https://github.com/trophee-bot/typesafe-oracles/blob/HEAD/probes/run-arms.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase)** — Next.js UI showing off TypeSafe's System One model (Jev) — parallel Noul judgments and a Choice-based citation checker, deployable to Vercel <sub>(upstream description)</sub>
  <sub>`Project` · ashadeepa · `TS` · call site [`lib/typesafe-client.ts`](https://github.com/Ashadeepa/typesafe-showcase/blob/HEAD/lib/typesafe-client.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — Three composable judgment pipelines on TypeSafe's Jev: support-ticket triage, observability alert triage, and a deploy-risk gate. <sub>(upstream description)</sub>
  <sub>`Project` · shivam2003-dev · `Py` · call site [`src/triage/mock.py`](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/HEAD/src/triage/mock.py), read 2026-09-22</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — Using Typesafe.AI to generate diff reviews. <sub>(upstream description)</sub>
  <sub>`Project` · rbalch · `Py` · call site [`src/typesafe_review/ask.py`](https://github.com/rbalch/typesafeai-review/blob/HEAD/src/typesafe_review/ask.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[vgi-typesafe](https://github.com/Query-farm/vgi-typesafe)** — A VGI worker exposing TypeSafe System One questions (choice, noul, score) to DuckDB/SQL as LATERAL-joinable table functions <sub>(upstream description)</sub>
  <sub>`Project` · query-farm · `Py` · call site [`vgi_typesafe/typesafe_api.py`](https://github.com/Query-farm/vgi-typesafe/blob/HEAD/vgi_typesafe/typesafe_api.py), read 2026-09-22</sub>

- **[watfile](https://github.com/jexp/watfile)** — Text/PDF - File categorization and sorting with Typesafe AI Jev or local calibrated decision model <sub>(upstream description)</sub>
  <sub>`Project` · jexp · `Py` · call site [`src/watfile/classifier/jev.py`](https://github.com/jexp/watfile/blob/HEAD/src/watfile/classifier/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — Typed judgment layer for coding agents — gates from PRD to ship. Jev-ready, provider-agnostic. <sub>(upstream description)</sub>
  <sub>`Integration` · zahrannnn · `TS` · call site [`src/backends/jev.ts`](https://github.com/Zahrannnn/zcode-jev/blob/HEAD/src/backends/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified claims`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
