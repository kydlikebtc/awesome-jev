# Human escalation

<sub>[awesome-jev](../../README.md) · [中文](human-escalation.zh-CN.md)</sub>

_Use calibrated confidence to decide what a person must see._

Every catalogued example of this decision — 67 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#human-escalation); [the site](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=en) can filter them further by language, primitive and kind.

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

- **[Confidence](https://docs.typesafe.ai/confidence)** ⭐ — How confidence is derived from the probability distribution, and why a threshold tuned on one question type does not transfer to another.
  <sub>`Official docs`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human.
  <sub>`Integration` · ★46,958 · `Py` · `choice`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.
  <sub>`Project` · ★30,300 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★12,328 · `TS` · `choice` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★582 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — Builds calibrated decision functions from human feedback.
  <sub>`Project` · ★284 · sutro-sh · `Py`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.
  <sub>`Benchmark` · ★190 · `Py` · ⚠ `no licence` `unverified claims`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — The pipe layer of an AI nervous system: one interface connecting provider neurons to an application, across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev or the open-weights Laya, not text.
  <sub>`Plugin` · ★139 · juspay · `TS`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★44 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — An open training and inference stack for Jev-style decision models. Train models to score dynamic candidate branches from a shared prefix, with support for high-cardinality choice, calibration, and fast batched inference.
  <sub>`Jev-like alternative` · ★34 · zwlijay · `Py` · ⚠ `not Jev itself`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial.
  <sub>`Project` · ★31 · smkrv · `TS`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow.
  <sub>`Project` · ★19 · ray-hughes · `Rb`</sub>

- **[jevwire](https://github.com/Brainwires/jevwire)** — Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)
  <sub>`Plugin` · ★18 · brainwires · `TS`</sub>

- **[jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)** — Typed, confidence-aware agent skill routing with TypeSafe Jev.
  <sub>`Plugin` · ★17 · godsboy · `Py`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.
  <sub>`Benchmark` · ★17 · abdelstark · `Py`</sub>

- **[jeval](https://github.com/rlaope/jeval)** — Measures what your Jev classifier's confidence is really worth, and sets the human hand-off line from what a mistake costs.
  <sub>`Project` · ★16 · rlaope · `Py`</sub>

- **[muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook)** — Jev decision layer for Muse: a fast, cheap TypeSafe AI gate before expensive agent work — confidence policy, recipes, reference router, honest measurement.
  <sub>`Plugin` · ★16 · bodila51 · `Py`</sub>

- **[discern](https://github.com/doeixd/discern)** — Craft Type-Safe Uncertainty-aware semantic pattern matching, control flow, and smart procedures for Effect DecisionModel and Jev
  <sub>`Project` · ★12 · doeixd · `TS`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.
  <sub>`Project` · ★12 · antoniocoppe · `TS`</sub>

- **[jevcal](https://github.com/abhixhek/jevcal)** — Calibrate, threshold and drift-check a decision model against an LLM teacher instead of guessing a cutoff.
  <sub>`Project` · ★10 · abhixhek · `Py`</sub>

- **[jevflow](https://github.com/Mawfyy/jevflow)** — Probabilistic AI decisions as composable backend primitives — typed judgments (noul/score/choice), deterministic thresholds, and explainable workflows. Powered by TypeSafe's Jev, provider-agnostic.
  <sub>`Integration` · ★9 · mawfyy · `TS` · ⚠ `no licence`</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Local-first, SQLite receipts, zero dependencies.
  <sub>`Project` · ★9 · romiluz13 · `Py`</sub>

- **[typesafe-local](https://github.com/aabolfazl/typesafe-local)** — Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.
  <sub>`Project` · ★8 · aabolfazl · `Py`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows
  <sub>`Benchmark` · ★7 · jmanhype · `Py`</sub>

- **[luce](https://github.com/scienthoon/luce)** — Luce: a recipe for calibrated decision models — a sentence about your task in, a small model that answers typed questions with honest probabilities out (init → synth → train → eval → serve)
  <sub>`Project` · ★7 · scienthoon · `Py`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.170→0.071). Typed decisions, runs offline, no API key, no waitlist.
  <sub>`Jev-like alternative` · ★7 · rupeshpoojary9 · `Py` · ⚠ `not Jev itself`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill
  <sub>`Plugin` · ★6 · docxology · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through.
  <sub>`Project` · ★6 · ufec · `Kt`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · ★6 · scienthoon · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.
  <sub>`Benchmark` · ★5 · anisselbd · `Py` · ⚠ `no licence`</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic
  <sub>`Project` · ★5 · kenhuangus · `Py`</sub>

- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** — Jev-shaped typed-decision model (state + Choice/Score/Noul questions -> calibrated probabilities, one pass) on ModernBERT / DeBERTa / LLaDA-MoE, with measured latency, accuracy, calibration and training cost
  <sub>`Project` · ★5 · kotoba-lang · `Py`</sub>

- **[opencode-jev-orchestrator](https://github.com/aaronshaf/opencode-jev-orchestrator)** — Keeps OpenCode on a cheap sticky model for warm cache; Jev escalates hard turns to stronger subagents.
  <sub>`Project` · ★4 · aaronshaf · `TS`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B
  <sub>`Jev-like alternative` · ★4 · shamazharikh · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[system-one-gemma](https://github.com/akash-kamat/system-one-gemma)** — Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.
  <sub>`Jev-like alternative` · ★4 · akash-kamat · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[tink-route](https://github.com/jon-devlapaz/tink-route)** — Dynamic, confidence-aware Agent Skill routing with TypeSafe Jev and Tink
  <sub>`Plugin` · ★4 · jon-devlapaz · `Py`</sub>

- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** — open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model. AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests. Jev evaluates state and outputs calibrated probabilities. Works with Cursor, Wind
  <sub>`Plugin` · ★3 · ravinder82 · `TS`</sub>

- **[jev-ui](https://github.com/etweisberg/jev-ui)** — React components that resolve which component to render, how to order a list, and whether to show an affordance — from calibrated judgments returned by TypeSafe's Jev.
  <sub>`Project` · ★3 · etweisberg · `TS` · ⚠ `no licence`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.
  <sub>`Plugin` · ★3 · legacybridge-tech · `TS`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score / Noul questions, lint them, measure on labelled data, and put calibrated thresholds in code
  <sub>`Plugin` · ★3 · simota · `TS`</sub>

- **[grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard)** — A typed preflight and approval layer for Grok Bot: local policy owns the hard boundaries, Jev judges the ambiguous cases, and Grok Bot executes within the envelope it gets back.
  <sub>`Project` · ★2 · 0xwhrari · `Py`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — MCP server for Jev (TypeSafe System One): the three official question types — choice, score, noul — plus batch classify. Calibrated probabilities, ~0.5s, <$0.001/call.
  <sub>`Plugin` · ★2 · wangkuangkuang · `Py`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.
  <sub>`Plugin` · ★2 · hamakyo · `TS`</sub>

- **[jevbus](https://github.com/zkjoie/jevbus)** — A streaming event bus whose routing, subscription and consumption are decided by a probabilistic judge. The reference judge is TypeSafe AI's Jev (System One) model: send it a payload and a set of typed questions, get back calibrated probabilities instead of prose.
  <sub>`Project` · ★2 · zkjoie · `Rs`</sub>

- **[opencode-jev-guard](https://github.com/CogFlux/opencode-jev-guard)** — OpenCode 2 plugin that sends every shell command (local or via FarHand) to TypeSafe's Jev and asks you first when it leaves files outside the project, installs software globally, changes global settings, is harmful or exposes private data
  <sub>`Plugin` · ★2 · cogflux · `TS`</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Code hook
  <sub>`Plugin` · ★2 · riskaversetech · `TS`</sub>

- **[toolgate](https://github.com/ndolinschi/toolgate)** — Agent tool/MCP call gate — allow / ask_human / deny via TypeSafe Jev
  <sub>`Plugin` · ★2 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[watfile](https://github.com/jexp/watfile)** — Text/PDF - File categorization and sorting with Typesafe AI Jev or local calibrated decision model
  <sub>`Project` · ★2 · jexp · `Py` · ⚠ `no licence`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost
  <sub>`Benchmark` · ★1 · 4esv · `Py` · ⚠ `no licence`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed.
  <sub>`Project` · ★1 · jyatesdotdev · `Py`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev.
  <sub>`Benchmark` · ★1 · zsavage8 · `Py`</sub>

- **[qualm](https://github.com/qddegtya/qualm)** — Typed decisions from a System One model, where uncertainty is something you have to handle.
  <sub>`Project` · ★1 · qddegtya · `TS`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full.
  <sub>`Project` · ★0 · jourdanlabs · `Py` · ⚠ `no licence`</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — Routing with an act-or-escalate gate, where the policy function is deliberately left unimplemented because the thresholds are yours to choose.
  <sub>`Snippet` · `Py` · `choice` · ⚠ `code untested`</sub>

- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** — A twenty-questions guesser that keeps asking until Jev's calibrated confidence crosses a threshold — or gives up and says so
  <sub>`Project` · ★0 · mintannn · `TS`</sub>

- **[jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit)** — Independent API-only calibration audit of TypeSafe AI's Jev decision model
  <sub>`Benchmark` · ★0 · jujumilk3 · `Py`</sub>

- **[jev-guard](https://github.com/CMaintz/jev-guard)** — Vets an LLM agent's tool calls through TypeSafe AI's Jev before they run — allow, block, or hold, failing safe on uncertainty.
  <sub>`Project` · ★0 · cmaintz · `TS`</sub>

- **[jev-review](https://github.com/thiago-ss/jev-review)** — Autonomous Jev pull-request review with typed decisions, calibrated approval gates, and trusted-owner escalation
  <sub>`Project` · ★0 · thiago-ss · `Py` · ⚠ `no licence`</sub>

- **[jev-the-janitor](https://github.com/kylehovance-ai/jev-the-janitor)** — A janitor for markdown vaults powered by TypeSafe Jev: Jev votes on each note, your code files it, you review the low-confidence pile.
  <sub>`Project` · ★0 · kylehovance-ai · `Py`</sub>

- **[n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** — n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibrated probabilities
  <sub>`Project` · ★0 · dommonte · `TS`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.
  <sub>`Benchmark` · Lindfors</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
