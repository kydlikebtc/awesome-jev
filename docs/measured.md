# Measured, not claimed

<sub>[awesome-jev](../README.md) · [中文](measured.zh-CN.md)</sub>

Independent measurement reports in the catalogue, including **negative results** that help explain where an approach fails. These are the original authors' measurements; this repository has not independently reproduced them. Check each report's dataset, method and model version before comparing results.

Every independent measurement report and negative result in the catalogue — 74 rows — with every note and caveat tag, the negative results first. [The README](../README.md#measured-not-claimed) shows those, then the picks of the curated [independent reports](https://kydlikebtc.github.io/awesome-jev/?collection=measured&lang=en) path and the first few others; [the site](https://kydlikebtc.github.io/awesome-jev/?indep=1&lang=en) lists the same rows and can filter them further.

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](benchmarks.md) sets every benchmark's measurement side by side.

## Negative results first

Rows whose own author measured Jev for the use and concluded against it: a benchmark whose measurement's direction is *unfavourable*, or another row flagged *measured, not adopted*. Author-stated, not reproduced here. Read them before the positive examples; [the site lists them](https://kydlikebtc.github.io/awesome-jev/?neg=1&lang=en).

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br>
  Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it.<br>
  <sub>`Benchmark` · ★100k+ · `Py` · `noul` · [call site](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/jev_arm.py), read 2026-09-22 · author's conclusion: unfavourable (author-stated, not reproduced here)</sub>

  > The single most credible row in this catalog. Recall came out below their existing summariser, and at a matched context budget it tied plain recency ordering. Cost was genuinely far lower. Publishing a negative result on a hyped model is rare.

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.<br>
  <sub>`Benchmark` · ★10k+ · `TS` · `choice` · [call site](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js), read 2026-09-22 · author's conclusion: unfavourable (author-stated, not reproduced here)</sub>

  **Caveats:** `shadow mode`

  > Wired in but deliberately inert: by their own statement nothing Jev returns reaches a label, a cache row or an alert. Ships a golden fixture. A model to copy for how to trial a new model without betting production on it.

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.<br>
  <sub>`Plugin` · ★1k+ · `Py` · `choice` · `score` · `noul` · [call site](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py), read 2026-09-22</sub>

  **Caveats:** `measured, not adopted`

  > Notable for publishing a use it dropped: Jev-summarised handoffs had worse recall than raw transcripts.

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)**<br>
  One Score per candidate file to pre-brief code review — measured twice, then removed: more billed input for essentially no wall-clock gain, and offline replay showed the candidate list could not reach where review findings land.<br>
  <sub>`Benchmark` · ★1k+ · `Go` · `score` · author's conclusion: unfavourable (author-stated, not reproduced here)</sub>

  > Removed in PR #1165 (2026-09-22). Their offline measurement found the candidate generator excluded changed files by construction while nearly all review findings sit in changed files, and that per-file excerpts made the list less precise at higher token cost. The code is gone from the default branch, so this row cites the change that removed it.

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)**<br>
  Claude Code hook asking Jev which installed skill fits each prompt: a choice ranks all skills beside three noul gates, then a choice and a noul per skill judge the top three, none suggested under 0.30. Shadow mode only logs; in the author's week, 28 of 539 suggestions were followed by that skill. <sub>(written by a model)</sub><br>
  <sub>`Plugin` · ★10+ · shimo4228 · `Py` · [call site](https://github.com/shimo4228/jev-skill-router/blob/HEAD/scripts/jev_client.py), read 2026-09-22</sub>

  **Caveats:** `measured, not adopted`

  > Its author ran it on 2026-09-21 and concluded that, as a router, it is unlikely to help a strong model, which already sees every skill's description. Its README: 6 of 6 scripted requests handled sensibly on 0.2.0, 3 of 6 real-session prompts wrong on 0.1.0, which the author calls an anecdote, not a rate. It stays in shadow mode. https://dev.to/shimo4228/i-added-jevs-skill-router-to-claude-code-and-turned-back-just-before-rewriting-the-skill-listing-34in A model wrote this row's Chinese note.

## Other independent reports

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)**<br>
  Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.<br>
  <sub>`Benchmark` · ★100+ · kitfunso · `TS` · [call site](https://github.com/kitfunso/hippo-memory/blob/HEAD/src/rerankers/jev.ts), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)**<br>
  An introduction to Jev with hands-on tests: Choice, Score and Noul turn natural language into typed judgements for classification, scoring and routing, compared with DeepSeek on comment labelling, speed and results, with CSV import, replay and offline reports.<br>
  <sub>`Benchmark` · ★100+ · nanmicoder · `JS` · [call site](https://github.com/NanmiCoder/jev-arena/blob/HEAD/src/backends/jev.mjs), read 2026-09-24</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)**<br>
  Benchmark Heaven's benchmark for Jev and Jev-compatible decision models: noul, choice and score tasks, sent through a /v1/systemone adapter and scored for accuracy, calibration, latency and cost. Release v1.6.1 (2026-10-06); some inputs are sealed, so it cannot be fully rerun independently. <sub>(written by a model)</sub><br>
  <sub>`Benchmark` · ★100+ · fstandhartinger · `Py` · [call site](https://github.com/fstandhartinger/jevbench/blob/HEAD/jevbench/adapters/typesafe.py), read 2026-09-22</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)**<br>
  Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · abdelstark · `Py` · [call site](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/src/jev_benchmarks/adapters/jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)**<br>
  Independent community map, mostly in Chinese, of which tasks suit Jev and why, from test suites with saved API calls, not a leaderboard: accurate when the answer is in the given text, like which DOM element to click, and miscalibrated elsewhere (48% right at 0.819 mean confidence on DAIR Emotion). <sub>(written by a model)</sub><br>
  <sub>`Benchmark` · ★10+ · zaious · `Py` · [call site](https://github.com/Zaious/jev-capability-atlas/blob/HEAD/scripts/common/jev_client.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)**<br>
  Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · jmanhype · `Py` · [call site](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/src/jev_dspy_lab/live.py), read 2026-09-22</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)**<br>
  Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark. <sub>(earlier upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · anisselbd · `Py` · [call site](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/run_jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)**<br>
  Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · erendikmenn · `Py` · [call site](https://github.com/erendikmenn/jev-rag-benchmark/blob/HEAD/src/jev_rag_benchmark/rerankers.py), read 2026-09-22 · author's conclusion: favourable (author-stated, not reproduced here)</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)**<br>
  An independent head-to-head against dedicated rerankers across fourteen datasets.<br>
  <sub>`Benchmark` · ★10+ · anessbelbati · `Py` · [call site](https://github.com/anessbelbati/jev-rerank-bench/blob/HEAD/rerankers/jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

  > An independent measurement rather than a vendor figure, and a direct comparison against purpose-built rerankers — the comparison that matters for the search-ranking pattern.

- **[jev-robot-control](https://github.com/openroboto-ai/jev-robot-control)**<br>
  Jev against two LLMs on direct Cartesian control of an xArm7 in MuJoCo — intent, movement and gripper each step — with recorded responses, trajectories and replays. One seed-0 trial per controller, not a success rate.<br>
  <sub>`Benchmark` · ★10+ · openroboto-ai · `Py` · [call site](https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/incremental-comparisons/20260919-193012-198478-0/sources/incremental_policy.py), read 2026-09-24 · author's conclusion: inconclusive (author-stated, not reproduced here)</sub>

  **Caveats:** `one commit`

- **[jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval)**<br>
  Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · zhuyansen · `Py` · [call site](https://github.com/zhuyansen/jev-search-rerank-eval/blob/HEAD/src/jse/openrouter.py), read 2026-09-24 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)**<br>
  LegalForecast-MTD benchmark alpha and official evaluation workflows <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · johnhughes3 · `Py` · [call site](https://github.com/johnhughes3/LegalForecastBench/blob/HEAD/legalforecast/jev/execution.py), read 2026-09-22</sub>

- **[pdf-race](https://github.com/goodrahstar/pdf-race)**<br>
  Races three pipelines on 12 arXiv papers: Docling then Jev, Docling then Gemini 3.8 Flash, and Gemini reading the PDF, each answering four questions per paper scored against arXiv's metadata. All got 12 of 12 categories and titles; the Jev lane cost $0.0022 against $0.036 and $0.088. <sub>(written by a model)</sub><br>
  <sub>`Benchmark` · ★10+ · goodrahstar · `JS` · [call site](https://github.com/goodrahstar/pdf-race/blob/HEAD/lib/lanes.mjs), read 2026-09-24</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)**<br>
  Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · myc0576 · `Py` · [call site](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/inference-benchmarks)**<br>
  A gateway that mimics the structured-output shape, used to benchmark against it.<br>
  <sub>`Benchmark` · ★10+ · iammrduncan · `TS` · [call site](https://github.com/iammrduncan/inference-benchmarks/blob/HEAD/packages/demos/lib/jev.ts), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)**<br>
  A WebMCP benchmark, measures WebMCP against other browser-agent interfaces. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ★10+ · nekuda-ai · `TS` · [call site](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/experiments/jev/frozen/arms/decision-providers.mjs), read 2026-09-22</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)**<br>
  An experimental protocol for evidence-aware agent handoffs, bounded worker continuation, and TypeSafe/Jev-assisted review, with reproducible evaluation. <sub>(earlier upstream description)</sub><br>
  <sub>`Benchmark` · zsoxi · `Py` · [call site](https://github.com/zsoXi/agent-handoff-gate/blob/HEAD/tools/build_benchmark_prompts.py), read 2026-09-22</sub>

  **Caveats:** `one commit` · `archived`

- **[antigravity-mcp-semantic-search-with-typesafeai](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)**<br>
  Fast semantic code search & diff sanity auditor for AI coding assistants (Antigravity, Cursor, Claude Code) powered by TypeSafe System One. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · greenyamao · `Py` · [call site](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi/blob/HEAD/mcp_server.py), read 2026-09-22</sub>

- **[can-jev-bayes](https://github.com/TomRichner/can-jev-bayes)**<br>
  Jev Bayes, No? Testing TypeSafe AI's Jev against Bayesian-optimal strategies, and testing if Jev can effectivly use Bayesian priors. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · tomrichner · `Py` · [call site](https://github.com/TomRichner/can-jev-bayes/blob/HEAD/src/jevbandits/client.py), read 2026-09-24</sub>

- **[Decision Models as Guardrails](https://dm-as-guardrails.raxitlabs.com)**<br>
  Asks Jev 1.13.0, Jev 1.14.0 and 17 other systems, Bedrock Guardrails among them, the same 9,975 labelled guardrail checks in six suites. Jev answers each as a noul; 0.5 or more blocks, nothing tuned per model. Reports balanced accuracy with 95% intervals and USD per 1,000 checks at list price.<br>
  <sub>`Benchmark` · raxIT Labs · `Py` · `noul` · `score` · [call site](https://github.com/raxITlabs/decision-models-as-guardrails/blob/HEAD/benchmark/goldrails_bench/systemone.py)</sub>

  **Caveats:** `self-submitted`

  > Submitted by raxIT Labs, which built and ran it. Version 1.0.0 (15 Oct 2026): balanced accuracy 90.4 for the Perplexity Decisions API, 88.7 for Jev 1.14.0, 79.0 for Bedrock Guardrails; Jev 1.14.0 costs $39 per million checks at list price, Bedrock $113. One fixed 0.5 threshold, no per-model calibration. Drafted with an AI coding assistant.

- **[decision-bench](https://github.com/Hanno-Labs/decision-bench)**<br>
  Open benchmark runtime for document-grounded decision models <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · hanno-labs · `Py` · [call site](https://github.com/Hanno-Labs/decision-bench/blob/HEAD/src/decision_bench/models/jev_openrouter.py), read 2026-09-24</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)**<br>
  Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design. <sub>(earlier upstream description)</sub><br>
  <sub>`Benchmark` · xienda · `JS` · [call site](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)**<br>
  Jev drives your Ego Lite browser: one typed-choice request per step. Single-file, zero-dependency port of browser-use/jev-ultrafast with multi-model benchmarks and extra guardrails. Unofficial. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · shikaizhong-design · `JS` · [call site](https://github.com/shikaizhong-design/ego-jev-ultrafast/blob/HEAD/jego.js), read 2026-09-22</sub>

- **[jev-acento](https://github.com/marcosmartinez/jev-acento)**<br>
  ¿Jev entiende tu acento? Pre-registered audit of TypeSafe AI's Jev on Spanish — accuracy, calibration and token cost — plus a CLI to run the same comparison on your own labelled data. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · marcosmartinez · `Py` · [call site](https://github.com/marcosmartinez/jev-acento/blob/HEAD/src/jev_acento/providers.py), read 2026-09-24</sub>

  > An independent, pre-registered audit of the model outside English — the gap docs/status.md lists as worth watching.

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)**<br>
  Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset). <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · tokentrim · `Py` · [call site](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/HEAD/src/jevbench/backends/jev.py), read 2026-09-22</sub>

- **[jev-bench](https://github.com/TheWayWithin/jev-bench)**<br>
  Does the cited source actually say it? A 42-claim benchmark: Jev (TypeSafe System One) against GPT-5.4, Claude Sonnet 5 and Gemini 3.1 Pro. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · thewaywithin · `Py` · [call site](https://github.com/TheWayWithin/jev-bench/blob/HEAD/run.py), read 2026-09-24</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)**<br>
  Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · wondertwins · `Py` · [call site](https://github.com/wondertwins/jev-benchmark/blob/HEAD/jevcommon/client.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)**<br>
  Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · themsquared · `Py` · [call site](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py), read 2026-09-24</sub>

- **[jev-calibration-audit](https://github.com/tapesymbolstate/jev-calibration-audit)**<br>
  Independent API-only calibration audit of TypeSafe AI's Jev decision model <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · jujumilk3 · `Py` · [call site](https://github.com/tapesymbolstate/jev-calibration-audit/blob/HEAD/src/jev_audit/client.py), read 2026-09-22</sub>

  **Caveats:** `one commit`

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)**<br>
  Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break<br>
  <sub>`Benchmark` · nikkoxgonzales · `Py` · [call site](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py), read 2026-09-22</sub>

- **[jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark)**<br>
  Comparing Jev, Gemini Flash, and Claude Fable on Python code review rules: cost, speed, accuracy, and consistency. Includes results, charts, and reproducible experiments. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · gemanor · `Py` · [call site](https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/determinest/clients.py), read 2026-09-24 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)**<br>
  Does TypeSafe's Jev keep its accuracy and calibration on Russian? Independent RU vs EN audit (ECE, reliability diagrams, paired bootstrap) on parallel human-labelled data. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ahtoooxa · `Py` · [call site](https://github.com/AHTOOOXA/jev-cyrillic-audit/blob/HEAD/src/jev_cyrillic_audit/run.py), read 2026-09-24</sub>

  > An independent calibration audit outside English — the gap docs/status.md lists as worth watching.

- **[jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks)**<br>
  JEV decision benchmark results on MetaTool, When2Call, and BFCL V4, with bilingual tables and reproducible reports. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · baibizhe · `Py` · [call site](https://github.com/baibizhe/jev-decision-benchmarks/blob/HEAD/scripts/build_tables.py), read 2026-09-24</sub>

  **Caveats:** `no licence`

- **[jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)**<br>
  Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · kantahayashiai · `JS` · [call site](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/HEAD/src/run.mjs), read 2026-09-24</sub>

- **[jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric)**<br>
  Architecture for running many semantic decisions through one validated path, with a labelled 111-case benchmark comparing TypeSafe Jev against a Claude baseline, and a dashboard for inspecting any single decision. Experimental, not production. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · ghubnab99 · `C#` · [call site](https://github.com/ghubnab99/jev-enterprise-decision-fabric/blob/HEAD/src/DecisionFabric.TypeSafe/TypeSafeClientOptions.cs), read 2026-09-22</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)**<br>
  Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost<br>
  <sub>`Benchmark` · 4esv · `Py` · [call site](https://github.com/4esv/jev-eval/blob/HEAD/evaljev/runners.py), read 2026-09-22</sub>

  **Caveats:** `no licence`

- **[jev-eval](https://github.com/onlyoneaman/jev-eval)**<br>
  TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · onlyoneaman · `TS` · [call site](https://github.com/onlyoneaman/jev-eval/blob/HEAD/jev_eval/backends.py), read 2026-09-24</sub>

  **Caveats:** `one commit`

- **[jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval)**<br>
  A third-party check of Jev against two LLMs under identical conditions: routing booking inquiries to a photo-shoot service for tourists in Japan, sixty synthetic messages in four languages.<br>
  <sub>`Benchmark` · shogo-nfrealmusic · `TS` · [call site](https://github.com/Shogo-nfrealmusic/jev-eval/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

  **Caveats:** `no licence`

- **[jev-exploration](https://github.com/SamuelSacco/jev-exploration)**<br>
  Jev (TypeSafe) exploratory thread: claim audit, live demos, and runnable code <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · samuelsacco · `Py` · [call site](https://github.com/SamuelSacco/jev-exploration/blob/HEAD/jevlab/client.py), read 2026-09-22</sub>

- **[jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench)**<br>
  Measured: asking TypeSafe Jev N questions in one call bills the state once. 2,976 real requests, raw data, exact billing check. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · blowxian · `Py` · [call site](https://github.com/blowxian/jev-fanout-bench/blob/HEAD/bench.py), read 2026-09-24</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)**<br>
  Reproducible early-access evaluation of Jev on Korean understanding and medical text, with runtime and cost evidence <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · mahlernim · `Py` · [call site](https://github.com/mahlernim/jev-korean-benchmark/blob/HEAD/jevbench/medqa_run.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

  **Caveats:** `no licence`

- **[jev-lab](https://github.com/danielhirt/jev-lab)**<br>
  Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · danielhirt · `TS` · [call site](https://github.com/danielhirt/jev-lab/blob/HEAD/packages/codenames/src/judge.ts), read 2026-09-24</sub>

  **Caveats:** `no licence`

- **[jev-lab](https://github.com/llt22/jev-lab)**<br>
  Hands-on research lab for TypeSafe's Jev (System One model): reproducible benchmarks of Noul/Choice/Score primitives, confidence gating, fan-out latency, agent control — plus a living audit of the Jev ecosystem. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · llt22 · `Py` · [call site](https://github.com/llt22/jev-lab/blob/HEAD/experiments/json-render-jev/src/demo.tsx), read 2026-09-24</sub>

  **Caveats:** `no licence`

- **[jev-lab](https://github.com/Menny1337/jev-lab)**<br>
  TypeScript experiments, evaluations, and latency benchmarks for TypeSafe's Jev model <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · menny1337 · `TS` · [call site](https://github.com/Menny1337/jev-lab/blob/HEAD/src/client.ts), read 2026-09-24</sub>

  **Caveats:** `no licence`

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)**<br>
  A show-and-tell capability study for Jev, TypeSafe's System One decision model. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · lbotinelly · `TS` · [call site](https://github.com/lbotinelly/jev-little-airways/blob/HEAD/demo/js/jev-monitor.mjs), read 2026-09-22</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)**<br>
  Benchmark-driven Jev router and judge for cost-aware, reliable LLM coding workflows <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · erendikmenn · `Py` · [call site](https://github.com/erendikmenn/jev-llm-router-benchmark/blob/HEAD/src/jev_router/providers/review.py), read 2026-09-22</sub>

- **[jev-no-enem](https://github.com/patryckalves/jev-no-enem)**<br>
  Reproducible benchmark evaluating TypeSafe AI's Jev (System One paradigm) on Brazil's ENEM 2025 standardized exam. Evaluates typed decision-making, domain-specific accuracy, and RLCD uncertainty calibration against open LLM baselines with an interactive GitHub Pages dashboard. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · patryckalves · `Py` · [call site](https://github.com/patryckalves/jev-no-enem/blob/HEAD/src/evaluate_jev.py), read 2026-09-24</sub>

  **Caveats:** `no licence`

  > An independent evaluation outside English, on a public exam with known answers.

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)**<br>
  Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~<br>
  <sub>`Benchmark` · scienthoon · `Py` · [call site](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)**<br>
  Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · yodablocks · `Py` · [call site](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py), read 2026-09-22</sub>

- **[jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong)**<br>
  Jev plays browser table tennis in real time: structured telemetry, typed decisions, ordinary Chrome inputs, and auditable evidence. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · icohen007 · `JS` · [call site](https://github.com/Icohen007/jev-play-ping-pong/blob/HEAD/src/typesafe.mjs), read 2026-09-22</sub>

- **[jev-playground](https://github.com/hegargarcia/jev-playground)**<br>
  Benchmarks Jev against other evaluation models in games with explicit states and legal actions: code owns the rules and transitions, each model picks the next action, and outcomes are measured.<br>
  <sub>`Benchmark` · hegargarcia · `TS` · [call site](https://github.com/hegargarcia/jev-playground/blob/HEAD/src/app/api/connect-four/move/route.ts), read 2026-09-24</sub>

  **Caveats:** `no licence`

- **[jev-plays](https://github.com/mansicer/jev-plays)**<br>
  A System One model plays Craftax while an LLM sets the goals: five agents on the same map, from Jev on raw actions to an LLM controlling every step, compared in logged episodes.<br>
  <sub>`Benchmark` · mansicer · `Py` · [call site](https://github.com/mansicer/jev-plays/blob/HEAD/craftax_agent/jev_policy.py), read 2026-09-24</sub>

- **[jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment)**<br>
  Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · tokentrim · `Py` · [call site](https://github.com/TokenTrim/jev-routing-experiment/blob/HEAD/jev_router/jev.py), read 2026-09-22</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)**<br>
  Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · teyhouse · `Py` · [call site](https://github.com/teyhouse/jev-secret-detection/blob/HEAD/main.py), read 2026-09-22</sub>

  **Caveats:** `no licence`

- **[jev-sim](https://github.com/dashbi1/jev-sim)**<br>
  Jev-compatible /v1/systemone server reading typed decisions from LLM logits, benchmarked against TypeSafe's Jev on the same items via JevBench <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · dashbi1 · `Py` · [call site](https://github.com/dashbi1/jev-sim/blob/HEAD/jev_sim/cli.py), read 2026-09-22</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)**<br>
  Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · sypherin · `Py` · [call site](https://github.com/sypherin/jev-trace-classifier/blob/HEAD/jev_client.py), read 2026-09-22</sub>

- **[jevarena](https://github.com/chenmingtang830/jevarena)**<br>
  Open-source BYOK arena for Jev and other AI judges. Find failures, compare quality, cost, and latency. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · chenmingtang830 · `TS` · [call site](https://github.com/chenmingtang830/jevarena/blob/HEAD/jevjudge/providers.py), read 2026-09-24</sub>

- **[jevbench](https://github.com/GautamTalksDev/jevbench)**<br>
  Preregistered, bias-corrected test of TypeSafe Jev's calibration under human disagreement (ChaosNLI, 100 labels per item) <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · Gautam Khosla · `Py` · `choice` · `noul` · [call site](https://github.com/GautamTalksDev/jevbench/blob/HEAD/jevbench/clients/jev.py) · author's conclusion: mixed (author-stated, not reproduced here)</sub>

  **Caveats:** `AI-written` · `self-submitted`

  > Submitted by its own author, who discloses that this entry was written with Claude Code and that the repository was built with AI coding assistance; the flags record that disclosure. Choice is close to calibrated on 750 low-disagreement items but overconfident on 750 high-disagreement ones (confidence 0.807 vs 0.468 agreement; bias-corrected ECE gap 0.264 vs a preregistered 0.09); Noul (0.076) is inconclusive. Aggregates are committed, per-call responses are not.

- **[jevsbistro](https://github.com/andrewsilber/JevsBistro)**<br>
  3D restaurant service simulator for benchmarking low-latency decision models <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · andrewsilber · `TS` · [call site](https://github.com/andrewsilber/JevsBistro/blob/HEAD/src/jev/protocol.ts), read 2026-09-22</sub>

- **[origin-civilization](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)**<br>
  AI life-and-civilization simulation: TypeSafe Jev makes every decision (typed, probabilistic, auditable); LLMs plan — OpenAI-compatible APIs, local models (Ollama, LM Studio), Claude Code, Codex. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · jacquesgariepy · `TS` · [call site](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION/blob/HEAD/legacy/source/providers.js), read 2026-09-22</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)**<br>
  Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · zsavage8 · `Py` · [call site](https://github.com/zsavage8/padflow-jev-evals/blob/HEAD/scripts/run_baseline.py), read 2026-09-22</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)**<br>
  Synthetic smoking-history extraction benchmark comparing TypeSafe Jev and OpenAI structured outputs, with reproducible accuracy, cost, and latency results. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · vclic · `Py` · [call site](https://github.com/vclic/smoking-extraction-benchmark/blob/HEAD/smoking_eval/providers.py), read 2026-09-22</sub>

  **Caveats:** `one commit` · `no licence`

- **[sysone-bench](https://github.com/instax-dutta/sysone-bench)**<br>
  First independent head-to-head benchmark of System One decision models (Laya vs Jev) on byte-identical inputs <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · instax-dutta · `Py` · [call site](https://github.com/instax-dutta/sysone-bench/blob/HEAD/runners/jev_runner.py), read 2026-09-22</sub>

- **[typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review)**<br>
  About calibrating Jev for code reviews <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · selmar · `Py` · [call site](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review/blob/HEAD/calibrate.py), read 2026-09-24</sub>

  **Caveats:** `no licence`

- **[what-is-jev](https://github.com/g0runmezadam/what-is-jev)**<br>
  Independent, source-linked research on TypeSafe AI's Jev (System One), with 947 rubric-scored public repositories, recurring patterns, datasets, and bilingual documentation. <sub>(upstream description)</sub><br>
  <sub>`Benchmark` · g0runmezadam · `Py`</sub>

  > Research about the ecosystem rather than a caller of the API, so it carries no call-site evidence.

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br>
  Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.<br>
  <sub>`Benchmark` · ★100+</sub>

  **Caveats:** `no licence` · `unverified claims`

  > The most actionable engineering caveat found anywhere: if option order alone can move a probability past your threshold, your threshold is not as stable as it looks. Independent and unreplicated, so treat the magnitude as indicative.

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br>
  The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.<br>
  <sub>`Benchmark` · Lindfors</sub>

  > Methodology is stated cleanly and scoped honestly as a single-day snapshot. Leading with a failure case is what makes it a real calibration test rather than a testimonial.

- **[Support-routing benchmark: 100 held-out cases](https://decisionmodelhub.com/benchmarks/support-routing)**<br>
  Compares Jev with Clef, Clef Flash, OpenAI's Decisions API and a GPT-6 Luna structured-output baseline on 100 held-out fictional support messages, each routed to one of five team labels; every case and recorded answer can be downloaded.<br>
  <sub>`Benchmark` · DecisionModelHub</sub>

  **Caveats:** `self-submitted`

  > Submitted by the site's own maintainer. Jev: 92 of 100 correct (95% interval 85 to 96), median 138 ms, in a single run. The page reports intervals and no paired comparison between models. Cases are fictional and were drafted with AI assistance, then reviewed by two people. The runner code is not public; the cases, per-case answers and probabilities are. This row was drafted with an AI coding assistant.

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br>
  The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.<br>
  <sub>`Benchmark` · Near Here</sub>

  > Self-limits correctly: a use-case study, not a model leaderboard. That restraint is rarer than the numbers.

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
