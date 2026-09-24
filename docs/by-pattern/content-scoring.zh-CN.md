# 内容评分

<sub>[awesome-jev](../../README.zh-CN.md) · [English](content-scoring.md)</sub>

_在有序量表上给质量、风险或相关性打分。_

这个决策的全部已收录例子 —— 共 164 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#内容评分)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐ — 把一个笼统的判断拆成若干原子评分，再用你自己代码里的权重（而不是提示词里的）组合起来。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★87,298 · `TS` · `choice` · ⚠ `仅影子运行`</sub>

- **[gptcache](https://github.com/zilliztech/GPTCache)** — 面向 LLM 的语义缓存，已完整集成主流框架。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8,201 · zilliztech · `Py`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★5,414 · `Java` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★4,578 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
  <sub>`开源项目` · ★582 · `TS` · `choice` · `score` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★324 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[llm2jev](https://github.com/Yinsongxu/LLM2Jev)** — 把本地语言模型改造成 Jev 兼容的结构化决策引擎，输出 Choice、Score、Noul。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★286 · yinsongxu · `Py`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — 一个本地优先的 MCP 插件，供编程智能体做持续的代码质量审查。
  <sub>`插件` · ★217 · niazmorshed2007 · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★173 · `JS` · `choice` · `score` · `noul`</sub>

- **[killmyidea](https://github.com/monteduro/killmyidea)** — 输入一个创业点子，Jev 从多个维度打分，最后给你 KILL、FIX 或 SHIP。
  <sub>`开源项目` · ★147 · `TS` · `score` · `choice` · ⚠ `无许可证`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接 40 家 AI 供应商，覆盖生成、流式与决策三种推理形态。 <sub>(机翻)</sub>
  <sub>`插件` · ★139 · juspay · `TS`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — 按含义 grep，跨语言：Jev 给每一行按含义打分，可用 AND/OR/NOT 组合多个含义。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★134 · uehaj · `JS`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — 给编程智能体用的代码质量与覆盖率判断，Rust 实现。
  <sub>`开源项目` · ★109 · supercorp-ai · `Rs`</sub>

- **[jevmeter](https://github.com/ChetasLua/jevmeter)** — 给视频里的每一句话打分，并把结果渲染成一个实时仪表。
  <sub>`开源项目` · ★81 · chetaslua · `Py`</sub>

- **[jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge)** — 把 Jev 当作评估器使用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★80 · danielgshea · `Py` · ⚠ `无许可证`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — 用 Jev 打分器给代码中的文本做 lint。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★78 · mizchi · `TS`</sub>

- **[jev-seo](https://github.com/AgriciDaniel/jev-seo)** — 从一个首页网址出发，对任意网站做实时 SEO 审计，由 Jev 判定，输出 PDF、XLSX 和 Markdown 报告。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★78 · agricidaniel · `Py`</sub>

- **[Working-Memory-Jev](https://github.com/AustinAWay/Working-Memory-Jev)** — Passage：帮助教师找出教学文本中可能让学习者同时记住过多概念的地方，借助真实的 Jev API 追踪活跃的概念组与认知负荷的变化。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★75 · austinaway · `Py`</sub>

- **[jev-dataops](https://github.com/RenaGao/jev-dataops)** — 由 Jev 驱动的开源工作台：流式数据筛选、质量评估、自动 LoRA 训练与留出集模型评估。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★54 · renagao · `Py`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★53 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。
  <sub>`开源项目` · ★45 · `Rs` · `score` · `noul`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★44 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 面向 Jev 式决策模型的开源训练与推理栈。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★34 · zwlijay · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[JevScout](https://github.com/hqman/JevScout)** — 在真实公司官网上找工作的编码智能体技能：Chrome 负责看和操作，Jev 为每个链接和职位打分，宿主 LLM 从不决定点哪里。 <sub>(机翻)</sub>
  <sub>`插件` · ★33 · hqman · `Py` · ⚠ `无许可证`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · smkrv · `TS`</sub>

- **[plugins](https://github.com/cline/plugins)** — Cline CLI 与扩展的官方精选插件集。 <sub>(机翻)</sub>
  <sub>`插件` · ★31 · cline · `TS`</sub>

- **[typed-decision-bert](https://github.com/hawkymisc/typed-decision-bert)** — 非官方概念验证：用 BERT 式编码器做类型化决策引擎。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · hawkymisc · `Py`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — 识别 AI 写作痕迹的文风 linter：零依赖，可计数规则外加一个判断模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★29 · danrwilloughby · `TS`</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — 用一个不会生成文本的模型搭的聊天机器人（自回归驱动）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★26 · bewinxed · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★26 · myc0576 · `Py`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(机翻)</sub>
  <sub>`插件` · ★25 · compozy · `TS`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★22 · blakestone-x · `Py`</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — 基于规则的文本评分器：每条规则并行跑过每一行，不跳读、不漏行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★22 · lukstei · `TS`</sub>

- **[hookmeter-jev](https://github.com/ehui1226/hookmeter-jev)** — 毫秒级的社交媒体爆款开头遥测与辅助工具（Chrome 扩展 + JEV System 1）。 <sub>(机翻)</sub>
  <sub>`插件` · ★21 · ehui1226 · `Py`</sub>

- **[jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers)** — 面向 AI 编程智能体的系统化开发框架，接入了 Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★21 · akashpriyadarshii · `TS`</sub>

- **[jev-yaba-wechat](https://github.com/wuxie888/jev-yaba-wechat)** — 微信里的话不知道怎么接？macOS 悬浮聊天助手：识别消息意图与沟通风险，GPT 生成多种话术，Jev 评估候选，一键填入微信。话我帮你想，发送你来定。
  <sub>`开源项目` · ★21 · wuxie888 · `Py`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19 · ray-hughes · `Rb`</sub>

- **[jsort](https://github.com/keltokhy/jsort)** — 按含义排序：沿着一条用自然语言描述的维度给文本行排序，依据是 TypeSafe Jev 判定的两两比较。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19 · keltokhy · `Py`</sub>

- **[MetaCog](https://github.com/ItIsCuthNotCup/MetaCog)** — 推理时的“元认知”：用一个小而快的裁判为大模型的答案打分并引导其推理；Jev 是它可用的裁判之一。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★18 · itiscuthnotcup · `Py`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome 扩展：给你在 X 上滑过的每条帖子打上类型化 Jev 判断与实时评分。 <sub>(机翻)</sub>
  <sub>`插件` · ★17 · oso95 · `TS`</sub>

- **[jev-test-filter](https://github.com/mizchi/jev-test-filter)** — 用 Jev 给每个测试相对 git diff 打分，并产出测试框架所需的过滤参数。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★16 · mizchi · `TS`</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(机翻)</sub>
  <sub>`插件` · ★15 · francoischastel · `TS`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · ktaletsk · `Py`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — 可配置的语义 lint，带文件级 NOUL 判断与一个「魔法字符串」插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★11 · huntedman · `TS`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · reachjalil · `JS`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — 把语义决策变成普通 Ruby —— feels?、decide、score，以及 Rails 校验与模式匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · qew7 · `Rb`</sub>

- **[anydecisionmodel](https://github.com/mattt/AnyDecisionModel)** — 一个 Swift 包：从语言模型获取类型化决策（概率、选择与分数）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · mattt · `Swift`</sub>

- **[jevflow](https://github.com/Mawfyy/jevflow)** — 把概率式 AI 决策做成可组合的后端原语。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★9 · mawfyy · `TS` · ⚠ `无许可证`</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — 编程智能体的记忆：每条事实都是一句逐字引文，由 Jev 的校准置信度评级。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · romiluz13 · `Py`</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — 让 Aside 智能体用 Jev 做决策（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★8 · himomohi · `Py`</sub>

- **[jev-rs](https://github.com/yijunyu/jev-rs)** — 用一次 prefill 从任意 LLM 得到 System One 判断的 Rust 兼容服务。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · yijunyu · `Rs`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — 给 omp 做的逐字保留式 Jev 打分上下文削减。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · jerryfane · `TS`</sub>

- **[typesafe-local](https://github.com/aabolfazl/typesafe-local)** — 受 TypeSafe 启发：向本地 LLM 提类型化问题，拿到校准概率。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · aabolfazl · `Py`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — 核查每篇被引论文是否支持引用它的那句话：一个模型证明引文，Jev 打分，人来裁定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · marissafamularo · `JS`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · abdelstark · `TS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — 面向智能体的 Haskell DSL：类型化数据包、类型推断，答案与问题同构。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · inanna-malick · `Hs`</sub>

- **[JEV-Paper-Radar](https://github.com/Eliot5566/JEV-Paper-Radar)** — 让 Jev 每天早上读完 arXiv 的新论文，挑出少数值得你读的几篇。用自然语言描述兴趣，输出校准概率，每天约 0.06 美元，fork 即用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · eliot5566 · `Py`</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — 本地离线的 System One 服务，兼容 Jev API，回答类型化的是非问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · amithgc · `Py`</sub>

- **[luce](https://github.com/scienthoon/luce)** — Luce：一份校准决策模型的配方 —— 输入一句任务描述，产出一个小模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · scienthoon · `Py`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — 开源的本地 Jev 替代品：一个有可证校准置信度的 System One 决策层。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★7 · rupeshpoojary9 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · scienthoon · `Py`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — 用 Jev 筛选一整个文件夹的简历：类型化判断、可编辑的策略、免费重新打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · gtaras7 · `TS`</sub>

- **[a0-typesafe-ai](https://github.com/3clyp50/a0-typesafe-ai)** — 给 Agent Zero 的 Jev 判断，带类型化工具与概率卡片。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · 3clyp50 · `Py`</sub>

- **[book-aurora](https://github.com/dani1005/book-aurora)** — Jev 几秒钟读完一整本小说，每个段落都变成一行颜色。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · dani1005 · `TS`</sub>

- **[claude-jev](https://github.com/buchmark/claude-jev)** — Claude Code 插件：用 TypeSafe Jev 为审查发现、调试假设和设计方案打分，给出校准概率。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · buchmark · `TS`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · shivampansuriya · `JS`</sub>

- **[jevchess](https://github.com/choxos/jevchess)** — 让 Jev 与任意 OpenRouter 模型、Stockfish 或你本人下国际象棋，单页网页应用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · choxos · `JS`</sub>

- **[jevmoji](https://github.com/cheeaun/jevmoji)** — 输入任意内容，得到由 Jev 打分（0–3）的相关表情符号。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · cheeaun · `JS`</sub>

- **[jevriel](https://github.com/thehan-co/jevriel)** — 给你的 AI 装上 JEV 的翅膀：用于构建与升级的技能与插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · thehan-co · `JS`</sub>

- **[pagegrade](https://github.com/kitze/pagegrade)** — 给页面各区块的清晰度、文案与页面 SEO 打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · kitze · `TS`</sub>

- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** — Jev 形状的类型化决策模型：状态加问题进，校准概率出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · kotoba-lang · `Py`</sub>

- **[ai-provider-for-jev](https://github.com/soderlind/ai-provider-for-jev)** — 把 WordPress 接到 Jev 上做结构化决策。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★4 · soderlind · `PHP` · ⚠ `无许可证`</sub>

- **[jevseo](https://github.com/epergaboni/jevseo)** — 由 Jev 驱动的类型化 SEO／AEO／GEO 判断，代码掌管其余。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · epergaboni · `TS`</sub>

- **[leanest](https://github.com/baronunread/leanest)** — 本地优先的测试选择器：用 Jev 判断哪些测试受某次变更影响。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · baronunread · `TS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — 由 Jev 驱动的 LlamaIndex 重排器与路由器 —— 类型化的分数与选择，比 LLM-as-judge 便宜。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · wiktorb2004 · `Py`</sub>

- **[prompt2jev](https://github.com/sumleo/prompt2jev)** — 把自然语言、LLM 提示或跑提示的代码，转换成一个 Jev 决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · sumleo · `Py`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — 基于 Qwen3.5-0.8B 的 Jev 风格校准决策模型（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · shamazharikh · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[system-one-gemma](https://github.com/akash-kamat/system-one-gemma)** — 开源的 Jev 式 System One 决策模型：Gemma 3 270M 加一个打分头。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · akash-kamat · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[typesafe-cli](https://github.com/y0usaf/typesafe-cli)** — 在 shell 里向 Jev 提类型化问题：noul、choice、score 都以数字返回，而不是散文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · y0usaf · `TS`</sub>

- **[dsh-jev](https://github.com/noetion/dsh-jev)** — 注册 jev_ask 的 DSH 包，提供 noul、choice、score 三种答案。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · noetion · `TS`</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — 给 DeepSeek Harness 的 Jev 判定式上下文压缩：语义化的工具结果裁剪。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · yangyu666 · `JS`</sub>

- **[jev-as-quant](https://github.com/jiayylu/jev-as-quant)** — 把类型化 System-1 决策作为量化研究栈的判断层。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · jiayylu · `Py`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — 从不做摘要的 Hermes 会话上下文压缩：每次工具调用都被打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · picaye · `JS`</sub>

- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** — 开源的 jev-flash-router：给 Jev 的 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · ravinder82 · `TS`</sub>

- **[jev-judgment](https://github.com/HyunjunJeon/jev-judgment)** — Agent 技能：把编程智能体的封闭式判断交给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · hyunjunjeon · `Py`</sub>

- **[jev-local](https://github.com/us/jev-local)** — 本地的 Jev 兼容评估服务：POST /v1/systemone，支持类型化的 noul／choice／score。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★3 · us · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[jev-ui](https://github.com/etweisberg/jev-ui)** — React 组件：由决策模型决定渲染哪个组件、列表如何排序、是否展示。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · etweisberg · `TS` · ⚠ `无许可证`</sub>

- **[jevmetrics](https://github.com/ishantanu/jevmetrics)** — 一个实验性的 OpenTelemetry Collector 指标处理器：根据元数据让 Jev 判断每个指标在运维上的价值，再由确定性策略决定保留哪些。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · ishantanu · `Go`</sub>

- **[jevseek](https://github.com/morcoan/JMP)** — 本地编程工作区：由 Jev 路由动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · morcoan · `Py` · ⚠ `已归档`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — 一个 Stop 钩子，阻止编程智能体过早收工 —— 用大白话写规则，由 Jev 裁定。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · noplan-inc · `Py`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · legacybridge-tech · `TS`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server 兼 agent 技能：把一个判断分解成多个类型化问题。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · simota · `TS`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — 在用户看到之前先审判每一条 LLM 响应。提供 AI SDK middleware 与 OpenAI 兼容代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★3 · noelzappy · `TS`</sub>

- **[typesafe-jev-bridge](https://github.com/RevocGG/typesafe-jev-bridge)** — 在任何地方使用 Jev：零依赖的 OpenAI 兼容封装。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · revocgg · `JS`</sub>

- **[vgi-typesafe](https://github.com/Query-farm/vgi-typesafe)** — 一个 VGI worker，把 System One 的 choice／noul／score 以可 LATERAL 连接的表函数形式暴露给 DuckDB／SQL。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · query-farm · `Py`</sub>

- **[ask-jev-ai](https://github.com/waynesutton/ask-jev-ai)** — 一面公开的墙：任何人用三到十五个词提问，由 Jev 作答。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · waynesutton · `JS` · ⚠ `无许可证`</sub>

- **[clarity-judge](https://github.com/TypeSafeAI/clarity-judge)** — 由 TypeSafe AI Jev 模型驱动的多维度写作质量检查器：每项检查独立命名，各自给出结论。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · bunsdev · `TS` · ⚠ `无许可证`</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop 钩子：核对 AI 助手的声明与它这轮实际读过的内容是否相符。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vladyslavhontar · `Py`</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)** — 一个 agent 技能：识别出有界判断步骤，优先尝试用类型化决策模型解决。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · harrymunro · `Py`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · nanami-0713 · `JS`</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — 不确定时保持沉默的 issue 分拣：校准过的标签，含垃圾与重复检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · emreozyoruk · `JS`</sub>

- **[jev-builder-loop](https://github.com/rainbowpuffpuff/jev-builder-loop)** — Grok 技能：把 Jev 当作构建者循环里的判断传感器（先验 × 概率 → 下一步）。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · rainbowpuffpuff · `Py`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — Jev 的 MCP server：提供官方三种问题类型。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · wangkuangkuang · `Py`</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — 编程智能体总在不难的决策上烧上下文 —— 分拣 400 条工单之类的活儿不该这么贵。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · ddfeyes · `Py`</sub>

- **[jev-model-router](https://github.com/lucianfialho/jev-model-router)** — 用 Jev 做成本优化的 OpenRouter 模型路由，带实时全目录。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · lucianfialho · `Py`</sub>

- **[jev-rl](https://github.com/Bring-AI/jev-rl)** — JEV 强化学习：用 JEV 提供的奖励训练四款经典游戏，附可复现实验与检查点。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · bring-ai · `Py`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — 由 Jev 打分驱动的开源仓库与 crate 侦察工具。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-workbench](https://github.com/molis-ai/jev-workbench)** — 在 Jev 之上构建带版本的判断函数，之后反复调用同一个已发布版本。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · molis-ai · `TS`</sub>

- **[jevbus](https://github.com/zkjoie/jevbus)** — 一个流式事件总线：路由、订阅与消费都由概率决策决定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · zkjoie · `Rs`</sub>

- **[JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach)** — 给你向编码智能体提问的方式打分，并显示你的习惯是否在进步的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · crowdlinker · `TS`</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — 亚 100 毫秒的智能体工具调用安全闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · lgy1027 · `Py`</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — Jev 的 n8n 社区节点：带校准概率的文本分类、打分与检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · khmuhtadin · `TS`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — 给 pytest 的语义断言：测试 LLM 应用输出的含义，由 Jev 判定。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · allebee · `Py`</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — 面向 AI 智能体的开源自动模式：一个校准过的工具调用防火墙。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · riskaversetech · `TS`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — 给 Codex 与 Claude Code 的非官方社区 MCP 插件，用 Jev 做有界路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · e-fl · `JS`</sub>

- **[watfile](https://github.com/jexp/watfile)** — 用 Jev 或本地校准决策模型给文本与 PDF 分类归档。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · jexp · `Py` · ⚠ `无许可证`</sub>

- **[draftpulse](https://github.com/pekth/draftpulse)** — 实验性的 X 草稿传播度实时评分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · pekth · `TS` · ⚠ `无许可证`</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — 给 DeepSeek Harness 的 Jev 决策工具与实时验证基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · xienda · `JS`</sub>

- **[gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev)** — 在同一输入上对比 GPT 的生成式语言与 JEV 的结构化 Noul 决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · tanaypadar · `TS`</sub>

- **[instruct-jev](https://github.com/ctaxnagomi/instruct-jev)** — INSTRUCT_JEV：Jev／System One 指令语料库（choice／noul／score）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ctaxnagomi · `Py`</sub>

- **[jev-carryforward](https://github.com/Dharundp6/jev-carryforward)** — 把上一轮会话知道的东西，对照这一轮正在做的事打分。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · dharundp6 · `TS`</sub>

- **[jev-hooks](https://github.com/microchipgnu/jev-hooks)** — 把类型化 Jev 判断组合成 React 与后端程序里的响应式语义状态。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · microchipgnu · `TS` · ⚠ `无许可证`</sub>

- **[jev-paper-judge](https://github.com/JacobLinCool/jev-paper-judge)** — 几秒内给出论文反馈。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jacoblincool · `TS`</sub>

- **[jev-score](https://github.com/a-Fig/jev-score)** — 由 Jev 驱动的本地优先文档评估工作区。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · a-fig · `JS`</sub>

- **[jev-wrapped](https://github.com/gaborishka/jev-wrapped)** — Telegram 频道年度透视：Jev 评判一年的帖子，生成一张卡片，跑在一个 Cloudflare Worker 上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · gaborishka · `JS`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — 先评估再信任：实战笔记、可运行脚本与一个 agent 技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · elshinq · `JS`</sub>

- **[judging-with-typesafe](https://github.com/carlsonchik/judging-with-typesafe)** — 给 Letta 智能体的技能：通过 System One 按给定标准做判断（俄语）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · carlsonchik · `Py` · ⚠ `无许可证`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — 来自某土地开发 SaaS 的类型化决策基准：schema、匿名标注数据与运行器。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · zsavage8 · `Py`</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — 给 Pi 编程智能体的 Jev 权限闸门：审判每一次 bash 与写入。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · kurihada · `TS`</sub>

- **[s1-rs](https://github.com/AbdelStark/s1-rs)** — Rust 的类型化 System One 层（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · abdelstark · `Rs`</sub>

- **[typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase)** — 展示 Jev 的 Next.js 界面：并行 Noul 判断与实时结果。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ashadeepa · `TS` · ⚠ `无许可证`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[decide-mcp](https://github.com/dakdevs/decide-mcp)** — 可配置的决策 MCP server，带百分比分数与偏好画像。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · dakdevs · `TS`</sub>

- **[deslop](https://github.com/yoichiojima-2/deslop)** — 给网页的广告、垃圾内容、SEO 和二手内容打分。一个基于 TypeSafe Jev 的智能体技能：每页四个概率。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yoichiojima-2 · `Py`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kalyanm45 · `Py`</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — 评判智能体的每一步：通过／重试／升级／停止。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** — 二十个问题猜谜：一直问下去，直到 Jev 的校准置信度越过阈值。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · mintannn · `TS`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-decision-lab](https://github.com/jlov7/jev-decision-lab)** — 一个本地实验室，观察 Jev 在真实业务场景上的判断表现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jlov7 · `Py`</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — 给 Claude Code 的六道校准闸门：规则、范围、意图、完成度等。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · rashedint32 · `JS`</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — 以基准驱动的 Jev 路由器与评判者，服务于成本可控的 LLM 编程流程。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · erendikmenn · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — 证据门控的 Jev 问题包注册表：精选问题、黄金样例与实测证据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · dtduc-git · `Py`</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — 给某 lint 工具做的二次评估：用 Jev 评判 linter 的判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · blas0 · `JS`</sub>

- **[jev-songwriter](https://github.com/beingcognitive/jev-songwriter)** — 一个一个音符都写不出的决策模型却写出了歌：代码负责计算，Jev 负责评判。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · beingcognitive · `JS`</sub>

- **[Jev-test](https://github.com/WeSecureYou/Jev-test)** — 一个 CLI 与 REST API：让 Jev 评估某个职业受 AI 裁员冲击的程度、未来走向、对人类问责的需要以及整体韧性。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · wesecureyou · `TS` · ⚠ `无许可证`</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — 把 Jev 的 noul 原语应用到一个共谋语料库上。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · sypherin · `Py`</sub>

- **[jevplay](https://github.com/ndolinschi/jevplay)** — Jev playground：自定义 Choice／Score／Noul 构造器，带实时概率分布。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** — 面向 System One API 的 n8n 社区节点：类型化的是非、选择与打分问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · dommonte · `TS`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — 给 OMP 的模型裁决式权限闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · strml · `TS` · ⚠ `已归档`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One 搜索：用类型化判断与仓库证据导航与追踪代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · cpaczek · `TS`</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town：客厅电视上的社交推理派对游戏，由 Jev 主持。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · tpaulshippy · `Rb` · ⚠ `无许可证`</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — 开源 Chrome 扩展：用 Jev 过滤 AI 生成的文字与广告。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · neddes · `JS`</sub>

- **[spendbrake](https://github.com/ndolinschi/spendbrake)** — 智能体预算刹车：继续／降级模型／停止。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[transcript-scorecard](https://github.com/brandonbryant12/transcript-scorecard)** — 实时客服通话评分演示。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · brandonbryant12 · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-demo-mcp](https://github.com/bestagentkits/typesafe-demo-mcp)** — 把 System One 判断暴露成智能体工具的 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · bestagentkits · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-oracles](https://github.com/trophee-bot/typesafe-oracles)** — 评估 System One 三原语：类型化的裁决在哪些场景胜过生成式模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · trophee-bot · `JS` · ⚠ `无许可证`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — 基于 Jev 的三条可组合判断流水线：工单分拣、可观测性等。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shivam2003-dev · `Py`</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — 用 Typesafe.AI 生成 diff 审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · rbalch · `Py` · ⚠ `无许可证`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — 给编程智能体的类型化判断层：从需求文档到发布的各道闸门。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★0 · zahrannnn · `TS` · ⚠ `无许可证`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
