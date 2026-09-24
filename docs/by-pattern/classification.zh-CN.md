# 分类

<sub>[awesome-jev](../../README.zh-CN.md) · [English](classification.md)</sub>

_把条目归入分类体系，包括用概率遍历的深层层级。_

这个决策的全部已收录例子 —— 共 119 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#分类)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — 用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★87,298 · `TS` · `choice` · ⚠ `仅影子运行`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★18,204 · Vercel Labs · `TS` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★12,328 · `TS` · `choice` · `noul`</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — 基于 Jev 决策的税务文档分页分类器，在 261 种 IRS 表单上达到严格全对，每页约 $0.001。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★419 · kyotofin · `TS`</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)** — 基于纯 HTTP 的零样本文本分类 —— 不需要密钥、不需要账号，一个 Cloudflare Worker。 <sub>(机翻)</sub>
  <sub>`插件` · ★417 · mrmps · `TS`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — 非常快的文档分类与切分器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★414 · jerryjliu · `Py`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★324 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — 一个浏览器扩展，用可复用的模板规则清除页面杂物。
  <sub>`开源项目` · ★224 · kitze · `TS`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。
  <sub>`基准测试` · ★190 · `Py` · ⚠ `无许可证` `宣称未核实`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★173 · `JS` · `choice` · `score` · `noul`</sub>

- **[Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis)** — 按需使用的加密市场情报终端：选定币种和推文样本数量，Jev 结合行情、资金费率与社交情绪给出买入、卖出、持有或止盈的决策卡片，不会自动下单。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★166 · brainstormity · `Py`</sub>

- **[332_lab-jev-chat](https://github.com/Liyucheng1997/332_lab-jev-chat)** — 电脑版微信助手：由 Jev 判断每条消息的意图，DeepSeek 给出建议回复。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★122 · liyucheng1997 · `Kt`</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — 本地优先的 AI 任务中枢：把邮件、Teams、Slack 与报表汇成一条时间线。 <sub>(机翻)</sub>
  <sub>`插件` · ★120 · ldbumble · `Py`</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)** — Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、原速回放与离线报告。
  <sub>`基准测试` · ★97 · nanmicoder · `JS`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★97 · `TS` · `choice` · `score`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 结合实时音频与字幕检测 YouTube 视频里的赞助片段。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★95 · trungdq88 · `JS` · ⚠ `无许可证`</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — 用于 Jev 分类决策的 PostgreSQL 扩展（预 alpha）。 <sub>(机翻)</sub>
  <sub>`插件` · ★82 · giuliosmall · `C`</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — 一个 Chrome 扩展，逐个询问 DOM 元素是不是广告。
  <sub>`开源项目` · ★74 · realzachi · `JS`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★69 · `TS` · `choice` · ⚠ `无许可证`</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把类型化答案变成传感器，并提供可用于自动化的动作。
  <sub>`平台集成` · ★58 · abovecolin · `Py`</sub>

- **[JevIntent](https://github.com/Nisaka520/JevIntent)** — 微信（FkWeChat 插件）：长按消息分析意图 / 情绪 / 回复姿态，只在本机弹提示，对方无感知
  <sub>`开源项目` · ★53 · nisaka520 · `Java`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★53 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★46 · kbhuw · `JS` · ⚠ `无许可证`</sub>

- **[jev-poly-crypto-demo](https://github.com/frankda/jev-poly-crypto-demo)** — 面向 Polymarket 五分钟 BTC 涨跌市场的研究工具：实时行情变成 Jev 的类别分数，由独立逻辑做决定，并在看板上展示。仅做模拟交易，从不连接钱包。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★37 · frankda · `TS` · ⚠ `无许可证`</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — 用 Jev 对 Git 提交的 diff 与信息做分类：缺陷修复、安全修复、变更类型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★36 · devanshbatham · `Rs` · ⚠ `无许可证`</sub>

- **[jev-guard](https://github.com/klauswg/jev-guard)** — 面向交易所充值与提现的实时风险分诊网关——Jev（TypeSafe System One）只负责分诊，裁决另有机制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★35 · klauswg · `Java`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · smkrv · `TS`</sub>

- **[sharp](https://github.com/tshmieldev/sharp)** — 用 Jev 或任意 LLM 过滤你的 X.com 信息流。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★30 · tshmieldev · `TS`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★24 · kyu1204 · `TS` · `noul` · `choice` · `score` · ⚠ `宣称未核实`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★23 · goodrahstar · `JS`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★22 · blakestone-x · `Py`</sub>

- **[jev-gmail-ai-spam-filter-and-labeling](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling)** — 自托管的 Gmail AI 邮件分类器，由 Jev 驱动：创建自定义标签、整理收件箱、过滤垃圾邮件。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · ilyamk · `JS`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome 扩展：给你在 X 上滑过的每条帖子打上类型化 Jev 判断与实时评分。 <sub>(机翻)</sub>
  <sub>`插件` · ★17 · oso95 · `TS`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★16 · parth-kp · `Py`</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(机翻)</sub>
  <sub>`插件` · ★15 · francoischastel · `TS`</sub>

- **[lkclean](https://github.com/stefw/lkclean)** — 清理 LinkedIn 信息流的 Chrome 扩展：用 TypeSafe 的 Jev 隐藏流量诱饵、自我推销和跑题的帖子。 <sub>(机翻)</sub>
  <sub>`插件` · ★15 · stefw · `TS`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · evoke-build · `Rs`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · ktaletsk · `Py`</sub>

- **[wechat-jev-assistant](https://github.com/yushen100/wechat-jev-assistant)** — Windows 微信对话分析助手：本地读取、脱敏、TypeSafe Jev 判断与加密历史
  <sub>`开源项目` · ★13 · yushen100 · `Py` · ⚠ `无许可证`</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — 对一大堆文本（工单、评论、日志）批量回答同一个问题：把多个条目打包进每次请求，并称吞吐量是逐条请求的 32 倍、成本低 41%。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · collapseindex · `Py` · ⚠ `宣称未核实`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · reachjalil · `JS`</sub>

- **[sift](https://github.com/bohutang/sift)** — Chrome 扩展：给 X 上的每条帖子打标（干货／幽默／闲聊／推广／垃圾／AI 生成）。 <sub>(机翻)</sub>
  <sub>`插件` · ★11 · bohutang · `JS`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · forvela · `JS`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★9 · 24601 · `Py`</sub>

- **[JevBystander](https://github.com/Nisaka520/JevBystander)** — 安卓无障碍版微信判读：只读屏、只弹 3 条 Toast（意图 / 情绪 / 着急 / 建议），不生成回复文案、不发送 · 零第三方依赖，APK 861 KB
  <sub>`开源项目` · ★9 · nisaka520 · `Kt`</sub>

- **[twitter-jev-guard](https://github.com/qs-lll/twitter-jev-guard)** — 使用 TypeSafe Jev 在 X/Twitter 时间线上识别低质量、垃圾和广告帖子，并在文字区域显示醒目的半透明水印。
  <sub>`插件` · ★9 · qs-lll · `JS` · ⚠ `无许可证`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · reachjalil · `TS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — 面向智能体的 Haskell DSL：类型化数据包、类型推断，答案与问题同构。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · inanna-malick · `Hs`</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — 本地离线的 System One 服务，兼容 Jev API，回答类型化的是非问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · amithgc · `Py`</sub>

- **[one-system](https://github.com/rawwerks/one-system)** — 通过统一接口使用本地与托管的分类器（即决策模型）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★7 · rawwerks · `TS` · ⚠ `并非 Jev 本身`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · carlosedm10 · `Py` · ⚠ `无许可证`</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — 对文本文档做快速且低成本的分类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · charlyhno-eng · `TS`</sub>

- **[jev-mail](https://github.com/muhammedilyasy/jev-mail)** — 用 TypeSafe Jev 模型为 Gmail 做分诊的 Chrome 扩展：为每封邮件给出类别、优先级、垃圾邮件概率和需回复概率。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · muhammedilyasy · `JS`</sub>

- **[jev-pr-labeler](https://github.com/1jehuang/jev-pr-labeler)** — 用 Jev 的类型化决策给 GitHub PR 打语义标签，依据概念范围而不是改动行数。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · 1jehuang · `Py`</sub>

- **[jev-skip](https://github.com/valentynkit/jev-skip)** — 读字幕、在观看时判断，从而跳过视频里的赞助段落。
  <sub>`开源项目` · ★4 · valentynkit · `TS`</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — 用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · jkrup · `JS`</sub>

- **[jlink](https://github.com/keltokhy/jlink)** — 给经济学家用的记录链接：用自然语言写匹配规则，对每一对记录得到一个概率，可审计、可引用。支持 Python、CLI、Stata 和 R。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · keltokhy · `Py`</sub>

- **[mysql-ailike](https://github.com/maayanlevy/mysql-ailike)** — MySQL 的自然语言行过滤，由 TypeSafe Jev 驱动。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · maayanlevy · `C++`</sub>

- **[tab-bouncer](https://github.com/MANISH007700/tab-bouncer)** — 一个关闭多余标签页的 Chrome 扩展，由 TypeSafe Jev 一次调用完成判断。告诉它你在做什么即可。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · manish007700 · `JS`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · abhishekswe · `TS`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · prasanthj · `C++`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · foadsf · `Py`</sub>

- **[jev-ids](https://github.com/jev-ids/jev-ids)** — 基于 Jev 的高速、省 token 的入侵检测系统。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · jev-ids · `Py`</sub>

- **[notiq](https://github.com/chengyongru/notiq)** — 原生 Android 通知过滤，用自然语言写规则，由 Jev 或自托管的 FastJev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · chengyongru · `Kt` · ⚠ `无许可证`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · nanami-0713 · `JS`</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — 不确定时保持沉默的 issue 分拣：校准过的标签，含垃圾与重复检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · emreozyoruk · `JS`</sub>

- **[jev-chess](https://github.com/hemanth/jev-chess)** — 用 Jev 做国际象棋的着法、局面评估、人格对手与棋局分类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · hemanth · `TS` · ⚠ `无许可证`</sub>

- **[jev-linkedin-slop-filter](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter)** — 给 LinkedIn 上的流量诱饵贴上 BAIT、CORP 或 BRAG 的标签，由 Jev（TypeSafe System One）实时判定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · arpit-khandelwal · `JS`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — Jev 的 MCP server：提供官方三种问题类型。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · wangkuangkuang · `Py`</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — 编程智能体总在不难的决策上烧上下文 —— 分拣 400 条工单之类的活儿不该这么贵。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · ddfeyes · `Py`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 给 Spring WebFlux 的非阻塞 Starter，实现一个语义熔断器来检测静默故障。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vicente-md · `Java` · ⚠ `无许可证`</sub>

- **[jev-slop-guard](https://github.com/davertor/jev-slop-guard)** — Jev Slop Guard：一个 Chrome 扩展，在你浏览 X 和 LinkedIn 时为 AI 生成的垃圾内容打分并盖章。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · davertor · `JS`</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — Jev 的 n8n 社区节点：带校准概率的文本分类、打分与检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · khmuhtadin · `TS`</sub>

- **[watfile](https://github.com/jexp/watfile)** — 用 Jev 或本地校准决策模型给文本与 PDF 分类归档。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · jexp · `Py` · ⚠ `无许可证`</sub>

- **[zerosweep](https://github.com/sysadarsh/zerosweep)** — 自主的 System-One 分拣引擎与基准，75 毫秒推理。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · sysadarsh · `TS` · ⚠ `无许可证`</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — 用 Jev 按主题、情绪与歌词复杂度给一位艺人的全部作品分类，并可视化呈现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · lirantal · `JS`</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — 为 DeepSeek Harness 中的每一次工具调用提供毫秒级 System-1 判断——由 Jev 驱动的风险分类与证据检查。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · asktheway · `TS`</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — 一个文本审核演示：一次 systemOne 调用并行检查七个 Noul 风险项和一个严重程度 Score，最终结论由代码按策略阈值计算。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · norbertbodziony · `TS` · ⚠ `无许可证`</sub>

- **[himalaya-jev-mail-classify](https://github.com/initrd/himalaya-jev-mail-classify)** — 用语言模型给 Gmail 打标签、排优先级：通过 himalaya 读取邮件，用 Jev（TypeSafe）为每个会话分类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · initrd · `Py`</sub>

- **[hunch](https://github.com/steven-shoemaker/hunch)** — 对数据列向 Jev 提问：封闭集合的问题，带缓存，并把结果连接回原表。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · steven-shoemaker · `Py`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `仅一次提交` `疑似 AI 生成`</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — TypeSafe AI Jev 在智能体工具调用风险分类上的可复现基准：准确率、延迟，以及其置信度是否可信。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · themsquared · `Py`</sub>

- **[jev-clean](https://github.com/Kunyanli230/jev-clean)** — 以决策为先的数据清洗系统，由 Jev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · kunyanli230 · `Py`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — 在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · 4esv · `Py` · ⚠ `无许可证`</sub>

- **[jev-issue-radar](https://github.com/Patrick-SCH03/jev-issue-radar)** — 带并排证据的 GitHub issue 分拣，可免配置试用公开样例。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · patrick-sch03 · `JS`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jyatesdotdev · `Py`</sub>

- **[jev-organize](https://github.com/nexibeo/jev-organize)** — 把一堆公司文件扔进去，就能按部门、类型、敏感度、日期、交易方等分类整理好。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · nexibeo · `JS`</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev 增强的 Playwright MCP 代理：页面状态分拣与提示注入防护。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · krw82 · `TS`</sub>

- **[jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline)** — 针对长期问题的每日研究监控：确定性的 Python 掌控流程，TypeSafe Jev 按问题筛选信息源，Qwen 撰写笔记（试点）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · shimo4228 · `Py`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — 可配置的 GitHub 提交审查与 PR 分类，不使用任何文本生成模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · fatwang2 · `JS`</sub>

- **[jev-screen-mcp](https://github.com/jiawei686/jev-screen-mcp)** — 单一用途的 MCP 服务器（一个工具，一件事）：由 TypeSafe Jev 驱动的内容审核关卡。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · jiawei686 · `TS`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · teyhouse · `Py` · ⚠ `无许可证`</sub>

- **[jev-triage](https://github.com/cephalization/jev-triage)** — 拉取并同步大型仓库以做 issue 分拣。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · cephalization · `TS`</sub>

- **[Jevatar](https://github.com/AppChainAI/Jevatar)** — 一个只用面部表情回复的 AI 伙伴：Jev（TypeSafe System One）判断你的消息，并挑选一个表情。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · appchainai · `TS`</sub>

- **[jevticktrouter](https://github.com/GhrezaKh74/JevTicktRouter)** — 用 .NET 10 与 React 19 做的快速结构化工单分拣。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ghrezakh74 · `C#` · ⚠ `无许可证`</sub>

- **[jevtriage](https://github.com/sathariels/jevtriage)** — GitHub Action 与 CLI：用 TypeSafe Jev 为 PR 分诊（可以合并 / 需要审查 / 有风险），并带置信度关卡。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · sathariels · `Py`</sub>

- **[metis](https://github.com/Ayush0054/metis)** — Metis：由 Jev 驱动的 GitHub issue 自动分拣，可复用的 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ayush0054 · `Py`</sub>

- **[triagedy](https://github.com/m0rphtail/triagedy)** — 把告警分拣做成 UNIX 过滤器：JSONL 安全告警进，类型化决策出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · m0rphtail · `Rs`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kalyanm45 · `Py`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-eval](https://github.com/onlyoneaman/jev-eval)** — 在四个公开分类数据集上比较 TypeSafe 的 Jev 与两款 GPT 模型：案例、逐条答案、评分全部公开。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · onlyoneaman · `TS`</sub>

- **[jev-labeler-action](https://github.com/yamadashy/jev-labeler-action)** — 零配置的 AI 议题打标签工具，基于 TypeSafe 的 Jev。不生成文本，非官方。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · yamadashy · `TS`</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — 把 Jev 的 noul 原语应用到一个共谋语料库上。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · sypherin · `Py`</sub>

- **[JevEye](https://github.com/Adityakhalkar/JevEye)** — 向 Jev 询问一张图片：CNN 报告它看到了什么（带校准置信度或选择弃权），再由 Jev 判断这意味着什么。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · adityakhalkar · `TS`</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — 面向社区和应用的内容审核，由 Jev（TypeSafe）驱动：按类别给出概率，阈值由你掌控。支持 Discord。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · ohernandezdev · `Py`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — 给 OMP 的模型裁决式权限闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · strml · `TS` · ⚠ `已归档`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — 检测 AI 智能体循环中的语义停滞。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ashutoshvjti · `TS`</sub>

- **[pulselane](https://github.com/ndolinschi/pulselane)** — PulseLane：诊所分诊决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — 用通用分类器做扩散风格像素画：256 个并行像素问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · wizhill05 · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — 基于 Jev 的三条可组合判断流水线：工单分拣、可观测性等。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shivam2003-dev · `Py`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。
  <sub>`基准测试` · Lindfors</sub>

- **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)** — 一位 ML 工程师从分类任务角度做的讲解 —— 这个切入角度最贴近模型的实际能力。
  <sub>`视频` · Sam Witteveen</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
