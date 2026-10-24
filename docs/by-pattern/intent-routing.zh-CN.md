# 意图路由

<sub>[awesome-jev](../../README.zh-CN.md) · [English](intent-routing.md)</sub>

_判断用户意图，把请求分流到正确的分支。_

这个决策的全部已收录例子 —— 共 38 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#意图路由)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=intent-routing&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#intent-routing)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#intent-routing)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 3 · 调用点 27 · 接口形态 0 · 仅示例 0 · 独立报告 2 · 负面结果 0 · 未引用文件 11。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home) <sub>`官方文档` · `Py`</sub>
- [Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) <sub>`官方文档` · `Py`</sub>
- [Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing) <sub>`官方文档` · `Py` · `choice`</sub>

## 本仓库的示例

本仓库 [`examples/`](../../examples/) 里归在这个模式下的代码。每一条在下文也都列出，附有摘要；[示例的 README](../../examples/README.md) 说明了它们核验到了哪一步。 <sub>(机翻)</sub>

- [Example: confidence-gated escalation](../../examples/02-confidence-gate/main.py) <sub>`代码片段` · `Py` · `choice` · ⚠ `代码未实测`</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。
  <sub>`平台集成` · ★10k+ · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · 调用点 [`apps/web/utils/decision-model/typesafe.ts`](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/typesafe.ts)，2026-09-22 阅读</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★1k+ · `Java` · `choice` · `score` · `noul` · 调用点 [`app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-09-22 阅读</sub>

- **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)** — 带对照组的教学示例：同一个问询台任务，一份是只认 Y/N 的纯 Python 写法，旁边是一个能读出意图的 Noul。
  <sub>`教程` · ★1k+ · Real Python · `Py` · `noul` · 调用点 [`hello-jev/jev_noul.py`](https://github.com/realpython/materials/blob/HEAD/hello-jev/jev_noul.py)，2026-09-22 阅读</sub>

- **[shapeshift](https://github.com/anishfn/shapeshift)** — 一个能变成你想要的样子的输入框：边输入边变形为合适的界面，由 TypeSafe Jev 驱动，可离线使用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · anishfn · `TS` · 调用点 [`src/lib/jev/client.ts`](https://github.com/anishfn/shapeshift/blob/HEAD/src/lib/jev/client.ts)，2026-09-24 阅读</sub>

- **[foreman](https://github.com/thruwire/foreman)** — 一个「软件工厂工头」，用 Jev 决定智能体流水线下一步该做什么。
  <sub>`开源项目` · ★100+ · thruwire · `Py` · 调用点 [`src/foreman/foreman/jev.py`](https://github.com/thruwire/foreman/blob/HEAD/src/foreman/foreman/jev.py)，2026-09-22 阅读</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · 调用点 [`scripts/jev.js`](https://github.com/kevinbadi/hyperedit/blob/HEAD/scripts/jev.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · 调用点 [`apps/server/src/jev/client.ts`](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts)，2026-09-22 阅读</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · 调用点 [`src/lib/typesafe.ts`](https://github.com/superagents-lab/jev-search/blob/HEAD/src/lib/typesafe.ts)，2026-09-22 阅读</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — 只读的 Instagram、TikTok 与 LinkedIn 调研：Jev 先路由平台，再从最新浏览器证据中选择受限的 socai CLI 动作；代码校验目标并保留来源链接。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · socai-io · `JS` · `choice` · 调用点 [`src/actions.js`](https://github.com/socai-io/jev-social/blob/HEAD/src/actions.js)，2026-09-23 阅读 · ⚠ `需第三方密钥`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/jev.js`](https://github.com/moritzkremb/jev-voice-browser/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[mu](https://github.com/qybaihe/mu)** — 基于 pi 的编程 Agent（命令行和桌面端），在 38 个决策点上问 Jev：工具输出的哪些片段进上下文、哪些过期的工具结果可以丢掉、被规则拦下的命令是不是用户要的、抓取的网页和 MCP 输出里有没有注入的指令。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · 调用点 [`packages/kyrn-judge/src/providers/typesafe.ts`](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts) · ⚠ `作者自荐`</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — 本地优先的 AI 任务中枢：把邮件、Teams、Slack 与报表汇成一条时间线。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · ldbumble · `Py` · 调用点 [`taskuary/jev.py`](https://github.com/ldbumble/taskuary/blob/HEAD/taskuary/jev.py)，2026-09-22 阅读</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把关于家的类型化答案变成传感器，提供可用于自动化的 noul、choice 和 score 动作，以及一个对话代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · 调用点 [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py)，2026-09-30 阅读 · ⚠ `疑似 AI 生成` `作者自荐`</sub>

- **[hono-jev-router](https://github.com/yusukebe/hono-jev-router)** — 按语义路由 HTTP 请求 —— 给 Web 框架做的语义路由器。
  <sub>`开源项目` · ★10+ · yusukebe · `TS` · 调用点 [`src/index.ts`](https://github.com/yusukebe/hono-jev-router/blob/HEAD/src/index.ts)，2026-09-22 阅读</sub>

- **[jev-ai-sdk-form-router](https://github.com/vercel-labs/jev-ai-sdk-form-router)** — 用 Jev 和 AI SDK 把表单提交路由给合适的负责人。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · vercel-labs · `TS` · 调用点 [`components/routing-result.tsx`](https://github.com/vercel-labs/jev-ai-sdk-form-router/blob/HEAD/components/routing-result.tsx)，2026-09-24 阅读</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · parth-kp · `Py` · 调用点 [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py)，2026-09-22 阅读</sub>

- **[jevcache](https://github.com/kushals256/jevcache)** — 当 TypeSafe Jev 判断意图相同时，跳过昂贵的 LLM 调用。一个兼容 OpenAI 的本地缓存代理。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kushals256 · `TS` · 调用点 [`scripts/eval.ts`](https://github.com/kushals256/jevcache/blob/HEAD/scripts/eval.ts)，2026-09-24 阅读</sub>

- **[jevyoumean](https://github.com/syumai/jevyoumean)** — 给任意 CLI 的语义化「你是不是想输入」：用 Jev 匹配子命令。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · syumai · `Go` · 调用点 [`internal/jev/client.go`](https://github.com/syumai/jevyoumean/blob/HEAD/internal/jev/client.go)，2026-09-22 阅读</sub>

- **[typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow)** — 一个小型异步 LangGraph 工作流：把模拟邮件交给 Jev 做带类型的 Choice（发票或一般邮件），再路由到演示处理器。分类会真实调用 API；处理器只设置去向。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · giesn · `Py` · 调用点 [`src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py`](https://github.com/GiesN/typesafe-jev-workflow/blob/HEAD/src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。
  <sub>`代码片段` · `Py` · `choice` · 调用点 [`examples/02-confidence-gate/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/02-confidence-gate/main.py)，2026-09-22 阅读 · ⚠ `代码未实测`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。
  <sub>`教程` · Mehul Gupta · `Py` · `choice` · ⚠ `付费墙`</sub>

- **[Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/)** — 在 Netlify function 里零配置调用：直接用官方 SDK，不需要 API key、baseURL 或 provider 配置，按 Netlify credits 计费。
  <sub>`平台集成` · `TS` · `choice`</sub>

- **[jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval)** — 第三方在相同条件下对比 Jev 与两款 LLM：为面向日本游客的摄影服务路由预订咨询，共六十条四种语言的合成消息。 <sub>(机翻)</sub>
  <sub>`基准测试` · shogo-nfrealmusic · `TS` · 调用点 [`src/jev.ts`](https://github.com/Shogo-nfrealmusic/jev-eval/blob/HEAD/src/jev.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-inbox-queue](https://github.com/tusharck/jev-inbox-queue)** — 用 Jev（TypeSafe System One）把收件箱变成一个简短的行动队列。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tusharck · `Py` · 调用点 [`inbox_queue/classify.py`](https://github.com/tusharck/jev-inbox-queue/blob/HEAD/inbox_queue/classify.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — 在 2000 封钓鱼邮件上对比 Jev 与一个轻量 LLM：准确率、校准度、延迟、成本。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · anisselbd · `Py` · 调用点 [`run_jev.py`](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/run_jev.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[JevT++](https://github.com/wiatrM/jevtpp)** — 一个 C++20 库，通过编译期模式把运行时的文本、JSON 或对象转换为枚举、布尔值和分数，提供完整概率分布并支持显式弃权。可在进程内运行本地 Laya 模型（ONNX Runtime 或 ggml），也可通过可选的远程后端调用 Jev；附带延迟指标和马里奥游戏演示。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · wiatrm · `C++` · 调用点 [`include/jevt/remote.hpp`](https://github.com/wiatrM/jevtpp/blob/HEAD/include/jevt/remote.hpp)，2026-10-24 模型阅读</sub>

- **[lanebreak](https://github.com/ndolinschi/lanebreak)** — LaneBreak：工单优先级与路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/lanebreak/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul` · ⚠ `需早期访问`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。
  <sub>`教程` · `TS` · `noul` · `choice` · `score`</sub>

- **[Jev router: how model routing works, and 16 routers compared](https://madewithjev.com/jev-router)** — 讲解用 Jev 在花钱之前判断下一轮该用哪个模型、工具或 skill 的路由器，说明先降级再升级为什么可能比不路由更贵，并对比了 16 个面向 Claude Code、Codex 和 OpenRouter 的路由器。 <sub>(机翻)</sub>
  <sub>`文章` · Jon Kraayenbrink · ⚠ `作者自荐`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
