# 实测，而非宣称

<sub>[awesome-jev](../README.zh-CN.md) · [English](measured.md)</sub>

本目录收录的独立测量报告，包括有助于理解适用边界的**负面结果**。这些是原作者的测量，本仓库没有独立复现。比较结果前，请分别查看数据集、测试方法和模型版本。

本目录收录的全部独立测量报告和负面结果 —— 共 92 条，附全部备注和警示标记，负面结果排在最前。[README](../README.zh-CN.md#实测而非宣称) 先显示负面结果，再显示精选路径[独立测量报告](https://kydlikebtc.github.io/awesome-jev/?collection=measured&lang=zh)选出的条目和其余条目中靠前的几条；[站点](https://kydlikebtc.github.io/awesome-jev/?indep=1&lang=zh)列出同样这些条目，并可进一步筛选。 <sub>(机翻)</sub>

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

## 负面结果优先

作者本人针对这一用途测量过 Jev 并得出不采用结论的行：基准测试的测量结论为*不利*，或其他行带有*实测后未采用*标记。作者自述，未经本仓库复现。请先读它们，再看正面例子；[站点也列出了它们](https://kydlikebtc.github.io/awesome-jev/?neg=1&lang=zh)。 <sub>(机翻)</sub>

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br>
  把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。<br>
  <sub>`基准测试` · ★100k+ · `Py` · `noul` · [调用点](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/jev_arm.py)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  > 本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。<br>
  <sub>`基准测试` · ★10k+ · `TS` · `choice` · [调用点](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  **注意:** `仅影子运行`

  > 接进去了但故意不生效：按他们自己的说法，Jev 返回的任何东西都不会进入标签、缓存行或告警。带黄金测试集。想在不拿生产环境下注的前提下试新模型，这是值得照抄的做法。

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。<br>
  <sub>`插件` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py)，2026-09-22 阅读</sub>

  **注意:** `实测后未采用`

  > 值得一提的是它公开了一个被放弃的用法：用 Jev 做交接摘要的召回率，反而不如原始对话记录。

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)**<br>
  为代码审查预选上下文：每个候选文件问一个 Score —— 测了两次后被移除：计费输入明显增加、耗时几乎没有收益；离线回放还表明，候选列表根本够不到审查发现实际所在的位置。<br>
  <sub>`基准测试` · ★1k+ · `Go` · `score` · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  > 已在 PR #1165（2026-09-22）中移除。他们的离线测量发现：候选生成器从构造上就排除了被改动的文件，而几乎所有审查发现都落在被改动的文件上；按文件附带摘录反而让列表更不精确、token 成本更高。代码已不在默认分支上，所以这一行引用的是移除它的那次改动。

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)**<br>
  Claude Code 钩子：每条提示都问 Jev 哪个已安装的技能合适。先用一个 choice 给全部技能排序，同时用三个 noul 判断提示本身；再用 choice 和逐个技能的 noul 评判前三名，低于 0.30 就不推荐。影子模式只记日志；作者用了一周，539 次推荐中只有 28 次随后调用了该技能。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · shimo4228 · `Py` · [调用点](https://github.com/shimo4228/jev-skill-router/blob/HEAD/scripts/jev_client.py)，2026-09-22 阅读</sub>

  **注意:** `实测后未采用`

  > 作者于 2026-09-21 运行后得出结论：作为路由器，它不太可能帮到本来就能看到全部技能描述的强模型。其 README 记录：0.2.0 版上 6 条脚本化请求全部处理得当，0.1.0 版在一次真实会话的 6 条提示中有 3 条出错，作者称这只是个例，不是比率。它一直停留在影子模式。https://dev.to/shimo4228/i-added-jevs-skill-router-to-claude-code-and-turned-back-just-before-rewriting-the-skill-listing-34in 本条中文备注由模型撰写。

## 其他独立测量报告

- **[deep-searcher](https://github.com/zilliztech/deep-searcher)**<br>
  深度研究工具：在 Milvus 等向量数据库中检索私有数据，再用 LLM 推理作答。它的评测把 LLM 自己做出的停止检索决定，与 Jev 就已收集的上下文是否足以作答给出的 noul 相比较，共 100 道题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★1k+ · zilliztech · `Py` · [调用点](https://github.com/zilliztech/deep-searcher/blob/HEAD/evaluation/jev_stopping/run_full100.py)，2026-09-22 阅读</sub>

  > 只在评测中调用 Jev：在 100 道 2WikiMultiHopQA 题上，用 Jev 的一个 Noul 代替 LLM 自己做出的停止检索决定，并在 evaluation/jev_stopping/README.md 中公布对比结果（召回率、轮数、延迟、成本）。2026-11-05 由 AI 助手把类别从替代品改为基准；维护者尚未亲自阅读该报告。

- **[Convex Coding Evals](https://github.com/convex/convex-evals)**<br>
  Convex 的编程基准新增了决策模型赛道：108 道关于 Convex 知识的选择题，每题四个选项，覆盖其 112 个编程评测中的 90 个。Jev 通过 OpenRouter 的决策端点，以一个 `choice` 回答每道题；语言模型则通过聊天补全接口回答同样的问题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★100+ · convex · `TS` · `choice` · [调用点](https://github.com/convex/convex-evals/blob/HEAD/runner/decisions/providers.ts)，2026-10-29 模型阅读</sub>

  > 决策赛道有独立的分数和排行榜；README 说明，选对答案并不代表模型能写出可用的 Convex 代码。托管运行固定使用 typesafe/jev-1.13，并采用三种选项排列。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-10-29 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)**<br>
  受生物启发的智能体记忆：衰减、检索强化与巩固。零运行时依赖，基于 SQLite。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★100+ · kitfunso · `TS` · [调用点](https://github.com/kitfunso/hippo-memory/blob/HEAD/src/infra/rerankers/endpoint.ts)，2026-11-05 模型阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)**<br>
  Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、原速回放与离线报告。<br>
  <sub>`基准测试` · ★100+ · nanmicoder · `JS` · [调用点](https://github.com/NanmiCoder/jev-arena/blob/HEAD/src/backends/jev.mjs)，2026-09-24 阅读</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)**<br>
  Benchmark Heaven 维护的基准，评测 Jev 及兼容 Jev 的决策模型：通过 /v1/systemone 适配器把 noul、choice 和 score 任务发给各个系统，按准确率、校准、延迟和成本打分。当前版本 v1.6.1（2026-10-06）；部分输入是封存的，因此无法完全独立重跑。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★100+ · fstandhartinger · `Py` · [调用点](https://github.com/fstandhartinger/jevbench/blob/HEAD/jevbench/adapters/typesafe.py)，2026-09-22 阅读</sub>

- **[Decision Index](https://github.com/apolinario/decision-index)**<br>
  Decision Index 的复现工具包。Decision Index 是类型化决策引擎（Jev 以及回答 choice 和 noul 问题的开源模型）的排行榜，涵盖 37 个公开基准，按扣除随机水平的方式计分。其 http 引擎把每个请求原样发给任何 /v1/systemone 服务器；参考模型为 jev-1.13.0。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · apolinario · `Py` · [调用点](https://github.com/apolinario/decision-index/blob/HEAD/decision_index/engines/http.py)，2026-10-30 模型阅读</sub>

  > 与 TypeSafe 无关联。发现队列引用的是常量文件；本条目改引 http 引擎，docs/engines.md 说明它通过 TypeSafe 的托管 API 运行 Jev。线上排行榜为 0.4 版；本工具包运行公开的 0.3 套件。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-10-30 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[DMB: decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)**<br>
  针对“从列表中选一项并给出置信度”这类 API 的基准测试：比较 Jev、带结构化输出的 LLM 和确定性基线的准确率、延迟、成本、失败率和置信度。作者报告 jev-latest 在 Banking77 上为 79.2%，CLINC150 上为 88.6%，NLU++ 上微平均 F1 为 48.3%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · nibzard · `Py` · `choice` · [调用点](https://github.com/nibzard/decision-model-benchmark/blob/HEAD/src/dmb/contenders/jev.py)，2026-11-04 模型阅读</sub>

  **注意:** `无许可证`

  > 2026-09-29 的扩展测试只测了 Jev；更早的试点还测了 LLM（Gemini 3.8 Flash 在银行意图上得分更高）。作者提醒，结果只适用于所测的端点、设置和数据集。仓库没有 LICENSE 文件。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-04 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[jev playground (deepdave98)](https://github.com/deepdave98/jev-playground)**<br>
  每周一个的市场销售（GTM）实验，均用 Jev 完成并与 Claude 对比：线索分拣和路由、交易风险、回复分拣、从通话摘要中提取 MEDDPICC 字段、重复账户识别、已流失交易的重新激活，另有一个 MCP 服务器。共享客户端在取整前减去实测的 0.30 分数偏差。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · deepdave98 · `Py` · `noul` · `choice` · `score` · [调用点](https://github.com/deepdave98/jev-playground/blob/HEAD/common/jev.py)，2026-10-31 模型阅读</sub>

  **注意:** `无许可证`

  > 本条目引用 common/jev.py，即第 03 周起各实验共用的客户端。仓库中没有 LICENSE 文件。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-10-31 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)**<br>
  面向类型化决策模型的概率感知评测：校准度、选择性风险、延迟，以及可复现的基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · abdelstark · `Py` · [调用点](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/src/jev_benchmarks/adapters/jev.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)**<br>
  独立的社区地图，以中文为主，说明哪些任务适合交给 Jev 以及原因，依据是附带真实 API 调用记录的测试集，而不是排行榜：答案就在给定文字里时很准，比如该点击哪个 DOM 元素；别处则可能失准（DAIR Emotion 上平均置信度 0.819，实际只对 48%）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · zaious · `Py` · [调用点](https://github.com/Zaious/jev-capability-atlas/blob/HEAD/scripts/common/jev_client.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)**<br>
  在 DSPy 工作流中对 Jev 决策做可复现的校准与选择性风险基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · jmanhype · `Py` · [调用点](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/src/jev_dspy_lab/live.py)，2026-09-22 阅读</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)**<br>
  在 2000 封钓鱼邮件上对比 Jev 与一个轻量 LLM：准确率、校准度、延迟、成本。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · anisselbd · `Py` · [调用点](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/run_jev.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)**<br>
  可复现的基准：衡量 Jev 在 RAG 里的重排质量、延迟与成本。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · erendikmenn · `Py` · [调用点](https://github.com/erendikmenn/jev-rag-benchmark/blob/HEAD/src/jev_rag_benchmark/rerankers.py)，2026-09-22 阅读 · 作者结论：有利（作者自述，未经本仓库复现）</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)**<br>
  与专用重排模型在 14 个数据集上的独立横评。<br>
  <sub>`基准测试` · ★10+ · anessbelbati · `Py` · [调用点](https://github.com/anessbelbati/jev-rerank-bench/blob/HEAD/rerankers/jev.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

  > 这是独立实测而非厂商数字，而且直接对比了专门做重排的模型 —— 这正是 search-ranking 模式该看的对比。

- **[jev-robot-control](https://github.com/openroboto-ai/jev-robot-control)**<br>
  在 MuJoCo 中直接对 xArm7 做笛卡尔控制，对比 Jev 与两个 LLM：每一步选择意图、移动方向和夹爪动作，附原始响应、轨迹与回放。每个控制器只跑了一次（seed 0），不是成功率估计。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · openroboto-ai · `Py` · [调用点](https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/incremental-comparisons/20260919-193012-198478-0/sources/incremental_policy.py)，2026-09-24 阅读 · 作者结论：无定论（作者自述，未经本仓库复现）</sub>

  **注意:** `仅一次提交`

- **[jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval)**<br>
  TypeSafe Jev 重排能否胜过向量检索？在 Agent Skills Hub 目录上做分级相关性评测（9,831 对、164 条中英文查询），并测量了“裁判循环”偏差。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · zhuyansen · `Py` · [调用点](https://github.com/zhuyansen/jev-search-rerank-eval/blob/HEAD/src/jse/openrouter.py)，2026-09-24 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)**<br>
  LegalForecast-MTD 基准 alpha 版与官方评测流程。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · johnhughes3 · `Py` · [调用点](https://github.com/johnhughes3/LegalForecastBench/blob/HEAD/legalforecast/jev/execution.py)，2026-09-22 阅读</sub>

- **[pdf-race](https://github.com/goodrahstar/pdf-race)**<br>
  让三条流水线在 12 篇 arXiv 论文上比赛：Docling 加 Jev、Docling 加 Gemini 3.8 Flash，以及 Gemini 直接读 PDF，每篇回答四个问题，按 arXiv 自己的元数据评分。三条都答对了 12 篇中全部的类别和标题；Jev 这条的成本是 $0.0022，另两条为 $0.036 和 $0.088。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · goodrahstar · `JS` · [调用点](https://github.com/goodrahstar/pdf-race/blob/HEAD/lib/lanes.mjs)，2026-09-24 阅读</sub>

- **[ProbabilityBench](https://github.com/ishida-lab/probabilitybench)**<br>
  把模型报告的概率与精确真值对比的基准测试：在模拟的文本世界（同行评审、隐蔽传输、信用风险）中，正面结果的概率是已知的。其示例通过 OpenRouter 向 Jev 1.13 和其他决策模型提出是非题，并按 KL 散度与成本评分。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · ishida-lab · `Py` · `noul` · [调用点](https://github.com/ishida-lab/probabilitybench/blob/HEAD/examples/decision_models.py)，2026-11-04 模型阅读</sub>

  **注意:** `仅一次提交`

  > 示例通过 OpenRouter 的 Decisions API 为每个模型发送 2,700 个请求，每个请求附 25 个带标签的样例。README 本身不公布分数，请看 arXiv 论文。这些世界是合成机制，并非真实评审或信贷的模型。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-04 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[RLCDAlignBench (Just Ask Jev)](https://github.com/sumleo/rlcdalignbench)**<br>
  基准数据集和论文代码（arXiv 2609.29429），检验 Jev 作为零样本检测器识别 AI 对齐失败的能力：涵盖 44 个基准、十类失败（从谄媚、越狱到奖励投机）的 7,193 条已标注模型输出。每个样本以一次请求发给 Jev，附带一组类型化问题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · sumleo · `Py` · `noul` · `choice` · `score` · [调用点](https://github.com/sumleo/rlcdalignbench/blob/HEAD/code/run_jev.py)，2026-11-01 模型阅读</sub>

  > 据作者报告，一个通用问题在零样本下的 AUROC 中位数为 0.886。数据在 Hugging Face 上需申请访问，采用 CC BY-NC 4.0 许可，含有有害的模型输出；代码采用 MIT 许可。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-01 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)**<br>
  只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · myc0576 · `Py` · [调用点](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/inference-benchmarks)**<br>
  一个模仿其结构化输出形状的网关，用于与之对比测试。<br>
  <sub>`基准测试` · ★10+ · iammrduncan · `TS` · [调用点](https://github.com/iammrduncan/inference-benchmarks/blob/HEAD/packages/decisions/src/jev.ts)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)**<br>
  一个 WebMCP 基准，衡量 WebMCP 与其他浏览器智能体接口的差距。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · nekuda-ai · `TS` · [调用点](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/experiments/jev/frozen/arms/decision-providers.mjs)，2026-09-22 阅读</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)**<br>
  面向证据感知的智能体交接与有界工作续跑的实验性协议。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · zsoxi · `Py` · [调用点](https://github.com/zsoXi/agent-handoff-gate/blob/HEAD/tools/build_benchmark_prompts.py)，2026-09-22 阅读</sub>

  **注意:** `仅一次提交` · `已归档`

- **[antigravity-mcp-semantic-search-with-typesafeai](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)**<br>
  给 AI 编程助手的快速语义代码搜索与 diff 合理性审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · greenyamao · `Py` · [调用点](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi/blob/HEAD/mcp_server.py)，2026-09-22 阅读</sub>

- **[can-jev-bayes](https://github.com/TomRichner/can-jev-bayes)**<br>
  Jev 会贝叶斯吗？把 TypeSafe AI 的 Jev 与贝叶斯最优策略对比，并测试它能否有效使用贝叶斯推理。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · tomrichner · `Py` · [调用点](https://github.com/TomRichner/can-jev-bayes/blob/HEAD/src/jevbandits/client.py)，2026-09-24 阅读</sub>

- **[choosekit](https://github.com/notxf1le/choosekit)**<br>
  一个 TypeScript 库，通过 llama.cpp、Ollama 或 OpenRouter，用模型的对数概率给一组固定选项打分。它的基准测试中，Jev 1.13 在 1,000 题的 SuperGPQA 样本上得 53.6%，在 SemIf 的 144 个用例上与本地 Qwen 3.8 27B 同为 96.53%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · notxf1le · `TS` · `JS` · `choice` · [调用点](https://github.com/notxf1le/choosekit/blob/HEAD/benchmarks/run-supergpqa.mjs)，2026-11-05 模型阅读</sub>

  > choosekit 本身不调用 Jev：只有基准脚本通过 OpenRouter 的 Decisions API 运行 Jev 1.13，作为托管对照。README 说明 SemIf 的延迟数据包含不同的传输开销。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-05 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[Decision Models as Guardrails](https://dm-as-guardrails.raxitlabs.com)**<br>
  让 Jev 1.13.0、Jev 1.14.0 及其他 17 个系统（包括 Bedrock Guardrails）回答同样的 9,975 条带标注的护栏检查，分为六个套件。Jev 以 noul 回答每条检查，概率达到 0.5 或以上即拦截，不对任何模型单独调参。报告平衡准确率（含 95% 区间）以及按公开价格计算的每 1,000 次检查的美元成本。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · raxIT Labs · `Py` · `noul` · `score` · [调用点](https://github.com/raxITlabs/decision-models-as-guardrails/blob/HEAD/benchmark/goldrails_bench/systemone.py)</sub>

  **注意:** `作者自荐`

- **[decision-bench](https://github.com/Hanno-Labs/decision-bench)**<br>
  面向基于文档的决策模型的开放基准运行框架。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · hanno-labs · `Py` · [调用点](https://github.com/Hanno-Labs/decision-bench/blob/HEAD/src/decision_bench/models/jev_openrouter.py)，2026-09-24 阅读</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)**<br>
  给 DeepSeek Harness 的 Jev 决策工具与实时验证基准。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · xienda · `JS` · [调用点](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)**<br>
  Jev 驱动你的轻量浏览器：每步一次类型化选择请求，单文件零依赖。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · shikaizhong-design · `JS` · [调用点](https://github.com/shikaizhong-design/ego-jev-ultrafast/blob/HEAD/jego.js)，2026-09-22 阅读</sub>

- **[Eikos Arena](https://github.com/caiovicentino/eikos-arena)**<br>
  作者的开源模型 Eikos-27B 与 Jev 在 14 个 Hyperliquid 永续合约上的模拟交易对局：每 5 分钟两者拿到同一份行情快照和 28 个问题（每个市场一个做多、观望或做空的 choice，以及一个是否会上涨的 noul），按账户价值和 Brier 分数计分。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · caiovicentino · `Py` · `choice` · `noul` · [调用点](https://github.com/caiovicentino/eikos-arena/blob/HEAD/arena/arena.py)，2026-11-08 模型阅读</sub>

  > 在 72 小时的正式对局（2026-09-24 至 09-27）中，Jev 收益 +0.87%、Brier 分数 0.249，Eikos 为 -3.40% 和 0.266；这些是作者公布的数字，来自冻结并做了哈希的代码。使用真实价格、模拟资金，不下真实订单。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-08 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[Evaluating and Benchmarking the System One Model Jev](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking)**<br>
  一篇 arXiv 论文的代码：在 37 个公开数据集上以 choice、noul 和 score 零样本测试 Jev，并用同样的请求给两个开源权重大模型打分作对比；另有一个序列决策部分，让 Jev 在 ALFWorld、TextWorld、FrozenLake 等五个环境里每步选一个动作。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · AppliedMachineLearning-Lab · `Py` · `choice` · `noul` · `score` · [调用点](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/blob/HEAD/jev_benchmarking/runner.py)，2026-11-10 模型阅读</sub>

  > 作为对比的模型（Qwen 和 Gemma，用它们自己的选项概率打分）不是 Jev。原始响应已发布在 Zenodo 上，不调用 API 也能重建论文里的表格。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-10 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[Jev and open decision-model benchmarks](https://github.com/akitaonrails/jev-docs-benchmarks)**<br>
  评测决策模型执行给定规则的可靠性、其概率的表现以及决策成本：把托管的 Jev 与 Microsoft Decision-1、OpenAI Decisions 以及 Clef、Decision 3.0、Laya、Kev、Jebadiah 等开源模型对比，使用冻结的输入并公开原始响应。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · akitaonrails · `Py` · `choice` · [调用点](https://github.com/akitaonrails/jev-docs-benchmarks/blob/HEAD/benchmark/tools/hosted.py)，2026-11-07 模型阅读</sub>

  **注意:** `无许可证`

  > 作者为 akitaonrails。在其 Decision 3.0 排名中，Jev 在该套件的 choice 任务上得分 97.6%。任务是作者自建的合成任务（分类、客服路由、检索），有英语和巴西葡萄牙语；README 说明这不是厂商官方基准。本地模型运行在 CUDA 和 ROCm 机器上。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-07 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[JEV Healthcare Lab](https://github.com/juneyaooo/jev-healthcare-lab)**<br>
  Jev 医疗决策基准：以 choice 问题覆盖 26 项任务、1,514 项判断（分诊紧急程度、禁忌判断、用药选择、护理、临床试验筛选），与 DeepSeek Flash 和 Qwen 对比准确率、持续吞吐和成本，并公开原始响应。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · juneyaooo · `Py` · `choice` · [调用点](https://github.com/juneyaooo/jev-healthcare-lab/blob/HEAD/scripts/run_model_evaluation.py)，2026-11-07 模型阅读</sub>

  **注意:** `无许可证`

  > Jev 的主要结果是经第三方网关（ai.xiaohaima-edu.com）收集的，其响应自称为 jev-1.13.0，作者表示未独立核实；scripts/run_model_evaluation.py 则直接调用 TypeSafe。数据由作者自报；README 说明这不是临床有效性验证。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-07 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[Jev Persian Benchmark](https://github.com/armanjr/jev-persian-benchmark)**<br>
  在 480 道自编通用波斯语题、560 道文学题和一个古典诗歌试点上，把 Jev 与开源决策模型对比的基准：以 choice、noul 和 score 提问，保存原始响应并在本地评分；Jev 在 choice 和 noul 准确率上领先。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · armanjr · `Py` · `choice` · `noul` · `score` · [调用点](https://github.com/armanjr/jev-persian-benchmark/blob/HEAD/jev_benchmark/runner.py)，2026-11-11 模型阅读</sub>

  **注意:** `无许可证`

  > 其他模型（Jeff、Mizan 和 Laya）不是 Jev；在 score 上 Mizan 领先。结果是作者自己的。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-11 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[JEV Reranking Comparisons](https://github.com/carlaiau/jev-reranking)**<br>
  把 Jev 当作零样本重排器的基准：对每个查询与候选各问一个是否相关的 noul，用概率对 MS MARCO 段落和文档集（TREC DL 2019）以及 TREC-1 WSJ 上的 BM25 结果重新排序，与已发表的 BERT 重排器对比，并记录耗时和成本。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · carlaiau · `Py` · `noul` · [调用点](https://github.com/carlaiau/jev-reranking/blob/HEAD/reranking/jev.py)，2026-11-07 模型阅读</sub>

  > 在 TREC DL 2019 段落集上，作者的 Jev 运行 nDCG@10 为 0.68，已发表的最佳 BERT 运行为 0.74；在文档集上为 0.75 对 0.72；这些都是作者自己的运行结果。另有交互式模拟器可重放 WSJ 结果。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-07 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[Jev vs. the right baselines](https://github.com/ickma2311/jev-baselines-eval)**<br>
  两项预注册的独立研究：Jev 以 choice 在 CLINC150 和 Banking77 上分类客户意图，作为升级级联的关卡，与小型和前沿大模型以及有监督编码器对比；第二项研究检验在提示注入下，Jev 的置信度能否区分被劫持的决策和抵抗住的决策。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ickma2311 · `Py` · `choice` · `noul` · [调用点](https://github.com/ickma2311/jev-baselines-eval/blob/HEAD/code/common.py)，2026-11-10 模型阅读</sub>

  > 作者的结论：两个级联实验结果都不明确；在注入条件下，Jev 的置信度把被劫持的决策排在抵抗住的决策之上。第一项研究经 Vercel AI Gateway 调用 Jev，第二项直接调用。参与对比的其他模型不是 Jev。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-10 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[Jev × DimABSA](https://github.com/zhangyiqun018/jev-dimabsa)**<br>
  只用 Jev、不生成文本也不微调的 SemEval-2026 任务 3（DimABSA）参赛系统：用 score 把每个方面词的效价和唤醒度放到 1 到 9 的刻度上，再用 choice 和 noul 抽取方面词、观点词和类别组成的三元组与四元组。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · zhangyiqun018 · `Py` · `score` · `choice` · `noul` · [调用点](https://github.com/zhangyiqun018/jev-dimabsa/blob/HEAD/jev/client.py)，2026-11-10 模型阅读</sub>

  **注意:** `无许可证`

  > 仓库没有 LICENSE 文件。它在官方测试集上的数据（任务 1 的 RMSE 为 1.0645，在提交全部十个语料的 14 支队伍里微平均最低）是作者自己报告的。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-10 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[jev-acento](https://github.com/marcosmartinez/jev-acento)**<br>
  Jev 听得懂你的口音吗？一项预先注册的、针对 TypeSafe AI Jev 西班牙语表现的审计——准确率、校准与 token 成本。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · marcosmartinez · `Py` · [调用点](https://github.com/marcosmartinez/jev-acento/blob/HEAD/src/jev_acento/providers.py)，2026-09-24 阅读</sub>

  > 一项独立、预先注册的非英语审计——正是 docs/status.md 中列为值得关注的空白。

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)**<br>
  在一个智能体失败归因基准上，把 Jev 与一个强 LLM 做对比测试。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · tokentrim · `Py` · [调用点](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/HEAD/src/jevbench/backends/jev.py)，2026-09-22 阅读</sub>

- **[jev-bench](https://github.com/TheWayWithin/jev-bench)**<br>
  引用的来源真的这么说了吗？一个包含 42 条论断的基准：Jev（TypeSafe System One）对比 GPT 与 Claude 等模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · thewaywithin · `Py` · [调用点](https://github.com/TheWayWithin/jev-bench/blob/HEAD/run.py)，2026-09-24 阅读</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)**<br>
  Jev 的基准与 playground：国际象棋，以及语音转写中的说话对象判定。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · wondertwins · `Py` · [调用点](https://github.com/wondertwins/jev-benchmark/blob/HEAD/jevcommon/client.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)**<br>
  TypeSafe AI Jev 在智能体工具调用风险分类上的可复现基准：准确率、延迟，以及其置信度是否可信。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · themsquared · `Py` · [调用点](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py)，2026-09-24 阅读</sub>

- **[jev-calibration-audit](https://github.com/tapesymbolstate/jev-calibration-audit)**<br>
  仅通过 API 对 Jev 做的独立校准审计。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · jujumilk3 · `Py` · [调用点](https://github.com/tapesymbolstate/jev-calibration-audit/blob/HEAD/src/jev_audit/client.py)，2026-09-22 阅读</sub>

  **注意:** `仅一次提交`

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)**<br>
  给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · nikkoxgonzales · `Py` · [调用点](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py)，2026-09-22 阅读</sub>

- **[jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark)**<br>
  在 Python 代码审查规则上比较 Jev、Gemini Flash 与 Claude Fable：成本、速度、准确率与一致性。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · gemanor · `Py` · [调用点](https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/determinest/clients.py)，2026-09-24 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)**<br>
  TypeSafe 的 Jev 在俄语上能保持准确率与校准吗？一项独立的俄英对照审计（ECE、可靠性图）。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ahtoooxa · `Py` · [调用点](https://github.com/AHTOOOXA/jev-cyrillic-audit/blob/HEAD/src/jev_cyrillic_audit/run.py)，2026-09-24 阅读</sub>

  > 一项独立的非英语校准审计——正是 docs/status.md 中列为值得关注的空白。

- **[jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks)**<br>
  JEV 在 MetaTool、When2Call 与 BFCL V4 上的决策基准结果，附双语表格和可复现报告。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · baibizhe · `Py` · [调用点](https://github.com/baibizhe/jev-decision-benchmarks/blob/HEAD/scripts/build_tables.py)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)**<br>
  关于 Jev 概率校准、不确定性表达以及预测概率保真度的实验。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · kantahayashiai · `JS` · [调用点](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/HEAD/src/run.mjs)，2026-09-24 阅读</sub>

- **[jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric)**<br>
  让大量语义决策走同一条经过验证的路径的架构，附带标注数据集。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ghubnab99 · `C#` · [调用点](https://github.com/ghubnab99/jev-enterprise-decision-fabric/blob/HEAD/src/DecisionFabric.TypeSafe/TypeSafeClientOptions.cs)，2026-09-22 阅读</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)**<br>
  在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · 4esv · `Py` · [调用点](https://github.com/4esv/jev-eval/blob/HEAD/evaljev/runners.py)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

- **[jev-eval](https://github.com/onlyoneaman/jev-eval)**<br>
  在四个公开分类数据集上比较 TypeSafe 的 Jev 与两款 GPT 模型：案例、逐条答案、评分全部公开。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · onlyoneaman · `TS` · [调用点](https://github.com/onlyoneaman/jev-eval/blob/HEAD/jev_eval/backends.py)，2026-09-24 阅读</sub>

  **注意:** `仅一次提交`

- **[jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval)**<br>
  第三方在相同条件下对比 Jev 与两款 LLM：为面向日本游客的摄影服务路由预订咨询，共六十条四种语言的合成消息。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · shogo-nfrealmusic · `TS` · [调用点](https://github.com/Shogo-nfrealmusic/jev-eval/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[jev-exploration](https://github.com/SamuelSacco/jev-exploration)**<br>
  Jev 探索性合集：宣称核查、实时演示与可运行代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · samuelsacco · `Py` · [调用点](https://github.com/SamuelSacco/jev-exploration/blob/HEAD/jevlab/client.py)，2026-09-22 阅读</sub>

- **[jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench)**<br>
  实测：在一次调用里向 TypeSafe Jev 提 N 个问题，state 只计费一次。基于 2,976 次真实请求，附原始数据和精确的计费核对。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · blowxian · `Py` · [调用点](https://github.com/blowxian/jev-fanout-bench/blob/HEAD/bench.py)，2026-09-24 阅读</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)**<br>
  可复现的早期访问评测：Jev 在韩语理解与医学文本上的表现，附运行时与成本证据。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · mahlernim · `Py` · [调用点](https://github.com/mahlernim/jev-korean-benchmark/blob/HEAD/jevbench/medqa_run.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

  **注意:** `无许可证`

- **[jev-lab](https://github.com/danielhirt/jev-lab)**<br>
  通过 OpenRouter 对 TypeSafe Jev（System One 决策模型）做的实验：可重复性、扰动敏感性与 LLM 基线对比。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · danielhirt · `TS` · [调用点](https://github.com/danielhirt/jev-lab/blob/HEAD/packages/codenames/src/judge.ts)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[jev-lab](https://github.com/llt22/jev-lab)**<br>
  TypeSafe Jev（System One 模型）的动手研究实验室：对 Noul/Choice/Score 原语的可复现基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · llt22 · `Py` · [调用点](https://github.com/llt22/jev-lab/blob/HEAD/experiments/json-render-jev/src/demo.tsx)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[jev-lab](https://github.com/Menny1337/jev-lab)**<br>
  针对 TypeSafe Jev 模型的 TypeScript 实验、评测与延迟基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · menny1337 · `TS` · [调用点](https://github.com/Menny1337/jev-lab/blob/HEAD/src/client.ts)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)**<br>
  Jev 的能力展示与研究：一次 show-and-tell 式的考察。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · lbotinelly · `TS` · [调用点](https://github.com/lbotinelly/jev-little-airways/blob/HEAD/demo/js/jev-monitor.mjs)，2026-09-22 阅读</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)**<br>
  以基准驱动的 Jev 路由器与评判者，服务于成本可控的 LLM 编程流程。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · erendikmenn · `Py` · [调用点](https://github.com/erendikmenn/jev-llm-router-benchmark/blob/HEAD/src/jev_router/providers/review.py)，2026-09-22 阅读</sub>

- **[jev-no-enem](https://github.com/patryckalves/jev-no-enem)**<br>
  在巴西 2025 年 ENEM 标准化考试上评测 TypeSafe AI Jev（System One 范式）的可复现基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · patryckalves · `Py` · [调用点](https://github.com/patryckalves/jev-no-enem/blob/HEAD/src/evaluate_jev.py)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

  > 一项非英语的独立评测，使用的是有标准答案的公开考试。

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)**<br>
  在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · scienthoon · `Py` · [调用点](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)**<br>
  按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · yodablocks · `Py` · [调用点](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py)，2026-09-22 阅读</sub>

- **[jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong)**<br>
  让 Jev 实时玩浏览器乒乓球：结构化遥测与类型化决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · icohen007 · `JS` · [调用点](https://github.com/Icohen007/jev-play-ping-pong/blob/HEAD/src/typesafe.mjs)，2026-09-22 阅读</sub>

- **[jev-playground](https://github.com/hegargarcia/jev-playground)**<br>
  在状态明确、合法动作清晰的游戏里，把 Jev 与其他评估模型做对比：规则和状态转移由代码掌控，每个模型选择下一步动作，结果可测量。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · hegargarcia · `TS` · [调用点](https://github.com/hegargarcia/jev-playground/blob/HEAD/src/app/api/connect-four/move/route.ts)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[jev-plays](https://github.com/mansicer/jev-plays)**<br>
  由 System One 模型玩 Craftax，LLM 负责设定目标：同一张地图上的五种智能体，从 Jev 直接操作原始动作到 LLM 控制每一步，用记录下来的对局进行比较。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · mansicer · `Py` · [调用点](https://github.com/mansicer/jev-plays/blob/HEAD/craftax_agent/jev_policy.py)，2026-09-24 阅读</sub>

- **[jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment)**<br>
  在 RouterArena 上把 Jev 当作低成本 LLM 路由器做基准测试。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · tokentrim · `Py` · [调用点](https://github.com/TokenTrim/jev-routing-experiment/blob/HEAD/jev_router/jev.py)，2026-09-22 阅读</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)**<br>
  衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · teyhouse · `Py` · [调用点](https://github.com/teyhouse/jev-secret-detection/blob/HEAD/main.py)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

- **[jev-sim](https://github.com/dashbi1/jev-sim)**<br>
  从 LLM logits 读出类型化决策的 Jev 兼容 /v1/systemone 服务，带基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · dashbi1 · `Py` · [调用点](https://github.com/dashbi1/jev-sim/blob/HEAD/jev_sim/cli.py)，2026-09-22 阅读</sub>

- **[jev-test](https://github.com/mity-prodgen/jev-test)**<br>
  三篇 Jev 测评文章背后的测试工具：检验 Jev 的置信度是否有意义；让 Jev 判断某个论断是否有来源段落支持，并与大模型评判对比；以及把 Jev 用在 RAG 里做重排序，包括某个片段自身的文字能否改变它的排名。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · mity-prodgen · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/mity-prodgen/jev-test/blob/HEAD/jev_harness/client.py)，2026-11-11 模型阅读</sub>

  > 大模型评判和困难负例用的是 Claude，它不是 Jev。每个原始请求和响应都有记录。它不是已收录的 jev-test（WeSecureYou）。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-11 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)**<br>
  把 Jev 的 noul 原语应用到一个共谋语料库上。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · sypherin · `Py` · [调用点](https://github.com/sypherin/jev-trace-classifier/blob/HEAD/jev_client.py)，2026-09-22 阅读</sub>

- **[jevarena](https://github.com/chenmingtang830/jevarena)**<br>
  开源的自带 key 竞技场，用来评测 Jev 与其他 AI 裁判：找出失败案例，比较质量、成本与延迟。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · chenmingtang830 · `TS` · [调用点](https://github.com/chenmingtang830/jevarena/blob/HEAD/jevjudge/providers.py)，2026-09-24 阅读</sub>

- **[jevbench](https://github.com/GautamTalksDev/jevbench)**<br>
  对 TypeSafe Jev 在人类意见分歧下的校准进行预注册、经偏差校正的测试（ChaosNLI，每条 100 个人工标注） <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · Gautam Khosla · `Py` · `choice` · `noul` · [调用点](https://github.com/GautamTalksDev/jevbench/blob/HEAD/jevbench/clients/jev.py) · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

  **注意:** `疑似 AI 生成` · `作者自荐`

- **[jevsbistro](https://github.com/andrewsilber/JevsBistro)**<br>
  用于低延迟决策模型基准测试的 3D 餐厅服务模拟器。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · andrewsilber · `TS` · [调用点](https://github.com/andrewsilber/JevsBistro/blob/HEAD/src/jev/protocol.ts)，2026-09-22 阅读</sub>

- **[origin-civilization](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)**<br>
  AI 生命与文明模拟：每个决策都由 Jev 做出。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · jacquesgariepy · `TS` · [调用点](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION/blob/HEAD/legacy/source/providers.js)，2026-09-22 阅读</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)**<br>
  来自某土地开发 SaaS 的类型化决策基准：schema、匿名标注数据与运行器。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · zsavage8 · `Py` · [调用点](https://github.com/zsavage8/padflow-jev-evals/blob/HEAD/scripts/run_baseline.py)，2026-09-22 阅读</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)**<br>
  合成的吸烟史抽取基准：对比 Jev 与 OpenAI 结构化输出。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · vclic · `Py` · [调用点](https://github.com/vclic/smoking-extraction-benchmark/blob/HEAD/smoking_eval/providers.py)，2026-09-22 阅读</sub>

  **注意:** `仅一次提交` · `无许可证`

- **[sysone-bench](https://github.com/instax-dutta/sysone-bench)**<br>
  首个独立的 System One 决策模型横评（Laya 对比 Jev）。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · instax-dutta · `Py` · [调用点](https://github.com/instax-dutta/sysone-bench/blob/HEAD/runners/jev_runner.py)，2026-09-22 阅读</sub>

- **[tev1-4B-experimental](https://github.com/togethercomputer/tev1)**<br>
  Together AI 微调 Qwen3.5-4B，用一个选项字母回答决策问题。在对三个公开 Jev 基准的配对重跑中，它在钓鱼邮件上得 50.6%，Jev 1.13 为 62.9%；工具风险上两者都是 93.3%；工单路由上为 96.3%，Jev 为 100%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · togethercomputer · `Py` · `choice` · [调用点](https://github.com/togethercomputer/tev1/blob/HEAD/evaluation/public-third-party/run.py)，2026-11-05 模型阅读</sub>

  > Jev 只作为基线：通过 OpenRouter 的 Decisions API 调用 typesafe/jev-1.13，每次请求一个 Choice 问题，题目来自 anisselbd/jev-phishing-bench、themsquared/jev-benchmark 和 WallerChen/jev-measured。结果和原始响应在 evaluation/public-third-party/。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-11-05 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review)**<br>
  关于为代码审查校准 Jev 的研究。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · selmar · `Py` · [调用点](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review/blob/HEAD/calibrate.py)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[what-is-jev](https://github.com/g0runmezadam/what-is-jev)**<br>
  关于 TypeSafe AI Jev（System One）的独立、有来源的研究，包含对 947 个公开仓库的评分。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · g0runmezadam · `Py`</sub>

  > 这是对生态的研究，而不是 API 的调用者，因此没有调用点证据。

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br>
  独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。<br>
  <sub>`基准测试` · ★100+</sub>

  **注意:** `无许可证` · `宣称未核实`

  > 在所有资料里找到的最具操作价值的工程警示：如果仅仅选项顺序就能把概率推过你的阈值，那你的阈值没有看上去那么稳。这是独立且未被复现的结果，具体幅度请当作指示性数据。

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br>
  找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。<br>
  <sub>`基准测试` · Lindfors</sub>

  > 方法论交代干净，并诚实限定为「单日快照」。开篇就摆失败案例，这才让它成为真正的校准检验，而不是一篇软文。

- **[Support-routing benchmark: 100 held-out cases](https://decisionmodelhub.com/benchmarks/support-routing)**<br>
  在 100 条留出的虚构客服消息上，将 Jev 与 Clef、Clef Flash、OpenAI 的 Decisions API 以及 GPT-6 Luna 结构化输出基线进行对比：每条消息路由到五个团队标签之一；所有用例和各模型的作答记录均可下载。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · DecisionModelHub</sub>

  **注意:** `作者自荐`

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br>
  找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。<br>
  <sub>`基准测试` · Near Here</sub>

  > 自我限定很规范：这是用例研究，不是模型排行榜。这种克制比数字本身更少见。

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
