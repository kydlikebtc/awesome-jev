<!-- Written by scripts/build_benchmarks.py from catalog.json. Edit that, not this file. -->

# 基准测试索引

<sub>[awesome-jev](../README.zh-CN.md) · [English](benchmarks.md)</sub>

> 本页的中文说明由模型撰写（机翻），未经人工审校。任务、数据集和对比对象的名称按作者的叫法以英文记录，两种语言的页面上都原样显示。

所有带 `measurement` 的 `kind: benchmark` 行：作者本人测了什么，按作者的报告逐项索引。这些测量本仓库一项都没有做过或重跑过。**结论方向**是作者本人对 Jev 在该任务上的结论，属作者自述、未经本仓库复现；作者没有用文字说明结论的，这一栏留空。

共 **73** 条基准测试行；其中 **27** 条带测量字段。这些行里，**0** 条已由人对照报告核读（`measurement.read_on`），**0** 条只有模型读过（`measurement.model_read_on`）；其余 **27** 条由脚本或模型填写，还没有人或模型读回核对。复核队列列出了[未读的行](review-queue.md#measurement-unread)和[只有模型读过的行](review-queue.md#model-read)。这些字段最初如何填写：[docs/method.md](method.md)。字段规则：[CONTRIBUTING](../CONTRIBUTING.md#field-rules)。

## 按决策模式看结论方向

每个决策模式下的基准测试行数，按作者自述的结论方向分列。归入多个模式的行在每个模式下各计一次。

| 模式 | 有利 (作者自述，未经本仓库复现) | 好坏参半 (作者自述，未经本仓库复现) | 不利 (作者自述，未经本仓库复现) | 无定论 (作者自述，未经本仓库复现) | 作者未说明 | 尚无测量字段 |
| --- | --- | --- | --- | --- | --- | --- |
| 工具选择 | · | 1 | · | 1 | 1 | 8 |
| 意图路由 | · | 1 | · | · | · | 1 |
| 上下文压缩 | · | · | 1 | · | · | 1 |
| 安全闸门 | · | 2 | · | · | 2 | 6 |
| 输出校验 | 1 | 2 | · | · | · | 8 |
| 人工升级 | · | 4 | · | · | 2 | 4 |
| 并行扇出 | · | · | · | · | · | 1 |
| 检索与排序 | 1 | 3 | 1 | · | · | 1 |
| 结构化抽取 | · | · | · | · | · | 1 |
| 分类 | · | 1 | 1 | · | 2 | 7 |
| 文档分拣 | · | 1 | · | · | 1 | · |
| 工单分拣 | · | · | · | · | 1 | · |
| 内容评分 | · | 2 | 1 | · | · | 6 |
| 总览 | · | 3 | · | · | 2 | 19 |

## 按对比对象

作者拿 Jev 与什么对比（按作者的叫法），以及做了这种对比的行。

| 对比对象 | 行 |
| --- | --- |
| Laya | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench), [jev-capability-atlas](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-capability-atlas), [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| Clef | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails), [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decisionmodelhub-support-routing) |
| Amazon Bedrock Guardrails | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| ash keyword ranker | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-search-rerank-eval) |
| BART-MNLI | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench-human-disagreement) |
| base order without a reranker | [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hippo-memory) |
| bge-m3 | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-search-rerank-eval) |
| bge-reranker-v2-m3 | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| BM25 | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-search-rerank-eval) |
| Claude Fable 5.1 | [jev-code-review-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-code-review-benchmark) |
| Claude Haiku 4.5 | [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-phishing-bench) |
| Claude Opus 5 | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) |
| Clef Flash | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decisionmodelhub-support-routing) |
| Cohere Rerank 3.5 | [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rag-benchmark) |
| Cohere Rerank 4 Fast | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| Cohere Rerank 4 Pro | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| decider-4b v2 | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) |
| Decisions API | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decisionmodelhub-support-routing) |
| DeepSeek Flash | [jev-arena](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-arena) |
| DeepSeek V4.1 Flash | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| DeepSeek V4.1 Flash labeller | [worldmonitor: news threat classification](https://kydlikebtc.github.io/awesome-jev/?lang=zh#worldmonitor-shadow-mode) |
| deterministic rule baseline | [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=zh#smartmoney-cub) |
| djev | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) |
| fuzzy name-matching heuristic | [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmark) |
| Gemini 3.6 Flash | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) |
| Gemini 3.8 Flash | [jev-code-review-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-code-review-benchmark) |
| Gemini 3.8 Flash on the parsed text | [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=zh#pdf-race) |
| Gemini 3.8 Flash reading the PDF | [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=zh#pdf-race) |
| GLiNER2 | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) |
| GLiNER2.5 (fastino/gliner2.5-multi-v1) | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmarks) |
| GPT-4.1 mini | [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-robot-control) |
| GPT-5.6 Luna | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) |
| GPT-5.6 Luna, reasoning effort none | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-korean-benchmark) |
| GPT-5.6 SOL | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) |
| GPT-6 Astra | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) |
| GPT-6 Astra, low reasoning | [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-robot-control) |
| GPT-6 Luna | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decisionmodelhub-support-routing) |
| Hermes summary compaction with session_search recovery | [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hermes-agent-jev-evaluation) |
| Hermes summary compaction, closed-book | [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hermes-agent-jev-evaluation) |
| hybrid order without a reranker | [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rag-benchmark) |
| Imajev-4B | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) |
| JevK5 v0.2.0 | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) |
| Kev | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| Laya 421M | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| local cross-encoder reranker | [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hippo-memory) |
| Needle 3, local | [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#typesafe-ai-benchmark) |
| Open-Jev | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| Open-Jev 9B | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| OpenAI Decisions API | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| Perplexity Decisions API | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| Plumb-4B | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) |
| Qwen 3.8 27B on Cerebras, structured output | [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#typesafe-ai-benchmark) |
| Qwen3-Reranker-4B | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| random mover | [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmark) |
| recency-ranked tool retention at the same budget | [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hermes-agent-jev-evaluation) |
| regex rule on link hosts | [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-phishing-bench) |
| Sonnet 5 | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) |
| Stockfish | [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmark) |
| Strands Deciders | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| text-embedding-3-small | [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-search-rerank-eval) |
| the same review without the pre-brief | [no-mistakes: Jev review pre-brief, measured and retired](https://kydlikebtc.github.io/awesome-jev/?lang=zh#no-mistakes-review-context) |
| ZeroEntropy zerank-2 | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |

## 按数据集

测量用到的有名称的数据集和基准套件，按作者的叫法。

| 数据集 | 行 |
| --- | --- |
| AG News | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmarks) |
| Banking77 | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmarks) |
| Belebele | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-korean-benchmark) |
| BRIGHT | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| BTZSC | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmarks) |
| ChaosNLI | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench-human-disagreement) |
| CodeSearchNet | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| CommonsenseQA | [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-ood-calibration) |
| DAIR Emotion | [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmarks) |
| finance-jev-v1 | [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=zh#smartmoney-cub) |
| FiQA-2018 | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| HellaSwag | [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-ood-calibration) |
| JevBench | [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) |
| KorMedMCQA | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-korean-benchmark) |
| LongMemEval | [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hippo-memory) |
| MedQA | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-korean-benchmark) |
| MIRACL | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| Natural Questions | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| NevIR | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| NFCorpus | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| OpenBookQA | [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-ood-calibration) |
| PAWS-X | [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-korean-benchmark) |
| PhishNChips v5.2 | [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-phishing-bench) |
| raxITLabs/decision-models-as-guardrails | [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) |
| SciFact | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| Support routing v1 | [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decisionmodelhub-support-routing) |
| TREC-COVID | [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) |
| WindTunnel | [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) |
| XQuAD-TR | [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rag-benchmark) |

## 全部带测量的报告

按 star 区间、再按标题排序。**独立**：除非该行带 vendor-reported 标记，否则为「是」。**原始数据**：作者公开逐条结果或原始响应为「是」，作者说明只公开汇总为「否」，两者都无法确认为「—」。**预注册**：作者说明方案或数据集在运行前已固定为「是」。**测量日期**取测量的 `as_of`，没有则取该行的发布日期。**核读**是人对照报告核读字段的日期；标 *（模型）* 的日期是模型的阅读，尚无人核对。

| 行 | 星标 | 独立 | 原始数据 | 预注册 | 警示 | 任务 | 指标 | n | 模型字符串 | 测量日期 | 结论方向（作者自述，未经本仓库复现） | 核读 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hermes-agent-jev-evaluation) | ★100k+ | 是 | — | — | — | Compact long agent transcripts with a port of fast-jev-compaction and score recall on a fixed question exam · [报告](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/results/SCORECARD-2026-09-19-jev.md) | 召回率, token 用量, 成本, 延迟 | 45 | `~typesafe/jev-latest` | 2026-09-19 | 不利 | — |
| [worldmonitor: news threat classification](https://kydlikebtc.github.io/awesome-jev/?lang=zh#worldmonitor-shadow-mode) | ★10k+ | 是 | — | — | `仅影子运行` | Label news headlines' threat level, scored on alerts against a blind human judgement · [报告](https://github.com/koala73/worldmonitor/pull/8326) | 召回率, 精确率 | 413 | `jev-1.13.0` | 2026-09-19 | 不利 | — |
| [no-mistakes: Jev review pre-brief, measured and retired](https://kydlikebtc.github.io/awesome-jev/?lang=zh#no-mistakes-review-context) | ★1k+ | 是 | 是 | — | — | Pre-brief a code review with a Jev-ranked list of candidate files, one Score per file · [报告](https://github.com/kunchenguid/no-mistakes/blob/HEAD/benchmarks/issue-1055/results.md) | token 用量, 延迟, 召回率, 精确率 | — | `jev-1.13.0` | 2026-09-19 | 不利 | — |
| [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=zh#hippo-memory) | ★100+ | 是 | — | — | — | Rerank memory-recall candidates with one Noul per candidate, scored on ranking and on graded answers · [报告](https://github.com/kitfunso/hippo-memory/blob/HEAD/docs/evals/2026-09-19-jev-reranker.md) | 排序质量, 召回率, 准确率, 延迟, 成本 | 300 | `jev-1.13.0` | 2026-09-19 | 好坏参半 | — |
| [jev-arena](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-arena) | ★100+ | 是 | 是 | — | — | Label comments for relevance, sentiment and intent, scored against an independent AI reference labelling · [报告](https://github.com/NanmiCoder/jev-arena/blob/HEAD/audit/accuracy-0919-124001/report.md) | 准确率, F1, 延迟, 成本 | 10000 | `typesafe/jev-1.13` | 2026-09-19 | — | — |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench) | ★100+ | 是 | — | — | — | Rank decision models on bounded-rubric decisions by accuracy above chance, calibration, speed and cost | 准确率, 校准, 延迟, 成本 | — | `jev-1.13.0` | 2026-09-19 | — | — |
| [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmarks) | ★10+ | 是 | 否 | 是 | — | Zero-shot single-label text classification with per-label probabilities, scored on accuracy, calibration and coverage at a fixed error budget · [报告](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/results/reports/btzsc-pilot-v1.md) | 准确率, F1, 校准, 延迟, token 用量 | 300 | `jev-1.13.0` | 2026-09-17 | 好坏参半 | — |
| [jev-capability-atlas](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-capability-atlas) | ★10+ | 是 | 是 | — | — | Map where Jev's calibrated decisions hold and where they break, across small suites of its own and third-party reports | 准确率, 校准, 延迟 | — | `jev-latest` | 2026-09-18 | 好坏参半 | — |
| [jev-dspy-lab](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-dspy-lab) | ★10+ | 是 | 是 | — | — | Confidence-gated support-ticket routing in a DSPy-style pipeline, on synthetic cases · [报告](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/evidence/live/jev-latest/benchmark.md) | 准确率, 校准, 延迟, 成本, token 用量 | 24 | `jev-latest` | 2026-09-17 | — | — |
| [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-phishing-bench) | ★10+ | 是 | 否 | — | — | Decide whether an email agent should click the link in an email · [报告](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/results/report.md) | 准确率, 召回率, 校准, 稳健性, 延迟, 成本 | 2000 | `jev-1.13.0` | 2026-09-17 | 好坏参半 | — |
| [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rag-benchmark) | ★10+ | 是 | 是 | — | — | Rerank hybrid-retrieval candidates for a small RAG system with batched Nouls, then answer from the top five | 召回率, 排序质量, F1, 延迟, 成本 | 1044 | `typesafe/jev-1.13` | 2026-09-20 | 有利 | — |
| [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-rerank-bench) | ★10+ | 是 | 是 | — | — | Rerank BM25's top 30 search results, with several Jev question shapes, against dedicated rerankers | 排序质量, 准确率, 延迟, 成本 | 1617 | `jev-latest` | 2026-09-16 | 好坏参半 | — |
| [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-robot-control) | ★10+ | 是 | 是 | — | `仅一次提交` | Pick up an apple and place it on a plate with a simulated xArm7, choosing intent, motion direction and gripper each cycle · [报告](https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/docs/RESULTS.md) | 任务成功率, 成本, 延迟 | 1 | `typesafe/jev-1.13` | 2026-09-19 | 无定论 | — |
| [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-search-rerank-eval) | ★10+ | 是 | 是 | — | — | Rerank a skills catalogue's search results with one Score per candidate, graded with the judge's own bias measured | 排序质量, 精确率 | 164 | `~typesafe/jev-latest` | 2026-09-18 | 好坏参半 | — |
| [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=zh#pdf-race) | ★10+ | 是 | 是 | — | — | Classify arXiv papers and pick their titles from their PDFs, scored against arXiv's own metadata | 准确率, 延迟, 成本 | 12 | `jev-latest` | 2026-09-20 | — | — |
| [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=zh#smartmoney-cub) | ★10+ | 是 | — | — | — | Answer typed finance judgements over trading logs, filings, industry news and central-bank text in a frozen offline suite · [报告](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/assets/benchmark/run.json) | 准确率, F1, 校准, 延迟 | 240 | `jev-1.13.0` | 2026-09-20 | 好坏参半 | — |
| [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#typesafe-ai-benchmark) | ★10+ | 是 | 是 | — | — | Seven synthetic application workloads (ticket triage, routing, driving, guardrails, approvals, answer scoring, home control) with the same typed outputs · [报告](https://github.com/iammrduncan/typesafe-ai-benchmark/blob/HEAD/docs/benchmarks/README.md) | 准确率, 延迟, 成本, token 用量 | 480 | `jev-latest` | 2026-09-17 | 好坏参半 | — |
| [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=zh#windtunnel) | ★10+ | 是 | 是 | — | — | Complete browser tasks on eight self-hosted web apps, Jev choosing each action while Mercury 2.5 writes arguments and answers · [报告](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/results/2026-09-18-jev-mercury/PROVENANCE.md) | 任务成功率, 成本, 延迟, token 用量 | 49 | `jev-1.13.0` | 2026-09-18 | — | — |
| [Decision Models as Guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decision-models-as-guardrails) | — | 是 | 是 | — | `作者自荐` | Decide whether to block a guardrail check across six suites: content, prompt attacks, denied topics, profanity, PII and grounding | 准确率, 召回率, 成本 | 9975 | — | 2026-10-15 | — | — |
| [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-benchmark) | — | 是 | 是 | — | — | Choose chess moves among legal candidates, and tell which game characters a spoken line addresses | 准确率, F1, 精确率, 延迟 | — | `jev-1.13.0` | 2026-09-16 | 好坏参半 | — |
| [jev-code-review-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-code-review-benchmark) | — | 是 | 是 | — | — | Check whether small Python programs follow four supplied rules · [报告](https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/docs/results/README.md) | 准确率, 成本, 延迟, 稳健性 | 360 | `jev-1.13.0` | 2026-09-17 | 好坏参半 | — |
| [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-korean-benchmark) | — | 是 | 是 | — | `无许可证` | Answer the same test questions in Korean and in English, to see whether Korean text needs translating first | 准确率, 校准, 稳健性, 延迟, 成本 | 100 | `jev-latest` | 2026-09-17 | 好坏参半 | — |
| [jev-little-airways](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-little-airways) | — | 是 | — | — | — | Make in-flight judgements for aircraft in a toy air-traffic simulation: divert, declare an emergency, give way, landing order | 延迟, 成本 | — | `jev-latest` | 2026-09-17 | — | — |
| [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jev-ood-calibration) | — | 是 | 是 | — | — | Check whether Jev's probabilities stay calibrated on a rule-based ticket task it cannot have seen, beside three public benchmarks | 准确率, 校准 | 4621 | `typesafe-ai/jev` | 2026-09-19 | 好坏参半 | — |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=zh#jevbench-human-disagreement) | — | 是 | 否 | 是 | `疑似 AI 生成` `作者自荐` | Whether Jev's stated confidence drops on natural language inference items where human annotators disagree · [报告](https://doi.org/10.5281/zenodo.22971491) | 校准, 排序质量 | 1500 | `jev-1.13.0` | 2026-09-26 | 好坏参半 | — |
| [Probing Jev's behaviour with repeated API calls](https://kydlikebtc.github.io/awesome-jev/?lang=zh#ahastudio-til-jev-probing) | ★100+ | 是 | — | — | `无许可证` `宣称未核实` | Probe how Jev is built from about 10,000 API calls, including reversing the order of options · [报告](https://github.com/ahastudio/til/blob/HEAD/jev/architecture-unmasked.md) | 稳健性, 延迟, token 用量 | — | `jev-1.13.0` | 2026-09-17 | — | — |
| [Support-routing benchmark: 100 held-out cases](https://kydlikebtc.github.io/awesome-jev/?lang=zh#decisionmodelhub-support-routing) | — | 是 | 是 | — | `作者自荐` | Route a support message to one of five team labels: billing, technical, account, sales or needs_clarification | 准确率, F1, 校准, 延迟, 成本 | 100 | `jev-1.13.0` | 2026-10-09 | — | — |

---

由 `scripts/build_benchmarks.py` 根据 `catalog.json` 生成；请修改目录数据，不要改本页。
