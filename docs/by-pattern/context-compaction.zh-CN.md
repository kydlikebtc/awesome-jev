# 上下文压缩

<sub>[awesome-jev](../../README.zh-CN.md) · [English](context-compaction.md)</sub>

_判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。_

这个决策的全部已收录例子 —— 共 34 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#上下文压缩)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。
  <sub>`基准测试` · ★248,479 · `Py` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。
  <sub>`开源项目` · ★20,069 · `Rs` · `noul`</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** — 一个 Claude Code 插件，用逐条决策取代压缩式摘要：过期的工具调用被丢弃或截断，保留下来的全部逐字不变。
  <sub>`插件` · ★6,616 · tamaratran · `TS` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★718 · `Py` · `choice` · `score` · `noul`</sub>

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)** — 判断工作是否已完成或已记录，据此提示运行上下文压缩。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★183 · kunchenguid · `TS`</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)** — 在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。
  <sub>`插件` · ★144 · tamaratran · `TS` · `noul`</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)** — 给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。
  <sub>`插件` · ★79 · `Py` · `noul`</sub>

- **[save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean)** — 为编码智能体提供可移植的、由 Jev 引导的上下文压缩：不让另一个 LLM 把旧上下文改写成有损摘要，而是由 Jev 判断哪些工具调用和结果仍然重要，用户与助手的文字保持原样。 <sub>(机翻)</sub>
  <sub>`插件` · ★69 · iamunbounded · `TS`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(机翻)</sub>
  <sub>`插件` · ★25 · compozy · `TS`</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code 插件：Jev 负责规则检查、逐字压缩与提示路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★12 · 0x7067 · `Py`</sub>

- **[jev-compact](https://github.com/fatelei/jev-compact)** — 为 OpenAI Codex CLI 提供由 Jev 打分的上下文压缩——在压缩前为每个工具调用打分，并恢复关键内容。 <sub>(机翻)</sub>
  <sub>`插件` · ★8 · fatelei · `TS`</sub>

- **[lcc](https://github.com/lucasmartins-ai/lcc)** — 本地上下文编译器（lcc）：在提示上下文送达模型之前清洗、去重并压缩，并报告每一处改动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · lucasmartins-ai · `Py`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — 给 omp 做的逐字保留式 Jev 打分上下文削减。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · jerryfane · `TS`</sub>

- **[pi-jev](https://github.com/iefnaf/pi-jev)** — 由 Jev 驱动的 Pi 扩展套件：选择性上下文压缩与模型路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★8 · iefnaf · `TS`</sub>

- **[pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context)** — 一个 Pi 扩展：感知新鲜度的读取去重、Jev 日志过滤，模型表现优先、省 token 其次。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — 给 DeepSeek Harness 的压缩前顾问，在标准压缩流程之前运行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · wjw66 · `TS`</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — 用 Jev 做判断而不是生成：修剪过长的工具输出、筛查抓取页面中注入的指令、为“完成”把关。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · horusjiang · `TS`</sub>

- **[fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)** — Codex 插件：在会话压缩前后，由 Jev 引导逐字恢复上下文。移植自 tamaratran/fast-jev-compaction，适配 Codex 的生命周期钩子。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · leonaaardob · `TS`</sub>

- **[jit-context](https://github.com/wojciechwiesner/jit-context)** — JIT-JEV 上下文操作系统：面向 AI 智能体的认知运行时与 JEV System 1 上下文关卡。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · wojciechwiesner · `Py`</sub>

- **[pi-jev-context-curator](https://github.com/Shashank-H/pi-jev-context-curator)** — 基于 Jev 的 pi 上下文整理器。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · shashank-h · `TS`</sub>

- **[jev-compaction](https://github.com/Waxmell114514/jev-compaction)** — 只能打分、不能写作的上下文压缩器——因此智能体的记忆里不可能出现对话记录中从未有过的事实。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · waxmell114514 · `Py`</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — 给 DeepSeek Harness 的 Jev 判定式上下文压缩：语义化的工具结果裁剪。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · yangyu666 · `JS`</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — 给 DeepSeek Harness 的判定式上下文压缩，取代有损的 LLM 摘要。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · kolawong · `TS`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — 从不做摘要的 Hermes 会话上下文压缩：每次工具调用都被打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · picaye · `JS`</sub>

- **[jselect](https://github.com/keltokhy/jselect)** — 在 token 预算内给 AI 挑出有用证据：快速、带来源链接的上下文选择器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · keltokhy · `Py`</sub>

- **[pi-fast-jev-compaction](https://github.com/QuentinDanblon/pi-fast-jev-compaction)** — 为 pi 编码智能体提供逐字的上下文修剪，由 TypeSafe Jev 打分：过期的工具调用和结果被丢弃或截短。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · quentindanblon · `TS`</sub>

- **[pi-jev-compaction](https://github.com/nourhelmi/pi-jev-compaction)** — 为 Pi 自动清理 Jev 上下文：保留对话，修剪过期的工具输出，无需重跑命令即可取回原始内容。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · nourhelmi · `TS`</sub>

- **[jev-docs](https://github.com/chenrui333/jev-docs)** — 社区维护的 Jev／System One API、SDK 与智能体指南的变更史。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · chenrui333 · `Py`</sub>

- **[jevprune](https://github.com/ibrahemid/jevprune)** — 根据任务描述为编码智能体过滤命令输出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · ibrahemid · `TS`</sub>

- **[pi-fast-jev-compaction](https://github.com/KamilPostrozny/pi-fast-jev-compaction)** — 给 pi 的快速 JEV 压缩扩展。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · kamilpostrozny · `TS`</sub>

- **[pi-jev-context](https://github.com/kevinpita/pi-jev-context)** — 为 Pi 提供可逆的上下文修剪，由 TypeSafe Jev 驱动：保留有用的上下文，同时不删除会话历史。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · kevinpita · `TS`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `仅一次提交` `疑似 AI 生成`</sub>

- **[pi-jev-compact](https://github.com/ilkerulusoy/pi-jev-compact)** — 为 Pi 提供选择性的逐字上下文压缩：Jev 为每个工具调用及其结果打分，不再需要的被丢弃，其余原样保留，不让 LLM 写摘要。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · ilkerulusoy · `TS` · ⚠ `无许可证`</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** — 合成的吸烟史抽取基准：对比 Jev 与 OpenAI 结构化输出。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · vclic · `Py` · ⚠ `无许可证`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
