# Content scoring

<sub>[awesome-jev](../../README.md) · [中文](content-scoring.zh-CN.md)</sub>

_Score quality, risk or relevance on an ordered scale._

Every catalogued example of this decision — 164 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#content-scoring); [the site](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=en) can filter them further by language, primitive and kind.

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐ — Break one broad judgement into atomic scores and combine them with weights that live in your code, not in the prompt.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.
  <sub>`Benchmark` · ★87,298 · `TS` · `choice` · ⚠ `shadow mode`</sub>

- **[gptcache](https://github.com/zilliztech/GPTCache)** — Semantic cache for LLMs. Fully integrated with LangChain and llama_index.
  <sub>`Project` · ★8,201 · zilliztech · `Py`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★5,414 · `Java` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★4,578 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★582 · `TS` · `choice` · `score` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★324 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[llm2jev](https://github.com/Yinsongxu/LLM2Jev)** — Adapt local language models into Jev-compatible structured decision engines with Choice, Score, and Noul outputs powered by prefill-only binary inference.
  <sub>`Project` · ★286 · yinsongxu · `Py`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — A local-first MCP plugin for continuous code-quality review by coding agents.
  <sub>`Plugin` · ★217 · niazmorshed2007 · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★173 · `JS` · `choice` · `score` · `noul`</sub>

- **[killmyidea](https://github.com/monteduro/killmyidea)** — Scores a startup idea across several dimensions and returns a verdict of kill, fix or ship.
  <sub>`Project` · ★147 · `TS` · `score` · `choice` · ⚠ `no licence`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — The pipe layer of an AI nervous system: one interface connecting provider neurons to an application, across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev, not text.
  <sub>`Plugin` · ★139 · juspay · `TS`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる
  <sub>`Project` · ★134 · uehaj · `JS`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — Code quality and coverage judgements for coding agents, in Rust.
  <sub>`Project` · ★109 · supercorp-ai · `Rs`</sub>

- **[jevmeter](https://github.com/ChetasLua/jevmeter)** — Scores every sentence of a video and renders the result as a live meter.
  <sub>`Project` · ★81 · chetaslua · `Py`</sub>

- **[jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge)** — Using Jev as an evaluator.
  <sub>`Project` · ★80 · danielgshea · `Py` · ⚠ `no licence`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — lint text in code by jev scorerer
  <sub>`Project` · ★78 · mizchi · `TS`</sub>

- **[jev-seo](https://github.com/AgriciDaniel/jev-seo)** — Live SEO audit for any website from one homepage URL, judged by Jev. PDF, XLSX and Markdown reports.
  <sub>`Project` · ★78 · agricidaniel · `Py`</sub>

- **[Working-Memory-Jev](https://github.com/AustinAWay/Working-Memory-Jev)** — Passage: helps educators see where instructional text may ask a learner to hold too many ideas at once, using the real Jev API to trace active groups and changes in demand.
  <sub>`Project` · ★75 · austinaway · `Py`</sub>

- **[jev-dataops](https://github.com/RenaGao/jev-dataops)** — An open-source JEV-powered workbench for streaming data selection, quality evaluation, automatic LoRA training and held-out model evaluation.
  <sub>`Project` · ★54 · renagao · `Py`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines.
  <sub>`Plugin` · ★53 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — Curates training data: JSONL and Parquet rows are judged on quality, relevance and risk before deciding what reaches downstream training.
  <sub>`Project` · ★45 · `Rs` · `score` · `noul`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★44 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — An open training and inference stack for Jev-style decision models. Train models to score dynamic candidate branches from a shared prefix, with support for high-cardinality choice, calibration, and fast batched inference.
  <sub>`Jev-like alternative` · ★34 · zwlijay · `Py` · ⚠ `not Jev itself`</sub>

- **[JevScout](https://github.com/hqman/JevScout)** — A coding-agent skill that hunts jobs on real company sites: Chrome sees and acts, Jev scores every link and posting, and the host LLM never picks what to click.
  <sub>`Plugin` · ★33 · hqman · `Py` · ⚠ `no licence`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial.
  <sub>`Project` · ★31 · smkrv · `TS`</sub>

- **[plugins](https://github.com/cline/plugins)** — Official curated plugins for Cline CLI and extensions
  <sub>`Plugin` · ★31 · cline · `TS`</sub>

- **[typed-decision-bert](https://github.com/hawkymisc/typed-decision-bert)** — Unofficial PoC: a BERT-style encoder decision engine behind a typed-decision (noul / choice / score) HTTP API. Not affiliated with TypeSafe.
  <sub>`Project` · ★31 · hawkymisc · `Py`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.
  <sub>`Project` · ★29 · danrwilloughby · `TS`</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — A chatbot built on a model that cannot generate text (TypeSafe AI's Jev, driven autoregressively)
  <sub>`Project` · ★26 · bewinxed · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy
  <sub>`Plugin` · ★25 · compozy · `TS`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — An MCP server exposing classify, score, check, match and screen to any agent.
  <sub>`Plugin` · ★22 · blakestone-x · `Py`</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — Jev-powered, rule-based grader for text files. Runs every rule against every line in parallel. No skimming, no missed lines.
  <sub>`Project` · ★22 · lukstei · `TS`</sub>

- **[hookmeter-jev](https://github.com/ehui1226/hookmeter-jev)** — ⚡ Millisecond-level Viral Hook Telemetry & Co-pilot for Social Media (Chrome Extension + JEV System 1)
  <sub>`Plugin` · ★21 · ehui1226 · `Py`</sub>

- **[jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers)** — Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions
  <sub>`Project` · ★21 · akashpriyadarshii · `TS`</sub>

- **[jev-yaba-wechat](https://github.com/wuxie888/jev-yaba-wechat)** — A macOS floating assistant for replying in WeChat: it reads a message's intent and communication risk, GPT drafts several replies, Jev rates the candidates, and one click fills the chosen one in. You still decide what to send.
  <sub>`Project` · ★21 · wuxie888 · `Py`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow.
  <sub>`Project` · ★19 · ray-hughes · `Rb`</sub>

- **[jsort](https://github.com/keltokhy/jsort)** — sort by meaning: order lines along a plain-English dimension, from pairwise comparisons judged by TypeSafe's Jev model
  <sub>`Project` · ★19 · keltokhy · `Py`</sub>

- **[MetaCog](https://github.com/ItIsCuthNotCup/MetaCog)** — Inference-time metacognition: a small, fast judge scores a bigger model's answers and steers its reasoning; Jev is one of the judges it can use.
  <sub>`Project` · ★18 · itiscuthnotcup · `Py`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter
  <sub>`Plugin` · ★17 · oso95 · `TS`</sub>

- **[jev-test-filter](https://github.com/mizchi/jev-test-filter)** — Score every test against a git diff with Jev, and emit the filter arguments vitest, node:test, Playwright, cargo test and go test already understand
  <sub>`Project` · ★16 · mizchi · `TS`</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and OpenCode: typed classify, check, score, rank, and ask, plus one-command setup.
  <sub>`Plugin` · ★15 · francoischastel · `TS`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-language questions and full probabilities using TypeSafe Jev.
  <sub>`Project` · ★14 · ktaletsk · `Py`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.
  <sub>`Plugin` · ★11 · huntedman · `TS`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis.
  <sub>`Project` · ★11 · reachjalil · `JS`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered by Jev
  <sub>`Project` · ★10 · qew7 · `Rb`</sub>

- **[anydecisionmodel](https://github.com/mattt/AnyDecisionModel)** — A Swift package for typed decisions from language models (probabilities, choices, and scores), with support for local MLX models and the TypeSafe Jev API.
  <sub>`Project` · ★9 · mattt · `Swift`</sub>

- **[jevflow](https://github.com/Mawfyy/jevflow)** — Probabilistic AI decisions as composable backend primitives — typed judgments (noul/score/choice), deterministic thresholds, and explainable workflows. Powered by TypeSafe's Jev, provider-agnostic.
  <sub>`Integration` · ★9 · mawfyy · `TS` · ⚠ `no licence`</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Local-first, SQLite receipts, zero dependencies.
  <sub>`Project` · ★9 · romiluz13 · `Py`</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.
  <sub>`SDK` · ★8 · himomohi · `Py`</sub>

- **[jev-rs](https://github.com/yijunyu/jev-rs)** — System One judgments (noul/choice/score) from any LLM in one prefill — a Rust, Jev-compatible /v1/systemone engine
  <sub>`Project` · ★8 · yijunyu · `Rs`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter
  <sub>`Project` · ★8 · jerryfane · `TS`</sub>

- **[typesafe-local](https://github.com/aabolfazl/typesafe-local)** — Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.
  <sub>`Project` · ★8 · aabolfazl · `Py`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides.
  <sub>`Project` · ★7 · marissafamularo · `JS`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world.
  <sub>`Project` · ★7 · abdelstark · `TS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels
  <sub>`Project` · ★7 · inanna-malick · `Hs`</sub>

- **[JEV-Paper-Radar](https://github.com/Eliot5566/JEV-Paper-Radar)** — Let Jev read every new arXiv paper each morning and surface the few you should read. Plain-English interests, calibrated probabilities, ~$0.06/day, fork and go.
  <sub>`Project` · ★7 · eliot5566 · `Py`</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — A local, offline System One server compatible with TypeSafe's Jev API. It answers typed yes/no, category and score questions with small open models.
  <sub>`Project` · ★7 · amithgc · `Py`</sub>

- **[luce](https://github.com/scienthoon/luce)** — Luce: a recipe for calibrated decision models — a sentence about your task in, a small model that answers typed questions with honest probabilities out (init → synth → train → eval → serve)
  <sub>`Project` · ★7 · scienthoon · `Py`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.170→0.071). Typed decisions, runs offline, no API key, no waitlist.
  <sub>`Jev-like alternative` · ★7 · rupeshpoojary9 · `Py` · ⚠ `not Jev itself`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · ★6 · scienthoon · `Py`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — Screen a folder of CVs with the TypeSafe Jev decision model: typed judgments, an editable policy, free re-scoring.
  <sub>`Project` · ★6 · gtaras7 · `TS`</sub>

- **[a0-typesafe-ai](https://github.com/3clyp50/a0-typesafe-ai)** — TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.
  <sub>`Project` · ★5 · 3clyp50 · `Py`</sub>

- **[book-aurora](https://github.com/dani1005/book-aurora)** — Jev reads a whole novel in seconds. Every passage becomes a row of colour.
  <sub>`Project` · ★5 · dani1005 · `TS`</sub>

- **[claude-jev](https://github.com/buchmark/claude-jev)** — Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — calibrated probabilities instead of one more opinion.
  <sub>`Plugin` · ★5 · buchmark · `TS`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session.
  <sub>`Plugin` · ★5 · shivampansuriya · `JS`</sub>

- **[jevchess](https://github.com/choxos/jevchess)** — Jev, TypeSafe's System One model, plays chess against any OpenRouter LLM, Stockfish and you. One-page web app with live moves, Jev's move probabilities, saved games and win rates.
  <sub>`Project` · ★5 · choxos · `JS`</sub>

- **[jevmoji](https://github.com/cheeaun/jevmoji)** — Type anything. Get related emojis scored 0–3 with Jev.
  <sub>`Project` · ★5 · cheeaun · `JS`</sub>

- **[jevriel](https://github.com/thehan-co/jevriel)** — Give your AI JEV wings. A skill and plugin to build with TypeSafe Jev, upgrade LLM-only workflows and measure the result.
  <sub>`Plugin` · ★5 · thehan-co · `JS`</sub>

- **[pagegrade](https://github.com/kitze/pagegrade)** — Grade page sections for clarity, writing and on-page SEO. WXT + TypeSafe AI Jev.
  <sub>`Project` · ★5 · kitze · `TS`</sub>

- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** — Jev-shaped typed-decision model (state + Choice/Score/Noul questions -> calibrated probabilities, one pass) on ModernBERT / DeBERTa / LLaDA-MoE, with measured latency, accuracy, calibration and training cost
  <sub>`Project` · ★5 · kotoba-lang · `Py`</sub>

- **[ai-provider-for-jev](https://github.com/soderlind/ai-provider-for-jev)** — Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).
  <sub>`Integration` · ★4 · soderlind · `PHP` · ⚠ `no licence`</sub>

- **[jevseo](https://github.com/epergaboni/jevseo)** — Typed SEO, AEO and GEO judgments powered by Jev, a System One decision model. Code owns the rules, the model owns the meaning.
  <sub>`Project` · ★4 · epergaboni · `TS`</sub>

- **[leanest](https://github.com/baronunread/leanest)** — Local-first test selector using Jev judgments to determine which tests are affected by a code change
  <sub>`Project` · ★4 · baronunread · `TS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
  <sub>`Project` · ★4 · wiktorb2004 · `Py`</sub>

- **[prompt2jev](https://github.com/sumleo/prompt2jev)** — Agent skill and CLI that turn natural language, an LLM prompt, or the code that runs one into a TypeSafe Jev decision: typed state, Choice/Score/Noul questions, and a runnable script
  <sub>`Plugin` · ★4 · sumleo · `Py`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B
  <sub>`Jev-like alternative` · ★4 · shamazharikh · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[system-one-gemma](https://github.com/akash-kamat/system-one-gemma)** — Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.
  <sub>`Jev-like alternative` · ★4 · akash-kamat · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[typesafe-cli](https://github.com/y0usaf/typesafe-cli)** — Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose
  <sub>`Project` · ★4 · y0usaf · `TS`</sub>

- **[dsh-jev](https://github.com/noetion/dsh-jev)** — DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.
  <sub>`Project` · ★3 · noetion · `TS`</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — Jev-judged context compaction for DeepSeek Harness: semantic tool-result pruning + deterministic receipt compaction
  <sub>`Project` · ★3 · yangyu666 · `JS`</sub>

- **[jev-as-quant](https://github.com/jiayylu/jev-as-quant)** — Typed System-1 decisions (Laya/Jev) as the judgment layer of a quant research stack, with Claude as System 2. Requirements → design → code → experiments.
  <sub>`Project` · ★3 · jiayylu · `Py`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — Context compaction for Hermes sessions that never summarises: every tool call is scored by TypeSafe's Jev model, stale calls are dropped, everything kept stays verbatim.
  <sub>`Project` · ★3 · picaye · `JS`</sub>

- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** — open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model. AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests. Jev evaluates state and outputs calibrated probabilities. Works with Cursor, Wind
  <sub>`Plugin` · ★3 · ravinder82 · `TS`</sub>

- **[jev-judgment](https://github.com/HyunjunJeon/jev-judgment)** — Agent Skill: send closed coding-agent judgments to TypeSafe Jev
  <sub>`Plugin` · ★3 · hyunjunjeon · `Py`</sub>

- **[jev-local](https://github.com/us/jev-local)** — Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no waitlist
  <sub>`Jev-like alternative` · ★3 · us · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[jev-ui](https://github.com/etweisberg/jev-ui)** — React components that resolve which component to render, how to order a list, and whether to show an affordance — from calibrated judgments returned by TypeSafe's Jev.
  <sub>`Project` · ★3 · etweisberg · `TS` · ⚠ `no licence`</sub>

- **[jevmetrics](https://github.com/ishantanu/jevmetrics)** — An experimental OpenTelemetry Collector processor that asks Jev how operationally valuable each metric instrument is, from its metadata, then applies deterministic policy to decide what to keep.
  <sub>`Project` · ★3 · ishantanu · `Go`</sub>

- **[jevseek](https://github.com/morcoan/JMP)** — JMP — Joint Model Participation. A local coding workspace where Jev routes actions and OpenAI, DeepSeek, or local models generate arguments.
  <sub>`Project` · ★3 · morcoan · `Py` · ⚠ `archived`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — A Stop hook that stops your coding agent from stopping too early. Plain-language rules, judged by jev.
  <sub>`Plugin` · ★3 · noplan-inc · `Py`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.
  <sub>`Plugin` · ★3 · legacybridge-tech · `TS`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score / Noul questions, lint them, measure on labelled data, and put calibrated thresholds in code
  <sub>`Plugin` · ★3 · simota · `TS`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — Judge every LLM response before the user sees it. AI SDK middleware and OpenAI-compatible proxy.
  <sub>`Integration` · ★3 · noelzappy · `TS`</sub>

- **[typesafe-jev-bridge](https://github.com/RevocGG/typesafe-jev-bridge)** — Use the TypeSafe Jev decision model (System One) anywhere: zero-dependency OpenAI-compatible bridge for 9Router, Claude Code, Cursor, Cline & any OpenAI SDK. Typed yes/no, choice & score judgments via CLI or HTTP.
  <sub>`SDK` · ★3 · revocgg · `JS`</sub>

- **[vgi-typesafe](https://github.com/Query-farm/vgi-typesafe)** — A VGI worker exposing TypeSafe System One questions (choice, noul, score) to DuckDB/SQL as LATERAL-joinable table functions
  <sub>`Project` · ★3 · query-farm · `Py`</sub>

- **[ask-jev-ai](https://github.com/waynesutton/ask-jev-ai)** — A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe's judgment model, answers yes, no, or it depends in about 100 milliseconds. Every judged ask lands on the wall in realtime, with a running count toward one million, showing cost.
  <sub>`Project` · ★2 · waynesutton · `JS` · ⚠ `no licence`</sub>

- **[clarity-judge](https://github.com/TypeSafeAI/clarity-judge)** — Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its own verdict and confidence.
  <sub>`Project` · ★2 · bunsdev · `TS` · ⚠ `no licence`</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop hook that checks an AI assistant's claims against what it actually read this session, using TypeSafe's Jev as the judge
  <sub>`Plugin` · ★2 · vladyslavhontar · `Py`</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)** — Agent skill that spots bounded-judgment steps, tries a typed decision model (TypeSafe's Jev) first, and documents every attempt
  <sub>`Plugin` · ★2 · harrymunro · `Py`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrated probabilities (noul/choice/score) for routing/triage/guardrail judgments, no text generation. 把 TypeSafe Jev 决策模型注册为 DSH agent 工具
  <sub>`Plugin` · ★2 · nanami-0713 · `JS`</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — Issue triage that stays quiet when it isn't sure. Calibrated labels, spam and duplicate detection — with abstention.
  <sub>`Project` · ★2 · emreozyoruk · `JS`</sub>

- **[jev-builder-loop](https://github.com/rainbowpuffpuff/jev-builder-loop)** — Grok skill: Jev as a judgment sensor in a builder-agent loop (priors × probabilities → next act)
  <sub>`Plugin` · ★2 · rainbowpuffpuff · `Py`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — MCP server for Jev (TypeSafe System One): the three official question types — choice, score, noul — plus batch classify. Calibrated probabilities, ~0.5s, <$0.001/call.
  <sub>`Plugin` · ★2 · wangkuangkuang · `Py`</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no d
  <sub>`Project` · ★2 · ddfeyes · `Py`</sub>

- **[jev-model-router](https://github.com/lucianfialho/jev-model-router)** — Cost-optimized OpenRouter model router using TypeSafe's Jev, with a live full-catalog scorer instead of a hardcoded model list
  <sub>`Project` · ★2 · lucianfialho · `Py`</sub>

- **[jev-rl](https://github.com/Bring-AI/jev-rl)** — JEV Reinforcement Learning: four classic games trained with JEV-powered rewards, reproducible experiments and checkpoint replays.
  <sub>`Project` · ★2 · bring-ai · `Py`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring
  <sub>`Project` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-workbench](https://github.com/molis-ai/jev-workbench)** — Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.
  <sub>`Plugin` · ★2 · molis-ai · `TS`</sub>

- **[jevbus](https://github.com/zkjoie/jevbus)** — A streaming event bus whose routing, subscription and consumption are decided by a probabilistic judge. The reference judge is TypeSafe AI's Jev (System One) model: send it a payload and a set of typed questions, get back calibrated probabilities instead of prose.
  <sub>`Project` · ★2 · zkjoie · `Rs`</sub>

- **[JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach)** — Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improving. Runs on TypeSafe's Jev model. Zero added latency.
  <sub>`Plugin` · ★2 · crowdlinker · `TS`</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — Sub-100ms security gate for AI agent tool calls, powered by TypeSafe's Jev (System-1) decision model. Single-request Choice/Noul/Score evaluation, dual-factor blocking matrix, calibrated-confidence routing, fail-closed parsing, zero-config local fallback. LangChain-ready.
  <sub>`Project` · ★2 · lgy1027 · `Py`</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — n8n community node for Jev by TypeSafe AI: classify, score and check text with calibrated probabilities. Parallel requests and multi-item batching.
  <sub>`Project` · ★2 · khmuhtadin · `TS`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — Semantic assertions for pytest: test what your LLM app's output means, judged by TypeSafe's Jev.
  <sub>`Plugin` · ★2 · allebee · `Py`</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Code hook
  <sub>`Plugin` · ★2 · riskaversetech · `TS`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — Unofficial community MCP plugin for Codex and Claude Code using TypeSafe Jev for bounded routing, ranking, extraction, verification, and escalation
  <sub>`Plugin` · ★2 · e-fl · `JS`</sub>

- **[watfile](https://github.com/jexp/watfile)** — Text/PDF - File categorization and sorting with Typesafe AI Jev or local calibrated decision model
  <sub>`Project` · ★2 · jexp · `Py` · ⚠ `no licence`</sub>

- **[draftpulse](https://github.com/pekth/draftpulse)** — Experimental: live X draft viral scorer powered by TypeSafe Jev
  <sub>`Project` · ★1 · pekth · `TS` · ⚠ `no licence`</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design.
  <sub>`Benchmark` · ★1 · xienda · `JS`</sub>

- **[gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev)** — Compare GPT generated language with JEV structured Noul decisions on the same input.
  <sub>`Project` · ★1 · tanaypadar · `TS`</sub>

- **[instruct-jev](https://github.com/ctaxnagomi/instruct-jev)** — INSTRUCT_JEV - TypeSafe AI Jev / System One instruction corpus (choice/noul/score), compiled by DeckerGUI. 119 rows. Mirrored on HuggingFace.
  <sub>`Project` · ★1 · ctaxnagomi · `Py`</sub>

- **[jev-carryforward](https://github.com/Dharundp6/jev-carryforward)** — What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway.
  <sub>`Plugin` · ★1 · dharundp6 · `TS`</sub>

- **[jev-hooks](https://github.com/microchipgnu/jev-hooks)** — Compose typed Jev judgments as reactive semantic state in React and backend programs
  <sub>`Project` · ★1 · microchipgnu · `TS` · ⚠ `no licence`</sub>

- **[jev-paper-judge](https://github.com/JacobLinCool/jev-paper-judge)** — Feedback on your paper in seconds.
  <sub>`Project` · ★1 · jacoblincool · `TS`</sub>

- **[jev-score](https://github.com/a-Fig/jev-score)** — Local-first document evaluation workspaces powered by Jev
  <sub>`Project` · ★1 · a-fig · `JS`</sub>

- **[jev-wrapped](https://github.com/gaborishka/jev-wrapped)** — Telegram channel X-ray: Jev judges a year of posts, you get a card. One Cloudflare Worker.
  <sub>`Project` · ★1 · gaborishka · `JS`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — Jevaluate: evaluate before you trust. Field notes, runnable scripts and an agent skill for TypeSafe Jev: gated evals, a browser loop, a product walk with DeepSeek vision, a UI text judge and a first-click tree test. Co-authored with Claude Fable 5.1.
  <sub>`Plugin` · ★1 · elshinq · `JS`</sub>

- **[judging-with-typesafe](https://github.com/carlsonchik/judging-with-typesafe)** — Скилл для агентов Letta: суждения по критериям через TypeSafe System One (Jev)
  <sub>`Project` · ★1 · carlsonchik · `Py` · ⚠ `no licence`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev.
  <sub>`Benchmark` · ★1 · zsavage8 · `Py`</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — A Jev (TypeSafe System One) permission gate for the Pi coding agent: judges every bash / write / edit call before it runs
  <sub>`Project` · ★1 · kurihada · `TS`</sub>

- **[s1-rs](https://github.com/AbdelStark/s1-rs)** — Typed System One layer for Rust (Choice/Score/Noul).
  <sub>`Project` · ★1 · abdelstark · `Rs`</sub>

- **[typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase)** — Next.js UI showing off TypeSafe's System One model (Jev) — parallel Noul judgments and a Choice-based citation checker, deployable to Vercel
  <sub>`Project` · ★1 · ashadeepa · `TS` · ⚠ `no licence`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails.
  <sub>`Tutorial` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[decide-mcp](https://github.com/dakdevs/decide-mcp)** — Configurable decision MCP server with AI SDK, Jev, percentage scores, and bias profile routing
  <sub>`SDK` · ★0 · dakdevs · `TS`</sub>

- **[deslop](https://github.com/yoichiojima-2/deslop)** — Score web pages for ads, slop, SEO and second-hand content. An agent skill built on TypeSafe Jev: four probabilities per page, no verdict, the caller sets the thresholds.
  <sub>`Plugin` · ★0 · yoichiojima-2 · `Py`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — This repository contains a GitHub issue classifier built on Jev, TypeSafe AI's System One model. It labels every new issue with typed values and calibrated confidence in milliseconds, labelling what it is sure about and escalating what it is not. Three guardrail layers guard every write, and a
  <sub>`Project` · ★0 · kalyanm45 · `Py`</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — Judge agent steps — ok / retry / escalate / stop via TypeSafe Jev
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** — A twenty-questions guesser that keeps asking until Jev's calibrated confidence crosses a threshold — or gives up and says so
  <sub>`Project` · ★0 · mintannn · `TS`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-decision-lab](https://github.com/jlov7/jev-decision-lab)** — A local lab for seeing what TypeSafe's Jev judgment model does on realistic business cases: typed answers, probabilities, policy in code, receipts.
  <sub>`Project` · ★0 · jlov7 · `Py`</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves.
  <sub>`Plugin` · ★0 · rashedint32 · `JS`</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — Benchmark-driven Jev router and judge for cost-aware, reliable LLM coding workflows
  <sub>`Benchmark` · ★0 · erendikmenn · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev-compatible decision endpoints
  <sub>`Project` · ★0 · dtduc-git · `Py`</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — A small second eval for shadcn-ui/lint that uses TypeSafe's Jev to judge the linter's own output.
  <sub>`Project` · ★0 · blas0 · `JS`</sub>

- **[jev-songwriter](https://github.com/beingcognitive/jev-songwriter)** — A decision model that cannot write a single note writes songs. Code computes, Jev judges, and every call is replayable.
  <sub>`Project` · ★0 · beingcognitive · `JS`</sub>

- **[Jev-test](https://github.com/WeSecureYou/Jev-test)** — A CLI and REST API that asks Jev how exposed an occupation is to AI-driven layoffs, where it is heading, how much human accountability it needs, and how resilient it is.
  <sub>`Project` · ★0 · wesecureyou · `TS` · ⚠ `no licence`</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next
  <sub>`Benchmark` · ★0 · sypherin · `Py`</sub>

- **[jevplay](https://github.com/ndolinschi/jevplay)** — TypeSafe Jev playground — custom Choice/Score/Noul builder with live distributions
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** — n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibrated probabilities
  <sub>`Project` · ★0 · dommonte · `TS`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — Jev-powered model-judged permission gate for OMP (TypeSafe System One)
  <sub>`Project` · ★0 · strml · `TS` · ⚠ `archived`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One Search: navigate and trace code with TypeSafe judgments and repository evidence
  <sub>`Project` · ★0 · cpaczek · `TS`</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town: social-deduction party game for the living room TV, moderated by TypeSafe Jev
  <sub>`Project` · ★0 · tpaulshippy · `Rb` · ⚠ `no licence`</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — Open-source Chrome extension that filters AI-generated prose and ads with Jev
  <sub>`Plugin` · ★0 · neddes · `JS`</sub>

- **[spendbrake](https://github.com/ndolinschi/spendbrake)** — Agent budget brake — continue / downgrade_model / stop via TypeSafe Jev
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[transcript-scorecard](https://github.com/brandonbryant12/transcript-scorecard)** — ACME live support-call scoring demo with TypeSafe AI, Effect, SQLite, React, Vite, and Turborepo
  <sub>`Project` · ★0 · brandonbryant12 · `TS` · ⚠ `no licence`</sub>

- **[typesafe-demo-mcp](https://github.com/bestagentkits/typesafe-demo-mcp)** — MCP server exposing TypeSafe System One judgments (noul, choice, score) as agent tools
  <sub>`Plugin` · ★0 · bestagentkits · `TS` · ⚠ `no licence`</sub>

- **[typesafe-oracles](https://github.com/trophee-bot/typesafe-oracles)** — Evaluating TypeSafe's System One primitives (Choice/Score/Noul) — where a typed oracle beats an LLM call
  <sub>`Project` · ★0 · trophee-bot · `JS` · ⚠ `no licence`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — Three composable judgment pipelines on TypeSafe's Jev: support-ticket triage, observability alert triage, and a deploy-risk gate.
  <sub>`Project` · ★0 · shivam2003-dev · `Py`</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — Using Typesafe.AI to generate diff reviews.
  <sub>`Project` · ★0 · rbalch · `Py` · ⚠ `no licence`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — Typed judgment layer for coding agents — gates from PRD to ship. Jev-ready, provider-agnostic.
  <sub>`Integration` · ★0 · zahrannnn · `TS` · ⚠ `no licence`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified claims`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
