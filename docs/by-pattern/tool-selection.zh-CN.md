# 工具选择

<sub>[awesome-jev](../../README.zh-CN.md) · [English](tool-selection.md)</sub>

_智能体下一步该调用哪个工具或动作。_

这个决策的全部已收录例子 —— 共 236 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#工具选择)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#tool-selection)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#tool-selection)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 3 · 调用点 228 · 接口形态 4 · 仅示例 0 · 独立报告 11 · 负面结果 1 · 未引用文件 4。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling) <sub>`官方文档` · `Py` · `choice`</sub>
- [Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) <sub>`官方文档` · `Py` · `choice` · `noul`</sub>
- [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home) <sub>`官方文档` · `Py`</sub>

## 本仓库的示例

本仓库 [`examples/`](../../examples/) 里归在这个模式下的代码。每一条在下文也都列出，附有摘要；[示例的 README](../../examples/README.md) 说明了它们核验到了哪一步。 <sub>(机翻)</sub>

- [Example: speculative fan-out](../../examples/03-fan-out/main.py) <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>
- [Example: tool selection with a none option](../../examples/04-tool-selection/main.py) <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐ — 把自然语言的交易请求映射到普通的类型化函数：函数名和有限取值的参数各自变成一个带置信度的问题。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐ — 为智能体的一轮对话从 182 个技能里最多挑一个：第一次请求给所有技能排序并顺便问「这轮到底需不需要技能」，第二次细读前三名。
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。
  <sub>`官方文档` · `Py`</sub>

- **[ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)** — 教学用的模拟交易与回测应用：每个“投资者人格”智能体把一份财务快照变成看涨、看跌或中性信号。选 TypeSafe 作为模型提供方时，每个智能体发一次 Jev 请求：用 choice 选方向，再用五级 score 分别评估看涨和看跌理由的强度，换算成与 LLM 智能体相同的 JSON。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · ★10k+ · virattt · `Py` · 调用点 [`hedge_fund/llm/client.py`](https://github.com/virattt/ai-hedge-fund/blob/HEAD/hedge_fund/llm/client.py)，2026-09-24 阅读</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · 调用点 [`scripts/jev-spike.mjs`](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs)，2026-09-22 阅读</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。
  <sub>`开源项目` · ★10k+ · `Py` · `choice` · 调用点 [`python/providers/typesafe/composio_typesafe/provider.py`](https://github.com/ComposioHQ/composio/blob/HEAD/python/providers/typesafe/composio_typesafe/provider.py)，2026-09-22 阅读</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)** — Python 与 TypeScript 双实现的 computer-use 动作选择：Jev 从不可变候选集里挑下一个浏览器动作，保留 reobserve 和 abstain 两个特殊选项。
  <sub>`开源项目` · ★10k+ · `Py` · `TS` · `choice` · 调用点 [`libs/cua-driver/examples/jev-use/python/jev_adapter.py`](https://github.com/trycua/cua/blob/HEAD/libs/cua-driver/examples/jev-use/python/jev_adapter.py)，2026-09-22 阅读</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。
  <sub>`开源项目` · ★10k+ · `Py` · `choice` · `noul` · 调用点 [`fastmcp_slim/fastmcp/experimental/transforms/jev_search.py`](https://github.com/PrefectHQ/fastmcp/blob/HEAD/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)，2026-09-22 阅读</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。
  <sub>`开源项目` · ★10k+ · Browser Use · `Py` · `choice` · 调用点 [`jev_ultrafast/model.py`](https://github.com/browser-use/jev-ultrafast/blob/HEAD/jev_ultrafast/model.py)，2026-09-22 阅读 · ⚠ `厂商自报数据`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★10k+ · Vercel Labs · `TS` · `choice` · 调用点 [`apps/web/lib/jev/compose.ts`](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts)，2026-09-22 阅读</sub>

- **[agent-desktop](https://github.com/lahfir/agent-desktop)** — 桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。
  <sub>`开源项目` · ★1k+ · `Rs` · `choice` · `noul` · 调用点 [`scripts/jev/policy.mjs`](https://github.com/lahfir/agent-desktop/blob/HEAD/scripts/jev/policy.mjs)，2026-09-24 阅读</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。
  <sub>`开源项目` · ★1k+ · `TS` · `choice` · `noul` · 调用点 [`src/shared/jevProtocol.ts`](https://github.com/ThinkInAIXYZ/deepchat/blob/HEAD/src/shared/jevProtocol.ts)，2026-09-22 阅读</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★1k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`jevkit/client.py`](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py)，2026-09-22 阅读 · ⚠ `实测后未采用`</sub>

- **[jev-browser-use](https://github.com/wy-coliney/jev-browser-use)** — 把循环拆开：Jev 负责点击，推理模型负责思考与验证。
  <sub>`开源项目` · ★1k+ · wy-coliney · `JS` · 调用点 [`skills/jev-browser-use/bridge.mjs`](https://github.com/wy-coliney/jev-browser-use/blob/HEAD/skills/jev-browser-use/bridge.mjs)，2026-09-22 阅读</sub>

- **[jev-trader](https://github.com/jarrodwatts/jev-trader)** — 在 Monad 测试网上做高频做市。Jev 根据价差和成交方向判断下一步买还是卖。
  <sub>`开源项目` · ★1k+ · `TS` · `choice` · 调用点 [`src/config.ts`](https://github.com/jarrodwatts/jev-trader/blob/HEAD/src/config.ts)，2026-09-22 阅读 · ⚠ `宣称未核实`</sub>

- **[reticle](https://github.com/reticlehq/reticle)** — 通过实际操作正在运行的应用来核实 AI 智能体说的“完成”，给出通过、失败或无法判断。其基准测试框架就采集到的证据用一次调用问 Jev：五个 noul（预期结果是否发生、采集是否干净、应用是否报错等）、一个通过／失败／未知的 choice，以及一个严重程度 score。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · reticlehq · `TS` · 调用点 [`bench/harness/jev.mjs`](https://github.com/reticlehq/reticle/blob/HEAD/bench/harness/jev.mjs)，2026-09-24 阅读</sub>

- **[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)** — macOS 上的 computer use：OCR 屏幕、分类下一步动作、点击。每步成本不到一分钱的零头。
  <sub>`开源项目` · ★1k+ · awlevin · `Py` · 调用点 [`typesafe_computer_use/decide.py`](https://github.com/awlevin/typesafe-computer-use/blob/HEAD/typesafe_computer_use/decide.py)，2026-09-22 阅读</sub>

- **[agent](https://github.com/AgentiLoop/Agent)** — 面向 Mac 的自主智能体 harness。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★100+ · agentiloop · `Swift` · 调用点 [`TypeSafeKit/Sources/TypeSafeKit/TypeSafeClient.swift`](https://github.com/AgentiLoop/Agent/blob/HEAD/TypeSafeKit/Sources/TypeSafeKit/TypeSafeClient.swift)，2026-09-22 阅读</sub>

- **[embodied-jev](https://github.com/FBddcz/embodied-jev)** — 基于 MuJoCo 的工作台：由模型驱动仿真的 Franka 机械臂完成搬运、堆叠和越障任务。接 Jev 时，每一步都是在控制器给出的候选动作中做一次 choice，输入是文本状态和检测到的坐标，成功与否由物理判定。Jev 两局搬运试跑分别用 89 和 88 步到达终态，但两局都在下放时失抓。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · fbddcz · `Py` · 调用点 [`src/embodied_jev/policies.py`](https://github.com/FBddcz/embodied-jev/blob/HEAD/src/embodied_jev/policies.py)，2026-09-22 阅读</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — 浏览器智能体：每个页面被索引成候选控件，由 Jev 选出下一步，因此不会点击页面上没有的东西；规划和阅读由 Gemini Flash 负责，答案引用页面原文。维护者记录的 46 个任务中成功率为 99.2%，托管版 Browser Use 为 97.8%，而成本不到其十分之一。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · agent-labs-dev · `Py` · 调用点 [`src/fastbrowse/clients/typesafe.py`](https://github.com/agent-labs-dev/fastbrowse/blob/HEAD/src/fastbrowse/clients/typesafe.py)，2026-09-22 阅读</sub>

- **[foreman](https://github.com/thruwire/foreman)** — 一个「软件工厂工头」，用 Jev 决定智能体流水线下一步该做什么。
  <sub>`开源项目` · ★100+ · thruwire · `Py` · 调用点 [`src/foreman/foreman/jev.py`](https://github.com/thruwire/foreman/blob/HEAD/src/foreman/foreman/jev.py)，2026-09-22 阅读</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · 调用点 [`scripts/jev.js`](https://github.com/kevinbadi/hyperedit/blob/HEAD/scripts/jev.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[interlinked-cli](https://github.com/QuentinCody/interlinked-cli)** — 面向 Claude Code、Codex 等 AI 编程智能体的本地防护层：按确定性规则检查每个工具钩子，拦下危险操作。Jev 是可选的评分信号：它的答案只能让判定更严，不能单独决定放行或拦截；任何失败或达到 0.25 美元的花费上限，都记为未测量。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · quentincody · `TS` · 调用点 [`src/harness/jev/client.ts`](https://github.com/QuentinCody/interlinked-cli/blob/HEAD/src/harness/jev/client.ts)，2026-09-22 阅读</sub>

- **[jev-browser](https://github.com/jkudish/jev-browser)** — 浏览器自动化，下一步动作由 Jev 选择。
  <sub>`开源项目` · ★100+ · jkudish · `TS` · 调用点 [`src/index.ts`](https://github.com/jkudish/jev-browser/blob/HEAD/src/index.ts)，2026-09-24 阅读</sub>

- **[jev-browser](https://github.com/Ying-Kai-Liao/jev-browser)** — 浏览器自动化：LLM 负责规划，Jev 负责决策。每一轮发一个约 300 毫秒的请求，同时问选哪个元素、做什么动作、填什么值，以及这一步是否已完成、受阻、出错或即将做不可逆的操作；再由 Playwright 执行。作者最近一次运行在真实网站的 42 个任务中做对 40 个，误报完成 0 次。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · ying-kai-liao · `JS` · 调用点 [`src/jev.mjs`](https://github.com/Ying-Kai-Liao/jev-browser/blob/HEAD/src/jev.mjs)，2026-09-24 阅读</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · 调用点 [`apps/server/src/jev/client.ts`](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts)，2026-09-22 阅读</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `noul` · 调用点 [`scripts/jev-decide.mjs`](https://github.com/Sac-Y/Jev-cu/blob/HEAD/scripts/jev-decide.mjs)，2026-09-22 阅读</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。
  <sub>`开源项目` · ★100+ · `Py` · `choice` · `score` · `noul` · 调用点 [`tactics.py`](https://github.com/RomanSlack/jev-drone/blob/HEAD/tactics.py)，2026-09-22 阅读 · ⚠ `宣称未核实`</sub>

- **[jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision)** — DeepSeek Harness 插件，也可经 iPolloWork 供 OpenCode 和 Codex Harness 使用：让智能体问 Jev 当前可用的哪个工具、技能或智能体适合任务，是否需要某项能力，以及结果按给定标准得分如何。它只返回选择和概率，不执行任何动作。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · devin-axis · `JS` · 调用点 [`service/jev.mjs`](https://github.com/Devin-AXIS/jev-dsh-decision/blob/HEAD/service/jev.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — 面向 Codex、Claude Code、OpenCode 等编程智能体的本地网关。每一轮它都问 Jev 现有工具里哪个合适；Jev 有把握时就引导 LLM 调用该工具，否则请求原样放行。Jev 宕机、变慢或配置有误时，请求直接发给 LLM。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · vinilana · `TS` · 调用点 [`src/jev.ts`](https://github.com/vinilana/jev-gateway/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给编程智能体用的安全钩子：每次工具调用前，Jev 判断这次调用可能造成多大危害、是不是用户要求的、是否在执行不可信的文字，再由代码决定拒绝、询问还是放行；调用返回后，Jev 扫描结果中的提示注入。支持 Claude Code、Codex、Cursor 等。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · leepokai · `JS` · 调用点 [`src/jev.js`](https://github.com/leepokai/jev-guard/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[jev-mem](https://github.com/libingzheren/Jev-Mem)** — 智能体记忆系统：频繁的记忆决策由 Jev（或本地的 Laya）用 noul 和 choice 来做，包括记忆之间该建立哪些关系、在哪个图视图中检索、何时证据已经足够；答案由 LLM 撰写。论文报告在 LoCoMo 上答案质量高出 11.0%，查询延迟低 36.7%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · libingzheren · `Py` · 调用点 [`memory/jev_client.py`](https://github.com/libingzheren/Jev-Mem/blob/HEAD/memory/jev_client.py)，2026-09-22 阅读</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — 只读的 Instagram、TikTok 与 LinkedIn 调研：Jev 先路由平台，再从最新浏览器证据中选择受限的 socai CLI 动作；代码校验目标并保留来源链接。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · socai-io · `JS` · `choice` · 调用点 [`src/actions.js`](https://github.com/socai-io/jev-social/blob/HEAD/src/actions.js)，2026-09-23 阅读 · ⚠ `需第三方密钥`</sub>

- **[jev-trade](https://github.com/aowang-ai/jev-trade)** — 在 Hyperliquid 上交易的机器人，用五个钱包运行五个币种。每个 tick，Jev 读取订单簿和持仓并回答几个 choice：做多还是做空；开仓、平仓还是持有；以及全仓杠杆倍数。下单由机器人完成，持有则不下单。没有钱包私钥时是模拟成交的演练。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · aowang-ai · `TS` · 调用点 [`src/model.ts`](https://github.com/aowang-ai/jev-trade/blob/HEAD/src/model.ts)，2026-09-24 阅读</sub>

- **[jev-use](https://github.com/savka777/jev-use)** — macOS 上用语音或打字操作电脑：读取前台窗口的辅助功能树而不截图；每一步发一个 Jev 请求，选出一个操作和一个带编号的目标，要输入的文字取自你原话中的片段，再用 noul 判断是否还需要后续步骤、效果是否已经出现。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · savka777 · `Swift` · 调用点 [`Sources/JevCore/Decision.swift`](https://github.com/savka777/jev-use/blob/HEAD/Sources/JevCore/Decision.swift)，2026-09-24 阅读</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/jev.js`](https://github.com/moritzkremb/jev-voice-browser/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension)** — Chrome 侧边栏扩展：边输入边把页面的 WebMCP 工具变成 Jev 问题：在所有工具加“都不是”之间做一次 choice，枚举字段用 choice，布尔字段用 noul，自由文本变成在你自己话语片段之间的 choice，每个可选字段再加一个“是否提到了”的 noul。只有有把握的只读调用才会自动执行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · sdras · `JS` · 调用点 [`src/jev.js`](https://github.com/sdras/jev-webmcp-extension/blob/HEAD/src/jev.js)，2026-09-24 阅读</sub>

- **[jevharness](https://github.com/TianyuCodings/JevHarness)** — 由 LLM 编写针对具体任务的 harness：代码计算特征、向 Jev 提问，再把答案组合成动作；之后可以用奖励和完整执行轨迹来修改它。在作者的 Pokémon 实验中，经过五轮反思，评测胜率从 12 局赢 3 局升到 12 局赢 9 局。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · tianyucodings · `Py` · 调用点 [`auto_jev/providers.py`](https://github.com/TianyuCodings/JevHarness/blob/HEAD/auto_jev/providers.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevpilot](https://github.com/standardagents/jevpilot)** — 驾驶模拟器的自动驾驶，每个 tick 问两个 choice；只剩单一选项的问题直接在本地短路，不花钱发出去。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · 调用点 [`server/jev.js`](https://github.com/standardagents/jevpilot/blob/HEAD/server/jev.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — 面向模型、工具和子智能体的路由器。
  <sub>`开源项目` · ★100+ · billionsbobby · `TS` · 调用点 [`functions/api/jev.js`](https://github.com/BillionsBobby/JevRouter/blob/HEAD/functions/api/jev.js)，2026-09-22 阅读</sub>

- **[macbrow](https://github.com/timpratim/macbrow)** — 用语音控制 Mac 和 Chrome。每句话由一次约 300 毫秒的 Jev 请求来路由：在当前打开的应用可用的工具以及“闲聊”“新动作”之间做一次 choice，同时用 choice 回答参数；置信度高就执行，中等就先确认。LLM 为新动作写出的脚本，会再用一个 noul 检查它是否真能完成请求。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · timpratim · `Py` · 调用点 [`macbrow/generator.py`](https://github.com/timpratim/macbrow/blob/HEAD/macbrow/generator.py)，2026-09-22 阅读</sub>

- **[mobile-jev](https://github.com/droidrun/mobile-jev)** — 移动端 computer use：由 Jev 决定手机屏幕上的下一个动作。
  <sub>`开源项目` · ★100+ · droidrun · `JS` · 调用点 [`apps/jev-studio/app/components/use-studio.ts`](https://github.com/droidrun/mobile-jev/blob/HEAD/apps/jev-studio/app/components/use-studio.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。
  <sub>`开源项目` · ★100+ · `Py` · `choice` · 调用点 [`src/neo4jev/navigator.py`](https://github.com/jexp/neo4jev/blob/HEAD/src/neo4jev/navigator.py)，2026-09-22 阅读</sub>

- **[omg.dev](https://github.com/BennyKok/omg.dev)** — 用手机遥控在你电脑或托管云机上运行的 Claude Code、Codex 等编程智能体。它的移动端端到端测试把 Jev 当作决策层：给定屏幕的无障碍树，用 noul 判断某一步是否完成、是否走进死胡同，再用 choice 选出下一步要点的元素。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · bennykok · `TS` · 调用点 [`mobile/scripts/jev.ts`](https://github.com/BennyKok/omg.dev/blob/HEAD/mobile/scripts/jev.ts)，2026-09-22 阅读</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — 给编程智能体做的决策层：一个可度量的工具调用闸门，外加一个返回校准答案的类型化提问。
  <sub>`插件` · ★100+ · y0usaf · `TS` · 调用点 [`src/client.ts`](https://github.com/y0usaf/pi-jev/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — 统管所有机器人的 CLI：每台机器人配一个 LLM 作大脑，由 Jev 做决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · rokbenko · `Py` · 调用点 [`quackd/agent/decision/systemone.py`](https://github.com/rokbenko/quackd/blob/HEAD/quackd/agent/decision/systemone.py)，2026-09-24 阅读</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — 用当前会话上下文给智能体的技能排序以决定下一步，带 Claude Code hook。
  <sub>`插件` · ★100+ · dicklesworthstone · `Rs` · 调用点 [`src/jev/endpoint.rs`](https://github.com/Dicklesworthstone/skillranker/blob/HEAD/src/jev/endpoint.rs)，2026-09-22 阅读</sub>

- **[system1-agents](https://github.com/ThinkFlowLab/system1-agents)** — 预置的浏览器操作、电脑操作、游戏和机器人智能体，决策以类型化 choice 的形式交给 System 1 模型（Jev、Laya 或 Cua-S1）。在作者的测试中，Jev 与聊天模型得分相同，而各场景下快 1.41 到 6.39 倍、便宜 5.3 到 25.3 倍。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · thinkflowlab · `Py` · 调用点 [`s1a/decision_models/wire.py`](https://github.com/ThinkFlowLab/system1-agents/blob/HEAD/s1a/decision_models/wire.py)，2026-09-24 阅读</sub>

- **[systemoneharness](https://github.com/HarnessRouter/SystemOneHarness)** — 面向 System One 模型的 harness。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · harnessrouter · `Py` · 调用点 [`systemone_harness/provider.py`](https://github.com/HarnessRouter/SystemOneHarness/blob/HEAD/systemone_harness/provider.py)，2026-09-22 阅读</sub>

- **[tiptour-macos](https://github.com/milind-soni/tiptour-macos)** — 替你点击的 macOS 菜单栏助手。默认的 Jev 模式下你输入任务；每一步由 Jev 的 choice 从本地检测到的屏幕控件中选一个，TipTour 照此点击，不设置信度门槛，直到 Jev 选择“无”或报告任务完成，或满 12 步为止。截图不离开本机。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · milind-soni · `Swift` · 调用点 [`TipTour/Jev/JevClient.swift`](https://github.com/milind-soni/tiptour-macos/blob/HEAD/TipTour/Jev/JevClient.swift)，2026-09-22 阅读</sub>

- **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)** — 让 Jev 玩《超级马里奥》。不看截图，直接读模拟器 RAM 里的结构化状态，再决定跑、跳、躲。
  <sub>`开源项目` · ★100+ · `Py` · `choice` · `score` · `noul` · 调用点 [`src/typesafe_mario/policy.py`](https://github.com/fhshaik/typesafe-mario/blob/HEAD/src/typesafe_mario/policy.py)，2026-09-22 阅读 · ⚠ `代码未实测` `仅一次提交` `无许可证`</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — 开源编程智能体，自带内核、记忆、多智能体编队和权限策略，可在终端、TUI 或浏览器中使用。可选开启的 TypeSafe 服务会向 Jev 提出类型化的 choice、noul 和 score 问题，用于推荐技能和给派发分类，智能体也可以把 Jev 当作工具调用。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · wrongstack · `TS` · 调用点 [`packages/core/src/typesafe/client.ts`](https://github.com/WrongStack/WrongStack/blob/HEAD/packages/core/src/typesafe/client.ts)，2026-09-22 阅读</sub>

- **[agent-chaperone](https://github.com/agent-chaperone/agent-chaperone)** — 在智能体工具调用执行前、以及工具结果被读取前做筛查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · agent-chaperone · `TS` · 调用点 [`src/backends/typesafe.ts`](https://github.com/agent-chaperone/agent-chaperone/blob/HEAD/src/backends/typesafe.ts)，2026-09-22 阅读</sub>

- **[azdaja](https://github.com/kubet/azdaja)** — 与 harness 无关的极简递归语言模型层：单个二进制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kubet · `Py` · 调用点 [`bench/jev/adapter.py`](https://github.com/kubet/azdaja/blob/HEAD/bench/jev/adapter.py)，2026-09-22 阅读</sub>

- **[browserclaw](https://github.com/GoldenLoaf24h/browserpaw)** — 高效率的 Chrome 浏览器自动化 MCP server。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · goldenloaf24h · `TS` · 调用点 [`app/native-server/src/jev/jev-client.ts`](https://github.com/GoldenLoaf24h/browserpaw/blob/HEAD/app/native-server/src/jev/jev-client.ts)，2026-09-22 阅读</sub>

- **[CUA-JEV](https://github.com/ZJU-REAL/CUA-JEV)** — 用 Jev 做电脑操作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · zju-real · `Py` · 调用点 [`src/cua_jev/cost.py`](https://github.com/ZJU-REAL/CUA-JEV/blob/HEAD/src/cua_jev/cost.py)，2026-09-24 阅读</sub>

- **[dejevu](https://github.com/idovmamane/dejevu)** — Jev？似曾相识。靠直觉运行的浏览器智能体，不需要 Jev：看一眼页面，调用一次任意开源模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · idovmamane · `Py` · 引用文件 [`dejevu/policy.py`](https://github.com/idovmamane/dejevu/blob/HEAD/dejevu/policy.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[discern](https://github.com/doeixd/discern)** — 类型安全、感知不确定性的语义模式匹配与控制流。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · doeixd · `TS` · 调用点 [`examples/headline.ts`](https://github.com/doeixd/discern/blob/HEAD/examples/headline.ts)，2026-09-22 阅读</sub>

- **[dsh-jev](https://github.com/buberlo/dsh-jev)** — 为 DeepSeek Harness 提供的、由 Jev 驱动的决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · buberlo · `TS` · 调用点 [`packages/dsh-jev/src/config.ts`](https://github.com/buberlo/dsh-jev/blob/HEAD/packages/dsh-jev/src/config.ts)，2026-09-24 阅读 · ⚠ `已归档`</sub>

- **[dsh-jev](https://github.com/zhangxaochen/dsh-jev)** — 面向 DeepSeek Harness（dsh）的 Jev（System One 决策模型）插件套件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · zhangxaochen · `TS` · 调用点 [`lib/typesafe-client.d.ts`](https://github.com/zhangxaochen/dsh-jev/blob/HEAD/lib/typesafe-client.d.ts)，2026-09-24 阅读</sub>

- **[ego-jev](https://github.com/jiangkoumo/ego-decision-layer)** — 用 Jev 驱动轻量浏览器：输入一张带索引的元素表，输出一个动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jiangkoumo · `JS` · 调用点 [`scripts/ego-jev.mjs`](https://github.com/jiangkoumo/ego-decision-layer/blob/HEAD/scripts/ego-jev.mjs)，2026-09-22 阅读</sub>

- **[ego-jev](https://github.com/ZephyrDeng/ego-jev)** — 为 ego-browser 提供的 Jev（TypeSafe System One）内循环：每个 DOM 步骤一次约 0.4 秒的类型化决策，而不是一轮 LLM 对话。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · zephyrdeng · `JS` · 调用点 [`skills/ego-jev/scripts/jev-loop.mjs`](https://github.com/ZephyrDeng/ego-jev/blob/HEAD/skills/ego-jev/scripts/jev-loop.mjs)，2026-09-24 阅读</sub>

- **[eutrya](https://github.com/hellozenstrategist-lab/eutrya)** — 原生面向 Jev 的 AI 安全研究框架，用于自主研究、多智能体集群、持久的狩猎看板和长时间运行的任务。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · hellozenstrategist-lab · `JS` · 调用点 [`bin/eutrya.mjs`](https://github.com/hellozenstrategist-lab/eutrya/blob/HEAD/bin/eutrya.mjs)，2026-09-24 阅读</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · evoke-build · `Rs` · 调用点 [`crates/evoke-adapters/src/systemone.rs`](https://github.com/evoke-build/evoke/blob/HEAD/crates/evoke-adapters/src/systemone.rs)，2026-09-24 阅读</sub>

- **[hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)** — 由 Jev 驱动的自主多源租房搜索。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · nancy-chauhan · `JS` · 调用点 [`jev_ultrafast/model.py`](https://github.com/Nancy-Chauhan/hearth-jev-rental-search/blob/HEAD/jev_ultrafast/model.py)，2026-09-22 阅读</sub>

- **[jcr](https://github.com/NiazMorshed2007/jcr)** — 由 Jev 驱动的解析器，帮智能体 harness 在仓库里找到确定性命令及其上下文。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · niazmorshed2007 · `JS` · 调用点 [`src/jcr/jev.ts`](https://github.com/NiazMorshed2007/jcr/blob/HEAD/src/jcr/jev.ts)，2026-09-22 阅读</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · forvela · `JS` · 调用点 [`src/decision.js`](https://github.com/forvela/jev-agent-browser/blob/HEAD/src/decision.js)，2026-09-22 阅读</sub>

- **[Jev-as-Policy](https://github.com/YuanKJing/Jev-as-Policy)** — “JEV 作为策略”的开源仓库：一键搭建仿真环境，用 Jev 选择动作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · yuankjing · `Py` · 调用点 [`jev_policy.py`](https://github.com/YuanKJing/Jev-as-Policy/blob/HEAD/jev_policy.py)，2026-09-24 阅读</sub>

- **[jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm)** — 在仿真机械臂上执行零样本英文目标：Jev 串联写死的原语动作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · taruntomar122 · `Py` · 调用点 [`jev_robotics/common.py`](https://github.com/TarunTomar122/jev-askable-arm/blob/HEAD/jev_robotics/common.py)，2026-09-22 阅读</sub>

- **[jev-autopilot](https://github.com/arielweinberger/jev-autopilot)** — 这个演示用 Jev 自主驾驶无人机在随机城市里从 A 点飞到 B 点。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · arielweinberger · `TS` · 调用点 [`server/pilot.ts`](https://github.com/arielweinberger/jev-autopilot/blob/HEAD/server/pilot.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-bot](https://github.com/bl888m/jev-bot)** — 由 JEV 驱动的股票、加密货币与迷因币市场决策机器人：输入状态，输出 BUY/SELL/HOLD/AVOID，默认模拟交易。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · bl888m · `Py` · 调用点 [`jev_bot/jev.py`](https://github.com/bl888m/jev-bot/blob/HEAD/jev_bot/jev.py)，2026-09-24 阅读</sub>

- **[jev-browser](https://github.com/openqa-cn/jev-browser)** — Jev Browser：带索引的浏览器自动化。Jev 选择要操作的控件，Playwright 负责执行。一个 CodexQA 技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · openqa-cn · `TS` · 调用点 [`src/jev.ts`](https://github.com/openqa-cn/jev-browser/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[jev-browser](https://github.com/tontoko/jev-browser)** — 一个基于 Jev 与 Playwright 的统一内核：带类型的 SDK、常驻 CLI，以及带原生浏览器操作和确定性断言的 MCP 服务器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tontoko · `JS` · 调用点 [`src/decision.ts`](https://github.com/tontoko/jev-browser/blob/HEAD/src/decision.ts)，2026-09-24 阅读</sub>

- **[jev-browser-skill](https://github.com/hqman/jev-browser-skill)** — 由 Jev 驱动的隔离 Playwright Chromium：编码智能体执行一个范围很窄的浏览器目标，由 Jev 选择页面内的操作；默认经 Vercel AI Gateway，也可直接调用 TypeSafe API。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · hqman · `TS` · 调用点 [`src/jev-model.ts`](https://github.com/hqman/jev-browser-skill/blob/HEAD/src/jev-model.ts)，2026-09-24 阅读</sub>

- **[jev-code](https://github.com/rhighs/jev-code)** — 由 Jev 类型化决策和受约束的 AST 生成驱动的交互式 TypeScript 编码 CLI。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · rhighs · `TS` · 调用点 [`src/bash-ast.ts`](https://github.com/rhighs/jev-code/blob/HEAD/src/bash-ast.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-cua](https://github.com/ronadin2002/jev-cua)** — 用语音和文字控制 macOS：一个悬浮栏，由 Jev 实时选择界面操作，并持续执行“观察—行动—验证”循环。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ronadin2002 · `Swift` · 调用点 [`Sources/Core.swift`](https://github.com/ronadin2002/jev-cua/blob/HEAD/Sources/Core.swift)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-desktop](https://github.com/yikangy873-gif/jev-desktop)** — 在 Codex Computer Use 内部做动作选择。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · yikangy873-gif · `JS` · 调用点 [`plugins/jev-desktop/scripts/bridge-server.mjs`](https://github.com/yikangy873-gif/jev-desktop/blob/HEAD/plugins/jev-desktop/scripts/bridge-server.mjs)，2026-09-22 阅读</sub>

- **[jev-doom-agent](https://github.com/lukaske/jev-doom-agent)** — 浏览器原生的 Doom 智能体实验，带结构化空间状态与实时决策遥测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · lukaske · `TS` · 调用点 [`server/typesafe.ts`](https://github.com/lukaske/jev-doom-agent/blob/HEAD/server/typesafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-for-chrome](https://github.com/chy4pro/jev-for-chrome)** — Jev for Chrome：用亚秒级决策模型驱动你正在看的那个标签页。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · chy4pro · `TS` · 调用点 [`src/shared/providers/typesafe.ts`](https://github.com/chy4pro/jev-for-chrome/blob/HEAD/src/shared/providers/typesafe.ts)，2026-09-22 阅读</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · antoniocoppe · `TS` · 调用点 [`demos/proof/row-filter/run.ts`](https://github.com/AntonioCoppe/jev-harness/blob/HEAD/demos/proof/row-filter/run.ts)，2026-09-22 阅读</sub>

- **[jev-harness](https://github.com/TypeSafeAI/jev-harness)** — 为 TypeSafe AI Jev 打造的编码框架：LLM 提出方案，Jev 回答窄问题，代码做决定，每一步都有记录。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · typesafeai · `TS` · 调用点 [`examples/host/jev-choice.ts`](https://github.com/TypeSafeAI/jev-harness/blob/HEAD/examples/host/jev-choice.ts)，2026-09-24 阅读</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — 精细的机器人控制，带物理预览与可配置的 LIBERO 任务。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · dimweaker · `Py` · 调用点 [`src/jev_libero/client.py`](https://github.com/Dimweaker/jev-libero/blob/HEAD/src/jev_libero/client.py)，2026-09-22 阅读</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 面向 Apple 芯片上原生 macOS 应用的 computer use 智能体：由 OmniParser CoreML、Apple Vision OCR 和辅助功能标签在本机找出窗口里的控件，再由 Jev 根据观察到的文字（从不看像素）用 choice 选下一步动作。输入前有防护检查，基准测试核对的是实际结果，而不是 Jev 的 DONE 判断。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jcpsimmons · `JS` · 调用点 [`src/providers.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs)，2026-09-22 阅读</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · parth-kp · `Py` · 调用点 [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py)，2026-09-22 阅读</sub>

- **[jev-mobile](https://github.com/Friedjof/jev-mobile)** — 结合 Mobile MCP 的快速 Android 结构化控制循环。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · friedjof · `Py` · 调用点 [`src/jev_mobile/cli.py`](https://github.com/Friedjof/jev-mobile/blob/HEAD/src/jev_mobile/cli.py)，2026-09-22 阅读</sub>

- **[jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)** — 多无人机自主实验室：展示 Jev 的反射式决策，可选叠加 System 2 战略指导。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · khordoo · `TS` · 调用点 [`lib/reflex/jev-server.ts`](https://github.com/khordoo/jev-reflex-autonomy-lab/blob/HEAD/lib/reflex/jev-server.ts)，2026-09-22 阅读</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · choxos · `JS` · 调用点 [`docs/jev.js`](https://github.com/choxos/jev-reviewer/blob/HEAD/docs/jev.js)，2026-09-22 阅读</sub>

- **[jev-robot-control](https://github.com/openroboto-ai/jev-robot-control)** — 在 MuJoCo 中直接对 xArm7 做笛卡尔控制，对比 Jev 与两个 LLM：每一步选择意图、移动方向和夹爪动作，附原始响应、轨迹与回放。每个控制器只跑了一次（seed 0），不是成功率估计。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · openroboto-ai · `Py` · 调用点 [`incremental-comparisons/20260919-193012-198478-0/sources/incremental_policy.py`](https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/incremental-comparisons/20260919-193012-198478-0/sources/incremental_policy.py)，2026-09-24 阅读 · 作者结论：无定论（作者自述，未经本仓库复现） · ⚠ `仅一次提交`</sub>

- **[jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp)** — 把整个浏览器任务一次性交出去：决策模型在服务端驱动页面，一个流程只需一次调用，而不是每次点击一轮。基于 Chrome DevTools 协议，提供基于引用的元素表、代码检查的断言和零模型的宏回放。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · jiawei686 · `Py` · 调用点 [`jev_ultrafast_mcp/config.py`](https://github.com/jiawei686/jev-ultrafast-mcp/blob/HEAD/jev_ultrafast_mcp/config.py)，2026-09-24 阅读</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — 一个智能体插件：把不需要文本输出的步骤交给 Jev，而不是主模型。
  <sub>`插件` · ★10+ · shitianfang · `JS` · 调用点 [`src/backends/typesafe.ts`](https://github.com/shitianfang/jev-use/blob/HEAD/src/backends/typesafe.ts)，2026-09-22 阅读</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — 生产级的 Jev 用例 harness，带置信度门控的决策逻辑。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kenhuangus · `Py` · 调用点 [`src/jev_usecases/client.py`](https://github.com/kenhuangus/jev-usecases/blob/HEAD/src/jev_usecases/client.py)，2026-09-22 阅读</sub>

- **[Jev_Star](https://github.com/sc2musa/Jev_Star)** — 星际争霸 II 的宏观运营与微操：由 JEV 选择动作，可选配 LLM 做规划；附论文和完整的获胜对局录像。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sc2musa · `Py` · 调用点 [`macro/sc2_rl_agent/starcraftenv_test/agent/jev_agent.py`](https://github.com/sc2musa/Jev_Star/blob/HEAD/macro/sc2_rl_agent/starcraftenv_test/agent/jev_agent.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ray-hughes · `Rb` · 调用点 [`lib/jevalyn/configuration.rb`](https://github.com/Ray-Hughes/jevalyn/blob/HEAD/lib/jevalyn/configuration.rb)，2026-09-22 阅读</sub>

- **[Jevbridge](https://github.com/tacticocc/Jevbridge)** — 把 TypeSafe Jev 与任意 LLM 连起来的 ACP 与 MCP 适配器：在 Codex、Claude 等旁边提供电脑操作和带类型的决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · gamesonrblx · `TS` · 调用点 [`src/types.ts`](https://github.com/tacticocc/Jevbridge/blob/HEAD/src/types.ts)，2026-09-24 阅读</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — 用一个不会生成文本的模型搭的聊天机器人（自回归驱动）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · bewinxed · `TS` · 调用点 [`src/jevgpt/sampler.py`](https://github.com/Bewinxed/jevgpt/blob/HEAD/src/jevgpt/sampler.py)，2026-09-22 阅读</sub>

- **[jevscape](https://github.com/Skyvern-AI/jevscape)** — 给 Jev 的 RuneBench harness：有界动作目录、tick 模式控制器与实时看板。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · skyvern-ai · `TS` · 调用点 [`agents/jev/jev-client.ts`](https://github.com/Skyvern-AI/jevscape/blob/HEAD/agents/jev/jev-client.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[JevScout](https://github.com/hqman/JevScout)** — 在真实公司官网上找工作的编码智能体技能：Chrome 负责看和操作，Jev 为每个链接和职位打分，宿主 LLM 从不决定点哪里。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · hqman · `Py` · 调用点 [`jev_job_hunter/jev.py`](https://github.com/hqman/JevScout/blob/HEAD/jev_job_hunter/jev.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent)** — 本地开源的 Jev 替代：用 Laya 做浏览器智能体决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · chenneyzhuang · `Py` · 引用文件 [`examples/diagnostics/jev_flow_h2h.py`](https://github.com/ChenneyZhuang/laya-browser-agent/blob/HEAD/examples/diagnostics/jev_flow_h2h.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[laya-jev-GraphRAG](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG)** — 一个智能体式 GraphRAG 引擎，可切换 System One 决策模型（本地 Laya 或云端 Jev）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · bodepudimuneendra-netizen · `Py` · 调用点 [`graphrag_neo4j_laya/graphrag/models/jev.py`](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG/blob/HEAD/graphrag_neo4j_laya/graphrag/models/jev.py)，2026-09-24 阅读</sub>

- **[live-jev](https://github.com/vinilana/live-jev)** — 浏览器里的 2D 自动驾驶仿真，由 Jev 决策模型驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · vinilana · `JS` · 调用点 [`server.js`](https://github.com/vinilana/live-jev/blob/HEAD/server.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[live-jev](https://github.com/okinaaudio/live-jev)** — 用一句简短的话（日语或英语）控制 Ableton Live。⌘⇧Space 呼出，打字或口述，完成。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · okinaaudio · `Py` · 调用点 [`daemon.py`](https://github.com/okinaaudio/live-jev/blob/HEAD/daemon.py)，2026-09-24 阅读</sub>

- **[mario-jev](https://github.com/shantanugoel/mario-jev)** — 一个玩《超级马力欧兄弟》的原型：Jev 读取结构化的内存观测，回答关于移动与跳跃的具体问题，再由代码把答案组合成手柄按键。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · shantanugoel · `Py` · 调用点 [`src/mario_jev/policy.py`](https://github.com/shantanugoel/mario-jev/blob/HEAD/src/mario_jev/policy.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[OmniJev](https://github.com/shapsider/OmniJev)** — OmniJev：多模态的有限选项决策接口与 MuJoCo 具身工作台，提供轨迹回放与决策概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · shapsider · `Py` · 调用点 [`embodied/src/embodied_jev/policies.py`](https://github.com/shapsider/OmniJev/blob/HEAD/embodied/src/embodied_jev/policies.py)，2026-09-24 阅读</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。
  <sub>`开源项目` · ★10+ · `TS` · `choice` · 调用点 [`server/src/jev.ts`](https://github.com/emrickgarrett/OneVOneJev/blob/HEAD/server/src/jev.ts)，2026-09-22 阅读 · ⚠ `代码未实测` `无许可证`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — 给 pi 编程智能体的运行时约束：每个有副作用的工具调用执行前，先对照你说过的话检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · nyarlathoteppppp · `TS` · 调用点 [`bench/jev-lab.ts`](https://github.com/Nyarlathoteppppp/pi-heed/blob/HEAD/bench/jev-lab.ts)，2026-09-22 阅读</sub>

- **[pi-jev](https://github.com/TheoOliveira/pi-jev)** — 为 Pi 编码智能体提供语义化的工具路由和带类型的 System One 决策，基于 TypeSafe Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · theooliveira · `TS` · 调用点 [`src/jev.ts`](https://github.com/TheoOliveira/pi-jev/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode)** — 给 Pi 编程智能体做的自动模式：在语义层面自动批准 bash、写入和编辑类工具调用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jomatsu · `TS` · 调用点 [`src/jev/transport.ts`](https://github.com/jomatsu/pi-jev-auto-mode/blob/HEAD/src/jev/transport.ts)，2026-09-22 阅读</sub>

- **[playjev](https://github.com/filedcom/playjev)** — 由 Jev 与 Playwright 驱动的快速、带类型的浏览器自动化。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · filedcom · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/filedcom/playjev/blob/HEAD/src/jev/client.ts)，2026-09-24 阅读</sub>

- **[public-browser](https://github.com/Silbercue/public-browser)** — 让 Claude Code 和 Cursor 驱动 Chrome，使用你真实的浏览器配置，并称能减少 token、成本与工具调用。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · silbercue · `TS` · 调用点 [`examples/jev-loop.mjs`](https://github.com/Silbercue/public-browser/blob/HEAD/examples/jev-loop.mjs)，2026-09-24 阅读 · ⚠ `宣称未核实`</sub>

- **[robojev](https://github.com/lykycy123/RoboJEV)** — 在 MuJoCo 里对 Franka Panda 做两阶段 JEV 控制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · lykycy123 · `Py` · 调用点 [`src/jev_vla_sim/config.py`](https://github.com/lykycy123/RoboJEV/blob/HEAD/src/jev_vla_sim/config.py)，2026-09-22 阅读</sub>

- **[Sedum (npm: sedum-cli)](https://github.com/sedum-dev/sedum)** — 在 Playwright 代码旁用纯英文句子编写浏览器端到端测试。目标模式下，由 Jev 的 Choice 选出每一步操作（点击、输入、完成或受阻）及其目标；逐句步骤每句用一个 Choice；每条验证断言是两个 Noul（holds、contradicted）。动作由 Playwright 执行，阈值由代码判定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sedum-dev · `TS` · `choice` · `noul` · 调用点 [`packages/provider-typesafe/src/index.ts`](https://github.com/sedum-dev/sedum/blob/HEAD/packages/provider-typesafe/src/index.ts)，2026-09-30 阅读 · ⚠ `宣称未核实` `作者自荐`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · myc0576 · `Py` · 调用点 [`src/smartmoney_cub_harness/jev/direct.py`](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[super-jev](https://github.com/Kevthetech143/super-jev)** — 小而可扩展的「决策到动作」harness。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kevthetech143 · `Py` · 调用点 [`skills/super-jev/superjev.py`](https://github.com/Kevthetech143/super-jev/blob/HEAD/skills/super-jev/superjev.py)，2026-09-22 阅读</sub>

- **[tsai-sc](https://github.com/phyous/tsai-sc)** — 通过键鼠操作一款 90 年代即时战略游戏，并记录每次动作的概率。
  <sub>`开源项目` · ★10+ · phyous · `Py` · 调用点 [`tsai_sc/typesafe.py`](https://github.com/phyous/tsai-sc/blob/HEAD/tsai_sc/typesafe.py)，2026-09-22 阅读</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — 用 Jev 筛选一整个文件夹的简历：类型化判断、可编辑的策略、免费重新打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · gtaras7 · `TS` · 调用点 [`cv-screen/src/cli.ts`](https://github.com/gtaras7/typesafe-jev/blob/HEAD/cv-screen/src/cli.ts)，2026-09-22 阅读</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — 一个 WebMCP 基准，衡量 WebMCP 与其他浏览器智能体接口的差距。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · nekuda-ai · `TS` · 调用点 [`experiments/jev/frozen/arms/decision-providers.mjs`](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/experiments/jev/frozen/arms/decision-providers.mjs)，2026-09-22 阅读</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · abhishekswe · `TS` · 调用点 [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts)，2026-09-22 阅读</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · carlosedm10 · `Py` · 调用点 [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — 让 Aside 智能体用 Jev 做决策（Choice／Score／Noul）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · himomohi · `Py` · 调用点 [`src/aside_jev/jev.py`](https://github.com/himomohi/aside-jev/blob/HEAD/src/aside_jev/jev.py)，2026-09-22 阅读</sub>

- **[AskJev](https://github.com/ranjan2829/AskJev)** — AskJev：适用于任意网站的 Jev 自动驾驶，并对不可逆的点击加一道防护（使用 TypeSafe System One，而不是 Claude）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ranjan2829 · `TS` · 调用点 [`mcp/src/jev-client.ts`](https://github.com/ranjan2829/AskJev/blob/HEAD/mcp/src/jev-client.ts)，2026-09-24 阅读</sub>

- **[beebots](https://github.com/imikerussell/beebots)** — 三个交易机器人在 OKX 永续合约上比赛，默认是模拟盘：每一步由 Jev（或 Gemini）用 choice 从合法动作中选出，再用 score 给出信心；另有确定性的备用选择器、纯代码写的风控层，以及显示每个决策由谁做出的实时面板。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · imikerussell · `TS` · `choice` · `score` · 调用点 [`src/jev.ts`](https://github.com/imikerussell/beebots/blob/HEAD/src/jev.ts)，2026-10-24 模型阅读</sub>

- **[bicameral](https://github.com/AbdelStark/bicameral)** — 混合式编程 harness：System 2 负责写，System 1（Jev）负责反射式动作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · abdelstark · `TS` · 调用点 [`packages/s1-runtime/src/backends/typesafe.ts`](https://github.com/AbdelStark/bicameral/blob/HEAD/packages/s1-runtime/src/backends/typesafe.ts)，2026-09-22 阅读</sub>

- **[browser-use-olympics](https://github.com/eriestra/browser-use-olympics)** — 浏览器操作奥运会：一个提示、五个项目、一块秒表。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · eriestra · `TS` · 调用点 [`almond-fastloop.mjs`](https://github.com/eriestra/browser-use-olympics/blob/HEAD/almond-fastloop.mjs)，2026-09-22 阅读</sub>

- **[casse-brique-typesafe](https://github.com/Para-FR/casse-brique-typesafe)** — 一个 Next.js 打砖块游戏，球拍由 Jev 实时控制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · para-fr · `TS` · 调用点 [`src/app/api/paddle/route.ts`](https://github.com/Para-FR/casse-brique-typesafe/blob/HEAD/src/app/api/paddle/route.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[computer-use-jev](https://github.com/paulsmith/computer-use-jev)** — 以 Jev 为决策者的 macOS computer use。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · paulsmith · `Go` · 调用点 [`typesafe/client.go`](https://github.com/paulsmith/computer-use-jev/blob/HEAD/typesafe/client.go)，2026-09-22 阅读</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — 给 DeepSeek Harness 的压缩前顾问，在标准压缩流程之前运行。 <sub>(机翻)</sub>
  <sub>`开源项目` · wjw66 · `TS` · 调用点 [`src/jev/protocol.ts`](https://github.com/wjw66/deepseek-harness-jev-pre-compaction/blob/HEAD/src/jev/protocol.ts)，2026-09-22 阅读</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — 给 DeepSeek Harness 的 Jev 判定式上下文压缩：语义化的工具结果裁剪。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · yangyu666 · `JS` · 调用点 [`jev.js`](https://github.com/yangyu666/dsh-jev-prune/blob/HEAD/jev.js)，2026-09-22 阅读</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — 给 DeepSeek Harness 的 Jev 决策工具与实时验证基准。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · xienda · `JS` · 调用点 [`lib/index.js`](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev 驱动你的轻量浏览器：每步一次类型化选择请求，单文件零依赖。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · shikaizhong-design · `JS` · 调用点 [`jego.js`](https://github.com/shikaizhong-design/ego-jev-ultrafast/blob/HEAD/jego.js)，2026-09-22 阅读</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。
  <sub>`代码片段` · `Py` · `choice` · `noul` · 调用点 [`examples/03-fan-out/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/03-fan-out/main.py)，2026-09-22 阅读 · ⚠ `代码未实测`</sub>

- **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)** — 把「选哪个工具」的 choice 和「到底需不需要工具」的 noul 配对使用 —— 因为这是两个不同的问题。
  <sub>`代码片段` · `Py` · `choice` · `noul` · 调用点 [`examples/04-tool-selection/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/04-tool-selection/main.py)，2026-09-22 阅读 · ⚠ `代码未实测`</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — 给 DeepSeek Harness 的判定式上下文压缩，取代有损的 LLM 摘要。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kolawong · `TS` · 调用点 [`src/jev.ts`](https://github.com/kolawong/fast-compaction-dsh/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[Flick](https://github.com/bgivenb/flick-computer-use)** — 本地 stdio MCP 服务器，可执行完整的浏览器和 macOS 任务：每一步“观察—决定—行动”都向 Jev 问一个 choice，选项是以观测到的元素 ID 为键的动作；另有几个 choice 决定填哪个字段、填什么值。浏览器用 Playwright 驱动，macOS 用 Swift 辅助功能驱动。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · bgivenb · `TS` · `Swift` · `choice` · `noul` · 调用点 [`src/providers/typesafe.ts`](https://github.com/bgivenb/flick-computer-use/blob/HEAD/src/providers/typesafe.ts)，2026-10-24 模型阅读</sub>

- **[gg-friggin-ez](https://github.com/ItisShikhar/gg-friggin-ez)** — 给 Node.js 的快速多语言脏话与毒性筛查器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · itisshikhar · `TS` · 调用点 [`demo/js/models.js`](https://github.com/ItisShikhar/gg-friggin-ez/blob/HEAD/demo/js/models.js)，2026-09-22 阅读</sub>

- **[Harness Router](https://github.com/Protocol-Lattice/harness-router)** — 在现有 Agent 循环中挑选下一个工具：给定目标、当前观测和工具列表，由 Jev 返回带置信度的工具选择，或交回宿主规划器处理。会缓存可复用的选择，可选 MCTS 搜索，能挂接到 Codex 等框架，也可作为 MCP 服务器运行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · protocol-lattice · `Py` · `choice` · 调用点 [`src/harness_router/config.py`](https://github.com/Protocol-Lattice/harness-router/blob/HEAD/src/harness_router/config.py)，2026-10-24 模型阅读</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — 面向智能体开发者的网页应用：粘贴某一步的执行轨迹，由 Jev 判定为通过、重试、升级或停止。没有 TYPESAFE_API_KEY 时，本地启发式规则返回同样结构的答案，并标为演示模式。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/harnessjudge/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · abdelstark · `TS` · 调用点 [`apps/server/src/jev.ts`](https://github.com/AbdelStark/heist-one/blob/HEAD/apps/server/src/jev.ts)，2026-09-22 阅读</sub>

- **[jet](https://github.com/arczhi/jet)** — 原生面向 TypeSafe（Jev）的编码智能体，基于递归式 LLM 上下文分解，配有原生 macOS 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arczhi · `Py` · 调用点 [`src/jet/providers/typesafe_judge.py`](https://github.com/arczhi/jet/blob/HEAD/src/jet/providers/typesafe_judge.py)，2026-09-24 阅读</sub>

- **[Jev Browser Bridge](https://github.com/lexmount/jev-browser-bridge)** — 让 Jev 浏览器 Agent 运行在任何支持 CDP 的浏览器上，包括从不渲染页面的浏览器：它读取 DOM 而不是坐标，向 Jev 问一个 choice 选操作、再问一个 choice 选目标。作者报告在六种浏览器上的 172 个 MiniWoB++ 回合中成功率为 59–65%，基于坐标的读取方式为 24–31%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lexmount · `Py` · `choice` · 调用点 [`jev_browser_bridge/model.py`](https://github.com/lexmount/jev-browser-bridge/blob/HEAD/jev_browser_bridge/model.py)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[Jev Civilizations](https://github.com/JonesSteven/jev_civilization)** — 一款带在线演示的小型策略游戏：四个部落自主生活，你只能改变环境。每回合 Jev 用 choice 从真正合法的行动中为每个部落选一个，普通的游戏引擎计算结果，检查器会显示 Jev 收到了哪些信息。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jonessteven · `TS` · `choice` · 调用点 [`scripts/probe-jev.ts`](https://github.com/JonesSteven/jev_civilization/blob/HEAD/scripts/probe-jev.ts)，2026-10-24 模型阅读</sub>

- **[Jev Plays Pokémon Red](https://github.com/christianmat/jev-pokemon)** — 让 Jev 通关《宝可梦 红》的框架：读取模拟器内存，列出合法选项及相关事实（属性克制、伤害估计、离目标还有多远），由 Jev 选一个。37 小时 40 分钟内共做出 16,150 次决策，花费约 1.65 美元，通过 Vercel AI Gateway 上的 AI SDK 调用。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · christianmat · `TS` · 调用点 [`src/jev/gateway.ts`](https://github.com/christianmat/jev-pokemon/blob/HEAD/src/jev/gateway.ts)，2026-10-24 模型阅读 · ⚠ `宣称未核实`</sub>

- **[jev-A-share-trader](https://github.com/Eric-Zhou-0302/jev-A-share-trader)** — 由 Jev 驱动的中国 A 股技术分析工作台，支持 AKShare/Tushare、市场扫描以及买入/持有/卖出建议。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · eric-zhou-0302 · `Py` · 调用点 [`src/jev_trader/jev.py`](https://github.com/Eric-Zhou-0302/jev-A-share-trader/blob/HEAD/src/jev_trader/jev.py)，2026-09-24 阅读</sub>

- **[jev-agent-design-with-topk-logits-choices](https://github.com/6Mikao9/jev-native-agent-with-extended-options)** — 一个原生面向 Jev 的智能体系统研究设计：工具集成、推测性参数提议、外部辅助 logits 等。 <sub>(机翻)</sub>
  <sub>`开源项目` · 6mikao9 · `Py` · 调用点 [`benchmarks/benchmark_jev_latency_breakdown.py`](https://github.com/6Mikao9/jev-native-agent-with-extended-options/blob/HEAD/benchmarks/benchmark_jev_latency_breakdown.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · yuyang2230 · `Py` · 调用点 [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py)，2026-09-22 阅读</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — 独立的 Jev 1.13.0 行为研究：报告、受控提示实验、原始结果与离线验证。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rinnecoder · `Py` · 调用点 [`behavior_study.py`](https://github.com/RINNECODER/jev-behavior-study/blob/HEAD/behavior_study.py)，2026-09-22 阅读</sub>

- **[jev-browse](https://github.com/danielnc/jev-browse)** — 为 browser-harness 提供的辅助函数，让 Claude Code 或 Codex 用一次 fast_run 调用交出整个网站子任务：每一步都由 Jev 决定，必须停下时返回带类型的原因。它移植自 browser-use/jev-ultrafast；作者报告速度快 1.6–3.0 倍、成本低 2.1–5.3 倍。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · danielnc · `Py` · 调用点 [`jev_browse/config.py`](https://github.com/danielnc/jev-browse/blob/HEAD/jev_browse/config.py)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jev-browse](https://github.com/0x7067/jev-browse)** — 以 Jev（TypeSafe）作为决策模型的浏览器自动化。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 0x7067 · `JS` · 调用点 [`bundled/cli.mjs`](https://github.com/0x7067/jev-browse/blob/HEAD/bundled/cli.mjs)，2026-09-24 阅读</sub>

- **[jev-browse](https://github.com/kyrylosyzonenko/jev-browse)** — 驱动真实浏览器，每个决定都由 Jev 做出——点哪里、把你的哪段文字填进哪个输入框、目标何时达成——由 agent-browser 执行操作。 <sub>(机翻)</sub>
  <sub>`开源项目` · kyrylosyzonenko · `JS` · 调用点 [`jev-browse.mjs`](https://github.com/kyrylosyzonenko/jev-browse/blob/HEAD/jev-browse.mjs)，2026-09-24 阅读</sub>

- **[jev-browser](https://github.com/KesavanKing/jev-browser)** — 本地浏览器自动化界面：用 TypeSafe Jev 选择有界的页面操作，只在需要填写字段时才调用文本模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kesavanking · `Py` · 调用点 [`jev_browser/model.py`](https://github.com/KesavanKing/jev-browser/blob/HEAD/jev_browser/model.py)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-browser](https://github.com/MahmoudAdelbghany/jev-browser)** — 由 Jev 驱动、面向 LLM 智能体的浏览器 MCP——约 300 毫秒一次决策，循环中不消耗 LLM token，附与 Playwright MCP 的对比基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · mahmoudadelbghany · `JS` · 调用点 [`src/jev.mjs`](https://github.com/MahmoudAdelbghany/jev-browser/blob/HEAD/src/jev.mjs)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-browser](https://github.com/vinilana/jev-browser)** — 一个混合式浏览器框架：OpenRouter 上的 LLM 把目标拆成可验证的子目标，Jev 选择每一个动作和表单字段，LLM 只在字段需要填写文字时才出场，Playwright 负责执行。 <sub>(机翻)</sub>
  <sub>`开源项目` · vinilana · `TS` · 调用点 [`src/infrastructure/models/jev.ts`](https://github.com/vinilana/jev-browser/blob/HEAD/src/infrastructure/models/jev.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-browser-control](https://github.com/nexibeo/jev-browser-control)** — 让编程智能体控制你自己的 Chrome：扩展加 MCP server。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nexibeo · `JS` · 调用点 [`extension/lib/provider.js`](https://github.com/nexibeo/jev-browser-control/blob/HEAD/extension/lib/provider.js)，2026-09-22 阅读</sub>

- **[jev-browser-local](https://github.com/rorshopping/jev-browser-local)** — 在完全本地的 JEV 式决策引擎上运行 jev-browser（不使用云 API），附显存保护和实测基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · rorshopping · `Py` · 引用文件 [`jev-browser-fork/dist/provider.js`](https://github.com/rorshopping/jev-browser-local/blob/HEAD/jev-browser-fork/dist/provider.js)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — 给浏览器与桌面自动化的有界决策层：只做决策的模型负责选择。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · aidil2105 · `Py` · 调用点 [`src/jev_pilot/providers/jev.py`](https://github.com/aidil2105/jev-browser-pilot/blob/HEAD/src/jev_pilot/providers/jev.py)，2026-09-22 阅读</sub>

- **[jev-browser-skill](https://github.com/zurfyx/jev-browser-skill)** — 让约 100 毫秒的 Jev 决策模型驱动你的浏览器 —— 给 Claude Code 和 Codex 的即插即用技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · zurfyx · `JS` · 调用点 [`scripts/jev.mjs`](https://github.com/zurfyx/jev-browser-skill/blob/HEAD/scripts/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-browser-skill](https://github.com/ChenYCL/jev-browser-skill)** — 为编码智能体提供浏览器与电脑操作，由 TypeSafe Jev 驱动：来自 System One 模型的校准判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · chenycl · `JS` · 调用点 [`skills/jev-browser/lib/typesafe.mjs`](https://github.com/ChenYCL/jev-browser-skill/blob/HEAD/skills/jev-browser/lib/typesafe.mjs)，2026-09-24 阅读</sub>

- **[jev-builder](https://github.com/collapseindex/jev-builder)** — 构建 Jev 请求的网页表单：选模板、填空、复制代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · collapseindex · `JS` · 调用点 [`jev-builder-core.js`](https://github.com/collapseindex/jev-builder/blob/HEAD/jev-builder-core.js)，2026-09-22 阅读</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · nikkoxgonzales · `Py` · 调用点 [`jev_certify/analysis.py`](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py)，2026-09-22 阅读</sub>

- **[jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** — 带 JEV 模型路由、上下文优化与看板自动化的 Codex 覆盖层。 <sub>(机翻)</sub>
  <sub>`插件` · charlyhno-eng · `TS` · `choice` · `score` · `noul` · 调用点 [`src/core/hooks/jev-client.ts`](https://github.com/Charlyhno-eng/jev-codex-pilot/blob/HEAD/src/core/hooks/jev-client.ts)，2026-09-24 阅读</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — 从不做摘要的 Hermes 会话上下文压缩：每次工具调用都被打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · picaye · `JS` · 调用点 [`hermes-compact.mjs`](https://github.com/picaye/jev-compaction/blob/HEAD/hermes-compact.mjs)，2026-09-22 阅读</sub>

- **[jev-connect4](https://github.com/hazlema/jev-connect4)** — 四子棋：Jev 对人，或 Jev 对 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hazlema · `TS` · 调用点 [`src/jev-client.ts`](https://github.com/hazlema/jev-connect4/blob/HEAD/src/jev-client.ts)，2026-09-24 阅读</sub>

- **[jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks)** — JEV 在 MetaTool、When2Call 与 BFCL V4 上的决策基准结果，附双语表格和可复现报告。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · baibizhe · `Py` · 调用点 [`scripts/build_tables.py`](https://github.com/baibizhe/jev-decision-benchmarks/blob/HEAD/scripts/build_tables.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-flappy-bird](https://github.com/hosseintoussi/jev-flappy-bird)** — TypeSafe Jev 模型玩 Flappy Bird 的实时演示，每次只决定一件事：扇翅还是等待。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hosseintoussi · `TS` · 调用点 [`server/jev.ts`](https://github.com/hosseintoussi/jev-flappy-bird/blob/HEAD/server/jev.ts)，2026-09-24 阅读</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · foadsf · `Py` · 调用点 [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/HEAD/jev.py)，2026-09-22 阅读</sub>

- **[jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa)** — 证据驱动的前端 QA，构建在 Jev Ultrafast 与浏览器 harness 之上。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · nainish-rai · `Py` · 调用点 [`src/jev_frontend_qa/core/model_client.py`](https://github.com/Nainish-Rai/jev-frontend-qa/blob/HEAD/src/jev_frontend_qa/core/model_client.py)，2026-09-22 阅读</sub>

- **[jev-harness-router](https://github.com/JoacoMarc/jev-harness-router)** — 面向智能体框架的逐轮路由器：一次约 350 毫秒的 Jev 调用选出模型档位、推理力度、工具与技能，并有硬性兜底。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · joacomarc · `TS` · 调用点 [`src/jev.ts`](https://github.com/JoacoMarc/jev-harness-router/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[jev-in-codex](https://github.com/teempai/jev-in-codex)** — 通过 MCP 为 Codex 提供由 Jev 驱动的工具与技能选择、上下文搜索和输出分诊。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · teempai · `TS` · 调用点 [`src/labelling.ts`](https://github.com/teempai/jev-in-codex/blob/HEAD/src/labelling.ts)，2026-09-24 阅读</sub>

- **[jev-kit](https://github.com/jonathanavis96/jev-kit)** — 一套 Claude Code 工具包：PreToolUse 守卫先用免费的代码预筛放行约 93% 的工具调用，其余交给 Jev 判断（放行、警告、改写或拦截，出错时默认放行）；还能为子 Agent 选择合适的规格，并把 Jev 接入文件搜索、浏览和代码审阅。作者报告浏览器任务 9/9 成功，Claude 花费仅 0.0008 美元。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · jonathanavis96 · `Py` · `choice` · `noul` · 调用点 [`vendor/jev-ultrafast/jev_ultrafast/model.py`](https://github.com/jonathanavis96/jev-kit/blob/HEAD/vendor/jev-ultrafast/jev_ultrafast/model.py)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jev-lab](https://github.com/jammaru/jev-lab)** — 100 个 AI NPC 住在一个小镇里：Jev 选择下一步动作，世界自己写故事。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jammaru · `TS` · 调用点 [`apps/shogi-server/src/jev.ts`](https://github.com/jammaru/jev-lab/blob/HEAD/apps/shogi-server/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-layer](https://github.com/typakon4/jev-layer)** — 可移植的 System-1 决策层，面向智能体 harness，含宿主自控路由、凭据与回放。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · typakon4 · `JS` · 调用点 [`src/providers/typesafe.mjs`](https://github.com/typakon4/jev-layer/blob/HEAD/src/providers/typesafe.mjs)，2026-09-22 阅读</sub>

- **[jev-life](https://github.com/ARCJ137442/jev-life)** — 生命棋 × Jev：一款实验性游戏——写一套新规则，然后看决策模型来下。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arcj137442 · `TS` · 调用点 [`src/client/api.ts`](https://github.com/ARCJ137442/jev-life/blob/HEAD/src/client/api.ts)，2026-09-24 阅读</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — 以基准驱动的 Jev 路由器与评判者，服务于成本可控的 LLM 编程流程。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · erendikmenn · `Py` · 调用点 [`src/jev_router/providers/review.py`](https://github.com/erendikmenn/jev-llm-router-benchmark/blob/HEAD/src/jev_router/providers/review.py)，2026-09-22 阅读</sub>

- **[jev-market-reflex](https://github.com/zzsong1023/jev-market-reflex)** — 用 TypeSafe AI Jev 在实时加密市场上做快速的类型化决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · zzsong1023 · `TS` · 调用点 [`src/jev.ts`](https://github.com/zzsong1023/jev-market-reflex/blob/HEAD/src/jev.ts)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-mobile](https://github.com/xinwang-nwpu/jev-mobile)** — 在无障碍树上每一步做一次 TypeSafe Jev 决策，通过 ADB 执行。不需要截图，速度极快。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · xinwang-nwpu · `Py` · 调用点 [`jev_mobile/model.py`](https://github.com/xinwang-nwpu/jev-mobile/blob/HEAD/jev_mobile/model.py)，2026-09-24 阅读</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — OpenAI 兼容代理，夹在你的 LLM 与用户之间，逐窗口评估输出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · thanh-mathieu95 · `JS` · 调用点 [`evaluator.js`](https://github.com/Thanh-Mathieu95/jev-model-tokengate/blob/HEAD/evaluator.js)，2026-09-22 阅读</sub>

- **[jev-physical-ai](https://github.com/robokrunch/jev-physical-ai)** — 把 Jev 用在机器人、机群与边缘硬件上 —— 附真实实测数字。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · robokrunch · `Py` · 调用点 [`code/demo-a.py`](https://github.com/robokrunch/jev-physical-ai/blob/HEAD/code/demo-a.py)，2026-09-22 阅读</sub>

- **[jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong)** — 让 Jev 实时玩浏览器乒乓球：结构化遥测与类型化决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · icohen007 · `JS` · 调用点 [`src/typesafe.mjs`](https://github.com/Icohen007/jev-play-ping-pong/blob/HEAD/src/typesafe.mjs)，2026-09-22 阅读</sub>

- **[jev-playground](https://github.com/hegargarcia/jev-playground)** — 在状态明确、合法动作清晰的游戏里，把 Jev 与其他评估模型做对比：规则和状态转移由代码掌控，每个模型选择下一步动作，结果可测量。 <sub>(机翻)</sub>
  <sub>`基准测试` · hegargarcia · `TS` · 调用点 [`src/app/api/connect-four/move/route.ts`](https://github.com/hegargarcia/jev-playground/blob/HEAD/src/app/api/connect-four/move/route.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-plays](https://github.com/mansicer/jev-plays)** — 由 System One 模型玩 Craftax，LLM 负责设定目标：同一张地图上的五种智能体，从 Jev 直接操作原始动作到 LLM 控制每一步，用记录下来的对局进行比较。 <sub>(机翻)</sub>
  <sub>`基准测试` · mansicer · `Py` · 调用点 [`craftax_agent/jev_policy.py`](https://github.com/mansicer/jev-plays/blob/HEAD/craftax_agent/jev_policy.py)，2026-09-24 阅读</sub>

- **[jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red)** — 在 PyBoy 上玩《宝可梦 红》：路线和算术交给代码，Jev 在分叉点约 100 毫秒做出选择，校准是实测的而不是假设的。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · valentynkit · `Py` · 调用点 [`src/jpp/policy.py`](https://github.com/valentynkit/jev-plays-pokemon-red/blob/HEAD/src/jpp/policy.py)，2026-09-24 阅读</sub>

- **[jev-pong](https://github.com/ably-labs/jev-pong)** — 一个每次模型决策球才走一步的乒乓游戏：Jev 对阵多个 LLM，经由 Vercel AI Gateway。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ably-labs · `TS` · 调用点 [`lib/compare/compare-models.ts`](https://github.com/ably-labs/jev-pong/blob/HEAD/lib/compare/compare-models.ts)，2026-09-24 阅读</sub>

- **[jev-ra](https://github.com/brnyxx/jev-ra)** — 给编程智能体的浏览器操作，号称比 browser-use 快 3–5 倍：每一步由 Jev 决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · brnyxx · `Py` · 调用点 [`jev_ra/config.py`](https://github.com/brnyxx/jev-ra/blob/HEAD/jev_ra/config.py)，2026-09-22 阅读</sub>

- **[jev-robotics-demo](https://github.com/FazalAAli/jev-robotics-demo)** — Jev 对比某大模型：在 MuJoCo 里驾驶仿真机械臂。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · fazalaali · `Py` · 调用点 [`jev_agent.py`](https://github.com/FazalAAli/jev-robotics-demo/blob/HEAD/jev_agent.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-routing](https://github.com/nekowasabi/jev-routing)** — 给多个编程智能体的 Go 版 Jev harness，不依赖 npx，也不是 MCP server。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nekowasabi · `Go` · 调用点 [`internal/jev/jev.go`](https://github.com/nekowasabi/jev-routing/blob/HEAD/internal/jev/jev.go)，2026-09-22 阅读 · ⚠ `已归档`</sub>

- **[jev-skill-router](https://github.com/himomohi/jev-skill-router)** — 把技能目录放在主 LLM 上下文之外：Jev 通过一个只读 MCP 工具挑选相关技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · himomohi · `Py` · 调用点 [`src/jev_skill_router/jev.py`](https://github.com/himomohi/jev-skill-router/blob/HEAD/src/jev_skill_router/jev.py)，2026-09-24 阅读</sub>

- **[jev-skill-scout](https://github.com/karanb192/jev-skill-scout)** — 找出 Claude Code 本该加载你的某个技能却没有加载的那些回合，由 TypeSafe 的 Jev 判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · karanb192 · `JS` · 调用点 [`lib/scout.js`](https://github.com/karanb192/jev-skill-scout/blob/HEAD/lib/scout.js)，2026-09-24 阅读</sub>

- **[jev-skills](https://github.com/eran-broder/jev-skills)** — 没有“上下文税”的技能：Claude Code 与 Codex 插件，由 TypeSafe 的 Jev 在每一轮决定模型需要哪些技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · eran-broder · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/eran-broder/jev-skills/blob/HEAD/src/jev/client.ts)，2026-09-24 阅读</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · hamakyo · `TS` · 调用点 [`src/providers/jev-provider.ts`](https://github.com/hamakyo/jev-starter/blob/HEAD/src/providers/jev-provider.ts)，2026-09-22 阅读</sub>

- **[jev-table-tennis](https://github.com/LiuHao-1443/jev-table-tennis)** — 与 TypeSafe 的 Jev（System One）打乒乓球。右侧球拍的每一次移动都是实时的模型决策，没有本地预测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · liuhao-1443 · `Py` · 调用点 [`jev_eval_compare.py`](https://github.com/LiuHao-1443/jev-table-tennis/blob/HEAD/jev_eval_compare.py)，2026-09-24 阅读</sub>

- **[jev-tetris](https://github.com/MachineLearning-Nerd/jev-tetris)** — 一个可视化的 TypeSafe 演示：由 Jev 选择经过校验的俄罗斯方块落点。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · machinelearning-nerd · `Py` · 调用点 [`courtroom.py`](https://github.com/MachineLearning-Nerd/jev-tetris/blob/HEAD/courtroom.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-tetris](https://github.com/thelau/jev-tetris)** — 由判断模型来玩的俄罗斯方块：代码找出方块所有可能的落点，并把每一种写成一句话，交给 JEV 选择。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · thelau · `JS` · 调用点 [`src/jev.js`](https://github.com/thelau/jev-tetris/blob/HEAD/src/jev.js)，2026-09-24 阅读</sub>

- **[jev-tool-router](https://github.com/jackbarunz/jev-tool-router)** — 给 Codex 的 Jev 驱动 MCP 工具路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · jackbarunz · `JS` · 调用点 [`scripts/setup-codex.mjs`](https://github.com/jackbarunz/jev-tool-router/blob/HEAD/scripts/setup-codex.mjs)，2026-09-22 阅读</sub>

- **[jev-turbo](https://github.com/sightmap/jev-turbo)** — 由 Jev 驱动的语义化浏览器操作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · sightmap · `Go` · 调用点 [`explore/jev.go`](https://github.com/sightmap/jev-turbo/blob/HEAD/explore/jev.go)，2026-09-22 阅读</sub>

- **[jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control)** — 用语音控制 Mac：语音 → Jev 类型化决策 → macOS 自动化。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · chris-wozniczek · `Swift` · 调用点 [`Sources/JevVoice/Agent/JevStepPlanner.swift`](https://github.com/chris-wozniczek/jev-voice-control/blob/HEAD/Sources/JevVoice/Agent/JevStepPlanner.swift)，2026-09-22 阅读</sub>

- **[jev-windows-voice](https://github.com/mstf-svndk/jev-windows-voice)** — 用土耳其语或英语自然对话来控制 Windows 10/11 电脑：结合 OpenAI Realtime、本地 Whisper、Jev 与 UI Automation。 <sub>(机翻)</sub>
  <sub>`开源项目` · mstf-svndk · `JS` · 调用点 [`src/jev.js`](https://github.com/mstf-svndk/jev-windows-voice/blob/HEAD/src/jev.js)，2026-09-24 阅读</sub>

- **[jev-zork](https://github.com/Resadan-dev/jev-zork)** — Jev（TypeSafe System One）玩《魔域》：每一步在 Jericho 给出的合法动作中做一次 Choice，并显示其置信度。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · resadan-dev · `Py` · 调用点 [`src/jev_zork/judges.py`](https://github.com/Resadan-dev/jev-zork/blob/HEAD/src/jev_zork/judges.py)，2026-09-24 阅读</sub>

- **[jev2048](https://github.com/erhanmeydan/jev2048)** — TypeSafe 的 Jev 决策模型在一个真实的在线 2048 网站上玩游戏：每一步一次 API 调用，只需一个 key。 <sub>(机翻)</sub>
  <sub>`开源项目` · erhanmeydan · `Py` · 调用点 [`jev2048/model.py`](https://github.com/erhanmeydan/jev2048/blob/HEAD/jev2048/model.py)，2026-09-24 阅读</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — 先评估再信任：实战笔记、可运行脚本与一个 agent 技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · elshinq · `JS` · 调用点 [`scripts/jev.mjs`](https://github.com/ElshinQ/jevaluate/blob/HEAD/scripts/jev.mjs)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jevarena](https://github.com/raihankhan-rk/jevarena)** — JevArena：两个 Jev 智能体在仅可点击的浏览器游戏里对决。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · raihankhan-rk · `TS` · 调用点 [`lib/server/jev.ts`](https://github.com/raihankhan-rk/jevarena/blob/HEAD/lib/server/jev.ts)，2026-09-22 阅读</sub>

- **[jevball](https://github.com/atarikcaliskan/jevball)** — 22 个 Jev 模型，一颗球：一场 3D 足球赛，每名球员都是一个独立的 Jev（TypeSafe AI System One）决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · atarikcaliskan · `JS` · 调用点 [`server/jev.js`](https://github.com/atarikcaliskan/jevball/blob/HEAD/server/jev.js)，2026-09-24 阅读</sub>

- **[jevcumber](https://github.com/RubyBrewsday/jevcumber)** — 只写 .feature 文件就能写 Cucumber 测试：无需步骤定义，由 Jev（TypeSafe AI）解析每一个 Gherkin 步骤。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rubybrewsday · `TS` · 调用点 [`src/resolver.ts`](https://github.com/RubyBrewsday/jevcumber/blob/HEAD/src/resolver.ts)，2026-09-24 阅读</sub>

- **[jevdroid](https://github.com/antiyro/jevdroid)** — 用 Jev 通过 ADB 控制 Android 的类型化 Python 框架。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · antiyro · `Py` · 调用点 [`src/jevdroid/providers/http.py`](https://github.com/antiyro/jevdroid/blob/HEAD/src/jevdroid/providers/http.py)，2026-09-22 阅读</sub>

- **[jevex](https://github.com/jvsteiner/jevex)** — 一个最小化的智能体：由 Jev 主导循环，LangChain 聊天模型只负责填写参数和最终回复；背后是三个本地 MCP 服务器、十二个可用工具。 <sub>(机翻)</sub>
  <sub>`开源项目` · jvsteiner · `Py` · 调用点 [`src/jevex/benchmark.py`](https://github.com/jvsteiner/jevex/blob/HEAD/src/jevex/benchmark.py)，2026-09-24 阅读</sub>

- **[jevloop](https://github.com/parkavenue9639/jevloop)** — 由 Jev 驱动的通用智能体框架，追求更快、更低成本的执行，并内置与纯 LLM 智能体的并排对比实验。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · parkavenue9639 · `Py` · 调用点 [`backend/jevloop/decision/model.py`](https://github.com/parkavenue9639/jevloop/blob/HEAD/backend/jevloop/decision/model.py)，2026-09-24 阅读</sub>

- **[jevnav](https://github.com/dtduc-git/jevnav)** — 为浏览器智能体提供“页面真相”，以及可回放、可测试、可审计的决策。Jev 选择元素，高风险操作需要把关。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dtduc-git · `Py` · 调用点 [`src/jevnav/decide.py`](https://github.com/dtduc-git/jevnav/blob/HEAD/src/jevnav/decide.py)，2026-09-24 阅读</sub>

- **[jevonly](https://github.com/buluoray/JevOnly)** — 纯 Jev 驱动的智能体：能「打字」并推进任务直至完成。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · buluoray · `Py` · 调用点 [`src/jevonly/core/jev.py`](https://github.com/buluoray/JevOnly/blob/HEAD/src/jevonly/core/jev.py)，2026-09-22 阅读</sub>

- **[Jevry](https://github.com/michaelswissa/jevry)** — 一款开源桌面浏览器，可根据自然语言任务操作网站：文本模型负责规划，Jev 用 choice 从浏览器真正能执行的动作中挑选每一步（绝不生成 JavaScript 或选择器），Chromium 执行，步骤可见并可随时停止。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · michaelswissa · `TS` · `choice` · 调用点 [`desktop/jev-direct-plan.ts`](https://github.com/michaelswissa/jevry/blob/HEAD/desktop/jev-direct-plan.ts)，2026-10-24 模型阅读</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — 亚 100 毫秒的智能体工具调用安全闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lgy1027 · `Py` · 调用点 [`jevshield/client.py`](https://github.com/lgy1027/jevshield/blob/HEAD/jevshield/client.py)，2026-09-22 阅读</sub>

- **[JevTest](https://github.com/CorieW/JevTest)** — 用 Jev 做有边界的探索式浏览器测试，配合确定性断言和可回放的证据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · coriew · `TS` · 调用点 [`src/jev.ts`](https://github.com/CorieW/JevTest/blob/HEAD/src/jev.ts)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[langchain-skill-router](https://github.com/deyna256/langchain-skill-router)** — 为 LangChain 与 deepagents 智能体按轮选择技能：由快速的裁判挑出本轮需要的少数技能，让上百个技能的目录不必塞进提示词。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · deyna256 · `Py` · 调用点 [`src/langchain_skill_router/providers/jev.py`](https://github.com/deyna256/langchain-skill-router/blob/HEAD/src/langchain_skill_router/providers/jev.py)，2026-09-24 阅读</sub>

- **[macos-computer-use-kit](https://github.com/Sur-Cai/macos-computer-use-kit)** — 面向 macOS AI 智能体的、以辅助功能为先的电脑操作工具包，可选配 Jev（TypeSafe System One）语义护栏。 <sub>(机翻)</sub>
  <sub>`插件` · sur-cai · `Py` · 调用点 [`src/macos_computer_use/jev.py`](https://github.com/Sur-Cai/macos-computer-use-kit/blob/HEAD/src/macos_computer_use/jev.py)，2026-09-24 阅读</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — 给 Codex 与 Claude Code 的二值批准闸门：每次被拦截的工具调用都要审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · alexj11324 · `Go` · 引用文件 [`internal/jev/client.go`](https://github.com/alexj11324/open-jev-approvals/blob/HEAD/internal/jev/client.go)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[otto](https://github.com/NobleSpartan6/otto)** — 面向 macOS 与 Windows 的开源原生 computer use：Jev 加本地 OCR。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · noblespartan6 · `TS` · 调用点 [`core/typesafe.ts`](https://github.com/NobleSpartan6/otto/blob/HEAD/core/typesafe.ts)，2026-09-22 阅读</sub>

- **[pi-Jev-browser](https://github.com/laihenyi/pi-Jev-browser)** — 面向 pi 的浏览器与 macOS 桌面智能体：Jev（TypeSafe System One）根据结构化观察选择每一个动作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · laihenyi · `TS` · 调用点 [`src/policy.ts`](https://github.com/laihenyi/pi-Jev-browser/blob/HEAD/src/policy.ts)，2026-09-24 阅读</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · legacybridge-tech · `TS` · 调用点 [`src/client.ts`](https://github.com/legacybridge-tech/pi-typesafe-jev/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[pijev](https://github.com/tonyzdev/pijev)** — PiJev：Jev 参与循环的终端编码智能体——在第一次调用前由 Jev 给仓库文件排序，并挑选技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tonyzdev · `TS` · 调用点 [`src/jev.ts`](https://github.com/tonyzdev/pijev/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[ps2-ai-agent](https://github.com/opaielsheikh/ps2-ai-agent)** — 自主的 PS2 AI 智能体，带实时视觉遥测 HUD。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · opaielsheikh · `Py` · 调用点 [`agent_bridge.py`](https://github.com/opaielsheikh/ps2-ai-agent/blob/HEAD/agent_bridge.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[reflex](https://github.com/kaustav1996/reflex)** — 构建在 Pi 编码智能体之上的编码助手与个人助理，拥有 System One 式的“条件反射”（TypeSafe Jev）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · kaustav1996 · `TS` · 调用点 [`src/extensions/typesafe/provider.ts`](https://github.com/kaustav1996/reflex/blob/HEAD/src/extensions/typesafe/provider.ts)，2026-09-24 阅读</sub>

- **[robo-harness](https://github.com/grmkris/robo-harness)** — SO-101 机械臂智能体工作台：Bun/Effect 协调器、React 工作台、Python 电机控制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · grmkris · `TS` · 调用点 [`apps/server/src/decision/jev.ts`](https://github.com/grmkris/robo-harness/blob/HEAD/apps/server/src/decision/jev.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[roverlab](https://github.com/juancamiloqhz/roverlab)** — 一个 3D 行星探测车沙盒，用来试验由 TypeSafe AI 做出的自主决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · juancamiloqhz · `TS` · 调用点 [`server/decisions.ts`](https://github.com/juancamiloqhz/roverlab/blob/HEAD/server/decisions.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[rpg-jev](https://github.com/lmvdz/rpg-jev)** — 一款活的世界 RPG，NPC 的行为由 TypeSafe 的 Jev 判断模型决定；规则、数值与状态由代码掌控。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lmvdz · `TS` · 调用点 [`spikes/m0-jev/src/run.ts`](https://github.com/lmvdz/rpg-jev/blob/HEAD/spikes/m0-jev/src/run.ts)，2026-09-24 阅读 · ⚠ `无许可证` `已归档`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One 搜索：用类型化判断与仓库证据导航与追踪代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cpaczek · `TS` · 调用点 [`src/client.ts`](https://github.com/cpaczek/s1s/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[slidepilot](https://github.com/harshil1712/slidepilot)** — 给 Slidev 做的语音驱动语义自动翻页，由 Cloudflare Agents 与 Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · harshil1712 · `TS` · 调用点 [`apps/worker/src/decision.ts`](https://github.com/harshil1712/slidepilot/blob/HEAD/apps/worker/src/decision.ts)，2026-09-22 阅读</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — 由并行 Jev 判断控制的贪吃蛇，每个游戏 tick 一次 API 调用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · siroccomask · `Py` · 调用点 [`jev_controller.py`](https://github.com/siroccomask/snake-jev/blob/HEAD/jev_controller.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — 智能体的每一次工具调用在执行前都过一遍检查的 Claude Code 插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · getexcited · `TS` · 调用点 [`lib/jev.ts`](https://github.com/getexcited/stepwarden/blob/HEAD/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[swarmrouter](https://github.com/ndolinschi/swarmrouter)** — 用 Jev 把任务路由给研究／编码／浏览／客服／写作智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/swarmrouter/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[terrarium](https://github.com/TheGali/terrarium)** — 一个沙盒：System One 模型按下小生物的操控键，代码负责其余。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · thegali · `JS` · 调用点 [`bench/run-jev.mjs`](https://github.com/TheGali/terrarium/blob/HEAD/bench/run-jev.mjs)，2026-09-22 阅读</sub>

- **[tictacjev](https://github.com/darthblanc/tictacjev)** — 一个井字棋应用，其中一方是 TypeSafe AI 的 System One 模型 Jev，并实时显示置信度与概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · darthblanc · `TS` · 调用点 [`backend/app/jev_client.py`](https://github.com/darthblanc/tictacjev/blob/HEAD/backend/app/jev_client.py)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[tsai-civ2](https://github.com/phyous/tsai-civ2)** — 让 Jev 在浏览器里玩初代《文明 II》，实时展示动作概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · phyous · `Py` · 调用点 [`civ2/typesafe.py`](https://github.com/phyous/tsai-civ2/blob/HEAD/civ2/typesafe.py)，2026-09-22 阅读</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — 智能体工具调用执行前防火墙的影子模式验证 harness。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · anshchoudhary · `Py` · 调用点 [`firewall/judge.py`](https://github.com/AnshChoudhary/typesafe-ai-firewall/blob/HEAD/firewall/judge.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-ai-trading-showcase](https://github.com/JordiParraCrespo/typesafe-ai-trading-showcase)** — 实时展示 BTC、ETH 和 XRP 价格，并基于最近一分钟的真实成交，演示由 TypeSafe 做出的“买入或等待”判断。不会真的下单。 <sub>(机翻)</sub>
  <sub>`开源项目` · jordiparracrespo · `TS` · 调用点 [`lib/market.ts`](https://github.com/JordiParraCrespo/typesafe-ai-trading-showcase/blob/HEAD/lib/market.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-chess](https://github.com/Dimesio/typesafe-chess)** — 一个有趣的小实验：让 TypeSafe AI 的 Jev 模型和 Stockfish 下国际象棋。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dimesio · `JS` · 调用点 [`server/jev.js`](https://github.com/Dimesio/typesafe-chess/blob/HEAD/server/jev.js)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo)** — Three.js 无人机模拟器，Python 后端加 Jev 实时导航。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kxzk · `Py` · 调用点 [`backend/jev.py`](https://github.com/kxzk/typesafe-jev-drone-demo/blob/HEAD/backend/jev.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[typesafe-minecraft-demo](https://github.com/ellistev/typesafe-minecraft-demo)** — 由 TypeSafe AI 控制的 Minecraft Java 版玩家：实时决策、建造加拿大国旗，并配有并排的数据看板。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ellistev · `JS` · 调用点 [`src/decisions.cjs`](https://github.com/ellistev/typesafe-minecraft-demo/blob/HEAD/src/decisions.cjs)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[ui-generator-instinct-jev](https://github.com/joevidev/ui-generator-instinct-jev)** — 把 Jev 当作界面生成器：用自由文本描述需求，Jev 只回答基于真实选项集合的类型化问题，挑选并配置真实的 shadcn/ui 组件或页面块，从不生成代码或文案。 <sub>(机翻)</sub>
  <sub>`开源项目` · joevidev · `TS` · 调用点 [`lib/typesafe-client.ts`](https://github.com/joevidev/ui-generator-instinct-jev/blob/HEAD/lib/typesafe-client.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)** — 把 Jev 接到 Browser Use 上，驱动一个浏览器自动化智能体。
  <sub>`视频` · AICodeKing · ⚠ `宣称未核实`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
