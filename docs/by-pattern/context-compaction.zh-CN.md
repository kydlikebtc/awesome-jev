# 上下文压缩

<sub>[awesome-jev](../../README.zh-CN.md) · [English](context-compaction.md)</sub>

_判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。_

这个决策的全部已收录例子 —— 共 38 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#上下文压缩)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#context-compaction)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#context-compaction)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 0 · 调用点 38 · 接口形态 0 · 仅示例 0 · 独立报告 2 · 负面结果 2 · 未引用文件 0。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

目录里没有归在这个模式下的 TypeSafe AI 官方材料。 <sub>(机翻)</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。
  <sub>`基准测试` · ★100k+ · `Py` · `noul` · 调用点 [`evals/compaction/jev_arm.py`](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/jev_arm.py)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。
  <sub>`开源项目` · ★10k+ · `Rs` · `noul` · 调用点 [`crates/jcode-base/src/jev.rs`](https://github.com/1jehuang/jcode/blob/HEAD/crates/jcode-base/src/jev.rs)，2026-09-22 阅读</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** — 一个 Claude Code 插件，用逐条决策取代压缩式摘要：过期的工具调用被丢弃或截断，保留下来的全部逐字不变。
  <sub>`插件` · ★1k+ · tamaratran · `TS` · `noul` · 调用点 [`src/request.ts`](https://github.com/tamaratran/fast-jev-compaction/blob/HEAD/src/request.ts)，2026-09-22 阅读</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★1k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`jevkit/client.py`](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py)，2026-09-22 阅读 · ⚠ `实测后未采用`</sub>

- **[jevgrep (dzhng)](https://github.com/dzhng/jevgrep)** — 一个命令行工具和 Agent 技能，用“这段代码做什么”来找代码：`jg "遥测事件是如何记录的？" ./repo` 让 Jev 在目录、文件和声明层面判断相关性，返回相关文件、阅读线索和原文摘录。作者报告在 10 个 SWE-bench 任务上同样解决 8 个，成本约低 30%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · dzhng · `TS` · `noul` · 调用点 [`packages/core/test-node/provider-protocol.mjs`](https://github.com/dzhng/jevgrep/blob/HEAD/packages/core/test-node/provider-protocol.mjs)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)** — 只回答一个问题的插件：现在该不该 /compact。一次 Jev 请求问两个 choice（最近一段工作是否已完成；是亲手干活还是在协调他人），由代码合成一个分数，随着上下文变满，门槛从 0.90 放宽到 0.50。它给出提示；在 Pi 和 Claude Code 上若你开启，也可以自动压缩。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · kunchenguid · `TS` · 调用点 [`packages/claude-mod/lib/judge.ts`](https://github.com/kunchenguid/compact-adviser/blob/HEAD/packages/claude-mod/lib/judge.ts)，2026-09-22 阅读</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)** — 在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。
  <sub>`插件` · ★100+ · tamaratran · `TS` · `noul` · 调用点 [`src/jev.ts`](https://github.com/tamaratran/jev-pruner/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[mu](https://github.com/qybaihe/mu)** — 基于 pi 的编程 Agent（命令行和桌面端），在 38 个决策点上问 Jev：工具输出的哪些片段进上下文、哪些过期的工具结果可以丢掉、被规则拦下的命令是不是用户要的、抓取的网页和 MCP 输出里有没有注入的指令。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · 调用点 [`packages/kyrn-judge/src/providers/typesafe.ts`](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts) · ⚠ `作者自荐`</sub>

- **[Quicksilver](https://github.com/UditAkhourii/quicksilver)** — 一个 Claude Code 技能，把“是否相关”的判断交给 Jev：对每个文件、每行日志或每张工单问一个 noul（例如“这些文件里哪些处理鉴权？”），并行询问并按概率排序，于是 Claude 拿到的是带置信度的候选清单，而不必通读全部内容。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · uditakhourii · `JS` · `noul` · 调用点 [`skills/quicksilver/scripts/qs.mjs`](https://github.com/UditAkhourii/quicksilver/blob/HEAD/skills/quicksilver/scripts/qs.mjs)，2026-10-24 模型阅读</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)** — 给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。
  <sub>`插件` · ★100+ · `Py` · `noul` · 调用点 [`sidecar/src/winnow/judge.py`](https://github.com/GhalebDweikat/winnow/blob/HEAD/sidecar/src/winnow/judge.py)，2026-09-22 阅读</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code 与 Pi 插件，把智能体的小判断交给 Jev：一次编辑是否违反 CLAUDE.md 中的规则（违反则拦下并给出 file:line 引用）、压缩时逐字保留哪些上下文块、为每个子智能体选模型档位并用 noul 检查其任务说明，以及为每条提示给出路由提示。所有钩子都失败即放行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · 0x7067 · `Py` · 调用点 [`scripts/jev.py`](https://github.com/0x7067/claude-jev/blob/HEAD/scripts/jev.py)，2026-09-22 阅读</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — DeepSeek Harness 插件，在工具输出进入上下文之前先问 Jev：长篇读取或抓取结果里哪些段落相关（按排序保留，不卡阈值）；抓回的页面里有没有针对 AI 的指令（概率达到 0.75 时附提醒，内容原样保留）；推荐哪一个技能；以及每条“完成”声明有没有证据。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · horusjiang · `TS` · 调用点 [`src/config.ts`](https://github.com/HorusJiang/dsh-jev-tools/blob/HEAD/src/config.ts)，2026-09-24 阅读</sub>

- **[fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)** — Codex 插件：在会话压缩前后，由 Jev 引导逐字恢复上下文。移植自 tamaratran/fast-jev-compaction，适配 Codex 的生命周期钩子。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · leonaaardob · `TS` · 调用点 [`src/request.ts`](https://github.com/leonaaardob/fast-dev-compaction/blob/HEAD/src/request.ts)，2026-09-24 阅读</sub>

- **[jev-compact](https://github.com/fatelei/jev-compact)** — 为 OpenAI Codex CLI 提供由 Jev 打分的上下文压缩——在压缩前为每个工具调用打分，并恢复关键内容。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · fatelei · `TS` · 调用点 [`plugins/jev-compact/dist/fast-jev.mjs`](https://github.com/fatelei/jev-compact/blob/HEAD/plugins/jev-compact/dist/fast-jev.mjs)，2026-09-24 阅读</sub>

- **[lcc](https://github.com/lucasmartins-ai/lcc)** — 本地上下文编译器（lcc）：在提示上下文送达模型之前清洗、去重并压缩，并报告每一处改动。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · lucasmartins-ai · `Py` · 调用点 [`src/lcc/relevance/jev.py`](https://github.com/lucasmartins-ai/lcc/blob/HEAD/src/lcc/relevance/jev.py)，2026-09-24 阅读</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — 给 omp 做的逐字保留式 Jev 打分上下文削减。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jerryfane · `TS` · 调用点 [`src/vendor/fast-jev/request.ts`](https://github.com/jerryfane/omp-jev-compaction/blob/HEAD/src/vendor/fast-jev/request.ts)，2026-09-22 阅读</sub>

- **[pi-jev](https://github.com/iefnaf/pi-jev)** — 由 Jev 驱动的 Pi 扩展套件：选择性上下文压缩与模型路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · iefnaf · `TS` · 调用点 [`src/vendor/fast-jev-compaction/request.ts`](https://github.com/iefnaf/pi-jev/blob/HEAD/src/vendor/fast-jev-compaction/request.ts)，2026-09-24 阅读</sub>

- **[pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context)** — 一个 Pi 扩展：感知新鲜度的读取去重、Jev 日志过滤，模型表现优先、省 token 其次。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · nyarlathoteppppp · `TS` · 调用点 [`bench/experimental/jev.ts`](https://github.com/Nyarlathoteppppp/pi-jev-context/blob/HEAD/bench/experimental/jev.ts)，2026-09-22 阅读</sub>

- **[save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean)** — 为编码智能体提供可移植的、由 Jev 引导的上下文压缩：不让另一个 LLM 把旧上下文改写成有损摘要，而是由 Jev 判断哪些工具调用和结果仍然重要，用户与助手的文字保持原样。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · iamunbounded · `TS` · 调用点 [`src/cli.ts`](https://github.com/IAmUnbounded/save-token-jev-clean/blob/HEAD/src/cli.ts)，2026-09-24 阅读</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · compozy · `TS` · 调用点 [`benchmarks/jev-calibrate.ts`](https://github.com/compozy/yoshi/blob/HEAD/benchmarks/jev-calibrate.ts)，2026-09-22 阅读</sub>

- **[deepseek-harness-jev (luobosibing2)](https://github.com/luobosibing2/dsh-jev-plugin)** — DeepSeek Harness 插件，提供 12 项需手动开启的功能，用 Jev 作为判断模型：技能选择和 glob 结果排序（每个候选一个 `noul`）、完成度与目标检查、偏离提醒、插话路由、工具输出和测试日志过滤，以及对单个工作区操作的审批。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · luobosibing2 · `TS` · `noul` · 调用点 [`packages/jev/src/selection.ts`](https://github.com/luobosibing2/dsh-jev-plugin/blob/HEAD/packages/jev/src/selection.ts)，2026-10-28 模型阅读</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — 给 DeepSeek Harness 的压缩前顾问，在标准压缩流程之前运行。 <sub>(机翻)</sub>
  <sub>`开源项目` · wjw66 · `TS` · 调用点 [`src/jev/protocol.ts`](https://github.com/wjw66/deepseek-harness-jev-pre-compaction/blob/HEAD/src/jev/protocol.ts)，2026-09-22 阅读</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — 给 DeepSeek Harness 的 Jev 判定式上下文压缩：语义化的工具结果裁剪。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · yangyu666 · `JS` · 调用点 [`src/jev.js`](https://github.com/yangyu666/dsh-jev-prune/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — 给 DeepSeek Harness 的判定式上下文压缩，取代有损的 LLM 摘要。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kolawong · `TS` · 调用点 [`src/jev.ts`](https://github.com/kolawong/fast-compaction-dsh/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · Really Artificial · `JS` · `choice` · `score` · `noul` · 调用点 [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs)，2026-09-22 阅读 · ⚠ `疑似 AI 生成`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — 从不做摘要的 Hermes 会话上下文压缩：每次工具调用都被打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · picaye · `JS` · 调用点 [`hermes-compact.mjs`](https://github.com/picaye/jev-compaction/blob/HEAD/hermes-compact.mjs)，2026-09-22 阅读</sub>

- **[jev-compaction](https://github.com/Waxmell114514/jev-compaction)** — 只能打分、不能写作的上下文压缩器——因此智能体的记忆里不可能出现对话记录中从未有过的事实。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · waxmell114514 · `Py` · 调用点 [`jevctx/jev.py`](https://github.com/Waxmell114514/jev-compaction/blob/HEAD/jevctx/jev.py)，2026-09-24 阅读</sub>

- **[jev-docs](https://github.com/chenrui333/jev-docs)** — 社区维护的 Jev／System One API、SDK 与智能体指南的变更史。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · chenrui333 · `Py` · 调用点 [`src/jev_docs/sync.py`](https://github.com/chenrui333/jev-docs/blob/HEAD/src/jev_docs/sync.py)，2026-09-22 阅读</sub>

- **[jevprune](https://github.com/ibrahemid/jevprune)** — 根据任务描述为编码智能体过滤命令输出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ibrahemid · `TS` · 调用点 [`src/typesafe-client.ts`](https://github.com/ibrahemid/jevprune/blob/HEAD/src/typesafe-client.ts)，2026-09-24 阅读</sub>

- **[jit-context](https://github.com/wojciechwiesner/jit-context)** — JIT-JEV 上下文操作系统：面向 AI 智能体的认知运行时与 JEV System 1 上下文关卡。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · wojciechwiesner · `Py` · 调用点 [`src/cognitive/jev_engine.py`](https://github.com/wojciechwiesner/jit-context/blob/HEAD/src/cognitive/jev_engine.py)，2026-09-24 阅读</sub>

- **[jselect](https://github.com/keltokhy/jselect)** — 在 token 预算内给 AI 挑出有用证据：快速、带来源链接的上下文选择器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · keltokhy · `Py` · 调用点 [`src/jselect/judge.py`](https://github.com/keltokhy/jselect/blob/HEAD/src/jselect/judge.py)，2026-09-22 阅读</sub>

- **[pi-fast-jev-compaction](https://github.com/KamilPostrozny/pi-fast-jev-compaction)** — 给 pi 的快速 JEV 压缩扩展。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · kamilpostrozny · `TS` · 调用点 [`extensions/fast-jev-core.ts`](https://github.com/KamilPostrozny/pi-fast-jev-compaction/blob/HEAD/extensions/fast-jev-core.ts)，2026-09-22 阅读</sub>

- **[pi-fast-jev-compaction](https://github.com/QuentinDanblon/pi-fast-jev-compaction)** — 为 pi 编码智能体提供逐字的上下文修剪，由 TypeSafe Jev 打分：过期的工具调用和结果被丢弃或截短。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · quentindanblon · `TS` · 调用点 [`vendor/fast-jev-compaction/dist/request.d.ts`](https://github.com/QuentinDanblon/pi-fast-jev-compaction/blob/HEAD/vendor/fast-jev-compaction/dist/request.d.ts)，2026-09-24 阅读</sub>

- **[pi-jev-compact](https://github.com/ilkerulusoy/pi-jev-compact)** — 为 Pi 提供选择性的逐字上下文压缩：Jev 为每个工具调用及其结果打分，不再需要的被丢弃，其余原样保留，不让 LLM 写摘要。 <sub>(机翻)</sub>
  <sub>`插件` · ilkerulusoy · `TS` · 调用点 [`src/core/jev.ts`](https://github.com/ilkerulusoy/pi-jev-compact/blob/HEAD/src/core/jev.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[pi-jev-compaction](https://github.com/nourhelmi/pi-jev-compaction)** — 为 Pi 自动清理 Jev 上下文：保留对话，修剪过期的工具输出，无需重跑命令即可取回原始内容。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nourhelmi · `TS` · 调用点 [`src/pruning.ts`](https://github.com/nourhelmi/pi-jev-compaction/blob/HEAD/src/pruning.ts)，2026-09-24 阅读</sub>

- **[pi-jev-context](https://github.com/kevinpita/pi-jev-context)** — 为 Pi 提供可逆的上下文修剪，由 TypeSafe Jev 驱动：保留有用的上下文，同时不删除会话历史。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · kevinpita · `TS` · 调用点 [`src/jev.ts`](https://github.com/kevinpita/pi-jev-context/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[pi-jev-context-curator](https://github.com/Shashank-H/pi-jev-context-curator)** — 基于 Jev 的 pi 上下文整理器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · shashank-h · `TS` · 调用点 [`extensions/curator-jev/config.ts`](https://github.com/Shashank-H/pi-jev-context-curator/blob/HEAD/extensions/curator-jev/config.ts)，2026-09-24 阅读</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** — 合成的吸烟史抽取基准：对比 Jev 与 OpenAI 结构化输出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · vclic · `Py` · 调用点 [`smoking_eval/providers.py`](https://github.com/vclic/smoking-extraction-benchmark/blob/HEAD/smoking_eval/providers.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
