<!--
  This file is generated from catalog.json. Edit the catalog, then run `python3 scripts/build_readme.py`.
-->

<a name="top"></a>
<a name="awesome-jev"></a>
<a name="-awesome-jev"></a>

<a href="https://kydlikebtc.github.io/awesome-jev/?lang=en">
<picture>
  <source media="(min-width: 768px) and (prefers-color-scheme: light)" srcset="docs/assets/readme-cover-en-light.svg">
  <source media="(max-width: 767px) and (prefers-color-scheme: light)" srcset="docs/assets/readme-cover-en-light-mobile.svg">
  <source media="(max-width: 767px)" srcset="docs/assets/readme-cover-en-dark-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-cover-en-dark.svg">
  <img src="docs/assets/readme-cover-en-light.svg" alt="awesome-jev — Jev Decision Atlas: 1,208 public resources, 1,205 dated HTTP 2xx link records, and 1,122 call-site citation records. Counts describe saved records, not current link availability or passed runtime and performance tests." width="100%">
</picture>
</a>

<p align="center">
<a href="https://kydlikebtc.github.io/awesome-jev/?lang=en"><kbd>&nbsp;<b>Explore&nbsp;the&nbsp;catalogue&nbsp;↗</b>&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=first-call&amp;lang=en"><kbd>&nbsp;First&nbsp;call&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=build&amp;lang=en"><kbd>&nbsp;Adapt&nbsp;a&nbsp;project&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=measured&amp;lang=en"><kbd>&nbsp;Independent&nbsp;reports&nbsp;</kbd></a>
<a href="README.zh-CN.md"><kbd>&nbsp;中文&nbsp;</kbd></a>
</p>

<p align="center"><sub>Counts describe saved link and evidence records, not current CI passes or runtime tests. <a href="#what-is-verified-and-what-is-not">About these counts</a></sub></p>

<details>
<summary><b>On this page · full reading map</b></summary>

[Patterns](docs/patterns.md) · [Compatibility](docs/compatibility.md) · [Vetting](docs/vetting.md)

- 01 [What this is](#what-this-is)
- 02 [What Jev returns](#what-jev-returns)
- 03 [Start here](#start-here)
- 04 [Coverage](#coverage)
- 05 [Measured, not claimed](#measured-not-claimed)
- 06 [By decision pattern](#by-decision-pattern)
- 07 [By resource kind](#by-resource-kind)
- 08 [Also in this repo](#also-in-this-repo)
- 09 [What is verified, and what is not](#what-is-verified-and-what-is-not)
- 10 [Machine-readable data](#machine-readable-data)
- 11 [Contributing and licence](#contributing-and-licence)

</details>

---

## What this is

- **Jev** is a decision model from TypeSafe AI. It does not write text — you hand it state plus typed questions and it returns typed answers with calibrated confidence, fast and cheap enough to sit in an agent's inner loop.
- **This repo** indexes public examples of using it, organised by the *decision* being made. The resource you read this week is disposable; the decision pattern is not.
- **How to assess it:** every row names its source. Call-site citations, primitive claims and caveats are recorded where available, so you can inspect what was read and what remains untested.

> [!NOTE]
> Not the product, not an SDK, not affiliated with TypeSafe AI, and not a recommendation. Inclusion is a source record, not a runtime or performance endorsement. See [what is verified](#what-is-verified-and-what-is-not).

## What Jev returns

Three primitives. Every pattern below is built out of them, and the asymmetry in the last row is the single most common source of bugs.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/primitives-en-dark.svg">
  <img src="docs/assets/primitives-en-light.svg" alt="Three panels describing the choice, score and noul primitives and what each returns" width="660">
</picture>

Input is **text only** — string, JSON object, or array of text. Context is **64k** tokens per request, **32k** for the state plus the longest question. Output tokens are free. There are no published weights, so it cannot be run locally. Full cross-platform differences: [`docs/compatibility.md`](docs/compatibility.md).

## Start here

Six things in reading order. Hand-picked, because "most starred" is not the same as "read this first".

1. **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)**

   The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.

2. **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)**

   The most useful page in the docs and the least linked. It explains, among other things, that a Choice over options and one Noul per option answer different questions.

3. **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**

   Written from the official API reference and checked field by field against it, but not executed against the live API.

4. **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**

   Exactly two nouls per tool call: does knowing this call happened still matter, and is the full output still needed verbatim. Despite the word "scored" in its own description, no score primitive is used.

5. **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**

   The best structured tutorial found. It states plainly that typed output does not guarantee a correct decision, lists the documented weaknesses, and qualifies its own cost illustration rather than selling it.

6. **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**

   The single most credible row in this catalog. Recall came out below their existing summariser, and at a matched context budget it tied plain recency ordering. Cost was genuinely far lower. Publishing a negative result on a hyped model is rare.

## Coverage

Every decision pattern, sized by how many entries this catalogue contains. Use the pattern index below the chart to jump to a section. A zero is a research gap, not a rendering bug.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/coverage-en-dark.svg">
  <img src="docs/assets/coverage-en-light.svg" alt="Horizontal bar chart of how many catalog examples exist for each of the eighteen decision patterns" width="100%">
</picture>

All 18 patterns have at least one catalogue entry. Coverage does not imply runtime testing or equal maturity. See [`docs/status.md`](docs/status.md).

<a name="pattern-index"></a>

**Pattern index · jump to the examples**

| Decision pattern | Decision pattern |
| :--- | :--- |
| [Tool selection](#tool-selection) · **230** | [Intent routing](#intent-routing) · **35** |
| [Context compaction](#context-compaction) · **34** | [Safety gating](#safety-gating) · **139** |
| [Output validation](#output-validation) · **134** | [Retry control](#retry-control) · **7** |
| [Human escalation](#human-escalation) · **68** | [Model routing](#model-routing) · **44** |
| [Speculative fan-out](#speculative-fan-out) · **32** | [Search & ranking](#search--ranking) · **64** |
| [Structured extraction](#structured-extraction) · **16** | [Classification](#classification) · **119** |
| [ML feature extraction](#ml-feature-extraction) · **8** | [Document triage](#document-triage) · **20** |
| [Support triage](#support-triage) · **8** | [Content scoring](#content-scoring) · **164** |
| [Recommendation](#recommendation) · **1** | [Overview](#overview) · **451** |

## Measured, not claimed

Independent measurement reports in the catalogue, including **negative results** that help explain where an approach fails. These are the original authors' measurements; this repository has not independently reproduced them. Check each report's dataset, method and model version before comparing results.

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br>
  Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it.<br>
  <sub>`Benchmark` · ★248,479 · `Py` · `noul`</sub>

  > The single most credible row in this catalog. Recall came out below their existing summariser, and at a matched context budget it tied plain recency ordering. Cost was genuinely far lower. Publishing a negative result on a hyped model is rare.

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.<br>
  <sub>`Benchmark` · ★87,298 · `TS` · `choice`</sub>

  **Caveats:** `shadow mode`

  > Wired in but deliberately inert: by their own statement nothing Jev returns reaches a label, a cache row or an alert. Ships a golden fixture. A model to copy for how to trial a new model without betting production on it.

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)**<br>
  One Score per candidate file to pre-brief code review — measured twice, then removed: more billed input for essentially no wall-clock gain, and offline replay showed the candidate list could not reach where review findings land.<br>
  <sub>`Benchmark` · ★8,617 · `Go` · `score`</sub>

  > Removed in PR #1165 (2026-09-22). Their offline measurement found the candidate generator excluded changed files by construction while nearly all review findings sit in changed files, and that per-file excerpts made the list less precise at higher token cost. The code is gone from the default branch, so this row cites the change that removed it.

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)**<br>
  Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.<br>
  <sub>`Benchmark` · ★756 · kitfunso · `TS`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br>
  Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.<br>
  <sub>`Benchmark` · ★190 · `Py`</sub>

  **Caveats:** `no licence` · `unverified claims`

  > The most actionable engineering caveat found anywhere: if option order alone can move a probability past your threshold, your threshold is not as stable as it looks. Independent and unreplicated, so treat the magnitude as indicative.

- **[jevbench](https://github.com/fstandhartinger/jevbench)**<br>
  JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open.<br>
  <sub>`Benchmark` · ★107 · fstandhartinger · `Py`</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)**<br>
  An introduction to Jev with hands-on tests: Choice, Score and Noul turn natural language into typed judgements for classification, scoring and routing, compared with DeepSeek on comment labelling, speed and results, with CSV import, replay and offline reports.<br>
  <sub>`Benchmark` · ★97 · nanmicoder · `JS`</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)**<br>
  A WebMCP benchmark, measures WebMCP against other browser-agent interfaces.<br>
  <sub>`Benchmark` · ★80 · nekuda-ai · `TS`</sub>

- **[jev-robot-control](https://github.com/openroboto-ai/jev-robot-control)**<br>
  Jev against two LLMs on direct Cartesian control of an xArm7 in MuJoCo — intent, movement and gripper each step — with recorded responses, trajectories and replays. One seed-0 trial per controller, not a success rate.<br>
  <sub>`Benchmark` · ★44 · openroboto-ai · `Py`</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)**<br>
  A gateway that mimics the structured-output shape, used to benchmark against it.<br>
  <sub>`Benchmark` · ★38 · iammrduncan · `TS`</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)**<br>
  Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。<br>
  <sub>`Benchmark` · ★26 · zaious · `Py`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)**<br>
  Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.<br>
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)**<br>
  Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.<br>
  <sub>`Benchmark` · ★17 · abdelstark · `Py`</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)**<br>
  Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG<br>
  <sub>`Benchmark` · ★14 · erendikmenn · `Py`</sub>

- **[pdf-race](https://github.com/goodrahstar/pdf-race)**<br>
  Docling → Jev vs Docling → Gemini 3.8 Flash vs Gemini reading the PDF: same documents, one clock, scored against arXiv's own metadata<br>
  <sub>`Benchmark` · ★9 · goodrahstar · `JS`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)**<br>
  Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows<br>
  <sub>`Benchmark` · ★7 · jmanhype · `Py`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)**<br>
  An independent head-to-head against dedicated rerankers across fourteen datasets.<br>
  <sub>`Benchmark` · ★7 · anessbelbati · `Py`</sub>

  > An independent measurement rather than a vendor figure, and a direct comparison against purpose-built rerankers — the comparison that matters for the search-ranking pattern.

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)**<br>
  Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs<br>
  <sub>`Benchmark` · ★6 · wondertwins · `Py`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)**<br>
  Reproducible early-access evaluation of Jev on Korean understanding and medical text, with runtime and cost evidence<br>
  <sub>`Benchmark` · ★6 · mahlernim · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)**<br>
  Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~<br>
  <sub>`Benchmark` · ★6 · scienthoon · `Py`</sub>

- **[jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval)**<br>
  Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured.<br>
  <sub>`Benchmark` · ★6 · zhuyansen · `Py`</sub>

- **[jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark)**<br>
  Comparing Jev, Gemini Flash, and Claude Fable on Python code review rules: cost, speed, accuracy, and consistency. Includes results, charts, and reproducible experiments.<br>
  <sub>`Benchmark` · ★5 · gemanor · `Py`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)**<br>
  A show-and-tell capability study for Jev, TypeSafe's System One decision model.<br>
  <sub>`Benchmark` · ★5 · lbotinelly · `TS`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)**<br>
  Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.<br>
  <sub>`Benchmark` · ★5 · anisselbd · `Py`</sub>

  **Caveats:** `no licence`

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)**<br>
  LegalForecast-MTD benchmark alpha and official evaluation workflows<br>
  <sub>`Benchmark` · ★5 · johnhughes3 · `Py`</sub>

- **[jevarena](https://github.com/chenmingtang830/jevarena)**<br>
  Open-source BYOK arena for Jev and other AI judges. Find failures, compare quality, cost, and latency.<br>
  <sub>`Benchmark` · ★4 · chenmingtang830 · `TS`</sub>

- **[sysone-bench](https://github.com/instax-dutta/sysone-bench)**<br>
  First independent head-to-head benchmark of System One decision models (Laya vs Jev) on byte-identical inputs<br>
  <sub>`Benchmark` · ★4 · instax-dutta · `Py`</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)**<br>
  Jev drives your Ego Lite browser: one typed-choice request per step. Single-file, zero-dependency port of browser-use/jev-ultrafast with multi-model benchmarks and extra guardrails. Unofficial.<br>
  <sub>`Benchmark` · ★3 · shikaizhong-design · `JS`</sub>

- **[jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)**<br>
  Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.<br>
  <sub>`Benchmark` · ★3 · kantahayashiai · `JS`</sub>

- **[jev-exploration](https://github.com/SamuelSacco/jev-exploration)**<br>
  Jev (TypeSafe) exploratory thread: claim audit, live demos, and runnable code<br>
  <sub>`Benchmark` · ★3 · samuelsacco · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-plays](https://github.com/mansicer/jev-plays)**<br>
  A System One model plays Craftax while an LLM sets the goals: five agents on the same map, from Jev on raw actions to an LLM controlling every step, compared in logged episodes.<br>
  <sub>`Benchmark` · ★3 · mansicer · `Py`</sub>

- **[origin-civilization](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)**<br>
  AI life-and-civilization simulation: TypeSafe Jev makes every decision (typed, probabilistic, auditable); LLMs plan — OpenAI-compatible APIs, local models (Ollama, LM Studio), Claude Code, Codex.<br>
  <sub>`Benchmark` · ★3 · jacquesgariepy · `TS`</sub>

- **[typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review)**<br>
  About calibrating Jev for code reviews<br>
  <sub>`Benchmark` · ★3 · selmar · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)**<br>
  Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset).<br>
  <sub>`Benchmark` · ★2 · tokentrim · `Py`</sub>

- **[jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong)**<br>
  Jev plays browser table tennis in real time: structured telemetry, typed decisions, ordinary Chrome inputs, and auditable evidence.<br>
  <sub>`Benchmark` · ★2 · icohen007 · `JS`</sub>

- **[jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment)**<br>
  Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena<br>
  <sub>`Benchmark` · ★2 · tokentrim · `Py`</sub>

- **[zerosweep](https://github.com/sysadarsh/zerosweep)**<br>
  Autonomous System-One Triage Engine & Benchmark powered by TypeSafe AI (Jev). 75ms inference, $0 output tokens, and RLCD epistemic safety gates.<br>
  <sub>`Benchmark` · ★2 · sysadarsh · `TS`</sub>

  **Caveats:** `no licence`

- **[antigravity-mcp-semantic-search-with-typesafeai](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)**<br>
  Fast semantic code search & diff sanity auditor for AI coding assistants (Antigravity, Cursor, Claude Code) powered by TypeSafe System One.<br>
  <sub>`Benchmark` · ★1 · greenyamao · `Py`</sub>

  **Caveats:** `no licence`

- **[can-jev-bayes](https://github.com/TomRichner/can-jev-bayes)**<br>
  Jev Bayes, No? Testing TypeSafe AI's Jev against Bayesian-optimal strategies, and testing if Jev can effectivly use Bayesian priors.<br>
  <sub>`Benchmark` · ★1 · tomrichner · `Py`</sub>

- **[decision-bench](https://github.com/Hanno-Labs/decision-bench)**<br>
  Open benchmark runtime for document-grounded decision models<br>
  <sub>`Benchmark` · ★1 · hanno-labs · `Py`</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)**<br>
  Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design.<br>
  <sub>`Benchmark` · ★1 · xienda · `JS`</sub>

- **[jev-bench](https://github.com/TheWayWithin/jev-bench)**<br>
  Does the cited source actually say it? A 42-claim benchmark: Jev (TypeSafe System One) against GPT-5.4, Claude Sonnet 5 and Gemini 3.1 Pro.<br>
  <sub>`Benchmark` · ★1 · thewaywithin · `Py`</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)**<br>
  Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.<br>
  <sub>`Benchmark` · ★1 · themsquared · `Py`</sub>

- **[jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks)**<br>
  JEV decision benchmark results on MetaTool, When2Call, and BFCL V4, with bilingual tables and reproducible reports.<br>
  <sub>`Benchmark` · ★1 · baibizhe · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-eval](https://github.com/4esv/jev-eval)**<br>
  Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost<br>
  <sub>`Benchmark` · ★1 · 4esv · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-lab](https://github.com/llt22/jev-lab)**<br>
  Hands-on research lab for TypeSafe's Jev (System One model): reproducible benchmarks of Noul/Choice/Score primitives, confidence gating, fan-out latency, agent control — plus a living audit of the Jev ecosystem.<br>
  <sub>`Benchmark` · ★1 · llt22 · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-lab](https://github.com/danielhirt/jev-lab)**<br>
  Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison<br>
  <sub>`Benchmark` · ★1 · danielhirt · `TS`</sub>

  **Caveats:** `no licence`

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)**<br>
  Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets<br>
  <sub>`Benchmark` · ★1 · teyhouse · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-sim](https://github.com/dashbi1/jev-sim)**<br>
  Jev-compatible /v1/systemone server reading typed decisions from LLM logits, benchmarked against TypeSafe's Jev on the same items via JevBench<br>
  <sub>`Benchmark` · ★1 · dashbi1 · `Py`</sub>

- **[jevsbistro](https://github.com/andrewsilber/JevsBistro)**<br>
  3D restaurant service simulator for benchmarking low-latency decision models<br>
  <sub>`Benchmark` · ★1 · andrewsilber · `TS`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)**<br>
  Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev.<br>
  <sub>`Benchmark` · ★1 · zsavage8 · `Py`</sub>

- **[what-is-jev](https://github.com/g0runmezadam/what-is-jev)**<br>
  Independent, source-linked research on TypeSafe AI's Jev (System One), with 947 rubric-scored public repositories, recurring patterns, datasets, and bilingual documentation.<br>
  <sub>`Benchmark` · ★1 · g0runmezadam · `Py`</sub>

  > Research about the ecosystem rather than a caller of the API, so it carries no call-site evidence.

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)**<br>
  An experimental protocol for evidence-aware agent handoffs, bounded worker continuation, and TypeSafe/Jev-assisted review, with reproducible evaluation.<br>
  <sub>`Benchmark` · ★0 · zsoxi · `Py`</sub>

- **[jev-acento](https://github.com/marcosmartinez/jev-acento)**<br>
  ¿Jev entiende tu acento? Pre-registered audit of TypeSafe AI's Jev on Spanish — accuracy, calibration and token cost — plus a CLI to run the same comparison on your own labelled data.<br>
  <sub>`Benchmark` · ★0 · marcosmartinez · `Py`</sub>

  > An independent, pre-registered audit of the model outside English — the gap docs/status.md lists as worth watching.

- **[jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit)**<br>
  Independent API-only calibration audit of TypeSafe AI's Jev decision model<br>
  <sub>`Benchmark` · ★0 · jujumilk3 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)**<br>
  Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break<br>
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)**<br>
  Does TypeSafe's Jev keep its accuracy and calibration on Russian? Independent RU vs EN audit (ECE, reliability diagrams, paired bootstrap) on parallel human-labelled data.<br>
  <sub>`Benchmark` · ★0 · ahtoooxa · `Py`</sub>

  > An independent calibration audit outside English — the gap docs/status.md lists as worth watching.

- **[jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric)**<br>
  Architecture for running many semantic decisions through one validated path, with a labelled 111-case benchmark comparing TypeSafe Jev against a Claude baseline, and a dashboard for inspecting any single decision. Experimental, not production.<br>
  <sub>`Benchmark` · ★0 · ghubnab99 · `C#`</sub>

- **[jev-eval](https://github.com/onlyoneaman/jev-eval)**<br>
  TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts<br>
  <sub>`Benchmark` · ★0 · onlyoneaman · `TS`</sub>

- **[jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval)**<br>
  A third-party check of Jev against two LLMs under identical conditions: routing booking inquiries to a photo-shoot service for tourists in Japan, sixty synthetic messages in four languages.<br>
  <sub>`Benchmark` · ★0 · shogo-nfrealmusic · `TS`</sub>

  **Caveats:** `no licence`

- **[jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench)**<br>
  Measured: asking TypeSafe Jev N questions in one call bills the state once. 2,976 real requests, raw data, exact billing check.<br>
  <sub>`Benchmark` · ★0 · blowxian · `Py`</sub>

- **[jev-lab](https://github.com/Menny1337/jev-lab)**<br>
  TypeScript experiments, evaluations, and latency benchmarks for TypeSafe's Jev model<br>
  <sub>`Benchmark` · ★0 · menny1337 · `TS`</sub>

  **Caveats:** `no licence`

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)**<br>
  Benchmark-driven Jev router and judge for cost-aware, reliable LLM coding workflows<br>
  <sub>`Benchmark` · ★0 · erendikmenn · `Py`</sub>

- **[jev-no-enem](https://github.com/patryckalves/jev-no-enem)**<br>
  Reproducible benchmark evaluating TypeSafe AI's Jev (System One paradigm) on Brazil's ENEM 2025 standardized exam. Evaluates typed decision-making, domain-specific accuracy, and RLCD uncertainty calibration against open LLM baselines with an interactive GitHub Pages dashboard.<br>
  <sub>`Benchmark` · ★0 · patryckalves · `Py`</sub>

  **Caveats:** `no licence`

  > An independent evaluation outside English, on a public exam with known answers.

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)**<br>
  Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.<br>
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jev-playground](https://github.com/hegargarcia/jev-playground)**<br>
  Benchmarks Jev against other evaluation models in games with explicit states and legal actions: code owns the rules and transitions, each model picks the next action, and outcomes are measured.<br>
  <sub>`Benchmark` · ★0 · hegargarcia · `TS`</sub>

  **Caveats:** `no licence`

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)**<br>
  Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next<br>
  <sub>`Benchmark` · ★0 · sypherin · `Py`</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)**<br>
  Synthetic smoking-history extraction benchmark comparing TypeSafe Jev and OpenAI structured outputs, with reproducible accuracy, cost, and latency results.<br>
  <sub>`Benchmark` · ★0 · vclic · `Py`</sub>

  **Caveats:** `no licence`

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br>
  The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.<br>
  <sub>`Benchmark` · Lindfors</sub>

  > Methodology is stated cleanly and scoped honestly as a single-day snapshot. Leading with a failure case is what makes it a real calibration test rather than a testimonial.

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br>
  The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.<br>
  <sub>`Benchmark` · Near Here</sub>

  > Self-limits correctly: a use-case study, not a model leaderboard. That restraint is rarer than the numbers.

## By decision pattern

The primary index. Each heading is a decision an agent has to make; the rows are examples of making it. Caveats appear as short tags — the full note for each row is in [`catalog.json`](catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/).

### Tool selection

_Which tool or action the agent should call next._

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐<br>
  Maps natural-language trading requests onto ordinary typed functions by turning function names and closed-set arguments into confidence-aware questions.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐<br>
  Picks at most one skill out of 182 for an agent turn: one request ranks every skill and asks whether the turn needs one at all, a second reads the top three.<br>
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br>
  Runnable demo code for a smart home assistant that evaluates user requests with typed decisions.<br>
  <sub>`Official docs` · `Py`</sub>

- **[ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)**<br>
  An AI Hedge Fund Team<br>
  <sub>`Integration` · ★63,705 · virattt · `Py`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br>
  Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.<br>
  <sub>`Plugin` · ★31,582 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br>
  Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.<br>
  <sub>`Project` · ★30,300 · `Py` · `choice`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br>
  Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.<br>
  <sub>`Project` · ★27,886 · `Py` · `choice` · `noul`</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)**<br>
  Computer-use action selection in Python and TypeScript: Jev picks the next browser action from an immutable candidate set, with reobserve and abstain as reserved options.<br>
  <sub>`Project` · ★26,164 · `Py` · `TS` · `choice`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br>
  A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed.<br>
  <sub>`Project` · ★19,261 · Browser Use · `Py` · `choice`</sub>

  **Caveats:** `vendor numbers`

- **[json-render](https://github.com/vercel-labs/json-render)**<br>
  Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.<br>
  <sub>`Project` · ★18,204 · Vercel Labs · `TS` · `choice`</sub>

**10 of 230** shown · [all 230 on one page →](docs/by-pattern/tool-selection.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Intent routing

_Classify what the user wants and send the request down the right branch._

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br>
  Runnable demo code for a smart home assistant that evaluates user requests with typed decisions.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br>
  Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br>
  Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.<br>
  <sub>`Project` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br>
  Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human.<br>
  <sub>`Integration` · ★46,958 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br>
  Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.<br>
  <sub>`Project` · ★12,328 · `TS` · `choice` · `noul`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br>
  An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.<br>
  <sub>`Project` · ★5,414 · `Java` · `choice` · `score` · `noul`</sub>

- **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)**<br>
  A teaching example with a deliberate control group: the same station-enquiry task written in plain Python that only accepts Y/N, next to a Noul that reads intent.<br>
  <sub>`Tutorial` · ★5,205 · Real Python · `Py` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.<br>
  <sub>`Tutorial` · ★4,578 · `Py` · `choice` · `score` · `noul`</sub>

- **[foreman](https://github.com/thruwire/foreman)**<br>
  A software-factory foreman that uses Jev to decide what an agent pipeline should do next.<br>
  <sub>`Project` · ★538 · thruwire · `Py`</sub>

**10 of 35** shown · [all 35 on one page →](docs/by-pattern/intent-routing.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=intent-routing&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Context compaction

_Decide which tool calls and results still matter so stale context can be dropped._

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br>
  Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it.<br>
  <sub>`Benchmark` · ★248,479 · `Py` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br>
  Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.<br>
  <sub>`Project` · ★20,069 · `Rs` · `noul`</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**<br>
  A Claude Code plugin that replaces the compaction summary with per-item decisions: stale tool calls are dropped or truncated, everything kept stays verbatim.<br>
  <sub>`Plugin` · ★6,616 · tamaratran · `TS` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.<br>
  <sub>`Plugin` · ★718 · `Py` · `choice` · `score` · `noul`</sub>

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)**<br>
  "Work appears completed or recorded. Run /compact to save tokens."<br>
  <sub>`Project` · ★183 · kunchenguid · `TS`</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)**<br>
  Trims long shell output before the model sees it, asking one Noul per chunk.<br>
  <sub>`Plugin` · ★144 · tamaratran · `TS` · `noul`</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)**<br>
  Context garbage collection for Claude Code: when Read, Bash or Grep dump a wall of output, each chunk is judged for relevance to the current task.<br>
  <sub>`Plugin` · ★79 · `Py` · `noul`</sub>

- **[save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean)**<br>
  Portable, Jev-guided context compaction for coding agents: instead of an LLM rewriting old context into a lossy summary, Jev decides which tool calls and results still matter, and user and assistant text is kept verbatim.<br>
  <sub>`Plugin` · ★69 · iamunbounded · `TS`</sub>

- **[yoshi](https://github.com/compozy/yoshi)**<br>
  Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy<br>
  <sub>`Plugin` · ★25 · compozy · `TS`</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)**<br>
  Claude Code plugin: Jev for rule checks, verbatim compaction, and prompt routing<br>
  <sub>`Plugin` · ★12 · 0x7067 · `Py`</sub>

**10 of 34** shown · [all 34 on one page →](docs/by-pattern/context-compaction.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Safety gating

_Decide whether an action is safe to run. Defence in depth, never a security boundary._

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br>
  Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br>
  Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.<br>
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br>
  Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction.<br>
  <sub>`Project` · ★42,557 · `Go` · `noul`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br>
  Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.<br>
  <sub>`Plugin` · ★31,582 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br>
  The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.<br>
  <sub>`Integration` · ★18,223 · `TS` · `choice` · `score` · `noul`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)**<br>
  Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check.<br>
  <sub>`Project` · ★6,341 · `TS` · `choice` · `noul`</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)**<br>
  Three Score questions on a shared severity scale, blocking the request when two or more cross the line, and failing closed.<br>
  <sub>`Project` · ★5,017 · `Rs` · `score`</sub>

- **[atomic](https://github.com/bastani-inc/atomic)**<br>
  The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, checks, and approval gates instead of hoping it follows your instructions.<br>
  <sub>`Project` · ★820 · bastani-inc · `TS`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br>
  A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation.<br>
  <sub>`Project` · ★591 · `JS` · `choice` · `noul`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)**<br>
  VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.<br>
  <sub>`Project` · ★425 · notque · `Py`</sub>

**10 of 139** shown · [all 139 on one page →](docs/by-pattern/safety-gating.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Output validation

_Check a model's output against a rubric before it reaches a user._

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br>
  Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br>
  Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.<br>
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[latitude-llm](https://github.com/latitude-dev/latitude-llm)**<br>
  Open-source observability for AI agents. Find where your agents fail, dispatch your coding agent to fix it, and verify the fix against real traces.<br>
  <sub>`Project` · ★4,672 · latitude-dev · `TS`</sub>

- **[reticle](https://github.com/reticlehq/reticle)**<br>
  AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications.<br>
  <sub>`Project` · ★830 · reticlehq · `TS`</sub>

- **[atomic](https://github.com/bastani-inc/atomic)**<br>
  The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, checks, and approval gates instead of hoping it follows your instructions.<br>
  <sub>`Project` · ★820 · bastani-inc · `TS`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)**<br>
  VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.<br>
  <sub>`Project` · ★425 · notque · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br>
  A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.<br>
  <sub>`Plugin` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[JevRev](https://github.com/Alex314618-create/JevRev)**<br>
  The decision layer beside an LLM: Jev filters plans, checks progress and keeps attention on work worth continuing, while the LLM supplies breadth and implementation.<br>
  <sub>`Project` · ★303 · alex314618-create · `TS`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)**<br>
  A local-first MCP plugin for continuous code-quality review by coding agents.<br>
  <sub>`Plugin` · ★217 · niazmorshed2007 · `TS`</sub>

- **[abide](https://github.com/coldteadotai/abide)**<br>
  Make your coding agent abide by all your project rules<br>
  <sub>`Plugin` · ★211 · coldteadotai · `TS`</sub>

**10 of 134** shown · [all 134 on one page →](docs/by-pattern/output-validation.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Retry control

_Decide whether a failed step is worth retrying._

- **[jevswiftsdk](https://github.com/NSStudent/JevSwiftSDK)**<br>
  An independent, type-safe Swift SDK for TypeSafe Jev, with async/await, batching, retries, and SPM support.<br>
  <sub>`SDK` · ★8 · nsstudent · `Swift`</sub>

- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)**<br>
  Zero-dependency System One decision harness: 5 semantic gates saving frontier AI agent tokens on trivial errors & doom loops. Python + TypeScript + Rust. MCP-compatible.<br>
  <sub>`Plugin` · ★6 · ismaelsoilet · `Py`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)**<br>
  Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev.<br>
  <sub>`Plugin` · ★2 · vicente-md · `Java`</sub>

  **Caveats:** `no licence`

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)**<br>
  Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.<br>
  <sub>`Project` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul`</sub>

  **Caveats:** `one commit` · `AI-written`

- **[jev-reasoning-navigator](https://github.com/AndreuVM/jev-reasoning-navigator)**<br>
  JEV Reasoning Navigator: Cognitive supervision, loop prevention, and anti-hallucination engine for autonomous LLM agents using TypeSafe AI<br>
  <sub>`Project` · ★1 · andreuvm · `Py`</sub>

  **Caveats:** `no licence`

- **[XavierJev](https://github.com/liu-x27/XavierJev)**<br>
  A local decision layer in Jev's shape: yes/no, choice and rubric questions read off one token's logprobs from a local model, with a Claude Code permission gate measured on held-out command sets.<br>
  <sub>`Jev-like alternative` · ★1 · Xinyu Liu · `TS` · `noul` · `choice` · `score`</sub>

  **Caveats:** `not Jev itself` · `AI-written`

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)**<br>
  Judge agent steps — ok / retry / escalate / stop via TypeSafe Jev<br>
  <sub>`Project` · ★0 · ndolinschi · `TS`</sub>

  **Caveats:** `no licence`

All 7 shown · [on its own page](docs/by-pattern/retry-control.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=retry-control&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Human escalation

_Use calibrated confidence to decide what a person must see._

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br>
  Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br>
  Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br>
  Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions.<br>
  <sub>`Official docs` · `Py` · `score`</sub>

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br>
  Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐<br>
  Routes uncertain probabilities to human review while keeping the underlying noul values visible rather than collapsing them to a label.<br>
  <sub>`Official docs` · `Py` · `noul`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br>
  Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Confidence](https://docs.typesafe.ai/confidence)** ⭐<br>
  How confidence is derived from the probability distribution, and why a threshold tuned on one question type does not transfer to another.<br>
  <sub>`Official docs`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br>
  Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human.<br>
  <sub>`Integration` · ★46,958 · `Py` · `choice`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br>
  Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.<br>
  <sub>`Project` · ★30,300 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br>
  Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.<br>
  <sub>`Project` · ★12,328 · `TS` · `choice` · `noul`</sub>

**10 of 68** shown · [all 68 on one page →](docs/by-pattern/human-escalation.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Model routing

_Pick which downstream model or tier should handle a request._

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br>
  A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br>
  Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br>
  Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.<br>
  <sub>`Plugin` · ★31,582 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br>
  The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.<br>
  <sub>`Integration` · ★18,223 · `TS` · `choice` · `score` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.<br>
  <sub>`Plugin` · ★718 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)**<br>
  Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.<br>
  <sub>`Project` · ★582 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)**<br>
  Judges how hard a coding turn is, then picks the model tier, reasoning depth and speed mode to match.<br>
  <sub>`Plugin` · ★260 · `JS` · `choice` · `score`</sub>

- **[Astra-Ares](https://github.com/miuuyy/Astra-Ares)**<br>
  Adaptive reasoning effort for GPT-6 during Codex tasks, powered by Jev to reduce token usage.<br>
  <sub>`Plugin` · ★250 · miuuyy · `JS`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)**<br>
  A router for models, tools and subagents.<br>
  <sub>`Project` · ★189 · billionsbobby · `TS`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)**<br>
  An agent that routes evaluation work through typed decisions.<br>
  <sub>`Project` · ★105 · vinilana · `TS`</sub>

  **Caveats:** `no licence`

**10 of 44** shown · [all 44 on one page →](docs/by-pattern/model-routing.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Speculative fan-out

_Pack many questions — including speculative ones — into one request and let code pick what mattered._

- **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐<br>
  A 13-question regulatory briefing over one long article, showing that batching every question into one call is far cheaper and faster with no change in answers.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐<br>
  Pack many questions, including ones you may not need, into a single request and let your code decide afterwards what was relevant.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br>
  The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.<br>
  <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.<br>
  <sub>`Project` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br>
  Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction.<br>
  <sub>`Project` · ★42,557 · `Go` · `noul`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br>
  A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed.<br>
  <sub>`Project` · ★19,261 · Browser Use · `Py` · `choice`</sub>

  **Caveats:** `vendor numbers`

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.<br>
  <sub>`Tutorial` · ★4,578 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br>
  A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.<br>
  <sub>`Project` · ★94 · `TS` · `choice` · `noul`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)**<br>
  Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.<br>
  <sub>`Plugin` · ★46 · kbhuw · `JS`</sub>

  **Caveats:** `no licence`

- **[pi-typesafe](https://github.com/DevMortimer/pi-typesafe)**<br>
  TypeSafe decisions for Pi: batched evaluation tool, terminal playground, and typed API for extension authors<br>
  <sub>`Plugin` · ★45 · devmortimer · `TS`</sub>

**10 of 32** shown · [all 32 on one page →](docs/by-pattern/fan-out.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Search & ranking

_Score or re-rank candidates from a cheaper retrieval step._

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br>
  Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐<br>
  Semantic search over a terms-of-service document: one request scores 218 line ids with a Choice, and a Noul checks whether the document answers at all.<br>
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐<br>
  Re-ranks 30-passage BM25 shortlists for 40 legal queries with one question per query-candidate pair, reporting large top-1 and top-10 gains.<br>
  <sub>`Official docs` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.<br>
  <sub>`Project` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)**<br>
  One Noul per candidate document in a single batched request, with the yes-probability used directly as the relevance score.<br>
  <sub>`Project` · ★38,571 · `Py` · `noul`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br>
  Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.<br>
  <sub>`Project` · ★27,886 · `Py` · `choice` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br>
  Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.<br>
  <sub>`Project` · ★20,069 · `Rs` · `noul`</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)**<br>
  A vector-database reranker that asks one Noul per result and uses the yes-probability as an absolute relevance score, comparable across queries.<br>
  <sub>`Project` · ★11,513 · `Py` · `noul`</sub>

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)**<br>
  One Score per candidate file to pre-brief code review — measured twice, then removed: more billed input for essentially no wall-clock gain, and offline replay showed the candidate list could not reach where review findings land.<br>
  <sub>`Benchmark` · ★8,617 · `Go` · `score`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br>
  An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.<br>
  <sub>`Project` · ★5,414 · `Java` · `choice` · `score` · `noul`</sub>

**10 of 64** shown · [all 64 on one page →](docs/by-pattern/search-ranking.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Structured extraction

_Pull typed fields out of messy text by choosing among candidates rather than generating them._

- **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐<br>
  Extracts absolute and relative dates by asking for the parts a document names, then resolving and validating them in code with confidence-based review.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐<br>
  Regexes find candidate emails, phone numbers and amounts; the model selects the requested span so code can normalise a verbatim value.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br>
  Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block.<br>
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br>
  A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost.<br>
  <sub>`Official docs` · `Py`</sub>

- **[smart-paste](https://github.com/nomanjack/smart-paste)**<br>
  Fills form fields from pasted text: the form's heading, labels and your text go to TypeSafe, and it inserts the values it matches for you to review before submitting.<br>
  <sub>`Plugin` · ★38 · nomanjack · `JS`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)**<br>
  Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay i<br>
  <sub>`Project` · ★33 · choxos · `JS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)**<br>
  Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.<br>
  <sub>`Project` · ★21 · jcpsimmons · `JS`</sub>

- **[jevfill](https://github.com/imohitmayank/jevfill)**<br>
  A Chrome extension that fills web forms from unstructured notes with Jev: paste your details once as plain text, with no structured profile, then fill forms on demand.<br>
  <sub>`Plugin` · ★18 · imohitmayank · `TS`</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)**<br>
  Text extraction with Jev: field extraction, PII detection and exact quotes, built on TypeSafe's Jev.<br>
  <sub>`Project` · ★4 · jkrup · `JS`</sub>

- **[jev-mcp-dispatcher](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher)**<br>
  Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence.<br>
  <sub>`Plugin` · ★3 · abhishekashokvkumar · `Py`</sub>

  **Caveats:** `no licence`

**10 of 16** shown · [all 16 on one page →](docs/by-pattern/data-extraction.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Classification

_Put an item into a taxonomy, including deep hierarchies walked with probabilities._

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br>
  Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐<br>
  Walks deep patent, retail, biomedical and source-code taxonomies with a parallel beam search over Choice probabilities.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br>
  Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions.<br>
  <sub>`Official docs` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br>
  Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block.<br>
  <sub>`Official docs` · `Py`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.<br>
  <sub>`Benchmark` · ★87,298 · `TS` · `choice`</sub>

  **Caveats:** `shadow mode`

- **[json-render](https://github.com/vercel-labs/json-render)**<br>
  Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.<br>
  <sub>`Project` · ★18,204 · Vercel Labs · `TS` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br>
  Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.<br>
  <sub>`Project` · ★12,328 · `TS` · `choice` · `noul`</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)**<br>
  Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.<br>
  <sub>`Project` · ★419 · kyotofin · `TS`</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)**<br>
  Zero-shot text classification over plain HTTP — no API key, no account. One Cloudflare Worker, a CLI, and an MCP server. https://classifier.dev<br>
  <sub>`Plugin` · ★417 · mrmps · `TS`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)**<br>
  A very fast document classifier/splitter using Jev<br>
  <sub>`Project` · ★414 · jerryjliu · `Py`</sub>

**10 of 119** shown · [all 119 on one page →](docs/by-pattern/classification.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### ML feature extraction

_Turn free text into numeric features for a classical downstream model._

- **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐<br>
  An autoresearch loop that proposes questions, turns free text into numeric features, and uses model error to improve a supervised gradient-boosting regressor.<br>
  <sub>`Official docs` · `Py`</sub>

- **[nimble](https://github.com/bespokelabsai/nimble)**<br>
  Local typed decisions, contrastive data curation, and model evaluation.<br>
  <sub>`Project` · ★1,699 · bespokelabsai · `Py`</sub>

  **Caveats:** `no licence`

- **[jev-align](https://github.com/sutro-sh/jev-align)**<br>
  Builds calibrated decision functions from human feedback.<br>
  <sub>`Project` · ★284 · sutro-sh · `Py`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)**<br>
  Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy.<br>
  <sub>`Project` · ★97 · `TS` · `choice` · `score`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)**<br>
  Curates training data: JSONL and Parquet rows are judged on quality, relevance and risk before deciding what reaches downstream training.<br>
  <sub>`Project` · ★45 · `Rs` · `score` · `noul`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)**<br>
  Shift every LLM call to the cheapest model that can handle it. Routing decided by TypeSafe Jev in ~180 ms. No training data. Policy in plain YAML. TypeScript and Python.<br>
  <sub>`Project` · ★3 · iamvatsalpatel · `TS`</sub>

- **[jev-board-lab](https://github.com/WebGrga/jev-board-lab)**<br>
  Interactive explorer and Jev question workspace for Jev Board datasets.<br>
  <sub>`Project` · ★0 · webgrga · `JS`</sub>

  **Caveats:** `no licence`

- **[jev-calibrated-narrative-coding](https://github.com/pozapas/jev-calibrated-narrative-coding)**<br>
  Calibrated conversion of police crash narratives into probabilistic crash variables with a System One model. Pipeline, schema and aggregated results.<br>
  <sub>`Project` · ★0 · pozapas · `Py`</sub>

All 8 shown · [on its own page](docs/by-pattern/feature-extraction.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=feature-extraction&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Document triage

_Classify and route incoming documents, invoices and forms._

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)**<br>
  Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.<br>
  <sub>`Project` · ★419 · kyotofin · `TS`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)**<br>
  A very fast document classifier/splitter using Jev<br>
  <sub>`Project` · ★414 · jerryjliu · `Py`</sub>

- **[formanator](https://github.com/timrogers/formanator)**<br>
  Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) clients, with support for AI-powered receipt analysis with an LLM or Jev<br>
  <sub>`Plugin` · ★99 · timrogers · `Rs`</sub>

- **[doc-router](https://github.com/misbahsy/doc-router)**<br>
  A Document OCR Router to help route pages based on content.<br>
  <sub>`Project` · ★26 · misbahsy · `Rs`</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)**<br>
  Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。<br>
  <sub>`Benchmark` · ★26 · zaious · `Py`</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)**<br>
  Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Local-first, SQLite receipts, zero dependencies.<br>
  <sub>`Project` · ★9 · romiluz13 · `Py`</sub>

- **[pdf-race](https://github.com/goodrahstar/pdf-race)**<br>
  Docling → Jev vs Docling → Gemini 3.8 Flash vs Gemini reading the PDF: same documents, one clock, scored against arXiv's own metadata<br>
  <sub>`Benchmark` · ★9 · goodrahstar · `JS`</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)**<br>
  JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.<br>
  <sub>`Project` · ★4 · charlyhno-eng · `TS`</sub>

- **[jev-builder](https://github.com/collapseindex/jev-builder)**<br>
  A browser form for building requests to TypeSafe's Jev: pick a template, fill in the blanks, copy the request. No JSON, no install, runs locally.<br>
  <sub>`Project` · ★3 · collapseindex · `JS`</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)**<br>
  Agent skill that spots bounded-judgment steps, tries a typed decision model (TypeSafe's Jev) first, and documents every attempt<br>
  <sub>`Plugin` · ★2 · harrymunro · `Py`</sub>

**10 of 20** shown · [all 20 on one page →](docs/by-pattern/document-triage.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=document-triage&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Support triage

_Route support tickets and conversations by intent and urgency._

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br>
  The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.<br>
  <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.<br>
  <sub>`Tutorial` · ★4,578 · `Py` · `choice` · `score` · `noul`</sub>

- **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)**<br>
  A community Spring AI starter bringing typed decisions to Java, with a builder API over the three question types.<br>
  <sub>`Integration` · ★36 · `Java` · `choice` · `score` · `noul`</sub>

- **[jev-triage](https://github.com/boldbug1/jev-triage)**<br>
  Message triage CLI in Go, built on the Jev decision model from TypeSafe AI. Categorizes messages, scores urgency, and flags low-confidence ones for human review.<br>
  <sub>`Project` · ★3 · boldbug1 · `Go`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**<br>
  A minimal first call asking a choice, a score and a noul together, annotated with the asymmetries that catch people out.<br>
  <sub>`Snippet` · `Py` · `choice` · `score` · `noul`</sub>

  **Caveats:** `code untested`

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br>
  Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.<br>
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice`</sub>

  **Caveats:** `paywall`

- **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)**<br>
  Another gateway route, notable because its endpoint path and request envelope differ again from both the native API and Cloudflare's.<br>
  <sub>`Integration` · `Py` · `noul` · `choice` · `score`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)**<br>
  Workers AI binding and REST samples asking a noul, a choice and a score in one call, with the full response including per-answer confidence.<br>
  <sub>`Integration` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

All 8 shown · [on its own page](docs/by-pattern/support-triage.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=support-triage&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Content scoring

_Score quality, risk or relevance on an ordered scale._

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br>
  Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically.<br>
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐<br>
  Break one broad judgement into atomic scores and combine them with weights that live in your code, not in the prompt.<br>
  <sub>`Official docs` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.<br>
  <sub>`Project` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.<br>
  <sub>`Benchmark` · ★87,298 · `TS` · `choice`</sub>

  **Caveats:** `shadow mode`

- **[gptcache](https://github.com/zilliztech/GPTCache)**<br>
  Semantic cache for LLMs. Fully integrated with LangChain and llama_index.<br>
  <sub>`Project` · ★8,201 · zilliztech · `Py`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br>
  An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.<br>
  <sub>`Project` · ★5,414 · `Java` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.<br>
  <sub>`Tutorial` · ★4,578 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)**<br>
  Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.<br>
  <sub>`Project` · ★582 · `TS` · `choice` · `score` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)**<br>
  A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.<br>
  <sub>`Project` · ★324 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[llm2jev](https://github.com/Yinsongxu/LLM2Jev)**<br>
  Adapt local language models into Jev-compatible structured decision engines with Choice, Score, and Noul outputs powered by prefill-only binary inference.<br>
  <sub>`Project` · ★286 · yinsongxu · `Py`</sub>

**10 of 164** shown · [all 164 on one page →](docs/by-pattern/content-scoring.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Recommendation

_Choose what to surface next, fast enough for a live conversation._

- **[Jevflix](https://github.com/ArielBubis/Jevflix)**<br>
  Jev picks, you watch. A hybrid movie recommender: fast semantic + keyword search narrows 4,800 films to a shortlist, then TypeSafe Jev reads your constraints and picks the one film that fits - with a confidence score that decides whether to answer instantly or ask a follow-up.<br>
  <sub>`Project` · ★0 · arielbubis · `Py`</sub>

All 1 shown · [on its own page](docs/by-pattern/recommendation.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=recommendation&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

### Overview

_Surveys the model or the space rather than one pattern._

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐<br>
  Installs a TypeSafe skill into Claude Code so an agent can write correct Jev calls without you pasting the API shape each time.<br>
  <sub>`Official docs` · ★2,036 · `sh`</sub>

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐<br>
  The official agent-skills repository behind the Claude Code plugin, holding the SKILL.md that teaches an agent the System One API.<br>
  <sub>`Plugin` · ★2,036 · `sh`</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐<br>
  A drop-in TypeSafeClient replacement backed by ordinary LLM APIs, so you can run Jev-shaped code without Jev access.<br>
  <sub>`SDK` · ★285 · `Py`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐<br>
  The official TypeScript client. Ships ESM, CJS and type declarations, with lowercase choice()/score()/noul() helper factories.<br>
  <sub>`SDK` · ★232 · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐<br>
  The official Python client. Sync and async clients, retry policy with retry-after support, and Choice/Score/Noul helper classes.<br>
  <sub>`SDK` · ★219 · `Py` · `choice` · `score` · `noul`</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐<br>
  The one endpoint, POST /v1/systemone, with the exact request and answer shapes for all three question types.<br>
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐<br>
  The authoritative sheet: jev-1.13.0, $0.042 per Mtok input with output free, 64k context, 32k for state plus the longest question, text input only.<br>
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐<br>
  What each primitive is for and how to write criteria, including the 255-option cap on Choice and the 2-10 level range on Score.<br>
  <sub>`Official docs` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐<br>
  The launch post: what a System One model is, why decisions were split from generation, and the vendor's latency and cost claims.<br>
  <sub>`Article` · Diogo Almeida</sub>

  **Caveats:** `vendor numbers`

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐<br>
  The vendor's own list of where the model fails: literal reading, arithmetic and counting, date comparison, indirection, large noisy states, adversarial content.<br>
  <sub>`Official docs`</sub>

**10 of 451** shown · [all 451 on one page →](docs/by-pattern/overview.md) · [filter on the site](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=en)

<sub>[↑ Pattern index](#pattern-index)</sub>

## By resource kind

The same rows grouped by what you will find when you open the link.

| Kind | Examples | What you will find |
| --- | ---: | --- |
| **Official docs** | **31** | Vendor documentation, cookbooks and pattern pages. |
| **SDK** | **94** | Client libraries, official and community. |
| **Integration** | **34** | A gateway, framework or platform route to the model. |
| **Snippet** | **4** | Small runnable examples in this repository. |
| **Project** | **653** | An application or library that calls Jev in anger. |
| **Plugin** | **238** | Editor, agent and MCP integrations you can install. |
| **Tutorial** | **9** | Step-by-step material with code. |
| **Benchmark** | **70** | Measurement. Check whether it is independent or vendor-reported. |
| **Article** | **12** | Explainers, analysis and launch coverage. |
| **Video** | **3** | Walkthroughs and reviews. |
| **Discussion** | **2** | Threads worth reading, including the sceptical ones. |
| **Jev-like alternative** | **58** | Independent reimplementations. These do NOT call Jev. |

## Also in this repo

The parts that are not the catalog.

<details>
<summary><b>Preview the searchable catalogue</b></summary>

<a href="https://kydlikebtc.github.io/awesome-jev/?lang=en"><img src="https://kydlikebtc.github.io/awesome-jev/img/site-en.png?v=8689acd727850890" alt="Searchable Jev catalogue with curated paths, filters, dated source evidence and entry cards" width="760"></a>

<sub>Filter by clicking a bar. Two more views: <a href="https://kydlikebtc.github.io/awesome-jev/?view=prims">primitives</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat">compatibility</a>. Every filter and entry is a shareable URL.</sub>

</details>

| File | What it is |
| --- | --- |
| [`docs/patterns.md`](docs/patterns.md) | Every pattern defined, each with an explicit *when NOT to use this*. |
| [`docs/compatibility.md`](docs/compatibility.md) | Model string, field names, request shape, endpoint and env var differ per platform. This is that table. |
| [`docs/vetting.md`](docs/vetting.md) | What to check before trusting a row, and the one mistake most people make. |
| [`docs/status.md`](docs/status.md) | What week one of this ecosystem actually looked like, gaps included. |
| [`docs/method.md`](docs/method.md) | How the catalog was built, what was excluded, and where it is weakest. |
| [`docs/sources.md`](docs/sources.md) | Where every row came from, and the licence position. |
| [`examples/`](examples/) | Four runnable examples. One deliberately leaves the threshold policy to you. |
| [`schema/entry.schema.json`](schema/entry.schema.json) | What a catalog entry may contain. |
| [`.claude-plugin/`](.claude-plugin/) | Install the skill and the MCP server together in Claude Code: `/plugin marketplace add kydlikebtc/awesome-jev`, then `/plugin install awesome-jev@awesome-jev`. |
| [`src/awesome_jev_mcp/`](src/awesome_jev_mcp/) | An MCP server, so an agent can query the catalogue instead of reading it. Caveats travel with every result, and so does how current the data is. |
| [`skills/awesome-jev/`](skills/awesome-jev/) | An agent skill: the facts that generated Jev code most often gets wrong, and the design rules worth following. |
| [`scripts/verify_claims.py`](scripts/verify_claims.py) | Re-reads every cited call site weekly, so a primitive claim is checkable rather than asserted. |
| [`scripts/refresh_metadata.py`](scripts/refresh_metadata.py) | Re-reads stars, licences and archive status from the GitHub API and opens a PR. |

## What is verified, and what is not

- **Link checks** — 1205 rows carry an HTTP 2xx response and a `checked` date; 3 carry no dated success record. Dates vary by row and a past success does not guarantee availability today. Stars and licences are repository metadata snapshots.

- **Source and code review** — `evidence.path` cites the file read, `evidence.read_on` records the reported review date, and `evidence_none` explains missing file evidence. Reading a call site is separate from running it. Summaries include source descriptions and machine translations; see the [method and its limits](docs/method.md).

- **Call-site text checks** — 1122 rows record a file and matching strings in `evidence`. The weekly [claims job](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) checks that those strings remain on the default branch and reports missing text or files. This count measures recorded evidence, **not latest CI passes**. A text match does not prove that a call executes, the API is compatible, or the result is correct.

- **Runtime and performance not independently tested here** — treat every catalogue entry as untested by this repository, including entries without `code-untested`. Linked benchmarks describe their authors' measurements; this catalogue has not reproduced them. Repository build checks and package smoke tests do not exercise those integrations or the live Jev API, and inclusion is not a security review.


### What the tags mean

| Tag | Means |
| --- | --- |
| `not Jev itself` | Does not call Jev at all. A compatible API does not imply compatible calibration, so thresholds do not transfer. |
| `shadow mode` | Wired in but deliberately inert — nothing it returns reaches a user-visible decision. |
| `early access` | Needs waitlist access to run. |
| `code untested` | The code was read, not executed. |
| `one commit` | One commit, so maintenance is unlikely. |
| `no licence` | No LICENSE file, whatever a README badge claims. A blocker for reuse. |
| `3rd-party key` | Needs a key for a service other than TypeSafe. |
| `vendor numbers` | Repeats the vendor's own benchmarks rather than an independent measurement. |
| `unverified claims` | Makes measurement claims that could not be checked. |
| `AI-written` | Reads as machine-generated content. |
| `marketing` | Published to sell something as much as to explain. |
| `paywall` | Behind a paywall or a metered reader. |
| `archived` | Development has visibly stopped. |

### Retired links

Links that stopped resolving, kept so a dead reference stays searchable instead of vanishing.

| Example | Why |
| --- | --- |
| jev-atlas | Retired 2026-09-24: the repository returns 404 on both the API and the web while its owner's account still exists — deleted or made private. Kept here so the reference stays searchable. `HTTP 404` |
| jev-mac-voice | Retired 2026-09-24: the repository returns 404 on both the API and the web while its owner's account still exists — deleted or made private. Kept here so the reference stays searchable. `HTTP 404` |

## Machine-readable data

One entry per example, validated against a JSON Schema on every push.

| File | What it is |
| --- | --- |
| [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json) | 1208 entries |
| [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json) | 2 retired |
| [`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json) | The platform matrix behind `docs/compatibility.md` |
| [`patterns.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/patterns.json) | The decision taxonomy both generators and the MCP server read |
| [`collections.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/collections.json) | Bilingual editorial paths, selection reasons and limitations |
| [`schema/entry.schema.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/schema/entry.schema.json) | One entry's shape |
| [`llms.txt`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/llms.txt) | For agents, with the caveats spelled out |

## Contributing and licence

Corrections take priority over additions — a wrong row costs more than a missing one. See [CONTRIBUTING.md](CONTRIBUTING.md); the bar is *could a reader act on this row without opening the link?*

Code in `scripts/`, `site/` and `examples/` is [MIT](LICENSE-MIT). Catalog metadata is [CC0-1.0](LICENSE-CC0), with a per-row `license` field. Linked works keep their own licences — `repo_license` records what each declares.

**Maintenance checks:** [![lint](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml) · [Scheduled link checks](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml) · [Call-site text checks](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml)

---

**Jev Decision Atlas** · [↑ Back to top](#top) · [中文](README.zh-CN.md)
