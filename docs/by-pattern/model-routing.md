# Model routing

<sub>[awesome-jev](../../README.md) · [中文](model-routing.zh-CN.md)</sub>

_Pick which downstream model or tier should handle a request._

Every catalogued example of this decision — 48 of them. The same rows, with caveats, are in [the index](../../README.md#model-routing); [the site](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#model-routing): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 2 · call site 41 · wire shape 1 · example only 0 · independent reports 0 · negative results 1 · no file cited 6. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) <sub>`Official docs` · `Py`</sub>
- [Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing) <sub>`Official docs` · `Py` · `choice`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.
  <sub>`Integration` · ★10k+ · `TS` · `choice` · `score` · `noul` · call site [`libs/providers/langchain-typesafe/src/types.ts`](https://github.com/langchain-ai/langchainjs/blob/HEAD/libs/providers/langchain-typesafe/src/types.ts), read 2026-09-22</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · call site [`scripts/jev-spike.mjs`](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs), read 2026-09-22</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`jevkit/client.py`](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py), read 2026-09-22 · ⚠ `measured, not adopted`</sub>

- **[Astra-Ares](https://github.com/miuuyy/Astra-Ares)** — Adaptive reasoning effort for GPT-6 during Codex tasks, powered by Jev to reduce token usage. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · miuuyy · `JS` · call site [`src/jev.mjs`](https://github.com/miuuyy/Astra-Ares/blob/HEAD/src/jev.mjs), read 2026-09-24</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)** — Judges how hard a coding turn is, then picks the model tier, reasoning depth and speed mode to match.
  <sub>`Plugin` · ★100+ · `JS` · `choice` · `score` · call site [`server/jev_server.py`](https://github.com/0xNatoshi/jev-codex-router/blob/HEAD/server/jev_server.py), read 2026-09-22 · ⚠ `archived`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — An agent that routes evaluation work through typed decisions.
  <sub>`Project` · ★100+ · vinilana · `TS` · call site [`agent/lib/jev-router.ts`](https://github.com/vinilana/jev-eval-agent/blob/HEAD/agent/lib/jev-router.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★100+ · `TS` · `choice` · `score` · `noul` · call site [`src/review/codebase-judgments.ts`](https://github.com/devagrawal09/jev-review/blob/HEAD/src/review/codebase-judgments.ts), read 2026-09-22</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — A router for models, tools and subagents.
  <sub>`Project` · ★100+ · billionsbobby · `TS` · call site [`functions/api/jev.js`](https://github.com/BillionsBobby/JevRouter/blob/HEAD/functions/api/jev.js), read 2026-09-22</sub>

- **[a3m-router](https://github.com/Das-rebel/a3m-router)** — ⚡ Adaptive multi-model LLM router — 80+ providers, Jev System One single-pass routing (model=jev-auto), pheromone-trail failover, parallel ensemble merge. npm: adaptive-memory-multi-model-router <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · das-rebel · `TS` · call site [`dist/routing/jev/remote.d.ts`](https://github.com/Das-rebel/a3m-router/blob/HEAD/dist/routing/jev/remote.d.ts), read 2026-09-24</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — Claude Code PreToolUse gate: regex hard rules and a read-only allowlist first, then one Noul and one Choice decide allow, ask or deny, so clearly safe commands skip the permission prompt. Codex, Cursor and OpenCode adapters, plus a review-router GitHub Action.
  <sub>`Plugin` · ★10+ · eugeniughelbur · `Py` · `noul` · `choice` · call site [`jev_gate.py`](https://github.com/eugeniughelbur/jev-engineering/blob/HEAD/jev_gate.py), read 2026-09-28 · ⚠ `self-submitted`</sub>

- **[jev-router](https://github.com/prismhq/jev-router)** — Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · prismhq · `Py` · call site [`jev_router/deciders.py`](https://github.com/prismhq/jev-router/blob/HEAD/jev_router/deciders.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-router](https://github.com/rajdhakad9826/jev-router)** — LLM router that picks the cheapest model capable of handling a query, using TypeSafe's Jev for fast classification instead of an LLM call. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · rajdhakad9826 · `TS` · call site [`src/jev/classifier.ts`](https://github.com/rajdhakad9826/jev-router/blob/HEAD/src/jev/classifier.ts), read 2026-09-24</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — An agent plugin that hands steps needing no text output to Jev instead of the main model.
  <sub>`Plugin` · ★10+ · shitianfang · `JS` · call site [`src/backends/typesafe.ts`](https://github.com/shitianfang/jev-use/blob/HEAD/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[jevonian](https://github.com/xinyao27/jevonian)** — A local endpoint between a coding agent and its providers that routes each turn to the most cost-effective capable model, manages quota and cache, and logs every routing decision to a local ledger.
  <sub>`Project` · ★10+ · xinyao27 · `TS` · call site [`src/brain.ts`](https://github.com/xinyao27/jevonian/blob/HEAD/src/brain.ts), read 2026-09-24</sub>

- **[pi-jev](https://github.com/iefnaf/pi-jev)** — Pi extension suite powered by Jev: selective context compaction and model routing <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · iefnaf · `TS` · call site [`src/vendor/fast-jev-compaction/request.ts`](https://github.com/iefnaf/pi-jev/blob/HEAD/src/vendor/fast-jev-compaction/request.ts), read 2026-09-24</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · mejiasd3v · `JS` · call site [`index.ts`](https://github.com/mejiasd3v/pi-jev-router/blob/HEAD/index.ts), read 2026-09-22</sub>

- **[pi-jev-router](https://github.com/philippdubach/pi-jev-router)** — A minimal Pareto-optimal OpenRouter model router for pi, based on Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · philippdubach · `TS` · call site [`src/classifier.ts`](https://github.com/philippdubach/pi-jev-router/blob/HEAD/src/classifier.ts), read 2026-09-24</sub>

- **[slo-router](https://github.com/zeeshan8281/slo-router)** — SLO-aware LLM inference router with Jev decisions, live queue metrics, counterfactual evaluation, and reproducible latency/cost benchmarks <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · zeeshan8281 · `Py` · call site [`slo_router/core.py`](https://github.com/zeeshan8281/slo-router/blob/HEAD/slo_router/core.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[stuntd](https://github.com/bladedevoff/stuntd)** — Local proxy that learns your app's typed LLM decisions and answers them with a Laya head. Jev and OpenAI compatible. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · bladedevoff · `Py` · call site [`stuntd/jev/answer.py`](https://github.com/bladedevoff/stuntd/blob/HEAD/stuntd/jev/answer.py), read 2026-09-24</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run.
  <sub>`Article` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `vendor numbers`</sub>

- **[Codex Jev Router](https://github.com/suenot/codex-jev-router)** — Uses Jev Choice and Noul judgments on short task summaries to select a Codex subagent model and reasoning effort with a Sol fallback.
  <sub>`Project` · suenot · `JS` · `choice` · `noul` · call site [`src/router.mjs`](https://github.com/suenot/codex-jev-router/blob/HEAD/src/router.mjs), read 2026-09-24 · ⚠ `AI-written` `self-submitted`</sub>

- **[dsh-plugin-jev-effort-selector](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector)** — A DeepSeek Harness plugin that picks the reasoning level automatically: Jev judges how much thought each message deserves, follow-ups inherit the topic's depth, low confidence rounds up, and any failure falls back silently.
  <sub>`Plugin` · justhalfbit · `JS` · call site [`lib/client.js`](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector/blob/HEAD/lib/client.js), read 2026-09-24</sub>

- **[hermes-jev-router](https://github.com/ussyverse/hermes-jev-router)** — Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending. <sub>(upstream description)</sub>
  <sub>`Plugin` · ussyverse · `Py` · call site [`jev.py`](https://github.com/ussyverse/hermes-jev-router/blob/HEAD/jev.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[janus](https://github.com/FirasSX914/Janus)** — Measure when to use Jev and other models on your data, then route accordingly. <sub>(upstream description)</sub>
  <sub>`Project` · firassx914 · `Py` · call site [`experiments/run_jev.py`](https://github.com/FirasSX914/Janus/blob/HEAD/experiments/run_jev.py), read 2026-09-22</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice` · ⚠ `paywall`</sub>

- **[Jev Switch](https://github.com/ARCJ137442/jev-switch)** — Lightweight gateway that serves POST /v1/systemone and routes each call through an editable graph of upstreams (TypeSafe, Vercel, OpenRouter, Laya or a local server) with priorities and failover. Rust daemon with a React console, Tauri desktop app and Docker image. Chinese-first docs.
  <sub>`Project` · arcj137442 · `Rs` · `TS` · call site [`rs/crates/jev-switch-daemon/src/admin.rs`](https://github.com/ARCJ137442/jev-switch/blob/HEAD/rs/crates/jev-switch-daemon/src/admin.rs)</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local Responses proxy, with independent task verification. <sub>(upstream description)</sub>
  <sub>`Plugin` · minilv · `TS` · call site [`src/jev-adapter.ts`](https://github.com/miniLV/Jev-Auto-Router/blob/HEAD/src/jev-adapter.ts), read 2026-09-22</sub>

- **[jev-codex-bridge](https://github.com/ansidium/jev-codex-bridge)** — Model and reasoning routing for Codex Desktop and CLI, with a Windows service and validated updates <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ansidium · `JS` · call site [`src/router.mjs`](https://github.com/ansidium/jev-codex-bridge/blob/HEAD/src/router.mjs), read 2026-09-24</sub>

- **[jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** — Smart Codex overlay with JEV model routing, context optimization & Kanban automation. Reduce tokens, keep control
  <sub>`Plugin` · charlyhno-eng · `TS` · `choice` · `score` · `noul` · call site [`src/core/hooks/jev-client.ts`](https://github.com/Charlyhno-eng/jev-codex-pilot/blob/HEAD/src/core/hooks/jev-client.ts), read 2026-09-24</sub>

- **[jev-gate](https://github.com/MongLong0214/jev-gate)** — Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary. <sub>(upstream description)</sub>
  <sub>`Plugin` · monglong0214 · `TS` · call site [`src/jev.ts`](https://github.com/MongLong0214/jev-gate/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-harness-router](https://github.com/JoacoMarc/jev-harness-router)** — Per-turn router for agent harnesses: one 350ms Jev call picks the model tier, effort, tools and skill, behind a hard deadline with a regex fallback. Claude Agent SDK adapter included. <sub>(upstream description)</sub>
  <sub>`SDK` · joacomarc · `TS` · call site [`src/jev.ts`](https://github.com/JoacoMarc/jev-harness-router/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[jev-kit](https://github.com/jonathanavis96/jev-kit)** — Claude Code kit: a PreToolUse guard where a free pre-filter passes about 93% of tool calls and Jev judges the rest (allow, warn, rewrite or block; fails open), sub-agent sizing, and Jev wired into file search, browsing and review. The author reports 9/9 browser runs at 0.0008 USD of Claude spend.
  <sub>`Plugin` · jonathanavis96 · `Py` · `choice` · `noul` · call site [`vendor/jev-ultrafast/jev_ultrafast/model.py`](https://github.com/jonathanavis96/jev-kit/blob/HEAD/vendor/jev-ultrafast/jev_ultrafast/model.py) · ⚠ `vendor numbers`</sub>

- **[jev-model-router](https://github.com/az9713/jev-model-router)** — Jev (TypeSafe) model router on the Vercel AI Gateway <sub>(upstream description)</sub>
  <sub>`Project` · az9713 · `JS` · call site [`probe.mjs`](https://github.com/az9713/jev-model-router/blob/HEAD/probe.mjs), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-model-router](https://github.com/Mandrilsquad1441/jev-model-router)** — Pick the best AI model and reasoning effort for any task in ~1s. Plugin for Claude Code, Claude Desktop and Codex, powered by TypeSafe's Jev decision model and live OpenRouter pricing. Balance intelligence, speed and cost, or choose your priority. <sub>(upstream description)</sub>
  <sub>`Plugin` · mandrilsquad1441 · `TS` · call site [`plugins/jev-model-router/dist/cli.mjs`](https://github.com/Mandrilsquad1441/jev-model-router/blob/HEAD/plugins/jev-model-router/dist/cli.mjs), read 2026-09-24</sub>

- **[jev-model-router](https://github.com/satviksinha/jev-model-router)** — Model router for Claude Code using Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · satviksinha · `TS` · call site [`scripts/check-jev.mjs`](https://github.com/satviksinha/jev-model-router/blob/HEAD/scripts/check-jev.mjs), read 2026-09-24</sub>

- **[jev-smart-router](https://github.com/rmosleydb/jev-smart-router)** — JEV Smart Router — a Databricks App that uses TypeSafe JEV to pick which model answers each message, then runs inference on the chosen Databricks Foundation Model API endpoint. <sub>(upstream description)</sub>
  <sub>`Project` · rmosleydb · `Py` · call site [`src/app.py`](https://github.com/rmosleydb/jev-smart-router/blob/HEAD/src/app.py), read 2026-09-24</sub>

- **[jev-synthetic-survey](https://github.com/jjd-lab/jev-synthetic-survey)** — Jev vs GPT-4.1 as synthetic survey respondents on Twin-2K-500. How you ask mattered more than which model you used. <sub>(upstream description)</sub>
  <sub>`Project` · jjd-lab · `Py` · call site [`scripts/twin2k/jev_client.py`](https://github.com/jjd-lab/jev-synthetic-survey/blob/HEAD/scripts/twin2k/jev_client.py), read 2026-09-22</sub>

- **[Jevstiller](https://github.com/tomerglick57/Jevstiller)** — Proxy in front of a repeated Jev classification call: it forwards to Jev at first, trains a small local model on Jev's own answers and probabilities, and answers locally once it agrees with Jev on held-out traffic. The author reports 61.7% of Banking77 answered locally at 99.4% agreement.
  <sub>`Project` · tomerglick57 · `Py` · `choice` · `noul` · call site [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/HEAD/jevstiller/teachers/jev.py) · ⚠ `vendor numbers`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

- **[pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router)** — A Pi extension that has Jev classify each request and route it to the right model, off until you configure the mappings.
  <sub>`Plugin` · jekozyra · `TS` · call site [`src/config.ts`](https://github.com/jekozyra/pi-typesafe-router/blob/HEAD/src/config.ts), read 2026-09-24</sub>

- **[smart-switch](https://github.com/reycn/smart-switch)** — Reimagined window switcher for macOS using frontier artificial intelligence. Predicted by TypeSafe's Jev model <sub>(upstream description)</sub>
  <sub>`Project` · reycn · `Swift` · call site [`core/src/lib.rs`](https://github.com/reycn/smart-switch/blob/HEAD/core/src/lib.rs), read 2026-09-22</sub>

- **[stuntdouble](https://github.com/ReallyArtificial/stuntdouble)** — A drop-in /v1/systemone proxy: the app keeps calling Jev while local decision models answer the same requests in the shadow, then it reports whether they would have decided the same — per question, per confidence band, at the app's own decide() — plus Brier, ECE, latency and cost.
  <sub>`Project` · Really Artificial · `JS` · `choice` · `score` · `noul` · call site [`src/backends.mjs`](https://github.com/ReallyArtificial/stuntdouble/blob/HEAD/src/backends.mjs), read 2026-09-24 · ⚠ `AI-written`</sub>

- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** — Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python. <sub>(upstream description)</sub>
  <sub>`Project` · aniruddh-krovvidi · `Py` · call site [`jev.py`](https://github.com/aniruddh-krovvidi/switchboard/blob/HEAD/jev.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — Shift every LLM call to the cheapest model that can handle it. Routing decided by TypeSafe Jev in ~180 ms. No training data. Policy in plain YAML. TypeScript and Python. <sub>(upstream description)</sub>
  <sub>`Project` · iamvatsalpatel · `TS` · call site [`bench/experiments/gate-experiment.ts`](https://github.com/iamvatsalpatel/tiershift/blob/HEAD/bench/experiments/gate-experiment.ts), read 2026-09-22</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — A local decision layer in Jev's shape: yes/no, choice and rubric questions read off one token's logprobs from a local model, with a Claude Code permission gate measured on held-out command sets.
  <sub>`Jev-like alternative` · Xinyu Liu · `TS` · `noul` · `choice` · `score` · cited file [`src/gate.ts`](https://github.com/liu-x27/XavierJev/blob/HEAD/src/gate.ts), read 2026-09-25 · ⚠ `not Jev itself` `AI-written`</sub>

- **[Jev router: how model routing works, and 16 routers compared](https://madewithjev.com/jev-router)** — Explains a router that asks Jev which model, tool or skill the next turn needs before anything is spent, why routing down and back up can cost more than not routing, and compares 16 routers for Claude Code, Codex and OpenRouter.
  <sub>`Article` · Jon Kraayenbrink · ⚠ `self-submitted`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
