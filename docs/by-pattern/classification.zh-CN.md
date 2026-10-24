# 分类

<sub>[awesome-jev](../../README.zh-CN.md) · [English](classification.md)</sub>

_把条目归入分类体系，包括用概率遍历的深层层级。_

这个决策的全部已收录例子 —— 共 126 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#分类)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#classification)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#classification)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 4 · 调用点 116 · 接口形态 1 · 仅示例 0 · 独立报告 11 · 负面结果 1 · 未引用文件 9。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) <sub>`官方文档` · `Py` · `choice`</sub>
- [Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) <sub>`官方文档` · `Py` · `choice`</sub>
- [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) <sub>`官方文档` · `Py` · `score`</sub>
- [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) <sub>`官方文档` · `Py`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — 用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · 调用点 [`apps/web/utils/decision-model/typesafe.ts`](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/typesafe.ts)，2026-09-22 阅读</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★10k+ · Vercel Labs · `TS` · `choice` · 调用点 [`apps/web/lib/jev/compose.ts`](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts)，2026-09-22 阅读</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★10k+ · `TS` · `choice` · 调用点 [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现） · ⚠ `仅影子运行`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · 调用点 [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql)，2026-09-22 阅读</sub>

- **[332_lab-jev-chat](https://github.com/Liyucheng1997/332_lab-jev-chat)** — 电脑版微信助手：由 Jev 判断每条消息的意图，DeepSeek 给出建议回复。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · liyucheng1997 · `Kt` · 调用点 [`windows/jev_windows/jev_api.py`](https://github.com/Liyucheng1997/332_lab-jev-chat/blob/HEAD/windows/jev_windows/jev_api.py)，2026-09-24 阅读</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · 调用点 [`src/search.ts`](https://github.com/ellipsis-dev/blink/blob/HEAD/src/search.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)** — 基于纯 HTTP 的零样本文本分类 —— 不需要密钥、不需要账号，一个 Cloudflare Worker。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · mrmps · `TS` · 调用点 [`src/jev.ts`](https://github.com/mrmps/classifier-dev/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — 非常快的文档分类与切分器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · jerryjliu · `Py` · 调用点 [`src/jev_docs/engines/jev.py`](https://github.com/jerryjliu/docjev/blob/HEAD/src/jev_docs/engines/jev.py)，2026-09-22 阅读</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)** — Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、原速回放与离线报告。
  <sub>`基准测试` · ★100+ · nanmicoder · `JS` · 调用点 [`src/backends/jev.mjs`](https://github.com/NanmiCoder/jev-arena/blob/HEAD/src/backends/jev.mjs)，2026-09-24 阅读</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts)，2026-09-22 阅读</sub>

- **[Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis)** — 按需使用的加密市场情报终端：选定币种和推文样本数量，Jev 结合行情、资金费率与社交情绪给出买入、卖出、持有或止盈的决策卡片，不会自动下单。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · brainstormity · `Py` · 调用点 [`app/services/typesafe_service.py`](https://github.com/brainstormity/Jev-X-Sentiment-Analysis/blob/HEAD/app/services/typesafe_service.py)，2026-09-24 阅读</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js)，2026-09-22 阅读</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `score` · 调用点 [`engine/jev-service.ts`](https://github.com/irfndi/prism-liquidity-agent/blob/HEAD/engine/jev-service.ts)，2026-09-22 阅读</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — 本地优先的 AI 任务中枢：把邮件、Teams、Slack 与报表汇成一条时间线。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · ldbumble · `Py` · 调用点 [`taskuary/jev.py`](https://github.com/ldbumble/taskuary/blob/HEAD/taskuary/jev.py)，2026-09-22 阅读</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — 基于 Jev 决策的税务文档分页分类器，在 261 种 IRS 表单上达到严格全对，每页约 $0.001。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · kyotofin · `TS` · 调用点 [`src/backend.ts`](https://github.com/kyotofin/tax-doc-classifier/blob/HEAD/src/backend.ts)，2026-09-22 阅读</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — 一个浏览器扩展，用可复用的模板规则清除页面杂物。
  <sub>`开源项目` · ★100+ · kitze · `TS` · 调用点 [`lib/jev.ts`](https://github.com/kitze/unclutter/blob/HEAD/lib/jev.ts)，2026-09-22 阅读</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 结合实时音频与字幕检测 YouTube 视频里的赞助片段。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · trungdq88 · `JS` · 调用点 [`extension/lib/jev.js`](https://github.com/trungdq88/youtube-sponsor-detection/blob/HEAD/extension/lib/jev.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · 24601 · `Py` · 调用点 [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md)，2026-09-24 阅读</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — 用 Jev 对 Git 提交的 diff 与信息做分类：缺陷修复、安全修复、变更类型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · devanshbatham · `Rs` · 调用点 [`src/jev.rs`](https://github.com/devanshbatham/commit-miner/blob/HEAD/src/jev.rs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — 为 DeepSeek Harness 中的每一次工具调用提供毫秒级 System-1 判断——由 Jev 驱动的风险分类与证据检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · asktheway · `TS` · 调用点 [`scripts/smoke.mjs`](https://github.com/AskTheWay/dsh-jev-interceptor/blob/HEAD/scripts/smoke.mjs)，2026-09-24 阅读</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · prasanthj · `C++` · 调用点 [`benchmarks/live.py`](https://github.com/prasanthj/duckdb-jev/blob/HEAD/benchmarks/live.py)，2026-09-22 阅读</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · evoke-build · `Rs` · 调用点 [`crates/evoke-adapters/src/systemone.rs`](https://github.com/evoke-build/evoke/blob/HEAD/crates/evoke-adapters/src/systemone.rs)，2026-09-24 阅读</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把关于家的类型化答案变成传感器，提供可用于自动化的 noul、choice 和 score 动作，以及一个对话代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · 调用点 [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py)，2026-09-30 阅读 · ⚠ `疑似 AI 生成` `作者自荐`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · forvela · `JS` · 调用点 [`src/decision.js`](https://github.com/forvela/jev-agent-browser/blob/HEAD/src/decision.js)，2026-09-22 阅读</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · smkrv · `TS` · 调用点 [`src/client.ts`](https://github.com/smkrv/jev-calibrate/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · francoischastel · `TS` · 调用点 [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts)，2026-09-22 阅读</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · goodrahstar · `JS` · 调用点 [`lib/racers.mjs`](https://github.com/goodrahstar/jev-column-race/blob/HEAD/lib/racers.mjs)，2026-09-22 阅读</sub>

- **[jev-gmail-ai-spam-filter-and-labeling](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling)** — 自托管的 Gmail AI 邮件分类器，由 Jev 驱动：创建自定义标签、整理收件箱、过滤垃圾邮件。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ilyamk · `JS` · 调用点 [`CODE.gs`](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling/blob/HEAD/CODE.gs)，2026-09-24 阅读</sub>

- **[jev-guard](https://github.com/klauswg/jev-guard)** — 面向交易所充值与提现的实时风险分诊网关——Jev（TypeSafe System One）只负责分诊，裁决另有机制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · klauswg · `Java` · 调用点 [`src/main/java/com/jevguard/eval/EvalRunner.java`](https://github.com/klauswg/jev-guard/blob/HEAD/src/main/java/com/jevguard/eval/EvalRunner.java)，2026-09-24 阅读</sub>

- **[jev-ids](https://github.com/jev-sec/jev-ids)** — 基于 Jev 的高速、省 token 的入侵检测系统。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jev-ids · `Py` · 调用点 [`jev_ids/detectors/jev.py`](https://github.com/jev-sec/jev-ids/blob/HEAD/jev_ids/detectors/jev.py)，2026-09-24 阅读</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · parth-kp · `Py` · 调用点 [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py)，2026-09-22 阅读</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★10+ · blakestone-x · `Py` · 调用点 [`jev_mcp/client.py`](https://github.com/blakestone-x/jev-mcp/blob/HEAD/jev_mcp/client.py)，2026-09-22 阅读</sub>

- **[jev-poly-crypto-demo](https://github.com/frankda/jev-poly-crypto-demo)** — 面向 Polymarket 五分钟 BTC 涨跌市场的研究工具：实时行情变成 Jev 的类别分数，由独立逻辑做决定，并在看板上展示。仅做模拟交易，从不连接钱包。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · frankda · `TS` · 调用点 [`scripts/check-jev.ts`](https://github.com/frankda/jev-poly-crypto-demo/blob/HEAD/scripts/check-jev.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · kbhuw · `JS` · 调用点 [`dist/server.mjs`](https://github.com/kbhuw/jev-sift/blob/HEAD/dist/server.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · reachjalil · `TS` · 调用点 [`benchmarks/run.mjs`](https://github.com/reachjalil/jev-tree/blob/HEAD/benchmarks/run.mjs)，2026-09-22 阅读</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — 对一大堆文本（工单、评论、日志）批量回答同一个问题：把多个条目打包进每次请求，并称吞吐量是逐条请求的 32 倍、成本低 41%。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · collapseindex · `Py` · 调用点 [`src/jev_ultralightspeed/_settings.py`](https://github.com/collapseindex/jev-ultralightspeed/blob/HEAD/src/jev_ultralightspeed/_settings.py)，2026-09-24 阅读 · ⚠ `宣称未核实`</sub>

- **[JevBystander](https://github.com/Nisaka520/JevBystander)** — 安卓无障碍版微信判读：只读屏、只弹 3 条 Toast（意图 / 情绪 / 着急 / 建议），不生成回复文案、不发送 · 零第三方依赖，APK 861 KB
  <sub>`开源项目` · ★10+ · nisaka520 · `Kt` · 调用点 [`app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt`](https://github.com/Nisaka520/JevBystander/blob/HEAD/app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt)，2026-09-24 阅读</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ktaletsk · `Py` · 调用点 [`src/jevframe/_engine.py`](https://github.com/ktaletsk/jevframe/blob/HEAD/src/jevframe/_engine.py)，2026-09-22 阅读</sub>

- **[JevIntent](https://github.com/Nisaka520/JevIntent)** — 微信（FkWeChat 插件）：长按消息分析意图 / 情绪 / 回复姿态，只在本机弹提示，对方无感知
  <sub>`开源项目` · ★10+ · nisaka520 · `Java` · 调用点 [`main.java`](https://github.com/Nisaka520/JevIntent/blob/HEAD/main.java)，2026-09-24 阅读</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · reachjalil · `JS` · 调用点 [`benchmarks/pager/run-jev-v2.mjs`](https://github.com/reachjalil/jevlogs/blob/HEAD/benchmarks/pager/run-jev-v2.mjs)，2026-09-22 阅读</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · 调用点 [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts)，2026-09-23 阅读 · ⚠ `宣称未核实` `作者自荐`</sub>

- **[lkclean](https://github.com/stefw/lkclean)** — 清理 LinkedIn 信息流的 Chrome 扩展：用 TypeSafe 的 Jev 隐藏流量诱饵、自我推销和跑题的帖子。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · stefw · `TS` · 调用点 [`src/jev.ts`](https://github.com/stefw/lkclean/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — 本地离线的 System One 服务，兼容 Jev API，回答类型化的是非问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · amithgc · `Py` · 调用点 [`src/local_jev/ui/app.js`](https://github.com/amithgc/local-jev/blob/HEAD/src/local_jev/ui/app.js)，2026-09-22 阅读</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — 用于 Jev 分类决策的 PostgreSQL 扩展（预 alpha）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · giuliosmall · `C` · 调用点 [`sql/typesafe.sql`](https://github.com/giuliosmall/pg_typesafe/blob/HEAD/sql/typesafe.sql)，2026-09-22 阅读</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★10+ · `Py` · `sh` · `choice` · `score` · `noul` · 调用点 [`src/reflex_guard/providers/typesafe.py`](https://github.com/sharziki/semdecide/blob/HEAD/src/reflex_guard/providers/typesafe.py)，2026-09-22 阅读</sub>

- **[sharp](https://github.com/tshmieldev/sharp)** — 用 Jev 或任意 LLM 过滤你的 X.com 信息流。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tshmieldev · `TS` · 调用点 [`src/common/settings.ts`](https://github.com/tshmieldev/sharp/blob/HEAD/src/common/settings.ts)，2026-09-24 阅读</sub>

- **[sift](https://github.com/bohutang/sift)** — Chrome 扩展：给 X 上的每条帖子打标（干货／幽默／闲聊／推广／垃圾／AI 生成）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · bohutang · `JS` · 调用点 [`background.js`](https://github.com/bohutang/sift/blob/HEAD/background.js)，2026-09-22 阅读</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — 一个 Chrome 扩展，逐个询问 DOM 元素是不是广告。
  <sub>`开源项目` · ★10+ · realzachi · `JS` · 调用点 [`src/typesafe.js`](https://github.com/realZachi/typesafe-adblock/blob/HEAD/src/typesafe.js)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[wechat-jev-assistant](https://github.com/yushen100/wechat-jev-assistant)** — Windows 微信对话分析助手：本地读取、脱敏、TypeSafe Jev 判断与加密历史
  <sub>`开源项目` · ★10+ · yushen100 · `Py` · 调用点 [`src/wechat_jev/typesafe_client.py`](https://github.com/yushen100/wechat-jev-assistant/blob/HEAD/src/wechat_jev/typesafe_client.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome 扩展：给你在 X 上滑过的每条帖子打上类型化 Jev 判断与实时评分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · oso95 · `TS` · 调用点 [`src/shared/jev.ts`](https://github.com/oso95/x-scanner/blob/HEAD/src/shared/jev.ts)，2026-09-22 阅读</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · abhishekswe · `TS` · 调用点 [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts)，2026-09-22 阅读</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · carlosedm10 · `Py` · 调用点 [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — 用 Jev 按主题、情绪与歌词复杂度给一位艺人的全部作品分类，并可视化呈现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lirantal · `JS` · 调用点 [`src/jev.ts`](https://github.com/lirantal/discoprint/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nanami-0713 · `JS` · 调用点 [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[DuoMind](https://github.com/j1s4nn/duomind)** — 一个 OpenAI 兼容的本地服务器，把 llama.cpp 上的小模型与 Jev 搭配：在生成之前、之中和之后共 18 个决策点（是否需要推理、是否安全、输出格式、是否该停、是否重试）引导本地模型。提示词会发送给 TypeSafe，生成过程留在本地。 <sub>(机翻)</sub>
  <sub>`开源项目` · j1s4nn · `Py` · `noul` · `choice` · 调用点 [`src/duomind/jev_client.py`](https://github.com/j1s4nn/duomind/blob/HEAD/src/duomind/jev_client.py) · ⚠ `厂商自报数据`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · kalyanm45 · `Py` · 调用点 [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[grev](https://github.com/aurorainfra/grev)** — 用提问代替模式匹配的 Unix 过滤工具：`grev 'is a vegan meal' menu.txt` 只保留 Jev 回答“是”的行；配套工具还会用到 choice 的置信度或路径分数。默认固定 jev-1.13.0，因为阈值是按模型版本调的。 <sub>(机翻)</sub>
  <sub>`开源项目` · aurorainfra · `Go` · 调用点 [`internal/jev/price.go`](https://github.com/aurorainfra/grev/blob/HEAD/internal/jev/price.go)</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — 一个文本审核演示：一次 systemOne 调用并行检查七个 Noul 风险项和一个严重程度 Score，最终结论由代码按策略阈值计算。 <sub>(机翻)</sub>
  <sub>`开源项目` · norbertbodziony · `TS` · 调用点 [`app/api/moderate/route.ts`](https://github.com/NorbertBodziony/guard-jev/blob/HEAD/app/api/moderate/route.ts)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[himalaya-jev-mail-classify](https://github.com/initrd/himalaya-jev-mail-classify)** — 用语言模型给 Gmail 打标签、排优先级：通过 himalaya 读取邮件，用 Jev（TypeSafe）为每个会话分类。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · initrd · `Py` · 调用点 [`mail_classify.py`](https://github.com/initrd/himalaya-jev-mail-classify/blob/HEAD/mail_classify.py)，2026-09-24 阅读</sub>

- **[hunch](https://github.com/steven-shoemaker/hunch)** — 对数据列向 Jev 提问：封闭集合的问题，带缓存，并把结果连接回原表。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · steven-shoemaker · `Py` · 调用点 [`src/hunch/client.py`](https://github.com/steven-shoemaker/hunch/blob/HEAD/src/hunch/client.py)，2026-09-24 阅读</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — 不确定时保持沉默的 issue 分拣：校准过的标签，含垃圾与重复检测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · emreozyoruk · `JS` · 调用点 [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · Really Artificial · `JS` · `choice` · `score` · `noul` · 调用点 [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs)，2026-09-22 阅读 · ⚠ `疑似 AI 生成`</sub>

- **[Jev Playwright](https://github.com/arthurfiorette/jev-playwright)** — 一个 Playwright 报告器：在启动任何浏览器之前，询问 Jev 某次代码改动可能影响哪些现有端到端测试，并跳过明显无关的测试。默认会发送改动路径、补丁和测试代码；README 提醒它可能漏掉受影响的测试。 <sub>(机翻)</sub>
  <sub>`开源项目` · arthurfiorette · `TS` · 调用点 [`src/config.ts`](https://github.com/arthurfiorette/jev-playwright/blob/HEAD/src/config.ts)</sub>

- **[JEV Sees](https://github.com/CharlesFeng0314/JEV_sees)** — 让 Jev“看见”：本地的 Florence-2 和 CLIP 模型在图像、视频或 RGB-D 画面中找出物体，并在帧之间保持物体 ID 一致，然后由 Jev 针对每个相关物体回答 choice、noul 或 score 问题（如公交车颜色、行人风险、动物运动状态）。 <sub>(机翻)</sub>
  <sub>`开源项目` · charlesfeng0314 · `Py` · `choice` · `noul` · `score` · 调用点 [`jev_sees/session.py`](https://github.com/CharlesFeng0314/JEV_sees/blob/HEAD/jev_sees/session.py)</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · yuyang2230 · `Py` · 调用点 [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py)，2026-09-22 阅读</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — TypeSafe AI Jev 在智能体工具调用风险分类上的可复现基准：准确率、延迟，以及其置信度是否可信。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · themsquared · `Py` · 调用点 [`bench.py`](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py)，2026-09-24 阅读</sub>

- **[jev-chess](https://github.com/hemanth/jev-chess)** — 用 Jev 做国际象棋的着法、局面评估、人格对手与棋局分类。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hemanth · `TS` · 调用点 [`src/typeSafeClient.ts`](https://github.com/hemanth/jev-chess/blob/HEAD/src/typeSafeClient.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-clean](https://github.com/Kunyanli230/jev-clean)** — 以决策为先的数据清洗系统，由 Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kunyanli230 · `Py` · 调用点 [`src/idac/typesafe_client.py`](https://github.com/Kunyanli230/jev-clean/blob/HEAD/src/idac/typesafe_client.py)，2026-09-24 阅读</sub>

- **[Jev-Code-Reviewer](https://github.com/egma-ai/jev-code-reviewer)** — 用于审阅编程 Agent 所提 PR 的本地工具：按书面的优先级规则，用 Jev 的 choice 把每处改动分为 P0、P1 或 P2，默认只显示 P0。不会向 GitHub 发布任何内容。 <sub>(机翻)</sub>
  <sub>`开源项目` · egma-ai · `JS` · `choice` · 调用点 [`src/providers.mjs`](https://github.com/egma-ai/jev-code-reviewer/blob/HEAD/src/providers.mjs)</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — 对文本文档做快速且低成本的分类。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · charlyhno-eng · `TS` · 调用点 [`server/classification-cache.ts`](https://github.com/Charlyhno-eng/jev-document-classification/blob/HEAD/server/classification-cache.ts)，2026-09-22 阅读</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — 面向智能体的 Haskell DSL：类型化数据包、类型推断，答案与问题同构。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · inanna-malick · `Hs` · 调用点 [`scripts/curate-fixtures.py`](https://github.com/inanna-malick/jev-dsl/blob/HEAD/scripts/curate-fixtures.py)，2026-09-22 阅读</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — 在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub>
  <sub>`基准测试` · 4esv · `Py` · 调用点 [`evaljev/runners.py`](https://github.com/4esv/jev-eval/blob/HEAD/evaljev/runners.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-eval](https://github.com/onlyoneaman/jev-eval)** — 在四个公开分类数据集上比较 TypeSafe 的 Jev 与两款 GPT 模型：案例、逐条答案、评分全部公开。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · onlyoneaman · `TS` · 调用点 [`jev_eval/backends.py`](https://github.com/onlyoneaman/jev-eval/blob/HEAD/jev_eval/backends.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · foadsf · `Py` · 调用点 [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/HEAD/jev.py)，2026-09-22 阅读</sub>

- **[jev-issue-radar](https://github.com/Patrick-SCH03/jev-issue-radar)** — 带并排证据的 GitHub issue 分拣，可免配置试用公开样例。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · patrick-sch03 · `JS` · 调用点 [`lib/jev.mjs`](https://github.com/Patrick-SCH03/jev-issue-radar/blob/HEAD/lib/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-labeler-action](https://github.com/yamadashy/jev-labeler-action)** — 零配置的 AI 议题打标签工具，基于 TypeSafe 的 Jev。不生成文本，非官方。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · yamadashy · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/yamadashy/jev-labeler-action/blob/HEAD/src/jev/client.ts)，2026-09-24 阅读</sub>

- **[jev-linkedin-slop-filter](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter)** — 给 LinkedIn 上的流量诱饵贴上 BAIT、CORP 或 BRAG 的标签，由 Jev（TypeSafe System One）实时判定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arpit-khandelwal · `JS` · 调用点 [`server/jev.js`](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter/blob/HEAD/server/jev.js)，2026-09-24 阅读</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jyatesdotdev · `Py` · 调用点 [`logtriage/cli.py`](https://github.com/jyatesdotdev/jev-logtriage/blob/HEAD/logtriage/cli.py)，2026-09-22 阅读</sub>

- **[jev-mail](https://github.com/muhammedilyasy/jev-mail)** — 用 TypeSafe Jev 模型为 Gmail 做分诊的 Chrome 扩展：为每封邮件给出类别、优先级、垃圾邮件概率和需回复概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · muhammedilyasy · `JS` · 调用点 [`src/common/jev.js`](https://github.com/muhammedilyasy/jev-mail/blob/HEAD/src/common/jev.js)，2026-09-24 阅读</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — Jev 的 MCP server：提供官方三种问题类型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · wangkuangkuang · `Py` · 调用点 [`src/jev_mcp_server/config.py`](https://github.com/wangkuangkuang/jev-mcp-server/blob/HEAD/src/jev_mcp_server/config.py)，2026-09-22 阅读</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — 编程智能体总在不难的决策上烧上下文 —— 分拣 400 条工单之类的活儿不该这么贵。 <sub>(机翻)</sub>
  <sub>`开源项目` · ddfeyes · `Py` · 调用点 [`src/jev_mode/client.py`](https://github.com/ddfeyes/jev-mode/blob/HEAD/src/jev_mode/client.py)，2026-09-22 阅读</sub>

- **[jev-organize](https://github.com/nexibeo/jev-organize)** — 把一堆公司文件扔进去，就能按部门、类型、敏感度、日期、交易方等分类整理好。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nexibeo · `JS` · 调用点 [`skills/jev-organize/scripts/src/jev.mjs`](https://github.com/nexibeo/jev-organize/blob/HEAD/skills/jev-organize/scripts/src/jev.mjs)，2026-09-24 阅读</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev 增强的 Playwright MCP 代理：页面状态分拣与提示注入防护。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · krw82 · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/krw82/jev-playwright-mcp/blob/HEAD/src/jev/client.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-pr-labeler](https://github.com/1jehuang/jev-pr-labeler)** — 用 Jev 的类型化决策给 GitHub PR 打语义标签，依据概念范围而不是改动行数。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 1jehuang · `Py` · 调用点 [`jev_labeler/classifier.py`](https://github.com/1jehuang/jev-pr-labeler/blob/HEAD/jev_labeler/classifier.py)，2026-09-24 阅读</sub>

- **[jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline)** — 针对长期问题的每日研究监控：确定性的 Python 掌控流程，TypeSafe Jev 按问题筛选信息源，Qwen 撰写笔记（试点）。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shimo4228 · `Py` · 调用点 [`src/jev_research_pipeline/jev/core.py`](https://github.com/shimo4228/jev-research-pipeline/blob/HEAD/src/jev_research_pipeline/jev/core.py)，2026-09-24 阅读</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 给 Spring WebFlux 的非阻塞 Starter，实现一个语义熔断器来检测静默故障。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · vicente-md · `Java` · 调用点 [`src/main/java/ai/jev/resilience/client/dto/JevRequest.java`](https://github.com/Vicente-MD/jev-resilience/blob/HEAD/src/main/java/ai/jev/resilience/client/dto/JevRequest.java)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — 可配置的 GitHub 提交审查与 PR 分类，不使用任何文本生成模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · fatwang2 · `JS` · 调用点 [`src/jev.mjs`](https://github.com/fatwang2/jev-review-action/blob/HEAD/src/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · teyhouse · `Py` · 调用点 [`main.py`](https://github.com/teyhouse/jev-secret-detection/blob/HEAD/main.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-skip](https://github.com/valentynkit/jev-skip)** — 读字幕、在观看时判断，从而跳过视频里的赞助段落。
  <sub>`开源项目` · valentynkit · `TS` · 调用点 [`lib/jev.ts`](https://github.com/valentynkit/jev-skip/blob/HEAD/lib/jev.ts)，2026-09-22 阅读</sub>

- **[jev-slop-guard](https://github.com/davertor/jev-slop-guard)** — Jev Slop Guard：一个 Chrome 扩展，在你浏览 X 和 LinkedIn 时为 AI 生成的垃圾内容打分并盖章。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · davertor · `JS` · 调用点 [`lib/jev.ts`](https://github.com/davertor/jev-slop-guard/blob/HEAD/lib/jev.ts)，2026-09-24 阅读</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — 把 Jev 的 noul 原语应用到一个共谋语料库上。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · sypherin · `Py` · 调用点 [`jev_client.py`](https://github.com/sypherin/jev-trace-classifier/blob/HEAD/jev_client.py)，2026-09-22 阅读</sub>

- **[jev-triage](https://github.com/cephalization/jev-triage)** — 拉取并同步大型仓库以做 issue 分拣。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cephalization · `TS` · 调用点 [`apps/api/src/worker/typesafe.ts`](https://github.com/cephalization/jev-triage/blob/HEAD/apps/api/src/worker/typesafe.ts)，2026-09-22 阅读</sub>

- **[Jevatar](https://github.com/AppChainAI/Jevatar)** — 一个只用面部表情回复的 AI 伙伴：Jev（TypeSafe System One）判断你的消息，并挑选一个表情。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · appchainai · `TS` · 调用点 [`server.ts`](https://github.com/AppChainAI/Jevatar/blob/HEAD/server.ts)，2026-09-24 阅读</sub>

- **[jevbench](https://github.com/GautamTalksDev/jevbench)** — 对 TypeSafe Jev 在人类意见分歧下的校准进行预注册、经偏差校正的测试（ChaosNLI，每条 100 个人工标注） <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · Gautam Khosla · `Py` · `choice` · `noul` · 调用点 [`jevbench/clients/jev.py`](https://github.com/GautamTalksDev/jevbench/blob/HEAD/jevbench/clients/jev.py) · 作者结论：好坏参半（作者自述，未经本仓库复现） · ⚠ `疑似 AI 生成` `作者自荐`</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — 用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jkrup · `JS` · 调用点 [`src/client.mjs`](https://github.com/jkrup/jeveryword/blob/HEAD/src/client.mjs)，2026-09-22 阅读</sub>

- **[JevEye](https://github.com/Adityakhalkar/JevEye)** — 向 Jev 询问一张图片：CNN 报告它看到了什么（带校准置信度或选择弃权），再由 Jev 判断这意味着什么。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · adityakhalkar · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/Adityakhalkar/JevEye/blob/HEAD/src/lib/jev.ts)，2026-09-24 阅读</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — 面向社区和应用的内容审核，由 Jev（TypeSafe）驱动：按类别给出概率，阈值由你掌控。支持 Discord。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ohernandezdev · `Py` · 调用点 [`jevmod/judge.py`](https://github.com/ohernandezdev/jevmod/blob/HEAD/jevmod/judge.py)，2026-09-24 阅读</sub>

- **[Jevstiller](https://github.com/tomerglick57/Jevstiller)** — 放在重复性 Jev 分类调用前面的代理：起初全部转发给 Jev，用 Jev 自己的答案和概率训练一个本地小模型，等它在留出流量上与 Jev 足够一致后改为本地作答。作者报告 Banking77 上有 61.7% 的消息由本地回答，与 Jev 的一致率为 99.4%。 <sub>(机翻)</sub>
  <sub>`开源项目` · tomerglick57 · `Py` · `choice` · `noul` · 调用点 [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/HEAD/jevstiller/teachers/jev.py) · ⚠ `厂商自报数据`</sub>

- **[JevT++](https://github.com/wiatrM/jevtpp)** — 一个 C++20 库，通过编译期模式把运行时的文本、JSON 或对象转换为枚举、布尔值和分数，提供完整概率分布并支持显式弃权。可在进程内运行本地 Laya 模型（ONNX Runtime 或 ggml），也可通过可选的远程后端调用 Jev；附带延迟指标和马里奥游戏演示。 <sub>(机翻)</sub>
  <sub>`SDK` · wiatrm · `C++` · 调用点 [`include/jevt/remote.hpp`](https://github.com/wiatrM/jevtpp/blob/HEAD/include/jevt/remote.hpp)</sub>

- **[jevticktrouter](https://github.com/GhrezaKh74/JevTicktRouter)** — 用 .NET 10 与 React 19 做的快速结构化工单分拣。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ghrezakh74 · `C#` · 调用点 [`backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs`](https://github.com/GhrezaKh74/JevTicktRouter/blob/HEAD/backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevtriage](https://github.com/sathariels/jevtriage)** — GitHub Action 与 CLI：用 TypeSafe Jev 为 PR 分诊（可以合并 / 需要审查 / 有风险），并带置信度关卡。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · sathariels · `Py` · 调用点 [`src/jevtriage/client.py`](https://github.com/sathariels/jevtriage/blob/HEAD/src/jevtriage/client.py)，2026-09-24 阅读</sub>

- **[jlink](https://github.com/keltokhy/jlink)** — 给经济学家用的记录链接：用自然语言写匹配规则，对每一对记录得到一个概率，可审计、可引用。支持 Python、CLI、Stata 和 R。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · keltokhy · `Py` · 调用点 [`bench/local_models.py`](https://github.com/keltokhy/jlink/blob/HEAD/bench/local_models.py)，2026-09-24 阅读</sub>

- **[metis](https://github.com/Ayush0054/metis)** — Metis：由 Jev 驱动的 GitHub issue 自动分拣，可复用的 GitHub Action。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ayush0054 · `Py` · 调用点 [`src/metis_triage/_triage.py`](https://github.com/Ayush0054/metis/blob/HEAD/src/metis_triage/_triage.py)，2026-09-22 阅读</sub>

- **[mysql-ailike](https://github.com/maayanlevy/mysql-ailike)** — MySQL 的自然语言行过滤，由 TypeSafe Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · maayanlevy · `C++` · 调用点 [`src/typesafe.h`](https://github.com/maayanlevy/mysql-ailike/blob/HEAD/src/typesafe.h)，2026-09-24 阅读</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — Jev 的 n8n 社区节点：带校准概率的文本分类、打分与检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · khmuhtadin · `TS` · 调用点 [`nodes/JevClassification/JevClassification.node.ts`](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/HEAD/nodes/JevClassification/JevClassification.node.ts)，2026-09-22 阅读</sub>

- **[notiq](https://github.com/chengyongru/notiq)** — 原生 Android 通知过滤，用自然语言写规则，由 Jev 或自托管的 FastJev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · chengyongru · `Kt` · 调用点 [`app/src/main/java/dev/notiq/data/Settings.kt`](https://github.com/chengyongru/notiq/blob/HEAD/app/src/main/java/dev/notiq/data/Settings.kt)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — 给 OMP 的模型裁决式权限闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · strml · `TS` · 调用点 [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts)，2026-09-22 阅读 · ⚠ `已归档`</sub>

- **[one-system](https://github.com/rawwerks/one-system)** — 通过统一接口使用本地与托管的分类器（即决策模型）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · rawwerks · `TS` · 引用文件 [`examples/public_release_review.py`](https://github.com/rawwerks/one-system/blob/HEAD/examples/public_release_review.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — 检测 AI 智能体循环中的语义停滞。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ashutoshvjti · `TS` · 调用点 [`experiments/jev-client.ts`](https://github.com/AshutoshVJTI/progressgate/blob/HEAD/experiments/jev-client.ts)，2026-09-22 阅读</sub>

- **[pulselane](https://github.com/ndolinschi/pulselane)** — PulseLane：诊所分诊决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/pulselane/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[tab-bouncer](https://github.com/MANISH007700/tab-bouncer)** — 一个关闭多余标签页的 Chrome 扩展，由 TypeSafe Jev 一次调用完成判断。告诉它你在做什么即可。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · manish007700 · `JS` · 调用点 [`judge.js`](https://github.com/MANISH007700/tab-bouncer/blob/HEAD/judge.js)，2026-09-24 阅读</sub>

- **[triagedy](https://github.com/m0rphtail/triagedy)** — 把告警分拣做成 UNIX 过滤器：JSONL 安全告警进，类型化决策出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · m0rphtail · `Rs` · 调用点 [`src/backends/jev.rs`](https://github.com/m0rphtail/triagedy/blob/HEAD/src/backends/jev.rs)，2026-09-22 阅读</sub>

- **[twitter-jev-guard](https://github.com/qs-lll/twitter-jev-guard)** — 使用 TypeSafe Jev 在 X/Twitter 时间线上识别低质量、垃圾和广告帖子，并在文字区域显示醒目的半透明水印。
  <sub>`插件` · qs-lll · `JS` · 调用点 [`extension/background.js`](https://github.com/qs-lll/twitter-jev-guard/blob/HEAD/extension/background.js)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — 用通用分类器做扩散风格像素画：256 个并行像素问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · wizhill05 · `TS` · 调用点 [`fix_synthesizer.py`](https://github.com/Wizhill05/typesafe-image-diffusion/blob/HEAD/fix_synthesizer.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — 基于 Jev 的三条可组合判断流水线：工单分拣、可观测性等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shivam2003-dev · `Py` · 调用点 [`src/triage/mock.py`](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/HEAD/src/triage/mock.py)，2026-09-22 阅读</sub>

- **[vibecheck](https://github.com/jlowin/vibecheck)** — 把 System One 调用变成普通 Python 值的库：check（是/否）、classify（选一个）、label（选出所有适用项）和 score，支持阈值、“不确定”回答，以及把针对同一数据的多个问题合并成一批。可对接 TypeSafe 或任何兼容服务器。 <sub>(机翻)</sub>
  <sub>`SDK` · jlowin · `Py` · `noul` · 调用点 [`src/vibecheck/backends.py`](https://github.com/jlowin/vibecheck/blob/HEAD/src/vibecheck/backends.py)</sub>

- **[watfile](https://github.com/jexp/watfile)** — 用 Jev 或本地校准决策模型给文本与 PDF 分类归档。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jexp · `Py` · 调用点 [`src/watfile/classifier/jev.py`](https://github.com/jexp/watfile/blob/HEAD/src/watfile/classifier/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。
  <sub>`基准测试` · ★100+ · ⚠ `无许可证` `宣称未核实`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。
  <sub>`基准测试` · Lindfors</sub>

- **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)** — 一位 ML 工程师从分类任务角度做的讲解 —— 这个切入角度最贴近模型的实际能力。
  <sub>`视频` · Sam Witteveen</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
