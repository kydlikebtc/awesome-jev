# 安全闸门

<sub>[awesome-jev](../../README.zh-CN.md) · [English](safety-gating.md)</sub>

_在执行前判断一个动作是否安全。属纵深防御，绝不是安全边界。_

这个决策的全部已收录例子 —— 共 142 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#安全闸门)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#safety-gating)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#safety-gating)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 2 · 调用点 136 · 接口形态 2 · 仅示例 0 · 独立报告 10 · 负面结果 0 · 未引用文件 4。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) <sub>`官方文档` · `Py`</sub>
- [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) <sub>`官方文档` · `Py` · `noul` · `score`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。
  <sub>`平台集成` · ★10k+ · `TS` · `choice` · `score` · `noul` · 调用点 [`libs/providers/langchain-typesafe/src/types.ts`](https://github.com/langchain-ai/langchainjs/blob/HEAD/libs/providers/langchain-typesafe/src/types.ts)，2026-09-22 阅读</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · 调用点 [`scripts/jev-spike.mjs`](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs)，2026-09-22 阅读</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。
  <sub>`开源项目` · ★10k+ · `Go` · `noul` · 调用点 [`backend/internal/pkg/typesafe/client.go`](https://github.com/Wei-Shaw/sub2api/blob/HEAD/backend/internal/pkg/typesafe/client.go)，2026-09-22 阅读</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)** — 三个共用同一严重度量表的 Score 问题，两项以上越线即拦截请求，并且失败时默认关闭。
  <sub>`开源项目` · ★1k+ · `Rs` · `score` · 调用点 [`examples/llm-guardrail-jev/guardrail.ts`](https://github.com/agentgateway/agentgateway/blob/HEAD/examples/llm-guardrail-jev/guardrail.ts)，2026-09-22 阅读</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。
  <sub>`开源项目` · ★1k+ · `TS` · `choice` · `noul` · 调用点 [`src/shared/jevProtocol.ts`](https://github.com/ThinkInAIXYZ/deepchat/blob/HEAD/src/shared/jevProtocol.ts)，2026-09-22 阅读</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — 编程智能体运行时：工作流是带版本的 TypeScript 阶段，包含可执行检查、评审关卡和人工审批。其 AI 包从 models.dev 收录 Jev，作为 5 家提供方上的 System One 决策模型，与聊天模型分开列出；README 没有说明工作流在哪里调用它。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · bastani-inc · `TS` · 调用点 [`packages/ai/src/decision-models.generated.ts`](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts)，2026-09-24 阅读</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)** — Grok Bot 的路由器：在调研、浏览、重试或启动子智能体之前，先问 Jev 这个请求需要哪种动作：复用已缓存的产物、停止失败的重试、运行确定性代码、限制调研规模、允许子智能体，或请人决定。影子模式只记日志；主动模式要靠粘贴进去的技能来执行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · bodila51 · `Py` · 调用点 [`src/jev_client.py`](https://github.com/Bodila51/grok-bot-jev/blob/HEAD/src/jev_client.py)，2026-09-22 阅读</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `noul` · 调用点 [`scripts/jev-decide.mjs`](https://github.com/Sac-Y/Jev-cu/blob/HEAD/scripts/jev-decide.mjs)，2026-09-22 阅读</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。
  <sub>`开源项目` · ★100+ · `Py` · `choice` · `score` · `noul` · 调用点 [`tactics.py`](https://github.com/RomanSlack/jev-drone/blob/HEAD/tactics.py)，2026-09-22 阅读 · ⚠ `宣称未核实`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — 把 Jev 接进编程智能体，用于工具调用的推理判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · vinilana · `TS` · 调用点 [`src/jev.ts`](https://github.com/vinilana/jev-gateway/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给所有编程智能体做的自动模式：结合会话上下文给每次工具调用打风险分（拒绝／询问／放行）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · leepokai · `JS` · 调用点 [`src/jev.js`](https://github.com/leepokai/jev-guard/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts)，2026-09-22 阅读</sub>

- **[jevals](https://github.com/openlayer-ai/jevals)** — 把智能体评测与护栏做成 Jev 决策：每条 trace 一次请求，成本不到一美分的零头。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · openlayer-ai · `Py` · 调用点 [`src/jevals/backends/typesafe.py`](https://github.com/openlayer-ai/jevals/blob/HEAD/src/jevals/backends/typesafe.py)，2026-09-22 阅读</sub>

- **[mu](https://github.com/qybaihe/mu)** — 基于 pi 的编程 Agent（命令行和桌面端），在 38 个决策点上问 Jev：工具输出的哪些片段进上下文、哪些过期的工具结果可以丢掉、被规则拦下的命令是不是用户要的、抓取的网页和 MCP 输出里有没有注入的指令。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · 调用点 [`packages/kyrn-judge/src/providers/typesafe.ts`](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts) · ⚠ `作者自荐`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — 给编程智能体做的决策层：一个可度量的工具调用闸门，外加一个返回校准答案的类型化提问。
  <sub>`插件` · ★100+ · y0usaf · `TS` · 调用点 [`src/client.ts`](https://github.com/y0usaf/pi-jev/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — 统管所有机器人的 CLI：每台机器人配一个 LLM 作大脑，由 Jev 做决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · rokbenko · `Py` · 调用点 [`quackd/agent/decision/systemone.py`](https://github.com/rokbenko/quackd/blob/HEAD/quackd/agent/decision/systemone.py)，2026-09-24 阅读</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — 带 Jev 智能路由的 AI 智能体：把大白话请求分派给合适的专家智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · notque · `Py` · 调用点 [`plugins/jev-auto-compact/hooks/jev-auto-compact.mjs`](https://github.com/notque/vexjoy-agent/blob/HEAD/plugins/jev-auto-compact/hooks/jev-auto-compact.mjs)，2026-09-22 阅读</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — 一个 AI 编程智能体：读代码、改文件、跑命令、推理 bug。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · wrongstack · `TS` · 调用点 [`packages/core/src/typesafe/client.ts`](https://github.com/WrongStack/WrongStack/blob/HEAD/packages/core/src/typesafe/client.ts)，2026-09-22 阅读</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 结合实时音频与字幕检测 YouTube 视频里的赞助片段。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · trungdq88 · `JS` · 调用点 [`extension/lib/jev.js`](https://github.com/trungdq88/youtube-sponsor-detection/blob/HEAD/extension/lib/jev.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · 24601 · `Py` · 调用点 [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md)，2026-09-24 阅读</sub>

- **[bluenoise](https://github.com/rokcso/bluenoise)** — 模糊或隐藏 X 上嘈杂的回复、帖子与广告，并清理界面。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · rokcso · `TS` · 调用点 [`src/contracts/ai.ts`](https://github.com/rokcso/bluenoise/blob/HEAD/src/contracts/ai.ts)，2026-09-22 阅读</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — 为 DeepSeek Harness 中的每一次工具调用提供毫秒级 System-1 判断——由 Jev 驱动的风险分类与证据检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · asktheway · `TS` · 调用点 [`scripts/smoke.mjs`](https://github.com/AskTheWay/dsh-jev-interceptor/blob/HEAD/scripts/smoke.mjs)，2026-09-24 阅读</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — DeepSeek Harness 插件，在工具输出进入上下文之前先问 Jev：长篇读取或抓取结果里哪些段落相关（按排序保留，不卡阈值）；抓回的页面里有没有针对 AI 的指令（概率达到 0.75 时附提醒，内容原样保留）；推荐哪一个技能；以及每条“完成”声明有没有证据。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · horusjiang · `TS` · 调用点 [`src/config.ts`](https://github.com/HorusJiang/dsh-jev-tools/blob/HEAD/src/config.ts)，2026-09-24 阅读</sub>

- **[flue-jev-demo](https://github.com/matthewp/flue-jev-demo)** — 通过 Cloudflare AI Gateway 用 Jev 做 Flue 智能体路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · matthewp · `TS` · 调用点 [`src/flue-jev.ts`](https://github.com/matthewp/flue-jev-demo/blob/HEAD/src/flue-jev.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · keeltrace · `Py` · 调用点 [`hermes_nerve/client.py`](https://github.com/keeltrace/hermes-nerve/blob/HEAD/hermes_nerve/client.py)，2026-09-22 阅读</sub>

- **[is-malicious](https://github.com/luantak/is-malicious)** — 代码库扫描器，帮你避免运行恶意代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · luantak · `TS` · 调用点 [`src/jev.ts`](https://github.com/luantak/is-malicious/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code 的 Stop 钩子：在未经验证的“完成”之前拦下——读取会话记录找证据，只问 Jev 一次，其余情况一律放行。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · valentynkit · `JS` · 调用点 [`belay.mjs`](https://github.com/valentynkit/jev-belay/blob/HEAD/belay.mjs)，2026-09-24 阅读</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — 面向类型化决策模型的概率感知评测：校准度、选择性风险、延迟，以及可复现的基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · abdelstark · `Py` · 调用点 [`src/jev_benchmarks/adapters/jev.py`](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/src/jev_benchmarks/adapters/jev.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — 在 DSPy 工作流中对 Jev 决策做可复现的校准与选择性风险基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · jmanhype · `Py` · 调用点 [`src/jev_dspy_lab/live.py`](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/src/jev_dspy_lab/live.py)，2026-09-22 阅读</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — Claude Code 的 PreToolUse 门禁：先用正则硬规则和只读白名单，再用一个 Noul 和一个 Choice 判定放行、询问或拒绝，明确安全的命令无需权限确认。附 Codex、Cursor、OpenCode 适配和 review-router GitHub Action。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · eugeniughelbur · `Py` · `noul` · `choice` · 调用点 [`jev_gate.py`](https://github.com/eugeniughelbur/jev-engineering/blob/HEAD/jev_gate.py)，2026-09-28 阅读 · ⚠ `作者自荐`</sub>

- **[jev-guard](https://github.com/klauswg/jev-guard)** — 面向交易所充值与提现的实时风险分诊网关——Jev（TypeSafe System One）只负责分诊，裁决另有机制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · klauswg · `Java` · 调用点 [`src/main/java/com/jevguard/eval/EvalRunner.java`](https://github.com/klauswg/jev-guard/blob/HEAD/src/main/java/com/jevguard/eval/EvalRunner.java)，2026-09-24 阅读</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · antoniocoppe · `TS` · 调用点 [`demos/proof/row-filter/run.ts`](https://github.com/AntonioCoppe/jev-harness/blob/HEAD/demos/proof/row-filter/run.ts)，2026-09-22 阅读</sub>

- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)** — 面向 AI 编码智能体的决策关卡，提供 CLI、MCP 服务器、CI 钩子以及 Python、TypeScript 和 Rust SDK：先用离线启发式规则，再可选地交给 Jev 判断：失败的测试日志是否需要动用 LLM、是否中止反复修改的循环、该用哪个模型档位和推理力度、某一步是否已完成。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · ismaelsoilet · `Py` · 调用点 [`src/jev_harness/client.py`](https://github.com/ismaelsoilet/jev-harness/blob/HEAD/src/jev_harness/client.py)，2026-09-24 阅读</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 面向 Apple 芯片上原生 macOS 应用的 computer use 智能体：由 OmniParser CoreML、Apple Vision OCR 和辅助功能标签在本机找出窗口里的控件，再由 Jev 根据观察到的文字（从不看像素）用 choice 选下一步动作。输入前有防护检查，基准测试核对的是实际结果，而不是 Jev 的 DONE 判断。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jcpsimmons · `JS` · 调用点 [`src/providers.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs)，2026-09-22 阅读</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★10+ · brainstormity · `Py` · `choice` · `noul` · 调用点 [`typesafe/__init__.py`](https://github.com/brainstormity/Jev-Moderation-Bot/blob/HEAD/typesafe/__init__.py)，2026-09-22 阅读</sub>

- **[jev-runtime-security](https://github.com/ringzerosec/jev-runtime-security)** — 面向 AI 编码智能体的运行时安全：策略在内核的系统调用层强制执行，位于智能体及其所写的一切之下，模糊情况交给 Jev 判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ringzerosec · `Rs` · 调用点 [`agent/src/scanner/jev_layer.rs`](https://github.com/ringzerosec/jev-runtime-security/blob/HEAD/agent/src/scanner/jev_layer.rs)，2026-09-24 阅读</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 的可疑行为，结合静态证据并明确标注覆盖范围。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · win4r · `Py` · 调用点 [`scripts/jev_client.py`](https://github.com/win4r/jev-security-scan/blob/HEAD/scripts/jev_client.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-sentinel](https://github.com/harshwasan/jev-sentinel)** — Pi 编码智能体扩展：用 TypeSafe Jev 检查工具调用、工具输出和回复（提示注入、审批、敏感信息等）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · harshwasan · `TS` · 调用点 [`src/guard.ts`](https://github.com/harshwasan/jev-sentinel/blob/HEAD/src/guard.ts)，2026-09-24 阅读</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — 生产级的 Jev 用例 harness，带置信度门控的决策逻辑。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kenhuangus · `Py` · 调用点 [`src/jev_usecases/client.py`](https://github.com/kenhuangus/jev-usecases/blob/HEAD/src/jev_usecases/client.py)，2026-09-22 阅读</sub>

- **[jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot)** — 基于 grammY 的极简 Telegram 反垃圾机器人。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · backmeupplz · `TS` · 调用点 [`src/spam.ts`](https://github.com/backmeupplz/jev_antispam_bot/blob/HEAD/src/spam.ts)，2026-09-22 阅读</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — 由 Jev 自动完成的 PR 风险审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · hexyedev · `Py` · 调用点 [`src/JevPR/providers/jev.py`](https://github.com/HexyeDEV/JevPR/blob/HEAD/src/JevPR/providers/jev.py)，2026-09-24 阅读</sub>

- **[muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook)** — 为 Muse 提供的 Jev 决策层：在昂贵的智能体工作之前加一道快速、便宜的 TypeSafe AI 关卡——置信度策略与配方。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · bodila51 · `Py` · 调用点 [`src/jev_client.py`](https://github.com/Bodila51/muse-jev-playbook/blob/HEAD/src/jev_client.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — 用 Jev 做拦截、引导与「模糊 lint」，让智能体遵守你的规则与约定。含 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tyler-dot-earth · `TS` · 调用点 [`apps/patdown/src/typesafe-judge.ts`](https://github.com/tyler-dot-earth/patdown/blob/HEAD/apps/patdown/src/typesafe-judge.ts)，2026-09-22 阅读</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — 通过 Vercel AI Gateway 为 Pi 做自动模型路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · mejiasd3v · `JS` · 调用点 [`index.ts`](https://github.com/mejiasd3v/pi-jev-router/blob/HEAD/index.ts)，2026-09-22 阅读</sub>

- **[pi-verdict](https://github.com/jesset/pi-verdict)** — 给 Pi 的最小权限闸门，仿照 Claude Code 的自动模式。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · jesset · `TS` · 调用点 [`extensions/jev-adapter.ts`](https://github.com/jesset/pi-verdict/blob/HEAD/extensions/jev-adapter.ts)，2026-09-22 阅读</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — 面向 AI 智能体的开源自动模式：一个校准过的工具调用防火墙。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · riskaversetech · `TS` · 调用点 [`src/backends/typesafe.ts`](https://github.com/RiskAverseTech/toolgate/blob/HEAD/src/backends/typesafe.ts)，2026-09-22 阅读</sub>

- **[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)** — 开源的智能体工具调用授权网关：确定性策略加 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · omkarghugarkar007 · `TS` · 调用点 [`packages/decision-provider/src/typesafe-jev.ts`](https://github.com/omkarghugarkar007/actiongate-jev/blob/HEAD/packages/decision-provider/src/typesafe-jev.ts)，2026-09-22 阅读</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · abhishekswe · `TS` · 调用点 [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts)，2026-09-22 阅读</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — 可复用的 GitHub Action：由检查、AI 审查者与 Jev 共同把关的智能体修复循环。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ripwords · `TS` · 调用点 [`src/jev.ts`](https://github.com/Ripwords/agent-gate-loop/blob/HEAD/src/jev.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — 面向证据感知的智能体交接与有界工作续跑的实验性协议。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · zsoxi · `Py` · 调用点 [`tools/build_benchmark_prompts.py`](https://github.com/zsoXi/agent-handoff-gate/blob/HEAD/tools/build_benchmark_prompts.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `已归档`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · carlosedm10 · `Py` · 调用点 [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[AskJev](https://github.com/ranjan2829/AskJev)** — AskJev：适用于任意网站的 Jev 自动驾驶，并对不可逆的点击加一道防护（使用 TypeSafe System One，而不是 Claude）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ranjan2829 · `TS` · 调用点 [`mcp/src/jev-client.ts`](https://github.com/ranjan2829/AskJev/blob/HEAD/mcp/src/jev-client.ts)，2026-09-24 阅读</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jourdanlabs · `Py` · 调用点 [`harness/run.py`](https://github.com/jourdanlabs/assay-001/blob/HEAD/harness/run.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。
  <sub>`文章` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `厂商自报数据`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — 用确定性规则加 Jev 评估代码变更风险的 CLI 与 GitHub Action。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · moezubair · `TS` · 调用点 [`src/jev.ts`](https://github.com/moezubair/check-risk/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev)** — 经由 OpenRouter 为 Claude Code 提供实验性的 Jev 权限关卡，附可复现的延迟与成本基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · rahulbalakavi · `Py` · 调用点 [`src/jev_auto_mode/cli.py`](https://github.com/RahulBalakavi/claude-code-jev/blob/HEAD/src/jev_auto_mode/cli.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[claude-jev-plugin](https://github.com/dr-dimitru/claude-jev-plugin)** — 给 Claude Code 的 Jev 语义护栏。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · dr-dimitru · `TS` · 调用点 [`dist/client.d.ts`](https://github.com/dr-dimitru/claude-jev-plugin/blob/HEAD/dist/client.d.ts)，2026-09-22 阅读</sub>

- **[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)** — 面向 AI 编码智能体 shell 命令的安全关卡（OpenCode、Antigravity）：先用快速的结构规则，再交给 TypeSafe Jev 判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · godspede · `TS` · 调用点 [`src/classifier/jev-client.ts`](https://github.com/godspede/construct-auto-classifier/blob/HEAD/src/classifier/jev-client.ts)，2026-09-24 阅读</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — 可组合的 Python 工具包：问题构造器、置信闸门等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · docxology · `Py` · 调用点 [`src/daf_jev/client.py`](https://github.com/docxology/daf-jev/blob/HEAD/src/daf_jev/client.py)，2026-09-22 阅读</sub>

- **[Decision Models as Guardrails](https://dm-as-guardrails.raxitlabs.com)** — 让 Jev 1.13.0、Jev 1.14.0 及其他 17 个系统（包括 Bedrock Guardrails）回答同样的 9,975 条带标注的护栏检查，分为六个套件。Jev 以 noul 回答每条检查，概率达到 0.5 或以上即拦截，不对任何模型单独调参。报告平衡准确率（含 95% 区间）以及按公开价格计算的每 1,000 次检查的美元成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · raxIT Labs · `Py` · `noul` · `score` · 调用点 [`benchmark/goldrails_bench/systemone.py`](https://github.com/raxITlabs/decision-models-as-guardrails/blob/HEAD/benchmark/goldrails_bench/systemone.py) · ⚠ `作者自荐`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — PR 风险路由器兼代码审查教练。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · raihankhan-rk · `TS` · 调用点 [`src/lib/review.ts`](https://github.com/raihankhan-rk/diffjury/blob/HEAD/src/lib/review.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nanami-0713 · `JS` · 调用点 [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev 驱动你的轻量浏览器：每步一次类型化选择请求，单文件零依赖。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · shikaizhong-design · `JS` · 调用点 [`jego.js`](https://github.com/shikaizhong-design/ego-jev-ultrafast/blob/HEAD/jego.js)，2026-09-22 阅读</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — 经过验证的浏览器智能体：在任意 LLM 浏览器智能体前加一道便宜的 Jev 防护（经证据检查的完成判断、破坏性操作关卡）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tom-r-main · `Py` · 调用点 [`jevdual/evals/runner.py`](https://github.com/Tom-R-Main/Footwork/blob/HEAD/jevdual/evals/runner.py)，2026-09-24 阅读</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · kalyanm45 · `Py` · 调用点 [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard)** — Grok Bot 的类型化预检与审批层：硬性边界由本地策略掌控，模糊情况交给 Jev 判断，Grok Bot 只在返回的范围内执行。 <sub>(机翻)</sub>
  <sub>`开源项目` · 0xwhrari · `Py` · 调用点 [`src/grok_jev_guard/jev.py`](https://github.com/0xwhrari/grok-jev-guard/blob/HEAD/src/grok_jev_guard/jev.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — 一个文本审核演示：一次 systemOne 调用并行检查七个 Noul 风险项和一个严重程度 Score，最终结论由代码按策略阈值计算。 <sub>(机翻)</sub>
  <sub>`开源项目` · norbertbodziony · `TS` · 调用点 [`app/api/moderate/route.ts`](https://github.com/NorbertBodziony/guard-jev/blob/HEAD/app/api/moderate/route.ts)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · abdelstark · `TS` · 调用点 [`apps/server/src/jev.ts`](https://github.com/AbdelStark/heist-one/blob/HEAD/apps/server/src/jev.ts)，2026-09-22 阅读</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — 不确定时保持沉默的 issue 分拣：校准过的标签，含垃圾与重复检测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · emreozyoruk · `JS` · 调用点 [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · Really Artificial · `JS` · `choice` · `score` · `noul` · 调用点 [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs)，2026-09-22 阅读 · ⚠ `疑似 AI 生成`</sub>

- **[JEV Safety Gateway](https://github.com/dark-hxx/jev-safety-gateway)** — 位于 nginx 与 OpenAI 兼容大模型后端之间的反向代理：取出每个请求中的用户输入，用一个 noul 让 Jev 判断是否安全，拦截有害请求、放行正常请求；可在多个 API 密钥之间轮换。文档以中文为主。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dark-hxx · `Go` · `noul` · 调用点 [`internal/jev/client.go`](https://github.com/dark-hxx/jev-safety-gateway/blob/HEAD/internal/jev/client.go)，2026-10-24 模型阅读</sub>

- **[jev-agent-authorization](https://github.com/kinde-starter-kits/jev-agent-authorization)** — 面向 MCP 工具调用的 Jev 智能体授权：结合 Kinde 的身份与权限，以及 Jev 的类型化校准决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · kinde-starter-kits · `TS` · 调用点 [`convex/jev/client.ts`](https://github.com/kinde-starter-kits/jev-agent-authorization/blob/HEAD/convex/jev/client.ts)，2026-09-24 阅读</sub>

- **[jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper)** — 用 Jev 类型化决策加 ffmpeg 实现的低延迟音频消音原型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · santos-sanz · `TS` · 调用点 [`index.ts`](https://github.com/santos-sanz/jev-audio-beeper/blob/HEAD/index.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — TypeSafe AI Jev 在智能体工具调用风险分类上的可复现基准：准确率、延迟，以及其置信度是否可信。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · themsquared · `Py` · 调用点 [`bench.py`](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py)，2026-09-24 阅读</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ufec · `Kt` · 调用点 [`app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt`](https://github.com/ufec/jev-block-android-ad/blob/HEAD/app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt)，2026-09-22 阅读</sub>

- **[jev-carryforward](https://github.com/dharun-cohere/jev-carryforward)** — 把上一轮会话知道的东西，对照这一轮正在做的事打分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · dharundp6 · `TS` · 调用点 [`src/gateway.ts`](https://github.com/dharun-cohere/jev-carryforward/blob/HEAD/src/gateway.ts)，2026-09-22 阅读</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · nikkoxgonzales · `Py` · 调用点 [`jev_certify/analysis.py`](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py)，2026-09-22 阅读</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions-hermes)** — 给 Hermes 及其他智能体的 Jev 决策插件：工具风险审查与人工批准。 <sub>(机翻)</sub>
  <sub>`插件` · bojansandhaus · `Py` · 调用点 [`jev_client.py`](https://github.com/bojansandhaus/jev-decisions-hermes/blob/HEAD/jev_client.py)，2026-09-22 阅读</sub>

- **[jev-dev](https://github.com/n-yokomachi/jev-dev)** — 把同一句话同时交给 Jev 和 LLM 判定，在一屏内对比情绪波动值与响应速度（日语）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · n-yokomachi · `TS` · 调用点 [`scripts/probe-jev.ts`](https://github.com/n-yokomachi/jev-dev/blob/HEAD/scripts/probe-jev.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-gate](https://github.com/MongLong0214/jev-gate)** — 不是每个编程任务都需要你最好的模型：实验性的 Jev 模型路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · monglong0214 · `TS` · 调用点 [`src/jev.ts`](https://github.com/MongLong0214/jev-gate/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — 给 Claude Code 的六道校准闸门：规则、范围、意图、完成度等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · rashedint32 · `JS` · 调用点 [`lib/jev.mjs`](https://github.com/rashedInt32/jev-gates/blob/HEAD/lib/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-guard](https://github.com/ClemensSchartmueller/jev-guard)** — 面向 Claude Code、Codex CLI 与 Antigravity 的跨智能体安全关卡：拦截 shell 执行、文件写入和补丁，先做快速的本地边界检查，再让 Jev 判断影响范围、可逆性与破坏性。 <sub>(机翻)</sub>
  <sub>`插件` · clemensschartmueller · `Go` · 调用点 [`pkg/evaluator/typesafe.go`](https://github.com/ClemensSchartmueller/jev-guard/blob/HEAD/pkg/evaluator/typesafe.go)，2026-09-24 阅读</sub>

- **[jev-guard](https://github.com/CMaintz/jev-guard)** — 在 LLM 智能体的工具调用执行前，交给 TypeSafe AI 的 Jev 审核——放行、阻止或挂起，不确定时安全失败。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cmaintz · `TS` · 调用点 [`src/providers/typesafe.ts`](https://github.com/CMaintz/jev-guard/blob/HEAD/src/providers/typesafe.ts)，2026-09-24 阅读 · ⚠ `已归档`</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — 为 Claude Code 提供概率评分的护栏：拒绝违反规则的修改和未经要求的部署，并把文档路由到合适的位置。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · muratcakmak · `TS` · 调用点 [`scripts/jev-lint.ts`](https://github.com/muratcakmak/jev-guard/blob/HEAD/scripts/jev-lint.ts)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-kit](https://github.com/jonathanavis96/jev-kit)** — 一套 Claude Code 工具包：PreToolUse 守卫先用免费的代码预筛放行约 93% 的工具调用，其余交给 Jev 判断（放行、警告、改写或拦截，出错时默认放行）；还能为子 Agent 选择合适的规格，并把 Jev 接入文件搜索、浏览和代码审阅。作者报告浏览器任务 9/9 成功，Claude 花费仅 0.0008 美元。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · jonathanavis96 · `Py` · `choice` · `noul` · 调用点 [`vendor/jev-ultrafast/jev_ultrafast/model.py`](https://github.com/jonathanavis96/jev-kit/blob/HEAD/vendor/jev-ultrafast/jev_ultrafast/model.py)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jyatesdotdev · `Py` · 调用点 [`logtriage/cli.py`](https://github.com/jyatesdotdev/jev-logtriage/blob/HEAD/logtriage/cli.py)，2026-09-22 阅读</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — OpenAI 兼容代理，夹在你的 LLM 与用户之间，逐窗口评估输出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · thanh-mathieu95 · `JS` · 调用点 [`evaluator.js`](https://github.com/Thanh-Mathieu95/jev-model-tokengate/blob/HEAD/evaluator.js)，2026-09-22 阅读</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · scienthoon · `Py` · 调用点 [`scripts/jev_eval.mjs`](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · yodablocks · `Py` · 调用点 [`harness/client.py`](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py)，2026-09-22 阅读</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — 证据门控的 Jev 问题包注册表：精选问题、黄金样例与实测证据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dtduc-git · `Py` · 调用点 [`scripts/refresh.py`](https://github.com/dtduc-git/jev-packs/blob/HEAD/scripts/refresh.py)，2026-09-22 阅读</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev 增强的 Playwright MCP 代理：页面状态分拣与提示注入防护。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · krw82 · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/krw82/jev-playwright-mcp/blob/HEAD/src/jev/client.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — 给 Claude Code 的有界 Jev 风险检查：八个风险维度、一次请求。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · muse0509 · `Go` · 调用点 [`internal/jev/client.go`](https://github.com/muse0509/jev-preflight/blob/HEAD/internal/jev/client.go)，2026-09-22 阅读</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 面向 WebFlux 的 Spring Boot Starter：标注了 @SemanticCircuitBreaker 的方法会把每个响应体发给 Jev，用一个 noul 判断这个 HTTP 200 是否掩盖了错误、堆栈信息或维护通知；超过阈值（示例中为 0.85）就抛出熔断器可以计数的异常。失败即放行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · vicente-md · `Java` · 调用点 [`src/main/java/ai/jev/resilience/client/dto/JevRequest.java`](https://github.com/Vicente-MD/jev-resilience/blob/HEAD/src/main/java/ai/jev/resilience/client/dto/JevRequest.java)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · teyhouse · `Py` · 调用点 [`main.py`](https://github.com/teyhouse/jev-secret-detection/blob/HEAD/main.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-shield](https://github.com/vmendes90/jev-shield)** — 隐私优先的 Chrome 扩展：语义拦截原生广告与赞助信息流卡片。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · vmendes90 · `TS` · 调用点 [`src/background/typesafe.ts`](https://github.com/vmendes90/jev-shield/blob/HEAD/src/background/typesafe.ts)，2026-09-22 阅读</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · shivampansuriya · `JS` · 调用点 [`src/providers/typesafe.mjs`](https://github.com/ShivamPansuriya/jev-skill-gate/blob/HEAD/src/providers/typesafe.mjs)，2026-09-24 阅读</sub>

- **[jev-skillful](https://github.com/bestagentkits/jev-skillful)** — 给编程智能体的逐提示能力路由器：解析已安装的技能、MCP server 与子智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · bestagentkits · `TS` · 调用点 [`packages/cli/src/core/jev/types.ts`](https://github.com/bestagentkits/jev-skillful/blob/HEAD/packages/cli/src/core/jev/types.ts)，2026-09-22 阅读</sub>

- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** — 用 Jev 的 Noul 问题做零样本垃圾邮件过滤，并与 TF-IDF 基线对比。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · bitnovus · `Py` · 调用点 [`experiments/jev-context/evaluate.py`](https://github.com/bitnovus/jev-spam-eval/blob/HEAD/experiments/jev-context/evaluate.py)，2026-09-22 阅读</sub>

- **[jev-switchboard](https://github.com/ZIJIAN004/jev-switchboard)** — 给并行编程智能体的 JEV 门控语义通信层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · zijian004 · `JS` · 调用点 [`src/jev.mjs`](https://github.com/ZIJIAN004/jev-switchboard/blob/HEAD/src/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-tool-permissions](https://github.com/NicolasMontone/jev-tool-permissions)** — 给 Vercel AI SDK 的 Jev 工具批准闸门与工具列表裁剪。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · nicolasmontone · `TS` · 调用点 [`src/types.ts`](https://github.com/NicolasMontone/jev-tool-permissions/blob/HEAD/src/types.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer)** — 看看 Jev 怎么评价你的 SaaS 网站。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · replynodes · `TS` · 调用点 [`app/api/analyze/route.ts`](https://github.com/replynodes/jev-web-analyzer/blob/HEAD/app/api/analyze/route.ts)，2026-09-22 阅读</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — 先评估再信任：实战笔记、可运行脚本与一个 agent 技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · elshinq · `JS` · 调用点 [`scripts/jev.mjs`](https://github.com/ElshinQ/jevaluate/blob/HEAD/scripts/jev.mjs)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jevc](https://github.com/doronp/jevc)** — 把智能体的策略文字编译成确定性的裁决程序：给模型窄的证据问题，裁决由编译出的代码给出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · doronp · `TS` · 调用点 [`src/runtime.ts`](https://github.com/doronp/jevc/blob/HEAD/src/runtime.ts)，2026-09-24 阅读</sub>

- **[jevegis](https://github.com/0xArx/jevegis)** — 一次 API 调用搞定 LLM 应用的护栏：提示注入、越狱、泄露与不安全内容。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 0xarx · `TS` · 调用点 [`src/lib/typesafe.ts`](https://github.com/0xArx/jevegis/blob/HEAD/src/lib/typesafe.ts)，2026-09-22 阅读</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — 面向 CI 与编码智能体的代码审查关卡：就函数、文件、测试与依赖向 TypeSafe Jev 提出小而具体的类型化问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tech-byte-frontier · `Rs` · 调用点 [`src/auth/provider.rs`](https://github.com/Tech-Byte-Frontier/jevgate/blob/HEAD/src/auth/provider.rs)，2026-09-24 阅读</sub>

- **[JevLang](https://github.com/TimMikeladze/JevLang)** — 面向 LLM 决策的策略引擎：用 TypeScript 或 Python 一次性声明路由、关卡和动作，每个决策都可追溯。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · timmikeladze · `JS` · 调用点 [`examples/entity-alignment.js`](https://github.com/TimMikeladze/JevLang/blob/HEAD/examples/entity-alignment.js)，2026-09-24 阅读</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — 面向社区和应用的内容审核，由 Jev（TypeSafe）驱动：按类别给出概率，阈值由你掌控。支持 Discord。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ohernandezdev · `Py` · 调用点 [`jevmod/judge.py`](https://github.com/ohernandezdev/jevmod/blob/HEAD/jevmod/judge.py)，2026-09-24 阅读</sub>

- **[jevnav](https://github.com/dtduc-git/jevnav)** — 为浏览器智能体提供“页面真相”，以及可回放、可测试、可审计的决策。Jev 选择元素，高风险操作需要把关。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dtduc-git · `Py` · 调用点 [`src/jevnav/decide.py`](https://github.com/dtduc-git/jevnav/blob/HEAD/src/jevnav/decide.py)，2026-09-24 阅读</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — 亚 100 毫秒的智能体工具调用安全闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lgy1027 · `Py` · 调用点 [`jevshield/client.py`](https://github.com/lgy1027/jevshield/blob/HEAD/jevshield/client.py)，2026-09-22 阅读</sub>

- **[jit-context](https://github.com/wojciechwiesner/jit-context)** — JIT-JEV 上下文操作系统：面向 AI 智能体的认知运行时与 JEV System 1 上下文关卡。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · wojciechwiesner · `Py` · 调用点 [`src/cognitive/jev_engine.py`](https://github.com/wojciechwiesner/jit-context/blob/HEAD/src/cognitive/jev_engine.py)，2026-09-24 阅读</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul` · ⚠ `需早期访问`</sub>

- **[last-exit](https://github.com/0x963D/last-exit)** — 由 Jev 驱动的赛博朋克边境遭遇战：忽悠守卫，检查凭据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 0x963d · `JS` · 调用点 [`lib/hosted.mjs`](https://github.com/0x963D/last-exit/blob/HEAD/lib/hosted.mjs)，2026-09-22 阅读</sub>

- **[macos-computer-use-kit](https://github.com/Sur-Cai/macos-computer-use-kit)** — 面向 macOS AI 智能体的、以辅助功能为先的电脑操作工具包，可选配 Jev（TypeSafe System One）语义护栏。 <sub>(机翻)</sub>
  <sub>`插件` · sur-cai · `Py` · 调用点 [`src/macos_computer_use/jev.py`](https://github.com/Sur-Cai/macos-computer-use-kit/blob/HEAD/src/macos_computer_use/jev.py)，2026-09-24 阅读</sub>

- **[mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation)** — 给 Mastra 智能体的输入审核，基于 Jev，单文件实现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · codealive-ai · `TS` · 调用点 [`jev-moderation.ts`](https://github.com/CodeAlive-AI/mastra-jev-moderation/blob/HEAD/jev-moderation.ts)，2026-09-22 阅读</sub>

- **[nachalnik](https://github.com/ljedrz/nachalnik)** — 一个透明的 Rust 智能体运行时：上下文、工具、权限与请求都是显式状态，另附 MCP 桥接。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ljedrz · `Rs` · 调用点 [`kamchatka/src/args.rs`](https://github.com/ljedrz/nachalnik/blob/HEAD/kamchatka/src/args.rs)，2026-09-24 阅读</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — 给 OMP 的模型裁决式权限闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · strml · `TS` · 调用点 [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts)，2026-09-22 阅读 · ⚠ `已归档`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — 给 Codex 与 Claude Code 的二值批准闸门：每次被拦截的工具调用都要审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · alexj11324 · `Go` · 引用文件 [`internal/jev/client.go`](https://github.com/alexj11324/open-jev-approvals/blob/HEAD/internal/jev/client.go)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — 给 OpenClaw 的可选类型化 Jev 决策，带 SecretRef 凭据与严格的 API 校验。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · olli0103 · `TS` · 调用点 [`src/client.ts`](https://github.com/Olli0103/openclaw-typesafe-ai/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[opencode-jev-guard](https://github.com/CogFlux/opencode-jev-guard)** — OpenCode 2 插件：把每条 shell 命令发给 TypeSafe 的 Jev，看起来有风险时先询问你。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · cogflux · `TS` · 调用点 [`jev-guard.ts`](https://github.com/CogFlux/opencode-jev-guard/blob/HEAD/jev-guard.ts)，2026-09-24 阅读</sub>

- **[openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp)** — 由 OpenRouter 驱动的高速 System One 决策网关与 MCP server。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ctmx · `Py` · 调用点 [`examples/demo_typesafe_sdk.py`](https://github.com/ctmx/openrouter-jev-mcp/blob/HEAD/examples/demo_typesafe_sdk.py)，2026-09-22 阅读</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — 单智能体的 Pi 编程协处理器，带 Jev 语义闸门与基线对比 diff 审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kamilpostrozny · `TS` · 调用点 [`src/index.ts`](https://github.com/KamilPostrozny/pi-jev-code/blob/HEAD/src/index.ts)，2026-09-22 阅读</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — 给 Pi 编程智能体的 Jev 权限闸门：审判每一次 bash 与写入。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kurihada · `TS` · 调用点 [`src/jev.ts`](https://github.com/kurihada/pi-jev-permit/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[pkg-gate](https://github.com/hemanth/pkg-gate)** — 用 System One 给 npm 生命周期脚本做安装前安全闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hemanth · `JS` · 调用点 [`src/gate.js`](https://github.com/hemanth/pkg-gate/blob/HEAD/src/gate.js)，2026-09-22 阅读</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — 检测 AI 智能体循环中的语义停滞。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ashutoshvjti · `TS` · 调用点 [`experiments/jev-client.ts`](https://github.com/AshutoshVJTI/progressgate/blob/HEAD/experiments/jev-client.ts)，2026-09-22 阅读</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One 搜索：用类型化判断与仓库证据导航与追踪代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cpaczek · `TS` · 调用点 [`src/client.ts`](https://github.com/cpaczek/s1s/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[shade-arena-jev-monitor](https://github.com/nican2018/shade-arena-jev-monitor)** — 评估 Jev 作为智能体破坏行为的快速监控与动作闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · nican2018 · `Py` · 调用点 [`llms/typesafe_llm.py`](https://github.com/nican2018/shade-arena-jev-monitor/blob/HEAD/llms/typesafe_llm.py)，2026-09-22 阅读</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town：客厅电视上的社交推理派对游戏，由 Jev 主持。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tpaulshippy · `Rb` · 调用点 [`lib/shady_town/evaluator.rb`](https://github.com/tpaulshippy/shady-town/blob/HEAD/lib/shady_town/evaluator.rb)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[siege](https://github.com/vnmoorthy/siege)** — SIEGE：200 人对战一个智能体，一道会学习的类型化动作闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · vnmoorthy · `TS` · 调用点 [`backend/app/gate.py`](https://github.com/vnmoorthy/siege/blob/HEAD/backend/app/gate.py)，2026-09-22 阅读</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — 开源 Chrome 扩展：用 Jev 过滤 AI 生成的文字与广告。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · neddes · `JS` · 调用点 [`background.js`](https://github.com/neddes/sloppy-jevs-extension/blob/HEAD/background.js)，2026-09-22 阅读</sub>

- **[solvi](https://github.com/solvi-ai/solvi)** — Python 决策运行时，内置 System One API 适配器：由 Jev、LLM 或本地模型给出类型化答案，再由硬性检查、规则和校准阈值决定采纳、弃权或转交人工；每个决策都保存为可重放的哈希链记录。 <sub>(机翻)</sub>
  <sub>`SDK` · mxkuzn · `Py` · `choice` · `noul` · 调用点 [`src/solvi/core/deciders/systemone.py`](https://github.com/solvi-ai/solvi/blob/HEAD/src/solvi/core/deciders/systemone.py)，2026-10-23 阅读 · ⚠ `作者自荐`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — 智能体的每一次工具调用在执行前都过一遍检查的 Claude Code 插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · getexcited · `TS` · 调用点 [`lib/jev.ts`](https://github.com/getexcited/stepwarden/blob/HEAD/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** — 基于 TypeSafe Jev（System One 模型）的 LLM 网关护栏与模型路由器，附带独立的准确率与校准评估。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · aniruddh-krovvidi · `Py` · 调用点 [`jev.py`](https://github.com/aniruddh-krovvidi/switchboard/blob/HEAD/jev.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[toolgate](https://github.com/ndolinschi/toolgate)** — 智能体工具与 MCP 调用关卡：通过 TypeSafe Jev 决定放行、询问人类或拒绝。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/toolgate/blob/HEAD/src/lib/jev.ts)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[trustgate](https://github.com/ndolinschi/trustgate)** — TrustGate：面向独立媒体的信任与安全闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/trustgate/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — 由 Jev 驱动的数据库迁移安全自动审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · opaielsheikh · `TS` · 调用点 [`lib/typesafe.ts`](https://github.com/opaielsheikh/typesafe-migration-guard/blob/HEAD/lib/typesafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — 基于 Jev 的三条可组合判断流水线：工单分拣、可观测性等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shivam2003-dev · `Py` · 调用点 [`src/triage/mock.py`](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/HEAD/src/triage/mock.py)，2026-09-22 阅读</sub>

- **[wakegate](https://github.com/shitianfang/wakegate)** — 在唤醒一个休眠智能体之前，先问 Jev 这次唤醒是否值得一次完整的 LLM 轮次。失败时默认放行。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shitianfang · `TS` · 调用点 [`src/index.ts`](https://github.com/shitianfang/wakegate/blob/HEAD/src/index.ts)，2026-09-22 阅读</sub>

- **[x402check](https://github.com/caiovicentino/jev-risk-check-provider)** — 面向 x402 Agent 和钱包的付款前风险检查服务：结合制裁名单、钓鱼情报、交易模拟和盗币工具包指纹，再用 Jev 的多个 noul、一个 choice 和一个 score 检查 Agent 所依据的内容里有没有被注入的指令。结论以签名证明的形式给出。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · caiovicentino · `TS` · `noul` · `choice` · `score` · 调用点 [`src/jev.ts`](https://github.com/caiovicentino/jev-risk-check-provider/blob/HEAD/src/jev.ts)，2026-10-24 模型阅读 · ⚠ `营销内容`</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — Jev 形状的本地决策层：是非、选择和量表问题都从本地模型单个 token 的 logprob 读出答案；附带一个在留出命令集上测量过的 Claude Code 权限闸门。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · Xinyu Liu · `TS` · `noul` · `choice` · `score` · 引用文件 [`src/gate.ts`](https://github.com/liu-x27/XavierJev/blob/HEAD/src/gate.ts)，2026-09-25 阅读 · ⚠ `并非 Jev 本身` `疑似 AI 生成`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — 给编程智能体的类型化判断层：从需求文档到发布的各道闸门。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · zahrannnn · `TS` · 调用点 [`src/backends/jev.ts`](https://github.com/Zahrannnn/zcode-jev/blob/HEAD/src/backends/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
