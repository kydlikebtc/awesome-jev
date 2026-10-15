# Human escalation

<sub>[awesome-jev](../../README.md) · [中文](human-escalation.zh-CN.md)</sub>

_Use calibrated confidence to decide what a person must see._

Every catalogued example of this decision — 69 of them. The same rows, with caveats, are in [the index](../../README.md#human-escalation); [the site](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#human-escalation): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 7 · call site 54 · wire shape 5 · example only 0 · independent reports 10 · negative results 0 · no file cited 10. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) <sub>`Official docs` · `Py` · `score`</sub>
- [Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) <sub>`Official docs` · `Py` · `noul`</sub>
- [Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) <sub>`Official docs` · `Py`</sub>
- [Confidence](https://docs.typesafe.ai/confidence) <sub>`Official docs`</sub>

## Examples in this repository

Code under this repository's [`examples/`](../../examples/) filed under this pattern. Each is also listed below, with its summary; [the examples' README](../../examples/README.md) says how far they have been checked.

- [Example: confidence-gated escalation](../../examples/02-confidence-gate/main.py) <sub>`Snippet` · `Py` · `choice` · ⚠ `code untested`</sub>

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐ — Routes uncertain probabilities to human review while keeping the underlying noul values visible rather than collapsing them to a label.
  <sub>`Official docs` · `Py` · `noul`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it.
  <sub>`Official docs` · `Py`</sub>

- **[Confidence](https://docs.typesafe.ai/confidence)** ⭐ — How Choice and Score confidence is derived from probabilities, how Noul differs, and how to tune thresholds for the question and application.
  <sub>`Official docs`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human.
  <sub>`Integration` · ★10k+ · `Py` · `choice`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.
  <sub>`Project` · ★10k+ · `Py` · `choice` · call site [`python/providers/typesafe/composio_typesafe/provider.py`](https://github.com/ComposioHQ/composio/blob/HEAD/python/providers/typesafe/composio_typesafe/provider.py), read 2026-09-22</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★10k+ · `TS` · `choice` · `noul` · call site [`apps/web/utils/decision-model/typesafe.ts`](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/typesafe.ts), read 2026-09-22</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — Builds calibrated decision functions from human feedback.
  <sub>`Project` · ★100+ · sutro-sh · `Py` · call site [`src/jev_align/jev.py`](https://github.com/sutro-sh/jev-align/blob/HEAD/src/jev_align/jev.py), read 2026-09-22</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — An open training and inference stack for Jev-style decision models. Train models to score dynamic candidate branches from a shared prefix, with support for high-cardinality choice, calibration, and fast batched inference. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · zwlijay · `Py` · cited file [`jevforge/bench_jev.py`](https://github.com/zwliJay/jev-forge/blob/HEAD/jevforge/bench_jev.py), read 2026-09-22 · ⚠ `not Jev itself` `one commit`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★100+ · `TS` · `choice` · `score` · `noul` · call site [`src/review/codebase-judgments.ts`](https://github.com/devagrawal09/jev-review/blob/HEAD/src/review/codebase-judgments.ts), read 2026-09-22</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — The pipe layer of an AI nervous system: one interface connecting provider neurons to an application, across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev, not text.
  <sub>`Plugin` · ★100+ · juspay · `TS` · call site [`src/lib/providers/typesafe.ts`](https://github.com/juspay/neurolink/blob/HEAD/src/lib/providers/typesafe.ts), read 2026-09-22</sub>

- **[discern](https://github.com/doeixd/discern)** — Craft Type-Safe Uncertainty-aware semantic pattern matching, control flow, and smart procedures for Effect DecisionModel and Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · doeixd · `TS` · call site [`examples/headline.ts`](https://github.com/doeixd/discern/blob/HEAD/examples/headline.ts), read 2026-09-22</sub>

- **[jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)** — Typed, confidence-aware agent skill routing with TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · godsboy · `Py` · call site [`src/jev_router/transport.py`](https://github.com/GodsBoy/jev-agent-skill-router/blob/HEAD/src/jev_router/transport.py), read 2026-09-22</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · abdelstark · `Py` · call site [`src/jev_benchmarks/adapters/jev.py`](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/src/jev_benchmarks/adapters/jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · smkrv · `TS` · call site [`src/client.ts`](https://github.com/smkrv/jev-calibrate/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · jmanhype · `Py` · call site [`src/jev_dspy_lab/live.py`](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/src/jev_dspy_lab/live.py), read 2026-09-22</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · antoniocoppe · `TS` · call site [`demos/proof/row-filter/run.ts`](https://github.com/AntonioCoppe/jev-harness/blob/HEAD/demos/proof/row-filter/run.ts), read 2026-09-22</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★10+ · brainstormity · `Py` · `choice` · `noul` · call site [`typesafe/__init__.py`](https://github.com/brainstormity/Jev-Moderation-Bot/blob/HEAD/typesafe/__init__.py), read 2026-09-22</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kenhuangus · `Py` · call site [`src/jev_usecases/client.py`](https://github.com/kenhuangus/jev-usecases/blob/HEAD/src/jev_usecases/client.py), read 2026-09-22</sub>

- **[jeval](https://github.com/rlaope/jeval)** — Measures what your Jev classifier's confidence is really worth, and sets the human hand-off line from what a mistake costs. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · rlaope · `Py` · call site [`jeval/collect.py`](https://github.com/rlaope/jeval/blob/HEAD/jeval/collect.py), read 2026-09-24</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ray-hughes · `Rb` · call site [`lib/jevalyn/configuration.rb`](https://github.com/Ray-Hughes/jevalyn/blob/HEAD/lib/jevalyn/configuration.rb), read 2026-09-22</sub>

- **[jevcal](https://github.com/abhixhek/jevcal)** — Calibrate, threshold and drift-check a decision model against an LLM teacher instead of guessing a cutoff.
  <sub>`Project` · ★10+ · abhixhek · `Py` · call site [`src/jevcal/providers/typesafe.py`](https://github.com/abhixhek/jevcal/blob/HEAD/src/jevcal/providers/typesafe.py), read 2026-09-22</sub>

- **[jevflow](https://github.com/Mawfyy/jevflow)** — Probabilistic AI decisions as composable backend primitives — typed judgments (noul/score/choice), deterministic thresholds, and explainable workflows. Powered by TypeSafe's Jev, provider-agnostic. <sub>(upstream description)</sub>
  <sub>`Integration` · ★10+ · mawfyy · `TS` · call site [`packages/provider-jev/src/index.ts`](https://github.com/Mawfyy/jevflow/blob/HEAD/packages/provider-jev/src/index.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Local-first, SQLite receipts, zero dependencies. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · romiluz13 · `Py` · call site [`jevmory/cli.py`](https://github.com/romiluz13/jevmory/blob/HEAD/jevmory/cli.py), read 2026-09-22</sub>

- **[jevwire](https://github.com/Brainwires/jevwire)** — Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev) <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · brainwires · `TS` · call site [`src/jev/client.ts`](https://github.com/Brainwires/jevwire/blob/HEAD/src/jev/client.ts), read 2026-09-22</sub>

- **[muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook)** — Jev decision layer for Muse: a fast, cheap TypeSafe AI gate before expensive agent work — confidence policy, recipes, reference router, honest measurement. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · bodila51 · `Py` · call site [`src/jev_client.py`](https://github.com/Bodila51/muse-jev-playbook/blob/HEAD/src/jev_client.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.170→0.071). Typed decisions, runs offline, no API key, no waitlist. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · rupeshpoojary9 · `Py` · cited file [`crossbench/jev_client.py`](https://github.com/rupeshpoojary9/poorjev/blob/HEAD/crossbench/jev_client.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Code hook <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · riskaversetech · `TS` · call site [`src/backends/typesafe.ts`](https://github.com/RiskAverseTech/toolgate/blob/HEAD/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** — Jev-shaped typed-decision model (state + Choice/Score/Noul questions -> calibrated probabilities, one pass) on ModernBERT / DeBERTa / LLaDA-MoE, with measured latency, accuracy, calibration and training cost <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kotoba-lang · `Py` · call site [`src/typed_decisions/jev_holes.py`](https://github.com/kotoba-lang/typed-decisions/blob/HEAD/src/typed_decisions/jev_holes.py), read 2026-09-22</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full. <sub>(upstream description)</sub>
  <sub>`Project` · jourdanlabs · `Py` · call site [`harness/run.py`](https://github.com/jourdanlabs/assay-001/blob/HEAD/harness/run.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill <sub>(upstream description)</sub>
  <sub>`Plugin` · docxology · `Py` · call site [`src/daf_jev/client.py`](https://github.com/docxology/daf-jev/blob/HEAD/src/daf_jev/client.py), read 2026-09-22</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — Routing with an act-or-escalate gate, where the policy function is deliberately left unimplemented because the thresholds are yours to choose.
  <sub>`Snippet` · `Py` · `choice` · call site [`examples/02-confidence-gate/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/02-confidence-gate/main.py), read 2026-09-22 · ⚠ `code untested`</sub>

- **[grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard)** — A typed preflight and approval layer for Grok Bot: local policy owns the hard boundaries, Jev judges the ambiguous cases, and Grok Bot executes within the envelope it gets back.
  <sub>`Project` · 0xwhrari · `Py` · call site [`src/grok_jev_guard/jev.py`](https://github.com/0xwhrari/grok-jev-guard/blob/HEAD/src/grok_jev_guard/jev.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** — A twenty-questions guesser that keeps asking until Jev's calibrated confidence crosses a threshold — or gives up and says so <sub>(upstream description)</sub>
  <sub>`Project` · mintannn · `TS` · call site [`lib/jev.ts`](https://github.com/mintannn/jev-asks-until-sure/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through. <sub>(upstream description)</sub>
  <sub>`Project` · ufec · `Kt` · call site [`app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt`](https://github.com/ufec/jev-block-android-ad/blob/HEAD/app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt), read 2026-09-22</sub>

- **[jev-calibration-audit](https://github.com/tapesymbolstate/jev-calibration-audit)** — Independent API-only calibration audit of TypeSafe AI's Jev decision model <sub>(upstream description)</sub>
  <sub>`Benchmark` · jujumilk3 · `Py` · call site [`src/jev_audit/client.py`](https://github.com/tapesymbolstate/jev-calibration-audit/blob/HEAD/src/jev_audit/client.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost
  <sub>`Benchmark` · 4esv · `Py` · call site [`evaljev/runners.py`](https://github.com/4esv/jev-eval/blob/HEAD/evaljev/runners.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** — open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model. AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests. Jev evaluates state and outputs calibrated probabilities. Works with Cursor, Wind
  <sub>`Plugin` · ravinder82 · `TS` · call site [`dist/index.js`](https://github.com/Ravinder82/jev-flash-router/blob/HEAD/dist/index.js), read 2026-09-22</sub>

- **[jev-guard](https://github.com/CMaintz/jev-guard)** — Vets an LLM agent's tool calls through TypeSafe AI's Jev before they run — allow, block, or hold, failing safe on uncertainty. <sub>(upstream description)</sub>
  <sub>`Project` · cmaintz · `TS` · call site [`src/providers/typesafe.ts`](https://github.com/CMaintz/jev-guard/blob/HEAD/src/providers/typesafe.ts), read 2026-09-24 · ⚠ `archived`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed. <sub>(upstream description)</sub>
  <sub>`Project` · jyatesdotdev · `Py` · call site [`logtriage/cli.py`](https://github.com/jyatesdotdev/jev-logtriage/blob/HEAD/logtriage/cli.py), read 2026-09-22</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — MCP server for Jev (TypeSafe System One): the three official question types — choice, score, noul — plus batch classify. Calibrated probabilities, ~0.5s, <$0.001/call. <sub>(upstream description)</sub>
  <sub>`Plugin` · wangkuangkuang · `Py` · call site [`src/jev_mcp_server/config.py`](https://github.com/wangkuangkuang/jev-mcp-server/blob/HEAD/src/jev_mcp_server/config.py), read 2026-09-22</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · scienthoon · `Py` · call site [`scripts/jev_eval.mjs`](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark. <sub>(upstream description)</sub>
  <sub>`Benchmark` · anisselbd · `Py` · call site [`run_jev.py`](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/run_jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here) · ⚠ `no licence`</sub>

- **[jev-review](https://github.com/thiago-ss/jev-review)** — Autonomous Jev pull-request review with typed decisions, calibrated approval gates, and trusted-owner escalation <sub>(upstream description)</sub>
  <sub>`Project` · thiago-ss · `Py` · call site [`jev_review/provider.py`](https://github.com/thiago-ss/jev-review/blob/HEAD/jev_review/provider.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps. <sub>(upstream description)</sub>
  <sub>`Plugin` · hamakyo · `TS` · call site [`src/providers/jev-provider.ts`](https://github.com/hamakyo/jev-starter/blob/HEAD/src/providers/jev-provider.ts), read 2026-09-22</sub>

- **[jev-the-janitor](https://github.com/kylehovance-ai/jev-the-janitor)** — A janitor for markdown vaults powered by TypeSafe Jev: Jev votes on each note, your code files it, you review the low-confidence pile.
  <sub>`Project` · kylehovance-ai · `Py` · call site [`janitor/client.py`](https://github.com/kylehovance-ai/jev-the-janitor/blob/HEAD/janitor/client.py), read 2026-09-22</sub>

- **[jev-ui](https://github.com/etweisberg/jev-ui)** — React components that resolve which component to render, how to order a list, and whether to show an affordance — from calibrated judgments returned by TypeSafe's Jev. <sub>(upstream description)</sub>
  <sub>`Project` · etweisberg · `TS` · call site [`packages/jev-ui/src/transport/live.ts`](https://github.com/etweisberg/jev-ui/blob/HEAD/packages/jev-ui/src/transport/live.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevbench](https://github.com/GautamTalksDev/jevbench)** — Preregistered, bias-corrected test of TypeSafe Jev's calibration under human disagreement (ChaosNLI, 100 labels per item) <sub>(upstream description)</sub>
  <sub>`Benchmark` · Gautam Khosla · `Py` · `choice` · `noul` · call site [`jevbench/clients/jev.py`](https://github.com/GautamTalksDev/jevbench/blob/HEAD/jevbench/clients/jev.py) · author's conclusion: mixed (author-stated, not reproduced here) · ⚠ `AI-written` `self-submitted`</sub>

- **[jevbus](https://github.com/zkjoie/jevbus)** — A streaming event bus whose routing, subscription and consumption are decided by a probabilistic judge. The reference judge is TypeSafe AI's Jev (System One) model: send it a payload and a set of typed questions, get back calibrated probabilities instead of prose. <sub>(upstream description)</sub>
  <sub>`Project` · zkjoie · `Rs` · call site [`src/jev/http.rs`](https://github.com/zkjoie/jevbus/blob/HEAD/src/jev/http.rs), read 2026-09-22</sub>

- **[luce](https://github.com/scienthoon/luce)** — Luce: a recipe for calibrated decision models — a sentence about your task in, a small model that answers typed questions with honest probabilities out (init → synth → train → eval → serve) <sub>(upstream description)</sub>
  <sub>`Project` · scienthoon · `Py` · call site [`scripts/jev_eval.mjs`](https://github.com/scienthoon/luce/blob/HEAD/scripts/jev_eval.mjs), read 2026-09-22</sub>

- **[n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** — n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibrated probabilities <sub>(upstream description)</sub>
  <sub>`Project` · dommonte · `TS` · call site [`nodes/TypeSafeAi/constants.ts`](https://github.com/DomMonte/n8n-nodes-typesafe-ai/blob/HEAD/nodes/TypeSafeAi/constants.ts), read 2026-09-22</sub>

- **[opencode-jev-guard](https://github.com/CogFlux/opencode-jev-guard)** — OpenCode 2 plugin that sends every shell command (local or via FarHand) to TypeSafe's Jev and asks you first when it leaves files outside the project, installs software globally, changes global settings, is harmful or exposes private data <sub>(upstream description)</sub>
  <sub>`Plugin` · cogflux · `TS` · call site [`jev-guard.ts`](https://github.com/CogFlux/opencode-jev-guard/blob/HEAD/jev-guard.ts), read 2026-09-24</sub>

- **[opencode-jev-orchestrator](https://github.com/aaronshaf/opencode-jev-orchestrator)** — Keeps OpenCode on a cheap sticky model for warm cache; Jev escalates hard turns to stronger subagents. <sub>(upstream description)</sub>
  <sub>`Project` · aaronshaf · `TS` · call site [`src/jev.ts`](https://github.com/aaronshaf/opencode-jev-orchestrator/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Benchmark` · zsavage8 · `Py` · call site [`scripts/run_baseline.py`](https://github.com/zsavage8/padflow-jev-evals/blob/HEAD/scripts/run_baseline.py), read 2026-09-22</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions. <sub>(upstream description)</sub>
  <sub>`Plugin` · legacybridge-tech · `TS` · call site [`src/client.ts`](https://github.com/legacybridge-tech/pi-typesafe-jev/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[qualm](https://github.com/qddegtya/qualm)** — Typed decisions from a System One model, where uncertainty is something you have to handle. <sub>(upstream description)</sub>
  <sub>`Project` · qddegtya · `TS` · call site [`src/client.ts`](https://github.com/qddegtya/qualm/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · shamazharikh · `Py` · cited file [`scripts/bench_fork.py`](https://github.com/shamazharikh/qwen-rlcd/blob/HEAD/scripts/bench_fork.py), read 2026-09-22 · ⚠ `not Jev itself` `no licence`</sub>

- **[system-one-gemma](https://github.com/akash-kamat/system-one-gemma)** — Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · akash-kamat · `Py` · cited file [`system_one.py`](https://github.com/akash-kamat/system-one-gemma/blob/HEAD/system_one.py), read 2026-09-22 · ⚠ `not Jev itself` `no licence`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score / Noul questions, lint them, measure on labelled data, and put calibrated thresholds in code <sub>(upstream description)</sub>
  <sub>`Plugin` · simota · `TS` · call site [`skills/tenbin/scripts/evaluate.py`](https://github.com/simota/tenbin/blob/HEAD/skills/tenbin/scripts/evaluate.py), read 2026-09-22</sub>

- **[tink-route](https://github.com/jon-devlapaz/tink-route)** — Dynamic, confidence-aware Agent Skill routing with TypeSafe Jev and Tink <sub>(upstream description)</sub>
  <sub>`Plugin` · jon-devlapaz · `Py` · call site [`src/tink_route/core/constants.py`](https://github.com/jon-devlapaz/tink-route/blob/HEAD/src/tink_route/core/constants.py), read 2026-09-24</sub>

- **[toolgate](https://github.com/ndolinschi/toolgate)** — Agent tool/MCP call gate — allow / ask_human / deny via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/toolgate/blob/HEAD/src/lib/jev.ts), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[typesafe-local](https://github.com/aabolfazl/typesafe-local)** — Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon. <sub>(upstream description)</sub>
  <sub>`Project` · aabolfazl · `Py` · call site [`ots/server.py`](https://github.com/aabolfazl/typesafe-local/blob/HEAD/ots/server.py), read 2026-09-22</sub>

- **[watfile](https://github.com/jexp/watfile)** — Text/PDF - File categorization and sorting with Typesafe AI Jev or local calibrated decision model <sub>(upstream description)</sub>
  <sub>`Project` · jexp · `Py` · call site [`src/watfile/classifier/jev.py`](https://github.com/jexp/watfile/blob/HEAD/src/watfile/classifier/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — A local decision layer in Jev's shape: yes/no, choice and rubric questions read off one token's logprobs from a local model, with a Claude Code permission gate measured on held-out command sets.
  <sub>`Jev-like alternative` · Xinyu Liu · `TS` · `noul` · `choice` · `score` · cited file [`src/gate.ts`](https://github.com/liu-x27/XavierJev/blob/HEAD/src/gate.ts), read 2026-09-25 · ⚠ `not Jev itself` `AI-written`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.
  <sub>`Benchmark` · ★100+ · ⚠ `no licence` `unverified claims`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.
  <sub>`Benchmark` · Lindfors</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
