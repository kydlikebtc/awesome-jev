# Model routing

<sub>[awesome-jev](../../README.md) · [中文](model-routing.zh-CN.md)</sub>

_Pick which downstream model or tier should handle a request._

Every catalogued example of this decision — 81 of them. The same rows, with caveats, are in [the index](../../README.md#model-routing); [the site](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#model-routing): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 2 · call site 73 · wire shape 1 · example only 1 · independent reports 0 · negative results 1 · no file cited 6. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) <sub>`Official docs` · `Py`</sub>
- [Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing) <sub>`Official docs` · `Py` · `choice`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.
  <sub>`Integration` · ★10k+ · `TS` · `choice` · `score` · `noul` · call site [`libs/providers/langchain-typesafe/src/types.ts`](https://github.com/langchain-ai/langchainjs/blob/HEAD/libs/providers/langchain-typesafe/src/types.ts), read 2026-09-22</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · call site [`scripts/jev-spike.mjs`](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs), read 2026-09-22</sub>

- **[Hindsight](https://github.com/vectorize-io/hindsight)** — Agent memory server that can hand two jobs to a decision model: re-ranking a recall pool with one Noul per candidate, optionally dropping unhelpful and duplicate memories, and settling easy consolidation cases with Choice questions before the LLM sees them. <sub>(written by a model)</sub>
  <sub>`Project` · ★10k+ · vectorize-io · `Py` · `noul` · `choice` · call site [`hindsight-api-slim/hindsight_api/engine/decision_model.py`](https://github.com/vectorize-io/hindsight/blob/HEAD/hindsight-api-slim/hindsight_api/engine/decision_model.py), read by a model 2026-11-05</sub>

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)** — ⌥ Coding agent with the IDE wired in
  <sub>`Project` · ★10k+ · can1357 · `TS` · call site [`packages/ai/src/judgment/native.ts`](https://github.com/can1357/oh-my-pi/blob/HEAD/packages/ai/src/judgment/native.ts), read by a model 2026-11-05</sub>

- **[openwork](https://github.com/different-ai/openwork)** — Open-source alternative to Claude Cowork, built on opencode. Its gateway's Auto route asks Jev one Score per Smart Router task and one for the thinking level, then routes the prompt by the answers; without a TypeSafe key it takes the fallback route. <sub>(written by a model)</sub>
  <sub>`Project` · ★10k+ · different-ai · `TS` · `score` · call site [`ee/apps/gateway/src/auto-router/jev.ts`](https://github.com/different-ai/openwork/blob/HEAD/ee/apps/gateway/src/auto-router/jev.ts), read by a model 2026-11-05</sub>

- **[Harness](https://github.com/autonomous-ai/openharness)** — Command center that runs coding agents such as Claude Code and Codex side by side across machines. Its ⌘B router asks Jev 1.13 through OpenRouter's Decisions API, in one request of Choice questions, which session, project and agent a new task goes to. <sub>(written by a model)</sub>
  <sub>`Project` · ★1k+ · autonomous-ai · `TS` · `choice` · call site [`cli/src/lib/jev/jevClient.ts`](https://github.com/autonomous-ai/openharness/blob/HEAD/cli/src/lib/jev/jevClient.ts), read by a model 2026-11-05</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`jevkit/client.py`](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py), read 2026-09-22 · ⚠ `measured, not adopted`</sub>

- **[Astra-Ares](https://github.com/miuuyy/Astra-Ares)** — Runs a patched Codex CLI in which Jev reads bounded task context and, with two choices, picks the reasoning effort for GPT-6's next response and how many responses (1, 2, 5 or 10) it should last; GPT-6 can change effort without breaking the prompt cache. An experimental reference implementation. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · miuuyy · `JS` · call site [`src/jev.mjs`](https://github.com/miuuyy/Astra-Ares/blob/HEAD/src/jev.mjs), read 2026-09-24</sub>

- **[distill](https://github.com/samuelfaj/distill)** — Coding-agent harness and TUI for Grok and Codex subscriptions and any OpenAI-compatible model, built to spend fewer tokens. When a model tier's effort is left on auto, the default, Jev picks the reasoning effort for every call; the client reaches Jev through OpenRouter by default. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · samuelfaj · `Rs` · call site [`crates/codegen/distill-workspace/src/jev/client.rs`](https://github.com/samuelfaj/distill/blob/HEAD/crates/codegen/distill-workspace/src/jev/client.rs), read 2026-09-22</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)** — Judges how hard a coding turn is, then picks the model tier, reasoning depth and speed mode to match.
  <sub>`Plugin` · ★100+ · `JS` · `choice` · `score` · call site [`server/jev_server.py`](https://github.com/0xNatoshi/jev-codex-router/blob/HEAD/server/jev_server.py), read 2026-09-22 · ⚠ `archived`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — An agent that routes evaluation work through typed decisions.
  <sub>`Project` · ★100+ · vinilana · `TS` · call site [`agent/lib/jev-router.ts`](https://github.com/vinilana/jev-eval-agent/blob/HEAD/agent/lib/jev-router.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★100+ · `TS` · `choice` · `score` · `noul` · call site [`src/review/codebase-judgments.ts`](https://github.com/devagrawal09/jev-review/blob/HEAD/src/review/codebase-judgments.ts), read 2026-09-22</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — A router for models, tools and subagents.
  <sub>`Project` · ★100+ · billionsbobby · `TS` · call site [`functions/api/jev.js`](https://github.com/BillionsBobby/JevRouter/blob/HEAD/functions/api/jev.js), read 2026-09-22</sub>

- **[Keel](https://github.com/codejunkie99/keel)** — macOS coding workspace in Rust for Claude Code, Codex and other coding agents. For a fresh task, an opt-in Jev selector asks one `choice` over the installed provider/model routes plus `escalate`, and a `noul` per route (does it directly help?); the host validates the pick or falls back. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · codejunkie99 · `Rs` · `choice` · `noul` · call site [`crates/jev-core/src/lib.rs`](https://github.com/codejunkie99/keel/blob/HEAD/crates/jev-core/src/lib.rs), read by a model 2026-10-29</sub>

- **[smithers](https://github.com/smithersai/smithers)** — Smithers is an agentic workflow framework for defining workflows in simple TypeScript configuration files and executing them quickly, durably, and reliably <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · smithersai · `TS` · call site [`packages/smithers/agent/model/src/Evaluator.ts`](https://github.com/smithersai/smithers/blob/HEAD/packages/smithers/agent/model/src/Evaluator.ts), read by a model 2026-11-05</sub>

- **[Yielded Agent](https://github.com/yielded-dev/agent)** — TypeScript runtime for durable agent threads on Effect and Effect AI. Its AutoModel picks a model profile when a thread is created, asking a decision model through Decision.classify which of the application's described models fits, and keeps that choice for later runs; the docs example uses Jev. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · yielded-dev · `TS` · `choice` · cited file [`docs/snippets/travel-planner/auto-model.ts`](https://github.com/yielded-dev/agent/blob/HEAD/docs/snippets/travel-planner/auto-model.ts), read by a model 2026-11-05</sub>

- **[a3m-router](https://github.com/Das-rebel/a3m-router)** — ⚡ Adaptive multi-model LLM router — 80+ providers, Jev System One single-pass routing (model=jev-auto), pheromone-trail failover, parallel ensemble merge. npm: adaptive-memory-multi-model-router <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · das-rebel · `TS` · call site [`dist/routing/jev/remote.d.ts`](https://github.com/Das-rebel/a3m-router/blob/HEAD/dist/routing/jev/remote.d.ts), read 2026-09-24</sub>

- **[Claude Model Router](https://github.com/alexei-led/claude-router)** — Claude Code mod that picks the model and effort for each turn and each subagent from a classifier's advice. Jev is the default classifier: one choice for the tier and one for the turn's activity, re-asked every few requests. Clef, OpenAI or a local Ollama model can stand in. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · alexei-led · `JS` · `choice` · call site [`lib/classifier-apis.mjs`](https://github.com/alexei-led/claude-router/blob/HEAD/lib/classifier-apis.mjs), read by a model 2026-10-31</sub>

- **[Claude x Jev](https://github.com/charlesdove977/claude-x-jev)** — Claude Code skill and commands in which Jev, through OpenRouter, sorts and Claude writes: classify, check or score batches, send only unsure items to Claude, verify Claude's drafts, and gate tool calls with a PreToolUse hook that asks whether a call can be undone and whether it serves the task. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · charlesdove977 · `Py` · `choice` · `noul` · `score` · call site [`skill/scripts/jev.py`](https://github.com/charlesdove977/claude-x-jev/blob/HEAD/skill/scripts/jev.py), read by a model 2026-10-30 · ⚠ `marketing`</sub>

- **[Codex Jev Router](https://github.com/suenot/codex-jev-router)** — Uses Jev Choice and Noul judgments on short task summaries to select a Codex subagent model and reasoning effort with a Sol fallback.
  <sub>`Project` · ★10+ · suenot · `JS` · `choice` · `noul` · call site [`src/router.mjs`](https://github.com/suenot/codex-jev-router/blob/HEAD/src/router.mjs), read 2026-09-24 · ⚠ `AI-written` `self-submitted`</sub>

- **[Hermes Switchyard](https://github.com/bgrablin/hermes-switchyard)** — Hermes Agent plugin that hands a session's small decisions to Jev and acts on the answers within limits you set: the reasoning effort each turn needs, which skill to load, which control to click in computer use, and re-ranking past-session search, with a local receipt of each. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · bgrablin · `Py` · `choice` · `noul` · `score` · call site [`hermes_switchyard/client.py`](https://github.com/bgrablin/hermes-switchyard/blob/HEAD/hermes_switchyard/client.py), read by a model 2026-11-07</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local Responses proxy, with independent task verification. <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★10+ · minilv · `TS` · call site [`src/codex-router/jev.ts`](https://github.com/miniLV/Jev-Auto-Router/blob/HEAD/src/codex-router/jev.ts), read by a model 2026-11-05</sub>

- **[jev-demo](https://github.com/soyjorgepilo/jev-demo)** — Three Spanish-language demos of one pattern, Jev decides and code acts: Jira ticket triage that applies, marks for review or escalates; a pre-flight pass that flags functions before Claude explains only those; and a PR router sending each pull request to rules, Haiku or Sonnet. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · soyjorgepilo · `TS` · `choice` · `noul` · `score` · call site [`shared/jev.ts`](https://github.com/soyjorgepilo/jev-demo/blob/HEAD/shared/jev.ts), read by a model 2026-11-04 · ⚠ `one commit` `no licence` `3rd-party key`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — Claude Code PreToolUse gate: regex hard rules and a read-only allowlist first, then one Noul and one Choice decide allow, ask or deny, so clearly safe commands skip the permission prompt. Codex, Cursor and OpenCode adapters, plus a review-router GitHub Action.
  <sub>`Plugin` · ★10+ · eugeniughelbur · `Py` · `noul` · `choice` · call site [`jev_gate.py`](https://github.com/eugeniughelbur/jev-engineering/blob/HEAD/jev_gate.py), read 2026-09-28 · ⚠ `self-submitted`</sub>

- **[jev-for-all](https://github.com/emirbartu/jev-for-all)** — Connects Jev to OpenCode, Claude Code, Hermes and pi through one shared decision contract: Jev picks the model tier from the first prompt, which skill to load and which tools a step needs, and can start a lean session without skills or MCP servers. It does nothing when Jev is slow or unsure. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · emirbartu · `TS` · `choice` · `noul` · call site [`src/jev.ts`](https://github.com/emirbartu/jev-for-all/blob/HEAD/src/jev.ts), read by a model 2026-11-02</sub>

- **[jev-kit](https://github.com/jonathanavis96/jev-kit)** — Claude Code kit: a PreToolUse guard where a free pre-filter passes about 93% of tool calls and Jev judges the rest (allow, warn, rewrite or block; fails open), sub-agent sizing, and Jev wired into file search, browsing and review. The author reports 9/9 browser runs at 0.0008 USD of Claude spend. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · jonathanavis96 · `Py` · `choice` · `noul` · call site [`vendor/jev-ultrafast/jev_ultrafast/model.py`](https://github.com/jonathanavis96/jev-kit/blob/HEAD/vendor/jev-ultrafast/jev_ultrafast/model.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[jev-opus](https://github.com/WXK-AI/jev-opus)** — Runs Claude Code on Opus 5.5 with Jev re-picking the effort level when a prompt arrives and after every tool batch (up after a failing test, back down once it passes), sent as per-message effort statements so the prompt cache survives. Works as a local gateway or a headless driver. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · wxk-ai · `TS` · call site [`dist/config.js`](https://github.com/WXK-AI/jev-opus/blob/HEAD/dist/config.js), read by a model 2026-10-24</sub>

- **[jev-pilot](https://github.com/akramovic1/jev-pilot)** — Claude Code plugin that asks Jev about each prompt before the turn: which reasoning effort it needs, which model and effort a subagent should get, whether to work directly, delegate or run in parallel, and which one skill applies. It raises effort once when tool calls keep failing. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · akramovic1 · `TS` · `choice` · `noul` · call site [`hooks/model-router.policy.ts`](https://github.com/akramovic1/jev-pilot/blob/HEAD/hooks/model-router.policy.ts), read by a model 2026-11-04</sub>

- **[jev-router](https://github.com/prismhq/jev-router)** — Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · prismhq · `Py` · call site [`jev_router/deciders.py`](https://github.com/prismhq/jev-router/blob/HEAD/jev_router/deciders.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-router](https://github.com/rajdhakad9826/jev-router)** — LLM router that picks the cheapest model capable of handling a query, using TypeSafe's Jev for fast classification instead of an LLM call. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · rajdhakad9826 · `TS` · call site [`src/jev/classifier.ts`](https://github.com/rajdhakad9826/jev-router/blob/HEAD/src/jev/classifier.ts), read 2026-09-24</sub>

- **[jev-router (dirien)](https://github.com/dirien/jev-router)** — Local pass-through proxy for Claude Code and the Codex CLI: on each message a person writes, Jev picks the model tier the work needs (a Choice), with optional yes/no guards for risky operations and routing claims; within a session it only moves up, to protect the prompt cache. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · dirien · `JS` · `choice` · `noul` · call site [`src/jev.mjs`](https://github.com/dirien/jev-router/blob/HEAD/src/jev.mjs), read by a model 2026-11-02</sub>

- **[jev-router (dominicrico)](https://github.com/dominicrico/jev-router)** — Claude Code plugin that sends each prompt, step and subagent to the cheapest Claude model that can do the job (Haiku, Sonnet, Opus or Fable) and caps reasoning effort: Jev picks the model and effort as a Choice, and a live band above the prompt shows every pick. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · dominicrico · `TS` · `choice` · call site [`hooks/register.tsx`](https://github.com/dominicrico/jev-router/blob/HEAD/hooks/register.tsx), read by a model 2026-11-02</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — An agent plugin that hands steps needing no text output to Jev instead of the main model.
  <sub>`Plugin` · ★10+ · shitianfang · `JS` · call site [`src/backends/typesafe.ts`](https://github.com/shitianfang/jev-use/blob/HEAD/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[JevDo](https://github.com/yinhong-zhou/jevdo)** — Loop for DeepSeek Harness (DSH) in which Jev decides each step: run a saved, validated Action (a command or script bound to a project), call the main model, ask for clarification or finish. The main model handles new problems and saves reusable Actions for later sessions. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · yinhong-zhou · `TS` · `choice` · call site [`src/decision.ts`](https://github.com/yinhong-zhou/jevdo/blob/HEAD/src/decision.ts), read by a model 2026-11-01</sub>

- **[Jevia](https://github.com/assistant-ui/jevia)** — Local-first model router for coding harnesses (Claude Code, Codex, OpenCode, Gemini CLI, Cursor Agent): for each task Jev chooses a capability tier, informed by your safety policy and recorded outcomes of earlier routes, and the tier maps to whichever models the harness offers. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · assistant-ui · `Rs` · `choice` · call site [`crates/jevia-core/src/jev.rs`](https://github.com/assistant-ui/jevia/blob/HEAD/crates/jevia-core/src/jev.rs), read by a model 2026-11-07</sub>

- **[jevonian](https://github.com/xinyao27/jevonian)** — A local endpoint between a coding agent and its providers that routes each turn to the most cost-effective capable model, manages quota and cache, and logs every routing decision to a local ledger.
  <sub>`Project` · ★10+ · xinyao27 · `Go` · `TS` · call site [`internal/brain/client.go`](https://github.com/xinyao27/jevonian/blob/HEAD/internal/brain/client.go), read by a model 2026-11-05</sub>

- **[Jevstiller](https://github.com/tomerglick57/Jevstiller)** — Proxy in front of a repeated Jev classification call: it forwards to Jev at first, trains a small local model on Jev's own answers and probabilities, and answers locally once it agrees with Jev on held-out traffic. The author reports 61.7% of Banking77 answered locally at 99.4% agreement. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · tomerglick57 · `Py` · `choice` · `noul` · call site [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/HEAD/jevstiller/teachers/jev.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[NetworkChuck's Jev guide](https://github.com/thenetworkchuck/jev-guide)** — Companion guide to NetworkChuck's Jev video, in five chapters from the Playground to code: curl calls with noul, choice and score questions, TypeSafe's skill for a coding agent, and a Bun model router where one choice question picks a small, medium or large model for each prompt. <sub>(written by a model)</sub>
  <sub>`Tutorial` · ★10+ · thenetworkchuck · `TS` · `choice` · call site [`examples/router/router.ts`](https://github.com/thenetworkchuck/jev-guide/blob/HEAD/examples/router/router.ts), read by a model 2026-11-06</sub>

- **[omo-jev-plugin](https://github.com/brianhong-dev/omo-jev-plugin)** — Plugin for the OmO and senpi coding agents that asks Jev which loaded skill and next tool fit the task, whether recent results repeat a failure and whether the work looks complete; in act mode also which model and thinking level to use and whether to block a tool call. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · brianhong-dev · `TS` · `noul` · `choice` · `score` · call site [`src/decision.ts`](https://github.com/brianhong-dev/omo-jev-plugin/blob/HEAD/src/decision.ts), read by a model 2026-11-01</sub>

- **[optim-jev](https://github.com/Oqura-ai/optim-jev)** — Claude Code plugin (Codex too) with three Jev tools: jev-compacter asks which stale tool calls and outputs can be dropped when context is compacted, jev-router picks a model and effort for each subagent, and jev-skills sends a short relevant skill list per prompt instead of the whole catalog. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · Oqura-ai · `Py` · `noul` · call site [`src/optim_jev/tools/jev_compacter/jev.py`](https://github.com/Oqura-ai/optim-jev/blob/HEAD/src/optim_jev/tools/jev_compacter/jev.py), read by a model 2026-10-30</sub>

- **[pi-jev](https://github.com/iefnaf/pi-jev)** — Pi extension suite powered by Jev: selective context compaction and model routing <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · iefnaf · `TS` · call site [`src/vendor/fast-jev-compaction/request.ts`](https://github.com/iefnaf/pi-jev/blob/HEAD/src/vendor/fast-jev-compaction/request.ts), read 2026-09-24</sub>

- **[pi-jev-model-router](https://github.com/da-vinci-noob/pi-jev-model-router)** — Extension for the pi coding agent that picks the model for each request: Jev names the kind of work, scores its complexity and the capability it deserves, and says whether it needs deep reasoning, while code composes those into a tier and weighs it against the spend caps and the budget used so far. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · da-vinci-noob · `TS` · `choice` · `noul` · `score` · call site [`extensions/pi-jev-model-router/jev.ts`](https://github.com/da-vinci-noob/pi-jev-model-router/blob/HEAD/extensions/pi-jev-model-router/jev.ts), read by a model 2026-11-04</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · mejiasd3v · `JS` · call site [`index.ts`](https://github.com/mejiasd3v/pi-jev-router/blob/HEAD/index.ts), read 2026-09-22</sub>

- **[pi-shift-router](https://github.com/green-dalii/pi-shift-router)** — Extension for the pi coding agent that routes each turn between a fast and a smart model tier, with failover on rate limits and exhausted quotas. Its judge can be a decision model such as Jev: one choice picks the tier and one noul decides whether to hand the task to subagents. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · green-dalii · `TS` · `choice` · `noul` · call site [`src/judge.ts`](https://github.com/green-dalii/pi-shift-router/blob/HEAD/src/judge.ts), read by a model 2026-11-03</sub>

- **[slo-router](https://github.com/zeeshan8281/slo-router)** — SLO-aware LLM inference router with Jev decisions, live queue metrics, counterfactual evaluation, and reproducible latency/cost benchmarks <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · zeeshan8281 · `Py` · call site [`slo_router/core.py`](https://github.com/zeeshan8281/slo-router/blob/HEAD/slo_router/core.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[stuntd](https://github.com/bladedevoff/stuntd)** — Local proxy that learns your app's typed LLM decisions and answers them with a Laya head. Jev and OpenAI compatible. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · bladedevoff · `Py` · call site [`stuntd/jev/answer.py`](https://github.com/bladedevoff/stuntd/blob/HEAD/stuntd/jev/answer.py), read 2026-09-24</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run.
  <sub>`Article` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `vendor numbers`</sub>

- **[ClauJev](https://github.com/civalski/claujev)** — Claude Code plugin in which Jev checks Claude's work before the reply reaches you: scores and nouls compare the turn's real git diff with what Claude says it did and send it back when the work looks unfinished; Jev also scores each request to suggest an effort level and routes subagents. <sub>(written by a model)</sub>
  <sub>`Plugin` · civalski · `JS` · `choice` · `score` · `noul` · call site [`plugins/claujev/hooks/claujev.mjs`](https://github.com/civalski/claujev/blob/HEAD/plugins/claujev/hooks/claujev.mjs), read by a model 2026-11-10</sub>

- **[codex-jev-router](https://github.com/tiandee/codex-jev-router)** — Wrapper for the Codex CLI that runs a local proxy and, on each fresh turn, asks Jev a choice of Codex model and scores for task complexity, reasoning required and tool complexity, then sets the model and reasoning effort; without Jev, Codex keeps its current settings. <sub>(written by a model)</sub>
  <sub>`Plugin` · tiandee · `JS` · `choice` · `score` · call site [`src/jev-client.mjs`](https://github.com/tiandee/codex-jev-router/blob/HEAD/src/jev-client.mjs), read by a model 2026-11-10</sub>

- **[dsh-jev-plugin](https://github.com/jackie-cqz/dsh-jev-plugin)** — DeepSeek Harness plugin that gives agents Jev's noul, choice and score as tools, and can also use Jev as a pre-execution risk gate (a score over risk levels that denies a tool call, asks for approval or lets it run), a review of tool results and a model router. <sub>(written by a model)</sub>
  <sub>`Plugin` · jackie-cqz · `TS` · `noul` · `choice` · `score` · call site [`src/client.ts`](https://github.com/jackie-cqz/dsh-jev-plugin/blob/HEAD/src/client.ts), read by a model 2026-11-08</sub>

- **[dsh-plugin-jev-effort-selector](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector)** — A DeepSeek Harness plugin that picks the reasoning level automatically: Jev judges how much thought each message deserves, follow-ups inherit the topic's depth, low confidence rounds up, and any failure falls back silently.
  <sub>`Plugin` · justhalfbit · `JS` · call site [`lib/client.js`](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector/blob/HEAD/lib/client.js), read 2026-09-24</sub>

- **[DuckDB Dual Cognition](https://github.com/prasanthj/duckdb-dual-cognition)** — Native DuckDB extension whose SQL functions ask Jev choices, scores and nouls over every row in batches, including picking a row's foreign key from candidates or answering ambiguous or no_match, and send only rows below a confidence threshold to an OpenAI model for reasoning. <sub>(written by a model)</sub>
  <sub>`Plugin` · prasanthj · `C++` · `choice` · `score` · `noul` · call site [`src/dc_extension.cpp`](https://github.com/prasanthj/duckdb-dual-cognition/blob/HEAD/src/dc_extension.cpp), read by a model 2026-11-11 · ⚠ `3rd-party key`</sub>

- **[hermes-jev-router](https://github.com/ussyverse/hermes-jev-router)** — Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending. <sub>(upstream description)</sub>
  <sub>`Plugin` · ussyverse · `Py` · call site [`jev.py`](https://github.com/ussyverse/hermes-jev-router/blob/HEAD/jev.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[Hiep Paseo plugins](https://github.com/hieppp/hiep-paseo-plugin)** — Plugins for the Paseo agent app, three of them on Jev: a permission gate that asks a noul on whether a shell command is read-only and a choice to allow, deny or escalate it to you, an orchestrator that routes delegated tasks to a model and effort, and an MCP evaluation tool. <sub>(written by a model)</sub>
  <sub>`Plugin` · hieppp · `TS` · `noul` · `choice` · call site [`plugins/jev-permission-gate/server/jev-worker.ts`](https://github.com/hieppp/hiep-paseo-plugin/blob/HEAD/plugins/jev-permission-gate/server/jev-worker.ts), read by a model 2026-11-10 · ⚠ `no licence`</sub>

- **[janus](https://github.com/FirasSX914/Janus)** — Measure when to use Jev and other models on your data, then route accordingly. <sub>(upstream description)</sub>
  <sub>`Project` · firassx914 · `Py` · call site [`experiments/run_jev.py`](https://github.com/FirasSX914/Janus/blob/HEAD/experiments/run_jev.py), read 2026-09-22</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice` · ⚠ `paywall`</sub>

- **[Jev Switch](https://github.com/ARCJ137442/SysTorch)** — Lightweight gateway that serves POST /v1/systemone and routes each call through an editable graph of upstreams (TypeSafe, Vercel, OpenRouter, Laya or a local server) with priorities and failover. Rust daemon with a React console, Tauri desktop app and Docker image. Chinese-first docs. <sub>(written by a model)</sub>
  <sub>`Project` · arcj137442 · `Rs` · `TS` · call site [`rs/crates/systorch-daemon/src/admin.rs`](https://github.com/ARCJ137442/SysTorch/blob/HEAD/rs/crates/systorch-daemon/src/admin.rs), read by a model 2026-10-24</sub>

- **[jev-codex-bridge](https://github.com/ansidium/jev-codex-bridge)** — Model and reasoning routing for Codex Desktop and CLI, with a Windows service and validated updates <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ansidium · `JS` · call site [`src/router.mjs`](https://github.com/ansidium/jev-codex-bridge/blob/HEAD/src/router.mjs), read 2026-09-24</sub>

- **[jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** — Smart Codex overlay with JEV model routing, context optimization & Kanban automation. Reduce tokens, keep control
  <sub>`Plugin` · charlyhno-eng · `TS` · `choice` · `score` · `noul` · call site [`src/core/hooks/jev-client.ts`](https://github.com/Charlyhno-eng/jev-codex-pilot/blob/HEAD/src/core/hooks/jev-client.ts), read 2026-09-24</sub>

- **[jev-gate](https://github.com/MongLong0214/jev-gate)** — Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary. <sub>(upstream description)</sub>
  <sub>`Plugin` · monglong0214 · `TS` · call site [`src/jev.ts`](https://github.com/MongLong0214/jev-gate/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-harness-router](https://github.com/JoacoMarc/jev-harness-router)** — Per-turn router for agent harnesses: one 350ms Jev call picks the model tier, effort, tools and skill, behind a hard deadline with a regex fallback. Claude Agent SDK adapter included. <sub>(upstream description)</sub>
  <sub>`SDK` · joacomarc · `TS` · call site [`src/jev.ts`](https://github.com/JoacoMarc/jev-harness-router/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

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

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

- **[model-router-python](https://github.com/TheCoder30ec4/model_router_python)** — Python library that, for each prompt, drops models whose context, output or budget cannot fit, then asks Jev to choose among the rest with their live prices and limits, and returns the model id for your code to call; Jev is reached through jevai.org or OpenRouter. <sub>(written by a model)</sub>
  <sub>`Project` · TheCoder30ec4 · `Py` · `choice` · call site [`src/model_router/jev.py`](https://github.com/TheCoder30ec4/model_router_python/blob/HEAD/src/model_router/jev.py), read by a model 2026-11-11</sub>

- **[pi-jev-router](https://github.com/philippdubach/pi-jev-router)** — A minimal Pareto-optimal OpenRouter model router for pi, based on Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · philippdubach · `TS` · call site [`src/classifier.ts`](https://github.com/philippdubach/pi-jev-router/blob/HEAD/src/classifier.ts), read 2026-09-24</sub>

- **[pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router)** — A Pi extension that has Jev classify each request and route it to the right model, off until you configure the mappings.
  <sub>`Plugin` · jekozyra · `TS` · call site [`src/config.ts`](https://github.com/jekozyra/pi-typesafe-router/blob/HEAD/src/config.ts), read 2026-09-24</sub>

- **[reasoning-router](https://github.com/robertn702/reasoning-router)** — Asks a classifier such as Jev how much reasoning effort each step of a coding session needs, with one choice question, so one strong model handles quick edits and hard debugging without switching effort by hand; works in OpenCode, Pi, Codex CLI and any client behind its local proxy. <sub>(written by a model)</sub>
  <sub>`Plugin` · robertn702 · `TS` · `choice` · call site [`packages/classifiers/src/jev.ts`](https://github.com/robertn702/reasoning-router/blob/HEAD/packages/classifiers/src/jev.ts), read by a model 2026-11-07</sub>

- **[smart-switch](https://github.com/reycn/smart-switch)** — Reimagined window switcher for macOS using frontier artificial intelligence. Predicted by TypeSafe's Jev model <sub>(upstream description)</sub>
  <sub>`Project` · reycn · `Swift` · call site [`core/src/lib.rs`](https://github.com/reycn/smart-switch/blob/HEAD/core/src/lib.rs), read 2026-09-22</sub>

- **[sommelier](https://github.com/wide3751/sommelier)** — Claude Code mod that picks the model and effort for each request: Jev scores how much reasoning it needs and answers nouls on whether it starts a new task and whether it is high-risk, and code maps that onto a Haiku, Sonnet, Opus ladder; an optional choice suggests a skill. <sub>(written by a model)</sub>
  <sub>`Plugin` · wide3751 · `TS` · `score` · `noul` · `choice` · call site [`hooks/register.ts`](https://github.com/wide3751/sommelier/blob/HEAD/hooks/register.ts), read by a model 2026-11-09</sub>

- **[spending-effort-with-jev](https://github.com/Yaxin9Luo/spending-effort-with-jev)** — Claude Code mod that reads each message you send and asks Jev a choice for the /effort level the task deserves and a noul on whether a long hand-off is still ambiguous; when the session's level looks wrong it offers a one-key switch, and it warns about fuzzy specs. <sub>(written by a model)</sub>
  <sub>`Plugin` · Yaxin9Luo · `TS` · `choice` · `noul` · call site [`plugins/spending-effort-with-jev/hooks/judge.ts`](https://github.com/Yaxin9Luo/spending-effort-with-jev/blob/HEAD/plugins/spending-effort-with-jev/hooks/judge.ts), read by a model 2026-11-10</sub>

- **[stuntdouble](https://github.com/ReallyArtificial/stuntdouble)** — A drop-in /v1/systemone proxy: the app keeps calling Jev while local decision models answer the same requests in the shadow, then it reports whether they would have decided the same — per question, per confidence band, at the app's own decide() — plus Brier, ECE, latency and cost.
  <sub>`Project` · Really Artificial · `JS` · `choice` · `score` · `noul` · call site [`src/backends.mjs`](https://github.com/ReallyArtificial/stuntdouble/blob/HEAD/src/backends.mjs), read 2026-09-24 · ⚠ `AI-written`</sub>

- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** — Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python. <sub>(upstream description)</sub>
  <sub>`Project` · aniruddh-krovvidi · `Py` · call site [`jev.py`](https://github.com/aniruddh-krovvidi/switchboard/blob/HEAD/jev.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — Model router that starts each request on the cheapest tier and lifts it only when Jev's signals (multi-step reasoning, difficulty, stakes, safety) cross a YAML policy. On its author's 120 prompts it matched the flagship's quality at 40% less cost; the fast model alone did as well at 3% of the cost. <sub>(written by a model)</sub>
  <sub>`Project` · iamvatsalpatel · `TS` · call site [`bench/experiments/gate-experiment.ts`](https://github.com/iamvatsalpatel/tiershift/blob/HEAD/bench/experiments/gate-experiment.ts), read 2026-09-22</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — A local decision layer in Jev's shape: yes/no, choice and rubric questions read off one token's logprobs from a local model, with a Claude Code permission gate measured on held-out command sets.
  <sub>`Jev-like alternative` · Xinyu Liu · `TS` · `noul` · `choice` · `score` · cited file [`src/gate.ts`](https://github.com/liu-x27/XavierJev/blob/HEAD/src/gate.ts), read 2026-09-25 · ⚠ `not Jev itself` `AI-written`</sub>

- **[Jev router: how model routing works, and 16 routers compared](https://madewithjev.com/jev-router)** — Explains a router that asks Jev which model, tool or skill the next turn needs before anything is spent, why routing down and back up can cost more than not routing, and compares 16 routers for Claude Code, Codex and OpenRouter.
  <sub>`Article` · Jon Kraayenbrink · ⚠ `self-submitted`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
