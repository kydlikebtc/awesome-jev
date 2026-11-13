# Classification

<sub>[awesome-jev](../../README.md) · [中文](classification.zh-CN.md)</sub>

_Put an item into a taxonomy, including deep hierarchies walked with probabilities._

Every catalogued example of this decision — 191 of them. The same rows, with caveats, are in [the index](../../README.md#classification); [the site](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#classification): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 4 · call site 179 · wire shape 3 · example only 0 · independent reports 19 · negative results 1 · no file cited 9. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [WorkflowEvals](https://github.com/typesafe-ai/workflowevals) <sub>`Benchmark` · `Py` · `noul` · `choice` · `score` · ⚠ `one commit` `vendor numbers`</sub>
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

- **[WorkflowEvals](https://github.com/typesafe-ai/workflowevals)** ⭐ — TypeSafe's code for reproducing its WorkflowEvals site: four business workflows (invoice approval and fraud triage, customer-service routing and actions, agent-run action selection, security-alert triage), 705 cases scored against OpenAI, Anthropic and consensus references. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★10+ · typesafe-ai · `Py` · `noul` · `choice` · `score` · call site [`core/clients.py`](https://github.com/typesafe-ai/workflowevals/blob/HEAD/core/clients.py), read by a model 2026-11-02 · ⚠ `one commit` `vendor numbers`</sub>

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — Walks deep patent, retail, biomedical and source-code taxonomies with a parallel beam search over Choice probabilities.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block.
  <sub>`Official docs` · `Py`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★10k+ · `TS` · `choice` · `noul` · call site [`apps/web/utils/decision-model/decision-model.ts`](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/decision-model.ts), read by a model 2026-11-05</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.
  <sub>`Project` · ★10k+ · Vercel Labs · `TS` · `choice` · call site [`apps/web/lib/jev/compose.ts`](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts), read 2026-09-22</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.
  <sub>`Benchmark` · ★10k+ · `TS` · `choice` · call site [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js), read 2026-09-22 · author's conclusion: unfavourable (author-stated, not reproduced here) · ⚠ `shadow mode`</sub>

- **[ContextGem](https://github.com/shcherbak-ai/contextgem)** — Python framework that extracts structured data from documents with LLMs and decision models. Given a decision model such as Jev, it asks a yes/no question per paragraph to find each aspect's clauses and turns Boolean, label and rating concepts into noul, choice and score questions. <sub>(written by a model)</sub>
  <sub>`Project` · ★1k+ · shcherbak-ai · `Py` · `noul` · `choice` · `score` · call site [`contextgem/internal/base/decision_models.py`](https://github.com/shcherbak-ai/contextgem/blob/HEAD/contextgem/internal/base/decision_models.py), read by a model 2026-11-06</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · call site [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql), read 2026-09-22</sub>

- **[332_lab-jev-chat](https://github.com/Liyucheng1997/332_lab-jev-chat)** — A Windows WeChat assistant: Jev judges the intent of each incoming message and DeepSeek suggests replies.
  <sub>`Project` · ★100+ · liyucheng1997 · `Kt` · call site [`windows/jev_windows/jev_api.py`](https://github.com/Liyucheng1997/332_lab-jev-chat/blob/HEAD/windows/jev_windows/jev_api.py), read 2026-09-24</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends.
  <sub>`Project` · ★100+ · `TS` · `choice` · call site [`src/search.ts`](https://github.com/ellipsis-dev/blink/blob/HEAD/src/search.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)** — Zero-shot text classification over plain HTTP, no key or signup: labels and text in, a label and a calibrated confidence out, a thousand texts per request. Jev answers both tiers, a choice per text or a noul per label for multi-label; the smart tier re-asks answers below 0.7 of a reasoning model. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · mrmps · `TS` · call site [`src/jev.ts`](https://github.com/mrmps/classifier-dev/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[crush-monitor](https://github.com/FerryCorleone/crush-monitor)** — Local web tool that analyses a pasted WeChat chat with a crush. For each message Jev weighs 12 emotions and 35 intents, showing the top three of each, and it scores the affection signals and your own replies, graded SSS to D. Text LLMs can stand in for Jev. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · ferrycorleone · `TS` · call site [`server/provider-config.ts`](https://github.com/FerryCorleone/crush-monitor/blob/HEAD/server/provider-config.ts), read 2026-09-24</sub>

- **[dasheng](https://github.com/wquguru/dasheng)** — Read-aloud trainer for English: a streaming ASR model transcribes, alignment picks the words that differ, and Jev judges only those, a noul on whether it is the same word, a choice of error type, and a 1–5 score of whether the sentence kept its meaning. Pronunciation is not scored. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · wquguru · `JS` · call site [`lib/jev.js`](https://github.com/wquguru/dasheng/blob/HEAD/lib/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — Classifies and splits PDF, DOCX and PPTX files: LiteParse extracts page text locally, then Jev picks a document's category with a choice over your rules, or for a packet answers per page a category choice and a noul on whether a new document starts there. Its report covers 40 real PDFs. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · jerryjliu · `Py` · call site [`src/jev_docs/engines/jev.py`](https://github.com/jerryjliu/docjev/blob/HEAD/src/jev_docs/engines/jev.py), read 2026-09-22</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)** — An introduction to Jev with hands-on tests: Choice, Score and Noul turn natural language into typed judgements for classification, scoring and routing, compared with DeepSeek on comment labelling, speed and results, with CSV import, replay and offline reports.
  <sub>`Benchmark` · ★100+ · nanmicoder · `JS` · call site [`src/backends/jev.mjs`](https://github.com/NanmiCoder/jev-arena/blob/HEAD/src/backends/jev.mjs), read 2026-09-24</sub>

- **[Jev-Code-Reviewer](https://github.com/egma-ai/jev-code-reviewer)** — Local reviewer for coding agents' pull requests: each change is classified P0, P1 or P2 by Jev choices against a written priority policy, and only P0 changes are shown by default. Posts nothing to GitHub. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · egma-ai · `JS` · `choice` · call site [`src/providers.mjs`](https://github.com/egma-ai/jev-code-reviewer/blob/HEAD/src/providers.mjs), read by a model 2026-10-24</sub>

- **[jev-job-search](https://github.com/qbeka/jev-job-search)** — Job application tool run from Claude Code that asks Jev, through OpenRouter, whether each posting is a paid software role at the right level and term, how well the stack matches, and which saved answer or option fits each form field, then fills the forms in Chrome for you to approve. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · qbeka · `TS` · `noul` · `choice` · `score` · call site [`src/jev/client.ts`](https://github.com/qbeka/jev-job-search/blob/HEAD/src/jev/client.ts), read by a model 2026-11-10</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts), read 2026-09-22</sub>

- **[Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis)** — An on-demand crypto market terminal: pick a coin and a tweet sample, and Jev turns market data, funding rates and social sentiment into a Buy, Sell, Hold or Take Profit decision card. It never places trades.
  <sub>`Project` · ★100+ · brainstormity · `Py` · call site [`app/services/typesafe_service.py`](https://github.com/brainstormity/Jev-X-Sentiment-Analysis/blob/HEAD/app/services/typesafe_service.py), read 2026-09-24</sub>

- **[jev4pg](https://github.com/Sheltercosmo/jev4pg)** — Natural-language SQL and 41 semantic operators for PostgreSQL. Filtering, extraction, ranking, matching and verification go to Jev in bounded batches with validated answers; a choice option needs 0.55 and a noul 0.8 to count. The authors report 98% accuracy against 92% for pg-jev's request path. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · Sheltercosmo · `Py` · `choice` · `noul` · call site [`sdd/generic/jev.py`](https://github.com/Sheltercosmo/jev4pg/blob/HEAD/sdd/generic/jev.py), read by a model 2026-10-26 · ⚠ `vendor numbers`</sub>

- **[jevmem](https://github.com/Avinash-jetwani/jevmem)** — Project memory for Claude Code, Cursor and Codex: a Jev noul asks if a decision is worth keeping, kept ones go to JEVMEM.md and return when relevant, and edits and commands are checked against them. Author's runs: Claude followed them in 66 of 72 sessions, 28 without, 67 with a hand-kept CLAUDE.md. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · avinash-jetwani · `TS` · call site [`src/jev.ts`](https://github.com/Avinash-jetwani/jevmem/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[orchestkit](https://github.com/yonatangross/orchestkit)** — Claude Code plugin of 110 skills, 36 agents and 163 hooks for review, testing, security and memory. Optionally, Jev is a second classifier of a session's work category: one choice over 9 categories from the git branch and first prompt; the cited script runs it on 150 held-out sessions. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · yonatangross · `TS` · call site [`docs/audits/jev-session-category-heldout-2026-09-17/run_jev_b.mjs`](https://github.com/yonatangross/orchestkit/blob/HEAD/docs/audits/jev-session-category-heldout-2026-09-17/run_jev_b.mjs), read 2026-09-22</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js), read 2026-09-22</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy.
  <sub>`Project` · ★100+ · `TS` · `choice` · `score` · call site [`engine/jev-service.ts`](https://github.com/irfndi/prism-liquidity-agent/blob/HEAD/engine/jev-service.ts), read 2026-09-22</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — Local-first work assistant that turns mail, chats and tickets into tasks your coding agents do, sending nothing until you approve. With a TypeSafe key, Jev triages: nouls asked as the owner would judge, with their profile and past verdicts in the state, such as whether to make an item a task. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · ldbumble · `Py` · call site [`taskuary/jev.py`](https://github.com/ldbumble/taskuary/blob/HEAD/taskuary/jev.py), read 2026-09-22</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — Classifies tax document pages: one request per page asks Jev two choices, page kind (7 options) and IRS form (230 plus none), and a follow-up choice for five forms' schedules; criteria come from IRS PDFs and code gates at 0.95. Its author measured no strict error on 314 filled pages. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · kyotofin · `TS` · call site [`src/backend.ts`](https://github.com/kyotofin/tax-doc-classifier/blob/HEAD/src/backend.ts), read 2026-09-22</sub>

- **[tev1-4B-experimental](https://github.com/togethercomputer/tev1)** — Together AI fine-tuned Qwen3.5-4B to answer decisions with one option letter. In a paired rerun of three public Jev benchmarks it scored 50.6% on phishing against Jev 1.13's 62.9%, 93.3% on tool risk for both, and 96.3% against 100% on ticket routing. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★100+ · togethercomputer · `Py` · `choice` · call site [`evaluation/public-third-party/run.py`](https://github.com/togethercomputer/tev1/blob/HEAD/evaluation/public-third-party/run.py), read by a model 2026-11-05</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — A browser extension that removes page clutter, with reusable template rules.
  <sub>`Project` · ★100+ · kitze · `TS` · call site [`lib/jev.ts`](https://github.com/kitze/unclutter/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — Chrome extension that skips YouTube sponsor reads: per 80-line transcript window, a Jev noul asks if a read starts there and a choice names the line, then nouls on short phrases place the cut; code maps lines to seconds. Audio modes ask Jev every few seconds if a read is on. Default skip bar: 70%. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · trungdq88 · `JS` · call site [`extension/lib/jev.js`](https://github.com/trungdq88/youtube-sponsor-detection/blob/HEAD/extension/lib/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Apparite](https://github.com/dglazkov/jev2ui)** — Design tool that turns a text prompt into a clickable app mock painted by a DESIGN.md: Jev decides, in one request of choices and nouls, which sections, layout and icon a screen gets, and what each later message asks to change; a small Gemini model writes the words and code assembles the screen. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · dglazkov · `TS` · `choice` · `noul` · `score` · call site [`src/server/plan.ts`](https://github.com/dglazkov/jev2ui/blob/HEAD/src/server/plan.ts), read by a model 2026-11-09 · ⚠ `3rd-party key`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★10+ · 24601 · `Py` · call site [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md), read 2026-09-24</sub>

- **[Claude x Jev](https://github.com/charlesdove977/claude-x-jev)** — Claude Code skill and commands in which Jev, through OpenRouter, sorts and Claude writes: classify, check or score batches, send only unsure items to Claude, verify Claude's drafts, and gate tool calls with a PreToolUse hook that asks whether a call can be undone and whether it serves the task. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · charlesdove977 · `Py` · `choice` · `noul` · `score` · call site [`skill/scripts/jev.py`](https://github.com/charlesdove977/claude-x-jev/blob/HEAD/skill/scripts/jev.py), read by a model 2026-10-30 · ⚠ `marketing`</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · devanshbatham · `Rs` · call site [`src/jev.rs`](https://github.com/devanshbatham/commit-miner/blob/HEAD/src/jev.rs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[DMB: decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — Benchmark of APIs that pick one option from a list with a confidence: Jev, LLMs with structured output and deterministic baselines, on accuracy, latency, cost, failures and confidence. The author reports jev-latest at 79.2% on Banking77, 88.6% on CLINC150 and 48.3% micro F1 on NLU++. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★10+ · nibzard · `Py` · `choice` · call site [`src/dmb/contenders/jev.py`](https://github.com/nibzard/decision-model-benchmark/blob/HEAD/src/dmb/contenders/jev.py), read by a model 2026-11-04 · ⚠ `no licence`</sub>

- **[DriveSceneMiner](https://github.com/bskkimm/drivesceneminer)** — Mines driving manoeuvres from recorded vehicle data: it turns motion, lane geometry and object interactions into readable evidence, Jev classifies each moment's lateral and longitudinal manoeuvre with choice questions, and the moments merge into timestamped, reviewable scenes. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · bskkimm · `Py` · `choice` · call site [`src/jevsceneminer/inference/jev.py`](https://github.com/bskkimm/drivesceneminer/blob/HEAD/src/jevsceneminer/inference/jev.py), read by a model 2026-11-07</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness — Jev-powered risk classification & evidence-gated auto-approval. Fail-closed by construction. dsh 生态第一个 System-1 决策插件 <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · asktheway · `TS` · call site [`scripts/smoke.mjs`](https://github.com/AskTheWay/dsh-jev-interceptor/blob/HEAD/scripts/smoke.mjs), read 2026-09-24</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scoring, and semantic predicates from SQL. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · prasanthj · `C++` · call site [`benchmarks/live.py`](https://github.com/prasanthj/duckdb-jev/blob/HEAD/benchmarks/live.py), read 2026-09-22</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — Software, by reflex. A sentence becomes a call of a small program, chosen by Jev, TypeSafe AI's classifier, and run only when it is sure enough. Reflexes are recipes anyone can write, share and improve. A CLI you talk to, a package manager for reflexes from git, and a TypeScript SDK.
  <sub>`Project` · ★10+ · evoke-build · `Rs` · call site [`crates/evoke-adapters/src/systemone.rs`](https://github.com/evoke-build/evoke/blob/HEAD/crates/evoke-adapters/src/systemone.rs), read 2026-09-24</sub>

- **[grev](https://github.com/aurorainfra/grev)** — Unix filters that ask questions instead of matching patterns: `grev 'is a vegan meal' menu.txt` keeps the lines Jev says yes to, with related tools that use a choice's confidence or a path score. Pins jev-1.13.0 because thresholds are tuned per model version. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · aurorainfra · `Go` · call site [`internal/jev/price.go`](https://github.com/aurorainfra/grev/blob/HEAD/internal/jev/price.go), read by a model 2026-10-24</sub>

- **[Gut](https://github.com/vinibrsl/gut)** — Elixir DSL for LLM decisions: Gut.feel(subject, question, choices) returns one of your Elixir values, such as the team that should handle a ticket. Its Jev adapter asks the question as one Choice through ReqLLM; other adapters use any ReqLLM model, Ollama or your own code. <sub>(written by a model)</sub>
  <sub>`SDK` · ★10+ · vinibrsl · `Ex` · `choice` · call site [`lib/gut/req_llm/jev.ex`](https://github.com/vinibrsl/gut/blob/HEAD/lib/gut/req_llm/jev.ex), read by a model 2026-11-02</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — A Home Assistant integration: typed answers about the house as sensors, noul, choice and score actions for automations, and a conversation agent.
  <sub>`Integration` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · call site [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py), read 2026-09-30 · ⚠ `AI-written` `self-submitted`</sub>

- **[Jev Account Filter](https://github.com/caiweihan/jev-account-filter)** — Screens video-platform accounts (Douyin, Kuaishou, YouTube, Bilibili) as dataset sources: from an account's titles, thumbnails, name and bio, one Jev request picks its category, the probability it is relevant, each video's relevance and the best video. Sign-language creators are the tested case. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · caiweihan · `Py` · `choice` · `noul` · call site [`account_filter/screening/classifier.py`](https://github.com/caiweihan/jev-account-filter/blob/HEAD/account_filter/screening/classifier.py), read by a model 2026-10-31</sub>

- **[Jev Ad Blocker](https://github.com/fazlerocks/jev-adblock)** — Chrome extension that blocks ads without filter lists: it describes each ad-shaped element in a few structural fields and asks Jev one choice per element in a single batched request (display ad, sponsored, consent or popup, own promo, content, UI); code hides those past a per-category threshold. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · fazlerocks · `TS` · `choice` · call site [`src/shared/jev/questions.ts`](https://github.com/fazlerocks/jev-adblock/blob/HEAD/src/shared/jev/questions.ts), read by a model 2026-11-08</sub>

- **[Jev and open decision-model benchmarks](https://github.com/akitaonrails/jev-docs-benchmarks)** — Benchmarks how reliably decision models apply supplied rules, how their probabilities behave and what decisions cost: hosted Jev against Microsoft Decision-1, OpenAI Decisions and open models such as Clef, Decision 3.0, Laya, Kev and Jebadiah, with frozen inputs and raw responses. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★10+ · akitaonrails · `Py` · `choice` · call site [`benchmark/tools/hosted.py`](https://github.com/akitaonrails/jev-docs-benchmarks/blob/HEAD/benchmark/tools/hosted.py), read by a model 2026-11-07 · ⚠ `no licence`</sub>

- **[Jev Guard](https://github.com/gulbaki/jev-llm-guard)** — Guardrail for text an LLM app handles, whether user input, retrieved content, tool output or model output: Jev answers a noul for each of the ten OWASP LLM Top 10 risks, plus the attack type and a severity score, and a versioned local policy turns them into allow, review or block. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · gulbaki · `JS` · `noul` · `choice` · `score` · call site [`src/guard.js`](https://github.com/gulbaki/jev-llm-guard/blob/HEAD/src/guard.js), read by a model 2026-11-03</sub>

- **[JEV Healthcare Lab](https://github.com/juneyaooo/jev-healthcare-lab)** — Benchmark of Jev on medical decisions (triage urgency, contraindications, medication choice, nursing, trial screening) as choice questions over 26 tasks and 1,514 judgements, against DeepSeek Flash and Qwen, with accuracy, sustained throughput and cost, and raw responses published. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★10+ · juneyaooo · `Py` · `choice` · call site [`scripts/run_model_evaluation.py`](https://github.com/juneyaooo/jev-healthcare-lab/blob/HEAD/scripts/run_model_evaluation.py), read by a model 2026-11-07 · ⚠ `no licence`</sub>

- **[JEV Sees](https://github.com/CharlesFeng0314/JEV_sees)** — Gives Jev vision: local Florence-2 and CLIP models find the objects in an image, video or RGB-D frame and keep their IDs across frames, then Jev answers a choice, noul or score about each relevant object (bus colour, pedestrian risk, animal motion). <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · charlesfeng0314 · `Py` · `choice` · `noul` · `score` · call site [`jev_sees/session.py`](https://github.com/CharlesFeng0314/JEV_sees/blob/HEAD/jev_sees/session.py), read by a model 2026-10-24</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and safe orchestration. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · forvela · `JS` · call site [`src/decision.js`](https://github.com/forvela/jev-agent-browser/blob/HEAD/src/decision.js), read 2026-09-22</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · smkrv · `TS` · call site [`src/client.ts`](https://github.com/smkrv/jev-calibrate/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and OpenCode: typed classify, check, score, rank, and ask, plus one-command setup. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · francoischastel · `TS` · call site [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts), read 2026-09-22</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · goodrahstar · `JS` · call site [`lib/racers.mjs`](https://github.com/goodrahstar/jev-column-race/blob/HEAD/lib/racers.mjs), read 2026-09-22</sub>

- **[jev-datafusion](https://github.com/parable-work/jev-datafusion)** — Rust crate that registers Jev as SQL functions in Apache DataFusion: noul, choice, score and a multi-question ask run per row, so one query can score every ticket or route a year of email at warehouse scale. Works with TypeSafe, OpenRouter or any /v1/systemone endpoint. <sub>(written by a model)</sub>
  <sub>`Integration` · ★10+ · parable-work · `Rs` · `noul` · `choice` · `score` · call site [`src/provider.rs`](https://github.com/parable-work/jev-datafusion/blob/HEAD/src/provider.rs), read by a model 2026-11-03</sub>

- **[jev-gmail-ai-spam-filter-and-labeling](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling)** — Self-hosted AI email classifier for Gmail powered by Jev. Create custom labels, organize your inbox, and filter spam with confidence and cost controls. <sub>(earlier upstream description)</sub>
  <sub>`Project` · ★10+ · ilyamk · `JS` · call site [`CODE.gs`](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling/blob/HEAD/CODE.gs), read 2026-09-24</sub>

- **[jev-ids](https://github.com/jev-sec/jev-ids)** — Blazing-Fast Token-Efficient Intrusion Detection System (IDS) based on TypeSafe's Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jev-ids · `Py` · call site [`jev_ids/detectors/jev.py`](https://github.com/jev-sec/jev-ids/blob/HEAD/jev_ids/detectors/jev.py), read 2026-09-24</sub>

- **[jev-linkmap](https://github.com/stas4000/jev-linkmap)** — Rebuilds a website's internal links: code crawls the site and shortlists 15 similar pages per page with anchor phrases already in its copy, then one Jev request per page asks, for each target, whether to link (yes/no) and which phrase is the anchor (choice). <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · stas4000 · `Py` · `noul` · `choice` · call site [`jev_linkmap/jev.py`](https://github.com/stas4000/jev-linkmap/blob/HEAD/jev_linkmap/jev.py), read by a model 2026-11-01</sub>

- **[Jev-Mail](https://github.com/vynnlee/jev-mail)** — Gmail inbox classifier that runs on Google Apps Script and is managed from a CLI: for each thread Jev judges whether it needs action, whether it deserves a star and which configured category it belongs to, and the worker labels, stars or archives it. Ambiguous answers stay in the inbox. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · vynnlee · `TS` · `noul` · `choice` · call site [`src/gas/worker.ts`](https://github.com/vynnlee/jev-mail/blob/HEAD/src/gas/worker.ts), read by a model 2026-11-03</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · parth-kp · `Py` · call site [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py), read 2026-09-22</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — An MCP server exposing classify, score, check, match and screen to any agent.
  <sub>`Plugin` · ★10+ · blakestone-x · `Py` · call site [`jev_mcp/client.py`](https://github.com/blakestone-x/jev-mcp/blob/HEAD/jev_mcp/client.py), read 2026-09-22</sub>

- **[jev-poly-crypto-demo](https://github.com/frankda/jev-poly-crypto-demo)** — A research tool for Polymarket's five-minute BTC Up/Down markets: live market data becomes Jev class scores, independent logic decides, and a dashboard shows it. Paper trading only; it never connects a wallet.
  <sub>`Project` · ★10+ · frankda · `TS` · call site [`scripts/check-jev.ts`](https://github.com/frankda/jev-poly-crypto-demo/blob/HEAD/scripts/check-jev.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · kbhuw · `JS` · call site [`dist/server.mjs`](https://github.com/kbhuw/jev-sift/blob/HEAD/dist/server.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-trader](https://github.com/buberlo/jev-trader)** — Paper-trading market-making system that asks Jev six judgments in one call per 300 ms block: market regime and direction (choice), whether flow is toxic and liquidity thin (yes/no), how good quoting conditions are and how urgent cutting inventory is (score). Code applies policy and risk vetoes. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · buberlo · `Py` · `choice` · `noul` · `score` · call site [`src/jev_trader/judgment/client.py`](https://github.com/buberlo/jev-trader/blob/HEAD/src/jev_trader/judgment/client.py), read by a model 2026-10-31 · ⚠ `one commit`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · reachjalil · `TS` · call site [`benchmarks/run.mjs`](https://github.com/reachjalil/jev-tree/blob/HEAD/benchmarks/run.mjs), read 2026-09-22</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — Answers one question over a pile of text — tickets, reviews, logs — by packing many items into each request, and reports 32x the throughput of one request per item at 41% lower cost.
  <sub>`Project` · ★10+ · collapseindex · `Py` · call site [`src/jev_ultralightspeed/_settings.py`](https://github.com/collapseindex/jev-ultralightspeed/blob/HEAD/src/jev_ultralightspeed/_settings.py), read 2026-09-24 · ⚠ `unverified claims`</sub>

- **[JevBystander](https://github.com/Nisaka520/JevBystander)** — An Android accessibility reader for WeChat: it only reads the screen and pops three toasts — intent, emotion, urgency, a suggestion — and never writes or sends a reply. No third-party dependencies; an 861 KB APK.
  <sub>`Project` · ★10+ · nisaka520 · `Kt` · call site [`app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt`](https://github.com/Nisaka520/JevBystander/blob/HEAD/app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt), read 2026-09-24</sub>

- **[jevclip](https://github.com/cclank/jevclip)** — Cuts video from its subtitles: Jev reads each ~20-second segment and answers five questions (which of eight kinds of talk it is, information density 0–3, unfounded claims, whether it stands alone, whether it fits your focus); code keeps, ranks and cuts a 3-minute highlight and a trimmed full cut. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · cclank · `Py` · `choice` · `score` · `noul` · call site [`jevclip/jev.py`](https://github.com/cclank/jevclip/blob/HEAD/jevclip/jev.py), read by a model 2026-10-31</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — Text extraction with Jev: field extraction, PII detection and exact quotes, built on TypeSafe's Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jkrup · `JS` · call site [`src/client.mjs`](https://github.com/jkrup/jeveryword/blob/HEAD/src/client.mjs), read 2026-09-22</sub>

- **[Jevflake](https://github.com/KranzL/Jevflake)** — dbt package (with a Terraform module) that lets Snowflake ask Jev about table rows: it sets up external access to api.typesafe.ai and creates SQL functions jev_noul, jev_choice, jev_score and jev_ask, plus dbt macros and tests so answers are stored once, reused and checked. <sub>(written by a model)</sub>
  <sub>`Integration` · ★10+ · KranzL · `Py` · `noul` · `choice` · `score` · call site [`macros/setup/handler.sql`](https://github.com/KranzL/Jevflake/blob/HEAD/macros/setup/handler.sql), read by a model 2026-11-02</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-language questions and full probabilities using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ktaletsk · `Py` · call site [`src/jevframe/_engine.py`](https://github.com/ktaletsk/jevframe/blob/HEAD/src/jevframe/_engine.py), read 2026-09-22</sub>

- **[jevintegration for SAP Commerce](https://github.com/emenowicz/jev-sap-commerce)** — SAP Commerce extension: Jev answers four nouls per product review (abusive, spam, personal data, on topic) so code approves or rejects only past your thresholds, and choices suggest categories, level by level down the tree, and attribute values; anything unsure stays with a person. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · emenowicz · `Java` · `noul` · `choice` · call site [`jevintegration/src/org/jevintegration/JevClient.java`](https://github.com/emenowicz/jev-sap-commerce/blob/HEAD/jevintegration/src/org/jevintegration/JevClient.java), read by a model 2026-11-08</sub>

- **[JevIntent](https://github.com/Nisaka520/JevIntent)** — A WeChat plugin (FkWeChat): long-press a message to analyse its intent, emotion and a suggested reply stance, shown only as a local hint the sender never sees.
  <sub>`Project` · ★10+ · nisaka520 · `Java` · call site [`main.java`](https://github.com/Nisaka520/JevIntent/blob/HEAD/main.java), read 2026-09-24</sub>

- **[Jevline](https://github.com/tsale/jevline)** — Scopes an incident from security telemetry: from one confirmed-malicious process, it asks Jev of every process, account, host, address or domain the logs link to whether it belongs to the same incident, and follows what joins round by round. Answers near the threshold are marked for analyst review. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · tsale · `TS` · `noul` · call site [`engine/src/jev.ts`](https://github.com/tsale/jevline/blob/HEAD/engine/src/jev.ts), read by a model 2026-10-31</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · reachjalil · `JS` · call site [`benchmarks/pager/run-jev-v2.mjs`](https://github.com/reachjalil/jevlogs/blob/HEAD/benchmarks/pager/run-jev-v2.mjs), read 2026-09-22</sub>

- **[jevotron](https://github.com/ai4curation/jevotron)** — Command-line field-level anomaly detection for CSV, JSON, text, SQLite and DuckDB: Jev labels each field of each entry NORMAL or ANOMALY, or with your own classes, given optional guidance and exemplars, and the output is a review queue sorted by confidence. SQLite caching reuses past answers. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · ai4curation · `Py` · `choice` · call site [`src/jevotron/client.py`](https://github.com/ai4curation/jevotron/blob/HEAD/src/jevotron/client.py), read by a model 2026-11-03</sub>

- **[Jevstiller](https://github.com/tomerglick57/Jevstiller)** — Proxy in front of a repeated Jev classification call: it forwards to Jev at first, trains a small local model on Jev's own answers and probabilities, and answers locally once it agrees with Jev on held-out traffic. The author reports 61.7% of Banking77 answered locally at 99.4% agreement. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · tomerglick57 · `Py` · `choice` · `noul` · call site [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/HEAD/jevstiller/teachers/jev.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — grep for what code does: one Noul per code chunk, diff hunk or CSV row, printed as file:line hits with probabilities. --diff gates a PR in CI on a rule written in English (exit 0 match / 1 clean / 2 error); --tests lists the test files a diff can affect.
  <sub>`Project` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · call site [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts), read 2026-09-23 · ⚠ `unverified claims` `self-submitted`</sub>

- **[Laser](https://github.com/iyassr/omarchy-laser)** — Focus-mode plugin for Omarchy and Hyprland on Linux: for each screen it asks Jev whether what is on it serves the task you declared (a noul) and which kind of activity it is (a choice), and when you drift it escalates from a red dot to a nudge, a red edge, a haze, then closing the tab. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · iyassr · `Py` · `noul` · `choice` · call site [`laser/jev.py`](https://github.com/iyassr/omarchy-laser/blob/HEAD/laser/jev.py), read by a model 2026-11-07</sub>

- **[laya-opencv](https://github.com/uu889/laya-opencv)** — Local workbench and installer (Windows, Linux) for decision models. Inspection recipes turn OpenCV measurements into rule checks, then ask Choice, Noul and Score questions of local Laya, TypeSafe's Jev or aiask.me; disagreements and low-confidence answers are flagged for review. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · uu889 · `Py` · `choice` · `noul` · `score` · call site [`app/launcher.py`](https://github.com/uu889/laya-opencv/blob/HEAD/app/launcher.py), read by a model 2026-11-05</sub>

- **[lkclean](https://github.com/stefw/lkclean)** — Chrome extension that cleans up your LinkedIn feed: hides engagement bait, self-promo and off-topic posts using Jev, TypeSafe AI's typed classification model — and explains every decision. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · stefw · `TS` · call site [`src/jev.ts`](https://github.com/stefw/lkclean/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — A local, offline System One server compatible with TypeSafe's Jev API. It answers typed yes/no, category and score questions with small open models. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · amithgc · `Py` · call site [`src/local_jev/ui/app.js`](https://github.com/amithgc/local-jev/blob/HEAD/src/local_jev/ui/app.js), read 2026-09-22</sub>

- **[Natural Language Logic Interpreter](https://github.com/narphorium/nl-logic-interpreter)** — Step-through logic interpreter for facts and rules in plain English: it proves goals by SLD resolution as Prolog does, but Jev does the unification, with a choice on how two sentences relate, nouls on whether they state the same fact and choices that bind each variable to a phrase. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · narphorium · `TS` · `choice` · `noul` · call site [`src/server/aiUnifier.ts`](https://github.com/narphorium/nl-logic-interpreter/blob/HEAD/src/server/aiUnifier.ts), read by a model 2026-11-08</sub>

- **[OnlyRead](https://github.com/onlyreadai/onlyread)** — Chrome extension that keeps browser agents read-only on the sites you pick: rules, per-site decoders and a verdict cache settle most requests, and Jev answers a noul on the rest (does this request create, modify or delete stored data?); code allows, blocks or sends the middle band to a review model. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · onlyreadai · `TS` · `noul` · call site [`extension/src/background/judge/jev.ts`](https://github.com/onlyreadai/onlyread/blob/HEAD/extension/src/background/judge/jev.ts), read by a model 2026-11-08 · ⚠ `self-submitted`</sub>

- **[Parallax](https://github.com/zilize/parallax-dsh)** — DeepSeek Harness plugin for finding the arXiv papers on a topic in a local SQLite corpus: the agent recalls by keyword and combines sets, then Jev screens each paper against the inclusion criteria with a noul (kept at p ≥ 0.5) and sorts papers into topics with nouls or a choice. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · zilize · `TS` · `noul` · `choice` · call site [`src/sets/jev.ts`](https://github.com/zilize/parallax-dsh/blob/HEAD/src/sets/jev.ts), read by a model 2026-11-06</sub>

- **[patrol-jev](https://github.com/patrol-jev/patrol-jev)** — Web app for Korean district-office street patrols: photos go in and a patrol log comes out as text or an .hwpx file. Claude or OpenAI turns each photo into text; Jev files it under one of four log sections, reads whether an address plate shows and judges whether two photos are the same spot. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · patrol-jev · `TS` · `choice` · `noul` · call site [`src/core/jev.ts`](https://github.com/patrol-jev/patrol-jev/blob/HEAD/src/core/jev.ts), read by a model 2026-11-02 · ⚠ `3rd-party key`</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · giuliosmall · `C` · call site [`sql/typesafe.sql`](https://github.com/giuliosmall/pg_typesafe/blob/HEAD/sql/typesafe.sql), read 2026-09-22</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines.
  <sub>`Plugin` · ★10+ · `Py` · `sh` · `choice` · `score` · `noul` · call site [`src/reflex_guard/providers/typesafe.py`](https://github.com/sharziki/semdecide/blob/HEAD/src/reflex_guard/providers/typesafe.py), read 2026-09-22</sub>

- **[sharp](https://github.com/tshmieldev/sharp)** — Filter your X.com feed with Jev or any LLM <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · tshmieldev · `TS` · call site [`src/common/settings.ts`](https://github.com/tshmieldev/sharp/blob/HEAD/src/common/settings.ts), read 2026-09-24</sub>

- **[sift](https://github.com/bohutang/sift)** — Chrome extension that labels every post on X (Substance · Humor · Chit-chat · Promo · Junk · AI-written) with TypeSafe Jev, and hides the ones you don't want. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · bohutang · `JS` · call site [`background.js`](https://github.com/bohutang/sift/blob/HEAD/background.js), read 2026-09-22</sub>

- **[Slop Filter](https://github.com/adamnroman/slop-filter)** — Chrome and Firefox extension that hides AI-written posts and comments on X, LinkedIn, Reddit and YouTube: Jev answers 30 narrow yes/no questions about how each text is written, code counts punctuation and stock words, and weights fitted to your own labels combine them into one score. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · adamnroman · `JS` · `noul` · call site [`src/jev-client.js`](https://github.com/adamnroman/slop-filter/blob/HEAD/src/jev-client.js), read by a model 2026-11-01</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — A Chrome extension that asks whether a DOM element is an advert.
  <sub>`Project` · ★10+ · realzachi · `JS` · call site [`src/typesafe.js`](https://github.com/realZachi/typesafe-adblock/blob/HEAD/src/typesafe.js), read 2026-09-22 · ⚠ `one commit`</sub>

- **[VerdictAD](https://github.com/sgstq0811/VerdictAD-Jev-AD)** — Training-free few-shot industrial anomaly detection: Cloudflare's open Jev-style model Clef-Flash 9B answers noul questions on whether a query image and its local windows show a defect against a few normal references, and the probabilities reweight an existing detector's image score and anomaly map. <sub>(written by a model)</sub>
  <sub>`Jev-like alternative` · ★10+ · sgstq0811 · `Py` · `noul` · cited file [`verdictad/decider.py`](https://github.com/sgstq0811/VerdictAD-Jev-AD/blob/HEAD/verdictad/decider.py), read by a model 2026-11-05 · ⚠ `not Jev itself` `AI-written` `self-submitted`</sub>

- **[vibecheck](https://github.com/jlowin/vibecheck)** — Python library that turns System One calls into plain values: check (yes/no), classify (one option), label (every option that applies) and score, with thresholds, an unsure answer and batching of several questions about the same data. Works against TypeSafe or any compatible server. <sub>(written by a model)</sub>
  <sub>`SDK` · ★10+ · jlowin · `Py` · `noul` · call site [`src/vibecheck/backends.py`](https://github.com/jlowin/vibecheck/blob/HEAD/src/vibecheck/backends.py), read by a model 2026-10-24 · ⚠ `no licence`</sub>

- **[wechat-jev-assistant](https://github.com/yushen100/wechat-jev-assistant)** — A Windows WeChat conversation assistant: reads chats locally, redacts them, has TypeSafe Jev judge them, and keeps an encrypted history.
  <sub>`Project` · ★10+ · yushen100 · `Py` · call site [`src/wechat_jev/typesafe_client.py`](https://github.com/yushen100/wechat-jev-assistant/blob/HEAD/src/wechat_jev/typesafe_client.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · oso95 · `TS` · call site [`src/shared/jev.ts`](https://github.com/oso95/x-scanner/blob/HEAD/src/shared/jev.ts), read 2026-09-22</sub>

- **[xscout](https://github.com/ethan-ab/xscout-jev)** — Watches X for the updates that matter to one profile: Jev classifies each post's topic and speaker, checks exclusions, scores significance and relevance and picks the actions that apply, then deterministic rules add momentum and send big, trending or notable alerts to Slack with a drafting prompt. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · ethan-ab · `TS` · `choice` · `noul` · `score` · call site [`src/jev.ts`](https://github.com/ethan-ab/xscout-jev/blob/HEAD/src/jev.ts), read by a model 2026-11-04 · ⚠ `3rd-party key`</sub>

- **[弦外之音 JevGuide](https://github.com/nisaka520/jevguide)** — Android accessibility app that reads a WeChat chat on screen and asks Jev eight questions in one request: the other person's intent, emotion and urgency, whether a reply is needed or risky, what to do, which reply style fits, and a relationship-progress score. A chat model drafts three replies. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · nisaka520 · `Kt` · `choice` · `score` · `noul` · call site [`app/src/main/java/io/github/nisaka520/jevguide/Prompt.kt`](https://github.com/nisaka520/jevguide/blob/HEAD/app/src/main/java/io/github/nisaka520/jevguide/Prompt.kt), read by a model 2026-10-31 · ⚠ `3rd-party key`</sub>

- **[言外 Yanwai](https://github.com/yirc99/yanwai)** — LSPosed/Xposed module for WeChat on Android: for a chat message and its context it asks Jev, in two rounds of `choice` questions, the sender's emotion (ten options), the chat scene and what reply the conversation is waiting for; an LLM then drafts replies or new topics. It never sends messages. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · yirc99 · `Kt` · `choice` · call site [`app/src/main/java/dev/jev/wechatmood/analysis/JevProtocol.kt`](https://github.com/yirc99/yanwai/blob/HEAD/app/src/main/java/dev/jev/wechatmood/analysis/JevProtocol.kt), read by a model 2026-10-30 · ⚠ `no licence` `3rd-party key`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server: a decision layer for coding agents, built on TypeSafe Jev (System One model). Ship gates, risk checks, file triage that keeps files out of context, and a safe headless browser, with calibrated confidence. For Claude Code, Codex, Cursor. <sub>(upstream description)</sub>
  <sub>`Plugin` · abhishekswe · `TS` · call site [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts), read 2026-09-22</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — AGI JEV Detection — local AI agent monitor: chain-level malicious-agent detection (TypeSafe Jev + Sentinel), escalate-only L1–L5 containment, Neo4j forensics, AngryRobot dashboard. HackSpain 2026. <sub>(upstream description)</sub>
  <sub>`Project` · carlosedm10 · `Py` · call site [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[AI 海龟汤 (AI Turtle Soup)](https://github.com/zerotang05/situation-puzzle)** — Lateral-thinking puzzle game hosted by Jev: each player question gets a choice of Yes, No or Irrelevant, a written solution is ruled Solved, Close or Not yet, and submitted puzzles are reviewed before the public library. A verdict below the confidence threshold goes to a MiniMax model. <sub>(written by a model)</sub>
  <sub>`Project` · zerotang05 · `TS` · `choice` · call site [`packages/jev/src/config.ts`](https://github.com/zerotang05/situation-puzzle/blob/HEAD/packages/jev/src/config.ts), read by a model 2026-11-12</sub>

- **[c9r plugins (browser-check, soft-lint)](https://github.com/c9r-dev/plugins)** — Claude Code and Codex plugins that use Jev as their classifier: browser-check runs a plain-English checklist in a real browser, asking which element each step means (choice) and whether each check holds (noul); soft-lint asks yes/no rules about the lines a diff adds. <sub>(written by a model)</sub>
  <sub>`Plugin` · c9r-dev · `TS` · `choice` · `noul` · call site [`shared/classifier.ts`](https://github.com/c9r-dev/plugins/blob/HEAD/shared/classifier.ts), read by a model 2026-11-13</sub>

- **[ComfyUI System One](https://github.com/dante01yoon/ComfyUI-SystemOne)** — ComfyUI custom nodes that branch a workflow on a typed judgement, such as which style a prompt wants, whether it is too graphic for children or whether it names a real person, with one dropdown switching the backend between Jev, Laya and Cloudflare's Clef. <sub>(written by a model)</sub>
  <sub>`Plugin` · dante01yoon · `Py` · `choice` · `noul` · `score` · call site [`systemone/backends.py`](https://github.com/dante01yoon/ComfyUI-SystemOne/blob/HEAD/systemone/backends.py), read by a model 2026-11-11</sub>

- **[decidekit](https://github.com/debuffjp/decidekit)** — A decision model that runs in the browser or Node: it picks one of your labels for a text with a confidence, learns from an LLM when unsure, and offers the shape of TypeSafe's SDK (client.systemOne({ state, questions })) for choice questions, so code written for Jev can run locally. <sub>(written by a model)</sub>
  <sub>`Jev-like alternative` · debuffjp · `TS` · cited file [`src/typesafe.ts`](https://github.com/debuffjp/decidekit/blob/HEAD/src/typesafe.ts), read by a model 2026-11-13 · ⚠ `not Jev itself` `vendor numbers`</sub>

- **[Decision Lab](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases)** — Site with fifty financial demos that put the same typed choices, scores and nouls about ledgers, orders, fraud, wallets, trades and filings to Jev, grade the answers against known data, and backtest Jev's trade decisions on daily candles; recorded answers replay without a key. <sub>(written by a model)</sub>
  <sub>`Project` · IslamBaraka90 · `JS` · `choice` · `noul` · `score` · call site [`src/services/demo-runner.js`](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases/blob/HEAD/src/services/demo-runner.js), read by a model 2026-11-10</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — Classify an artist's discography by theme, mood, and lyrical complexity with Jev (TypeSafe AI), and view it as a colorful terminal dashboard <sub>(upstream description)</sub>
  <sub>`Project` · lirantal · `JS` · call site [`src/jev.ts`](https://github.com/lirantal/discoprint/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[dsh-fact-check](https://github.com/7starsseeker/dsh-fact-check)** — Fact-check skill for DeepSeek Harness whose optional Jev layer asks factual nouls, such as whether the evidence supports a claim, whether it is enough to stop searching, and whether a source is primary; Jev may only downgrade a claim's tier, never raise it. <sub>(written by a model)</sub>
  <sub>`Plugin` · 7starsseeker · `JS` · `noul` · call site [`tools/jev-verdict.mjs`](https://github.com/7starsseeker/dsh-fact-check/blob/HEAD/tools/jev-verdict.mjs), read by a model 2026-11-11</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrated probabilities (noul/choice/score) for routing/triage/guardrail judgments, no text generation. 把 TypeSafe Jev 决策模型注册为 DSH agent 工具 <sub>(upstream description)</sub>
  <sub>`Plugin` · nanami-0713 · `JS` · call site [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[DuckDB Dual Cognition](https://github.com/prasanthj/duckdb-dual-cognition)** — Native DuckDB extension whose SQL functions ask Jev choices, scores and nouls over every row in batches, including picking a row's foreign key from candidates or answering ambiguous or no_match, and send only rows below a confidence threshold to an OpenAI model for reasoning. <sub>(written by a model)</sub>
  <sub>`Plugin` · prasanthj · `C++` · `choice` · `score` · `noul` · call site [`src/dc_extension.cpp`](https://github.com/prasanthj/duckdb-dual-cognition/blob/HEAD/src/dc_extension.cpp), read by a model 2026-11-11 · ⚠ `3rd-party key`</sub>

- **[DuoMind](https://github.com/j1s4nn/duomind)** — OpenAI-compatible local server that pairs a small llama.cpp model with Jev: 18 decision points before, during and after generation (needs reasoning, safety, format, should stop, needs retry) steer the local model. Prompts go to TypeSafe; generation stays local. <sub>(written by a model)</sub>
  <sub>`Project` · j1s4nn · `Py` · `noul` · `choice` · call site [`src/duomind/jev_client.py`](https://github.com/j1s4nn/duomind/blob/HEAD/src/duomind/jev_client.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[Eikos Arena](https://github.com/caiovicentino/eikos-arena)** — Paper-trading match between the author's open Eikos-27B and Jev on 14 Hyperliquid perpetuals: every 5 minutes both get the same snapshot and 28 questions (a long, flat or short choice and a will-it-rise noul per market), scored on account value and Brier score. <sub>(written by a model)</sub>
  <sub>`Benchmark` · caiovicentino · `Py` · `choice` · `noul` · call site [`arena/arena.py`](https://github.com/caiovicentino/eikos-arena/blob/HEAD/arena/arena.py), read by a model 2026-11-08</sub>

- **[ElBruno.AI.Decisions](https://github.com/elbruno/ElBruno.AI.Decisions)** — One .NET API on NuGet for classification, routing, rubric scoring and proposition checks that returns probability distributions, with a package that calls Jev's POST /v1/systemone natively beside packages for Microsoft's Foundry decision models and local models through Ollama. <sub>(written by a model)</sub>
  <sub>`SDK` · elbruno · `C#` · `choice` · `score` · `noul` · call site [`src/ElBruno.AI.Decisions.Jev/JevClient.cs`](https://github.com/elbruno/ElBruno.AI.Decisions/blob/HEAD/src/ElBruno.AI.Decisions.Jev/JevClient.cs), read by a model 2026-11-11</sub>

- **[Evaluating and Benchmarking the System One Model Jev](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking)** — Code for an arXiv paper that runs Jev zero-shot on 37 public datasets as choices, nouls and scores, against two open-weight LLMs scored on the same requests, plus a sequential track where Jev picks one action per step in five environments such as ALFWorld, TextWorld and FrozenLake. <sub>(written by a model)</sub>
  <sub>`Benchmark` · AppliedMachineLearning-Lab · `Py` · `choice` · `noul` · `score` · call site [`jev_benchmarking/runner.py`](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/blob/HEAD/jev_benchmarking/runner.py), read by a model 2026-11-10</sub>

- **[ex-regex](https://github.com/nothans/ex-regex)** — Python library shaped like the re module whose find, replace, split, filter and extract decide each match by meaning: Jev judges candidate spans of the input, so every match is a verbatim slice with its offsets, never invented text. <sub>(written by a model)</sub>
  <sub>`Project` · nothans · `Py` · `noul` · `choice` · `score` · call site [`src/exregex/backends.py`](https://github.com/nothans/ex-regex/blob/HEAD/src/exregex/backends.py), read by a model 2026-11-11</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — This repository contains a GitHub issue classifier built on Jev, TypeSafe AI's System One model. It labels every new issue with typed values and calibrated confidence in milliseconds, labelling what it is sure about and escalating what it is not. Three guardrail layers guard every write, and a
  <sub>`Project` · kalyanm45 · `Py` · call site [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — A text-moderation demo: one systemOne call screens seven Noul hazards and one severity Score in parallel, and the verdict is computed in code from policy thresholds.
  <sub>`Project` · norbertbodziony · `TS` · call site [`app/api/moderate/route.ts`](https://github.com/NorbertBodziony/guard-jev/blob/HEAD/app/api/moderate/route.ts), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[HekaJev](https://github.com/zurk/hekajev)** — Answers questions about Git history: for each commit it asks Jev the filters written in YAML as nouls and each category set as one choice (or a noul per label), splits large commits, and saves the evidence, answers and cost behind every result in JSONL, logs and an HTML report. <sub>(written by a model)</sub>
  <sub>`Project` · zurk · `Py` · `noul` · `choice` · call site [`src/hekajev/jev.py`](https://github.com/zurk/hekajev/blob/HEAD/src/hekajev/jev.py), read by a model 2026-11-13</sub>

- **[himalaya-jev-mail-classify](https://github.com/initrd/himalaya-jev-mail-classify)** — Label and prioritise Gmail with a language model. Reads mail through himalaya, classifies each thread with Jev (TypeSafe) over OpenRouter, and applies Gmail labels and colours. Dry run by default, idempotent, no state file. <sub>(upstream description)</sub>
  <sub>`Project` · initrd · `Py` · call site [`mail_classify.py`](https://github.com/initrd/himalaya-jev-mail-classify/blob/HEAD/mail_classify.py), read 2026-09-24</sub>

- **[hunch](https://github.com/steven-shoemaker/hunch)** — Ask Jev over columns of data: closed-set questions, cached and joined back. <sub>(upstream description)</sub>
  <sub>`Project` · steven-shoemaker · `Py` · call site [`src/hunch/client.py`](https://github.com/steven-shoemaker/hunch/blob/HEAD/src/hunch/client.py), read 2026-09-24</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — Issue triage that stays quiet when it isn't sure. Calibrated labels, spam and duplicate detection — with abstention. <sub>(upstream description)</sub>
  <sub>`Project` · emreozyoruk · `JS` · call site [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.
  <sub>`Project` · Really Artificial · `JS` · `choice` · `score` · `noul` · call site [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs), read 2026-09-22 · ⚠ `AI-written`</sub>

- **[Jev Persian Benchmark](https://github.com/armanjr/jev-persian-benchmark)** — Benchmark of Jev against open decision models on 480 authored general Persian questions, 560 literary questions and a classical poetry pilot, asked as choices, nouls and scores with raw responses saved and scored locally; Jev leads on choice and noul accuracy. <sub>(written by a model)</sub>
  <sub>`Benchmark` · armanjr · `Py` · `choice` · `noul` · `score` · call site [`jev_benchmark/runner.py`](https://github.com/armanjr/jev-persian-benchmark/blob/HEAD/jev_benchmark/runner.py), read by a model 2026-11-11 · ⚠ `no licence`</sub>

- **[Jev Playwright](https://github.com/arthurfiorette/jev-playwright)** — Playwright reporter that asks Jev which existing end-to-end tests a code change could affect and skips the clearly unrelated ones before any browser starts. Sends changed paths, patches and test bodies by default; its README warns it can miss affected tests. <sub>(written by a model)</sub>
  <sub>`Project` · arthurfiorette · `TS` · call site [`src/config.ts`](https://github.com/arthurfiorette/jev-playwright/blob/HEAD/src/config.ts), read by a model 2026-10-24</sub>

- **[Jev vs. the right baselines](https://github.com/ickma2311/jev-baselines-eval)** — Two pre-registered studies: Jev classifies customer intents on CLINC150 and Banking77 as a choice, as the gate of an escalation cascade, against LLMs and a supervised encoder; the second asks whether, under prompt injection, Jev's confidence separates hijacked decisions from resisted ones. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ickma2311 · `Py` · `choice` · `noul` · call site [`code/common.py`](https://github.com/ickma2311/jev-baselines-eval/blob/HEAD/code/common.py), read by a model 2026-11-10</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能 <sub>(upstream description)</sub>
  <sub>`Plugin` · yuyang2230 · `Py` · call site [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py), read 2026-09-22</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on. <sub>(upstream description)</sub>
  <sub>`Benchmark` · themsquared · `Py` · call site [`bench.py`](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py), read 2026-09-24</sub>

- **[jev-chess](https://github.com/hemanth/jev-chess)** — Chess moves, evaluations, persona opponents, and game classification with TypeSafe AI System One <sub>(upstream description)</sub>
  <sub>`Project` · hemanth · `TS` · call site [`src/typeSafeClient.ts`](https://github.com/hemanth/jev-chess/blob/HEAD/src/typeSafeClient.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-clean](https://github.com/Kunyanli230/jev-clean)** — decision-first data cleaning system powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · kunyanli230 · `Py` · call site [`src/idac/typesafe_client.py`](https://github.com/Kunyanli230/jev-clean/blob/HEAD/src/idac/typesafe_client.py), read 2026-09-24</sub>

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

- **[jev-guard](https://github.com/klauswg/jev-guard)** — Real-time risk triage gateway for exchange deposits and withdrawals — Jev (TypeSafe System One) handles triage only; adjudication stays in deterministic code. <sub>(upstream description)</sub>
  <sub>`Project` · klauswg · `Java` · call site [`src/main/java/com/jevguard/eval/EvalRunner.java`](https://github.com/klauswg/jev-guard/blob/HEAD/src/main/java/com/jevguard/eval/EvalRunner.java), read 2026-09-24</sub>

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

- **[jev-oncall](https://github.com/mingleiw/jev-oncall)** — On-call tooling in which Jev triages each production alert (a noul on whether it is actionable, a severity score, a choice of team and of a duplicate) and, in a root-cause benchmark, picks the next diagnostic check and the supported hypothesis while code enforces budgets. <sub>(written by a model)</sub>
  <sub>`Project` · mingleiw · `Py` · `noul` · `score` · `choice` · call site [`triage.py`](https://github.com/mingleiw/jev-oncall/blob/HEAD/triage.py), read by a model 2026-11-10</sub>

- **[jev-organize](https://github.com/nexibeo/jev-organize)** — Throw in a pile of company files and get them classified and organized by department, type, sensitivity, date, counterparty and PII, with an index for AI agents. Powered by TypeSafe's Jev on OpenRouter (17¢ per 1,000 files). Zero-dependency Node CLI + Claude skill + Codex agent. <sub>(upstream description)</sub>
  <sub>`Plugin` · nexibeo · `JS` · call site [`skills/jev-organize/scripts/src/jev.mjs`](https://github.com/nexibeo/jev-organize/blob/HEAD/skills/jev-organize/scripts/src/jev.mjs), read 2026-09-24</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent. <sub>(upstream description)</sub>
  <sub>`Plugin` · krw82 · `TS` · call site [`src/jev/client.ts`](https://github.com/krw82/jev-playwright-mcp/blob/HEAD/src/jev/client.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-pr-labeler](https://github.com/1jehuang/jev-pr-labeler)** — Semantic GitHub PR labels using Jev's typed decisions, with conceptual scope instead of line counts <sub>(upstream description)</sub>
  <sub>`Project` · 1jehuang · `Py` · call site [`jev_labeler/classifier.py`](https://github.com/1jehuang/jev-pr-labeler/blob/HEAD/jev_labeler/classifier.py), read 2026-09-24</sub>

- **[jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline)** — Daily research monitor for standing questions: deterministic Python owns the loop, TypeSafe Jev screens sources per question, Qwen writes the notes (pilot) <sub>(earlier upstream description)</sub>
  <sub>`Project` · shimo4228 · `Py` · call site [`src/jev_research_pipeline/jev/core.py`](https://github.com/shimo4228/jev-research-pipeline/blob/HEAD/src/jev_research_pipeline/jev/core.py), read 2026-09-24</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — Spring Boot starter for WebFlux: methods marked @SemanticCircuitBreaker send each response body to Jev with a noul on whether an HTTP 200 hides an error, a stack trace or a maintenance notice; above the threshold (0.85 in its example) it raises an exception a circuit breaker can count. Fails open. <sub>(written by a model)</sub>
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

- **[jevcut](https://github.com/VBS2004/jevcut)** — Turns a long video into ranked short clips: code lists every place a clip could start or end, and Jev only judges the clip each candidate edge would make, with nouls on whether it starts or ends mid-thought, stands alone or is an ad, choices among candidates and scores for how it holds attention. <sub>(written by a model)</sub>
  <sub>`Project` · VBS2004 · `Py` · `noul` · `choice` · `score` · call site [`src/jevcut/backends.py`](https://github.com/VBS2004/jevcut/blob/HEAD/src/jevcut/backends.py), read by a model 2026-11-09</sub>

- **[JevEye](https://github.com/Adityakhalkar/JevEye)** — Ask Jev about an image. A CNN reports what it sees with a calibrated confidence or an abstention; Jev judges what it means. <sub>(upstream description)</sub>
  <sub>`Project` · adityakhalkar · `TS` · call site [`src/lib/jev.ts`](https://github.com/Adityakhalkar/JevEye/blob/HEAD/src/lib/jev.ts), read 2026-09-24</sub>

- **[jevgate](https://github.com/gordonbrander/jevgate)** — Command-line gate for shell pipelines: it reads text on stdin and asks Jev one noul about it, such as whether it reports an outage; when P(yes) clears a threshold the text passes through like a grep match, or a command after -- runs, and otherwise nothing comes out. <sub>(written by a model)</sub>
  <sub>`Project` · gordonbrander · `Rs` · `noul` · call site [`src/provider.rs`](https://github.com/gordonbrander/jevgate/blob/HEAD/src/provider.rs), read by a model 2026-11-08</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you own. Discord/Telegram/Reddit bots, CLI, Python, npm, HTTP API, MCP. <sub>(upstream description)</sub>
  <sub>`Plugin` · ohernandezdev · `Py` · call site [`jevmod/judge.py`](https://github.com/ohernandezdev/jevmod/blob/HEAD/jevmod/judge.py), read 2026-09-24</sub>

- **[JEVsnap](https://github.com/brainstormity/jevsnap)** — Screenshot hotkey for macOS, Linux and Windows that blacks out secrets and personal data before the image reaches the clipboard: after local rules, Jev answers nouls on which OCR lines and words to hide, and an optional check finds what is left with box questions. <sub>(written by a model)</sub>
  <sub>`Project` · brainstormity · `TS` · `noul` · `choice` · call site [`desktop/src/core/jevClient.ts`](https://github.com/brainstormity/jevsnap/blob/HEAD/desktop/src/core/jevClient.ts), read by a model 2026-11-10 · ⚠ `one commit`</sub>

- **[JevT++](https://github.com/wiatrM/jevtpp)** — C++20 library that turns runtime text, JSON or objects into enums, booleans and scores through compile-time schemas, with full distributions and explicit abstention. Runs local Laya models in-process (ONNX Runtime or ggml) or Jev through an opt-in remote backend; latency metrics and a Mario demo. <sub>(written by a model)</sub>
  <sub>`SDK` · wiatrm · `C++` · call site [`include/jevt/remote.hpp`](https://github.com/wiatrM/jevtpp/blob/HEAD/include/jevt/remote.hpp), read by a model 2026-10-24</sub>

- **[jevticktrouter](https://github.com/GhrezaKh74/JevTicktRouter)** — A .NET 10 and React 19 application for fast, structured AI-powered ticket triage using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ghrezakh74 · `C#` · call site [`backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs`](https://github.com/GhrezaKh74/JevTicktRouter/blob/HEAD/backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[JevTools](https://github.com/RileyCarney/JevTools)** — A local dashboard and CLI demo for Jev: it scores a product review with a six-question fan-out (scores, nouls and a choice) into a composite, classifies topics (choice) and runs custom decisions, logging every request and answer to a local SQLite file. <sub>(written by a model)</sub>
  <sub>`Project` · RileyCarney · `Py` · `choice` · `noul` · `score` · call site [`jev_demo.py`](https://github.com/RileyCarney/JevTools/blob/HEAD/jev_demo.py), read by a model 2026-11-13</sub>

- **[jevtriage](https://github.com/sathariels/jevtriage)** — GitHub Action + CLI: triage PRs with TypeSafe Jev (ready / needs review / risky) with confidence gates and jevcheck-friendly contracts. <sub>(upstream description)</sub>
  <sub>`Project` · sathariels · `Py` · call site [`src/jevtriage/client.py`](https://github.com/sathariels/jevtriage/blob/HEAD/src/jevtriage/client.py), read 2026-09-24</sub>

- **[JevX](https://github.com/vij-sameerb5/JevX)** — CLI and MCP server that finds hardcoded rules that are really judgement calls and asks Jev, per candidate, nouls on whether it needs judgement, has bounded outcomes and should stay exact code, plus choices for the primitive and kind; strong fits are rewritten with the old rule as fallback. <sub>(written by a model)</sub>
  <sub>`Project` · vij-sameerb5 · `TS` · `noul` · `choice` · call site [`packages/typesafe/src/decision.ts`](https://github.com/vij-sameerb5/JevX/blob/HEAD/packages/typesafe/src/decision.ts), read by a model 2026-11-10 · ⚠ `3rd-party key`</sub>

- **[jlink](https://github.com/keltokhy/jlink)** — Record linkage for economists: write the match rule in plain English, get a probability per pair, audit it, cite it. Python, CLI, Stata and R. <sub>(upstream description)</sub>
  <sub>`Project` · keltokhy · `Py` · call site [`bench/local_models.py`](https://github.com/keltokhy/jlink/blob/HEAD/bench/local_models.py), read 2026-09-24</sub>

- **[krasivo-jev](https://github.com/SergeyBazhmin/krasivo-jev)** — Datasets and training code for open System One models (Qwen3.5-2B with LoRA and a pointer head, trained on 100 Hugging Face datasets), plus an evaluation that asks hosted Jev the same test rows, one choice or noul question each, as the reference for accuracy, NLL and calibration. <sub>(written by a model)</sub>
  <sub>`Benchmark` · SergeyBazhmin · `Py` · `choice` · `noul` · call site [`src/jev_model/typesafe/client.py`](https://github.com/SergeyBazhmin/krasivo-jev/blob/HEAD/src/jev_model/typesafe/client.py), read by a model 2026-11-13 · ⚠ `no licence` `vendor numbers`</sub>

- **[metis](https://github.com/Ayush0054/metis)** — Metis: automatic GitHub issue triage powered by TypeSafe AI Jev. A reusable GitHub Action. <sub>(upstream description)</sub>
  <sub>`Project` · ayush0054 · `Py` · call site [`src/metis_workflow/integrations/jev.py`](https://github.com/Ayush0054/metis/blob/HEAD/src/metis_workflow/integrations/jev.py), read by a model 2026-11-05</sub>

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

- **[OpenJev for opencode](https://github.com/darwintechlab/openjev)** — opencode plugin that gives the agent Jev as tools (jev_choice, jev_noul, jev_score, jev_ask) for the small decisions it would otherwise ask an LLM, such as whether a command is safe or which team gets a ticket. Each answer comes with a gate that acts when confident and escalates when not. <sub>(written by a model)</sub>
  <sub>`Plugin` · darwintechlab · `TS` · `choice` · `noul` · `score` · call site [`src/client.ts`](https://github.com/darwintechlab/openjev/blob/HEAD/src/client.ts), read by a model 2026-11-13</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — Detect semantic stagnation in AI agent loops <sub>(upstream description)</sub>
  <sub>`Project` · ashutoshvjti · `TS` · call site [`experiments/jev-client.ts`](https://github.com/AshutoshVJTI/progressgate/blob/HEAD/experiments/jev-client.ts), read 2026-09-22</sub>

- **[Qualixar Jev Decision Layer](https://github.com/qualixar/jev-decision-layer)** — Plugin and local MCP server that lets an agent hand Jev one closed question at a time, such as which tool, skill or format fits, whether a draft meets its brief, or which team a request belongs to, from 55 recipes; local policy gates check each typed answer and record a receipt. <sub>(written by a model)</sub>
  <sub>`Plugin` · qualixar · `Py` · `choice` · `score` · `noul` · call site [`plugins/qualixar-jev-decision-layer/runtime/jev_auto/providers.py`](https://github.com/qualixar/jev-decision-layer/blob/HEAD/plugins/qualixar-jev-decision-layer/runtime/jev_auto/providers.py), read by a model 2026-11-10</sub>

- **[Social Risk · Qwen3-VL + Jev](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev)** — Research project on misogyny in Chinese image-and-text memes: a LoRA-tuned Qwen3-VL turns each post into structured evidence, and Jev answers one noul under a fixed policy on whether the post attacks or demeans women; code turns the probability into risk bands. <sub>(written by a model)</sub>
  <sub>`Project` · TianJinWeiBoss520 · `Py` · `noul` · call site [`experiments/v1/src/run_ltedi_jev_cloud20.py`](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev/blob/HEAD/experiments/v1/src/run_ltedi_jev_cloud20.py), read by a model 2026-11-10</sub>

- **[tab-bouncer](https://github.com/MANISH007700/tab-bouncer)** — Chrome extension that closes the tabs you don't need, judged by TypeSafe's Jev in one call. Tell it what you're doing; it shows the rest the door. <sub>(upstream description)</sub>
  <sub>`Plugin` · manish007700 · `JS` · call site [`judge.js`](https://github.com/MANISH007700/tab-bouncer/blob/HEAD/judge.js), read 2026-09-24</sub>

- **[TRA](https://github.com/bijectivelabs/bitra)** — Crypto trading desk with deterministic execution. Before a rule's new entry its event guard asks Jev about recent headlines: the event's kind as a choice in two orders, nouls on whether it concerns the asset and the market, and a noul screening machine-addressed instructions. <sub>(written by a model)</sub>
  <sub>`Project` · bijectivelabs · `Py` · `choice` · `noul` · call site [`src/trading_research_agents/llm/providers/typesafe.py`](https://github.com/bijectivelabs/bitra/blob/HEAD/src/trading_research_agents/llm/providers/typesafe.py), read by a model 2026-11-12</sub>

- **[TradingAgents](https://github.com/tauricresearch/tradingagents)** — Multi-agent LLM trading framework. With a TypeSafe key set, its Sentiment Analyst screens each StockTwits or Reddit post with Jev: a noul on whether it is about the instrument, dropped below 0.3, and a choice of the author's stance, bullish, bearish or neutral, counted at confidence 0.5 or more. <sub>(written by a model)</sub>
  <sub>`Project` · tauricresearch · `Py` · `noul` · `choice` · call site [`tradingagents/agents/post_screen.py`](https://github.com/tauricresearch/tradingagents/blob/HEAD/tradingagents/agents/post_screen.py), read by a model 2026-11-12</sub>

- **[triagedy](https://github.com/m0rphtail/triagedy)** — Alert triage as a UNIX filter: JSONL security alerts in, typed decisions out. Runs on TypeSafe Jev or a local model; policy routing stays in code. <sub>(upstream description)</sub>
  <sub>`Project` · m0rphtail · `Rs` · call site [`src/backends/jev.rs`](https://github.com/m0rphtail/triagedy/blob/HEAD/src/backends/jev.rs), read 2026-09-22</sub>

- **[twitter-jev-guard](https://github.com/qs-lll/twitter-jev-guard)** — Uses TypeSafe Jev to spot low-quality, spam and advertising posts on the X/Twitter timeline and stamps a conspicuous translucent watermark over their text.
  <sub>`Plugin` · qs-lll · `JS` · call site [`extension/background.js`](https://github.com/qs-lll/twitter-jev-guard/blob/HEAD/extension/background.js), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — Diffusion-style pixel art out of a general classifier (TypeSafe Jev): 256 parallel pixel questions + refinement passes <sub>(upstream description)</sub>
  <sub>`Project` · wizhill05 · `TS` · call site [`fix_synthesizer.py`](https://github.com/Wizhill05/typesafe-image-diffusion/blob/HEAD/fix_synthesizer.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — Three composable judgment pipelines on TypeSafe's Jev: support-ticket triage, observability alert triage, and a deploy-risk gate. <sub>(upstream description)</sub>
  <sub>`Project` · shivam2003-dev · `Py` · call site [`src/triage/mock.py`](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/HEAD/src/triage/mock.py), read 2026-09-22</sub>

- **[undertone](https://github.com/nuu-maan/undertone)** — Text box that reads a message's tone as you type: one Jev request asks a choice for the overall tone, nouls for passive aggression, sarcasm, over-apologising, pushiness and whether it is safe to send a manager, and scores for urgency and formality; code turns them into a verdict and tips. <sub>(written by a model)</sub>
  <sub>`Project` · nuu-maan · `TS` · `choice` · `noul` · `score` · call site [`src/lib/jev/questions.ts`](https://github.com/nuu-maan/undertone/blob/HEAD/src/lib/jev/questions.ts), read by a model 2026-11-09 · ⚠ `no licence`</sub>

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
