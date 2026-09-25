# 安全闸门

<sub>[awesome-jev](../../README.zh-CN.md) · [English](safety-gating.md)</sub>

_在执行前判断一个动作是否安全。属纵深防御，绝不是安全边界。_

这个决策的全部已收录例子 —— 共 139 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#安全闸门)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。
  <sub>`开源项目` · ★42,557 · `Go` · `noul`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★31,582 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。
  <sub>`平台集成` · ★18,223 · `TS` · `choice` · `score` · `noul`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。
  <sub>`开源项目` · ★6,341 · `TS` · `choice` · `noul`</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)** — 三个共用同一严重度量表的 Score 问题，两项以上越线即拦截请求，并且失败时默认关闭。
  <sub>`开源项目` · ★5,017 · `Rs` · `score`</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — 可验证的编程智能体运行时：用自然语言定义智能体的流程。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★820 · bastani-inc · `TS`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。
  <sub>`开源项目` · ★591 · `JS` · `choice` · `noul`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — 带 Jev 智能路由的 AI 智能体：把大白话请求分派给合适的专家智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★425 · notque · `Py`</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — 一个 AI 编程智能体：读代码、改文件、跑命令、推理 bug。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★335 · wrongstack · `TS`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — 统管所有机器人的 CLI：每台机器人配一个 LLM 作大脑，由 Jev 做决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★231 · rokbenko · `Py`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — 把 Jev 接进编程智能体，用于工具调用的推理判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★202 · vinilana · `TS`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。
  <sub>`开源项目` · ★164 · `Py` · `choice` · `score` · `noul` · ⚠ `宣称未核实`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — 给编程智能体做的决策层：一个可度量的工具调用闸门，外加一个返回校准答案的类型化提问。
  <sub>`插件` · ★142 · y0usaf · `TS`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 结合实时音频与字幕检测 YouTube 视频里的赞助片段。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★95 · trungdq88 · `JS` · ⚠ `无许可证`</sub>

- **[bluenoise](https://github.com/rokcso/bluenoise)** — 模糊或隐藏 X 上嘈杂的回复、帖子与广告，并清理界面。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★90 · rokcso · `TS`</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)** — 把 Jev 接到 Grok Bot 上作为廉价决策层，含用量闸门与技能模板。 <sub>(机翻)</sub>
  <sub>`插件` · ★77 · bodila51 · `Py`</sub>

- **[jevals](https://github.com/openlayer-ai/jevals)** — 把智能体评测与护栏做成 Jev 决策：每条 trace 一次请求，成本不到一美分的零头。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★77 · openlayer-ai · `Py`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★44 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-guard](https://github.com/klauswg/jev-guard)** — 面向交易所充值与提现的实时风险分诊网关——Jev（TypeSafe System One）只负责分诊，裁决另有机制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★35 · klauswg · `Java`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给所有编程智能体做的自动模式：结合会话上下文给每次工具调用打风险分（拒绝／询问／放行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★30 · leepokai · `JS`</sub>

- **[is-malicious](https://github.com/luantak/is-malicious)** — 代码库扫描器，帮你避免运行恶意代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★23 · luantak · `TS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 开源的 macOS computer use 与原生 GUI 自动化，运行在 Apple 芯片上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★21 · jcpsimmons · `JS`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20 · keeltrace · `Py`</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code 的 Stop 钩子：在未经验证的“完成”之前拦下——读取会话记录找证据，只问 Jev 一次，其余情况一律放行。 <sub>(机翻)</sub>
  <sub>`插件` · ★18 · valentynkit · `JS`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — 面向类型化决策模型的概率感知评测：校准度、选择性风险、延迟，以及可复现的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★17 · abdelstark · `Py`</sub>

- **[muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook)** — 为 Muse 提供的 Jev 决策层：在昂贵的智能体工作之前加一道快速、便宜的 TypeSafe AI 关卡——置信度策略与配方。 <sub>(机翻)</sub>
  <sub>`插件` · ★16 · bodila51 · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — 用 Jev 做拦截、引导与「模糊 lint」，让智能体遵守你的规则与约定。含 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · tyler-dot-earth · `TS`</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — 通过 Vercel AI Gateway 为 Pi 做自动模型路由。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · mejiasd3v · `JS`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · antoniocoppe · `TS`</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 的可疑行为，结合静态证据并明确标注覆盖范围。 <sub>(机翻)</sub>
  <sub>`插件` · ★10 · win4r · `Py`</sub>

- **[pi-verdict](https://github.com/jesset/pi-verdict)** — 给 Pi 的最小权限闸门，仿照 Claude Code 的自动模式。 <sub>(机翻)</sub>
  <sub>`插件` · ★10 · jesset · `TS`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★9 · 24601 · `Py`</sub>

- **[flue-jev-demo](https://github.com/matthewp/flue-jev-demo)** — 通过 Cloudflare AI Gateway 用 Jev 做 Flue 智能体路由。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · matthewp · `TS` · ⚠ `无许可证`</sub>

- **[jev-sentinel](https://github.com/harshwasan/jev-sentinel)** — Pi 编码智能体扩展：用 TypeSafe Jev 检查工具调用、工具输出和回复（提示注入、审批、敏感信息等）。 <sub>(机翻)</sub>
  <sub>`插件` · ★9 · harshwasan · `TS`</sub>

- **[jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot)** — 基于 grammY 的极简 Telegram 反垃圾机器人。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · backmeupplz · `TS`</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — 由 Jev 自动完成的 PR 风险审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · hexyedev · `Py`</sub>

- **[AskJev](https://github.com/ranjan2829/AskJev)** — AskJev：适用于任意网站的 Jev 自动驾驶，并对不可逆的点击加一道防护（使用 TypeSafe System One，而不是 Claude）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · ranjan2829 · `TS`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — PR 风险路由器兼代码审查教练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · raihankhan-rk · `TS` · ⚠ `无许可证`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · abdelstark · `TS`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — 在 DSPy 工作流中对 Jev 决策做可复现的校准与选择性风险基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★7 · jmanhype · `Py`</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — 为 Claude Code 提供概率评分的护栏：拒绝违反规则的修改和未经要求的部署，并把文档路由到合适的位置。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · muratcakmak · `TS`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — 可组合的 Python 工具包：问题构造器、置信闸门等。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · docxology · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · ufec · `Kt`</sub>

- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)** — 零依赖的 System One 决策框架：用 5 道语义关卡，在琐碎错误和“死循环”上替前沿 AI 智能体省下 token。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · ismaelsoilet · `Py`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · scienthoon · `Py`</sub>

- **[jevc](https://github.com/doronp/jevc)** — 把智能体的策略文字编译成确定性的裁决程序：给模型窄的证据问题，裁决由编译出的代码给出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · doronp · `TS`</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — 用 Jev 做判断而不是生成：修剪过长的工具输出、筛查抓取页面中注入的指令、为“完成”把关。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · horusjiang · `TS`</sub>

- **[jev-agent-authorization](https://github.com/kinde-starter-kits/jev-agent-authorization)** — 面向 MCP 工具调用的 Jev 智能体授权：结合 Kinde 的身份与权限，以及 Jev 的类型化校准决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · kinde-starter-kits · `TS`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · shivampansuriya · `JS`</sub>

- **[jev-tool-permissions](https://github.com/NicolasMontone/jev-tool-permissions)** — 给 Vercel AI SDK 的 Jev 工具批准闸门与工具列表裁剪。 <sub>(机翻)</sub>
  <sub>`SDK` · ★5 · nicolasmontone · `TS` · ⚠ `无许可证`</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — 生产级的 Jev 用例 harness，带置信度门控的决策逻辑。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · kenhuangus · `Py`</sub>

- **[jit-context](https://github.com/wojciechwiesner/jit-context)** — JIT-JEV 上下文操作系统：面向 AI 智能体的认知运行时与 JEV System 1 上下文关卡。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · wojciechwiesner · `Py`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · carlosedm10 · `Py` · ⚠ `无许可证`</sub>

- **[claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev)** — 经由 OpenRouter 为 Claude Code 提供实验性的 Jev 权限关卡，附可复现的延迟与成本基准。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · rahulbalakavi · `Py`</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — OpenAI 兼容代理，夹在你的 LLM 与用户之间，逐窗口评估输出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · thanh-mathieu95 · `JS`</sub>

- **[jev-shield](https://github.com/vmendes90/jev-shield)** — 隐私优先的 Chrome 扩展：语义拦截原生广告与赞助信息流卡片。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · vmendes90 · `TS`</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — 面向 CI 与编码智能体的代码审查关卡：就函数、文件、测试与依赖向 TypeSafe Jev 提出小而具体的类型化问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · tech-byte-frontier · `Rs`</sub>

- **[macos-computer-use-kit](https://github.com/Sur-Cai/macos-computer-use-kit)** — 面向 macOS AI 智能体的、以辅助功能为先的电脑操作工具包，可选配 Jev（TypeSafe System One）语义护栏。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · sur-cai · `Py`</sub>

- **[nachalnik](https://github.com/ljedrz/nachalnik)** — 一个透明的 Rust 智能体运行时：上下文、工具、权限与请求都是显式状态，另附 MCP 桥接。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · ljedrz · `Rs`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · abhishekswe · `TS`</sub>

- **[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)** — 面向 AI 编码智能体 shell 命令的安全关卡（OpenCode、Antigravity）：先用快速的结构规则，再交给 TypeSafe Jev 判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · godspede · `TS`</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev 驱动你的轻量浏览器：每步一次类型化选择请求，单文件零依赖。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · shikaizhong-design · `JS`</sub>

- **[jev-gate](https://github.com/MongLong0214/jev-gate)** — 不是每个编程任务都需要你最好的模型：实验性的 Jev 模型路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · monglong0214 · `TS` · ⚠ `无许可证`</sub>

- **[jev-guard](https://github.com/ClemensSchartmueller/jev-guard)** — 面向 Claude Code、Codex CLI 与 Antigravity 的跨智能体安全关卡：拦截 shell 执行、文件写入和补丁，先做快速的本地边界检查，再让 Jev 判断影响范围、可逆性与破坏性。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · clemensschartmueller · `Go`</sub>

- **[jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer)** — 看看 Jev 怎么评价你的 SaaS 网站。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · replynodes · `TS`</sub>

- **[mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation)** — 给 Mastra 智能体的输入审核，基于 Jev，单文件实现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · codealive-ai · `TS`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — 给 Codex 与 Claude Code 的二值批准闸门：每次被拦截的工具调用都要审查。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★3 · alexj11324 · `Go` · ⚠ `并非 Jev 本身`</sub>

- **[rh-guard](https://github.com/24601/rh-guard)** — 给编程智能体的奖励作弊雷达：结构化拒绝加 System One 旁路。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · 24601 · `TS`</sub>

- **[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)** — 开源的智能体工具调用授权网关：确定性策略加 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · omkarghugarkar007 · `TS`</sub>

- **[claude-jev-plugin](https://github.com/dr-dimitru/claude-jev-plugin)** — 给 Claude Code 的 Jev 语义护栏。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · dr-dimitru · `TS`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · nanami-0713 · `JS`</sub>

- **[grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard)** — Grok Bot 的类型化预检与审批层：硬性边界由本地策略掌控，模糊情况交给 Jev 判断，Grok Bot 只在返回的范围内执行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · 0xwhrari · `Py`</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — 不确定时保持沉默的 issue 分拣：校准过的标签，含垃圾与重复检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · emreozyoruk · `JS`</sub>

- **[jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper)** — 用 Jev 类型化决策加 ffmpeg 实现的低延迟音频消音原型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · santos-sanz · `TS` · ⚠ `无许可证`</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions)** — 给 Hermes 及其他智能体的 Jev 决策插件：工具风险审查与人工批准。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · bojansandhaus · `Py`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — 亚秒级的 Git pre-commit / pre-push 语义反射闸门。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 给 Spring WebFlux 的非阻塞 Starter，实现一个语义熔断器来检测静默故障。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vicente-md · `Java` · ⚠ `无许可证`</sub>

- **[jev-skillful](https://github.com/bestagentkits/jev-skillful)** — 给编程智能体的逐提示能力路由器：解析已安装的技能、MCP server 与子智能体。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · bestagentkits · `TS`</sub>

- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** — 用 Jev 的 Noul 问题做零样本垃圾邮件过滤，并与 TF-IDF 基线对比。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · bitnovus · `Py`</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — 亚 100 毫秒的智能体工具调用安全闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · lgy1027 · `Py`</sub>

- **[opencode-jev-guard](https://github.com/CogFlux/opencode-jev-guard)** — OpenCode 2 插件：把每条 shell 命令发给 TypeSafe 的 Jev，看起来有风险时先询问你。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · cogflux · `TS`</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — 面向 AI 智能体的开源自动模式：一个校准过的工具调用防火墙。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · riskaversetech · `TS`</sub>

- **[toolgate](https://github.com/ndolinschi/toolgate)** — 智能体工具与 MCP 调用关卡：通过 TypeSafe Jev 决定放行、询问人类或拒绝。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — 由 Jev 驱动的数据库迁移安全自动审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · opaielsheikh · `TS` · ⚠ `无许可证`</sub>

- **[zerosweep](https://github.com/sysadarsh/zerosweep)** — 自主的 System-One 分拣引擎与基准，75 毫秒推理。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · sysadarsh · `TS` · ⚠ `无许可证`</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — 为 DeepSeek Harness 中的每一次工具调用提供毫秒级 System-1 判断——由 Jev 驱动的风险分类与证据检查。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · asktheway · `TS`</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — 经过验证的浏览器智能体：在任意 LLM 浏览器智能体前加一道便宜的 Jev 防护（经证据检查的完成判断、破坏性操作关卡）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · tom-r-main · `Py`</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — 一个文本审核演示：一次 systemOne 调用并行检查七个 Noul 风险项和一个严重程度 Score，最终结论由代码按策略阈值计算。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · norbertbodziony · `TS` · ⚠ `无许可证`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `仅一次提交` `疑似 AI 生成`</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — TypeSafe AI Jev 在智能体工具调用风险分类上的可复现基准：准确率、延迟，以及其置信度是否可信。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · themsquared · `Py`</sub>

- **[jev-carryforward](https://github.com/Dharundp6/jev-carryforward)** — 把上一轮会话知道的东西，对照这一轮正在做的事打分。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · dharundp6 · `TS`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jyatesdotdev · `Py`</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev 增强的 Playwright MCP 代理：页面状态分拣与提示注入防护。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · krw82 · `TS`</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — 给 Claude Code 的有界 Jev 风险检查：八个风险维度、一次请求。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · muse0509 · `Go`</sub>

- **[jev-runtime-security](https://github.com/ringzerosec/jev-runtime-security)** — 面向 AI 编码智能体的运行时安全：策略在内核的系统调用层强制执行，位于智能体及其所写的一切之下，模糊情况交给 Jev 判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ringzerosec · `Rs`</sub>

- **[jev-screen-mcp](https://github.com/jiawei686/jev-screen-mcp)** — 单一用途的 MCP 服务器（一个工具，一件事）：由 TypeSafe Jev 驱动的内容审核关卡。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · jiawei686 · `TS`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · teyhouse · `Py` · ⚠ `无许可证`</sub>

- **[jev-switchboard](https://github.com/ZIJIAN004/jev-switchboard)** — 给并行编程智能体的 JEV 门控语义通信层。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · zijian004 · `JS`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — 先评估再信任：实战笔记、可运行脚本与一个 agent 技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · elshinq · `JS`</sub>

- **[jevegis](https://github.com/0xArx/jevegis)** — 一次 API 调用搞定 LLM 应用的护栏：提示注入、越狱、泄露与不安全内容。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · 0xarx · `TS`</sub>

- **[JevLang](https://github.com/TimMikeladze/JevLang)** — 面向 LLM 决策的策略引擎：用 TypeScript 或 Python 一次性声明路由、关卡和动作，每个决策都可追溯。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · timmikeladze · `JS`</sub>

- **[jevnav](https://github.com/dtduc-git/jevnav)** — 为浏览器智能体提供“页面真相”，以及可回放、可测试、可审计的决策。Jev 选择元素，高风险操作需要把关。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · dtduc-git · `Py`</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — 给 Pi 编程智能体的 Jev 权限闸门：审判每一次 bash 与写入。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · kurihada · `TS`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — 智能体的每一次工具调用在执行前都过一遍检查的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · getexcited · `TS`</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — Jev 形状的本地决策层：是非、选择和量表问题都从本地模型单个 token 的 logprob 读出答案；附带一个在留出命令集上测量过的 Claude Code 权限闸门。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★1 · Xinyu Liu · `TS` · `noul` · `choice` · `score` · ⚠ `并非 Jev 本身` `疑似 AI 生成`</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — 可复用的 GitHub Action：由检查、AI 审查者与 Jev 共同把关的智能体修复循环。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ripwords · `TS` · ⚠ `无许可证`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — 面向证据感知的智能体交接与有界工作续跑的实验性协议。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · zsoxi · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jourdanlabs · `Py` · ⚠ `无许可证`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。
  <sub>`文章` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `厂商自报数据`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — 用确定性规则加 Jev 评估代码变更风险的 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · moezubair · `TS`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kalyanm45 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-dev](https://github.com/n-yokomachi/jev-dev)** — 把同一句话同时交给 Jev 和 LLM 判定，在一屏内对比情绪波动值与响应速度（日语）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · n-yokomachi · `TS` · ⚠ `无许可证`</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — 给 Claude Code 的六道校准闸门：规则、范围、意图、完成度等。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · rashedint32 · `JS`</sub>

- **[jev-guard](https://github.com/CMaintz/jev-guard)** — 在 LLM 智能体的工具调用执行前，交给 TypeSafe AI 的 Jev 审核——放行、阻止或挂起，不确定时安全失败。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · cmaintz · `TS`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — 证据门控的 Jev 问题包注册表：精选问题、黄金样例与实测证据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · dtduc-git · `Py`</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — 面向社区和应用的内容审核，由 Jev（TypeSafe）驱动：按类别给出概率，阈值由你掌控。支持 Discord。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · ohernandezdev · `Py`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul` · ⚠ `需早期访问`</sub>

- **[last-exit](https://github.com/0x963D/last-exit)** — 由 Jev 驱动的赛博朋克边境遭遇战：忽悠守卫，检查凭据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · 0x963d · `JS`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — 给 OMP 的模型裁决式权限闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · strml · `TS` · ⚠ `已归档`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — 给 OpenClaw 的可选类型化 Jev 决策，带 SecretRef 凭据与严格的 API 校验。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · olli0103 · `TS`</sub>

- **[openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp)** — 由 OpenRouter 驱动的高速 System One 决策网关与 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · ctmx · `Py`</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — 单智能体的 Pi 编程协处理器，带 Jev 语义闸门与基线对比 diff 审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kamilpostrozny · `TS`</sub>

- **[pkg-gate](https://github.com/hemanth/pkg-gate)** — 用 System One 给 npm 生命周期脚本做安装前安全闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · hemanth · `JS`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — 检测 AI 智能体循环中的语义停滞。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ashutoshvjti · `TS`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One 搜索：用类型化判断与仓库证据导航与追踪代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · cpaczek · `TS`</sub>

- **[shade-arena-jev-monitor](https://github.com/nican2018/shade-arena-jev-monitor)** — 评估 Jev 作为智能体破坏行为的快速监控与动作闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · nican2018 · `Py`</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town：客厅电视上的社交推理派对游戏，由 Jev 主持。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · tpaulshippy · `Rb` · ⚠ `无许可证`</sub>

- **[siege](https://github.com/vnmoorthy/siege)** — SIEGE：200 人对战一个智能体，一道会学习的类型化动作闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · vnmoorthy · `TS`</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — 开源 Chrome 扩展：用 Jev 过滤 AI 生成的文字与广告。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · neddes · `JS`</sub>

- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** — 基于 TypeSafe Jev（System One 模型）的 LLM 网关护栏与模型路由器，附带独立的准确率与校准评估。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · aniruddh-krovvidi · `Py` · ⚠ `无许可证`</sub>

- **[trustgate](https://github.com/ndolinschi/trustgate)** — TrustGate：面向独立媒体的信任与安全闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — 基于 Jev 的三条可组合判断流水线：工单分拣、可观测性等。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shivam2003-dev · `Py`</sub>

- **[wakegate](https://github.com/shitianfang/wakegate)** — 在唤醒一个休眠智能体之前，先问 Jev 这次唤醒是否值得一次完整的 LLM 轮次。失败时默认放行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shitianfang · `TS`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — 给编程智能体的类型化判断层：从需求文档到发布的各道闸门。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★0 · zahrannnn · `TS` · ⚠ `无许可证`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
