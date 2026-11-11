# 分类

<sub>[awesome-jev](../../README.zh-CN.md) · [English](classification.md)</sub>

_把条目归入分类体系，包括用概率遍历的深层层级。_

这个决策的全部已收录例子 —— 共 179 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#分类)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#classification)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#classification)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 4 · 调用点 168 · 接口形态 2 · 仅示例 0 · 独立报告 19 · 负面结果 1 · 未引用文件 9。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [WorkflowEvals](https://github.com/typesafe-ai/workflowevals) <sub>`基准测试` · `Py` · `noul` · `choice` · `score` · ⚠ `仅一次提交` `厂商自报数据`</sub>
- [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) <sub>`官方文档` · `Py` · `choice`</sub>
- [Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) <sub>`官方文档` · `Py` · `choice`</sub>
- [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) <sub>`官方文档` · `Py` · `score`</sub>
- [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) <sub>`官方文档` · `Py`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[WorkflowEvals](https://github.com/typesafe-ai/workflowevals)** ⭐ — TypeSafe 用于复现其 WorkflowEvals 评测网站的代码：四个业务流程（发票审批与欺诈分拣、客服路由与处置、智能体运行中的动作选择、安全告警分拣），共 705 个案例，以 OpenAI、Anthropic 及共识结果为参考来评分。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · typesafe-ai · `Py` · `noul` · `choice` · `score` · 调用点 [`core/clients.py`](https://github.com/typesafe-ai/workflowevals/blob/HEAD/core/clients.py)，2026-11-02 模型阅读 · ⚠ `仅一次提交` `厂商自报数据`</sub>

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — 用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · 调用点 [`apps/web/utils/decision-model/decision-model.ts`](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/decision-model.ts)，2026-11-05 模型阅读</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★10k+ · Vercel Labs · `TS` · `choice` · 调用点 [`apps/web/lib/jev/compose.ts`](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts)，2026-09-22 阅读</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★10k+ · `TS` · `choice` · 调用点 [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现） · ⚠ `仅影子运行`</sub>

- **[ContextGem](https://github.com/shcherbak-ai/contextgem)** — 用 LLM 和决策模型从文档中抽取结构化数据的 Python 框架。配合 Jev 这类决策模型时，它对每个段落提一个是非题，找出每个方面（aspect）对应的条款，并把布尔、标签和评级概念转成 noul、choice 和 score 问题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · shcherbak-ai · `Py` · `noul` · `choice` · `score` · 调用点 [`contextgem/internal/base/decision_models.py`](https://github.com/shcherbak-ai/contextgem/blob/HEAD/contextgem/internal/base/decision_models.py)，2026-11-06 模型阅读</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · 调用点 [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql)，2026-09-22 阅读</sub>

- **[332_lab-jev-chat](https://github.com/Liyucheng1997/332_lab-jev-chat)** — 电脑版微信助手：由 Jev 判断每条消息的意图，DeepSeek 给出建议回复。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · liyucheng1997 · `Kt` · 调用点 [`windows/jev_windows/jev_api.py`](https://github.com/Liyucheng1997/332_lab-jev-chat/blob/HEAD/windows/jev_windows/jev_api.py)，2026-09-24 阅读</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · 调用点 [`src/search.ts`](https://github.com/ellipsis-dev/blink/blob/HEAD/src/search.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)** — 基于纯 HTTP 的零样本文本分类，无需密钥或注册：传入标签和文本，返回一个标签和校准过的置信度，一次请求可含一千条文本。两个档位都由 Jev 作答：每条文本一个 choice，多标签时每个标签一个 noul；smart 档会把置信度低于 0.7 的答案交给推理模型重答。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · mrmps · `TS` · 调用点 [`src/jev.ts`](https://github.com/mrmps/classifier-dev/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — 对 PDF、DOCX 和 PPTX 文件做分类和切分：LiteParse 在本地提取每页文字，然后 Jev 用一个 choice 按你的规则选出文档类别；对多文档合订本则逐页回答一个类别 choice 和一个“新文档是否从这里开始”的 noul。其报告涵盖 40 份真实 PDF。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · jerryjliu · `Py` · 调用点 [`src/jev_docs/engines/jev.py`](https://github.com/jerryjliu/docjev/blob/HEAD/src/jev_docs/engines/jev.py)，2026-09-22 阅读</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)** — Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、原速回放与离线报告。
  <sub>`基准测试` · ★100+ · nanmicoder · `JS` · 调用点 [`src/backends/jev.mjs`](https://github.com/NanmiCoder/jev-arena/blob/HEAD/src/backends/jev.mjs)，2026-09-24 阅读</sub>

- **[Jev-Code-Reviewer](https://github.com/egma-ai/jev-code-reviewer)** — 用于审阅编程 Agent 所提 PR 的本地工具：按书面的优先级规则，用 Jev 的 choice 把每处改动分为 P0、P1 或 P2，默认只显示 P0。不会向 GitHub 发布任何内容。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · egma-ai · `JS` · `choice` · 调用点 [`src/providers.mjs`](https://github.com/egma-ai/jev-code-reviewer/blob/HEAD/src/providers.mjs)，2026-10-24 模型阅读</sub>

- **[jev-job-search](https://github.com/qbeka/jev-job-search)** — 在 Claude Code 里运行的求职申请工具：经 OpenRouter 问 Jev 每个职位是否是带薪的软件岗位、级别和入职时间是否合适、技术栈匹配度如何，以及每个表单字段该填哪条已存答案或哪个选项，然后在 Chrome 里填好表单等你确认。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · qbeka · `TS` · `noul` · `choice` · `score` · 调用点 [`src/jev/client.ts`](https://github.com/qbeka/jev-job-search/blob/HEAD/src/jev/client.ts)，2026-11-10 模型阅读</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts)，2026-09-22 阅读</sub>

- **[Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis)** — 按需使用的加密市场情报终端：选定币种和推文样本数量，Jev 结合行情、资金费率与社交情绪给出买入、卖出、持有或止盈的决策卡片，不会自动下单。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · brainstormity · `Py` · 调用点 [`app/services/typesafe_service.py`](https://github.com/brainstormity/Jev-X-Sentiment-Analysis/blob/HEAD/app/services/typesafe_service.py)，2026-09-24 阅读</sub>

- **[jev4pg](https://github.com/Sheltercosmo/jev4pg)** — 为 PostgreSQL 提供自然语言 SQL 和 41 个语义算子。过滤、抽取、排序、匹配和核验以有上限的批次交给 Jev，答案须先通过校验；choice 选项需达 0.55、noul 需达 0.8 才算成立。作者报告其准确率为 98%，pg-jev 的请求路径为 92%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · Sheltercosmo · `Py` · `choice` · `noul` · 调用点 [`sdd/generic/jev.py`](https://github.com/Sheltercosmo/jev4pg/blob/HEAD/sdd/generic/jev.py)，2026-10-26 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js)，2026-09-22 阅读</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `score` · 调用点 [`engine/jev-service.ts`](https://github.com/irfndi/prism-liquidity-agent/blob/HEAD/engine/jev-service.ts)，2026-09-22 阅读</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — 本地优先的工作助手：把邮件、聊天和工单变成任务，交给你的编程智能体去做，未经你批准什么都不会发出。配置 TypeSafe 密钥后由 Jev 分诊：状态里带上你的资料和过往判断，用 noul 按你会怎么判断来提问，例如这一项要不要建成任务。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · ldbumble · `Py` · 调用点 [`taskuary/jev.py`](https://github.com/ldbumble/taskuary/blob/HEAD/taskuary/jev.py)，2026-09-22 阅读</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — 税务文档分页分类器：每页一次请求，问 Jev 两个 choice：页面类型（7 个选项）和 IRS 表单（230 个另加“不在列表中”），五种表单的附表再用一个后续 choice 细分；选项描述由 IRS 官方 PDF 生成，代码以 0.95 为门槛。作者在 314 页已填写表单上测得严格错误为零。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · kyotofin · `TS` · 调用点 [`src/backend.ts`](https://github.com/kyotofin/tax-doc-classifier/blob/HEAD/src/backend.ts)，2026-09-22 阅读</sub>

- **[tev1-4B-experimental](https://github.com/togethercomputer/tev1)** — Together AI 微调 Qwen3.5-4B，用一个选项字母回答决策问题。在对三个公开 Jev 基准的配对重跑中，它在钓鱼邮件上得 50.6%，Jev 1.13 为 62.9%；工具风险上两者都是 93.3%；工单路由上为 96.3%，Jev 为 100%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★100+ · togethercomputer · `Py` · `choice` · 调用点 [`evaluation/public-third-party/run.py`](https://github.com/togethercomputer/tev1/blob/HEAD/evaluation/public-third-party/run.py)，2026-11-05 模型阅读</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — 一个浏览器扩展，用可复用的模板规则清除页面杂物。
  <sub>`开源项目` · ★100+ · kitze · `TS` · 调用点 [`lib/jev.ts`](https://github.com/kitze/unclutter/blob/HEAD/lib/jev.ts)，2026-09-22 阅读</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 跳过 YouTube 赞助口播的 Chrome 扩展：字幕按每 80 行分窗，用 Jev 的 noul 判断口播是否从这里开始，用 choice 指出是哪一行，再对短语逐个用 noul 定下切点；由代码把行号换算成秒数。音频模式每隔几秒问 Jev 口播是否正在播放。默认把握达到 70% 才跳过。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · trungdq88 · `JS` · 调用点 [`extension/lib/jev.js`](https://github.com/trungdq88/youtube-sponsor-detection/blob/HEAD/extension/lib/jev.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[Apparite](https://github.com/dglazkov/jev2ui)** — 把文字描述变成可点击应用样稿、并按 DESIGN.md 上色的设计工具：Jev 在一次 choice 和 noul 请求里决定一个界面有哪些区块、用什么布局和图标，以及后续每条消息要求改什么；文字由一个小型 Gemini 模型撰写，界面由代码拼装。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · dglazkov · `TS` · `choice` · `noul` · `score` · 调用点 [`src/server/plan.ts`](https://github.com/dglazkov/jev2ui/blob/HEAD/src/server/plan.ts)，2026-11-09 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · 24601 · `Py` · 调用点 [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md)，2026-09-24 阅读</sub>

- **[Claude x Jev](https://github.com/charlesdove977/claude-x-jev)** — Claude Code 技能及配套命令：由 Jev（经 OpenRouter）负责分拣，Claude 负责写作。可以批量分类、核查或打分，只把不确定的条目交给 Claude，核对 Claude 的草稿，并用 PreToolUse 钩子把关工具调用，询问该调用能否撤销、是否服务于当前任务。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · charlesdove977 · `Py` · `choice` · `noul` · `score` · 调用点 [`skill/scripts/jev.py`](https://github.com/charlesdove977/claude-x-jev/blob/HEAD/skill/scripts/jev.py)，2026-10-30 模型阅读 · ⚠ `营销内容`</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — 用 Jev 对 Git 提交的 diff 与信息做分类：缺陷修复、安全修复、变更类型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · devanshbatham · `Rs` · 调用点 [`src/jev.rs`](https://github.com/devanshbatham/commit-miner/blob/HEAD/src/jev.rs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[DMB: decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — 针对“从列表中选一项并给出置信度”这类 API 的基准测试：比较 Jev、带结构化输出的 LLM 和确定性基线的准确率、延迟、成本、失败率和置信度。作者报告 jev-latest 在 Banking77 上为 79.2%，CLINC150 上为 88.6%，NLU++ 上微平均 F1 为 48.3%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · nibzard · `Py` · `choice` · 调用点 [`src/dmb/contenders/jev.py`](https://github.com/nibzard/decision-model-benchmark/blob/HEAD/src/dmb/contenders/jev.py)，2026-11-04 模型阅读 · ⚠ `无许可证`</sub>

- **[DriveSceneMiner](https://github.com/bskkimm/drivesceneminer)** — 从车辆记录数据中挖掘驾驶动作：把运动、车道几何和与其他物体的交互转换成可读的证据，由 Jev 用 choice 问题对每个时刻的横向和纵向动作分类，再把这些时刻合并成带时间戳、可供审阅的场景。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · bskkimm · `Py` · `choice` · 调用点 [`src/jevsceneminer/inference/jev.py`](https://github.com/bskkimm/drivesceneminer/blob/HEAD/src/jevsceneminer/inference/jev.py)，2026-11-07 模型阅读</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — 为 DeepSeek Harness 中的每一次工具调用提供毫秒级 System-1 判断——由 Jev 驱动的风险分类与证据检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · asktheway · `TS` · 调用点 [`scripts/smoke.mjs`](https://github.com/AskTheWay/dsh-jev-interceptor/blob/HEAD/scripts/smoke.mjs)，2026-09-24 阅读</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · prasanthj · `C++` · 调用点 [`benchmarks/live.py`](https://github.com/prasanthj/duckdb-jev/blob/HEAD/benchmarks/live.py)，2026-09-22 阅读</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · evoke-build · `Rs` · 调用点 [`crates/evoke-adapters/src/systemone.rs`](https://github.com/evoke-build/evoke/blob/HEAD/crates/evoke-adapters/src/systemone.rs)，2026-09-24 阅读</sub>

- **[grev](https://github.com/aurorainfra/grev)** — 用提问代替模式匹配的 Unix 过滤工具：`grev 'is a vegan meal' menu.txt` 只保留 Jev 回答“是”的行；配套工具还会用到 choice 的置信度或路径分数。默认固定 jev-1.13.0，因为阈值是按模型版本调的。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · aurorainfra · `Go` · 调用点 [`internal/jev/price.go`](https://github.com/aurorainfra/grev/blob/HEAD/internal/jev/price.go)，2026-10-24 模型阅读</sub>

- **[Gut](https://github.com/vinibrsl/gut)** — 用于 LLM 决策的 Elixir DSL：Gut.feel(subject, question, choices) 返回你给定的某个 Elixir 值，例如应处理某张工单的团队。其 Jev 适配器通过 ReqLLM 以一个 Choice 问题提问；其他适配器可用任意 ReqLLM 模型、Ollama 或你自己的代码。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · vinibrsl · `Ex` · `choice` · 调用点 [`lib/gut/req_llm/jev.ex`](https://github.com/vinibrsl/gut/blob/HEAD/lib/gut/req_llm/jev.ex)，2026-11-02 模型阅读</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把关于家的类型化答案变成传感器，提供可用于自动化的 noul、choice 和 score 动作，以及一个对话代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · 调用点 [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py)，2026-09-30 阅读 · ⚠ `疑似 AI 生成` `作者自荐`</sub>

- **[Jev Account Filter](https://github.com/caiweihan/jev-account-filter)** — 把视频平台账号（抖音、快手、YouTube、哔哩哔哩）作为数据集来源进行筛选：根据账号的视频标题、封面缩略图、名称和简介，用一次 Jev 请求判断其类别、相关概率、每个视频的相关度以及最佳视频。手语创作者是已验证的场景。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · caiweihan · `Py` · `choice` · `noul` · 调用点 [`account_filter/screening/classifier.py`](https://github.com/caiweihan/jev-account-filter/blob/HEAD/account_filter/screening/classifier.py)，2026-10-31 模型阅读</sub>

- **[Jev Ad Blocker](https://github.com/fazlerocks/jev-adblock)** — 不用过滤规则列表的 Chrome 广告拦截扩展：它用几个结构字段描述页面上每个像广告的元素，在一个批量请求里为每个元素问 Jev 一个 choice（展示广告、赞助内容、同意弹窗或弹出层、网站自家推广、正文内容、界面元素）；超过各类别阈值的元素由代码隐藏。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · fazlerocks · `TS` · `choice` · 调用点 [`src/shared/jev/questions.ts`](https://github.com/fazlerocks/jev-adblock/blob/HEAD/src/shared/jev/questions.ts)，2026-11-08 模型阅读</sub>

- **[Jev and open decision-model benchmarks](https://github.com/akitaonrails/jev-docs-benchmarks)** — 评测决策模型执行给定规则的可靠性、其概率的表现以及决策成本：把托管的 Jev 与 Microsoft Decision-1、OpenAI Decisions 以及 Clef、Decision 3.0、Laya、Kev、Jebadiah 等开源模型对比，使用冻结的输入并公开原始响应。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · akitaonrails · `Py` · `choice` · 调用点 [`benchmark/tools/hosted.py`](https://github.com/akitaonrails/jev-docs-benchmarks/blob/HEAD/benchmark/tools/hosted.py)，2026-11-07 模型阅读 · ⚠ `无许可证`</sub>

- **[Jev Guard](https://github.com/gulbaki/jev-llm-guard)** — 面向 LLM 应用所处理文本的护栏，涵盖用户输入、检索内容、工具输出或模型输出：Jev 针对 OWASP LLM Top 10 的十类风险各回答一个是非题，另给出攻击类型和严重度评分，再由带版本号的本地策略将其转为放行、复核或拦截。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · gulbaki · `JS` · `noul` · `choice` · `score` · 调用点 [`src/guard.js`](https://github.com/gulbaki/jev-llm-guard/blob/HEAD/src/guard.js)，2026-11-03 模型阅读</sub>

- **[JEV Healthcare Lab](https://github.com/juneyaooo/jev-healthcare-lab)** — Jev 医疗决策基准：以 choice 问题覆盖 26 项任务、1,514 项判断（分诊紧急程度、禁忌判断、用药选择、护理、临床试验筛选），与 DeepSeek Flash 和 Qwen 对比准确率、持续吞吐和成本，并公开原始响应。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · juneyaooo · `Py` · `choice` · 调用点 [`scripts/run_model_evaluation.py`](https://github.com/juneyaooo/jev-healthcare-lab/blob/HEAD/scripts/run_model_evaluation.py)，2026-11-07 模型阅读 · ⚠ `无许可证`</sub>

- **[JEV Sees](https://github.com/CharlesFeng0314/JEV_sees)** — 让 Jev“看见”：本地的 Florence-2 和 CLIP 模型在图像、视频或 RGB-D 画面中找出物体，并在帧之间保持物体 ID 一致，然后由 Jev 针对每个相关物体回答 choice、noul 或 score 问题（如公交车颜色、行人风险、动物运动状态）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · charlesfeng0314 · `Py` · `choice` · `noul` · `score` · 调用点 [`jev_sees/session.py`](https://github.com/CharlesFeng0314/JEV_sees/blob/HEAD/jev_sees/session.py)，2026-10-24 模型阅读</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · forvela · `JS` · 调用点 [`src/decision.js`](https://github.com/forvela/jev-agent-browser/blob/HEAD/src/decision.js)，2026-09-22 阅读</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · smkrv · `TS` · 调用点 [`src/client.ts`](https://github.com/smkrv/jev-calibrate/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · francoischastel · `TS` · 调用点 [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts)，2026-09-22 阅读</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · goodrahstar · `JS` · 调用点 [`lib/racers.mjs`](https://github.com/goodrahstar/jev-column-race/blob/HEAD/lib/racers.mjs)，2026-09-22 阅读</sub>

- **[jev-datafusion](https://github.com/parable-work/jev-datafusion)** — 一个 Rust crate，把 Jev 注册为 Apache DataFusion 中的 SQL 函数：noul、choice、score 以及多问题的 ask 按行执行，一条查询就能给所有工单打分，或在数仓规模上为一整年的邮件分流。支持 TypeSafe、OpenRouter 或任何 /v1/systemone 端点。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · parable-work · `Rs` · `noul` · `choice` · `score` · 调用点 [`src/provider.rs`](https://github.com/parable-work/jev-datafusion/blob/HEAD/src/provider.rs)，2026-11-03 模型阅读</sub>

- **[jev-gmail-ai-spam-filter-and-labeling](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling)** — 自托管的 Gmail AI 邮件分类器，由 Jev 驱动：创建自定义标签、整理收件箱、过滤垃圾邮件。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ilyamk · `JS` · 调用点 [`CODE.gs`](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling/blob/HEAD/CODE.gs)，2026-09-24 阅读</sub>

- **[jev-ids](https://github.com/jev-sec/jev-ids)** — 基于 Jev 的高速、省 token 的入侵检测系统。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jev-ids · `Py` · 调用点 [`jev_ids/detectors/jev.py`](https://github.com/jev-sec/jev-ids/blob/HEAD/jev_ids/detectors/jev.py)，2026-09-24 阅读</sub>

- **[jev-linkmap](https://github.com/stas4000/jev-linkmap)** — 重建网站的内部链接：代码抓取整站，为每个页面挑出 15 个相似页面以及正文中现成可用作锚文本的短语，然后每个页面向 Jev 发一次请求，针对每个目标询问是否应该链接（是非题）以及用哪个短语作锚文本（choice）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · stas4000 · `Py` · `noul` · `choice` · 调用点 [`jev_linkmap/jev.py`](https://github.com/stas4000/jev-linkmap/blob/HEAD/jev_linkmap/jev.py)，2026-11-01 模型阅读</sub>

- **[Jev-Mail](https://github.com/vynnlee/jev-mail)** — 运行在 Google Apps Script 上、由命令行管理的 Gmail 收件箱分类器：对每个会话，Jev 判断它是否需要处理、是否值得加星，以及属于哪个已配置的类别，然后由后台任务打标签、加星或归档。答案模糊的邮件留在收件箱中。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · vynnlee · `TS` · `noul` · `choice` · 调用点 [`src/gas/worker.ts`](https://github.com/vynnlee/jev-mail/blob/HEAD/src/gas/worker.ts)，2026-11-03 模型阅读</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · parth-kp · `Py` · 调用点 [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py)，2026-09-22 阅读</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★10+ · blakestone-x · `Py` · 调用点 [`jev_mcp/client.py`](https://github.com/blakestone-x/jev-mcp/blob/HEAD/jev_mcp/client.py)，2026-09-22 阅读</sub>

- **[jev-poly-crypto-demo](https://github.com/frankda/jev-poly-crypto-demo)** — 面向 Polymarket 五分钟 BTC 涨跌市场的研究工具：实时行情变成 Jev 的类别分数，由独立逻辑做决定，并在看板上展示。仅做模拟交易，从不连接钱包。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · frankda · `TS` · 调用点 [`scripts/check-jev.ts`](https://github.com/frankda/jev-poly-crypto-demo/blob/HEAD/scripts/check-jev.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · kbhuw · `JS` · 调用点 [`dist/server.mjs`](https://github.com/kbhuw/jev-sift/blob/HEAD/dist/server.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-trader](https://github.com/buberlo/jev-trader)** — 模拟盘做市系统：每个 300 毫秒的区块用一次调用向 Jev 提出六个判断——市场状态和方向（choice）、成交流是否有毒、流动性是否偏薄（是非题）、报价环境好坏以及减仓的紧迫程度（score）。由代码执行策略和硬性风控否决。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · buberlo · `Py` · `choice` · `noul` · `score` · 调用点 [`src/jev_trader/judgment/client.py`](https://github.com/buberlo/jev-trader/blob/HEAD/src/jev_trader/judgment/client.py)，2026-10-31 模型阅读 · ⚠ `仅一次提交`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · reachjalil · `TS` · 调用点 [`benchmarks/run.mjs`](https://github.com/reachjalil/jev-tree/blob/HEAD/benchmarks/run.mjs)，2026-09-22 阅读</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — 对一大堆文本（工单、评论、日志）批量回答同一个问题：把多个条目打包进每次请求，并称吞吐量是逐条请求的 32 倍、成本低 41%。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · collapseindex · `Py` · 调用点 [`src/jev_ultralightspeed/_settings.py`](https://github.com/collapseindex/jev-ultralightspeed/blob/HEAD/src/jev_ultralightspeed/_settings.py)，2026-09-24 阅读 · ⚠ `宣称未核实`</sub>

- **[JevBystander](https://github.com/Nisaka520/JevBystander)** — 安卓无障碍版微信判读：只读屏、只弹 3 条 Toast（意图 / 情绪 / 着急 / 建议），不生成回复文案、不发送 · 零第三方依赖，APK 861 KB
  <sub>`开源项目` · ★10+ · nisaka520 · `Kt` · 调用点 [`app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt`](https://github.com/Nisaka520/JevBystander/blob/HEAD/app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt)，2026-09-24 阅读</sub>

- **[jevclip](https://github.com/cclank/jevclip)** — 根据字幕剪辑视频：Jev 逐段阅读约 20 秒的片段并回答五个问题（属于八类内容中的哪一类、信息密度 0–3 分、有无缺乏依据的说法、脱离前文能否看懂、是否切合你的关注点）；由代码取舍、排序，剪出 3 分钟高亮版和去水完整版。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · cclank · `Py` · `choice` · `score` · `noul` · 调用点 [`jevclip/jev.py`](https://github.com/cclank/jevclip/blob/HEAD/jevclip/jev.py)，2026-10-31 模型阅读</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — 用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jkrup · `JS` · 调用点 [`src/client.mjs`](https://github.com/jkrup/jeveryword/blob/HEAD/src/client.mjs)，2026-09-22 阅读</sub>

- **[Jevflake](https://github.com/KranzL/Jevflake)** — dbt 包（附 Terraform 模块），让 Snowflake 就表中的行向 Jev 提问：它配置对 api.typesafe.ai 的外部访问，创建 SQL 函数 jev_noul、jev_choice、jev_score 和 jev_ask，并提供 dbt 宏和测试，使答案只存一次、可复用、可校验。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · KranzL · `Py` · `noul` · `choice` · `score` · 调用点 [`macros/setup/handler.sql`](https://github.com/KranzL/Jevflake/blob/HEAD/macros/setup/handler.sql)，2026-11-02 模型阅读</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ktaletsk · `Py` · 调用点 [`src/jevframe/_engine.py`](https://github.com/ktaletsk/jevframe/blob/HEAD/src/jevframe/_engine.py)，2026-09-22 阅读</sub>

- **[jevintegration for SAP Commerce](https://github.com/emenowicz/jev-sap-commerce)** — SAP Commerce 扩展：Jev 为每条商品评论回答四个 noul（是否辱骂、是否垃圾内容、是否含个人数据、是否与商品相关），只有越过你设定的阈值时代码才批准或拒绝；另用 choice 沿类目树逐层建议类目，并建议分类属性值；拿不准的都留给人处理。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · emenowicz · `Java` · `noul` · `choice` · 调用点 [`jevintegration/src/org/jevintegration/JevClient.java`](https://github.com/emenowicz/jev-sap-commerce/blob/HEAD/jevintegration/src/org/jevintegration/JevClient.java)，2026-11-08 模型阅读</sub>

- **[JevIntent](https://github.com/Nisaka520/JevIntent)** — 微信（FkWeChat 插件）：长按消息分析意图 / 情绪 / 回复姿态，只在本机弹提示，对方无感知
  <sub>`开源项目` · ★10+ · nisaka520 · `Java` · 调用点 [`main.java`](https://github.com/Nisaka520/JevIntent/blob/HEAD/main.java)，2026-09-24 阅读</sub>

- **[Jevline](https://github.com/tsale/jevline)** — 基于安全遥测数据划定事件范围：从一个已确认恶意的进程出发，针对日志所关联的每个进程、账户、主机、地址或域名，询问 Jev 它是否属于同一事件，并逐轮追踪新加入的部分。接近阈值的答案会标记出来交由分析师复核。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tsale · `TS` · `noul` · 调用点 [`engine/src/jev.ts`](https://github.com/tsale/jevline/blob/HEAD/engine/src/jev.ts)，2026-10-31 模型阅读</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · reachjalil · `JS` · 调用点 [`benchmarks/pager/run-jev-v2.mjs`](https://github.com/reachjalil/jevlogs/blob/HEAD/benchmarks/pager/run-jev-v2.mjs)，2026-09-22 阅读</sub>

- **[jevotron](https://github.com/ai4curation/jevotron)** — 命令行字段级异常检测工具，支持 CSV、JSON、文本、SQLite 和 DuckDB：Jev 结合可选的指导说明和示例，为每条记录的每个字段标注 NORMAL 或 ANOMALY，或你自定义的类别，输出按置信度排序的复核队列。SQLite 缓存会复用以往的判断结果。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ai4curation · `Py` · `choice` · 调用点 [`src/jevotron/client.py`](https://github.com/ai4curation/jevotron/blob/HEAD/src/jevotron/client.py)，2026-11-03 模型阅读</sub>

- **[Jevstiller](https://github.com/tomerglick57/Jevstiller)** — 放在重复性 Jev 分类调用前面的代理：起初全部转发给 Jev，用 Jev 自己的答案和概率训练一个本地小模型，等它在留出流量上与 Jev 足够一致后改为本地作答。作者报告 Banking77 上有 61.7% 的消息由本地回答，与 Jev 的一致率为 99.4%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tomerglick57 · `Py` · `choice` · `noul` · 调用点 [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/HEAD/jevstiller/teachers/jev.py)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · 调用点 [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts)，2026-09-23 阅读 · ⚠ `宣称未核实` `作者自荐`</sub>

- **[Laser](https://github.com/iyassr/omarchy-laser)** — 面向 Linux 上 Omarchy 和 Hyprland 的专注模式插件：针对每个屏幕，它询问 Jev 屏幕上的内容是否服务于你声明的任务（一个 noul），以及属于哪类活动（一个 choice）；你走神时，它会从红点、提醒、红色屏幕边缘、遮罩逐步升级到关闭标签页。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · iyassr · `Py` · `noul` · `choice` · 调用点 [`laser/jev.py`](https://github.com/iyassr/omarchy-laser/blob/HEAD/laser/jev.py)，2026-11-07 模型阅读</sub>

- **[laya-opencv](https://github.com/uu889/laya-opencv)** — 面向决策模型的本地工作台和安装包（Windows、Linux）。检测方案把 OpenCV 测量值变成规则检查，再向本地 Laya、TypeSafe 的 Jev 或 aiask.me 提出 Choice、Noul 和 Score 问题；规则与模型不一致或置信度低的结果会标记为待人工复核。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · uu889 · `Py` · `choice` · `noul` · `score` · 调用点 [`app/launcher.py`](https://github.com/uu889/laya-opencv/blob/HEAD/app/launcher.py)，2026-11-05 模型阅读</sub>

- **[lkclean](https://github.com/stefw/lkclean)** — 清理 LinkedIn 信息流的 Chrome 扩展：用 TypeSafe 的 Jev 隐藏流量诱饵、自我推销和跑题的帖子。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · stefw · `TS` · 调用点 [`src/jev.ts`](https://github.com/stefw/lkclean/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — 本地离线的 System One 服务，兼容 Jev API，回答类型化的是非问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · amithgc · `Py` · 调用点 [`src/local_jev/ui/app.js`](https://github.com/amithgc/local-jev/blob/HEAD/src/local_jev/ui/app.js)，2026-09-22 阅读</sub>

- **[Natural Language Logic Interpreter](https://github.com/narphorium/nl-logic-interpreter)** — 用自然英语书写事实和规则的单步逻辑解释器：它像 Prolog 一样用 SLD 归结证明目标，但合一由 Jev 完成：用一个 choice 判断两句话是什么关系，用 noul 判断它们是否陈述同一事实，再用 choice 把每个变量绑定到一个短语上。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · narphorium · `TS` · `choice` · `noul` · 调用点 [`src/server/aiUnifier.ts`](https://github.com/narphorium/nl-logic-interpreter/blob/HEAD/src/server/aiUnifier.ts)，2026-11-08 模型阅读</sub>

- **[OnlyRead](https://github.com/onlyreadai/onlyread)** — 让浏览器里的 AI 智能体在你选定的网站上只能读不能写的 Chrome 扩展：规则、按站点的解码器和判定缓存先处理大部分请求，其余的由 Jev 回答一个 noul（这个请求会不会创建、修改或删除服务器上存储的数据？）；代码据此放行、拦截，或把中间地带交给复核模型。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · onlyreadai · `TS` · `noul` · 调用点 [`extension/src/background/judge/jev.ts`](https://github.com/onlyreadai/onlyread/blob/HEAD/extension/src/background/judge/jev.ts)，2026-11-08 模型阅读 · ⚠ `作者自荐`</sub>

- **[Parallax](https://github.com/zilize/parallax-dsh)** — DeepSeek Harness 插件，用于在本地 SQLite 语料库中查找某个主题的 arXiv 论文：智能体按关键词召回并组合集合，然后由 Jev 用一个 noul 按纳入标准筛选每篇论文（p ≥ 0.5 保留），再用多个 noul 或一个 choice 把论文分到各主题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · zilize · `TS` · `noul` · `choice` · 调用点 [`src/sets/jev.ts`](https://github.com/zilize/parallax-dsh/blob/HEAD/src/sets/jev.ts)，2026-11-06 模型阅读</sub>

- **[patrol-jev](https://github.com/patrol-jev/patrol-jev)** — 面向韩国区政府街道巡查的网页应用：上传照片，生成巡查日志文本或 .hwpx 文件。由 Claude 或 OpenAI 把照片转成文字；Jev 判断它属于日志四个栏目中的哪一个、照片里是否有门牌，以及两张照片是否拍的是同一地点。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · patrol-jev · `TS` · `choice` · `noul` · 调用点 [`src/core/jev.ts`](https://github.com/patrol-jev/patrol-jev/blob/HEAD/src/core/jev.ts)，2026-11-02 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — 用于 Jev 分类决策的 PostgreSQL 扩展（预 alpha）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · giuliosmall · `C` · 调用点 [`sql/typesafe.sql`](https://github.com/giuliosmall/pg_typesafe/blob/HEAD/sql/typesafe.sql)，2026-09-22 阅读</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★10+ · `Py` · `sh` · `choice` · `score` · `noul` · 调用点 [`src/reflex_guard/providers/typesafe.py`](https://github.com/sharziki/semdecide/blob/HEAD/src/reflex_guard/providers/typesafe.py)，2026-09-22 阅读</sub>

- **[sharp](https://github.com/tshmieldev/sharp)** — 用 Jev 或任意 LLM 过滤你的 X.com 信息流。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tshmieldev · `TS` · 调用点 [`src/common/settings.ts`](https://github.com/tshmieldev/sharp/blob/HEAD/src/common/settings.ts)，2026-09-24 阅读</sub>

- **[sift](https://github.com/bohutang/sift)** — Chrome 扩展：给 X 上的每条帖子打标（干货／幽默／闲聊／推广／垃圾／AI 生成）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · bohutang · `JS` · 调用点 [`background.js`](https://github.com/bohutang/sift/blob/HEAD/background.js)，2026-09-22 阅读</sub>

- **[Slop Filter](https://github.com/adamnroman/slop-filter)** — Chrome 和 Firefox 扩展，隐藏 X、LinkedIn、Reddit 和 YouTube 上由 AI 写成的帖子和评论：Jev 针对每段文字的写法回答 30 个细分的是非题，代码统计标点和套话词汇，再用根据你自己的标注拟合的权重合成一个分数。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · adamnroman · `JS` · `noul` · 调用点 [`src/jev-client.js`](https://github.com/adamnroman/slop-filter/blob/HEAD/src/jev-client.js)，2026-11-01 模型阅读</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — 一个 Chrome 扩展，逐个询问 DOM 元素是不是广告。
  <sub>`开源项目` · ★10+ · realzachi · `JS` · 调用点 [`src/typesafe.js`](https://github.com/realZachi/typesafe-adblock/blob/HEAD/src/typesafe.js)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[VerdictAD](https://github.com/sgstq0811/VerdictAD-Jev-AD)** — 免训练的少样本工业异常检测：开源的 Jev 风格模型 Clef-Flash 9B 以 noul 问题判断查询图及其局部窗口相对少量正常参考图是否有缺陷，再用这些概率重新加权现有检测器的图像分数和异常图，在 MVTec AD、VisA 和 MVTec LOCO AD 上评测。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · sgstq0811 · `Py` · `noul` · 引用文件 [`verdictad/decider.py`](https://github.com/sgstq0811/VerdictAD-Jev-AD/blob/HEAD/verdictad/decider.py)，2026-11-05 模型阅读 · ⚠ `并非 Jev 本身` `疑似 AI 生成` `作者自荐`</sub>

- **[vibecheck](https://github.com/jlowin/vibecheck)** — 把 System One 调用变成普通 Python 值的库：check（是/否）、classify（选一个）、label（选出所有适用项）和 score，支持阈值、“不确定”回答，以及把针对同一数据的多个问题合并成一批。可对接 TypeSafe 或任何兼容服务器。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · jlowin · `Py` · `noul` · 调用点 [`src/vibecheck/backends.py`](https://github.com/jlowin/vibecheck/blob/HEAD/src/vibecheck/backends.py)，2026-10-24 模型阅读 · ⚠ `无许可证`</sub>

- **[wechat-jev-assistant](https://github.com/yushen100/wechat-jev-assistant)** — Windows 微信对话分析助手：本地读取、脱敏、TypeSafe Jev 判断与加密历史
  <sub>`开源项目` · ★10+ · yushen100 · `Py` · 调用点 [`src/wechat_jev/typesafe_client.py`](https://github.com/yushen100/wechat-jev-assistant/blob/HEAD/src/wechat_jev/typesafe_client.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome 扩展：给你在 X 上滑过的每条帖子打上类型化 Jev 判断与实时评分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · oso95 · `TS` · 调用点 [`src/shared/jev.ts`](https://github.com/oso95/x-scanner/blob/HEAD/src/shared/jev.ts)，2026-09-22 阅读</sub>

- **[xscout](https://github.com/ethan-ab/xscout-jev)** — 按一份个人配置监视 X 上重要的动态：Jev 对每条帖子判断话题和发帖人、检查排除条件、为重要性和相关性打分并选出适用的行动，再由确定性规则结合热度，把“重大”“趋势”或“值得注意”的提醒连同起草提示词发到 Slack。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ethan-ab · `TS` · `choice` · `noul` · `score` · 调用点 [`src/jev.ts`](https://github.com/ethan-ab/xscout-jev/blob/HEAD/src/jev.ts)，2026-11-04 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[弦外之音 JevGuide](https://github.com/nisaka520/jevguide)** — 面向微信的 Android 无障碍应用：读取屏幕上的聊天内容，在一次请求中向 Jev 提出八个问题——对方的意图、情绪和着急程度，是否需要回复、回复是否有风险，该怎么做，适合哪种回复风格，以及关系进展（攻略度）评分。随后由聊天模型起草三条回复。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · nisaka520 · `Kt` · `choice` · `score` · `noul` · 调用点 [`app/src/main/java/io/github/nisaka520/jevguide/Prompt.kt`](https://github.com/nisaka520/jevguide/blob/HEAD/app/src/main/java/io/github/nisaka520/jevguide/Prompt.kt)，2026-10-31 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[言外 Yanwai](https://github.com/yirc99/yanwai)** — Android 上的微信 LSPosed/Xposed 模块：针对一条聊天消息及其前文，分两轮用 `choice` 问题向 Jev 询问发送者的情绪（十个选项）、聊天场景以及对话在等待怎样的回应；随后由 LLM 起草回复或新话题。它从不自动发送消息。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · yirc99 · `Kt` · `choice` · 调用点 [`app/src/main/java/dev/jev/wechatmood/analysis/JevProtocol.kt`](https://github.com/yirc99/yanwai/blob/HEAD/app/src/main/java/dev/jev/wechatmood/analysis/JevProtocol.kt)，2026-10-30 模型阅读 · ⚠ `无许可证` `需第三方密钥`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · abhishekswe · `TS` · 调用点 [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts)，2026-09-22 阅读</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · carlosedm10 · `Py` · 调用点 [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[ComfyUI System One](https://github.com/dante01yoon/ComfyUI-SystemOne)** — ComfyUI 自定义节点：根据类型化判断为工作流分支，比如提示词想要哪种风格、是否对儿童过于血腥、是否提到了真实人物；用一个下拉框就能在 Jev、Laya 和 Cloudflare 的 Clef 之间切换后端。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · dante01yoon · `Py` · `choice` · `noul` · `score` · 调用点 [`systemone/backends.py`](https://github.com/dante01yoon/ComfyUI-SystemOne/blob/HEAD/systemone/backends.py)，2026-11-11 模型阅读</sub>

- **[Decision Lab](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases)** — 一个包含五十个金融演示的网站：就账本、订单、欺诈、钱包、交易和申报文件，把同样的类型化 choice、score 和 noul 发给 Jev，用已知数据给答案打分，并在日 K 线上回测 Jev 的交易决策；录制好的答案无需密钥即可重放。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · IslamBaraka90 · `JS` · `choice` · `noul` · `score` · 调用点 [`src/services/demo-runner.js`](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases/blob/HEAD/src/services/demo-runner.js)，2026-11-10 模型阅读</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — 用 Jev 按主题、情绪与歌词复杂度给一位艺人的全部作品分类，并可视化呈现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lirantal · `JS` · 调用点 [`src/jev.ts`](https://github.com/lirantal/discoprint/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[dsh-fact-check](https://github.com/7starsseeker/dsh-fact-check)** — DeepSeek Harness 的事实核查技能，其中可选的 Jev 层提出事实性 noul，比如证据是否支持某条论断、是否已足够停止搜索、来源是否为一手来源；Jev 只能下调论断的可信等级，不能上调。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · 7starsseeker · `JS` · `noul` · 调用点 [`tools/jev-verdict.mjs`](https://github.com/7starsseeker/dsh-fact-check/blob/HEAD/tools/jev-verdict.mjs)，2026-11-11 模型阅读</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nanami-0713 · `JS` · 调用点 [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[DuckDB Dual Cognition](https://github.com/prasanthj/duckdb-dual-cognition)** — 原生 DuckDB 扩展：用 SQL 函数批量对每一行问 Jev choice、score 和 noul，包括从候选里为一行挑出外键，或答 ambiguous、no_match；只有置信度低于阈值的行才交给 OpenAI 模型去推理。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · prasanthj · `C++` · `choice` · `score` · `noul` · 调用点 [`src/dc_extension.cpp`](https://github.com/prasanthj/duckdb-dual-cognition/blob/HEAD/src/dc_extension.cpp)，2026-11-11 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[DuoMind](https://github.com/j1s4nn/duomind)** — 一个 OpenAI 兼容的本地服务器，把 llama.cpp 上的小模型与 Jev 搭配：在生成之前、之中和之后共 18 个决策点（是否需要推理、是否安全、输出格式、是否该停、是否重试）引导本地模型。提示词会发送给 TypeSafe，生成过程留在本地。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · j1s4nn · `Py` · `noul` · `choice` · 调用点 [`src/duomind/jev_client.py`](https://github.com/j1s4nn/duomind/blob/HEAD/src/duomind/jev_client.py)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[Eikos Arena](https://github.com/caiovicentino/eikos-arena)** — 作者的开源模型 Eikos-27B 与 Jev 在 14 个 Hyperliquid 永续合约上的模拟交易对局：每 5 分钟两者拿到同一份行情快照和 28 个问题（每个市场一个做多、观望或做空的 choice，以及一个是否会上涨的 noul），按账户价值和 Brier 分数计分。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · caiovicentino · `Py` · `choice` · `noul` · 调用点 [`arena/arena.py`](https://github.com/caiovicentino/eikos-arena/blob/HEAD/arena/arena.py)，2026-11-08 模型阅读</sub>

- **[ElBruno.AI.Decisions](https://github.com/elbruno/ElBruno.AI.Decisions)** — NuGet 上的统一 .NET API，用于分类、路由、按评分标准打分和命题判断，返回概率分布；其中一个包原生调用 Jev 的 POST /v1/systemone，另有调用微软 Foundry 决策模型和通过 Ollama 调用本地模型的包。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · elbruno · `C#` · `choice` · `score` · `noul` · 调用点 [`src/ElBruno.AI.Decisions.Jev/JevClient.cs`](https://github.com/elbruno/ElBruno.AI.Decisions/blob/HEAD/src/ElBruno.AI.Decisions.Jev/JevClient.cs)，2026-11-11 模型阅读</sub>

- **[Evaluating and Benchmarking the System One Model Jev](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking)** — 一篇 arXiv 论文的代码：在 37 个公开数据集上以 choice、noul 和 score 零样本测试 Jev，并用同样的请求给两个开源权重大模型打分作对比；另有一个序列决策部分，让 Jev 在 ALFWorld、TextWorld、FrozenLake 等五个环境里每步选一个动作。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · AppliedMachineLearning-Lab · `Py` · `choice` · `noul` · `score` · 调用点 [`jev_benchmarking/runner.py`](https://github.com/AppliedMachineLearning-Lab/jev-benchmarking/blob/HEAD/jev_benchmarking/runner.py)，2026-11-10 模型阅读</sub>

- **[ex-regex](https://github.com/nothans/ex-regex)** — 形似 re 模块的 Python 库，其查找、替换、切分、过滤和提取都按语义判断每个匹配：由 Jev 判断输入里的候选片段，所以每个匹配都是带偏移量的原文切片，绝不会编造文本。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · nothans · `Py` · `noul` · `choice` · `score` · 调用点 [`src/exregex/backends.py`](https://github.com/nothans/ex-regex/blob/HEAD/src/exregex/backends.py)，2026-11-11 模型阅读</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · kalyanm45 · `Py` · 调用点 [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

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

- **[Jev Persian Benchmark](https://github.com/armanjr/jev-persian-benchmark)** — 在 480 道自编通用波斯语题、560 道文学题和一个古典诗歌试点上，把 Jev 与开源决策模型对比的基准：以 choice、noul 和 score 提问，保存原始响应并在本地评分；Jev 在 choice 和 noul 准确率上领先。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · armanjr · `Py` · `choice` · `noul` · `score` · 调用点 [`jev_benchmark/runner.py`](https://github.com/armanjr/jev-persian-benchmark/blob/HEAD/jev_benchmark/runner.py)，2026-11-11 模型阅读 · ⚠ `无许可证`</sub>

- **[Jev Playwright](https://github.com/arthurfiorette/jev-playwright)** — 一个 Playwright 报告器：在启动任何浏览器之前，询问 Jev 某次代码改动可能影响哪些现有端到端测试，并跳过明显无关的测试。默认会发送改动路径、补丁和测试代码；README 提醒它可能漏掉受影响的测试。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arthurfiorette · `TS` · 调用点 [`src/config.ts`](https://github.com/arthurfiorette/jev-playwright/blob/HEAD/src/config.ts)，2026-10-24 模型阅读</sub>

- **[Jev vs. the right baselines](https://github.com/ickma2311/jev-baselines-eval)** — 两项预注册的独立研究：Jev 以 choice 在 CLINC150 和 Banking77 上分类客户意图，作为升级级联的关卡，与小型和前沿大模型以及有监督编码器对比；第二项研究检验在提示注入下，Jev 的置信度能否区分被劫持的决策和抵抗住的决策。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ickma2311 · `Py` · `choice` · `noul` · 调用点 [`code/common.py`](https://github.com/ickma2311/jev-baselines-eval/blob/HEAD/code/common.py)，2026-11-10 模型阅读</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · yuyang2230 · `Py` · 调用点 [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py)，2026-09-22 阅读</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — TypeSafe AI Jev 在智能体工具调用风险分类上的可复现基准：准确率、延迟，以及其置信度是否可信。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · themsquared · `Py` · 调用点 [`bench.py`](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py)，2026-09-24 阅读</sub>

- **[jev-chess](https://github.com/hemanth/jev-chess)** — 用 Jev 做国际象棋的着法、局面评估、人格对手与棋局分类。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hemanth · `TS` · 调用点 [`src/typeSafeClient.ts`](https://github.com/hemanth/jev-chess/blob/HEAD/src/typeSafeClient.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-clean](https://github.com/Kunyanli230/jev-clean)** — 以决策为先的数据清洗系统，由 Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kunyanli230 · `Py` · 调用点 [`src/idac/typesafe_client.py`](https://github.com/Kunyanli230/jev-clean/blob/HEAD/src/idac/typesafe_client.py)，2026-09-24 阅读</sub>

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

- **[jev-guard](https://github.com/klauswg/jev-guard)** — 面向交易所充值与提现的实时风险分诊网关——Jev（TypeSafe System One）只负责分诊，裁决另有机制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · klauswg · `Java` · 调用点 [`src/main/java/com/jevguard/eval/EvalRunner.java`](https://github.com/klauswg/jev-guard/blob/HEAD/src/main/java/com/jevguard/eval/EvalRunner.java)，2026-09-24 阅读</sub>

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

- **[jev-oncall](https://github.com/mingleiw/jev-oncall)** — 值班工具：Jev 分诊每条生产告警（用 noul 判断是否需要处理，给出严重度 score，用 choice 选团队和重复项）；在根因分析基准里，由 Jev 选择下一项诊断检查和证据支持的假设，由代码控制预算。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · mingleiw · `Py` · `noul` · `score` · `choice` · 调用点 [`triage.py`](https://github.com/mingleiw/jev-oncall/blob/HEAD/triage.py)，2026-11-10 模型阅读</sub>

- **[jev-organize](https://github.com/nexibeo/jev-organize)** — 把一堆公司文件扔进去，就能按部门、类型、敏感度、日期、交易方等分类整理好。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nexibeo · `JS` · 调用点 [`skills/jev-organize/scripts/src/jev.mjs`](https://github.com/nexibeo/jev-organize/blob/HEAD/skills/jev-organize/scripts/src/jev.mjs)，2026-09-24 阅读</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev 增强的 Playwright MCP 代理：页面状态分拣与提示注入防护。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · krw82 · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/krw82/jev-playwright-mcp/blob/HEAD/src/jev/client.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-pr-labeler](https://github.com/1jehuang/jev-pr-labeler)** — 用 Jev 的类型化决策给 GitHub PR 打语义标签，依据概念范围而不是改动行数。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 1jehuang · `Py` · 调用点 [`jev_labeler/classifier.py`](https://github.com/1jehuang/jev-pr-labeler/blob/HEAD/jev_labeler/classifier.py)，2026-09-24 阅读</sub>

- **[jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline)** — 针对长期问题的每日研究监控：确定性的 Python 掌控流程，TypeSafe Jev 按问题筛选信息源，Qwen 撰写笔记（试点）。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shimo4228 · `Py` · 调用点 [`src/jev_research_pipeline/jev/core.py`](https://github.com/shimo4228/jev-research-pipeline/blob/HEAD/src/jev_research_pipeline/jev/core.py)，2026-09-24 阅读</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 面向 WebFlux 的 Spring Boot Starter：标注了 @SemanticCircuitBreaker 的方法会把每个响应体发给 Jev，用一个 noul 判断这个 HTTP 200 是否掩盖了错误、堆栈信息或维护通知；超过阈值（示例中为 0.85）就抛出熔断器可以计数的异常。失败即放行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
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

- **[jevcut](https://github.com/VBS2004/jevcut)** — 把长视频剪成排好序的短片：代码列出片段所有可能的起止位置，Jev 只评判每个候选边界会剪出的片段，用 noul 判断它是否从半句话开始或结束、能否独立成立、是不是广告，用 choice 在候选之间挑选，用 score 评估开头抓不抓人。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · VBS2004 · `Py` · `noul` · `choice` · `score` · 调用点 [`src/jevcut/backends.py`](https://github.com/VBS2004/jevcut/blob/HEAD/src/jevcut/backends.py)，2026-11-09 模型阅读</sub>

- **[JevEye](https://github.com/Adityakhalkar/JevEye)** — 向 Jev 询问一张图片：CNN 报告它看到了什么（带校准置信度或选择弃权），再由 Jev 判断这意味着什么。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · adityakhalkar · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/Adityakhalkar/JevEye/blob/HEAD/src/lib/jev.ts)，2026-09-24 阅读</sub>

- **[jevgate](https://github.com/gordonbrander/jevgate)** — 用于 shell 管道的命令行关卡：它从标准输入读取文本，就文本问 Jev 一个 noul，比如它是否在报告故障；P(yes) 超过阈值时，文本像 grep 匹配一样原样输出，或者运行 -- 之后的命令，否则什么也不输出。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · gordonbrander · `Rs` · `noul` · 调用点 [`src/provider.rs`](https://github.com/gordonbrander/jevgate/blob/HEAD/src/provider.rs)，2026-11-08 模型阅读</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — 面向社区和应用的内容审核，由 Jev（TypeSafe）驱动：按类别给出概率，阈值由你掌控。支持 Discord。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ohernandezdev · `Py` · 调用点 [`jevmod/judge.py`](https://github.com/ohernandezdev/jevmod/blob/HEAD/jevmod/judge.py)，2026-09-24 阅读</sub>

- **[JEVsnap](https://github.com/brainstormity/jevsnap)** — 适用于 macOS、Linux 和 Windows 的截图热键：图片进入剪贴板前先涂黑密钥和个人信息；本地规则之后，Jev 用 noul 判断哪些 OCR 文本行和单词要隐藏，可选的视觉检查再用 box 问题找出剩下的部分。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · brainstormity · `TS` · `noul` · `choice` · 调用点 [`desktop/src/core/jevClient.ts`](https://github.com/brainstormity/jevsnap/blob/HEAD/desktop/src/core/jevClient.ts)，2026-11-10 模型阅读 · ⚠ `仅一次提交`</sub>

- **[JevT++](https://github.com/wiatrM/jevtpp)** — 一个 C++20 库，通过编译期模式把运行时的文本、JSON 或对象转换为枚举、布尔值和分数，提供完整概率分布并支持显式弃权。可在进程内运行本地 Laya 模型（ONNX Runtime 或 ggml），也可通过可选的远程后端调用 Jev；附带延迟指标和马里奥游戏演示。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · wiatrm · `C++` · 调用点 [`include/jevt/remote.hpp`](https://github.com/wiatrM/jevtpp/blob/HEAD/include/jevt/remote.hpp)，2026-10-24 模型阅读</sub>

- **[jevticktrouter](https://github.com/GhrezaKh74/JevTicktRouter)** — 用 .NET 10 与 React 19 做的快速结构化工单分拣。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ghrezakh74 · `C#` · 调用点 [`backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs`](https://github.com/GhrezaKh74/JevTicktRouter/blob/HEAD/backend/JevTicketRouter.Application/Jev/Contracts/JevSystemOneRequest.cs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevtriage](https://github.com/sathariels/jevtriage)** — GitHub Action 与 CLI：用 TypeSafe Jev 为 PR 分诊（可以合并 / 需要审查 / 有风险），并带置信度关卡。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · sathariels · `Py` · 调用点 [`src/jevtriage/client.py`](https://github.com/sathariels/jevtriage/blob/HEAD/src/jevtriage/client.py)，2026-09-24 阅读</sub>

- **[JevX](https://github.com/vij-sameerb5/JevX)** — CLI 加 MCP 服务器：在代码库里找出其实是判断题的硬编码规则，并对每个候选问 Jev：用 noul 判断它是否需要判断力、结果是否有限、是否仍应保留为精确代码，再用 choice 选出原语和类别；把匹配度高的改写掉，旧规则保留作后备。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · vij-sameerb5 · `TS` · `noul` · `choice` · 调用点 [`packages/typesafe/src/decision.ts`](https://github.com/vij-sameerb5/JevX/blob/HEAD/packages/typesafe/src/decision.ts)，2026-11-10 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[jlink](https://github.com/keltokhy/jlink)** — 给经济学家用的记录链接：用自然语言写匹配规则，对每一对记录得到一个概率，可审计、可引用。支持 Python、CLI、Stata 和 R。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · keltokhy · `Py` · 调用点 [`bench/local_models.py`](https://github.com/keltokhy/jlink/blob/HEAD/bench/local_models.py)，2026-09-24 阅读</sub>

- **[metis](https://github.com/Ayush0054/metis)** — Metis：由 Jev 驱动的 GitHub issue 自动分拣，可复用的 GitHub Action。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ayush0054 · `Py` · 调用点 [`src/metis_workflow/integrations/jev.py`](https://github.com/Ayush0054/metis/blob/HEAD/src/metis_workflow/integrations/jev.py)，2026-11-05 模型阅读</sub>

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

- **[Qualixar Jev Decision Layer](https://github.com/qualixar/jev-decision-layer)** — 插件加本地 MCP 服务器：让智能体每次把一个封闭问题交给 Jev，比如该用哪个工具、技能或格式，草稿是否符合要求，请求该归哪个团队，共 55 个配方；本地策略关卡检查每个类型化答案并记录凭据。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · qualixar · `Py` · `choice` · `score` · `noul` · 调用点 [`plugins/qualixar-jev-decision-layer/runtime/jev_auto/providers.py`](https://github.com/qualixar/jev-decision-layer/blob/HEAD/plugins/qualixar-jev-decision-layer/runtime/jev_auto/providers.py)，2026-11-10 模型阅读</sub>

- **[Social Risk · Qwen3-VL + Jev](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev)** — 关于中文图文表情包中厌女内容的研究项目：经过 LoRA 微调的 Qwen3-VL 把每条内容转成结构化证据，Jev 按固定政策回答一个 noul，判断内容是否攻击或贬低女性；代码再把概率分成风险等级。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · TianJinWeiBoss520 · `Py` · `noul` · 调用点 [`experiments/v1/src/run_ltedi_jev_cloud20.py`](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev/blob/HEAD/experiments/v1/src/run_ltedi_jev_cloud20.py)，2026-11-10 模型阅读</sub>

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

- **[undertone](https://github.com/nuu-maan/undertone)** — 在你打字时读出消息语气的文本框：一次 Jev 请求用 choice 判断整体语气，用 noul 判断是否阴阳怪气、讽刺、过度道歉、咄咄逼人，以及能否发给上司，再用 score 评估紧迫程度和正式程度；代码把这些答案变成结论和修改提示。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · nuu-maan · `TS` · `choice` · `noul` · `score` · 调用点 [`src/lib/jev/questions.ts`](https://github.com/nuu-maan/undertone/blob/HEAD/src/lib/jev/questions.ts)，2026-11-09 模型阅读 · ⚠ `无许可证`</sub>

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
