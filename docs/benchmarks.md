<!-- Written by scripts/build_benchmarks.py from catalog.json. Edit that, not this file. -->

# Benchmarks, indexed

<sub>[awesome-jev](../README.md) · [中文](benchmarks.zh-CN.md)</sub>

Every `kind: benchmark` row that carries a `measurement`: what its own author measured, indexed field by field from the author's report. This repository measured and re-ran none of it. A **direction** is the author's own conclusion about Jev for that task, author-stated and not reproduced here, and is left blank where the author states none in words. Task, dataset and comparator names are recorded as the author names them.

**73** benchmark rows; **27** carry a measurement. Of those, a person has read **0** against their report (`measurement.read_on`) and only a model **0** (`measurement.model_read_on`); a script or a model filled in the other **27** and nobody has read them back. The review queue lists [the unread rows](review-queue.md#measurement-unread) and [those only a model has read](review-queue.md#model-read). How the fields were first filled in: [docs/method.md](method.md). Field rules: [CONTRIBUTING](../CONTRIBUTING.md#field-rules).

## Direction by decision pattern

Benchmark rows per decision pattern, by the direction their authors state. A row filed under several patterns counts under each.

| Pattern | favourable (author-stated, not reproduced here) | mixed (author-stated, not reproduced here) | unfavourable (author-stated, not reproduced here) | inconclusive (author-stated, not reproduced here) | none stated | no measurement recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Tool selection | · | 1 | · | 1 | 1 | 8 |
| Intent routing | · | 1 | · | · | · | 1 |
| Context compaction | · | · | 1 | · | · | 1 |
| Safety gating | · | 2 | · | · | 2 | 6 |
| Output validation | 1 | 2 | · | · | · | 8 |
| Human escalation | · | 4 | · | · | 2 | 4 |
| Speculative fan-out | · | · | · | · | · | 1 |
| Search & ranking | 1 | 3 | 1 | · | · | 1 |
| Structured extraction | · | · | · | · | · | 1 |
| Classification | · | 1 | 1 | · | 2 | 7 |
| Document triage | · | 1 | · | · | 1 | · |
| Support triage | · | · | · | · | 1 | · |
| Content scoring | · | 2 | 1 | · | · | 6 |
| Overview | · | 3 | · | · | 2 | 19 |

## By comparator

What authors compared Jev with, as each names it, and the rows that did.

| Comparator | Rows |
| --- | --- |
| Laya | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench), [jev-capability-atlas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-capability-atlas), [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| Clef | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails), [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) |
| Amazon Bedrock Guardrails | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| ash keyword ranker | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-search-rerank-eval) |
| BART-MNLI | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench-human-disagreement) |
| base order without a reranker | [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=en#hippo-memory) |
| bge-m3 | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-search-rerank-eval) |
| bge-reranker-v2-m3 | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| BM25 | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-search-rerank-eval) |
| Claude Fable 5.1 | [jev-code-review-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-code-review-benchmark) |
| Claude Haiku 4.5 | [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-phishing-bench) |
| Claude Opus 5 | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) |
| Clef Flash | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) |
| Cohere Rerank 3.5 | [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rag-benchmark) |
| Cohere Rerank 4 Fast | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| Cohere Rerank 4 Pro | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| decider-4b v2 | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) |
| Decisions API | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) |
| DeepSeek Flash | [jev-arena](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-arena) |
| DeepSeek V4.1 Flash | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| DeepSeek V4.1 Flash labeller | [worldmonitor: news threat classification](https://kydlikebtc.github.io/awesome-jev/?lang=en#worldmonitor-shadow-mode) |
| deterministic rule baseline | [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=en#smartmoney-cub) |
| djev | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) |
| fuzzy name-matching heuristic | [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmark) |
| Gemini 3.6 Flash | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) |
| Gemini 3.8 Flash | [jev-code-review-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-code-review-benchmark) |
| Gemini 3.8 Flash on the parsed text | [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#pdf-race) |
| Gemini 3.8 Flash reading the PDF | [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#pdf-race) |
| GLiNER2 | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) |
| GLiNER2.5 (fastino/gliner2.5-multi-v1) | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) |
| GPT-4.1 mini | [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robot-control) |
| GPT-5.6 Luna | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) |
| GPT-5.6 Luna, reasoning effort none | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-korean-benchmark) |
| GPT-5.6 SOL | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) |
| GPT-6 Astra | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) |
| GPT-6 Astra, low reasoning | [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robot-control) |
| GPT-6 Luna | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) |
| Hermes summary compaction with session_search recovery | [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-agent-jev-evaluation) |
| Hermes summary compaction, closed-book | [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-agent-jev-evaluation) |
| hybrid order without a reranker | [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rag-benchmark) |
| Imajev-4B | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) |
| JevK5 v0.2.0 | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) |
| Kev | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| Laya 421M | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| local cross-encoder reranker | [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=en#hippo-memory) |
| Needle 3, local | [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-benchmark) |
| Open-Jev | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| Open-Jev 9B | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| OpenAI Decisions API | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| Perplexity Decisions API | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| Plumb-4B | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) |
| Qwen 3.8 27B on Cerebras, structured output | [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-benchmark) |
| Qwen3-Reranker-4B | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| random mover | [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmark) |
| recency-ranked tool retention at the same budget | [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-agent-jev-evaluation) |
| regex rule on link hosts | [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-phishing-bench) |
| Sonnet 5 | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) |
| Stockfish | [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmark) |
| Strands Deciders | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| text-embedding-3-small | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-search-rerank-eval) |
| the same review without the pre-brief | [no-mistakes: Jev review pre-brief, measured and retired](https://kydlikebtc.github.io/awesome-jev/?lang=en#no-mistakes-review-context) |
| ZeroEntropy zerank-2 | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |

## By dataset

Named datasets and benchmark suites the measurements used, as each author names them.

| Dataset | Rows |
| --- | --- |
| AG News | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) |
| Banking77 | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) |
| Belebele | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-korean-benchmark) |
| BRIGHT | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| BTZSC | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) |
| ChaosNLI | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench-human-disagreement) |
| CodeSearchNet | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| CommonsenseQA | [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) |
| DAIR Emotion | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) |
| finance-jev-v1 | [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=en#smartmoney-cub) |
| FiQA-2018 | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| HellaSwag | [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) |
| JevBench | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) |
| KorMedMCQA | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-korean-benchmark) |
| LongMemEval | [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=en#hippo-memory) |
| MedQA | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-korean-benchmark) |
| MIRACL | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| Natural Questions | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| NevIR | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| NFCorpus | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| OpenBookQA | [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) |
| PAWS-X | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-korean-benchmark) |
| PhishNChips v5.2 | [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-phishing-bench) |
| raxITLabs/decision-models-as-guardrails | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |
| SciFact | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| Support routing v1 | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) |
| TREC-COVID | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) |
| WindTunnel | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) |
| XQuAD-TR | [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rag-benchmark) |

## Every measured report

Rows by star band, then title. **Independent** is yes unless the row is flagged vendor-reported. **Raw data**: yes when the author publishes per-item results or raw responses, no when the author says only aggregates are published, — when neither is established. **Pre-registered**: yes when the author states the protocol or set was fixed before the run. **Taken** is the measurement's `as_of`, else the row's publication date. **Read** is the day a person read the report against the fields; a date marked *(model)* is a model's reading, not yet checked by a person.

| Row | Stars | Independent | Raw data | Pre-registered | Caveats | Task | Metrics | n | Model string | Taken | Direction (author-stated, not reproduced here) | Read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-agent-jev-evaluation) | ★100k+ | yes | — | — | — | Compact long agent transcripts with a port of fast-jev-compaction and score recall on a fixed question exam · [report](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/results/SCORECARD-2026-09-19-jev.md) | recall, tokens, cost, latency | 45 | `~typesafe/jev-latest` | 2026-09-19 | unfavourable | — |
| [worldmonitor: news threat classification](https://kydlikebtc.github.io/awesome-jev/?lang=en#worldmonitor-shadow-mode) | ★10k+ | yes | — | — | `shadow mode` | Label news headlines' threat level, scored on alerts against a blind human judgement · [report](https://github.com/koala73/worldmonitor/pull/8326) | recall, precision | 413 | `jev-1.13.0` | 2026-09-19 | unfavourable | — |
| [no-mistakes: Jev review pre-brief, measured and retired](https://kydlikebtc.github.io/awesome-jev/?lang=en#no-mistakes-review-context) | ★1k+ | yes | yes | — | — | Pre-brief a code review with a Jev-ranked list of candidate files, one Score per file · [report](https://github.com/kunchenguid/no-mistakes/blob/HEAD/benchmarks/issue-1055/results.md) | tokens, latency, recall, precision | — | `jev-1.13.0` | 2026-09-19 | unfavourable | — |
| [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=en#hippo-memory) | ★100+ | yes | — | — | — | Rerank memory-recall candidates with one Noul per candidate, scored on ranking and on graded answers · [report](https://github.com/kitfunso/hippo-memory/blob/HEAD/docs/evals/2026-09-19-jev-reranker.md) | ranking quality, recall, accuracy, latency, cost | 300 | `jev-1.13.0` | 2026-09-19 | mixed | — |
| [jev-arena](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-arena) | ★100+ | yes | yes | — | — | Label comments for relevance, sentiment and intent, scored against an independent AI reference labelling · [report](https://github.com/NanmiCoder/jev-arena/blob/HEAD/audit/accuracy-0919-124001/report.md) | accuracy, F1, latency, cost | 10000 | `typesafe/jev-1.13` | 2026-09-19 | — | — |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) | ★100+ | yes | — | — | — | Rank decision models on bounded-rubric decisions by accuracy above chance, calibration, speed and cost | accuracy, calibration, latency, cost | — | `jev-1.13.0` | 2026-09-19 | — | — |
| [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) | ★10+ | yes | no | yes | — | Zero-shot single-label text classification with per-label probabilities, scored on accuracy, calibration and coverage at a fixed error budget · [report](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/results/reports/btzsc-pilot-v1.md) | accuracy, F1, calibration, latency, tokens | 300 | `jev-1.13.0` | 2026-09-17 | mixed | — |
| [jev-capability-atlas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-capability-atlas) | ★10+ | yes | yes | — | — | Map where Jev's calibrated decisions hold and where they break, across small suites of its own and third-party reports | accuracy, calibration, latency | — | `jev-latest` | 2026-09-18 | mixed | — |
| [jev-dspy-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-dspy-lab) | ★10+ | yes | yes | — | — | Confidence-gated support-ticket routing in a DSPy-style pipeline, on synthetic cases · [report](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/evidence/live/jev-latest/benchmark.md) | accuracy, calibration, latency, cost, tokens | 24 | `jev-latest` | 2026-09-17 | — | — |
| [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-phishing-bench) | ★10+ | yes | no | — | — | Decide whether an email agent should click the link in an email · [report](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/results/report.md) | accuracy, recall, calibration, robustness, latency, cost | 2000 | `jev-1.13.0` | 2026-09-17 | mixed | — |
| [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rag-benchmark) | ★10+ | yes | yes | — | — | Rerank hybrid-retrieval candidates for a small RAG system with batched Nouls, then answer from the top five | recall, ranking quality, F1, latency, cost | 1044 | `typesafe/jev-1.13` | 2026-09-20 | favourable | — |
| [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) | ★10+ | yes | yes | — | — | Rerank BM25's top 30 search results, with several Jev question shapes, against dedicated rerankers | ranking quality, accuracy, latency, cost | 1617 | `jev-latest` | 2026-09-16 | mixed | — |
| [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robot-control) | ★10+ | yes | yes | — | `one commit` | Pick up an apple and place it on a plate with a simulated xArm7, choosing intent, motion direction and gripper each cycle · [report](https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/docs/RESULTS.md) | task success, cost, latency | 1 | `typesafe/jev-1.13` | 2026-09-19 | inconclusive | — |
| [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-search-rerank-eval) | ★10+ | yes | yes | — | — | Rerank a skills catalogue's search results with one Score per candidate, graded with the judge's own bias measured | ranking quality, precision | 164 | `~typesafe/jev-latest` | 2026-09-18 | mixed | — |
| [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#pdf-race) | ★10+ | yes | yes | — | — | Classify arXiv papers and pick their titles from their PDFs, scored against arXiv's own metadata | accuracy, latency, cost | 12 | `jev-latest` | 2026-09-20 | — | — |
| [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=en#smartmoney-cub) | ★10+ | yes | — | — | — | Answer typed finance judgements over trading logs, filings, industry news and central-bank text in a frozen offline suite · [report](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/assets/benchmark/run.json) | accuracy, F1, calibration, latency | 240 | `jev-1.13.0` | 2026-09-20 | mixed | — |
| [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-benchmark) | ★10+ | yes | yes | — | — | Seven synthetic application workloads (ticket triage, routing, driving, guardrails, approvals, answer scoring, home control) with the same typed outputs · [report](https://github.com/iammrduncan/typesafe-ai-benchmark/blob/HEAD/docs/benchmarks/README.md) | accuracy, latency, cost, tokens | 480 | `jev-latest` | 2026-09-17 | mixed | — |
| [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) | ★10+ | yes | yes | — | — | Complete browser tasks on eight self-hosted web apps, Jev choosing each action while Mercury 2.5 writes arguments and answers · [report](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/results/2026-09-18-jev-mercury/PROVENANCE.md) | task success, cost, latency, tokens | 49 | `jev-1.13.0` | 2026-09-18 | — | — |
| [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) | — | yes | yes | — | `self-submitted` | Decide whether to block a guardrail check across six suites: content, prompt attacks, denied topics, profanity, PII and grounding | accuracy, recall, cost | 9975 | — | 2026-10-15 | — | — |
| [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmark) | — | yes | yes | — | — | Choose chess moves among legal candidates, and tell which game characters a spoken line addresses | accuracy, F1, precision, latency | — | `jev-1.13.0` | 2026-09-16 | mixed | — |
| [jev-code-review-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-code-review-benchmark) | — | yes | yes | — | — | Check whether small Python programs follow four supplied rules · [report](https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/docs/results/README.md) | accuracy, cost, latency, robustness | 360 | `jev-1.13.0` | 2026-09-17 | mixed | — |
| [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-korean-benchmark) | — | yes | yes | — | `no licence` | Answer the same test questions in Korean and in English, to see whether Korean text needs translating first | accuracy, calibration, robustness, latency, cost | 100 | `jev-latest` | 2026-09-17 | mixed | — |
| [jev-little-airways](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-little-airways) | — | yes | — | — | — | Make in-flight judgements for aircraft in a toy air-traffic simulation: divert, declare an emergency, give way, landing order | latency, cost | — | `jev-latest` | 2026-09-17 | — | — |
| [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) | — | yes | yes | — | — | Check whether Jev's probabilities stay calibrated on a rule-based ticket task it cannot have seen, beside three public benchmarks | accuracy, calibration | 4621 | `typesafe-ai/jev` | 2026-09-19 | mixed | — |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench-human-disagreement) | — | yes | no | yes | `AI-written` `self-submitted` | Whether Jev's stated confidence drops on natural language inference items where human annotators disagree · [report](https://doi.org/10.5281/zenodo.22971491) | calibration, ranking quality | 1500 | `jev-1.13.0` | 2026-09-26 | mixed | — |
| [Probing Jev's behaviour with repeated API calls](https://kydlikebtc.github.io/awesome-jev/?lang=en#ahastudio-til-jev-probing) | ★100+ | yes | — | — | `no licence` `unverified claims` | Probe how Jev is built from about 10,000 API calls, including reversing the order of options · [report](https://github.com/ahastudio/til/blob/HEAD/jev/architecture-unmasked.md) | robustness, latency, tokens | — | `jev-1.13.0` | 2026-09-17 | — | — |
| [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) | — | yes | yes | — | `self-submitted` | Route a support message to one of five team labels: billing, technical, account, sales or needs_clarification | accuracy, F1, calibration, latency, cost | 100 | `jev-1.13.0` | 2026-10-09 | — | — |

---

Generated by `scripts/build_benchmarks.py` from `catalog.json`; edit the catalogue, not this page.
