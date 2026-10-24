<!-- Written by scripts/build_review_queue.py from catalog.json. Edit those, not this file. -->

# Review queue · 复核队列

<sub>The Chinese on this page is model-written and has not been reviewed by a person. · 本页中文由模型撰写（机翻），未经人工审校。</sub>

Rows a script has singled out for a person to read. Each entry is a machine signal (a path, a string or a combination of fields matched a rule), not a finding about the row, and nothing on this page is written into `catalog.json`. Whoever reads a row records the decision in it, as each section says, and the row leaves this page when it is next regenerated. [status.md](status.md) publishes the counts.

脚本挑出、需要人来读的行。每一项都是机器信号（某个路径、字符串或字段组合命中了规则），不是对该行的结论，本页内容也不会写回 `catalog.json`。读过某一行的人按各节所说把判断记进该行，下次重新生成时它就会离开本页。数量见 [status.md](status.md)。

| Signal · 信号 | Rows · 行数 |
| --- | --- |
| [Rows the README shows, still lacking a person's summary, Chinese or reading · README 展示、仍缺人写摘要、人写中文或人读所引文件的行](#front-page) | 61 |
| [Evidence read from an examples directory · 证据取自 examples 目录](#examples-dir) | 22 |
| [Evidence resting on one model name or the API host · 证据只靠一个模型名或 API 主机](#single-model-name) | 76 |
| [Tool selection resting on words the keyword rules no longer count · 工具选择只靠关键词规则已不再计入的词](#tool-selection-broad-words) | 63 |
| [Overview rows with code, not yet indexed by pattern · 带代码、尚未按模式索引的 overview 行](#unsorted-overview) | 251 |
| [Rows with code whose summary names nothing about Jev · 带代码、摘要没有提到 Jev 的行](#generic-summary) | 73 |
| [Benchmark measurements nobody has read against the report · 人和模型都还没有对照报告读过的基准测试测量](#measurement-unread) | 27 |
| [Interfaces of alternatives nobody has read in the cited files · 人和模型都还没有在所引文件中读过的替代实现接口](#wire-unread) | 14 |
| [Thresholds nobody has read in the cited file · 人和模型都还没有在所引文件中读过的阈值](#thresholds-unread) | 31 |
| [Read or written by a model, not yet checked by a person · 模型读过或撰写、尚无人核对](#model-read) | 148 |

<a id="front-page"></a>

## Rows the README shows, still lacking a person's summary, Chinese or reading · README 展示、仍缺人写摘要、人写中文或人读所引文件的行

Most readers see only the README, and of the catalogue only the rows it prints by name: the *Start here* list, the first 10 reports under *Measured, not claimed* and the first 10 rows of each decision pattern, 134 rows in all. A row is listed here, in the order the README first prints it, while it lacks any of three things a person gives it: a summary written for this catalogue, Chinese a person wrote, and a person's reading of the file it cites. A summary lacks it when `summary_source` says it is the project's own GitHub description or a model's that no person has checked, or when any other summary names nothing about Jev (the [`generic-summary`](#generic-summary) rule); the Chinese, while `zh_machine` is set; the cited file, while `evidence` records no `read_on`. Each is a fact about who wrote or read the text, not a verdict on it: a project's own description can be clear and a machine translation right. Whether a row is filed under the right pattern is for the pattern sections below. The README orders each pattern's rows by star band, so the weekly refresh can move a row on or off this list when it crosses a band floor.

大多数读者只看 README，而目录里他们看得到的只有 README 点名列出的行：“从这里开始”列表、“实测，而非宣称”下的前 10 份报告，以及每个决策模式的前 10 行，共 134 行。这里按 README 首次列出的顺序，列出其中仍缺以下任何一项的行，三项都要由人来补：为本目录撰写的摘要、人写的中文、人对所引文件的阅读。`summary_source` 表明摘要是项目自己的 GitHub 描述，或是尚无人核对的模型撰写时，摘要算缺；其他摘要没有提到 Jev 的（[`generic-summary`](#generic-summary) 规则），也算缺。设置了 `zh_machine` 的中文算缺；`evidence` 没有 `read_on` 的，所引文件算缺。每一项说的都是谁写了、谁读了这些文字，不是对文字的评判：项目自己的描述可能很清楚，机翻也可能是对的。某行是否归在正确的模式下，由下面的模式各节负责。README 按星标档位排列每个模式的行，所以每周刷新让某行跨过档位下限时，它可能进入或离开这个列表。

To take a row off, give it what it lacks. Write a summary that says what the project asks Jev to decide and set `summary_source` to `curated` (see the `summary` field rules in [CONTRIBUTING](../CONTRIBUTING.md#field-rules)); a model's summary takes `curated` once you have checked or rewritten it. Write the Chinese yourself and delete `zh_machine` ([Claim a translation](../CONTRIBUTING.md#claim-a-translation): a model's draft keeps the flag, however carefully you corrected it). Read the cited file, check `question_types` against it and set `evidence.read_on`. A model can draft any of these, recorded as a model's work (`model-written`, `zh_machine`, `evidence.model_read_on`), and the row stays here until a person has checked it.

移出方法：补上它缺的。写一条说明该项目让 Jev 决定什么的摘要，并把 `summary_source` 设为 `curated`（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `summary` 的字段规则）；模型写的摘要，经你核对或改写后再设为 `curated`。中文由你亲自撰写，并删去 `zh_machine`（见[认领翻译](../CONTRIBUTING.md#claim-a-translation)：模型起草的译文无论你改得多仔细，都保留这个标记）。读所引文件，对照它核对 `question_types`，再设置 `evidence.read_on`。模型可以起草其中任何一项，但要记为模型的工作（`model-written`、`zh_machine`、`evidence.model_read_on`），该行会留在这里，直到有人核对。

| Row · 行 | Where the README prints it · README 中的位置 | Summary · 摘要 | Chinese · 中文 | Cited file · 引用的文件 |
| --- | --- | --- | --- | --- |
| [typesafe-jaggedness](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-jaggedness) | [Start here](../README.md#start-here) 2 · [Overview](../README.md#overview) 9 | — | `zh_machine` | — |
| [jev-skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-router) | [Measured, not claimed](../README.md#measured-not-claimed) 5 | `model-written` | `zh_machine` | — |
| [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=en#hippo-memory) | [Measured, not claimed](../README.md#measured-not-claimed) 8 | — | `zh_machine` | — |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) | [Measured, not claimed](../README.md#measured-not-claimed) 10 | `model-written` | `zh_machine` | — |
| [ai-hedge-fund](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai-hedge-fund) | [Tool selection](../README.md#tool-selection) 4 | `model-written` | `zh_machine` | — |
| [shapeshift](https://kydlikebtc.github.io/awesome-jev/?lang=en#shapeshift) | [Intent routing](../README.md#intent-routing) 10 | `model-written` | `zh_machine` | — |
| [compact-adviser](https://kydlikebtc.github.io/awesome-jev/?lang=en#compact-adviser) | [Context compaction](../README.md#context-compaction) 5 | `model-written` | `zh_machine` | — |
| [mu](https://kydlikebtc.github.io/awesome-jev/?lang=en#mu) | [Context compaction](../README.md#context-compaction) 7 | — | `zh_machine` | unread |
| [claude-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#claude-jev) | [Context compaction](../README.md#context-compaction) 9 | `model-written` | `zh_machine` | — |
| [dsh-jev-tools](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-tools) | [Context compaction](../README.md#context-compaction) 10 | `model-written` | `zh_machine` | — |
| [langchainjs-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#langchainjs-typesafe) | [Safety gating](../README.md#safety-gating) 3 · [Model routing](../README.md#model-routing) 3 | [`generic-summary`](#generic-summary) | — | — |
| [atomic](https://kydlikebtc.github.io/awesome-jev/?lang=en#atomic) | [Safety gating](../README.md#safety-gating) 8 · [Output validation](../README.md#output-validation) 6 | `model-written` | `zh_machine` | — |
| [grok-bot-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#grok-bot-jev) | [Safety gating](../README.md#safety-gating) 9 | `model-written` | `zh_machine` | — |
| [latitude-llm](https://kydlikebtc.github.io/awesome-jev/?lang=en#latitude-llm) | [Output validation](../README.md#output-validation) 3 | `model-written` | `zh_machine` | — |
| [reticle](https://kydlikebtc.github.io/awesome-jev/?lang=en#reticle) | [Output validation](../README.md#output-validation) 4 | `model-written` | `zh_machine` | — |
| [abide](https://kydlikebtc.github.io/awesome-jev/?lang=en#abide) | [Output validation](../README.md#output-validation) 5 | `model-written` | `zh_machine` | — |
| [fastbrowse](https://kydlikebtc.github.io/awesome-jev/?lang=en#fastbrowse) | [Output validation](../README.md#output-validation) 8 | `model-written` | `zh_machine` | — |
| [formanator](https://kydlikebtc.github.io/awesome-jev/?lang=en#formanator) | [Output validation](../README.md#output-validation) 9 · [Document triage](../README.md#document-triage) 2 | `model-written` | `zh_machine` | — |
| [jev-harness-ismaelsoilet](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness-ismaelsoilet) | [Retry control](../README.md#retry-control) 1 | `model-written` | `zh_machine` | — |
| [duomind](https://kydlikebtc.github.io/awesome-jev/?lang=en#duomind) | [Retry control](../README.md#retry-control) 2 | `model-written` | `zh_machine` | [`model_read_on`](#model-read) 2026-10-24 |
| [harnessjudge](https://kydlikebtc.github.io/awesome-jev/?lang=en#harnessjudge) | [Retry control](../README.md#retry-control) 3 | `model-written` | `zh_machine` | — |
| [jev-reasoning-navigator](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-reasoning-navigator) | [Retry control](../README.md#retry-control) 5 | — | `zh_machine` | — |
| [jev-resilience](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-resilience) | [Retry control](../README.md#retry-control) 6 | `model-written` | `zh_machine` | — |
| [jevswiftsdk](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevswiftsdk) | [Retry control](../README.md#retry-control) 7 | `model-written` | `zh_machine` | — |
| [xavierjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#xavierjev) | [Retry control](../README.md#retry-control) 8 | — | `zh_machine` | — |
| [typesafe-confidence](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-confidence) | [Human escalation](../README.md#human-escalation) 7 | — | `zh_machine` | — |
| [astra-ares](https://kydlikebtc.github.io/awesome-jev/?lang=en#astra-ares) | [Model routing](../README.md#model-routing) 6 | `model-written` | `zh_machine` | — |
| [jevrouter](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevrouter) | [Model routing](../README.md#model-routing) 10 | [`generic-summary`](#generic-summary) | — | — |
| [jev-forge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-forge) | [Speculative fan-out](../README.md#speculative-fan-out) 9 · [Content scoring](../README.md#content-scoring) 10 | `model-written` | `zh_machine` | — |
| [videojev](https://kydlikebtc.github.io/awesome-jev/?lang=en#videojev) | [Speculative fan-out](../README.md#speculative-fan-out) 10 | — | `zh_machine` | — |
| [jev-macos-loop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-macos-loop) | [Structured extraction](../README.md#structured-extraction) 5 | `model-written` | `zh_machine` | — |
| [jev-reviewer](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-reviewer) | [Structured extraction](../README.md#structured-extraction) 6 | — | `zh_machine` | — |
| [jevfill](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevfill) | [Structured extraction](../README.md#structured-extraction) 7 | — | `zh_machine` | — |
| [jev-span](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-span) | [Structured extraction](../README.md#structured-extraction) 8 | — | `zh_machine` | — |
| [smart-paste](https://kydlikebtc.github.io/awesome-jev/?lang=en#smart-paste) | [Structured extraction](../README.md#structured-extraction) 9 | — | `zh_machine` | — |
| [ask-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#ask-jev) | [Structured extraction](../README.md#structured-extraction) 10 | `model-written` | `zh_machine` | — |
| [332-lab-jev-chat](https://kydlikebtc.github.io/awesome-jev/?lang=en#332-lab-jev-chat) | [Classification](../README.md#classification) 9 | — | `zh_machine` | — |
| [nimble](https://kydlikebtc.github.io/awesome-jev/?lang=en#nimble) | [ML feature extraction](../README.md#ml-feature-extraction) 2 | `model-written` | `zh_machine` | — |
| [jev-sees](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-sees) | [ML feature extraction](../README.md#ml-feature-extraction) 5 | `model-written` | `zh_machine` | [`model_read_on`](#model-read) 2026-10-24 |
| [jev-board-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-board-lab) | [ML feature extraction](../README.md#ml-feature-extraction) 6 | `model-written` | `zh_machine` | — |
| [jev-calibrated-narrative-coding](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-calibrated-narrative-coding) | [ML feature extraction](../README.md#ml-feature-extraction) 7 | `model-written` | `zh_machine` | — |
| [tiershift](https://kydlikebtc.github.io/awesome-jev/?lang=en#tiershift) | [ML feature extraction](../README.md#ml-feature-extraction) 8 | `model-written` | `zh_machine` | — |
| [docjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#docjev) | [Document triage](../README.md#document-triage) 1 | `model-written` | `zh_machine` | — |
| [tax-doc-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#tax-doc-classifier) | [Document triage](../README.md#document-triage) 3 | `model-written` | `zh_machine` | — |
| [doc-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#doc-router) | [Document triage](../README.md#document-triage) 4 | `model-written` | `zh_machine` | — |
| [jev-capability-atlas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-capability-atlas) | [Document triage](../README.md#document-triage) 5 | `model-written` | `zh_machine` | — |
| [jevmory](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmory) | [Document triage](../README.md#document-triage) 6 | `model-written` | `zh_machine` | — |
| [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#pdf-race) | [Document triage](../README.md#document-triage) 7 | `model-written` | `zh_machine` | — |
| [decision-first](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-first) | [Document triage](../README.md#document-triage) 8 | `model-written` | `zh_machine` | — |
| [jev-playwright](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-playwright) | [Document triage](../README.md#document-triage) 9 | `model-written` | `zh_machine` | [`model_read_on`](#model-read) 2026-10-24 |
| [jev-boe-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-boe-demo) | [Document triage](../README.md#document-triage) 10 | `model-written` | `zh_machine` | — |
| [jev-triage-boldbug1](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-triage-boldbug1) | [Support triage](../README.md#support-triage) 8 | `model-written` | `zh_machine` | — |
| [decisionmodelhub-support-routing](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) | [Support triage](../README.md#support-triage) 9 | — | `zh_machine` | — |
| [gptcache](https://kydlikebtc.github.io/awesome-jev/?lang=en#gptcache) | [Content scoring](../README.md#content-scoring) 6 | `model-written` | `zh_machine` | — |
| [jev-as-a-judge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-as-a-judge) | [Content scoring](../README.md#content-scoring) 9 | `model-written` | `zh_machine` | — |
| [1-million-emojis](https://kydlikebtc.github.io/awesome-jev/?lang=en#1-million-emojis) | [Recommendation](../README.md#recommendation) 1 | `model-written` | `zh_machine` | [`model_read_on`](#model-read) 2026-10-24 |
| [jevflix](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevflix) | [Recommendation](../README.md#recommendation) 2 | `model-written` | `zh_machine` | — |
| [system-one-adapter-python](https://kydlikebtc.github.io/awesome-jev/?lang=en#system-one-adapter-python) | [Overview](../README.md#overview) 3 | — | — | unread |
| [typesafe-api-reference](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-api-reference) | [Overview](../README.md#overview) 5 | — | `zh_machine` | — |
| [typesafe-models](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-models) | [Overview](../README.md#overview) 6 | — | `zh_machine` | — |
| [typesafe-primitives](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-primitives) | [Overview](../README.md#overview) 7 | — | `zh_machine` | — |

<a id="examples-dir"></a>

## Evidence read from an examples directory · 证据取自 examples 目录

The cited file sits under an `examples/` or `example/` directory and the row does not record `evidence.kind`. An SDK's examples are often its clearest call site; a project's examples can also be all it has, and say little about how it uses Jev itself. The path cannot tell which.

引用的文件位于 `examples/` 或 `example/` 目录下，而该行没有记录 `evidence.kind`。SDK 的示例往往就是最清楚的调用点；但一个项目的示例也可能是它仅有的调用，说明不了它自己如何使用 Jev。单凭路径无法判断是哪一种。

To take a row off, read the file and set `evidence.kind`: `call-site` when it is the project's own use of Jev, `example-only` when it is only an example. Citing a better file from the project's own code instead also takes it off. A model that does either records its reading in `evidence.model_read_on`, never in `evidence.read_on`.

移出方法：读这个文件，然后设置 `evidence.kind`——它就是项目自身对 Jev 的使用时设为 `call-site`，只是示例时设为 `example-only`。改为引用项目自身代码中更合适的文件，也会让它移出。由模型来做时，把阅读记在 `evidence.model_read_on`，不要记在 `evidence.read_on`。

| Row · 行 | Kind · 类型 | Cited file · 引用的文件 | Matched · 匹配文本 |
| --- | --- | --- | --- |
| [agentgateway-guardrail](https://kydlikebtc.github.io/awesome-jev/?lang=en#agentgateway-guardrail) | `project` | [`examples/llm-guardrail-jev/guardrail.ts`](https://github.com/agentgateway/agentgateway/blob/HEAD/examples/llm-guardrail-jev/guardrail.ts) | `jev-latest` `choice` `score` |
| [ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai) | `sdk` | [`examples/ai-functions/src/evaluate/typesafe-ai/basic.ts`](https://github.com/vercel/ai/blob/HEAD/examples/ai-functions/src/evaluate/typesafe-ai/basic.ts) | `jev-latest` |
| [celesto](https://kydlikebtc.github.io/awesome-jev/?lang=en#celesto) | `project` | [`examples/pr-review-jev/models.py`](https://github.com/CelestoAI/celesto/blob/HEAD/examples/pr-review-jev/models.py) | `api.typesafe.ai` `jev-latest` `/v1/systemone` |
| [cua-jev-use](https://kydlikebtc.github.io/awesome-jev/?lang=en#cua-jev-use) | `project` | [`libs/cua-driver/examples/jev-use/python/jev_adapter.py`](https://github.com/trycua/cua/blob/HEAD/libs/cua-driver/examples/jev-use/python/jev_adapter.py) | `typesafe_sdk` `system_one` `choice` `Choice` |
| [decision-circuits](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-circuits) | `sdk` | [`examples/02_jev_backend.py`](https://github.com/Barneyjm/decision-circuits/blob/HEAD/examples/02_jev_backend.py) | `jev-latest` |
| [discern](https://kydlikebtc.github.io/awesome-jev/?lang=en#discern) | `project` | [`examples/headline.ts`](https://github.com/doeixd/discern/blob/HEAD/examples/headline.ts) | `jev-latest` `TypeSafeClient` |
| [dspy-typesafeify](https://kydlikebtc.github.io/awesome-jev/?lang=en#dspy-typesafeify) | `project` | [`examples/typesafe_dspy_ticket_triage/run_demo.py`](https://github.com/typesafeainate/dspy-typesafeify/blob/HEAD/examples/typesafe_dspy_ticket_triage/run_demo.py) | `typesafe_sdk` `system_one` `TypeSafeClient` |
| [example-confidence-gate](https://kydlikebtc.github.io/awesome-jev/?lang=en#example-confidence-gate) | `snippet` | [`examples/02-confidence-gate/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/02-confidence-gate/main.py) | `typesafe_sdk` `system_one` `Choice` |
| [example-fan-out](https://kydlikebtc.github.io/awesome-jev/?lang=en#example-fan-out) | `snippet` | [`examples/03-fan-out/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/03-fan-out/main.py) | `typesafe_sdk` `system_one` `Choice` `Noul` |
| [example-three-primitives](https://kydlikebtc.github.io/awesome-jev/?lang=en#example-three-primitives) | `snippet` | [`examples/01-three-primitives/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/01-three-primitives/main.py) | `typesafe_sdk` `system_one` `Choice` `Noul` |
| [example-tool-selection](https://kydlikebtc.github.io/awesome-jev/?lang=en#example-tool-selection) | `snippet` | [`examples/04-tool-selection/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/04-tool-selection/main.py) | `typesafe_sdk` `system_one` `Choice` `Noul` |
| [jev-cookbook](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cookbook) | `tutorial` | [`examples/01-customer-support-triage/triage.py`](https://github.com/paramjeetn/jev-cookbook/blob/HEAD/examples/01-customer-support-triage/triage.py) | `api.typesafe.ai` `typesafe/jev` `jev-latest` |
| [jev-harness-typesafeai](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness-typesafeai) | `project` | [`examples/host/jev-choice.ts`](https://github.com/TypeSafeAI/jev-harness/blob/HEAD/examples/host/jev-choice.ts) | `api.typesafe.ai` `/v1/systemone` |
| [jev-recipes](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-recipes) | `project` | [`examples/checkers/ai.mjs`](https://github.com/agencyenterprise/jev-recipes/blob/HEAD/examples/checkers/ai.mjs) | `@typesafe-ai/sdk` `TypeSafeClient` |
| [jev-skills-laguagu](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skills-laguagu) | `plugin` | [`examples/decisions/run.mjs`](https://github.com/laguagu/jev-skills/blob/HEAD/examples/decisions/run.mjs) | `api.typesafe.ai` `@typesafe-ai/sdk` `systemOne` |
| [jevlang-timmikeladze](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevlang-timmikeladze) | `sdk` | [`examples/entity-alignment.js`](https://github.com/TimMikeladze/JevLang/blob/HEAD/examples/entity-alignment.js) | `jev-1.13` |
| [metacog](https://kydlikebtc.github.io/awesome-jev/?lang=en#metacog) | `project` | [`examples/jev_best_of_n.py`](https://github.com/ItIsCuthNotCup/MetaCog/blob/HEAD/examples/jev_best_of_n.py) | `api.typesafe.ai` |
| [openrouter-jev-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#openrouter-jev-mcp) | `plugin` | [`examples/demo_typesafe_sdk.py`](https://github.com/ctmx/openrouter-jev-mcp/blob/HEAD/examples/demo_typesafe_sdk.py) | `typesafe_sdk` `system_one` `TypeSafeClient` |
| [public-browser](https://kydlikebtc.github.io/awesome-jev/?lang=en#public-browser) | `plugin` | [`examples/jev-loop.mjs`](https://github.com/Silbercue/public-browser/blob/HEAD/examples/jev-loop.mjs) | `typesafe-ai/jev` |
| [spring-ai-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#spring-ai-typesafe) | `integration` | [`examples/src/main/java/org/springaicommunity/typesafe/demo/JevQuickstart.java`](https://github.com/spring-ai-community/spring-ai-typesafe/blob/HEAD/examples/src/main/java/org/springaicommunity/typesafe/demo/JevQuickstart.java) | `systemOne` `TypeSafeClient` `Noul` `choice` |
| [typesafe-ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai) | `sdk` | [`examples/tsg/main.rs`](https://github.com/Twister915/typesafe-ai/blob/HEAD/examples/tsg/main.rs) | `api.typesafe.ai` `jev-latest` |
| [typesafeai-dotnet-sdk](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafeai-dotnet-sdk) | `sdk` | [`examples/TypeSafe.BureauOfBadIdeas/Program.cs`](https://github.com/saibimajdi/typesafeai-dotnet-sdk/blob/HEAD/examples/TypeSafe.BureauOfBadIdeas/Program.cs) | `TypeSafeClient` |

<a id="single-model-name"></a>

## Evidence resting on one model name or the API host · 证据只靠一个模型名或 API 主机

The only string in `evidence.matched` is one of `jev-latest`, `typesafe-ai/jev`, `typesafe/jev`, `api.typesafe.ai`, or a pinned model version (`jev-` and a version number). Any file that configures Jev contains one of them (a settings file, a pricing table, a model list) whether or not it calls the API, so the weekly text check can keep passing after the call itself is gone.

`evidence.matched` 里唯一的字符串是 `jev-latest`, `typesafe-ai/jev`, `typesafe/jev`, `api.typesafe.ai` 之一，或一个固定的模型版本号（`jev-` 加版本号）。任何配置 Jev 的文件都会包含它们（设置文件、价格表、模型列表），不论是否真的调用 API；所以即使调用本身已经删除，每周的文本检查也可能继续通过。

To take a row off, add a second string from the call itself (an import, the method called, a question type) to `evidence.matched`, then run `python3 scripts/verify_claims.py --only <slug>` to confirm the file holds every string. A model that does this records its reading in `evidence.model_read_on`, never in `evidence.read_on`.

移出方法：从调用本身再取一个字符串（import、被调用的方法、问题类型）加入 `evidence.matched`，然后运行 `python3 scripts/verify_claims.py --only <slug>`，确认文件含有每一个字符串。由模型来做时，把阅读记在 `evidence.model_read_on`，不要记在 `evidence.read_on`。

| Row · 行 | Kind · 类型 | Cited file · 引用的文件 | Matched · 匹配文本 |
| --- | --- | --- | --- |
| [a3m-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#a3m-router) | `project` | [`dist/routing/jev/remote.d.ts`](https://github.com/Das-rebel/a3m-router/blob/HEAD/dist/routing/jev/remote.d.ts) | `api.typesafe.ai` |
| [ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai) | `sdk` | [`examples/ai-functions/src/evaluate/typesafe-ai/basic.ts`](https://github.com/vercel/ai/blob/HEAD/examples/ai-functions/src/evaluate/typesafe-ai/basic.ts) | `jev-latest` |
| [bes-kelime-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#bes-kelime-jev) | `project` | [`src/jev.ts`](https://github.com/mahmut-gundogdu/bes-kelime-jev/blob/HEAD/src/jev.ts) | `typesafe-ai/jev` |
| [cua-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#cua-jev) | `project` | [`src/cua_jev/cost.py`](https://github.com/ZJU-REAL/CUA-JEV/blob/HEAD/src/cua_jev/cost.py) | `jev-1.13` |
| [decide-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#decide-mcp) | `sdk` | [`src/config.ts`](https://github.com/dakdevs/decide-mcp/blob/HEAD/src/config.ts) | `typesafe-ai/jev` |
| [decision-circuits](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-circuits) | `sdk` | [`examples/02_jev_backend.py`](https://github.com/Barneyjm/decision-circuits/blob/HEAD/examples/02_jev_backend.py) | `jev-latest` |
| [dinostomp](https://kydlikebtc.github.io/awesome-jev/?lang=en#dinostomp) | `project` | [`audits/xstest-refusal-guards/compare.py`](https://github.com/collapseindex/dinostomp/blob/HEAD/audits/xstest-refusal-guards/compare.py) | `jev-latest` |
| [dsh-jev-buberlo](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-buberlo) | `plugin` | [`packages/dsh-jev/src/config.ts`](https://github.com/buberlo/dsh-jev/blob/HEAD/packages/dsh-jev/src/config.ts) | `jev-latest` |
| [dsh-plugin-jev-effort-selector](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-plugin-jev-effort-selector) | `plugin` | [`lib/client.js`](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector/blob/HEAD/lib/client.js) | `jev-latest` |
| [eutrya](https://kydlikebtc.github.io/awesome-jev/?lang=en#eutrya) | `project` | [`bin/eutrya.mjs`](https://github.com/hellozenstrategist-lab/eutrya/blob/HEAD/bin/eutrya.mjs) | `typesafe-ai/jev` |
| [flue-jev-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#flue-jev-demo) | `project` | [`src/flue-jev.ts`](https://github.com/matthewp/flue-jev-demo/blob/HEAD/src/flue-jev.ts) | `typesafe/jev` |
| [go-system-one](https://kydlikebtc.github.io/awesome-jev/?lang=en#go-system-one) | `sdk` | [`docs/benchmarks/data/jevbench-public-20260923/protocol/aggregate.py`](https://github.com/rcarmo/go-system-one/blob/HEAD/docs/benchmarks/data/jevbench-public-20260923/protocol/aggregate.py) | `jev-1.13` |
| [instruct-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#instruct-jev) | `project` | [`DeckerGUI_JEV-CorpusDGUI/build_instruct_jev.py`](https://github.com/ctaxnagomi/instruct-jev/blob/HEAD/DeckerGUI_JEV-CorpusDGUI/build_instruct_jev.py) | `jev-latest` |
| [jev-ai-sdk-form-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ai-sdk-form-router) | `project` | [`components/routing-result.tsx`](https://github.com/vercel-labs/jev-ai-sdk-form-router/blob/HEAD/components/routing-result.tsx) | `typesafe-ai/jev` |
| [jev-align-caiovicentino](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-align-caiovicentino) | `project` | [`src/jev.mjs`](https://github.com/caiovicentino/jev-align/blob/HEAD/src/jev.mjs) | `typesafe-ai/jev` |
| [jev-autopilot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-autopilot) | `project` | [`server/pilot.ts`](https://github.com/arielweinberger/jev-autopilot/blob/HEAD/server/pilot.ts) | `jev-latest` |
| [jev-bot-bl888m](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-bot-bl888m) | `project` | [`jev_bot/jev.py`](https://github.com/bl888m/jev-bot/blob/HEAD/jev_bot/jev.py) | `api.typesafe.ai` |
| [jev-browser](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browser) | `project` | [`src/index.ts`](https://github.com/jkudish/jev-browser/blob/HEAD/src/index.ts) | `jev-latest` |
| [jev-browser-openqa-cn](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browser-openqa-cn) | `plugin` | [`src/jev.ts`](https://github.com/openqa-cn/jev-browser/blob/HEAD/src/jev.ts) | `jev-latest` |
| [jev-calculator](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-calculator) | `project` | [`shared/protocol.ts`](https://github.com/pc418/jev-calculator/blob/HEAD/shared/protocol.ts) | `jev-1.13` |
| [jev-carryforward](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-carryforward) | `plugin` | [`src/gateway.ts`](https://github.com/dharun-cohere/jev-carryforward/blob/HEAD/src/gateway.ts) | `typesafe-ai/jev` |
| [jev-code](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-code) | `plugin` | [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts) | `jev-latest` |
| [jev-compaction](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-compaction) | `project` | [`hermes-compact.mjs`](https://github.com/picaye/jev-compaction/blob/HEAD/hermes-compact.mjs) | `jev-latest` |
| [jev-dev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-dev) | `project` | [`scripts/probe-jev.ts`](https://github.com/n-yokomachi/jev-dev/blob/HEAD/scripts/probe-jev.ts) | `typesafe-ai/jev` |
| [jev-document-classification](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-document-classification) | `project` | [`server/classification-cache.ts`](https://github.com/Charlyhno-eng/jev-document-classification/blob/HEAD/server/classification-cache.ts) | `typesafe-ai/jev` |
| [jev-does-not-play-dice](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-does-not-play-dice) | `benchmark` | [`src/run.mjs`](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/HEAD/src/run.mjs) | `typesafe-ai/jev` |
| [jev-eval-shogo-nfrealmusic](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-eval-shogo-nfrealmusic) | `benchmark` | [`src/jev.ts`](https://github.com/Shogo-nfrealmusic/jev-eval/blob/HEAD/src/jev.ts) | `typesafe-ai/jev` |
| [jev-feels](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-feels) | `project` | [`lib/jev/client.rb`](https://github.com/Qew7/jev-feels/blob/HEAD/lib/jev/client.rb) | `jev-latest` |
| [jev-grug](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-grug) | `project` | [`lib/jev.ts`](https://github.com/mkotlikov/jev-grug/blob/HEAD/lib/jev.ts) | `jev-latest` |
| [jev-harness](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness) | `project` | [`demos/proof/row-filter/run.ts`](https://github.com/AntonioCoppe/jev-harness/blob/HEAD/demos/proof/row-filter/run.ts) | `jev-latest` |
| [jev-java-gudcks0305](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-java-gudcks0305) | `sdk` | [`jev-cloudflare/src/main/java/io/github/gudcks0305/jev/cloudflare/CloudflareJevClient.java`](https://github.com/gudcks0305/jev-java/blob/HEAD/jev-cloudflare/src/main/java/io/github/gudcks0305/jev/cloudflare/CloudflareJevClient.java) | `typesafe/jev` |
| [jev-jp-address](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-jp-address) | `sdk` | [`src/jev.ts`](https://github.com/smasato/jev-jp-address/blob/HEAD/src/jev.ts) | `jev-latest` |
| [jev-mail](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mail) | `plugin` | [`src/common/jev.js`](https://github.com/muhammedilyasy/jev-mail/blob/HEAD/src/common/jev.js) | `jev-1.13` |
| [jev-model-router-az9713](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-model-router-az9713) | `project` | [`probe.mjs`](https://github.com/az9713/jev-model-router/blob/HEAD/probe.mjs) | `typesafe-ai/jev` |
| [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) | `benchmark` | [`scripts/jev_eval.mjs`](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs) | `typesafe-ai/jev` |
| [jev-paint](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-paint) | `project` | [`web/jev.mjs`](https://github.com/achimala/jev-paint/blob/HEAD/web/jev.mjs) | `jev-latest` |
| [jev-playground-hegargarcia](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-playground-hegargarcia) | `benchmark` | [`src/app/api/connect-four/move/route.ts`](https://github.com/hegargarcia/jev-playground/blob/HEAD/src/app/api/connect-four/move/route.ts) | `typesafe-ai/jev` |
| [jev-pong](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-pong) | `project` | [`lib/compare/compare-models.ts`](https://github.com/ably-labs/jev-pong/blob/HEAD/lib/compare/compare-models.ts) | `typesafe-ai/jev` |
| [jev-report](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-report) | `project` | [`figs.py`](https://github.com/HackSing/jev-report/blob/HEAD/figs.py) | `jev-1.13` |
| [jev-tool-permissions](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tool-permissions) | `sdk` | [`src/types.ts`](https://github.com/NicolasMontone/jev-tool-permissions/blob/HEAD/src/types.ts) | `typesafe-ai/jev` |
| [jev-tool-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tool-router) | `plugin` | [`scripts/setup-codex.mjs`](https://github.com/jackbarunz/jev-tool-router/blob/HEAD/scripts/setup-codex.mjs) | `typesafe-ai/jev` |
| [jev-trader](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trader) | `project` | [`src/config.ts`](https://github.com/jarrodwatts/jev-trader/blob/HEAD/src/config.ts) | `jev-latest` |
| [jev-tree](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tree) | `project` | [`benchmarks/run.mjs`](https://github.com/reachjalil/jev-tree/blob/HEAD/benchmarks/run.mjs) | `typesafe-ai/jev` |
| [jevgate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgate) | `project` | [`src/auth/provider.rs`](https://github.com/Tech-Byte-Frontier/jevgate/blob/HEAD/src/auth/provider.rs) | `api.typesafe.ai` |
| [jevgraph](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgraph) | `project` | [`src/jevgraph/benchmark.py`](https://github.com/chenmingtang830/jevgraph/blob/HEAD/src/jevgraph/benchmark.py) | `typesafe-ai/jev` |
| [jevlang-timmikeladze](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevlang-timmikeladze) | `sdk` | [`examples/entity-alignment.js`](https://github.com/TimMikeladze/JevLang/blob/HEAD/examples/entity-alignment.js) | `jev-1.13` |
| [jevlogs](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevlogs) | `project` | [`benchmarks/pager/run-jev-v2.mjs`](https://github.com/reachjalil/jevlogs/blob/HEAD/benchmarks/pager/run-jev-v2.mjs) | `typesafe-ai/jev` |
| [jevloop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevloop) | `project` | [`bench/compare.ts`](https://github.com/zjunlp/JevLoop/blob/HEAD/bench/compare.ts) | `api.typesafe.ai` |
| [jevmory](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmory) | `project` | [`jevmory/cli.py`](https://github.com/romiluz13/jevmory/blob/HEAD/jevmory/cli.py) | `api.typesafe.ai` |
| [jevocks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevocks) | `project` | [`src/lib/classify.ts`](https://github.com/unicodeveloper/jevocks/blob/HEAD/src/lib/classify.ts) | `typesafe-ai/jev` |
| [jevtape](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevtape) | `project` | [`src/main/java/io/jevtape/cassette/RecordedRequest.java`](https://github.com/Hugo-DDT/JevTape/blob/HEAD/src/main/java/io/jevtape/cassette/RecordedRequest.java) | `jev-latest` |
| [json-render](https://kydlikebtc.github.io/awesome-jev/?lang=en#json-render) | `project` | [`apps/web/lib/jev/compose.ts`](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts) | `typesafe-ai/jev` |
| [kody](https://kydlikebtc.github.io/awesome-jev/?lang=en#kody) | `plugin` | [`packages/worker/src/mcp/tools/search-jev-rerank.ts`](https://github.com/kody-hq/kody/blob/HEAD/packages/worker/src/mcp/tools/search-jev-rerank.ts) | `typesafe/jev` |
| [metacog](https://kydlikebtc.github.io/awesome-jev/?lang=en#metacog) | `project` | [`examples/jev_best_of_n.py`](https://github.com/ItIsCuthNotCup/MetaCog/blob/HEAD/examples/jev_best_of_n.py) | `api.typesafe.ai` |
| [mobile-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#mobile-jev) | `project` | [`apps/jev-studio/app/components/use-studio.ts`](https://github.com/droidrun/mobile-jev/blob/HEAD/apps/jev-studio/app/components/use-studio.ts) | `jev-latest` |
| [oko](https://kydlikebtc.github.io/awesome-jev/?lang=en#oko) | `plugin` | [`scripts/benchmark-public/replay/replay.py`](https://github.com/bartlomein/oko/blob/HEAD/scripts/benchmark-public/replay/replay.py) | `jev-1.13` |
| [open-spark-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-spark-jev) | `project` | [`open_spark_jev/eval/speed_vs_generation.py`](https://github.com/abhishek085/open-spark-jev/blob/HEAD/open_spark_jev/eval/speed_vs_generation.py) | `jev-latest` |
| [openwork](https://kydlikebtc.github.io/awesome-jev/?lang=en#openwork) | `alternative` | [`.github/scripts/jev-test-coverage-review.mjs`](https://github.com/different-ai/openwork/blob/HEAD/.github/scripts/jev-test-coverage-review.mjs) | `typesafe-ai/jev` |
| [padflow-jev-evals](https://kydlikebtc.github.io/awesome-jev/?lang=en#padflow-jev-evals) | `benchmark` | [`scripts/run_baseline.py`](https://github.com/zsavage8/padflow-jev-evals/blob/HEAD/scripts/run_baseline.py) | `api.typesafe.ai` |
| [pagegrade](https://kydlikebtc.github.io/awesome-jev/?lang=en#pagegrade) | `project` | [`lib/jev.ts`](https://github.com/kitze/pagegrade/blob/HEAD/lib/jev.ts) | `typesafe-ai/jev` |
| [pg-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#pg-typesafe) | `plugin` | [`sql/typesafe.sql`](https://github.com/giuliosmall/pg_typesafe/blob/HEAD/sql/typesafe.sql) | `jev-latest` |
| [pi-jev-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-jev-router) | `project` | [`index.ts`](https://github.com/mejiasd3v/pi-jev-router/blob/HEAD/index.ts) | `typesafe-ai/jev` |
| [plugins](https://kydlikebtc.github.io/awesome-jev/?lang=en#plugins) | `plugin` | [`plugins/jev-browser/src/jev-model.ts`](https://github.com/cline/plugins/blob/HEAD/plugins/jev-browser/src/jev-model.ts) | `typesafe-ai/jev` |
| [profanity-checker](https://kydlikebtc.github.io/awesome-jev/?lang=en#profanity-checker) | `project` | [`src/endpoints/profanityCheck.ts`](https://github.com/4rays/profanity-checker/blob/HEAD/src/endpoints/profanityCheck.ts) | `typesafe/jev` |
| [public-browser](https://kydlikebtc.github.io/awesome-jev/?lang=en#public-browser) | `plugin` | [`examples/jev-loop.mjs`](https://github.com/Silbercue/public-browser/blob/HEAD/examples/jev-loop.mjs) | `typesafe-ai/jev` |
| [robo-harness](https://kydlikebtc.github.io/awesome-jev/?lang=en#robo-harness) | `project` | [`apps/server/src/decision/jev.ts`](https://github.com/grmkris/robo-harness/blob/HEAD/apps/server/src/decision/jev.ts) | `typesafe-ai/jev` |
| [search-function-test](https://kydlikebtc.github.io/awesome-jev/?lang=en#search-function-test) | `project` | [`htr-hero/src/lib/typesafeSearch.js`](https://github.com/Shifros/Search-Function-Test/blob/HEAD/htr-hero/src/lib/typesafeSearch.js) | `jev-latest` |
| [secondlayer](https://kydlikebtc.github.io/awesome-jev/?lang=en#secondlayer) | `project` | [`scripts/ops/jev-fault-triage.ts`](https://github.com/ryanwaits/secondlayer/blob/HEAD/scripts/ops/jev-fault-triage.ts) | `typesafe-ai/jev` |
| [shady-town](https://kydlikebtc.github.io/awesome-jev/?lang=en#shady-town) | `project` | [`lib/shady_town/evaluator.rb`](https://github.com/tpaulshippy/shady-town/blob/HEAD/lib/shady_town/evaluator.rb) | `jev-latest` |
| [smithers](https://kydlikebtc.github.io/awesome-jev/?lang=en#smithers) | `project` | [`apps/server/src/jev.ts`](https://github.com/smithersai/smithers/blob/HEAD/apps/server/src/jev.ts) | `typesafe-ai/jev` |
| [super-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#super-jev) | `project` | [`skills/super-jev/superjev.py`](https://github.com/Kevthetech143/super-jev/blob/HEAD/skills/super-jev/superjev.py) | `jev-1.13` |
| [tripwire](https://kydlikebtc.github.io/awesome-jev/?lang=en#tripwire) | `integration` | [`src/judge/jev.ts`](https://github.com/noelzappy/tripwire/blob/HEAD/src/judge/jev.ts) | `jev-latest` |
| [typesafe-playground-typesafeai](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-playground-typesafeai) | `project` | [`lib/callJev.ts`](https://github.com/TypeSafeAI/typesafe-playground/blob/HEAD/lib/callJev.ts) | `jev-latest` |
| [typesafe-ui](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ui) | `project` | [`apps/web/components/demos.tsx`](https://github.com/TypeSafeAI/typesafe-ui/blob/HEAD/apps/web/components/demos.tsx) | `jev-latest` |
| [wakegate](https://kydlikebtc.github.io/awesome-jev/?lang=en#wakegate) | `project` | [`src/index.ts`](https://github.com/shitianfang/wakegate/blob/HEAD/src/index.ts) | `typesafe-ai/jev` |
| [yoshi](https://kydlikebtc.github.io/awesome-jev/?lang=en#yoshi) | `plugin` | [`benchmarks/jev-calibrate.ts`](https://github.com/compozy/yoshi/blob/HEAD/benchmarks/jev-calibrate.ts) | `typesafe-ai/jev` |

<a id="tool-selection-broad-words"></a>

## Tool selection resting on words the keyword rules no longer count · 工具选择只靠关键词规则已不再计入的词

The row carries `tool-selection`, and the keyword rules suggest it for the row's summary and title only as they stood until 2026-09-27. They then counted "control", "harness" and "screen" on their own, and "robot", "autonomous" and "drive" with no word for deciding or acting beside them; the rules in `scripts/classify.py` no longer do. The bulk passes took the rules' patterns, so a row here may never have been read against tool-selection, or a person may have agreed with it without recording so. The rules read a project's GitHub description at discovery; the summary stands in for it here.

该行带有 `tool-selection`，而关键词规则只有按 2026-09-27 之前的写法才会从它的摘要和标题建议这个模式。当时的规则单凭 "control"、"harness"、"screen" 就算数，"robot"、"autonomous"、"drive" 旁边没有表示决定或动作的词也算数；`scripts/classify.py` 里现在的规则不再这样。批量收录时直接采用了规则给出的模式，所以这里的行可能从未有人对照 tool-selection 读过，也可能有人读过并同意，只是没有记录。规则在发现阶段读的是项目的 GitHub 描述；这里以摘要代替。

To take a row off, read the project against [`tool-selection`](patterns.md#tool-selection). If nothing in it decides which tool or action comes next, replace `tool-selection` in `patterns` with the pattern it does show, or with `overview`. Either way, set `patterns_reviewed` to the date you read it; that alone takes off a row whose `tool-selection` was right. A model that reads it sets `patterns_model_read_on` instead, which moves the row to [Read or written by a model](#model-read).

移出方法：对照 [`tool-selection`](patterns.md#tool-selection) 阅读该项目。如果其中没有任何东西在决定下一步调用哪个工具或采取哪个动作，就把 `patterns` 里的 `tool-selection` 换成它实际体现的模式，或换成 `overview`。无论哪种情况，都把阅读日期写入 `patterns_reviewed`；`tool-selection` 本来就对的行，只写这个日期也会移出。由模型阅读时改写 `patterns_model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。

| Row · 行 | Stars · 星标 | Patterns in the row · 该行的模式 | Suggested until 2026-09-27 · 2026-09-27 之前的建议 | Suggested now · 现在的建议 |
| --- | --- | --- | --- | --- |
| [reticle](https://kydlikebtc.github.io/awesome-jev/?lang=en#reticle) | ★1k+ | `output-validation` `tool-selection` | `tool-selection` `output-validation` `content-scoring` | `output-validation` `content-scoring` |
| [agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent) | ★100+ | `tool-selection` | `tool-selection` | `overview` |
| [jev-dsh-decision](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-dsh-decision) | ★100+ | `tool-selection` | `tool-selection` | `overview` |
| [jevharness](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevharness) | ★100+ | `tool-selection` | `tool-selection` `content-scoring` | `content-scoring` |
| [macbrow](https://kydlikebtc.github.io/awesome-jev/?lang=en#macbrow) | ★100+ | `tool-selection` | `tool-selection` `output-validation` `human-escalation` | `output-validation` `human-escalation` |
| [systemoneharness](https://kydlikebtc.github.io/awesome-jev/?lang=en#systemoneharness) | ★100+ | `tool-selection` | `tool-selection` | `overview` |
| [azdaja](https://kydlikebtc.github.io/awesome-jev/?lang=en#azdaja) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [discern](https://kydlikebtc.github.io/awesome-jev/?lang=en#discern) | ★10+ | `tool-selection` `human-escalation` | `tool-selection` `human-escalation` | `human-escalation` |
| [dsh-jev-buberlo](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-buberlo) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [dsh-jev-zhangxaochen](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-zhangxaochen) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [eutrya](https://kydlikebtc.github.io/awesome-jev/?lang=en#eutrya) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [hearth-jev-rental-search](https://kydlikebtc.github.io/awesome-jev/?lang=en#hearth-jev-rental-search) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [jcr](https://kydlikebtc.github.io/awesome-jev/?lang=en#jcr) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [jev-autopilot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-autopilot) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [jev-cua](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cua) | ★10+ | `tool-selection` `output-validation` | `tool-selection` `output-validation` | `output-validation` |
| [jev-harness](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness) | ★10+ | `tool-selection` `safety-gating` `human-escalation` | `tool-selection` `safety-gating` `human-escalation` | `safety-gating` `human-escalation` |
| [jev-harness-typesafeai](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness-typesafeai) | ★10+ | `tool-selection` | `tool-selection` `document-triage` | `document-triage` |
| [jev-libero](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-libero) | ★10+ | `tool-selection` `output-validation` | `tool-selection` `output-validation` | `output-validation` |
| [jev-mobile](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mobile) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [jev-usecases](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-usecases) | ★10+ | `tool-selection` `safety-gating` `human-escalation` | `tool-selection` `safety-gating` `human-escalation` | `safety-gating` `human-escalation` |
| [jevalyn](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevalyn) | ★10+ | `tool-selection` `content-scoring` `human-escalation` | `tool-selection` `content-scoring` `human-escalation` | `content-scoring` `human-escalation` |
| [jevgpt](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgpt) | ★10+ | `tool-selection` `content-scoring` | `tool-selection` `content-scoring` | `content-scoring` |
| [jevscape](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevscape) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [live-jev-okinaaudio](https://kydlikebtc.github.io/awesome-jev/?lang=en#live-jev-okinaaudio) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [mario-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#mario-jev) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [robojev](https://kydlikebtc.github.io/awesome-jev/?lang=en#robojev) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=en#smartmoney-cub) | ★10+ | `tool-selection` `output-validation` `content-scoring` | `tool-selection` `output-validation` `content-scoring` | `output-validation` `content-scoring` |
| [super-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#super-jev) | ★10+ | `tool-selection` | `tool-selection` | `overview` |
| [agi-jev-containment](https://kydlikebtc.github.io/awesome-jev/?lang=en#agi-jev-containment) |  | `classification` `tool-selection` `safety-gating` | `classification` `tool-selection` `safety-gating` | `classification` `safety-gating` `human-escalation` |
| [casse-brique-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#casse-brique-typesafe) |  | `tool-selection` | `tool-selection` | `overview` |
| [deepseek-harness-jev-pre-compaction](https://kydlikebtc.github.io/awesome-jev/?lang=en#deepseek-harness-jev-pre-compaction) |  | `tool-selection` `context-compaction` | `tool-selection` `context-compaction` | `context-compaction` |
| [dsh-jev-prune](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-prune) |  | `tool-selection` `content-scoring` `context-compaction` | `tool-selection` `content-scoring` `context-compaction` | `content-scoring` `context-compaction` `document-triage` |
| [dsh-jev-verify](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-verify) |  | `tool-selection` `output-validation` `content-scoring` | `tool-selection` `output-validation` `content-scoring` | `output-validation` `content-scoring` |
| [fast-compaction-dsh](https://kydlikebtc.github.io/awesome-jev/?lang=en#fast-compaction-dsh) |  | `tool-selection` `context-compaction` | `tool-selection` `context-compaction` | `context-compaction` |
| [gg-friggin-ez](https://kydlikebtc.github.io/awesome-jev/?lang=en#gg-friggin-ez) |  | `tool-selection` | `tool-selection` | `overview` |
| [harness-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#harness-router) |  | `tool-selection` | `tool-selection` `human-escalation` | `human-escalation` |
| [jev-plays-pokemon-red-christianmat](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-plays-pokemon-red-christianmat) |  | `tool-selection` | `tool-selection` `safety-gating` | `safety-gating` |
| [jev-agent-design-with-topk-logits-choices](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-agent-design-with-topk-logits-choices) |  | `tool-selection` | `tool-selection` `content-scoring` | `content-scoring` |
| [jev-agent-skill](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-agent-skill) |  | `classification` `tool-selection` `output-validation` | `classification` `tool-selection` `output-validation` | `classification` `output-validation` `content-scoring` |
| [jev-behavior-study](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-behavior-study) |  | `tool-selection` `output-validation` | `tool-selection` `output-validation` | `output-validation` |
| [jev-certify](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-certify) |  | `tool-selection` `safety-gating` `content-scoring` | `tool-selection` `safety-gating` `content-scoring` | `safety-gating` `content-scoring` `human-escalation` |
| [jev-codex-pilot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-codex-pilot) |  | `model-routing` `tool-selection` | `model-routing` `tool-selection` | `model-routing` |
| [jev-for-engineers](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-for-engineers) |  | `classification` `tool-selection` `output-validation` | `classification` `tool-selection` `output-validation` | `classification` `output-validation` `data-extraction` |
| [jev-harness-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness-router) |  | `model-routing` `tool-selection` | `model-routing` `tool-selection` | `model-routing` |
| [jev-layer](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-layer) |  | `tool-selection` `document-triage` | `tool-selection` `document-triage` | `document-triage` |
| [jev-llm-router-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-llm-router-benchmark) |  | `tool-selection` `content-scoring` | `tool-selection` `content-scoring` | `content-scoring` |
| [jev-model-tokengate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-model-tokengate) |  | `tool-selection` `safety-gating` | `tool-selection` `safety-gating` | `safety-gating` |
| [jev-physical-ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-physical-ai) |  | `tool-selection` | `tool-selection` | `overview` |
| [jev-plays](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-plays) |  | `tool-selection` | `tool-selection` | `overview` |
| [jev-robotics-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robotics-demo) |  | `tool-selection` | `tool-selection` | `overview` |
| [jev-routing](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-routing) |  | `tool-selection` | `tool-selection` | `overview` |
| [jev-voice-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice-control) |  | `tool-selection` | `tool-selection` | `overview` |
| [jev-windows-voice](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-windows-voice) |  | `tool-selection` | `tool-selection` | `overview` |
| [jevdroid](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevdroid) |  | `tool-selection` | `tool-selection` | `overview` |
| [jevloop-parkavenue9639](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevloop-parkavenue9639) |  | `tool-selection` | `tool-selection` | `overview` |
| [jevonly](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevonly) |  | `tool-selection` | `tool-selection` | `overview` |
| [pi-typesafe-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-typesafe-jev) |  | `tool-selection` `content-scoring` `human-escalation` | `tool-selection` `content-scoring` `human-escalation` | `content-scoring` `human-escalation` |
| [ps2-ai-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#ps2-ai-agent) |  | `tool-selection` | `tool-selection` | `overview` |
| [robo-harness](https://kydlikebtc.github.io/awesome-jev/?lang=en#robo-harness) |  | `tool-selection` | `tool-selection` | `overview` |
| [slidepilot](https://kydlikebtc.github.io/awesome-jev/?lang=en#slidepilot) |  | `tool-selection` | `tool-selection` | `overview` |
| [snake-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#snake-jev) |  | `tool-selection` `fan-out` | `tool-selection` `fan-out` | `fan-out` |
| [terrarium](https://kydlikebtc.github.io/awesome-jev/?lang=en#terrarium) |  | `tool-selection` | `tool-selection` | `overview` |
| [typesafe-minecraft-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-minecraft-demo) |  | `tool-selection` | `tool-selection` | `overview` |

<a id="unsorted-overview"></a>

## Overview rows with code, not yet indexed by pattern · 带代码、尚未按模式索引的 overview 行

The row is a project or a plugin with code, its only pattern is `overview`, and it records no reading against the patterns, neither a person's (`patterns_reviewed`) nor a model's (`patterns_model_read_on`). `overview` is for a row that surveys the model or the space ([patterns.md](patterns.md#overview)); it is also what the keyword rules suggest when nothing matches, and the bulk passes took the rules' patterns. The READMEs, the Overview page and the site list these rows apart, as not yet indexed by pattern. The last column is only a suggestion: what the keyword rules (`scripts/classify.py`) make of the row's summary and title, and a dash when none of them matches.

该行是带代码的项目或插件，唯一的模式是 `overview`，且没有任何对照决策模式阅读的记录：既没有人的（`patterns_reviewed`），也没有模型的（`patterns_model_read_on`）。`overview` 本是给介绍模型或整个领域的行用的（[patterns.md](patterns.md#overview)）；它也是关键词规则什么都没匹配到时给出的建议，而批量收录时直接采用了规则给出的模式。README、Overview 页面和站点把这些行单独列为“尚未按模式索引”。最后一列只是建议：关键词规则（`scripts/classify.py`）根据该行摘要和标题给出的结果，没有任何规则匹配时显示为破折号。

To take a row off, read the project against [the patterns](patterns.md). Put the patterns it shows in `patterns`, or keep `overview` if it surveys the space, and set `patterns_reviewed` to the date you read it. A model that reads it sets `patterns_model_read_on` instead, which moves the row to [Read or written by a model](#model-read).

移出方法：对照[决策模式](patterns.md)阅读该项目。把它体现的模式写进 `patterns`；如果它确实是在介绍整个领域，就保留 `overview`。然后把阅读日期写入 `patterns_reviewed`。由模型阅读时改写 `patterns_model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。

| Row · 行 | Kind · 类型 | Stars · 星标 | Keyword rules suggest (a suggestion) · 关键词规则的建议（仅供参考） |
| --- | --- | --- | --- |
| [langchain](https://kydlikebtc.github.io/awesome-jev/?lang=en#langchain) | `project` | ★100k+ | `content-scoring` `human-escalation` |
| [eliza](https://kydlikebtc.github.io/awesome-jev/?lang=en#eliza) | `project` | ★10k+ | — |
| [oh-my-pi](https://kydlikebtc.github.io/awesome-jev/?lang=en#oh-my-pi) | `project` | ★10k+ | — |
| [opik-typesafe-tracker](https://kydlikebtc.github.io/awesome-jev/?lang=en#opik-typesafe-tracker) | `project` | ★10k+ | — |
| [pydantic-ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#pydantic-ai) | `project` | ★10k+ | `content-scoring` |
| [ax](https://kydlikebtc.github.io/awesome-jev/?lang=en#ax) | `project` | ★1k+ | `content-scoring` `human-escalation` |
| [bifrost-typesafe-gateway](https://kydlikebtc.github.io/awesome-jev/?lang=en#bifrost-typesafe-gateway) | `project` | ★1k+ | `safety-gating` |
| [celesto](https://kydlikebtc.github.io/awesome-jev/?lang=en#celesto) | `project` | ★1k+ | — |
| [laya-mlx](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-mlx) | `project` | ★1k+ | `content-scoring` |
| [memsearch](https://kydlikebtc.github.io/awesome-jev/?lang=en#memsearch) | `plugin` | ★1k+ | `search-ranking` `classification` |
| [typesafe-skills-repo](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-skills-repo) | `plugin` | ★1k+ | — |
| [vellum-assistant](https://kydlikebtc.github.io/awesome-jev/?lang=en#vellum-assistant) | `project` | ★1k+ | — |
| [agent-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-router) | `plugin` | ★100+ | `search-ranking` |
| [aiavatarkit](https://kydlikebtc.github.io/awesome-jev/?lang=en#aiavatarkit) | `project` | ★100+ | `safety-gating` |
| [awesome-jev-fatwang2](https://kydlikebtc.github.io/awesome-jev/?lang=en#awesome-jev-fatwang2) | `project` | ★100+ | `output-validation` |
| [crush-monitor](https://kydlikebtc.github.io/awesome-jev/?lang=en#crush-monitor) | `project` | ★100+ | `content-scoring` `intent-routing` |
| [dasheng](https://kydlikebtc.github.io/awesome-jev/?lang=en#dasheng) | `project` | ★100+ | `content-scoring` |
| [distill](https://kydlikebtc.github.io/awesome-jev/?lang=en#distill) | `project` | ★100+ | `model-routing` |
| [djev-spark](https://kydlikebtc.github.io/awesome-jev/?lang=en#djev-spark) | `project` | ★100+ | `content-scoring` `document-triage` |
| [jev-cobusgreyling](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cobusgreyling) | `project` | ★100+ | `content-scoring` |
| [jev-chat-jarvis-mac](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-jarvis-mac) | `project` | ★100+ | — |
| [jev-chat-windows](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-windows) | `project` | ★100+ | — |
| [jev-docs-zh](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-docs-zh) | `project` | ★100+ | — |
| [jev-experiments](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-experiments) | `project` | ★100+ | `search-ranking` `safety-gating` `output-validation` |
| [jev-foundation-models](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-foundation-models) | `project` | ★100+ | `content-scoring` `data-extraction` |
| [jev-skill-wuyoscar](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-wuyoscar) | `plugin` | ★100+ | `output-validation` |
| [jev-voice](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice) | `project` | ★100+ | — |
| [jevmem](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmem) | `plugin` | ★100+ | — |
| [jevmind](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmind) | `project` | ★100+ | `safety-gating` `content-scoring` `human-escalation` |
| [kody](https://kydlikebtc.github.io/awesome-jev/?lang=en#kody) | `plugin` | ★100+ | `search-ranking` `content-scoring` `human-escalation` |
| [laya](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya) | `project` | ★100+ | `content-scoring` |
| [laya-ultrafast](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-ultrafast) | `project` | ★100+ | `tool-selection` |
| [laya-vs-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-vs-jev) | `project` | ★100+ | `classification` `safety-gating` `output-validation` |
| [openwhisper](https://kydlikebtc.github.io/awesome-jev/?lang=en#openwhisper) | `project` | ★100+ | — |
| [orchestkit](https://kydlikebtc.github.io/awesome-jev/?lang=en#orchestkit) | `plugin` | ★100+ | `classification` `output-validation` |
| [pi-fabric](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-fabric) | `project` | ★100+ | `classification` `content-scoring` |
| [req-llm](https://kydlikebtc.github.io/awesome-jev/?lang=en#req-llm) | `project` | ★100+ | `content-scoring` |
| [runline](https://kydlikebtc.github.io/awesome-jev/?lang=en#runline) | `project` | ★100+ | `output-validation` `content-scoring` |
| [smithers](https://kydlikebtc.github.io/awesome-jev/?lang=en#smithers) | `project` | ★100+ | — |
| [stanley-code](https://kydlikebtc.github.io/awesome-jev/?lang=en#stanley-code) | `project` | ★100+ | — |
| [third-hand](https://kydlikebtc.github.io/awesome-jev/?lang=en#third-hand) | `project` | ★100+ | `classification` `tool-selection` |
| [typesafe-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-mcp) | `plugin` | ★100+ | — |
| [webctl](https://kydlikebtc.github.io/awesome-jev/?lang=en#webctl) | `project` | ★100+ | `content-scoring` |
| [ask-jev-skill](https://kydlikebtc.github.io/awesome-jev/?lang=en#ask-jev-skill) | `plugin` | ★10+ | — |
| [awesome-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#awesome-jev) | `project` | ★10+ | — |
| [call-coach-ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#call-coach-ai) | `project` | ★10+ | — |
| [captaincore](https://kydlikebtc.github.io/awesome-jev/?lang=en#captaincore) | `project` | ★10+ | — |
| [clash-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#clash-jev) | `project` | ★10+ | — |
| [cultivar](https://kydlikebtc.github.io/awesome-jev/?lang=en#cultivar) | `project` | ★10+ | — |
| [dspy-typesafeify](https://kydlikebtc.github.io/awesome-jev/?lang=en#dspy-typesafeify) | `project` | ★10+ | — |
| [duckdb-jev-colliber](https://kydlikebtc.github.io/awesome-jev/?lang=en#duckdb-jev-colliber) | `plugin` | ★10+ | — |
| [edgejev](https://kydlikebtc.github.io/awesome-jev/?lang=en#edgejev) | `project` | ★10+ | — |
| [is-jeven](https://kydlikebtc.github.io/awesome-jev/?lang=en#is-jeven) | `project` | ★10+ | — |
| [james-library](https://kydlikebtc.github.io/awesome-jev/?lang=en#james-library) | `project` | ★10+ | `content-scoring` |
| [jeq](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeq) | `project` | ★10+ | — |
| [jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev) | `plugin` | ★10+ | — |
| [jev-mayank953](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mayank953) | `project` | ★10+ | — |
| [jev-okooo5km](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-okooo5km) | `plugin` | ★10+ | `search-ranking` `content-scoring` `human-escalation` |
| [jev-blindspot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-blindspot) | `plugin` | ★10+ | — |
| [jev-canvas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-canvas) | `project` | ★10+ | — |
| [jev-chat-for-twitch](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-for-twitch) | `plugin` | ★10+ | — |
| [jev-chat-windows-deepseek-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-windows-deepseek-jev) | `project` | ★10+ | — |
| [jev-cli-shaharia-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cli-shaharia-lab) | `project` | ★10+ | `content-scoring` `human-escalation` |
| [jev-judge-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-judge-mcp) | `plugin` | ★10+ | `search-ranking` `classification` `tool-selection` |
| [jev-leftpad](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-leftpad) | `project` | ★10+ | — |
| [jev-mcp-burnigtm](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-burnigtm) | `plugin` | ★10+ | — |
| [jev-paint](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-paint) | `project` | ★10+ | — |
| [jev-playground-mizchi](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-playground-mizchi) | `project` | ★10+ | `content-scoring` |
| [jev-realtime-trading](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-realtime-trading) | `project` | ★10+ | — |
| [jev-recipes](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-recipes) | `project` | ★10+ | `search-ranking` `output-validation` |
| [jev-register-tool](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-register-tool) | `project` | ★10+ | — |
| [jev-rules](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rules) | `project` | ★10+ | — |
| [jev-skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-router) | `plugin` | ★10+ | `search-ranking` `safety-gating` `content-scoring` |
| [jev-skill-suggester](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-suggester) | `plugin` | ★10+ | — |
| [jev-spring-boot-starter](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-spring-boot-starter) | `plugin` | ★10+ | — |
| [jev-studio](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-studio) | `project` | ★10+ | — |
| [jev-tetris](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tetris) | `project` | ★10+ | — |
| [jev-to-answer](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-to-answer) | `project` | ★10+ | — |
| [jev-trades](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trades) | `project` | ★10+ | — |
| [jev-tree-chuf-h](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tree-chuf-h) | `project` | ★10+ | `output-validation` |
| [jev-trip](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trip) | `project` | ★10+ | — |
| [jev-vs-ml](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-vs-ml) | `project` | ★10+ | — |
| [jev-ontology](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ontology) | `project` | ★10+ | — |
| [jev-project-context](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-project-context) | `plugin` | ★10+ | — |
| [jev-stock](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-stock) | `project` | ★10+ | — |
| [jevchat](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevchat) | `project` | ★10+ | — |
| [jevernetes](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevernetes) | `project` | ★10+ | — |
| [jevgraph](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgraph) | `project` | ★10+ | — |
| [jeview](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeview) | `project` | ★10+ | — |
| [jevify](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevify) | `plugin` | ★10+ | — |
| [jevloop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevloop) | `project` | ★10+ | — |
| [jevocks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevocks) | `project` | ★10+ | — |
| [jevplayspokemon](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevplayspokemon) | `project` | ★10+ | — |
| [jevthoven](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevthoven) | `project` | ★10+ | — |
| [jevtown](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevtown) | `project` | ★10+ | — |
| [jevvy](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevvy) | `plugin` | ★10+ | — |
| [jot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jot) | `project` | ★10+ | — |
| [jpp](https://kydlikebtc.github.io/awesome-jev/?lang=en#jpp) | `project` | ★10+ | — |
| [laya-jev-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-jev-lab) | `project` | ★10+ | — |
| [laya-vs-jev-arena](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-vs-jev-arena) | `project` | ★10+ | — |
| [llm-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#llm-typesafe) | `plugin` | ★10+ | — |
| [loki](https://kydlikebtc.github.io/awesome-jev/?lang=en#loki) | `project` | ★10+ | — |
| [open-spark-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-spark-jev) | `project` | ★10+ | — |
| [openthai-systemone](https://kydlikebtc.github.io/awesome-jev/?lang=en#openthai-systemone) | `project` | ★10+ | — |
| [pi-quiet-ask](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-quiet-ask) | `project` | ★10+ | — |
| [st-jeved](https://kydlikebtc.github.io/awesome-jev/?lang=en#st-jeved) | `plugin` | ★10+ | — |
| [switchboard](https://kydlikebtc.github.io/awesome-jev/?lang=en#switchboard) | `plugin` | ★10+ | — |
| [trade-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#trade-jev) | `project` | ★10+ | — |
| [typesafe-chess](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-chess) | `project` | ★10+ | — |
| [typesafe-playground](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-playground) | `project` | ★10+ | — |
| [typesafe-playground-typesafeai](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-playground-typesafeai) | `project` | ★10+ | — |
| [typesafe-skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-skill-router) | `plugin` | ★10+ | — |
| [xtags](https://kydlikebtc.github.io/awesome-jev/?lang=en#xtags) | `project` | ★10+ | — |
| [aegis-typesafe-provider](https://kydlikebtc.github.io/awesome-jev/?lang=en#aegis-typesafe-provider) | `project` |  | `safety-gating` `data-extraction` |
| [agent-jev-tetris](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-jev-tetris) | `project` |  | — |
| [ai-elo-ranker](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai-elo-ranker) | `project` |  | — |
| [ailerix](https://kydlikebtc.github.io/awesome-jev/?lang=en#ailerix) | `project` |  | — |
| [alphaoptimizer](https://kydlikebtc.github.io/awesome-jev/?lang=en#alphaoptimizer) | `plugin` |  | — |
| [askjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#askjev) | `plugin` |  | — |
| [askjev-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#askjev-mcp) | `plugin` |  | `content-scoring` `human-escalation` |
| [auto-mode-for-paseo](https://kydlikebtc.github.io/awesome-jev/?lang=en#auto-mode-for-paseo) | `plugin` |  | — |
| [awesome-jev-use-cases](https://kydlikebtc.github.io/awesome-jev/?lang=en#awesome-jev-use-cases) | `project` |  | `search-ranking` `model-routing` `safety-gating` |
| [barrunto](https://kydlikebtc.github.io/awesome-jev/?lang=en#barrunto) | `plugin` |  | — |
| [beatjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#beatjev) | `project` |  | — |
| [bes-kelime-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#bes-kelime-jev) | `project` |  | — |
| [btc-jev-signal](https://kydlikebtc.github.io/awesome-jev/?lang=en#btc-jev-signal) | `project` |  | — |
| [building-with-typesafe-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#building-with-typesafe-jev) | `plugin` |  | `content-scoring` `human-escalation` |
| [cairn-jev-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#cairn-jev-lab) | `project` |  | — |
| [cartshield](https://kydlikebtc.github.io/awesome-jev/?lang=en#cartshield) | `project` |  | — |
| [codex-jev-preflight](https://kydlikebtc.github.io/awesome-jev/?lang=en#codex-jev-preflight) | `plugin` |  | — |
| [commentcop](https://kydlikebtc.github.io/awesome-jev/?lang=en#commentcop) | `project` |  | — |
| [cyber-breach-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#cyber-breach-jev) | `project` |  | — |
| [dbt-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#dbt-jev) | `plugin` |  | — |
| [decisions-judge-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisions-judge-mcp) | `plugin` |  | `content-scoring` |
| [dgp](https://kydlikebtc.github.io/awesome-jev/?lang=en#dgp) | `project` |  | `safety-gating` `fan-out` |
| [emoji-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#emoji-jev) | `project` |  | — |
| [everything-about-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#everything-about-jev) | `project` |  | — |
| [extremely-specific-council](https://kydlikebtc.github.io/awesome-jev/?lang=en#extremely-specific-council) | `project` |  | — |
| [financialpredictionjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#financialpredictionjev) | `project` |  | — |
| [frost](https://kydlikebtc.github.io/awesome-jev/?lang=en#frost) | `project` |  | — |
| [functions](https://kydlikebtc.github.io/awesome-jev/?lang=en#functions) | `project` |  | — |
| [git-jev-stage](https://kydlikebtc.github.io/awesome-jev/?lang=en#git-jev-stage) | `project` |  | — |
| [got-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#got-jev) | `project` |  | — |
| [ha-conversation-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#ha-conversation-jev) | `project` |  | — |
| [harden-jev-decides](https://kydlikebtc.github.io/awesome-jev/?lang=en#harden-jev-decides) | `project` |  | — |
| [hermes-jev-curator](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-jev-curator) | `project` |  | — |
| [hiresignal](https://kydlikebtc.github.io/awesome-jev/?lang=en#hiresignal) | `project` |  | — |
| [jcm-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jcm-router) | `project` |  | — |
| [jeff-cli](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeff-cli) | `project` |  | `search-ranking` `content-scoring` `human-escalation` |
| [jev-2048](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-2048) | `project` |  | — |
| [jev-acp](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-acp) | `project` |  | — |
| [jev-anotacao-sentencas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-anotacao-sentencas) | `project` |  | — |
| [jev-arena-nanojev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-arena-nanojev) | `project` |  | — |
| [jev-bot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-bot) | `project` |  | — |
| [jev-broadcast-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-broadcast-lab) | `project` |  | — |
| [jev-calculator](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-calculator) | `project` |  | — |
| [jev-chat](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat) | `project` |  | — |
| [jev-ci-selector](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ci-selector) | `project` |  | — |
| [jev-cli-jtsang4](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cli-jtsang4) | `project` |  | — |
| [jev-cloud-quiz](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cloud-quiz) | `project` |  | `content-scoring` |
| [jev-codex-router-skill](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-codex-router-skill) | `plugin` |  | — |
| [jev-connector](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-connector) | `plugin` |  | `content-scoring` `human-escalation` |
| [jev-cvss](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cvss) | `project` |  | — |
| [jev-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-demo) | `project` |  | — |
| [jev-demo-penglonghuang](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-demo-penglonghuang) | `project` |  | `tool-selection` `content-scoring` `human-escalation` |
| [jev-evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-evaluation) | `project` |  | — |
| [jev-eyes](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-eyes) | `plugin` |  | — |
| [jev-freeform](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-freeform) | `project` |  | — |
| [jev-games](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-games) | `project` |  | — |
| [jev-gomoku](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-gomoku) | `project` |  | — |
| [jev-grand-prix](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-grand-prix) | `project` |  | — |
| [jev-grug](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-grug) | `project` |  | — |
| [jev-mcp-arunav25](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-arunav25) | `plugin` |  | `content-scoring` `feature-extraction` |
| [jev-mcp-byk](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-byk) | `plugin` |  | `content-scoring` |
| [jev-mcp-freepik-company](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-freepik-company) | `plugin` |  | — |
| [jev-mcp-rajasekharponakala](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-rajasekharponakala) | `plugin` |  | `content-scoring` |
| [jev-mcp-rashedint32](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-rashedint32) | `plugin` |  | `classification` `output-validation` `content-scoring` |
| [jev-mcp-spring](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-spring) | `plugin` |  | — |
| [jev-measured](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-measured) | `project` |  | — |
| [jev-minesweeper](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-minesweeper) | `project` |  | — |
| [jev-pick-and-place-study](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-pick-and-place-study) | `project` |  | — |
| [jev-pii-checker](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-pii-checker) | `project` |  | — |
| [jev-playground](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-playground) | `project` |  | — |
| [jev-playground-little-planet-labs](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-playground-little-planet-labs) | `project` |  | — |
| [jev-plays-pokemon](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-plays-pokemon) | `project` |  | — |
| [jev-practice-speed](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-practice-speed) | `project` |  | — |
| [jev-resume-disqualifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-resume-disqualifier) | `project` |  | — |
| [jev-search](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-search) | `project` |  | — |
| [jev-skills-laguagu](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skills-laguagu) | `plugin` |  | `search-ranking` `output-validation` |
| [jev-snake](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-snake) | `project` |  | — |
| [jev-system-one](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-system-one) | `project` |  | — |
| [jev-t-rex-runner](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-t-rex-runner) | `project` |  | — |
| [jev-torneo-animales](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-torneo-animales) | `project` |  | — |
| [jev-wingman](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-wingman) | `project` |  | — |
| [jev-x-kit](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-x-kit) | `project` |  | `safety-gating` `content-scoring` `human-escalation` |
| [jev-yt-time-saver](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-yt-time-saver) | `plugin` |  | — |
| [jev2048](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev2048) | `project` |  | — |
| [jev-jsonschema](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-jsonschema) | `project` |  | — |
| [jevals-dayhaysoos](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevals-dayhaysoos) | `project` |  | — |
| [jevcode](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevcode) | `project` |  | — |
| [jevometry](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevometry) | `project` |  | — |
| [jevopt](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevopt) | `project` |  | — |
| [jevscope](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevscope) | `project` |  | — |
| [jevseek-blingdivinity](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevseek-blingdivinity) | `project` |  | — |
| [jevslop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevslop) | `project` |  | — |
| [jevtape](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevtape) | `project` |  | — |
| [jevtest](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevtest) | `project` |  | — |
| [jevtok](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevtok) | `project` |  | — |
| [labs](https://kydlikebtc.github.io/awesome-jev/?lang=en#labs) | `project` |  | — |
| [magic-jev-ball](https://kydlikebtc.github.io/awesome-jev/?lang=en#magic-jev-ball) | `project` |  | `safety-gating` |
| [mcpmatch](https://kydlikebtc.github.io/awesome-jev/?lang=en#mcpmatch) | `plugin` |  | — |
| [mcts-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#mcts-agent) | `project` |  | — |
| [mimicry](https://kydlikebtc.github.io/awesome-jev/?lang=en#mimicry) | `project` |  | — |
| [n8n-nodes-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#n8n-nodes-jev) | `plugin` |  | `classification` `output-validation` `content-scoring` |
| [n8n-nodes-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#n8n-nodes-typesafe) | `plugin` |  | — |
| [n8n-nodes-typesafe-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#n8n-nodes-typesafe-jev) | `project` |  | — |
| [new-api-plugin-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#new-api-plugin-typesafe) | `plugin` |  | — |
| [open-jev-bridge](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-jev-bridge) | `plugin` |  | `output-validation` `content-scoring` `context-compaction` |
| [openpoke-meets-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#openpoke-meets-jev) | `project` |  | — |
| [pi-agent-foreman](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-agent-foreman) | `project` |  | — |
| [pi-typesafe-twilwa](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-typesafe-twilwa) | `plugin` |  | — |
| [pong-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#pong-jev) | `project` |  | — |
| [pydantic-jev-examples](https://kydlikebtc.github.io/awesome-jev/?lang=en#pydantic-jev-examples) | `project` |  | — |
| [r2r-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#r2r-jev) | `project` |  | `content-scoring` |
| [research-desk](https://kydlikebtc.github.io/awesome-jev/?lang=en#research-desk) | `project` |  | — |
| [risc-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#risc-jev) | `project` |  | — |
| [river-run-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#river-run-typesafe) | `project` |  | — |
| [rubikjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#rubikjev) | `project` |  | — |
| [rust-sysone](https://kydlikebtc.github.io/awesome-jev/?lang=en#rust-sysone) | `project` |  | — |
| [scam-shield](https://kydlikebtc.github.io/awesome-jev/?lang=en#scam-shield) | `project` |  | — |
| [search-function-test](https://kydlikebtc.github.io/awesome-jev/?lang=en#search-function-test) | `project` |  | — |
| [second-thought](https://kydlikebtc.github.io/awesome-jev/?lang=en#second-thought) | `project` |  | — |
| [secondlayer](https://kydlikebtc.github.io/awesome-jev/?lang=en#secondlayer) | `project` |  | — |
| [should-ai-kill-us-all](https://kydlikebtc.github.io/awesome-jev/?lang=en#should-ai-kill-us-all) | `project` |  | — |
| [skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#skill-router) | `plugin` |  | — |
| [soupbase](https://kydlikebtc.github.io/awesome-jev/?lang=en#soupbase) | `project` |  | — |
| [sqlite3-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#sqlite3-jev) | `plugin` |  | — |
| [system-one-chess](https://kydlikebtc.github.io/awesome-jev/?lang=en#system-one-chess) | `project` |  | — |
| [systemone-lite](https://kydlikebtc.github.io/awesome-jev/?lang=en#systemone-lite) | `project` |  | — |
| [tempo-jev-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#tempo-jev-demo) | `project` |  | — |
| [typesafe-ai-playground](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-playground) | `project` |  | — |
| [typesafe-assist](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-assist) | `project` |  | — |
| [typesafe-comment](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-comment) | `project` |  | — |
| [typesafe-jev-examples](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-jev-examples) | `project` |  | — |
| [typesafe-jev-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-jev-mcp) | `plugin` |  | — |
| [typesafe-jev-tools](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-jev-tools) | `plugin` |  | — |
| [typesafe-ui](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ui) | `project` |  | `safety-gating` |
| [typesafe-chess-eval](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-chess-eval) | `project` |  | — |
| [typesafeai-cli](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafeai-cli) | `project` |  | — |
| [wellposed](https://kydlikebtc.github.io/awesome-jev/?lang=en#wellposed) | `project` |  | `output-validation` |
| [your-signal](https://kydlikebtc.github.io/awesome-jev/?lang=en#your-signal) | `plugin` |  | — |

<a id="generic-summary"></a>

## Rows with code whose summary names nothing about Jev · 带代码、摘要没有提到 Jev 的行

The row has code, is not TypeSafe AI's own (`official`), has no `notes`, and its English summary contains none of `jev`, `typesafe`, `System One`, `choice`, `score`, `noul`, `decision`, `confidence` (in any case, also inside a longer word). Most are the project's own GitHub description (`summary_source`), which has no reason to mention Jev, so a reader of the list cannot tell what the project asks Jev to decide. The words are a floor, not a test: a summary without them may still say it, and one with them may say little. The last column links the file the row cites, as the READMEs and the pattern pages do.

该行带代码，不是 TypeSafe AI 自己发布的（`official`），没有 `notes`，而且英文摘要里没有 `jev`、`typesafe`、`System One`、`choice`、`score`、`noul`、`decision`、`confidence` 中的任何一个（不分大小写，出现在更长的词里也算）。其中多数是项目自己在 GitHub 上的描述（`summary_source`），它没有理由提到 Jev，于是读列表的人看不出这个项目让 Jev 做什么决策。这些词只是底线，不是检验：没有这些词的摘要也可能说清楚了，有这些词的也可能什么都没说。最后一列链接到该行引用的文件，与 README 和模式页面一样。

To take a row off, read the cited file and write a summary that says what the project asks Jev to decide, in words that include one of those above (naming Jev is enough; the rule reads only the words), with `summary_source` set to `curated` and `summary_zh` to match (see the `summary` field rules in [CONTRIBUTING](../CONTRIBUTING.md#field-rules)); or keep the summary and add a `notes` line that says it. A summary a model writes is labelled `model-written` instead, and the row moves to [Read or written by a model](#model-read).

移出方法：读引用的文件，写一条说明该项目让 Jev 决定什么的摘要，其中要含有上面列出的某个词（写出 Jev 即可；规则只看这些词），把 `summary_source` 设为 `curated`，并相应更新 `summary_zh`（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `summary` 的字段规则）；或者保留摘要，加一行 `notes` 说明这一点。由模型撰写的摘要改标为 `model-written`，该行会移到[模型读过或撰写](#model-read)一节。

| Row · 行 | Kind · 类型 | Stars · 星标 | Summary · 摘要 | Summary source · 摘要来源 | Cited file · 引用的文件 |
| --- | --- | --- | --- | --- | --- |
| [langchainjs-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#langchainjs-typesafe) | `integration` | ★10k+ | The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes. | — | [`libs/providers/langchain-typesafe/src/types.ts`](https://github.com/langchain-ai/langchainjs/blob/HEAD/libs/providers/langchain-typesafe/src/types.ts) |
| [ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai) | `sdk` | ★10k+ | The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents | `upstream-description` | [`examples/ai-functions/src/evaluate/typesafe-ai/basic.ts`](https://github.com/vercel/ai/blob/HEAD/examples/ai-functions/src/evaluate/typesafe-ai/basic.ts) |
| [eliza](https://kydlikebtc.github.io/awesome-jev/?lang=en#eliza) | `project` | ★10k+ | Open source agentic operating system | `upstream-description` | [`packages/agent/src/services/typesafe/client.ts`](https://github.com/elizaOS/eliza/blob/HEAD/packages/agent/src/services/typesafe/client.ts) |
| [oh-my-pi](https://kydlikebtc.github.io/awesome-jev/?lang=en#oh-my-pi) | `project` | ★10k+ | ⌥ Coding agent with the IDE wired in | — | [`packages/ai/src/judgment/typesafe.ts`](https://github.com/can1357/oh-my-pi/blob/HEAD/packages/ai/src/judgment/typesafe.ts) |
| [bifrost-typesafe-gateway](https://kydlikebtc.github.io/awesome-jev/?lang=en#bifrost-typesafe-gateway) | `project` | ★1k+ | A Go gateway provider that passes the native API through one-to-one, so the official SDKs work by changing only the base URL. | — | [`core/providers/typesafe/typesafe.go`](https://github.com/maximhq/bifrost/blob/HEAD/core/providers/typesafe/typesafe.go) |
| [celesto](https://kydlikebtc.github.io/awesome-jev/?lang=en#celesto) | `project` | ★1k+ | Secure and persistent computer for AI agents -- build your own Grokbot, and Muse. | — | [`examples/pr-review-jev/models.py`](https://github.com/CelestoAI/celesto/blob/HEAD/examples/pr-review-jev/models.py) |
| [typesafe-computer-use](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-computer-use) | `project` | ★1k+ | Computer use on macOS: OCR the screen, classify the next action, click. Costs a fraction of a cent per step. | — | [`typesafe_computer_use/decide.py`](https://github.com/awlevin/typesafe-computer-use/blob/HEAD/typesafe_computer_use/decide.py) |
| [agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent) | `integration` | ★100+ | AgentiLoop Agent! An Autonomous Agentic Agent for Mac, and exclusive Apple only harnesss. Supports automation, scripting, coding, build anything and more. Powered by 21 LLM providers across local and cloud platforms. Dark or Light Mode UI. | — | [`TypeSafeKit/Sources/TypeSafeKit/TypeSafeClient.swift`](https://github.com/AgentiLoop/Agent/blob/HEAD/TypeSafeKit/Sources/TypeSafeKit/TypeSafeClient.swift) |
| [jev-chat-jarvis-mac](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-jarvis-mac) | `project` | ★100+ | 微信消息意图识别悬浮窗（macOS）：看屏 + 本地小模型判断意图和风险，再按话术生成回复候选。纯只读、不注入微信。 | — | [`src/judge_jev.py`](https://github.com/jev-chat/jev-chat-jarvis-mac/blob/HEAD/src/judge_jev.py) |
| [jev-review](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-review) | `plugin` | ★100+ | A local-first MCP plugin for continuous code-quality review by coding agents. | — | [`src/jev/client.ts`](https://github.com/NiazMorshed2007/jev-review/blob/HEAD/src/jev/client.ts) |
| [jevrouter](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevrouter) | `project` | ★100+ | A router for models, tools and subagents. | — | [`functions/api/jev.js`](https://github.com/BillionsBobby/JevRouter/blob/HEAD/functions/api/jev.js) |
| [openwhisper](https://kydlikebtc.github.io/awesome-jev/?lang=en#openwhisper) | `project` | ★100+ | Local speech-to-text, dictation, and meetings with Whisper and OpenAI API. Optional Windows x64 engines: Parakeet, Qwen3-ASR, Nemotron Streaming, and Moonshine. | — | [`benchmarks/typesafe_experiments.py`](https://github.com/Knuckles92/OpenWhisper/blob/HEAD/benchmarks/typesafe_experiments.py) |
| [skillranker](https://kydlikebtc.github.io/awesome-jev/?lang=en#skillranker) | `plugin` | ★100+ | Ranks an agent's skills for the next step using live session context, with Claude Code hooks. | — | [`src/jev/endpoint.rs`](https://github.com/Dicklesworthstone/skillranker/blob/HEAD/src/jev/endpoint.rs) |
| [smithers](https://kydlikebtc.github.io/awesome-jev/?lang=en#smithers) | `project` | ★100+ | Smithers is an agentic workflow framework for defining workflows in simple TypeScript configuration files and executing them quickly, durably, and reliably | `upstream-description` | [`apps/server/src/jev.ts`](https://github.com/smithersai/smithers/blob/HEAD/apps/server/src/jev.ts) |
| [supercov](https://kydlikebtc.github.io/awesome-jev/?lang=en#supercov) | `project` | ★100+ | Code quality and coverage judgements for coding agents, in Rust. | — | [`crates/supercov-cli/src/quality.rs`](https://github.com/supercorp-ai/supercov/blob/HEAD/crates/supercov-cli/src/quality.rs) |
| [unclutter](https://kydlikebtc.github.io/awesome-jev/?lang=en#unclutter) | `project` | ★100+ | A browser extension that removes page clutter, with reusable template rules. | — | [`lib/jev.ts`](https://github.com/kitze/unclutter/blob/HEAD/lib/jev.ts) |
| [advocaat](https://kydlikebtc.github.io/awesome-jev/?lang=en#advocaat) | `sdk` | ★10+ | A small typed client for asking questions about your own data. | — | [`src/api.ts`](https://github.com/pithings/advocaat/blob/HEAD/src/api.ts) |
| [agent-chaperone](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-chaperone) | `plugin` | ★10+ | Screens an AI agent's tool calls before they run and tool results before the agent reads them. An MCP proxy plus a hooks adapter for a client's built-in tools. | `upstream-description` | [`src/backends/typesafe.ts`](https://github.com/agent-chaperone/agent-chaperone/blob/HEAD/src/backends/typesafe.ts) |
| [azdaja](https://kydlikebtc.github.io/awesome-jev/?lang=en#azdaja) | `project` | ★10+ | Minimal harness-agnostic recursive language model layer — one binary, Python + llm() | `upstream-description` | [`bench/jev/adapter.py`](https://github.com/kubet/azdaja/blob/HEAD/bench/jev/adapter.py) |
| [bluenoise](https://kydlikebtc.github.io/awesome-jev/?lang=en#bluenoise) | `project` | ★10+ | Blur or hide noisy replies, posts & ads on X (Twitter), and clean up its interface with local, reversible keyword/account rules — no X API, no data collection, no account changes. 用本地可逆的关键词/账号规则模糊或隐藏 X（推特）上的嘈杂回复、帖子和广告，并整理界面——不调用 X API、不收集数据、不修改账号。 | `upstream-description` | [`src/contracts/ai.ts`](https://github.com/rokcso/bluenoise/blob/HEAD/src/contracts/ai.ts) |
| [browserclaw](https://kydlikebtc.github.io/awesome-jev/?lang=en#browserclaw) | `plugin` | ★10+ | BrowserClaw - High-efficiency Chrome browser automation MCP server | `upstream-description-stale` | [`app/native-server/src/jev/jev-client.ts`](https://github.com/GoldenLoaf24h/browserpaw/blob/HEAD/app/native-server/src/jev/jev-client.ts) |
| [captaincore](https://kydlikebtc.github.io/awesome-jev/?lang=en#captaincore) | `project` | ★10+ | 👨🏽‍💻 CaptainCore is a command line application for automating WordPress maintenance. | `upstream-description` | [`typesafe/client.go`](https://github.com/CaptainCore/captaincore/blob/HEAD/typesafe/client.go) |
| [cultivar](https://kydlikebtc.github.io/awesome-jev/?lang=en#cultivar) | `project` | ★10+ | Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents. | `upstream-description` | [`evals/framework/typesafe_grader.py`](https://github.com/pinecone-io/cultivar/blob/HEAD/evals/framework/typesafe_grader.py) |
| [hono-jev-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#hono-jev-router) | `project` | ★10+ | Routes HTTP requests by meaning — a semantic router for a web framework. | — | [`src/index.ts`](https://github.com/yusukebe/hono-jev-router/blob/HEAD/src/index.ts) |
| [is-malicious](https://kydlikebtc.github.io/awesome-jev/?lang=en#is-malicious) | `project` | ★10+ | A codebase scanner that helps you not run malicous code | `upstream-description` | [`src/jev.ts`](https://github.com/luantak/is-malicious/blob/HEAD/src/jev.ts) |
| [james-library](https://kydlikebtc.github.io/awesome-jev/?lang=en#james-library) | `project` | ★10+ | R.A.I.N. Lab is an experimental scientific-agent architecture that separates fast local judgment, independent probabilistic evaluation, multi-agent deliberation, evidence, and authorization into distinct computational layers.🐙(Predates Karpathy's AutoResearch) | `upstream-description-stale` | [`james_library/judgment/typesafe.py`](https://github.com/topherchris420/james_library/blob/HEAD/james_library/judgment/typesafe.py) |
| [jev-blindspot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-blindspot) | `plugin` | ★10+ | A side-panel assistant that finds the blind spots in your prompts. For Claude Code and Codex CLI. | `upstream-description-stale` | [`scripts/gate-tune.mjs`](https://github.com/jsk4581/jev-blindspot/blob/HEAD/scripts/gate-tune.mjs) |
| [jev-commit](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-commit) | `project` | ★10+ | A pre-commit hook: one call judges whether the commit message matches the diff. | — | [`jev_commit/jev.py`](https://github.com/valentynkit/jev-commit/blob/HEAD/jev_commit/jev.py) |
| [jev-sift](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-sift) | `plugin` | ★10+ | Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification. | `upstream-description` | [`dist/server.mjs`](https://github.com/kbhuw/jev-sift/blob/HEAD/dist/server.mjs) |
| [jevbystander](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbystander) | `project` | ★10+ | An Android accessibility reader for WeChat: it only reads the screen and pops three toasts — intent, emotion, urgency, a suggestion — and never writes or sends a reply. No third-party dependencies; an 861 KB APK. | — | [`app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt`](https://github.com/Nisaka520/JevBystander/blob/HEAD/app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt) |
| [jevintent](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevintent) | `project` | ★10+ | A WeChat plugin (FkWeChat): long-press a message to analyse its intent, emotion and a suggested reply stance, shown only as a local hint the sender never sees. | — | [`main.java`](https://github.com/Nisaka520/JevIntent/blob/HEAD/main.java) |
| [jpp](https://kydlikebtc.github.io/awesome-jev/?lang=en#jpp) | `project` | ★10+ | J++: an experimental language with standalone source and a Rust runtime. Compose questions and methods. 独立源码，组合问题与方法。 | `upstream-description` | [`src/foundation/clients/eye_client.py`](https://github.com/Towow-ai/jpp/blob/HEAD/src/foundation/clients/eye_client.py) |
| [legalforecastbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#legalforecastbench) | `benchmark` | ★10+ | LegalForecast-MTD benchmark alpha and official evaluation workflows | `upstream-description` | [`legalforecast/jev/execution.py`](https://github.com/johnhughes3/LegalForecastBench/blob/HEAD/legalforecast/jev/execution.py) |
| [lintus](https://kydlikebtc.github.io/awesome-jev/?lang=en#lintus) | `project` | ★10+ | A linter whose rules are written in plain language. | `upstream-description` | [`crates/jev/src/client.rs`](https://github.com/virolea/lintus/blob/HEAD/crates/jev/src/client.rs) |
| [live-jev-okinaaudio](https://kydlikebtc.github.io/awesome-jev/?lang=en#live-jev-okinaaudio) | `project` | ★10+ | Control Ableton Live with one short sentence (Japanese / English). Summon with ⌘⇧Space, type or dictate, done. | `upstream-description` | [`daemon.py`](https://github.com/okinaaudio/live-jev/blob/HEAD/daemon.py) |
| [loki](https://kydlikebtc.github.io/awesome-jev/?lang=en#loki) | `project` | ★10+ | The agent that evolves with you 𖤍 | `upstream-description` | [`agent/typesafe_client.py`](https://github.com/wundercorp/loki/blob/HEAD/agent/typesafe_client.py) |
| [milvus-model](https://kydlikebtc.github.io/awesome-jev/?lang=en#milvus-model) | `integration` | ★10+ | A library integrating embedding and reranker models from OpenAI, SentenceTransformers etc for semantic search in vector database. | `upstream-description` | [`src/pymilvus/model/reranker/jev.py`](https://github.com/milvus-io/milvus-model/blob/HEAD/src/pymilvus/model/reranker/jev.py) |
| [pi-verdict](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-verdict) | `plugin` | ★10+ | A minimal permission gate for Pi in the style of Claude Code's auto mode | `upstream-description` | [`extensions/jev-adapter.ts`](https://github.com/jesset/pi-verdict/blob/HEAD/extensions/jev-adapter.ts) |
| [plugins](https://kydlikebtc.github.io/awesome-jev/?lang=en#plugins) | `plugin` | ★10+ | Official curated plugins for Cline CLI and extensions | `upstream-description` | [`plugins/jev-browser/src/jev-model.ts`](https://github.com/cline/plugins/blob/HEAD/plugins/jev-browser/src/jev-model.ts) |
| [ruby-llm-typesafe-provider](https://kydlikebtc.github.io/awesome-jev/?lang=en#ruby-llm-typesafe-provider) | `integration` | ★10+ | A structured-output provider for a Ruby LLM library. | — | [`lib/ruby_llm/providers/typesafe.rb`](https://github.com/kieranklaassen/ruby_llm-typesafe/blob/HEAD/lib/ruby_llm/providers/typesafe.rb) |
| [snifftest](https://kydlikebtc.github.io/awesome-jev/?lang=en#snifftest) | `project` | ★10+ | A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model. | `upstream-description` | [`src/jev.ts`](https://github.com/DanRWilloughby/snifftest/blob/HEAD/src/jev.ts) |
| [st-jeved](https://kydlikebtc.github.io/awesome-jev/?lang=en#st-jeved) | `plugin` | ★10+ | SillyTavern extension that measures each reply and instructs the narrator only when a rule matches. | `upstream-description` | [`src/classifier.js`](https://github.com/mossyfield/ST-jeved/blob/HEAD/src/classifier.js) |
| [taste-lint](https://kydlikebtc.github.io/awesome-jev/?lang=en#taste-lint) | `project` | ★10+ | Catch AI slop before you ship. | `upstream-description` | [`src/map/jev.ts`](https://github.com/mblode/taste-lint/blob/HEAD/src/map/jev.ts) |
| [tsai-sc](https://kydlikebtc.github.io/awesome-jev/?lang=en#tsai-sc) | `project` | ★10+ | Drives a 1990s real-time strategy game through keyboard and mouse, recording the action probabilities. | — | [`tsai_sc/typesafe.py`](https://github.com/phyous/tsai-sc/blob/HEAD/tsai_sc/typesafe.py) |
| [typesafe-adblock](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-adblock) | `project` | ★10+ | A Chrome extension that asks whether a DOM element is an advert. | — | [`src/typesafe.js`](https://github.com/realZachi/typesafe-adblock/blob/HEAD/src/typesafe.js) |
| [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-benchmark) | `benchmark` | ★10+ | A gateway that mimics the structured-output shape, used to benchmark against it. | — | [`packages/demos/lib/jev.ts`](https://github.com/iammrduncan/inference-benchmarks/blob/HEAD/packages/demos/lib/jev.ts) |
| [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) | `benchmark` | ★10+ | A WebMCP benchmark, measures WebMCP against other browser-agent interfaces. | `upstream-description` | [`experiments/jev/frozen/arms/decision-providers.mjs`](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/experiments/jev/frozen/arms/decision-providers.mjs) |
| [functions](https://kydlikebtc.github.io/awesome-jev/?lang=en#functions) | `project` |  | 👷 Cloudflare Workers for the TrainLCD mobile app. | `upstream-description` | [`src/cli/typesafe-triage-spike.ts`](https://github.com/TrainLCD/Functions/blob/HEAD/src/cli/typesafe-triage-spike.ts) |
| [git-jev-stage](https://kydlikebtc.github.io/awesome-jev/?lang=en#git-jev-stage) | `project` |  | Select Git changes for staging with a plain-language description. | `upstream-description` | [`src/core/jevClient.ts`](https://github.com/ibrahemid/git-jev-stage/blob/HEAD/src/core/jevClient.ts) |
| [hush](https://kydlikebtc.github.io/awesome-jev/?lang=en#hush) | `project` |  | Issue triage that stays quiet when it isn't sure. Calibrated labels, spam and duplicate detection — with abstention. | `upstream-description` | [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js) |
| [jackalope](https://kydlikebtc.github.io/awesome-jev/?lang=en#jackalope) | `project` |  | A desktop workspace for coding agents, parallel Git worktrees, and code review. | `upstream-description` | [`apps/desktop/src-tauri/src/commands/jev.rs`](https://github.com/Jackalope-Dev/jackalope/blob/HEAD/apps/desktop/src-tauri/src/commands/jev.rs) |
| [jev-codex-bridge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-codex-bridge) | `plugin` |  | Model and reasoning routing for Codex Desktop and CLI, with a Windows service and validated updates | `upstream-description-stale` | [`src/router.mjs`](https://github.com/ansidium/jev-codex-bridge/blob/HEAD/src/router.mjs) |
| [jev-information-extraction](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-information-extraction) | `project` |  | Parsing the PDF and extracting the relevant information | `upstream-description` | [`backend/main.py`](https://github.com/abhishekmamdapure/jev-information-extraction/blob/HEAD/backend/main.py) |
| [jev-model-tokengate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-model-tokengate) | `project` |  | An OpenAI-compatible proxy that sits between your LLM and your users. It evaluates each sliding window of tokens while the response is still streaming and cuts the stream before a violating token can reach the screen. | `upstream-description` | [`evaluator.js`](https://github.com/Thanh-Mathieu95/jev-model-tokengate/blob/HEAD/evaluator.js) |
| [jev-paper-judge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-paper-judge) | `project` |  | Feedback on your paper in seconds. | `upstream-description` | [`scripts/lib/typesafe.mjs`](https://github.com/JacobLinCool/jev-paper-judge/blob/HEAD/scripts/lib/typesafe.mjs) |
| [jev-skip](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skip) | `project` |  | Skips video sponsor segments by reading the captions and deciding at watch time. | — | [`lib/jev.ts`](https://github.com/valentynkit/jev-skip/blob/HEAD/lib/jev.ts) |
| [jevprune](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevprune) | `project` |  | Filter command output for coding agents using a task description. | `upstream-description` | [`src/typesafe-client.ts`](https://github.com/ibrahemid/jevprune/blob/HEAD/src/typesafe-client.ts) |
| [jlink](https://kydlikebtc.github.io/awesome-jev/?lang=en#jlink) | `project` |  | Record linkage for economists: write the match rule in plain English, get a probability per pair, audit it, cite it. Python, CLI, Stata and R. | `upstream-description` | [`bench/local_models.py`](https://github.com/keltokhy/jlink/blob/HEAD/bench/local_models.py) |
| [jselect](https://kydlikebtc.github.io/awesome-jev/?lang=en#jselect) | `project` |  | Useful evidence for your AI, within a token budget. A fast, source-linked context selector for files, records, and agents. | `upstream-description` | [`src/jselect/judge.py`](https://github.com/keltokhy/jselect/blob/HEAD/src/jselect/judge.py) |
| [labs](https://kydlikebtc.github.io/awesome-jev/?lang=en#labs) | `project` |  | Small, independent projects for experiments, research, and investigations. | `upstream-description` | [`2026/09/17/typesafe-jev-evaluation/client.py`](https://github.com/kiarina/labs/blob/HEAD/2026/09/17/typesafe-jev-evaluation/client.py) |
| [langchain-skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#langchain-skill-router) | `plugin` |  | Per-turn skill selection for LangChain and deepagents agents: a fast judge picks the few skills a turn needs, so a catalog of hundreds stays out of the prompt. | `upstream-description` | [`src/langchain_skill_router/providers/jev.py`](https://github.com/deyna256/langchain-skill-router/blob/HEAD/src/langchain_skill_router/providers/jev.py) |
| [nachalnik](https://kydlikebtc.github.io/awesome-jev/?lang=en#nachalnik) | `plugin` |  | A transparent agent runtime in Rust: context, tools, permissions and requests as explicit state. Plus an MCP bridge and a terminal agent. | `upstream-description` | [`kamchatka/src/args.rs`](https://github.com/ljedrz/nachalnik/blob/HEAD/kamchatka/src/args.rs) |
| [openpoke-meets-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#openpoke-meets-jev) | `project` |  | Open source implementation of Poke | `upstream-description` | [`server/jev/client.py`](https://github.com/0xShin0221/openpoke-meets-jev/blob/HEAD/server/jev/client.py) |
| [pi-agent-foreman](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-agent-foreman) | `project` |  | Send Pi agents back to work when they stop before the job is done. | `upstream-description` | [`src/typesafe.ts`](https://github.com/alexshpunt/pi-agent-foreman/blob/HEAD/src/typesafe.ts) |
| [progressgate](https://kydlikebtc.github.io/awesome-jev/?lang=en#progressgate) | `project` |  | Detect semantic stagnation in AI agent loops | `upstream-description` | [`experiments/jev-client.ts`](https://github.com/AshutoshVJTI/progressgate/blob/HEAD/experiments/jev-client.ts) |
| [robo-harness](https://kydlikebtc.github.io/awesome-jev/?lang=en#robo-harness) | `project` |  | SO-101 robot-arm agent workbench: Bun/Effect coordinator, React workbench, Python LeRobot motor owner | `upstream-description` | [`apps/server/src/decision/jev.ts`](https://github.com/grmkris/robo-harness/blob/HEAD/apps/server/src/decision/jev.ts) |
| [s1-ruby](https://kydlikebtc.github.io/awesome-jev/?lang=en#s1-ruby) | `sdk` |  | Makes S1-model 'measurement' (and the collapse that follows it) a Ruby primitive. | `upstream-description` | [`lib/s1/providers/typesafe.rb`](https://github.com/innocentdiaz/s1_ruby/blob/HEAD/lib/s1/providers/typesafe.rb) |
| [secondlayer](https://kydlikebtc.github.io/awesome-jev/?lang=en#secondlayer) | `project` |  | Decoded Stacks data in your own database. Self-hosted. | `upstream-description-stale` | [`scripts/ops/jev-fault-triage.ts`](https://github.com/ryanwaits/secondlayer/blob/HEAD/scripts/ops/jev-fault-triage.ts) |
| [semantic-assert](https://kydlikebtc.github.io/awesome-jev/?lang=en#semantic-assert) | `sdk` |  | Testing lib for asserting the real requirement. | `upstream-description` | [`packages/semantic-assert-typesafe/src/client.ts`](https://github.com/mondaychen/semantic-assert/blob/HEAD/packages/semantic-assert-typesafe/src/client.ts) |
| [tiab-review-plugin](https://kydlikebtc.github.io/awesome-jev/?lang=en#tiab-review-plugin) | `plugin` |  | A Chrome extension that speeds up title-and-abstract screening for systematic reviews, published on the Chrome Web Store. | — | [`src/lib/providers/typesafe.ts`](https://github.com/youkiti/tiab-review-plugin/blob/HEAD/src/lib/providers/typesafe.ts) |
| [tripwire](https://kydlikebtc.github.io/awesome-jev/?lang=en#tripwire) | `integration` |  | Judge every LLM response before the user sees it. AI SDK middleware and OpenAI-compatible proxy. | `upstream-description` | [`src/judge/jev.ts`](https://github.com/noelzappy/tripwire/blob/HEAD/src/judge/jev.ts) |
| [typesafe-sdk-elixir](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-sdk-elixir) | `sdk` |  | An Elixir port of the official SDK. | — | [`codegen/typesafe_sdk/codegen/source/openapi.ex`](https://github.com/nshkrdotcom/typesafe_sdk/blob/HEAD/codegen/typesafe_sdk/codegen/source/openapi.ex) |
| [your-signal](https://kydlikebtc.github.io/awesome-jev/?lang=en#your-signal) | `plugin` |  | Open-source BYOK Chrome extension for personal, reversible X timeline filters. | `upstream-description` | [`eval/run.py`](https://github.com/MithrilMan/your-signal/blob/HEAD/eval/run.py) |

<a id="measurement-unread"></a>

## Benchmark measurements nobody has read against the report · 人和模型都还没有对照报告读过的基准测试测量

The row's `measurement` has neither `read_on` nor `model_read_on`: a script or a model filled in its fields from the author's README or results, and nobody has recorded reading them since. The fields index what the author reports; the direction is the author's own conclusion (author-stated, not reproduced here). The fields first filled in on 2026-09-28 were read by a model; [method.md](method.md) says how. [benchmarks.md](benchmarks.md) shows every field.

该行的 `measurement` 既没有 `read_on` 也没有 `model_read_on`：字段由脚本或模型根据作者的 README 或结果填写，此后没有人或模型记录过核读。这些字段索引的是作者报告的内容；结论方向是作者本人的结论（作者自述，未经本仓库复现）。2026-09-28 首次填写的字段由模型阅读得出，做法见 [method.md](method.md)。全部字段见 [benchmarks.zh-CN.md](benchmarks.zh-CN.md)。

To take a row off, read the author's report (the row's link, or `measurement.report`) against every field, correct or remove any the report does not state, and set `measurement.read_on` to the day you read it (see the `measurement` field rules in [CONTRIBUTING](../CONTRIBUTING.md#field-rules)). A model that reads it sets `measurement.model_read_on` instead, which moves the row to [Read or written by a model](#model-read).

移出方法：对照作者的报告（该行的链接，或 `measurement.report`）逐项核读，改正或删去报告里没有说的字段，再把 `measurement.read_on` 设为核读当天（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `measurement` 的字段规则）。由模型核读时改写 `measurement.model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。

| Row · 行 | Stars · 星标 | Direction (author-stated, not reproduced here) · 结论方向（作者自述，未经本仓库复现） | Report · 报告 |
| --- | --- | --- | --- |
| [hermes-agent-jev-evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-agent-jev-evaluation) | ★100k+ | `unfavourable` | [`https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/results/SCORECARD-2026-09-19-jev.md`](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/results/SCORECARD-2026-09-19-jev.md) |
| [worldmonitor-shadow-mode](https://kydlikebtc.github.io/awesome-jev/?lang=en#worldmonitor-shadow-mode) | ★10k+ | `unfavourable` | [`https://github.com/koala73/worldmonitor/pull/8326`](https://github.com/koala73/worldmonitor/pull/8326) |
| [no-mistakes-review-context](https://kydlikebtc.github.io/awesome-jev/?lang=en#no-mistakes-review-context) | ★1k+ | `unfavourable` | [`https://github.com/kunchenguid/no-mistakes/blob/HEAD/benchmarks/issue-1055/results.md`](https://github.com/kunchenguid/no-mistakes/blob/HEAD/benchmarks/issue-1055/results.md) |
| [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=en#hippo-memory) | ★100+ | `mixed` | [`https://github.com/kitfunso/hippo-memory/blob/HEAD/docs/evals/2026-09-19-jev-reranker.md`](https://github.com/kitfunso/hippo-memory/blob/HEAD/docs/evals/2026-09-19-jev-reranker.md) |
| [jev-arena](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-arena) | ★100+ | — | [`https://github.com/NanmiCoder/jev-arena/blob/HEAD/audit/accuracy-0919-124001/report.md`](https://github.com/NanmiCoder/jev-arena/blob/HEAD/audit/accuracy-0919-124001/report.md) |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) | ★100+ | — | [`https://github.com/fstandhartinger/jevbench`](https://github.com/fstandhartinger/jevbench) |
| [ahastudio-til-jev-probing](https://kydlikebtc.github.io/awesome-jev/?lang=en#ahastudio-til-jev-probing) | ★100+ | — | [`https://github.com/ahastudio/til/blob/HEAD/jev/architecture-unmasked.md`](https://github.com/ahastudio/til/blob/HEAD/jev/architecture-unmasked.md) |
| [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) | ★10+ | `mixed` | [`https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/results/reports/btzsc-pilot-v1.md`](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/results/reports/btzsc-pilot-v1.md) |
| [jev-capability-atlas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-capability-atlas) | ★10+ | `mixed` | [`https://github.com/Zaious/jev-capability-atlas`](https://github.com/Zaious/jev-capability-atlas) |
| [jev-dspy-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-dspy-lab) | ★10+ | — | [`https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/evidence/live/jev-latest/benchmark.md`](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/evidence/live/jev-latest/benchmark.md) |
| [jev-rag-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rag-benchmark) | ★10+ | `favourable` | [`https://github.com/erendikmenn/jev-rag-benchmark`](https://github.com/erendikmenn/jev-rag-benchmark) |
| [jev-rerank-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rerank-bench) | ★10+ | `mixed` | [`https://github.com/anessbelbati/jev-rerank-bench`](https://github.com/anessbelbati/jev-rerank-bench) |
| [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robot-control) | ★10+ | `inconclusive` | [`https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/docs/RESULTS.md`](https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/docs/RESULTS.md) |
| [jev-search-rerank-eval](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-search-rerank-eval) | ★10+ | `mixed` | [`https://github.com/zhuyansen/jev-search-rerank-eval`](https://github.com/zhuyansen/jev-search-rerank-eval) |
| [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#pdf-race) | ★10+ | — | [`https://github.com/goodrahstar/pdf-race`](https://github.com/goodrahstar/pdf-race) |
| [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=en#smartmoney-cub) | ★10+ | `mixed` | [`https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/assets/benchmark/run.json`](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/assets/benchmark/run.json) |
| [typesafe-ai-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-benchmark) | ★10+ | `mixed` | [`https://github.com/iammrduncan/typesafe-ai-benchmark/blob/HEAD/docs/benchmarks/README.md`](https://github.com/iammrduncan/typesafe-ai-benchmark/blob/HEAD/docs/benchmarks/README.md) |
| [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) | ★10+ | — | [`https://github.com/nekuda-ai/WindTunnel/blob/HEAD/results/2026-09-18-jev-mercury/PROVENANCE.md`](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/results/2026-09-18-jev-mercury/PROVENANCE.md) |
| [decision-models-as-guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) |  | — | [`https://dm-as-guardrails.raxitlabs.com`](https://dm-as-guardrails.raxitlabs.com) |
| [jev-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmark) |  | `mixed` | [`https://github.com/wondertwins/jev-benchmark`](https://github.com/wondertwins/jev-benchmark) |
| [jev-code-review-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-code-review-benchmark) |  | `mixed` | [`https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/docs/results/README.md`](https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/docs/results/README.md) |
| [jev-korean-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-korean-benchmark) |  | `mixed` | [`https://github.com/mahlernim/jev-korean-benchmark`](https://github.com/mahlernim/jev-korean-benchmark) |
| [jev-little-airways](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-little-airways) |  | — | [`https://github.com/lbotinelly/jev-little-airways`](https://github.com/lbotinelly/jev-little-airways) |
| [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) |  | `mixed` | [`https://github.com/scienthoon/jev-ood-calibration`](https://github.com/scienthoon/jev-ood-calibration) |
| [jev-phishing-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-phishing-bench) |  | `mixed` | [`https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/results/report.md`](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/results/report.md) |
| [jevbench-human-disagreement](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench-human-disagreement) |  | `mixed` | [`https://doi.org/10.5281/zenodo.22971491`](https://doi.org/10.5281/zenodo.22971491) |
| [decisionmodelhub-support-routing](https://kydlikebtc.github.io/awesome-jev/?lang=en#decisionmodelhub-support-routing) |  | — | [`https://decisionmodelhub.com/benchmarks/support-routing`](https://decisionmodelhub.com/benchmarks/support-routing) |

<a id="wire-unread"></a>

## Interfaces of alternatives nobody has read in the cited files · 人和模型都还没有在所引文件中读过的替代实现接口

The row's `wire` record cites a file with neither `read_on` nor `model_read_on`: a script or a model read the project's code for its route, its yes/no spelling, where its answers come from and whether it calls Jev to compare, and no person has checked since. Every value is backed by a string in a cited file, which the weekly `claims` run re-reads; whether the strings mean what the fields say is the reading. The records first filled in on 2026-09-28 were read by a model; [method.md](method.md) says how. [compatibility.md](compatibility.md#7-compatible-interfaces-that-are-not-jev) shows every field.

该行的 `wire` 记录所引文件中有的既没有 `read_on` 也没有 `model_read_on`：由脚本或模型阅读项目代码，得出其路由、是/否题型的写法、答案来自哪里、是否调用 Jev 做对比，此后没有人核对过。每个值都有所引文件中的一段字符串作依据，每周的 `claims` 任务会重读这些字符串；这些字符串是否真如字段所说，则要靠人读。2026-09-28 首次填写的记录由模型阅读得出，做法见 [method.md](method.md)。全部字段见 [compatibility.md](compatibility.md#7-compatible-interfaces-that-are-not-jev)。

To take a row off, read each file in `wire.source` against every field, correct or remove any field the files do not show, and set `read_on` on each source to the day you read it (see the `wire` field rules in [CONTRIBUTING](../CONTRIBUTING.md#field-rules)). A model that reads them sets `model_read_on` instead, which moves the row to [Read or written by a model](#model-read).

移出方法：对照 `wire.source` 中的每个文件逐项核读，改正或删去文件里看不出的字段，再把每个来源的 `read_on` 设为核读当天（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `wire` 的字段规则）。由模型核读时改写 `model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。

| Row · 行 | Stars · 星标 | Weights · 权重 | Cited files · 引用的文件 |
| --- | --- | --- | --- |
| [laya-nandhakishorm](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-nandhakishorm) | ★10k+ | `open` | `laya/serve.py` `laya/agent.py` `laya/router.py` `research/benchmarks/feishu_zh/run.py` |
| [decider](https://kydlikebtc.github.io/awesome-jev/?lang=en#decider) | ★1k+ | `open` | `decider/serve.py` `decider/systemone.py` `README.md` |
| [jaredpalmer-kev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jaredpalmer-kev) | ★1k+ | `open` | `kev/serve.py` `kev/api.py` `playground/scripts/jev-evaluate.mjs` |
| [nanojev](https://kydlikebtc.github.io/awesome-jev/?lang=en#nanojev) | ★1k+ | `open` | `scripts/serve_decisions.py` `scripts/predict_toy_decisions.py` `scripts/jev_probe.mjs` |
| [jeff](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeff) | ★100+ | `open` | `src/jeff/server/app.py` `src/jeff/core/schemas.py` `src/jeff/server/config.py` `bench/jevbench.py` |
| [localjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#localjev) | ★100+ | `open` | `src/server.ts` `src/types.ts` `src/config.ts` |
| [open-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-jev) | ★100+ | `open` | `openjev/server.py` `openjev/systemone.py` `openjev/scorer.py` |
| [open-jev-zefan-cai](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-jev-zefan-cai) | ★100+ | `open` | `jev/server.py` `jev/api.py` `README.md` |
| [openjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#openjev) | ★100+ | `open` | `openjev/api.py` `openjev/engine.py` `openjev/config.py` |
| [openjev-siliconlabai](https://kydlikebtc.github.io/awesome-jev/?lang=en#openjev-siliconlabai) | ★100+ | `proxy` | `server/index.ts` `src/lib/evaluate.ts` |
| [openjev-sglang](https://kydlikebtc.github.io/awesome-jev/?lang=en#openjev-sglang) | ★100+ | `open` | `src/openjev/api.py` `src/openjev/models.py` `src/openjev/defaults.py` `evals/boolq.py` |
| [rizzo-flow](https://kydlikebtc.github.io/awesome-jev/?lang=en#rizzo-flow) | ★100+ | `open` | `src/rizzo_flow/api.py` `src/rizzo_flow/compat.py` `src/rizzo_flow/config.py` |
| [simple-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#simple-jev) | ★100+ | `open` | `hf-server/hf_server.py` `eval/benchmarks/jev-1.13/2026-09-20/RUN.md` |
| [von](https://kydlikebtc.github.io/awesome-jev/?lang=en#von) | ★100+ | `open` | `src/von/server.py` `src/von/types.py` `src/von/backends/option_marker_backend.py` |

<a id="thresholds-unread"></a>

## Thresholds nobody has read in the cited file · 人和模型都还没有在所引文件中读过的阈值

The row's `observed_thresholds` has an item with neither `read_on` nor `model_read_on`: a script or a model read the cited file for the constants it compares a Jev answer with, and no person has checked since. Each item's `source` is a string in `evidence.matched`, which the weekly `claims` run re-reads, and its `value` is written in it; which answer the constant is compared with, and what the code does on each side, is the reading. They are what the project chose, not recommendations. The thresholds first recorded on 2026-09-28 were read by a model; [method.md](method.md) says how.

该行的 `observed_thresholds` 中有条目既没有 `read_on` 也没有 `model_read_on`：由脚本或模型阅读所引文件，找出其中与 Jev 答案比较的常量，此后没有人核对过。每个条目的 `source` 是 `evidence.matched` 中的一段字符串，每周的 `claims` 任务会重读它，`value` 就写在其中；常量与哪个答案比较、两侧代码各做什么，则要靠人读。这些是该项目自己的选择，不是推荐值。2026-09-28 首次记录的阈值由模型阅读得出，做法见 [method.md](method.md)。

To take a row off, read the cited file against every item: correct `question_type`, `compares` and `decision`, remove any item that is not a decision on a Jev answer, and set each item's `read_on` to the day you read it (see the `observed_thresholds` field rules in [CONTRIBUTING](../CONTRIBUTING.md#field-rules)). A model that reads them sets `model_read_on` instead, which moves the row to [Read or written by a model](#model-read).

移出方法：对照所引文件逐条核读，改正 `question_type`、`compares` 和 `decision`，删去不是基于 Jev 答案做决定的条目，再把每个条目的 `read_on` 设为核读当天（见 [CONTRIBUTING](../CONTRIBUTING.md#field-rules) 中关于 `observed_thresholds` 的字段规则）。由模型核读时改写 `model_read_on`，该行会移到[模型读过或撰写](#model-read)一节。

| Row · 行 | Stars · 星标 | Thresholds · 阈值 | Cited file · 引用的文件 |
| --- | --- | --- | --- |
| [classifier-dev](https://kydlikebtc.github.io/awesome-jev/?lang=en#classifier-dev) | ★100+ | `noul probability 0.7` | [`src/jev.ts`](https://github.com/mrmps/classifier-dev/blob/HEAD/src/jev.ts) |
| [jev-social](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-social) | ★100+ | `choice confidence 0.35` | [`src/actions.js`](https://github.com/socai-io/jev-social/blob/HEAD/src/actions.js) |
| [macbrow](https://kydlikebtc.github.io/awesome-jev/?lang=en#macbrow) | ★100+ | `choice confidence 0.6` | [`macbrow/generator.py`](https://github.com/timpratim/macbrow/blob/HEAD/macbrow/generator.py) |
| [neo4jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#neo4jev) | ★100+ | `choice probability 0.05` `noul probability 0.5` | [`src/neo4jev/navigator.py`](https://github.com/jexp/neo4jev/blob/HEAD/src/neo4jev/navigator.py) |
| [third-hand](https://kydlikebtc.github.io/awesome-jev/?lang=en#third-hand) | ★100+ | `noul probability 0.7` | [`Sources/ThirdHand/JevClient.swift`](https://github.com/shhivv/third-hand/blob/HEAD/Sources/ThirdHand/JevClient.swift) |
| [unclutter](https://kydlikebtc.github.io/awesome-jev/?lang=en#unclutter) | ★100+ | `choice confidence 0.9` | [`lib/jev.ts`](https://github.com/kitze/unclutter/blob/HEAD/lib/jev.ts) |
| [vexjoy-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#vexjoy-agent) | ★100+ | `noul probability 0.5` `noul probability 0.35` | [`plugins/jev-auto-compact/hooks/jev-auto-compact.mjs`](https://github.com/notque/vexjoy-agent/blob/HEAD/plugins/jev-auto-compact/hooks/jev-auto-compact.mjs) |
| [ask-jev-skill](https://kydlikebtc.github.io/awesome-jev/?lang=en#ask-jev-skill) | ★10+ | `noul probability 0.7` `noul probability 0.3` `choice confidence 0.6` | [`scripts/askjev.py`](https://github.com/shantanugoel/ask-jev-skill/blob/HEAD/scripts/askjev.py) |
| [cmd-mod-jev-nudge](https://kydlikebtc.github.io/awesome-jev/?lang=en#cmd-mod-jev-nudge) | ★10+ | `noul probability 0.5` | [`src/protocol.ts`](https://github.com/CommandCodeAI/cmd-mod-jev-nudge/blob/HEAD/src/protocol.ts) |
| [hono-jev-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#hono-jev-router) | ★10+ | `noul probability 0.5` | [`src/index.ts`](https://github.com/yusukebe/hono-jev-router/blob/HEAD/src/index.ts) |
| [jev-belay](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-belay) | ★10+ | `noul probability 0.7` `noul probability 0.5` `choice confidence 0.4` | [`belay.mjs`](https://github.com/valentynkit/jev-belay/blob/HEAD/belay.mjs) |
| [jevernetes](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevernetes) | ★10+ | `choice confidence 0.7` | [`jevernetes/jev.py`](https://github.com/sunil-sadasivan/jevernetes/blob/HEAD/jevernetes/jev.py) |
| [jevgpt](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgpt) | ★10+ | `noul probability 0.9` | [`src/jevgpt/sampler.py`](https://github.com/Bewinxed/jevgpt/blob/HEAD/src/jevgpt/sampler.py) |
| [alphaoptimizer](https://kydlikebtc.github.io/awesome-jev/?lang=en#alphaoptimizer) |  | `noul probability 0.8` `noul probability 0.2` | [`dist/src/providers/jev.js`](https://github.com/alpha-tales/alphaoptimizer/blob/HEAD/dist/src/providers/jev.js) |
| [ask-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#ask-jev) |  | `choice confidence 0.85` | [`scripts/jev_context.py`](https://github.com/logicrw/ask-jev/blob/HEAD/scripts/jev_context.py) |
| [browser-use-olympics](https://kydlikebtc.github.io/awesome-jev/?lang=en#browser-use-olympics) |  | `noul probability 0.85` `noul probability 0.7` | [`almond-fastloop.mjs`](https://github.com/eriestra/browser-use-olympics/blob/HEAD/almond-fastloop.mjs) |
| [codex-jev-router-suenot](https://kydlikebtc.github.io/awesome-jev/?lang=en#codex-jev-router-suenot) |  | `noul probability 0.8` `choice confidence 0.75` | [`src/router.mjs`](https://github.com/suenot/codex-jev-router/blob/HEAD/src/router.mjs) |
| [construct-auto-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#construct-auto-classifier) |  | `noul probability 0.7` `choice confidence 0.6` `choice probability 0.6` | [`src/classifier/jev-client.ts`](https://github.com/godspede/construct-auto-classifier/blob/HEAD/src/classifier/jev-client.ts) |
| [jev-boe-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-boe-demo) |  | `noul probability 0.6` `score score 2` | [`pipeline/analyze.ts`](https://github.com/Tatuck/jev-boe-demo/blob/HEAD/pipeline/analyze.ts) |
| [jev-in-codex](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-in-codex) |  | `choice confidence 0.8` | [`src/labelling.ts`](https://github.com/teempai/jev-in-codex/blob/HEAD/src/labelling.ts) |
| [jev-mcp-spring](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-spring) |  | `noul probability 0.7` `noul probability 0.3` | [`src/main/java/dev/ashfaqbs/jevmcp/tools/JevTools.java`](https://github.com/Ashfaqbs/jev-mcp-spring/blob/HEAD/src/main/java/dev/ashfaqbs/jevmcp/tools/JevTools.java) |
| [jev-mobile-xinwang-nwpu](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mobile-xinwang-nwpu) |  | `noul probability 0.5` | [`jev_mobile/model.py`](https://github.com/xinwang-nwpu/jev-mobile/blob/HEAD/jev_mobile/model.py) |
| [jev-robotics-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robotics-demo) |  | `noul probability 0.9` | [`jev_agent.py`](https://github.com/FazalAAli/jev-robotics-demo/blob/HEAD/jev_agent.py) |
| [jev-skill-scout](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-scout) |  | `noul probability 0.3` | [`lib/scout.js`](https://github.com/karanb192/jev-skill-scout/blob/HEAD/lib/scout.js) |
| [jev-tetris-machinelearning-nerd](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tetris-machinelearning-nerd) |  | `noul probability 0.75` `score score 2` `score confidence 0.55` | [`courtroom.py`](https://github.com/MachineLearning-Nerd/jev-tetris/blob/HEAD/courtroom.py) |
| [jev-voice-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice-control) |  | `noul probability 0.7` `choice confidence 0.3` | [`Sources/JevVoice/Agent/JevStepPlanner.swift`](https://github.com/chris-wozniczek/jev-voice-control/blob/HEAD/Sources/JevVoice/Agent/JevStepPlanner.swift) |
| [jevatar](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevatar) |  | `choice confidence 0.4` | [`server.ts`](https://github.com/AppChainAI/Jevatar/blob/HEAD/server.ts) |
| [jevcumber](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevcumber) |  | `choice confidence 0.75` | [`src/resolver.ts`](https://github.com/RubyBrewsday/jevcumber/blob/HEAD/src/resolver.ts) |
| [jevpdf](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevpdf) |  | `noul probability 0.55` `noul probability 0.3` | [`src/lib/jev-config.ts`](https://github.com/kylemclaren/jevpdf/blob/HEAD/src/lib/jev-config.ts) |
| [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) |  | `choice probability 0.8` `noul probability 0.9` `noul probability 0.55` | [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts) |
| [river-run-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#river-run-typesafe) |  | `noul probability 0.5` | [`typesafe_pilot/pilot.py`](https://github.com/ashaazami/river-run-typesafe/blob/HEAD/typesafe_pilot/pilot.py) |

<a id="model-read"></a>

## Read or written by a model, not yet checked by a person · 模型读过或撰写、尚无人核对

Since 2026-10-24 a model's reading is recorded apart from a person's: `patterns_model_read_on`, and `model_read_on` on the call site (`evidence`), a benchmark's `measurement`, each file of an alternative's `wire` and each threshold; a summary a model wrote is labelled `model-written`, and `question_types` on a row whose call site only a model has read is that model's reading too. Every surface shows these as a model's work, never as a person's. A row here left the lists above because a model read it, not because a person agreed: a model can misread a file in ways a person would not, so these rows are for a person to check, all of them or a sample.

自 2026-10-24 起，模型的阅读与人的阅读分开记录：`patterns_model_read_on`，以及调用点（`evidence`）、基准测试的 `measurement`、替代实现 `wire` 的每个文件和每个阈值上的 `model_read_on`；模型撰写的摘要标为 `model-written`；调用点只有模型读过的行，其 `question_types` 也是模型的阅读。所有页面都把这些显示为模型的工作，从不当作人的。这里的行离开上面各节，是因为模型读过，而不是因为有人认可：模型可能以人不会的方式读错文件，所以这些行留给人核对，全部或抽查。

To take a row off, check what the model read or wrote, correct anything it got wrong, and record your own reading: `patterns_reviewed`, `evidence.read_on` (after checking `question_types` against the call site), `measurement.read_on`, or `read_on` on each file or threshold; keep or rewrite a summary and set `summary_source` to `curated`. The model's date may stay beside yours: a person's reading supersedes it everywhere it is shown.

移出方法：核对模型读过或写下的内容，改正它弄错的地方，再记下你自己的阅读：`patterns_reviewed`、`evidence.read_on`（先对照调用点核对 `question_types`）、`measurement.read_on`，或每个文件、每个阈值上的 `read_on`；摘要则保留或改写，并把 `summary_source` 设为 `curated`。模型的日期可以留在你的旁边：凡是显示日期的地方，人的阅读都优先。

| Row · 行 | Stars · 星标 | A model's work, unchecked · 模型的工作（未经核对） |
| --- | --- | --- |
| [langchain](https://kydlikebtc.github.io/awesome-jev/?lang=en#langchain) | ★100k+ | `summary` |
| [ai-hedge-fund](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai-hedge-fund) | ★10k+ | `summary` |
| [laya-nandhakishorm](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-nandhakishorm) | ★10k+ | `summary` |
| [litellm](https://kydlikebtc.github.io/awesome-jev/?lang=en#litellm) | ★10k+ | `summary` |
| [pydantic-ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#pydantic-ai) | ★10k+ | `summary` |
| [ax](https://kydlikebtc.github.io/awesome-jev/?lang=en#ax) | ★1k+ | `summary` |
| [deep-searcher](https://kydlikebtc.github.io/awesome-jev/?lang=en#deep-searcher) | ★1k+ | `summary` |
| [gptcache](https://kydlikebtc.github.io/awesome-jev/?lang=en#gptcache) | ★1k+ | `summary` |
| [latitude-llm](https://kydlikebtc.github.io/awesome-jev/?lang=en#latitude-llm) | ★1k+ | `summary` |
| [laya-mlx](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-mlx) | ★1k+ | `summary` |
| [memsearch](https://kydlikebtc.github.io/awesome-jev/?lang=en#memsearch) | ★1k+ | `summary` |
| [nimble](https://kydlikebtc.github.io/awesome-jev/?lang=en#nimble) | ★1k+ | `summary` |
| [reticle](https://kydlikebtc.github.io/awesome-jev/?lang=en#reticle) | ★1k+ | `summary` |
| [shapeshift](https://kydlikebtc.github.io/awesome-jev/?lang=en#shapeshift) | ★1k+ | `summary` |
| [vellum-assistant](https://kydlikebtc.github.io/awesome-jev/?lang=en#vellum-assistant) | ★1k+ | `summary` |
| [abide](https://kydlikebtc.github.io/awesome-jev/?lang=en#abide) | ★100+ | `summary` |
| [agent-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-router) | ★100+ | `summary` |
| [aiavatarkit](https://kydlikebtc.github.io/awesome-jev/?lang=en#aiavatarkit) | ★100+ | `summary` |
| [astra-ares](https://kydlikebtc.github.io/awesome-jev/?lang=en#astra-ares) | ★100+ | `summary` |
| [atomic](https://kydlikebtc.github.io/awesome-jev/?lang=en#atomic) | ★100+ | `summary` |
| [classifier-dev](https://kydlikebtc.github.io/awesome-jev/?lang=en#classifier-dev) | ★100+ | `summary` |
| [compact-adviser](https://kydlikebtc.github.io/awesome-jev/?lang=en#compact-adviser) | ★100+ | `summary` |
| [crush-monitor](https://kydlikebtc.github.io/awesome-jev/?lang=en#crush-monitor) | ★100+ | `summary` |
| [dasheng](https://kydlikebtc.github.io/awesome-jev/?lang=en#dasheng) | ★100+ | `summary` |
| [distill](https://kydlikebtc.github.io/awesome-jev/?lang=en#distill) | ★100+ | `summary` |
| [djev](https://kydlikebtc.github.io/awesome-jev/?lang=en#djev) | ★100+ | `summary` |
| [djev-spark](https://kydlikebtc.github.io/awesome-jev/?lang=en#djev-spark) | ★100+ | `summary` |
| [docjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#docjev) | ★100+ | `summary` |
| [embodied-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#embodied-jev) | ★100+ | `summary` |
| [fastbrowse](https://kydlikebtc.github.io/awesome-jev/?lang=en#fastbrowse) | ★100+ | `summary` |
| [formanator](https://kydlikebtc.github.io/awesome-jev/?lang=en#formanator) | ★100+ | `summary` |
| [grok-bot-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#grok-bot-jev) | ★100+ | `summary` |
| [interlinked-cli](https://kydlikebtc.github.io/awesome-jev/?lang=en#interlinked-cli) | ★100+ | `summary` |
| [jeff](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeff) | ★100+ | `summary` |
| [jegrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jegrep) | ★100+ | `summary` |
| [jev-cobusgreyling](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cobusgreyling) | ★100+ | `summary` |
| [jev-as-a-judge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-as-a-judge) | ★100+ | `summary` |
| [jev-browser-ying-kai-liao](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browser-ying-kai-liao) | ★100+ | `summary` |
| [jev-dsh-decision](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-dsh-decision) | ★100+ | `summary` |
| [jev-forge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-forge) | ★100+ | `summary` |
| [jev-foundation-models](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-foundation-models) | ★100+ | `summary` |
| [jev-gateway](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-gateway) | ★100+ | `summary` |
| [jev-guard](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-guard) | ★100+ | `summary` |
| [jev-lint](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-lint) | ★100+ | `summary` |
| [jev-mem](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mem) | ★100+ | `summary` |
| [jev-semgrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-semgrep) | ★100+ | `summary` |
| [jev-seo-agricidaniel](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-seo-agricidaniel) | ★100+ | `summary` |
| [jev-trade](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trade) | ★100+ | `summary` |
| [jev-use-savka777](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-use-savka777) | ★100+ | `summary` |
| [jev-voice](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice) | ★100+ | `summary` |
| [jev-webmcp-extension](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-webmcp-extension) | ★100+ | `summary` |
| [jevals](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevals) | ★100+ | `summary` |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) | ★100+ | `summary` |
| [jevcore](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevcore) | ★100+ | `summary` |
| [jevgrep-nassim-arifette](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgrep-nassim-arifette) | ★100+ | `summary` |
| [jevharness](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevharness) | ★100+ | `summary` |
| [jevk5](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevk5) | ★100+ | `summary` |
| [jevmem](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmem) | ★100+ | `summary` |
| [jgrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jgrep) | ★100+ | `summary` |
| [kody](https://kydlikebtc.github.io/awesome-jev/?lang=en#kody) | ★100+ | `summary` |
| [laya](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya) | ★100+ | `summary` |
| [laya-server](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-server) | ★100+ | `summary` |
| [laya-ultrafast](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-ultrafast) | ★100+ | `summary` |
| [laya-vs-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-vs-jev) | ★100+ | `summary` |
| [macbrow](https://kydlikebtc.github.io/awesome-jev/?lang=en#macbrow) | ★100+ | `summary` |
| [omg-dev](https://kydlikebtc.github.io/awesome-jev/?lang=en#omg-dev) | ★100+ | `summary` |
| [open-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-jev) | ★100+ | `summary` |
| [openjev-siliconlabai](https://kydlikebtc.github.io/awesome-jev/?lang=en#openjev-siliconlabai) | ★100+ | `summary` |
| [orchestkit](https://kydlikebtc.github.io/awesome-jev/?lang=en#orchestkit) | ★100+ | `summary` |
| [pi-fabric](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-fabric) | ★100+ | `summary` |
| [req-llm](https://kydlikebtc.github.io/awesome-jev/?lang=en#req-llm) | ★100+ | `summary` |
| [rizzo-flow](https://kydlikebtc.github.io/awesome-jev/?lang=en#rizzo-flow) | ★100+ | `summary` |
| [runline](https://kydlikebtc.github.io/awesome-jev/?lang=en#runline) | ★100+ | `summary` |
| [stanley-code](https://kydlikebtc.github.io/awesome-jev/?lang=en#stanley-code) | ★100+ | `summary` |
| [system1-agents](https://kydlikebtc.github.io/awesome-jev/?lang=en#system1-agents) | ★100+ | `summary` |
| [taskuary](https://kydlikebtc.github.io/awesome-jev/?lang=en#taskuary) | ★100+ | `summary` |
| [tax-doc-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#tax-doc-classifier) | ★100+ | `summary` |
| [third-hand](https://kydlikebtc.github.io/awesome-jev/?lang=en#third-hand) | ★100+ | `summary` |
| [tiptour-macos](https://kydlikebtc.github.io/awesome-jev/?lang=en#tiptour-macos) | ★100+ | `summary` |
| [vector-graph-rag](https://kydlikebtc.github.io/awesome-jev/?lang=en#vector-graph-rag) | ★100+ | `summary` |
| [vexjoy-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#vexjoy-agent) | ★100+ | `summary` |
| [von](https://kydlikebtc.github.io/awesome-jev/?lang=en#von) | ★100+ | `summary` |
| [warrenduffer](https://kydlikebtc.github.io/awesome-jev/?lang=en#warrenduffer) | ★100+ | `summary` |
| [webctl](https://kydlikebtc.github.io/awesome-jev/?lang=en#webctl) | ★100+ | `summary` |
| [wrongstack](https://kydlikebtc.github.io/awesome-jev/?lang=en#wrongstack) | ★100+ | `summary` |
| [youtube-sponsor-detection](https://kydlikebtc.github.io/awesome-jev/?lang=en#youtube-sponsor-detection) | ★100+ | `summary` |
| [claude-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#claude-jev) | ★10+ | `summary` |
| [doc-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#doc-router) | ★10+ | `summary` |
| [dsh-jev-tools](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-tools) | ★10+ | `summary` |
| [jev-capability-atlas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-capability-atlas) | ★10+ | `summary` |
| [jev-harness-ismaelsoilet](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness-ismaelsoilet) | ★10+ | `summary` |
| [jev-macos-loop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-macos-loop) | ★10+ | `summary` |
| [jev-skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-router) | ★10+ | `summary` |
| [jevmory](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmory) | ★10+ | `summary` |
| [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#pdf-race) | ★10+ | `summary` |
| [1-million-emojis](https://kydlikebtc.github.io/awesome-jev/?lang=en#1-million-emojis) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [ten-levels-of-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#ten-levels-of-jev) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [ask-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#ask-jev) |  | `summary` |
| [beebots](https://kydlikebtc.github.io/awesome-jev/?lang=en#beebots) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [building-with-typesafe-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#building-with-typesafe-jev) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [decis](https://kydlikebtc.github.io/awesome-jev/?lang=en#decis) |  | `call site` 2026-10-24 · `summary` |
| [decision-first](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-first) |  | `summary` |
| [duomind](https://kydlikebtc.github.io/awesome-jev/?lang=en#duomind) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [flick-computer-use](https://kydlikebtc.github.io/awesome-jev/?lang=en#flick-computer-use) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [grev](https://kydlikebtc.github.io/awesome-jev/?lang=en#grev) |  | `call site` 2026-10-24 · `summary` |
| [harness-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#harness-router) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [harnessjudge](https://kydlikebtc.github.io/awesome-jev/?lang=en#harnessjudge) |  | `summary` |
| [imajev](https://kydlikebtc.github.io/awesome-jev/?lang=en#imajev) |  | `call site` 2026-10-24 · `summary` |
| [jeeves-posthog](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeeves-posthog) |  | `call site` 2026-10-24 · `summary` |
| [jeff-firelex](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeff-firelex) |  | `call site` 2026-10-24 · `summary` |
| [jevos-feder-cr](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevos-feder-cr) |  | `call site` 2026-10-24 · `summary` |
| [jev-browser-bridge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browser-bridge) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-civilizations](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-civilizations) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-plays-pokemon-red-christianmat](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-plays-pokemon-red-christianmat) |  | `call site` 2026-10-24 · `summary` |
| [jev-playwright](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-playwright) |  | `call site` 2026-10-24 · `summary` |
| [jev-safety-gateway](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-safety-gateway) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-sees](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-sees) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-switch](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-switch) |  | `call site` 2026-10-24 · `summary` |
| [jev-board-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-board-lab) |  | `summary` |
| [jev-boe-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-boe-demo) |  | `summary` |
| [jev-browse](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browse) |  | `call site` 2026-10-24 · `summary` |
| [jev-calibrated-narrative-coding](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-calibrated-narrative-coding) |  | `summary` |
| [jev-code-reviewer](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-code-reviewer) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-enforce](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-enforce) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-kit](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-kit) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-lint-ckorhonen](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-lint-ckorhonen) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jev-opus](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-opus) |  | `call site` 2026-10-24 · `summary` |
| [jev-resilience](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-resilience) |  | `summary` |
| [jev-style](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-style) |  | `call site` 2026-10-24 · `summary` |
| [jev-triage-boldbug1](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-triage-boldbug1) |  | `summary` |
| [jevembed](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevembed) |  | `call site` 2026-10-24 · `summary` |
| [jevflix](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevflix) |  | `summary` |
| [jevgrep-dzhng](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgrep-dzhng) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jevry](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevry) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jevstiller](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevstiller) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [jevswiftsdk](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevswiftsdk) |  | `summary` |
| [jevtpp](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevtpp) |  | `call site` 2026-10-24 · `summary` |
| [ollaya](https://kydlikebtc.github.io/awesome-jev/?lang=en#ollaya) |  | `call site` 2026-10-24 · `summary` |
| [onejev](https://kydlikebtc.github.io/awesome-jev/?lang=en#onejev) |  | `call site` 2026-10-24 · `summary` |
| [quicksilver](https://kydlikebtc.github.io/awesome-jev/?lang=en#quicksilver) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [rsi-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#rsi-jev) |  | `call site` 2026-10-24 · `summary` |
| [tiershift](https://kydlikebtc.github.io/awesome-jev/?lang=en#tiershift) |  | `summary` |
| [typesafe-ai-php](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-php) |  | `call site` 2026-10-24 · `summary` |
| [typesafe-client-haileyok](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-client-haileyok) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [vibecheck-jlowin](https://kydlikebtc.github.io/awesome-jev/?lang=en#vibecheck-jlowin) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [vllm-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#vllm-jev) |  | `call site` 2026-10-24 · `summary` |
| [x402check](https://kydlikebtc.github.io/awesome-jev/?lang=en#x402check) |  | `call site` 2026-10-24 · `question_types` · `summary` |
| [yao-agents](https://kydlikebtc.github.io/awesome-jev/?lang=en#yao-agents) |  | `call site` 2026-10-24 · `summary` |
