# 内容评分

<sub>[awesome-jev](../../README.zh-CN.md) · [English](content-scoring.md)</sub>

_在有序量表上给质量、风险或相关性打分。_

这个决策的全部已收录例子 —— 共 166 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#内容评分)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#content-scoring)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#content-scoring)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 2 · 调用点 157 · 接口形态 5 · 仅示例 0 · 独立报告 9 · 负面结果 1 · 未引用文件 4。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) <sub>`官方文档` · `Py` · `choice`</sub>
- [Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) <sub>`官方文档` · `Py` · `score`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐ — 把一个笼统的判断拆成若干原子评分，再用你自己代码里的权重（而不是提示词里的）组合起来。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★10k+ · `TS` · `choice` · 调用点 [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现） · ⚠ `仅影子运行`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[gptcache](https://github.com/zilliztech/GPTCache)** — 面向 LLM 的语义缓存，已完整集成主流框架。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · zilliztech · `Py` · 调用点 [`gptcache/similarity_evaluation/jev.py`](https://github.com/zilliztech/GPTCache/blob/HEAD/gptcache/similarity_evaluation/jev.py)，2026-09-22 阅读</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★1k+ · `Java` · `choice` · `score` · `noul` · 调用点 [`app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-09-22 阅读</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — 用 Jev 打分器给代码中的文本做 lint。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · mizchi · `TS` · 调用点 [`src/jev.ts`](https://github.com/mizchi/jev-lint/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — 一个本地优先的 MCP 插件，供编程智能体做持续的代码质量审查。
  <sub>`插件` · ★100+ · niazmorshed2007 · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/NiazMorshed2007/jev-review/blob/HEAD/src/jev/client.ts)，2026-09-22 阅读</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `score` · `noul` · 调用点 [`src/review/codebase-judgments.ts`](https://github.com/devagrawal09/jev-review/blob/HEAD/src/review/codebase-judgments.ts)，2026-09-22 阅读</sub>

- **[jev-semgrep](https://github.com/uehaj/sys1grep)** — 按含义 grep，跨语言：Jev 给每一行按含义打分，可用 AND/OR/NOT 组合多个含义。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · uehaj · `JS` · 调用点 [`semgrep.mjs`](https://github.com/uehaj/sys1grep/blob/HEAD/semgrep.mjs)，2026-09-22 阅读</sub>

- **[jev-seo](https://github.com/AgriciDaniel/jev-seo)** — 从一个首页网址出发，对任意网站做实时 SEO 审计，由 Jev 判定，输出 PDF、XLSX 和 Markdown 报告。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · agricidaniel · `Py` · 调用点 [`jevseo/jev.py`](https://github.com/AgriciDaniel/jev-seo/blob/HEAD/jevseo/jev.py)，2026-09-24 阅读</sub>

- **[jevmeter](https://github.com/ChetasLua/jevmeter)** — 给视频里的每一句话打分，并把结果渲染成一个实时仪表。
  <sub>`开源项目` · ★100+ · chetaslua · `Py` · 调用点 [`jevmeter/score.py`](https://github.com/ChetasLua/jevmeter/blob/HEAD/jevmeter/score.py)，2026-09-22 阅读</sub>

- **[killmyidea](https://github.com/monteduro/killmyidea)** — 输入一个创业点子，Jev 从多个维度打分，最后给你 KILL、FIX 或 SHIP。
  <sub>`开源项目` · ★100+ · `TS` · `score` · `choice` · 调用点 [`src/lib/typesafe.ts`](https://github.com/monteduro/killmyidea/blob/HEAD/src/lib/typesafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[llm2jev](https://github.com/Yinsongxu/LLM2Jev)** — 把本地语言模型改造成 Jev 兼容的结构化决策引擎，输出 Choice、Score、Noul。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · yinsongxu · `Py` · 调用点 [`src/llm2jev/server/sglang_server.py`](https://github.com/Yinsongxu/LLM2Jev/blob/HEAD/src/llm2jev/server/sglang_server.py)，2026-09-24 阅读</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接 40 家 AI 供应商，覆盖生成、流式与决策三种推理形态。 <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · juspay · `TS` · 调用点 [`src/lib/providers/typesafe.ts`](https://github.com/juspay/neurolink/blob/HEAD/src/lib/providers/typesafe.ts)，2026-09-22 阅读</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js)，2026-09-22 阅读</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★100+ · `Py` · `sh` · `choice` · `score` · `noul` · 调用点 [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql)，2026-09-22 阅读</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — 给编程智能体用的代码质量与覆盖率判断，Rust 实现。
  <sub>`开源项目` · ★100+ · supercorp-ai · `Rs` · 调用点 [`crates/supercov-cli/src/quality.rs`](https://github.com/supercorp-ai/supercov/blob/HEAD/crates/supercov-cli/src/quality.rs)，2026-09-22 阅读</sub>

- **[anydecisionmodel](https://github.com/mattt/AnyDecisionModel)** — 一个 Swift 包：从语言模型获取类型化决策（概率、选择与分数）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · mattt · `Swift` · 调用点 [`Sources/AnyDecisionModel/Models/JevDecisionModel.swift`](https://github.com/mattt/AnyDecisionModel/blob/HEAD/Sources/AnyDecisionModel/Models/JevDecisionModel.swift)，2026-09-22 阅读</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — 核查每篇被引论文是否支持引用它的那句话：一个模型证明引文，Jev 打分，人来裁定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · marissafamularo · `JS` · 调用点 [`src/lib/typesafe.js`](https://github.com/MarissaFamularo/citation-verifier/blob/HEAD/src/lib/typesafe.js)，2026-09-22 阅读</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把关于家的类型化答案变成传感器，提供可用于自动化的 noul、choice 和 score 动作，以及一个对话代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · 调用点 [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py)，2026-09-30 阅读 · ⚠ `疑似 AI 生成` `作者自荐`</sub>

- **[hookmeter-jev](https://github.com/ehui1226/hookmeter-jev)** — 毫秒级的社交媒体爆款开头遥测与辅助工具（Chrome 扩展 + JEV System 1）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · ehui1226 · `Py` · 调用点 [`jev_mcp_server.py`](https://github.com/ehui1226/hookmeter-jev/blob/HEAD/jev_mcp_server.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge)** — 把 Jev 当作评估器使用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · danielgshea · `Py` · 调用点 [`src/evals/judges/__init__.py`](https://github.com/danielgshea/jev-as-a-judge/blob/HEAD/src/evals/judges/__init__.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · smkrv · `TS` · 调用点 [`src/client.ts`](https://github.com/smkrv/jev-calibrate/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · francoischastel · `TS` · 调用点 [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts)，2026-09-22 阅读</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。
  <sub>`开源项目` · ★10+ · `Rs` · `score` · `noul` · 调用点 [`src/client.rs`](https://github.com/AkashPriyadarshii/jev-curate/blob/HEAD/src/client.rs)，2026-09-22 阅读</sub>

- **[jev-dataops](https://github.com/RenaGao/jev-dataops)** — 由 Jev 驱动的开源工作台：流式数据筛选、质量评估、自动 LoRA 训练与留出集模型评估。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · renagao · `Py` · 调用点 [`jev_dataops/jev.py`](https://github.com/RenaGao/jev-dataops/blob/HEAD/jev_dataops/jev.py)，2026-09-24 阅读</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — 把语义决策变成普通 Ruby —— feels?、decide、score，以及 Rails 校验与模式匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · qew7 · `Rb` · 调用点 [`lib/jev/client.rb`](https://github.com/Qew7/jev-feels/blob/HEAD/lib/jev/client.rb)，2026-09-22 阅读</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 面向 Jev 式决策模型的开源训练与推理栈。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · zwlijay · `Py` · 引用文件 [`jevforge/bench_jev.py`](https://github.com/zwliJay/jev-forge/blob/HEAD/jevforge/bench_jev.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身` `仅一次提交`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★10+ · blakestone-x · `Py` · 调用点 [`jev_mcp/client.py`](https://github.com/blakestone-x/jev-mcp/blob/HEAD/jev_mcp/client.py)，2026-09-22 阅读</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★10+ · brainstormity · `Py` · `choice` · `noul` · 调用点 [`typesafe/__init__.py`](https://github.com/brainstormity/Jev-Moderation-Bot/blob/HEAD/typesafe/__init__.py)，2026-09-22 阅读</sub>

- **[JEV-Paper-Radar](https://github.com/Eliot5566/JEV-Paper-Radar)** — 让 Jev 每天早上读完 arXiv 的新论文，挑出少数值得你读的几篇。用自然语言描述兴趣，输出校准概率，每天约 0.06 美元，fork 即用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · eliot5566 · `Py` · 调用点 [`paper_radar/jev.py`](https://github.com/Eliot5566/JEV-Paper-Radar/blob/HEAD/paper_radar/jev.py)，2026-09-24 阅读</sub>

- **[jev-rs](https://github.com/yijunyu/jev-rs)** — 用一次 prefill 从任意 LLM 得到 System One 判断的 Rust 兼容服务。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · yijunyu · `Rs` · 调用点 [`src/backend/typesafe.rs`](https://github.com/yijunyu/jev-rs/blob/HEAD/src/backend/typesafe.rs)，2026-09-22 阅读</sub>

- **[jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers)** — 面向 AI 编程智能体的系统化开发框架，接入了 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · akashpriyadarshii · `TS` · 调用点 [`scripts/serve-laya.py`](https://github.com/AkashPriyadarshii/jev-superpowers/blob/HEAD/scripts/serve-laya.py)，2026-09-22 阅读</sub>

- **[jev-test-filter](https://github.com/mizchi/jev-test-filter)** — 用 Jev 给每个测试相对 git diff 打分，并产出测试框架所需的过滤参数。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · mizchi · `TS` · 调用点 [`src/jev.ts`](https://github.com/mizchi/jev-test-filter/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-yaba-wechat](https://github.com/wuxie888/jev-yaba-wechat)** — 微信里的话不知道怎么接？macOS 悬浮聊天助手：识别消息意图与沟通风险，GPT 生成多种话术，Jev 评估候选，一键填入微信。话我帮你想，发送你来定。
  <sub>`开源项目` · ★10+ · wuxie888 · `Py` · 调用点 [`src/judge_jev.py`](https://github.com/wuxie888/jev-yaba-wechat/blob/HEAD/src/judge_jev.py)，2026-09-24 阅读</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ray-hughes · `Rb` · 调用点 [`lib/jevalyn/configuration.rb`](https://github.com/Ray-Hughes/jevalyn/blob/HEAD/lib/jevalyn/configuration.rb)，2026-09-22 阅读</sub>

- **[jevflow](https://github.com/Mawfyy/jevflow)** — 把概率式 AI 决策做成可组合的后端原语。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · mawfyy · `TS` · 调用点 [`packages/provider-jev/src/index.ts`](https://github.com/Mawfyy/jevflow/blob/HEAD/packages/provider-jev/src/index.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ktaletsk · `Py` · 调用点 [`src/jevframe/_engine.py`](https://github.com/ktaletsk/jevframe/blob/HEAD/src/jevframe/_engine.py)，2026-09-22 阅读</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — 用一个不会生成文本的模型搭的聊天机器人（自回归驱动）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · bewinxed · `TS` · 调用点 [`src/jevgpt/sampler.py`](https://github.com/Bewinxed/jevgpt/blob/HEAD/src/jevgpt/sampler.py)，2026-09-22 阅读</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — 可配置的语义 lint，带文件级 NOUL 判断与一个「魔法字符串」插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · huntedman · `TS` · 调用点 [`src/jev-client.ts`](https://github.com/iamtoomas/JevLint/blob/HEAD/src/jev-client.ts)，2026-09-22 阅读</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · reachjalil · `JS` · 调用点 [`benchmarks/pager/run-jev-v2.mjs`](https://github.com/reachjalil/jevlogs/blob/HEAD/benchmarks/pager/run-jev-v2.mjs)，2026-09-22 阅读</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — 编程智能体的记忆：每条事实都是一句逐字引文，由 Jev 的校准置信度评级。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · romiluz13 · `Py` · 调用点 [`jevmory/cli.py`](https://github.com/romiluz13/jevmory/blob/HEAD/jevmory/cli.py)，2026-09-22 阅读</sub>

- **[JevScout](https://github.com/hqman/JevScout)** — 在真实公司官网上找工作的编码智能体技能：Chrome 负责看和操作，Jev 为每个链接和职位打分，宿主 LLM 从不决定点哪里。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · hqman · `Py` · 调用点 [`jev_job_hunter/jev.py`](https://github.com/hqman/JevScout/blob/HEAD/jev_job_hunter/jev.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jsort](https://github.com/keltokhy/jsort)** — 按含义排序：沿着一条用自然语言描述的维度给文本行排序，依据是 TypeSafe Jev 判定的两两比较。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · keltokhy · `Py` · 调用点 [`bench/local_models.py`](https://github.com/keltokhy/jsort/blob/HEAD/bench/local_models.py)，2026-09-24 阅读</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — 本地离线的 System One 服务，兼容 Jev API，回答类型化的是非问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · amithgc · `Py` · 调用点 [`src/local_jev/ui/app.js`](https://github.com/amithgc/local-jev/blob/HEAD/src/local_jev/ui/app.js)，2026-09-22 阅读</sub>

- **[MetaCog](https://github.com/ItIsCuthNotCup/MetaCog)** — 推理时的“元认知”：用一个小而快的裁判为大模型的答案打分并引导其推理；Jev 是它可用的裁判之一。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · itiscuthnotcup · `Py` · 调用点 [`examples/jev_best_of_n.py`](https://github.com/ItIsCuthNotCup/MetaCog/blob/HEAD/examples/jev_best_of_n.py)，2026-09-24 阅读</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — 给 omp 做的逐字保留式 Jev 打分上下文削减。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jerryfane · `TS` · 调用点 [`src/vendor/fast-jev/request.ts`](https://github.com/jerryfane/omp-jev-compaction/blob/HEAD/src/vendor/fast-jev/request.ts)，2026-09-22 阅读</sub>

- **[plugins](https://github.com/cline/plugins)** — Cline CLI 与扩展的官方精选插件集。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · cline · `TS` · 调用点 [`plugins/jev-browser/src/jev-model.ts`](https://github.com/cline/plugins/blob/HEAD/plugins/jev-browser/src/jev-model.ts)，2026-09-22 阅读</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — 开源的本地 Jev 替代品：一个有可证校准置信度的 System One 决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · rupeshpoojary9 · `Py` · 引用文件 [`crossbench/jev_client.py`](https://github.com/rupeshpoojary9/poorjev/blob/HEAD/crossbench/jev_client.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★10+ · `Py` · `sh` · `choice` · `score` · `noul` · 调用点 [`src/reflex_guard/providers/typesafe.py`](https://github.com/sharziki/semdecide/blob/HEAD/src/reflex_guard/providers/typesafe.py)，2026-09-22 阅读</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — 基于规则的文本评分器：每条规则并行跑过每一行，不跳读、不漏行。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · lukstei · `TS` · 调用点 [`src/providers/jev.ts`](https://github.com/lukstei/slop-grader/blob/HEAD/src/providers/jev.ts)，2026-09-22 阅读</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · myc0576 · `Py` · 调用点 [`src/smartmoney_cub_harness/jev/direct.py`](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — 识别 AI 写作痕迹的文风 linter：零依赖，可计数规则外加一个判断模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · danrwilloughby · `TS` · 调用点 [`src/jev.ts`](https://github.com/DanRWilloughby/snifftest/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[typed-decision-bert](https://github.com/hawkymisc/typed-decision-bert)** — 非官方概念验证：用 BERT 式编码器做类型化决策引擎。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · hawkymisc · `Py` · 调用点 [`src/jevbert/api/routes.py`](https://github.com/hawkymisc/typed-decision-bert/blob/HEAD/src/jevbert/api/routes.py)，2026-09-22 阅读</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — 用 Jev 筛选一整个文件夹的简历：类型化判断、可编辑的策略、免费重新打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · gtaras7 · `TS` · 调用点 [`cv-screen/src/cli.ts`](https://github.com/gtaras7/typesafe-jev/blob/HEAD/cv-screen/src/cli.ts)，2026-09-22 阅读</sub>

- **[Working-Memory-Jev](https://github.com/AustinAWay/Working-Memory-Jev)** — Passage：帮助教师找出教学文本中可能让学习者同时记住过多概念的地方，借助真实的 Jev API 追踪活跃的概念组与认知负荷的变化。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · austinaway · `Py` · 调用点 [`backend/jev.py`](https://github.com/AustinAWay/Working-Memory-Jev/blob/HEAD/backend/jev.py)，2026-09-24 阅读</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome 扩展：给你在 X 上滑过的每条帖子打上类型化 Jev 判断与实时评分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · oso95 · `TS` · 调用点 [`src/shared/jev.ts`](https://github.com/oso95/x-scanner/blob/HEAD/src/shared/jev.ts)，2026-09-22 阅读</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · compozy · `TS` · 调用点 [`benchmarks/jev-calibrate.ts`](https://github.com/compozy/yoshi/blob/HEAD/benchmarks/jev-calibrate.ts)，2026-09-22 阅读</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[a0-typesafe-ai](https://github.com/3clyp50/a0-typesafe-ai)** — 给 Agent Zero 的 Jev 判断，带类型化工具与概率卡片。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 3clyp50 · `Py` · 调用点 [`tools/typesafe_query.py`](https://github.com/3clyp50/a0-typesafe-ai/blob/HEAD/tools/typesafe_query.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[ai-provider-for-jev](https://github.com/soderlind/ai-provider-for-jev)** — 把 WordPress 接到 Jev 上做结构化决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · soderlind · `PHP` · 调用点 [`src/js/client.js`](https://github.com/soderlind/ai-provider-for-jev/blob/HEAD/src/js/client.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — 让 Aside 智能体用 Jev 做决策（Choice／Score／Noul）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · himomohi · `Py` · 调用点 [`src/aside_jev/jev.py`](https://github.com/himomohi/aside-jev/blob/HEAD/src/aside_jev/jev.py)，2026-09-22 阅读</sub>

- **[ask-jev-ai](https://github.com/waynesutton/ask-jev-ai)** — 一面公开的墙：任何人用三到十五个词提问，由 Jev 作答。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · waynesutton · `JS` · 调用点 [`convex/lib/typesafe.ts`](https://github.com/waynesutton/ask-jev-ai/blob/HEAD/convex/lib/typesafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[book-aurora](https://github.com/dani1005/book-aurora)** — Jev 几秒钟读完一整本小说，每个段落都变成一行颜色。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dani1005 · `TS` · 调用点 [`server/jev.ts`](https://github.com/dani1005/book-aurora/blob/HEAD/server/jev.ts)，2026-09-24 阅读</sub>

- **[clarity-judge](https://github.com/TypeSafeAI/clarity-judge)** — 由 TypeSafe AI Jev 模型驱动的多维度写作质量检查器：每项检查独立命名，各自给出结论。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · bunsdev · `TS` · 调用点 [`lib/jevClient.ts`](https://github.com/TypeSafeAI/clarity-judge/blob/HEAD/lib/jevClient.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[claude-jev](https://github.com/buchmark/claude-jev)** — Claude Code 插件：用 TypeSafe Jev 为审查发现、调试假设和设计方案打分，给出校准概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · buchmark · `TS` · 调用点 [`src/infrastructure/typesafe-jev.ts`](https://github.com/buchmark/claude-jev/blob/HEAD/src/infrastructure/typesafe-jev.ts)，2026-09-24 阅读</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop 钩子：核对 AI 助手的声明与它这轮实际读过的内容是否相符。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · vladyslavhontar · `Py` · 调用点 [`stop_verify.py`](https://github.com/VladyslavHontar/clear-head/blob/HEAD/stop_verify.py)，2026-09-22 阅读</sub>

- **[decide-mcp](https://github.com/dakdevs/decide-mcp)** — 可配置的决策 MCP server，带百分比分数与偏好画像。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · dakdevs · `TS` · 调用点 [`src/config.ts`](https://github.com/dakdevs/decide-mcp/blob/HEAD/src/config.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)** — 一个 agent 技能：识别出有界判断步骤，优先尝试用类型化决策模型解决。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · harrymunro · `Py` · 调用点 [`skills/decision-first/scripts/ask.py`](https://github.com/harrymunro/decision-first/blob/HEAD/skills/decision-first/scripts/ask.py)，2026-09-22 阅读</sub>

- **[deslop](https://github.com/yoichiojima-2/deslop)** — 给网页的广告、垃圾内容、SEO 和二手内容打分。一个基于 TypeSafe Jev 的智能体技能：每页四个概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · yoichiojima-2 · `Py` · 调用点 [`skills/deslop/jev.py`](https://github.com/yoichiojima-2/deslop/blob/HEAD/skills/deslop/jev.py)，2026-09-24 阅读</sub>

- **[draftpulse](https://github.com/pekth/draftpulse)** — 实验性的 X 草稿传播度实时评分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · pekth · `TS` · 调用点 [`server/analyze.ts`](https://github.com/pekth/draftpulse/blob/HEAD/server/analyze.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[dsh-jev](https://github.com/noetion/dsh-jev)** — 注册 jev_ask 的 DSH 包，提供 noul、choice、score 三种答案。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · noetion · `TS` · 调用点 [`src/client.ts`](https://github.com/noetion/dsh-jev/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nanami-0713 · `JS` · 调用点 [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — 给 DeepSeek Harness 的 Jev 判定式上下文压缩：语义化的工具结果裁剪。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · yangyu666 · `JS` · 调用点 [`jev.js`](https://github.com/yangyu666/dsh-jev-prune/blob/HEAD/jev.js)，2026-09-22 阅读</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — 给 DeepSeek Harness 的 Jev 决策工具与实时验证基准。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · xienda · `JS` · 调用点 [`lib/index.js`](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · kalyanm45 · `Py` · 调用点 [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev)** — 在同一输入上对比 GPT 的生成式语言与 JEV 的结构化 Noul 决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tanaypadar · `TS` · 调用点 [`lib/jev.ts`](https://github.com/TanayPadar/gpt-vs-jev/blob/HEAD/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — 评判智能体的每一步：通过／重试／升级／停止。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/harnessjudge/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · abdelstark · `TS` · 调用点 [`apps/server/src/jev.ts`](https://github.com/AbdelStark/heist-one/blob/HEAD/apps/server/src/jev.ts)，2026-09-22 阅读</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — 不确定时保持沉默的 issue 分拣：校准过的标签，含垃圾与重复检测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · emreozyoruk · `JS` · 调用点 [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[instruct-jev](https://github.com/ctaxnagomi/instruct-jev)** — INSTRUCT_JEV：Jev／System One 指令语料库（choice／noul／score）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ctaxnagomi · `Py` · 调用点 [`DeckerGUI_JEV-CorpusDGUI/build_instruct_jev.py`](https://github.com/ctaxnagomi/instruct-jev/blob/HEAD/DeckerGUI_JEV-CorpusDGUI/build_instruct_jev.py)，2026-09-22 阅读</sub>

- **[jev-as-quant](https://github.com/jiayylu/jev-as-quant)** — 把类型化 System-1 决策作为量化研究栈的判断层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jiayylu · `Py` · 调用点 [`src/jevquant/engines/jev.py`](https://github.com/jiayylu/jev-as-quant/blob/HEAD/src/jevquant/engines/jev.py)，2026-09-22 阅读</sub>

- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** — 二十个问题猜谜：一直问下去，直到 Jev 的校准置信度越过阈值。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · mintannn · `TS` · 调用点 [`lib/jev.ts`](https://github.com/mintannn/jev-asks-until-sure/blob/HEAD/lib/jev.ts)，2026-09-22 阅读</sub>

- **[jev-builder-loop](https://github.com/rainbowpuffpuff/jev-builder-loop)** — Grok 技能：把 Jev 当作构建者循环里的判断传感器（先验 × 概率 → 下一步）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · rainbowpuffpuff · `Py` · 调用点 [`scripts/loop.py`](https://github.com/rainbowpuffpuff/jev-builder-loop/blob/HEAD/scripts/loop.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-carryforward](https://github.com/dharun-cohere/jev-carryforward)** — 把上一轮会话知道的东西，对照这一轮正在做的事打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · dharundp6 · `TS` · 调用点 [`src/gateway.ts`](https://github.com/dharun-cohere/jev-carryforward/blob/HEAD/src/gateway.ts)，2026-09-22 阅读</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · nikkoxgonzales · `Py` · 调用点 [`jev_certify/analysis.py`](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py)，2026-09-22 阅读</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — 从不做摘要的 Hermes 会话上下文压缩：每次工具调用都被打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · picaye · `JS` · 调用点 [`hermes-compact.mjs`](https://github.com/picaye/jev-compaction/blob/HEAD/hermes-compact.mjs)，2026-09-22 阅读</sub>

- **[jev-decision-lab](https://github.com/jlov7/jev-decision-lab)** — 一个本地实验室，观察 Jev 在真实业务场景上的判断表现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jlov7 · `Py` · 调用点 [`jev_lab/adapters.py`](https://github.com/jlov7/jev-decision-lab/blob/HEAD/jev_lab/adapters.py)，2026-09-22 阅读</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — 面向智能体的 Haskell DSL：类型化数据包、类型推断，答案与问题同构。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · inanna-malick · `Hs` · 调用点 [`scripts/curate-fixtures.py`](https://github.com/inanna-malick/jev-dsl/blob/HEAD/scripts/curate-fixtures.py)，2026-09-22 阅读</sub>

- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** — 开源的 jev-flash-router：给 Jev 的 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ravinder82 · `TS` · 调用点 [`dist/index.js`](https://github.com/Ravinder82/jev-flash-router/blob/HEAD/dist/index.js)，2026-09-22 阅读</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — 给 Claude Code 的六道校准闸门：规则、范围、意图、完成度等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · rashedint32 · `JS` · 调用点 [`lib/jev.mjs`](https://github.com/rashedInt32/jev-gates/blob/HEAD/lib/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-hooks](https://github.com/microchipgnu/jev-hooks)** — 把类型化 Jev 判断组合成 React 与后端程序里的响应式语义状态。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · microchipgnu · `TS` · 调用点 [`src/adapters/typesafe.ts`](https://github.com/microchipgnu/jev-hooks/blob/HEAD/src/adapters/typesafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-judgment](https://github.com/HyunjunJeon/jev-judgment)** — Agent 技能：把编程智能体的封闭式判断交给 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · hyunjunjeon · `Py` · 调用点 [`skills/jev-judgment/scripts/jev.py`](https://github.com/HyunjunJeon/jev-judgment/blob/HEAD/skills/jev-judgment/scripts/jev.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — 以基准驱动的 Jev 路由器与评判者，服务于成本可控的 LLM 编程流程。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · erendikmenn · `Py` · 调用点 [`src/jev_router/providers/review.py`](https://github.com/erendikmenn/jev-llm-router-benchmark/blob/HEAD/src/jev_router/providers/review.py)，2026-09-22 阅读</sub>

- **[jev-local](https://github.com/us/jev-local)** — 本地的 Jev 兼容评估服务：POST /v1/systemone，支持类型化的 noul／choice／score。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · us · `Py` · 引用文件 [`src/jevlocal/app.py`](https://github.com/us/jev-local/blob/HEAD/src/jevlocal/app.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — Jev 的 MCP server：提供官方三种问题类型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · wangkuangkuang · `Py` · 调用点 [`src/jev_mcp_server/config.py`](https://github.com/wangkuangkuang/jev-mcp-server/blob/HEAD/src/jev_mcp_server/config.py)，2026-09-22 阅读</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — 编程智能体总在不难的决策上烧上下文 —— 分拣 400 条工单之类的活儿不该这么贵。 <sub>(机翻)</sub>
  <sub>`开源项目` · ddfeyes · `Py` · 调用点 [`src/jev_mode/client.py`](https://github.com/ddfeyes/jev-mode/blob/HEAD/src/jev_mode/client.py)，2026-09-22 阅读</sub>

- **[jev-model-router](https://github.com/lucianfialho/jev-model-router)** — 用 Jev 做成本优化的 OpenRouter 模型路由，带实时全目录。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lucianfialho · `Py` · 调用点 [`src/model_router/classifier.py`](https://github.com/lucianfialho/jev-model-router/blob/HEAD/src/model_router/classifier.py)，2026-09-22 阅读</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · scienthoon · `Py` · 调用点 [`scripts/jev_eval.mjs`](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · yodablocks · `Py` · 调用点 [`harness/client.py`](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py)，2026-09-22 阅读</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — 证据门控的 Jev 问题包注册表：精选问题、黄金样例与实测证据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dtduc-git · `Py` · 调用点 [`scripts/refresh.py`](https://github.com/dtduc-git/jev-packs/blob/HEAD/scripts/refresh.py)，2026-09-22 阅读</sub>

- **[jev-paper-judge](https://github.com/JacobLinCool/jev-paper-judge)** — 几秒内给出论文反馈。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jacoblincool · `TS` · 调用点 [`scripts/lib/typesafe.mjs`](https://github.com/JacobLinCool/jev-paper-judge/blob/HEAD/scripts/lib/typesafe.mjs)，2026-09-22 阅读</sub>

- **[jev-rl](https://github.com/Bring-AI/jev-rl)** — JEV 强化学习：用 JEV 提供的奖励训练四款经典游戏，附可复现实验与检查点。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · bring-ai · `Py` · 调用点 [`src/jev_reward/judges.py`](https://github.com/Bring-AI/jev-rl/blob/HEAD/src/jev_reward/judges.py)，2026-09-24 阅读</sub>

- **[jev-score](https://github.com/a-Fig/jev-score)** — 由 Jev 驱动的本地优先文档评估工作区。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · a-fig · `JS` · 调用点 [`src/jev.mjs`](https://github.com/a-Fig/jev-score/blob/HEAD/src/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — 由 Jev 打分驱动的开源仓库与 crate 侦察工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · akashpriyadarshii · `Rs` · 调用点 [`src/jev.rs`](https://github.com/AkashPriyadarshii/jev-scout/blob/HEAD/src/jev.rs)，2026-09-22 阅读</sub>

- **[jev-seo](https://github.com/DeployMates/jev-seo)** — 审计企业网站的 SEO 与 AI 搜索引擎可见性。确定性爬虫先测量每个页面，然后用一次请求把一批狭窄的类型化问题发给 Jev，答案以概率形式呈现在看板上。 <sub>(机翻)</sub>
  <sub>`开源项目` · vakandi · `TS` · `choice` · `score` · `noul` · 调用点 [`server/src/jevClient.ts`](https://github.com/DeployMates/jev-seo/blob/HEAD/server/src/jevClient.ts)，2026-09-30 阅读 · ⚠ `代码未实测` `无许可证` `疑似 AI 生成` `作者自荐`</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — 给某 lint 工具做的二次评估：用 Jev 评判 linter 的判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · blas0 · `JS` · 调用点 [`run-rule-cases.mjs`](https://github.com/blas0/jev-shadcn-lint-eval/blob/HEAD/run-rule-cases.mjs)，2026-09-22 阅读</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · shivampansuriya · `JS` · 调用点 [`src/providers/typesafe.mjs`](https://github.com/ShivamPansuriya/jev-skill-gate/blob/HEAD/src/providers/typesafe.mjs)，2026-09-24 阅读</sub>

- **[jev-songwriter](https://github.com/beingcognitive/jev-songwriter)** — 一个一个音符都写不出的决策模型却写出了歌：代码负责计算，Jev 负责评判。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · beingcognitive · `JS` · 调用点 [`lib/jev.js`](https://github.com/beingcognitive/jev-songwriter/blob/HEAD/lib/jev.js)，2026-09-22 阅读</sub>

- **[Jev-test](https://github.com/WeSecureYou/Jev-test)** — 一个 CLI 与 REST API：让 Jev 评估某个职业受 AI 裁员冲击的程度、未来走向、对人类问责的需要以及整体韧性。 <sub>(机翻)</sub>
  <sub>`开源项目` · wesecureyou · `TS` · 调用点 [`src/services/jevClient.ts`](https://github.com/WeSecureYou/Jev-test/blob/HEAD/src/services/jevClient.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — 把 Jev 的 noul 原语应用到一个共谋语料库上。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · sypherin · `Py` · 调用点 [`jev_client.py`](https://github.com/sypherin/jev-trace-classifier/blob/HEAD/jev_client.py)，2026-09-22 阅读</sub>

- **[jev-ui](https://github.com/etweisberg/jev-ui)** — React 组件：由决策模型决定渲染哪个组件、列表如何排序、是否展示。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · etweisberg · `TS` · 调用点 [`packages/jev-ui/src/transport/live.ts`](https://github.com/etweisberg/jev-ui/blob/HEAD/packages/jev-ui/src/transport/live.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-workbench](https://github.com/molis-ai/jev-workbench)** — 在 Jev 之上构建带版本的判断函数，之后反复调用同一个已发布版本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · molis-ai · `TS` · 调用点 [`apps/server/src/provider.ts`](https://github.com/molis-ai/jev-workbench/blob/HEAD/apps/server/src/provider.ts)，2026-09-22 阅读</sub>

- **[jev-wrapped](https://github.com/gaborishka/jev-wrapped)** — Telegram 频道年度透视：Jev 评判一年的帖子，生成一张卡片，跑在一个 Cloudflare Worker 上。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · gaborishka · `JS` · 调用点 [`shared/jev.js`](https://github.com/gaborishka/jev-wrapped/blob/HEAD/shared/jev.js)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — 先评估再信任：实战笔记、可运行脚本与一个 agent 技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · elshinq · `JS` · 调用点 [`scripts/jev.mjs`](https://github.com/ElshinQ/jevaluate/blob/HEAD/scripts/jev.mjs)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jevbus](https://github.com/zkjoie/jevbus)** — 一个流式事件总线：路由、订阅与消费都由概率决策决定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · zkjoie · `Rs` · 调用点 [`src/jev/http.rs`](https://github.com/zkjoie/jevbus/blob/HEAD/src/jev/http.rs)，2026-09-22 阅读</sub>

- **[jevchess](https://github.com/choxos/jevchess)** — 让 Jev 与任意 OpenRouter 模型、Stockfish 或你本人下国际象棋，单页网页应用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · choxos · `JS` · 调用点 [`docs/chess-ai.js`](https://github.com/choxos/jevchess/blob/HEAD/docs/chess-ai.js)，2026-09-22 阅读</sub>

- **[jevmetrics](https://github.com/ishantanu/jevmetrics)** — 一个实验性的 OpenTelemetry Collector 指标处理器：根据元数据让 Jev 判断每个指标在运维上的价值，再由确定性策略决定保留哪些。 <sub>(机翻)</sub>
  <sub>`开源项目` · ishantanu · `Go` · 调用点 [`internal/evaluator/jev.go`](https://github.com/ishantanu/jevmetrics/blob/HEAD/internal/evaluator/jev.go)，2026-09-24 阅读</sub>

- **[jevmoji](https://github.com/cheeaun/jevmoji)** — 输入任意内容，得到由 Jev 打分（0–3）的相关表情符号。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cheeaun · `JS` · 调用点 [`js/jev-chunked.js`](https://github.com/cheeaun/jevmoji/blob/HEAD/js/jev-chunked.js)，2026-09-24 阅读</sub>

- **[jevplay](https://github.com/ndolinschi/jevplay)** — Jev playground：自定义 Choice／Score／Noul 构造器，带实时概率分布。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/jevplay/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach)** — 给你向编码智能体提问的方式打分，并显示你的习惯是否在进步的 Claude Code 插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · crowdlinker · `TS` · 调用点 [`src/jev.ts`](https://github.com/CrowdLinker/JevPromptCoach/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[jevriel](https://github.com/thehan-co/jevriel)** — 给你的 AI 装上 JEV 的翅膀：用于构建与升级的技能与插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · thehan-co · `JS` · 调用点 [`vendor/typesafe-as-a-judge/judge.mjs`](https://github.com/thehan-co/jevriel/blob/HEAD/vendor/typesafe-as-a-judge/judge.mjs)，2026-09-22 阅读</sub>

- **[jevseek](https://github.com/morcoan/JMP)** — 本地编程工作区：由 Jev 路由动作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · morcoan · `Py` · 调用点 [`benchmarks/compare_deliberation.py`](https://github.com/morcoan/JMP/blob/HEAD/benchmarks/compare_deliberation.py)，2026-09-22 阅读 · ⚠ `已归档`</sub>

- **[jevseo](https://github.com/epergaboni/jevseo)** — 由 Jev 驱动的类型化 SEO／AEO／GEO 判断，代码掌管其余。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · epergaboni · `TS` · 调用点 [`src/lib/typesafe/client.ts`](https://github.com/epergaboni/jevseo/blob/HEAD/src/lib/typesafe/client.ts)，2026-09-22 阅读</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — 亚 100 毫秒的智能体工具调用安全闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lgy1027 · `Py` · 调用点 [`jevshield/client.py`](https://github.com/lgy1027/jevshield/blob/HEAD/jevshield/client.py)，2026-09-22 阅读</sub>

- **[judging-with-typesafe](https://github.com/carlsonchik/judging-with-typesafe)** — 给 Letta 智能体的技能：通过 System One 按给定标准做判断（俄语）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · carlsonchik · `Py` · 调用点 [`skills/judging-with-typesafe/scripts/typesafe.py`](https://github.com/carlsonchik/judging-with-typesafe/blob/HEAD/skills/judging-with-typesafe/scripts/typesafe.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[leanest](https://github.com/baronunread/leanest)** — 本地优先的测试选择器：用 Jev 判断哪些测试受某次变更影响。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · baronunread · `TS` · 调用点 [`packages/judge/src/providers/jev.ts`](https://github.com/baronunread/leanest/blob/HEAD/packages/judge/src/providers/jev.ts)，2026-09-22 阅读</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — 一个 Stop 钩子，阻止编程智能体过早收工 —— 用大白话写规则，由 Jev 裁定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · noplan-inc · `Py` · 调用点 [`limpet.py`](https://github.com/noplan-inc/limpet/blob/HEAD/limpet.py)，2026-09-22 阅读</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — 由 Jev 驱动的 LlamaIndex 重排器与路由器 —— 类型化的分数与选择，比 LLM-as-judge 便宜。 <sub>(机翻)</sub>
  <sub>`开源项目` · wiktorb2004 · `Py` · 调用点 [`packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py`](https://github.com/WiktorB2004/llama-index-jev/blob/HEAD/packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py)，2026-09-22 阅读</sub>

- **[luce](https://github.com/scienthoon/luce)** — Luce：一份校准决策模型的配方 —— 输入一句任务描述，产出一个小模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · scienthoon · `Py` · 调用点 [`scripts/jev_eval.mjs`](https://github.com/scienthoon/luce/blob/HEAD/scripts/jev_eval.mjs)，2026-09-22 阅读</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — Jev 的 n8n 社区节点：带校准概率的文本分类、打分与检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · khmuhtadin · `TS` · 调用点 [`nodes/JevClassification/JevClassification.node.ts`](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/HEAD/nodes/JevClassification/JevClassification.node.ts)，2026-09-22 阅读</sub>

- **[n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** — 面向 System One API 的 n8n 社区节点：类型化的是非、选择与打分问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dommonte · `TS` · 调用点 [`nodes/TypeSafeAi/constants.ts`](https://github.com/DomMonte/n8n-nodes-typesafe-ai/blob/HEAD/nodes/TypeSafeAi/constants.ts)，2026-09-22 阅读</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — 给 OMP 的模型裁决式权限闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · strml · `TS` · 调用点 [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts)，2026-09-22 阅读 · ⚠ `已归档`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — 来自某土地开发 SaaS 的类型化决策基准：schema、匿名标注数据与运行器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · zsavage8 · `Py` · 调用点 [`scripts/run_baseline.py`](https://github.com/zsavage8/padflow-jev-evals/blob/HEAD/scripts/run_baseline.py)，2026-09-22 阅读</sub>

- **[pagegrade](https://github.com/kitze/pagegrade)** — 给页面各区块的清晰度、文案与页面 SEO 打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kitze · `TS` · 调用点 [`lib/jev.ts`](https://github.com/kitze/pagegrade/blob/HEAD/lib/jev.ts)，2026-09-22 阅读</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — 给 Pi 编程智能体的 Jev 权限闸门：审判每一次 bash 与写入。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kurihada · `TS` · 调用点 [`src/jev.ts`](https://github.com/kurihada/pi-jev-permit/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · legacybridge-tech · `TS` · 调用点 [`src/client.ts`](https://github.com/legacybridge-tech/pi-typesafe-jev/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[prompt2jev](https://github.com/sumleo/prompt2jev)** — 把自然语言、LLM 提示或跑提示的代码，转换成一个 Jev 决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · sumleo · `Py` · 调用点 [`skills/prompt2jev/scripts/prompt2jev.py`](https://github.com/sumleo/prompt2jev/blob/HEAD/skills/prompt2jev/scripts/prompt2jev.py)，2026-09-22 阅读</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — 给 pytest 的语义断言：测试 LLM 应用输出的含义，由 Jev 判定。 <sub>(机翻)</sub>
  <sub>`插件` · allebee · `Py` · 调用点 [`src/pytest_jev/judge.py`](https://github.com/allebee/pytest-jev/blob/HEAD/src/pytest_jev/judge.py)，2026-09-22 阅读</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — 基于 Qwen3.5-0.8B 的 Jev 风格校准决策模型（Choice／Score／Noul）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · shamazharikh · `Py` · 引用文件 [`scripts/bench_fork.py`](https://github.com/shamazharikh/qwen-rlcd/blob/HEAD/scripts/bench_fork.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[s1-rs](https://github.com/AbdelStark/s1-rs)** — Rust 的类型化 System One 层（Choice／Score／Noul）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · abdelstark · `Rs` · 调用点 [`crates/s1/src/typesafe_rs.rs`](https://github.com/AbdelStark/s1-rs/blob/HEAD/crates/s1/src/typesafe_rs.rs)，2026-09-22 阅读</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One 搜索：用类型化判断与仓库证据导航与追踪代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cpaczek · `TS` · 调用点 [`src/client.ts`](https://github.com/cpaczek/s1s/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town：客厅电视上的社交推理派对游戏，由 Jev 主持。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tpaulshippy · `Rb` · 调用点 [`lib/shady_town/evaluator.rb`](https://github.com/tpaulshippy/shady-town/blob/HEAD/lib/shady_town/evaluator.rb)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — 开源 Chrome 扩展：用 Jev 过滤 AI 生成的文字与广告。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · neddes · `JS` · 调用点 [`background.js`](https://github.com/neddes/sloppy-jevs-extension/blob/HEAD/background.js)，2026-09-22 阅读</sub>

- **[spendbrake](https://github.com/ndolinschi/spendbrake)** — 智能体预算刹车：继续／降级模型／停止。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/spendbrake/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[system-one-gemma](https://github.com/akash-kamat/system-one-gemma)** — 开源的 Jev 式 System One 决策模型：Gemma 3 270M 加一个打分头。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · akash-kamat · `Py` · 引用文件 [`system_one.py`](https://github.com/akash-kamat/system-one-gemma/blob/HEAD/system_one.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server 兼 agent 技能：把一个判断分解成多个类型化问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · simota · `TS` · 调用点 [`skills/tenbin/scripts/evaluate.py`](https://github.com/simota/tenbin/blob/HEAD/skills/tenbin/scripts/evaluate.py)，2026-09-22 阅读</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — 面向 AI 智能体的开源自动模式：一个校准过的工具调用防火墙。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · riskaversetech · `TS` · 调用点 [`src/backends/typesafe.ts`](https://github.com/RiskAverseTech/toolgate/blob/HEAD/src/backends/typesafe.ts)，2026-09-22 阅读</sub>

- **[transcript-scorecard](https://github.com/brandonbryant12/transcript-scorecard)** — 实时客服通话评分演示。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · brandonbryant12 · `TS` · 调用点 [`apps/api/src/classifier.ts`](https://github.com/brandonbryant12/transcript-scorecard/blob/HEAD/apps/api/src/classifier.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — 在用户看到之前先审判每一条 LLM 响应。提供 AI SDK middleware 与 OpenAI 兼容代理。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · noelzappy · `TS` · 调用点 [`src/judge/jev.ts`](https://github.com/noelzappy/tripwire/blob/HEAD/src/judge/jev.ts)，2026-09-22 阅读</sub>

- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** — Jev 形状的类型化决策模型：状态加问题进，校准概率出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kotoba-lang · `Py` · 调用点 [`src/typed_decisions/jev_holes.py`](https://github.com/kotoba-lang/typed-decisions/blob/HEAD/src/typed_decisions/jev_holes.py)，2026-09-22 阅读</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — 给 Codex 与 Claude Code 的非官方社区 MCP 插件，用 Jev 做有界路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · e-fl · `JS` · 调用点 [`server/judge.mjs`](https://github.com/E-FL/typesafe-as-a-judge/blob/HEAD/server/judge.mjs)，2026-09-22 阅读</sub>

- **[typesafe-cli](https://github.com/y0usaf/typesafe-cli)** — 在 shell 里向 Jev 提类型化问题：noul、choice、score 都以数字返回，而不是散文。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · y0usaf · `TS` · 调用点 [`src/cli.ts`](https://github.com/y0usaf/typesafe-cli/blob/HEAD/src/cli.ts)，2026-09-22 阅读</sub>

- **[typesafe-demo-mcp](https://github.com/bestagentkits/typesafe-demo-mcp)** — 把 System One 判断暴露成智能体工具的 MCP server。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · bestagentkits · `TS` · 调用点 [`src/typesafe.ts`](https://github.com/bestagentkits/typesafe-demo-mcp/blob/HEAD/src/typesafe.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[typesafe-jev-bridge](https://github.com/RevocGG/typesafe-jev-bridge)** — 在任何地方使用 Jev：零依赖的 OpenAI 兼容封装。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · revocgg · `JS` · 调用点 [`typesafe-bridge/demo.py`](https://github.com/RevocGG/typesafe-jev-bridge/blob/HEAD/typesafe-bridge/demo.py)，2026-09-22 阅读</sub>

- **[typesafe-local](https://github.com/aabolfazl/typesafe-local)** — 受 TypeSafe 启发：向本地 LLM 提类型化问题，拿到校准概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · aabolfazl · `Py` · 调用点 [`ots/server.py`](https://github.com/aabolfazl/typesafe-local/blob/HEAD/ots/server.py)，2026-09-22 阅读</sub>

- **[typesafe-oracles](https://github.com/trophee-bot/typesafe-oracles)** — 评估 System One 三原语：类型化的裁决在哪些场景胜过生成式模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · trophee-bot · `JS` · 调用点 [`probes/run-arms.mjs`](https://github.com/trophee-bot/typesafe-oracles/blob/HEAD/probes/run-arms.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase)** — 展示 Jev 的 Next.js 界面：并行 Noul 判断与实时结果。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ashadeepa · `TS` · 调用点 [`lib/typesafe-client.ts`](https://github.com/Ashadeepa/typesafe-showcase/blob/HEAD/lib/typesafe-client.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — 基于 Jev 的三条可组合判断流水线：工单分拣、可观测性等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shivam2003-dev · `Py` · 调用点 [`src/triage/mock.py`](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/HEAD/src/triage/mock.py)，2026-09-22 阅读</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — 用 Typesafe.AI 生成 diff 审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rbalch · `Py` · 调用点 [`src/typesafe_review/ask.py`](https://github.com/rbalch/typesafeai-review/blob/HEAD/src/typesafe_review/ask.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[vgi-typesafe](https://github.com/Query-farm/vgi-typesafe)** — 一个 VGI worker，把 System One 的 choice／noul／score 以可 LATERAL 连接的表函数形式暴露给 DuckDB／SQL。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · query-farm · `Py` · 调用点 [`vgi_typesafe/typesafe_api.py`](https://github.com/Query-farm/vgi-typesafe/blob/HEAD/vgi_typesafe/typesafe_api.py)，2026-09-22 阅读</sub>

- **[watfile](https://github.com/jexp/watfile)** — 用 Jev 或本地校准决策模型给文本与 PDF 分类归档。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jexp · `Py` · 调用点 [`src/watfile/classifier/jev.py`](https://github.com/jexp/watfile/blob/HEAD/src/watfile/classifier/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — 给编程智能体的类型化判断层：从需求文档到发布的各道闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · zahrannnn · `TS` · 调用点 [`src/backends/jev.ts`](https://github.com/Zahrannnn/zcode-jev/blob/HEAD/src/backends/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
