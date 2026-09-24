# 总览

<sub>[awesome-jev](../../README.zh-CN.md) · [English](overview.md)</sub>

_介绍模型或整个领域，而非单一模式。_

这个决策的全部已收录例子 —— 共 451 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#总览)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐ — 把 TypeSafe 官方技能装进 Claude Code，让智能体自己写出正确的 Jev 调用，不必每次手动贴 API 结构。
  <sub>`官方文档` · ★2,036 · `sh`</sub>

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐ — Claude Code 插件背后的官方技能仓库，里面的 SKILL.md 教会智能体如何使用 System One API。
  <sub>`插件` · ★2,036 · `sh`</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐ — 一个可直接替换 TypeSafeClient 的适配器，底层走普通 LLM API —— 没有 Jev 权限也能跑 Jev 形状的代码。
  <sub>`SDK` · ★285 · `Py`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐ — 官方 TypeScript 客户端。同时提供 ESM、CJS 和类型声明，辅助函数是小写的 choice()/score()/noul()。
  <sub>`SDK` · ★232 · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐ — 官方 Python 客户端。含同步与异步客户端、支持 retry-after 的重试策略，以及 Choice/Score/Noul 辅助类。
  <sub>`SDK` · ★219 · `Py` · `choice` · `score` · `noul`</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐ — 唯一的端点 POST /v1/systemone，给出三种问题类型的完整请求与应答结构。
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐ — 权威参数表：jev-1.13.0、输入 $0.042/Mtok 且输出免费、64k 上下文、state 加最长问题 32k、仅支持文本输入。
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐ — 三个原语各自的用途与 criteria 写法，含 Choice 最多 255 个选项、Score 只能 2–10 级这些硬限制。
  <sub>`官方文档` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐ — 发布博文：什么是 System One 模型、为什么要把决策从生成里拆出来，以及厂商自报的延迟与成本数字。
  <sub>`文章` · Diogo Almeida · ⚠ `厂商自报数据`</sub>

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐ — 厂商自己列出的失效场景：字面化理解、算术与计数、日期比较、间接指代、夹杂大量无关细节的长 state、对抗性内容。
  <sub>`官方文档`</sub>

- **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐ — 厂商自己的分类体系：五大类、十九个行业方向、十种决策形态（从分类一直到结构化数据抽取）。
  <sub>`官方文档`</sub>

- **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)** — 一个编程智能体，其托管网关转售 Jev，还提供一个免费档位的模型 id。
  <sub>`平台集成` · ★209,715 · `TS`</sub>

- **[langchain](https://github.com/langchain-ai/langchain)** — 智能体工程平台。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★146,958 · langchain-ai · `Py`</sub>

- **[litellm](https://github.com/BerriAI/litellm)** — 高性能 AI 网关：Rust 内核加 Python SDK，以 OpenAI 或原生格式调用上百种 LLM API。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★59,514 · berriai · `Py`</sub>

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)** — 深度整合 IDE 的编程智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★33,049 · can1357 · `TS`</sub>

- **[ai](https://github.com/vercel/ai)** — TypeScript 的 AI 工具包，来自 Next.js 的作者们。 <sub>(机翻)</sub>
  <sub>`SDK` · ★26,922 · vercel · `TS`</sub>

- **[openwork](https://github.com/different-ai/openwork)** — 某协作工具的开源替代品。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★23,715 · different-ai · `TS` · ⚠ `并非 Jev 本身`</sub>

- **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)** — 包装同步与异步客户端，把每次 system_one 调用记录成一个可追踪的 span。
  <sub>`开源项目` · ★22,211 · `Py`</sub>

- **[laya](https://github.com/NandhaKishorM/laya)** — 非自回归的 System 1 决策引擎：一次前向传播即可对任意文本给出 choice、score 与是非判断，支持 100 多种语言，并按请求路由到合适的检查点。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★21,147 · nandhakishorm · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[pydantic-ai](https://github.com/pydantic/pydantic-ai)** — Python 做 AI 的方式：智能体、实时语音、图像生成、嵌入。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20,133 · pydantic · `Py`</sub>

- **[eliza](https://github.com/elizaOS/eliza)** — 开源的智能体操作系统。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19,474 · elizaos · `TS`</sub>

- **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)** — 在 Jev 之上实现 Effect 的 DecisionModel 接口，并罕见地坦白说明取整行为尚未核实。
  <sub>`平台集成` · ★16,195 · `TS` · `choice` · `score` · `noul`</sub>

- **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)** — Rust 集成，选项数量在编译期检查 —— 超过 255 个选项的 Choice 会编译失败，而不是运行时才报错。
  <sub>`平台集成` · ★8,713 · `Rs` · `choice` · `score` · `noul`</sub>

- **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)** — 一个 Go 网关 provider，对原生 API 做一比一透传 —— 官方 SDK 只需改 base URL 即可使用。
  <sub>`开源项目` · ★8,300 · `Go`</sub>

- **[deep-searcher](https://github.com/zilliztech/deep-searcher)** — 开源的深度研究替代方案，在私有数据上推理与检索。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★8,282 · zilliztech · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[kev](https://github.com/jaredpalmer/kev)** — 一套可训练、可自托管的 Jev-like 决策模型，API 与 System One 兼容 —— 官方 SDK 可以直接指向你自己的服务。
  <sub>`Jev 替代实现` · ★6,236 · Jared Palmer · `Py` · `choice` · `score` · `noul` · ⚠ `并非 Jev 本身`</sub>

- **[laya-mlx](https://github.com/mizorewww/laya-mlx)** — 给 Laya 类型化决策模型的原生 MLX 运行时：短决策 7–14 毫秒，不生成文本。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6,048 · mizorewww · `Py`</sub>

- **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)** — 一个接进 adapter registry 的「JSON Schema 转问题」编译器，并诚实说明了它无法支持的场景。
  <sub>`平台集成` · ★5,079 · `Py` · `choice` · `score` · `noul`</sub>

- **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)** — 带专门 System One 协议的 Ruby provider，是 Ruby 侧接入 Jev 的主要路径。
  <sub>`平台集成` · ★4,404 · `Rb` · `choice` · `score` · `noul`</sub>

- **[SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev)** — 一个独立的「语义 if」实现，开门见山声明与 Jev 和 TypeSafe 无隶属关系。
  <sub>`Jev 替代实现` · ★4,125 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[ax](https://github.com/ax-llm/ax)** — TypeScript 版的 DSPy 框架。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2,946 · ax-llm · `TS`</sub>

- **[memsearch](https://github.com/zilliztech/memsearch)** — 面向多个 AI 编程智能体的持久化统一记忆层。 <sub>(机翻)</sub>
  <sub>`插件` · ★2,649 · zilliztech · `Py`</sub>

- **[NanoJev](https://github.com/TianyuCodings/NanoJev)** — 自称 Jev 的「nano 复刻版」，用途是拿来读，不是拿来上生产。
  <sub>`Jev 替代实现` · ★2,137 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[vellum-assistant](https://github.com/vellum-ai/vellum-assistant)** — 易于配置的 AI 助手：全天候工作、了解你的偏好。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1,313 · vellum-ai · `TS`</sub>

- **[jevlike](https://github.com/vinnylarouge/jevlike)** — 一个独立可训练的模型，输入输出形状与 Jev 相同：文本加 N 个选项进，每个选项一个概率出，单次前向完成。
  <sub>`Jev 替代实现` · ★1,274 · vinnylarouge · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[celesto](https://github.com/CelestoAI/celesto)** — 给 AI 智能体的安全持久化计算环境。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★972 · celestoai · `Py`</sub>

- **[awesome-jev (heyjunpenn)](https://github.com/heyjunpenn/awesome-jev)** — 覆盖最广的同类目录：数百个项目、六种语言，且它的 README 本身就是被解析的数据源。
  <sub>`开源项目` · ★782 · heyjunpenn · `TS`</sub>

- **[localjev](https://github.com/githubnext/localjev)** — GitHub Next 用 TypeScript 写的本地 Jev 兼容 POST /v1/systemone 接口：在打过补丁的 vLLM 上，通过一步式结构化读取从 DiffusionGemma 模型得到概率。它重新实现的是协议，而不是模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★739 · githubnext · `TS` · ⚠ `并非 Jev 本身`</sub>

- **[distill](https://github.com/samuelfaj/distill)** — 用远更少的 token 完成远更多的事。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★688 · samuelfaj · `Rs`</sub>

- **[aiavatarkit](https://github.com/uezo/aiavatarkit)** — 快速构建基于 AI 的对话式虚拟形象。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★678 · uezo · `Py`</sub>

- **[kody](https://github.com/kentcdodds/kody)** — 你的助手之家：AI 智能体所需的记忆、密钥、代码与自动化。 <sub>(机翻)</sub>
  <sub>`插件` · ★672 · kentcdodds · `TS`</sub>

- **[von](https://github.com/wfzyx/von)** — 开源的 System One 决策模型：非自回归、15 毫秒以内，可在本地替换 TypeSafe Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★601 · wfzyx · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[req_llm](https://github.com/agentjido/req_llm)** — 基于 Req 和 Finch 的可组合 Elixir LLM 交互库。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★582 · agentjido · `Ex`</sub>

- **[simple-jev](https://github.com/featherless-ai/simple-jev)** — 通过读取 next-token logits，把任意开源权重模型变成 Jev 形状的端点 —— JSON 由服务端组装，而不是模型生成。
  <sub>`Jev 替代实现` · ★505 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev-chat-windows](https://github.com/jev-chat/jev-chat-windows)** — 微信（Windows）旁挂回复辅助：截图加本地 OCR 读消息，Jev 判断意图，生成候选，发送永远手动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★469 · jev-chat · `Py`</sub>

- **[jev-skill](https://github.com/wuyoscar/jev-skill)** — 一个 agent 技能加 CLI：校验三种原语、在产生计费调用前要求明确同意、并禁止在模拟时编造输出。
  <sub>`插件` · ★464 · `Py` · `choice` · `score` · `noul`</sub>

- **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)** — 一个同类目录，主打生态广度：来源锚定到具体 commit、四语 README、以及一个生成式站点。
  <sub>`开源项目` · ★461 · logicrw · `JS`</sub>

- **[smithers](https://github.com/smithersai/smithers)** — Smithers：用简单 TypeScript 配置定义工作流的智能体工作流框架。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★421 · smithersai · `TS`</sub>

- **[rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow)** — Jev 的开源本地版：由 LLM 产出类型化决策，且不生成任何 token。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★395 · rizzo-ai-academy · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev-experiments](https://github.com/dabit3/jev-experiments)** — Nader Dabit 的一组 Jev 小实验，每个目录一个：提交审查、shell 防护、发送防护、日志哨兵、即时搜索、重排、语音轮次检测等。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★378 · dabit3 · `TS` · ⚠ `无许可证`</sub>

- **[openjev](https://github.com/razorback16/openjev)** — 基于开源扩散模型的 Jev 兼容决策服务。
  <sub>`Jev 替代实现` · ★378 · razorback16 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[laya](https://github.com/receptron/laya)** — 通过 ONNX Runtime 从 Node.js／TypeScript 运行开源的 Jev 兼容 System-1 决策模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★371 · receptron · `TS`</sub>

- **[decider](https://github.com/Mapika/decider)** — 一族 System One 风格的模型，从开源基座微调而来，做单次类型化决策。
  <sub>`Jev 替代实现` · ★342 · mapika · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac)** — 微信消息意图识别悬浮窗（macOS）：看屏加本地小模型判断意图与风险，再生成回复候选。纯只读。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★333 · jev-chat · `Py`</sub>

- **[openjev-sglang](https://github.com/ekzhang/openjev-sglang)** — 用开源模型提供的 Jev 兼容端点，仅做 prefill。
  <sub>`Jev 替代实现` · ★307 · ekzhang · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[Open-Jev](https://github.com/Zefan-Cai/Open-Jev)** — Open-Jev-27B：开放权重模型，针对给定的上下文、问题和候选项直接返回带类型的概率，而不生成答案——一个可以自己运行的 Jev 式决策模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★295 · zefan-cai · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)** — 最适合刚拿到 API 的人。把 Jev 接进 Claude Code、Claude Desktop、Codex 和 Pi，随时做 Choice / Score / Noul。
  <sub>`插件` · ★287 · `Go` · `choice` · `score` · `noul`</sub>

- **[third-hand](https://github.com/shhivv/third-hand)** — 由决策模型驱动的 computer-use 助手。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★286 · shhivv · `Swift`</sub>

- **[orchestkit](https://github.com/yonatangross/orchestkit)** — 面向 Claude Code 的完整 AI 开发工具包：106 个技能、36 个智能体、171 个钩子。 <sub>(机翻)</sub>
  <sub>`插件` · ★283 · yonatangross · `TS`</sub>

- **[pi-fabric](https://github.com/monotykamary/pi-fabric)** — 给 Pi 的可编程工具与智能体运行时。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★258 · monotykamary · `TS`</sub>

- **[jeff](https://github.com/logan-markewich/jeff)** — 自托管的 Jev 直接替代品，底层由 GliFormer 驱动。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★233 · logan-markewich · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[crush-monitor](https://github.com/FerryCorleone/crush-monitor)** — 用 Jev 分析微信聊天的情绪、意图与回复表现，本机部署、自带密钥。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★207 · ferrycorleone · `TS`</sub>

- **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)** — 一个同类目录，提交由 Jev 自己审核，其多语言社区客户端清单相当完整。
  <sub>`开源项目` · ★203 · fatwang2 · `JS`</sub>

- **[djev-spark](https://github.com/mmastrac/djev-spark)** — 在 DGX Spark 上跑 DiffusionGemma NVFP4 结构化决策的容器配方。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★189 · mmastrac · `TS` · ⚠ `无许可证`</sub>

- **[openwhisper](https://github.com/Knuckles92/OpenWhisper)** — 基于 Whisper 的本地语音转写、听写与会议记录。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★188 · knuckles92 · `Py`</sub>

- **[Jevmind](https://github.com/dealerdefi/Jevmind)** — 把智能体的决策从它的文字中抽离出来集中管理：带置信度的类型化答案，经过用代码写的关卡，封存进账本，被评分并用于学习。默认在本地规则大脑上离线运行，一个开关即可换成 Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★166 · dealerdefi · `Py`</sub>

- **[runline](https://github.com/Michaelliv/runline)** — 给智能体的代码模式。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★164 · michaelliv · `TS` · ⚠ `无许可证`</sub>

- **[laya-ultrafast](https://github.com/ipenywis/laya-ultrafast)** — 与 jev-ultrafast 相同，但换成 Laya。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★145 · ipenywis · `Py`</sub>

- **[webctl](https://github.com/dorkitude/webctl)** — 给智能体用的智能网页搜索 CLI，由 Jev 支撑，大幅省 token。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★139 · dorkitude · `Go`</sub>

- **[dasheng](https://github.com/wquguru/dasheng)** — 英文朗读评分：流式 ASR 听，Jev 逐词判定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★138 · wquguru · `JS` · ⚠ `无许可证`</sub>

- **[OpenJev](https://github.com/SiliconLabAI/OpenJev)** — 开源版 Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★121 · siliconlabai · `TS` · ⚠ `并非 Jev 本身`</sub>

- **[stanley-code](https://github.com/devagrawal09/stanley-code)** — 给编程智能体的有界 Jev 工作流。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★114 · devagrawal09 · `TS`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 —— 面向 Jev 这类类型化决策模型的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★107 · fstandhartinger · `Py`</sub>

- **[open-jev](https://github.com/daseinlabs/open-jev)** — 带自定义微调的开源 Jev 实现。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★107 · daseinlabs · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev)** — Laya 对比 Jev：本地 MLX 与托管 API 并排玩恐龙跑酷，带实时指标。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★94 · virajbhartiya · `Py`</sub>

- **[advocaat](https://github.com/pithings/advocaat)** — 一个小巧的类型化客户端，用来对你自己的数据提问。
  <sub>`SDK` · ★91 · pithings · `TS`</sub>

- **[jevchat](https://github.com/kyle-pena-nlp/jevchat)** — 把 Jev 变成聊天机器人。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★90 · kyle-pena-nlp · `Py` · ⚠ `无许可证`</sub>

- **[jev-voice](https://github.com/kevinbadi/jev-voice)** — 对你的 Mac 说话：本地 whisper.cpp + 每条命令一次 Jev 调用 + macOS 自动化。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★84 · kevinbadi · `Py`</sub>

- **[jev-leftpad](https://github.com/f/jev-leftpad)** — 用 Jev 给字符串做左填充。就是想试试。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★83 · f · `JS`</sub>

- **[james_library](https://github.com/topherchris420/james_library)** — R.A.I.N. Lab：一个实验性的科学智能体架构，把快速的本地判断、独立的概率判断与推理分离开来。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★74 · topherchris420 · `Rs`</sub>

- **[captaincore](https://github.com/CaptainCore/captaincore)** — 自动化 WordPress 运维的命令行应用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★71 · captaincore · `Go`</sub>

- **[agent-router](https://github.com/nidhi-singh02/agent-router)** — CLI：为一个任务挑选编程智能体与模型／推理强度，然后启动它。 <sub>(机翻)</sub>
  <sub>`插件` · ★70 · nidhi-singh02 · `TS`</sub>

- **[djev](https://github.com/mmastrac/djev)** — 在 DiffusionGemma 上做 Jev 式结构化决策的示例服务。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★68 · mmastrac · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[dspy-typesafeify](https://github.com/typesafeainate/dspy-typesafeify)** — 给 dspy Signature 加一个装饰器，在合适处自动改用 TypeSafe。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★63 · typesafeainate · `Py`</sub>

- **[jevk5](https://github.com/allebee/jevk5)** — JevK5：TypeSafe Jev 的开放权重替代品，一次前向传播即给出带概率的类型化决策，权重采用 Apache-2.0。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★61 · allebee · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev-paint](https://github.com/achimala/jev-paint)** — 用 Jev 做艺术创作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★56 · achimala · `JS`</sub>

- **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)** — 一个开源语义决策引擎，本地跑零样本模型，其 FastAPI 服务已验证与官方 SDK 协议兼容。
  <sub>`Jev 替代实现` · ★56 · deepanwadhwa · `Py` · `choice` · `score` · `noul` · ⚠ `并非 Jev 本身`</sub>

- **[ruby_decision_model](https://github.com/obie/ruby_decision_model)** — 面向 Jev 这类决策模型的 Ruby 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★50 · obie · `Rb`</sub>

- **[jev-rules](https://github.com/EliaAlberti/jev-rules)** — 由 Jev 挑出哪些规则适用于当前提示，让模型只看到相关的那些。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★49 · eliaalberti · `JS`</sub>

- **[system-one](https://github.com/iamaamir/system-one)** — 面向 TypeScript 与 Pi 的、与提供方无关的 System One 运行时。 <sub>(机翻)</sub>
  <sub>`SDK` · ★48 · iamaamir · `TS` · ⚠ `无许可证`</sub>

- **[jeview](https://github.com/andududu/jeview)** — 非官方的本地可视化工具：实时查看你的代码发出的每一次 Jev 调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★47 · andududu · `JS`</sub>

- **[jev-seo](https://github.com/AkashPriyadarshii/jev-seo)** — 用 Rust 写的 agent 优先 SEO/GEO CLI 套件与 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★43 · akashpriyadarshii · `Rs`</sub>

- **[litjev](https://github.com/zhengxuyu/litjev)** — 把任意现成 LLM 变成一个 Jev 式的决策层。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★43 · zhengxuyu · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[openthai-systemone](https://github.com/iapp-technology/openthai-systemone)** — OpenThai-SystemOne：开源的泰语加英语 System One 决策模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★43 · iapp-technology · `Py`</sub>

- **[jev-foundation-models](https://github.com/peterfriese/jev-foundation-models)** — 轻量的原生 Swift 6 桥接，把 Jev 接入 Apple 的 Foundation Models。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★42 · peterfriese · `Swift`</sub>

- **[jev-mcp](https://github.com/burnigtm/jev-mcp)** — 把 TypeSafe Jev 接入 Cursor、Codex 等任意 MCP 客户端编码流程的 MCP 服务器。 <sub>(机翻)</sub>
  <sub>`插件` · ★42 · burnigtm · `TS`</sub>

- **[call-coach-ai](https://github.com/ZeroGold/call-coach-ai)** — 由 Jev 驱动的通话教练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★41 · zerogold · `TS`</sub>

- **[cultivar](https://github.com/pinecone-io/cultivar)** — 在沙盒里跨环境测试你的 Agent 技能与文档。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★41 · pinecone-io · `Py`</sub>

- **[laya-server](https://github.com/1Panel-dev/laya-server)** — 为 Laya 结构化决策模型提供的自托管 API 与网页界面，兼容 TypeSafe Jev 的 API 格式。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★41 · 1panel-dev · `TS` · ⚠ `并非 Jev 本身`</sub>

- **[solar-mini4-jev](https://github.com/hunkim/solar-mini4-jev)** — 一个即插即用的封装：让 Upstage 的 Solar 模型以 Jev System One 的 API 形状对外提供服务——noul、choice、score 使用相同的 schema，并提供自带 key 的托管端点。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★41 · hunkim · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill)** — 给 Hermes 及其他智能体用的技能，用来向 Jev 提问。 <sub>(机翻)</sub>
  <sub>`插件` · ★39 · shantanugoel · `Py`</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)** — 一个模仿其结构化输出形状的网关，用于与之对比测试。
  <sub>`基准测试` · ★38 · iammrduncan · `TS`</sub>

- **[jev-tree](https://github.com/Chuf-H/jev-tree)** — 原生面向 Jev 的概率树与图运行时，用于可验证的多步决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★37 · chuf-h · `Py`</sub>

- **[jev-spring-boot-starter](https://github.com/danvega/jev-spring-boot-starter)** — 给 Spring Boot 4 的简单 Jev starter，基于 Spring MVC 与 RestClient。 <sub>(机翻)</sub>
  <sub>`插件` · ★36 · danvega · `Java` · ⚠ `无许可证`</sub>

- **[jevify](https://github.com/fidecastro/jevify)** — 把任意 LLM 以类 Jev 端点形式提供服务的极简方案。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★36 · fidecastro · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev_local](https://github.com/Argos1111/jev_local)** — 用本地 LLM 复刻 Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★35 · argos1111 · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[OpenSourceJev](https://github.com/sabeel111/OpenSourceJev)** — 把 LLM 变成类 Jev 系统。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★33 · sabeel111 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[pijev](https://github.com/TypeLLM/pijev)** — 对 Jev 在不同选项顺序下的回答取平均——所有排列在一次请求中完成——并保证 Brier 分数与对数损失不劣于这些排列的平均水平。只需改一行 import。 <sub>(机翻)</sub>
  <sub>`SDK` · ★33 · typellm · `Py`</sub>

- **[clash-jev](https://github.com/bytelabs-oss/clash-jev)** — 没有训练策略的皇室战争机器人：每个决策都由 Jev 现场做出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★32 · bytelabs-oss · `Py`</sub>

- **[is-jeven](https://github.com/wobsoriano/is-jeven)** — 它是偶数吗？问 Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★32 · wobsoriano · `JS`</sub>

- **[jev (Elixir/OTP)](https://github.com/dannote/jev)** — 把 Jev 做成 OTP 进程：从 GenServer 回复，并对答案做模式匹配。
  <sub>`SDK` · ★32 · dannote · `Ex`</sub>

- **[jev-skill-suggester](https://github.com/win4r/jev-skill-suggester)** — 用 Jev 做有界的已安装技能推荐，含 Python CLI。 <sub>(机翻)</sub>
  <sub>`插件` · ★32 · win4r · `Py`</sub>

- **[refgarden](https://github.com/AlbionaHoti/refgarden)** — 面向创作者的空间参考浏览器：本地 Jev 查询选择、元数据高亮与带来源链接的合集。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★30 · albionahoti · `TS` · ⚠ `并非 Jev 本身`</sub>

- **[st-jeved](https://github.com/mossyfield/ST-jeved)** — SillyTavern 扩展：度量每条回复，并在规则命中时指导叙述者。 <sub>(机翻)</sub>
  <sub>`插件` · ★30 · mossyfield · `JS`</sub>

- **[sys1](https://github.com/alvarobartt/sys1)** — 用 Rust 编写、兼容 System One 的 API，面向 Laya 等开放决策模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★30 · alvarobartt · `Rs` · ⚠ `并非 Jev 本身`</sub>

- **[jev-explained](https://github.com/davila7/jev-explained)** — Jev 讲解。 <sub>(机翻)</sub>
  <sub>`教程` · ★29 · davila7 · `TS`</sub>

- **[jev-trades](https://github.com/zadescoxp/Jev-Trades)** — 用 Jev 驱动的交易机器人。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★29 · zadescoxp · `Py`</sub>

- **[laya-vs-jev-arena](https://github.com/PromptEngineer48/laya-vs-jev-arena)** — Laya（开源本地）对比 Jev（API）：两个模型比赛贪吃蛇。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★29 · promptengineer48 · `JS`</sub>

- **[Jev-Quantum](https://github.com/karminski/Jev-Quantum)** — 兼容 Jev 协议的随机基线：讲 noul、choice、score，但不读提示词，答案来自高速伪随机数——可以当 mock，也可以作为路由评测的下界。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★28 · karminski · `Rs` · ⚠ `并非 Jev 本身`</sub>

- **[jevify](https://github.com/altryne/jevify)** — 一个 agent 技能：发现适合用 Jev 的场景、设计类型化问题，并从近期社区实验中学习。 <sub>(机翻)</sub>
  <sub>`插件` · ★27 · altryne · `Py`</sub>

- **[typesafe](https://github.com/krzyzanowskim/TypeSafe)** — Swift 版 TypeSafe SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★27 · krzyzanowskim · `Swift`</sub>

- **[jev-register-tool](https://github.com/2951461586/Jev-Register-Tool)** — Jev 从申请到建密钥的全链路工具，纯 HTTP 无浏览器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★26 · 2951461586 · `Py` · ⚠ `无许可证`</sub>

- **[loki](https://github.com/wundercorp/loki)** — 与你一同演进的智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★26 · wundercorp · `Py`</sub>

- **[OpenJev](https://github.com/zhangcy122/OpenJev)** — OpenJev：TypeSafe Jev 的开源替代品。由开源模型驱动的带类型概率决策 API（Choice、Noul、Score）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★26 · zhangcy122 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev-cli](https://github.com/shaharia-lab/jev-cli)** — TypeSafe AI Jev 模型的命令行工具：对任意文本提出是非题、多选题和评分题，并得到校准后的答案。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★25 · shaharia-lab · `Rs`</sub>

- **[duckdb-jev](https://github.com/colliber/duckdb-jev)** — DuckDB 扩展：把 Jev 的类型化答案作为真正的 SQL 类型返回。 <sub>(机翻)</sub>
  <sub>`插件` · ★24 · colliber · `C++`</sub>

- **[jev-judge-mcp](https://github.com/PyModel/jev-judge-mcp)** — 面向 MCP 智能体的带类型判断工具：把 TypeSafe Jev 模型包装成 verify、screen、find、classify、rerank、decide、compare 等工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★24 · pymodel · `Py`</sub>

- **[jev-playground](https://github.com/mizchi/jev-playground)** — 一个从 MoonBit 调用 Jev 的演练场：每种问题类型（score、choice、noul）各有一个命令行入口，并附有哪种组合模式更好的实测报告。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★23 · mizchi · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground)** — 社区版 TypeSafe AI 演练场：110 个用例、游戏、两难问题和模型挑战，可编辑提示、做 A/B 对比，并适配移动端。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20 · typesafeai · `TS`</sub>

- **[fastjev](https://github.com/chengyongru/fastjev)** — 以 SDK 为先、独立维护的 SemIf 分支，用于快速的自托管语义决策。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★19 · chengyongru · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jot](https://github.com/runta-dev/jot)** — 第一个面向 Jev 的通用 System One 智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19 · runta-dev · `TS` · ⚠ `无许可证`</sub>

- **[ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)** — 给某个 Ruby LLM 库做的结构化输出 provider。
  <sub>`平台集成` · ★19 · kieranklaassen · `Rb`</sub>

- **[Jev](https://github.com/mayank953/Jev)** — 六个实时并排的演示：Jev 负责决策，LLM 负责写字，代码掌控流程；LLM 一侧可在 Claude 与 Kimi 模型之间切换。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★18 · mayank953 · `JS`</sub>

- **[jev-to-answer](https://github.com/csskrtao/jev-to-answer)** — 答案之书jev
  <sub>`开源项目` · ★18 · csskrtao · `JS` · ⚠ `无许可证`</sub>

- **[notjev](https://github.com/9pings/notjev)** — 超快的类 Jev 服务器，与模型无关，可对接任何 OpenAI 兼容端点。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★18 · 9pings · `JS` · ⚠ `并非 Jev 本身`</sub>

- **[jevcore](https://github.com/PerryLink/jevcore)** — 面向 DeepSeek Harness、MCP 与原生 Node 的 TypeSafe Jev 封装：返回带类型的判断而非文字，默认离线。 <sub>(机翻)</sub>
  <sub>`SDK` · ★17 · perrylink · `TS`</sub>

- **[jevgraph](https://github.com/chenmingtang830/jevgraph)** — 用类型化 Jev 关系决策构建有证据支撑的知识图谱。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · chenmingtang830 · `Py`</sub>

- **[jevloop](https://github.com/zjunlp/JevLoop)** — 决策不再消耗大模型调用的智能体循环：零依赖、可离线运行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · zjunlp · `TS`</sub>

- **[jevocks](https://github.com/unicodeveloper/jevocks)** — 用 Jev 看每日股票状态。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · unicodeveloper · `TS` · ⚠ `无许可证`</sub>

- **[snap](https://github.com/emnlmn/snap)** — 从非结构化状态得到类型化决策：一次前向传播、零生成文本。本地、确定性、兼容 Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★17 · emnlmn · `Rs` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[go-jev](https://github.com/mattn/go-jev)** — TypeSafe Jev 的 Go SDK 与 CLI：从模型获得带类型的决策（是非、选择、评分）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★16 · mattn · `Go`</sub>

- **[jev-vs-ml](https://github.com/QuicqDev/Jev-vs-ML)** — Jev 与传统机器学习的对比。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★16 · quicqdev · `Py` · ⚠ `无许可证`</sub>

- **[hunch](https://github.com/carldaws/hunch)** — 面向 Ruby 与 Rails 的概率化控制流，由 TypeSafe Jev 驱动。 <sub>(机翻)</sub>
  <sub>`SDK` · ★15 · carldaws · `Rb`</sub>

- **[jev](https://github.com/BorisLeMeec/jev)** — 一个 Jev 的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★15 · borislemeec · `Go`</sub>

- **[jev-studio](https://github.com/utk2103/jev-studio)** — 如果你在试用 Jev，从这里开始会更省事。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★15 · utk2103 · `Py`</sub>

- **[jevvy](https://github.com/PanAchy/jevvy)** — 给编程智能体的 Jev 插件集。 <sub>(机翻)</sub>
  <sub>`插件` · ★15 · panachy · `TS`</sub>

- **[open-spark-jev](https://github.com/abhishek085/open-spark-jev)** — 受 Jev 与 System One 启发、基于 Qwen3 的开源本地决策模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★15 · abhishek085 · `Py`</sub>

- **[swift-typesafe](https://github.com/ainame/swift-typesafe)** — 非官方 Swift SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★15 · ainame · `Swift`</sub>

- **[jev-tetris](https://github.com/trungdq88/jev-tetris)** — 让 Jev 实时与其他 AI 模型对战俄罗斯方块。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · trungdq88 · `JS` · ⚠ `无许可证`</sub>

- **[typesafe-sdk-go](https://github.com/atharvamhaske/typesafe-sdk-go)** — TypeSafe AI 的非官方 Go SDK，与 TypeSafe AI 无关、未获其背书，是为了填补空缺而做的业余项目。 <sub>(机翻)</sub>
  <sub>`SDK` · ★14 · atharvamhaske · `Go`</sub>

- **[jev_stock](https://github.com/sosopop/jev_stock)** — 实验性框架：从结构化市场数据预测短期股价方向。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · sosopop · `Py` · ⚠ `无许可证`</sub>

- **[llm-typesafe](https://github.com/simonw/llm-typesafe)** — 为 LLM 命令行工具访问 Jev 及其他 TypeSafe AI 模型的插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★13 · simonw · `Py`</sub>

- **[typesafe-playground](https://github.com/kavehmz/typesafe-playground)** — 围绕 Jev 的交互式实验，从工单路由到带真实 AI 决策的 3D 驾驶仿真。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · kavehmz · `JS` · ⚠ `无许可证`</sub>

- **[typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router)** — 给 Hermes Agent 的技能路由：在模型调用之前，指出唯一值得加载的那个技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★13 · decrux9812 · `Py`</sub>

- **[jev-cli](https://github.com/tumf/jev-cli)** — 小巧的零依赖 Jev 命令行工具。 <sub>(机翻)</sub>
  <sub>`SDK` · ★12 · tumf · `Py`</sub>

- **[jevper](https://github.com/zhulinchng/jevper)** — 形似 Jev（TypeSafe System One）的分类封装，基于类 OpenAI 客户端：给出概率与置信度，而不是文本。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★12 · zhulinchng · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jevthoven](https://github.com/cocktailpeanut/jevthoven)** — 由 Jev 驱动的 AI 音乐（MIDI）生成器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · cocktailpeanut · `TS`</sub>

- **[snapjudge](https://github.com/Micha0827/snapjudge)** — 在 Apple Silicon 上用本地 Qwen 模型给出带类型的决策（choice / score / 是非），概率直接来自模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★12 · micha0827 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[typesafe-ai](https://github.com/Twister915/typesafe-ai)** — Rust 的类型化客户端，含异步与阻塞后端，以及可观测的重试。 <sub>(机翻)</sub>
  <sub>`SDK` · ★12 · twister915 · `Rs`</sub>

- **[jev-chat-for-twitch](https://github.com/ethanplusai/jev-chat-for-twitch)** — 用 Jev 过滤任意 Twitch 直播聊天的自带密钥 Chrome 扩展。 <sub>(机翻)</sub>
  <sub>`插件` · ★11 · ethanplusai · `JS`</sub>

- **[pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)** — 把 Jev 作为 pi 编程智能体的安静决策层。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · hyunjunjeon · `TS`</sub>

- **[swift-jev](https://github.com/d-date/swift-jev)** — TypeSafe AI Jev 的 Swift 客户端：返回带类型的判断，而不是文本。 <sub>(机翻)</sub>
  <sub>`SDK` · ★11 · d-date · `Swift`</sub>

- **[xtags](https://github.com/manifoldor/xtags)** — 在 X 的时间线上，给每条帖子标出它想让你干什么 —— 判断来自只返回概率、不生成文本的 Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · manifoldor · `JS`</sub>

- **[jev](https://github.com/okooo5km/jev)** — 在命令行里做类型化决策：一个非官方的、只用标准库的 Python CLI 与智能体技能，面向 TypeSafe 的 Jev 模型。 <sub>(机翻)</sub>
  <sub>`插件` · ★10 · okooo5km · `Py`</sub>

- **[jev-recipes](https://github.com/agencyenterprise/jev-recipes)** — 80 多个由 Jev 驱动的可组合 TypeScript 配方，覆盖 AI 智能体、检索、答案校验与对话流程。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · agencyenterprise · `TS`</sub>

- **[JevAny](https://github.com/weitianxin/JevAny)** — JevAny：面向强化学习、智能体与模型框架的校准决策层，一次预填充即可返回带类型的答案和选项概率——一个基于 Qwen 骨干的开放 27B 模型，并不是 Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10 · weitianxin · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jevernetes](https://github.com/sunil-sadasivan/jevernetes)** — 由 Jev 驱动的 Kubernetes 实时日志分析、上下文调查与智能体交接。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · sunil-sadasivan · `Py`</sub>

- **[jev_project_context](https://github.com/poiuyjie/jev_project_context)** — 面向 AI 编程智能体的证据优先长期实验记忆技能，可选接入 Jev 决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★9 · poiuyjie · `Py`</sub>

- **[jpp](https://github.com/Towow-ai/jpp)** — J++：一门实验性语言，拥有独立源码和 Rust 运行时，可以组合问题与方法。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · towow-ai · `Rs`</sub>

- **[typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go)** — Go SDK —— 类型化问题进，概率分布出。 <sub>(机翻)</sub>
  <sub>`SDK` · ★9 · tangerg · `Go`</sub>

- **[edgejev](https://github.com/yzfly/edgejev)** — 离线可用的本地类型化决策：4 核 CPU 单题 15.6 毫秒，ONNX 加 INT8。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · yzfly · `Py`</sub>

- **[jeq](https://github.com/cristianoliveira/jeq)** — 当 jev 遇上 jq 会怎样？可以用管道串联的“智能”，适合快速实验和脚本。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · cristianoliveira · `Go`</sub>

- **[jev-minesweeper](https://github.com/comoc/jev-minesweeper)** — 让 Jev 解浏览器扫雷的演示（日语）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · comoc · `JS` · ⚠ `无许可证`</sub>

- **[laya-jev-lab](https://github.com/yibie/laya-jev-lab)** — 类型化决策模型的独立实测：Jev 对比开源权重的 Laya。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · yibie · `Py`</sub>

- **[trade-jev](https://github.com/justinhe16/trade-jev)** — 在 NQ 十档盘口数据上回测 Jev 作为买／卖／持有交易者的表现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · justinhe16 · `Py`</sub>

- **[typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk)** — 社区维护的 .NET SDK，支持 noul、choice、score 三种类型化问题。 <sub>(机翻)</sub>
  <sub>`SDK` · ★8 · saibimajdi · `C#`</sub>

- **[jev-grand-prix](https://github.com/enoyola/jev-grand-prix)** — 一个 F1 赛车游戏：Jev 选择赛车线与踏板，并逐条赛道学习。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · enoyola · `JS`</sub>

- **[jev-mcp](https://github.com/rashedInt32/jev-mcp)** — 把 TypeSafe Jev 暴露为带类型、经校准的判断工具的 MCP 服务器：classify、score、check 与批量提问，并以 Claude Code 插件形式发布。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · rashedint32 · `TS`</sub>

- **[jev-mcp](https://github.com/arunav25/jev-mcp)** — 把 JEV 接入 MCP 客户端，并用共享数据集和可衡量的指标，将它的判断与通用 LLM 进行对比。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · arunav25 · `JS`</sub>

- **[jev_jsonschema](https://github.com/Kiln-AI/jev_jsonschema)** — 把一份 JSON Schema 丢给 Jev API，拿回 JSON。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · kiln-ai · `Py`</sub>

- **[jevgo](https://github.com/devbackend/jevgo)** — TypeSafe AI System One API（Jev）的非官方 Go 客户端：输入带类型的问题，输出校准后的答案。 <sub>(机翻)</sub>
  <sub>`SDK` · ★7 · devbackend · `Go`</sub>

- **[switchboard](https://github.com/ruban-24/switchboard)** — 开源、模型无关的决策路由器，面向 Claude Code 和 Codex。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · ruban-24 · `TS`</sub>

- **[typesafe-sdk](https://github.com/joshmn/typesafe-sdk)** — typesafe.ai 的 Ruby 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★7 · joshmn · `Rb`</sub>

- **[awesome-jev](https://github.com/daftAI2026/awesome-jev)** — System One / Jev 社区目录：围绕类型化决策的 GitHub 项目与文章。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · daftai2026 · `TS` · ⚠ `无许可证`</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Jev 的基准与 playground：国际象棋，以及语音转写中的说话对象判定。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · wondertwins · `Py`</sub>

- **[jev-canvas](https://github.com/gaborishka/jev-canvas)** — 用语音加手指指向在 tldraw 画布上作画：由 Jev 决定动作与目标。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · gaborishka · `JS`</sub>

- **[jev-chat-windows-deepseek-jev](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev)** — Windows 微信回复助手：大模型生成话术、Jev 判断排序，支持可取消的三秒自动发送。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · aimark-dai · `Py`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — 可复现的早期访问评测：Jev 在韩语理解与医学文本上的表现，附运行时与成本证据。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · mahlernim · `Py` · ⚠ `无许可证`</sub>

- **[jev-search](https://github.com/larguesa/jev-search)** — 通过 OpenRouter 用 Jev 做实验性语义行检索的 Python CLI。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · larguesa · `Py`</sub>

- **[jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver)** — Chrome 扩展：用 Jev 遮住让人分心的 YouTube 视频，想看随时可展开。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · jaibhasin · `JS` · ⚠ `无许可证`</sub>

- **[jevtest](https://github.com/joshhu/jevtest)** — 情绪测谎器：嘴上说「好」，心里真的好吗？用 Jev 实时判断并与普通 LLM 对照。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · joshhu · `TS` · ⚠ `无许可证`</sub>

- **[learn-jev-end-to-end](https://github.com/harshithsunku/learn-jev-end-to-end)** — 端到端学习 Jev 的免费实践课程：用“快脑”（Jev）加“慢脑”（LLM）构建 13 个智能体用例，只需一个 OpenRouter key。 <sub>(机翻)</sub>
  <sub>`教程` · ★6 · harshithsunku · `Py`</sub>

- **[mcts-agent](https://github.com/lhemerly/mcts-agent)** — 用 System One 原语做判别式蒙特卡洛树搜索。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · lhemerly · `Py`</sub>

- **[midscene-jev-runner](https://github.com/KiritoKing/midscene-jev-runner)** — 社区维护的 Midscene Test JEV 运行器集成。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★6 · kiritoking · `TS`</sub>

- **[ruling](https://github.com/bradAGI/ruling)** — 由本地模型给出带类型、经校准的决策，不生成文本。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★6 · bradagi · `Py` · ⚠ `并非 Jev 本身` `宣称未核实`</sub>

- **[secondlayer](https://github.com/ryanwaits/secondlayer)** — 把解码后的链上数据放进你自己的数据库，可自托管。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · ryanwaits · `TS`</sub>

- **[ai-elo-ranker](https://github.com/opaielsheikh/ai-elo-ranker)** — 由 Jev 驱动的高速递归 AI Elo 锦标赛引擎，采用瑞士轮匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · opaielsheikh · `Py` · ⚠ `无许可证`</sub>

- **[jev-2048](https://github.com/ARCJ137442/jev-2048)** — 带插桩的 2048 网页实验：每一步都是一次 Jev Choice。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · arcj137442 · `TS`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — Jev 的能力展示与研究：一次 show-and-tell 式的考察。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · lbotinelly · `TS`</sub>

- **[jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon)** — 用 Jev 玩《宝可梦红》。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · milanboers · `Py`</sub>

- **[jev-system-one](https://github.com/haseeb-heaven/jev-system-one)** — 打磨过的终端界面，输出答案的同时给出透明的决策报告。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · haseeb-heaven · `Py`</sub>

- **[jev4k](https://github.com/pambrose/jev4k)** — Jev 的 Kotlin DSL 与客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★5 · pambrose · `Kt`</sub>

- **[Jev_Ontology](https://github.com/dagfinndybvig/Jev_Ontology)** — 尝试把 Jev 与本体论结合起来。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · dagfinndybvig · `Py` · ⚠ `无许可证`</sub>

- **[jevlang](https://github.com/sumanmichael/jevlang)** — 用 Python 编写决策工作流最简单的方式：带“智能 if”的 Python。 <sub>(机翻)</sub>
  <sub>`SDK` · ★5 · sumanmichael · `Py`</sub>

- **[jevplayspokemon](https://github.com/anxkhn/JevPlaysPokemon)** — 让 Jev 通过 Showdown 和真实 ROM 玩第三世代宝可梦。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · anxkhn · `TS`</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD 基准 alpha 版与官方评测流程。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · johnhughes3 · `Py`</sub>

- **[OpenJev](https://github.com/xingwudao/OpenJev)** — OpenJev：受 Jev 启发、基于 TypeSafe.ai 理念的独立 System One 决策 API，提供 choice、score、noul 原语、本地模拟服务器以及 Python 和 TypeScript SDK。真实推理尚在计划中，与 TypeSafe AI 无关。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★5 · xingwudao · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs)** — 独立的 Rust SDK，同时提供异步与阻塞两种形式。 <sub>(机翻)</sub>
  <sub>`SDK` · ★5 · gilljon · `Rs`</sub>

- **[typesafe-ui](https://github.com/TypeSafeAI/typesafe-ui)** — shadcn 风格的可复用组件与区块，用于接入 TypeSafe AI。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · bunsdev · `TS` · ⚠ `无许可证`</sub>

- **[typesafe_sdk (Elixir)](https://github.com/nshkrdotcom/typesafe_sdk)** — 官方 SDK 的 Elixir 移植。
  <sub>`SDK` · ★5 · nshkrdotcom · `Ex`</sub>

- **[dohnuts.cpp](https://github.com/DreamBlooms/dohnuts.cpp)** — 同样的决策，在 CPU 上完成。一个能在个人电脑上运行的 System One 模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · dreamblooms · `C++` · ⚠ `并非 Jev 本身`</sub>

- **[jcm-router](https://github.com/adarshmishra07/jcm-router)** — 本地代理：逐条消息用 Jev 选择 Claude 模型与推理强度，并路由子智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · adarshmishra07 · `TS`</sub>

- **[jev-android](https://github.com/dougsong/jev-android)** — 由 Jev 驱动的 Kotlin Android UI 自动化 SDK，带无障碍运行时。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · dougsong · `Kt`</sub>

- **[jev-arena-nanojev](https://github.com/liao96312/jev-arena-nanojev)** — 完全本地的 NanoJev 网格决策游戏实验场，支持中文界面与多关卡。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · liao96312 · `Py` · ⚠ `无许可证`</sub>

- **[jev-bot](https://github.com/nssmd/jev-bot)** — 自托管的 Jev 决策工作台与飞书机器人：自动选择、概率与证据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · nssmd · `JS`</sub>

- **[jev-chat](https://github.com/adhyaay-karnwal/jev-chat)** — 由类型化 Jev 决策构成的聊天机器人：在 System One 概率上做分层推测解码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · adhyaay-karnwal · `Py`</sub>

- **[jev-cookbook](https://github.com/paramjeetn/jev-cookbook)** — TypeSafe AI Jev 的完整食谱：120 多个用例、10 个可运行示例、4 种组合模式。 <sub>(机翻)</sub>
  <sub>`教程` · ★4 · paramjeetn · `Py`</sub>

- **[jev-docs-zh](https://github.com/Bald0Wang/jev-docs-zh)** — Jev 官方使用文档的非官方中文翻译。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · bald0wang · `Py` · ⚠ `无许可证`</sub>

- **[jev-go](https://github.com/Gaurav-Gosain/jev-go)** — TypeSafe System One API 及其模型 Jev 的 Go 客户端：返回带类型的判断与校准概率，而不是生成文本。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · gaurav-gosain · `Go`</sub>

- **[jev-grug](https://github.com/mkotlikov/jev-grug)** — 帮 Jev 开口说话。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · mkotlikov · `TS`</sub>

- **[jev-realtime-trading](https://github.com/rthomas24/jev-realtime-trading)** — 在实时行情上跑的模拟交易智能体，每秒由 Jev 决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · rthomas24 · `TS`</sub>

- **[jev-trip](https://github.com/liaoyuhua/jev-trip)** — 两个大脑，一次旅行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · liaoyuhua · `TS`</sub>

- **[jev-wingman](https://github.com/1104480426-hash/jev-wingman)** — 基于 Jev 的聊天决策辅助，不挑 App（QQ／微信／飞书皆可），端上返回类型化判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · 1104480426-hash · `Java`</sub>

- **[jevopt](https://github.com/Ramneet-Singh/jevopt)** — 用 Jev 做智能的编译器优化决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · ramneet-singh · `Py`</sub>

- **[jevseek](https://github.com/blingdivinity/jevseek)** — DeepSeek 提出下一个 token，由 TypeSafe 的 Jev 来选择：把决策模型用作采样器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · blingdivinity · `Py`</sub>

- **[OpenJev](https://github.com/GPT-AGI/OpenJev)** — 兼容 Jev 的 System 开源 Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · gpt-agi · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[rubikjev](https://github.com/0xtrou/rubikjev)** — 用魔方谜题挑战 Jev 的智力。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · 0xtrou · `TS` · ⚠ `无许可证`</sub>

- **[rust-sysone](https://github.com/zcoder-run/rust-sysone)** — 非官方的 System One Rust 客户端。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · zcoder-run · `Rs`</sub>

- **[soupbase](https://github.com/spoonnotfound/soupbase)** — Jev 版海龟汤。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · spoonnotfound · `TS`</sub>

- **[sysone-bench](https://github.com/instax-dutta/sysone-bench)** — 首个独立的 System One 决策模型横评（Laya 对比 Jev）。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★4 · instax-dutta · `Py`</sub>

- **[typesafe-ai-go](https://github.com/kisshan13/typesafe-ai-go)** — 社区维护的 TypeSafe AI System One 评估 API 的 Go SDK，支持带类型的问题、流式构建器与重试。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · kisshan13 · `Go`</sub>

- **[typesafe-ai-java](https://github.com/jamilxt/typesafe-ai-java)** — 社区维护的 TypeSafe AI System One（Jev）API 的 Java SDK，并非 TypeSafe 官方产品。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · jamilxt · `Java` · ⚠ `无许可证`</sub>

- **[typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift)** — 非官方的 Swift 客户端库。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · alterhq · `Swift`</sub>

- **[alphaoptimizer](https://github.com/alpha-tales/alphaoptimizer)** — 由 Jev 驱动的 Codex 输出优化，让庞大的工具结果保持简洁可用。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · alpha-tales · `TS`</sub>

- **[awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases)** — 浏览基于 TypeSafe AI Jev 构建的真实用例与项目：内容审核、AI 智能体、模型路由等。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · seeapi · `Py`</sub>

- **[cairn-jev-lab](https://github.com/Cairn-ink/cairn-jev-lab)** — 测试你的 AI 应该记住什么：实验性的、感知来源的记忆准入评估器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · cairn-ink · `JS`</sub>

- **[cu-Jev](https://github.com/dtunai/cu-Jev)** — cuda-Jev：原生 CUDA 的 Jev System One 决策推理引擎，提供 Jev 兼容 API、示例和可复现的基准。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★3 · dtunai · `C` · ⚠ `并非 Jev 本身`</sub>

- **[dbt_jev](https://github.com/smithclay/dbt_jev)** — 在 dbt 中使用 jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · smithclay · `Py`</sub>

- **[everything-about-jev](https://github.com/qingshungLI/everything-about-jev)** — 关于 Jev 这个类型化决策模型的全面介绍。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · qingshungli · `Py`</sub>

- **[go-system-one](https://github.com/rcarmo/go-system-one)** — 当地鼠遇上 Jev：一个 Go 语言的 System One 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · rcarmo · `Go`</sub>

- **[Jev](https://github.com/cobusgreyling/Jev)** — 非官方的 TypeSafe Jev 展示：System One 决策，而不是聊天。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · cobusgreyling · `Py`</sub>

- **[jev-cli](https://github.com/jtsang4/jev-cli)** — TypeSafe AI Jev 评估模型的命令行工具：输入带类型的问题，输出结构化的 JSON 答案。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · jtsang4 · `TS`</sub>

- **[jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)** — 关于 Jev 概率校准、不确定性表达以及预测概率保真度的实验。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · kantahayashiai · `JS`</sub>

- **[jev-gomoku](https://github.com/XieChengYuan/jev-gomoku)** — 弈瞬：双 Jev 五子棋实验台，逐手查看模型决策，支持对局回放与实时对战。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · xiechengyuan · `JS` · ⚠ `无许可证`</sub>

- **[jev-java](https://github.com/Olti1947/jev-java)** — 地道的 Java SDK，对接 System One 决策引擎。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · olti1947 · `Java` · ⚠ `无许可证`</sub>

- **[jev-java](https://github.com/gudcks0305/jev-java)** — TypeSafe Jev 与 Vercel AI Gateway 的非官方 Java SDK，支持 Spring Boot 与 WebClient。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · gudcks0305 · `Java`</sub>

- **[jev-resume-disqualifier](https://github.com/AiPersonacademy/jev-resume-disqualifier)** — 亚 25 毫秒的简历自动淘汰引擎。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · aipersonacademy · `Py`</sub>

- **[jev-rs](https://github.com/abeldzan/jev-rs)** — 以异步为先的 TypeSafe AI API Rust SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · abeldzan · `Rs`</sub>

- **[jevtown](https://github.com/gaborishka/jevtown)** — 一个社交网络：真人写帖，一万个 AI 人格来回应。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · gaborishka · `JS`</sub>

- **[n8n-nodes-jev](https://github.com/vibe-with-me-tools/n8n-nodes-jev)** — TypeSafe Jev 的 n8n 社区节点：用你定义的问题对文本做分类、路由与打分，并得到概率。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · vibe-with-me-tools · `TS`</sub>

- **[new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe)** — 给 new-api 的 Jev 任务插件：原生 /v1/systemone、同步评估。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · ffattiger · `JS`</sub>

- **[origin-civilization](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)** — AI 生命与文明模拟：每个决策都由 Jev 做出。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · jacquesgariepy · `TS`</sub>

- **[pydantic-jev-examples](https://github.com/adtyavrdhn/pydantic-jev-examples)** — 用 Jev 增强 Pydantic AI 能力的小型可运行演示，每个一个文件。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · adtyavrdhn · `Py` · ⚠ `无许可证`</sub>

- **[should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all)** — 每十分钟问一次 Jev：AI 是否应该毁灭人类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · hellogumbo · `JS`</sub>

- **[sqlite3-jev](https://github.com/mattn/sqlite3-jev)** — 在 SQL 中调用 TypeSafe Jev（或 tensai serve）的 SQLite 扩展。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · mattn · `C`</sub>

- **[system-one-chess](https://github.com/dperezcabrera/system-one-chess)** — 通过 OpenRouter 与 Jev 下国际象棋。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · dperezcabrera · `Py`</sub>

- **[systemone-lite](https://github.com/fritzprix/systemone-lite)** — 玩具级的本地 System One 风格决策 API，与官方无关。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · fritzprix · `Py`</sub>

- **[SystemOneDotNet](https://github.com/JabbaKadabra/SystemOneDotNet)** — TypeSafe System One（Jev）的 .NET 客户端：输入带类型的问题，输出带概率与置信度的类型化答案。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · jabbakadabra · `C#`</sub>

- **[tinyjev](https://github.com/ankit-aglawe/tinyjev)** — 一个微型类 Jev 模型：一次前向传播回答 Choice、Score 与 Noul 问题并返回校准概率。支持 MLX 或 PyTorch，完全离线，兼容 System One 接口。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★3 · ankit-aglawe · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[typesafe-ai-rails](https://github.com/GenieRobot/typesafe-ai-rails)** — TypeSafe AI System One API 的社区版 Rails 集成，基于社区 typesafe-sdk gem：提供 Rails 配置、持久化的用量与成本记录，以及针对 Choice 和 Score 答案的可选置信度策略。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · genierobot · `Rb`</sub>

- **[typesafe-assist](https://github.com/JanOstrowka/typesafe-assist)** — 由 Jev 驱动的 Home Assistant 对话智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · janostrowka · `Py` · ⚠ `无许可证`</sub>

- **[typesafe-sdk-dotnet](https://github.com/hardkoded/typesafe-sdk-dotnet)** — TypeSafe AI 客户端 SDK 的非官方 .NET 移植（带类型的问题与答案）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · hardkoded · `C#`</sub>

- **[typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java)** — 社区维护的 Java 客户端（非官方）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · premo-cloud · `Java`</sub>

- **[typesafe-sdk-rust](https://github.com/codeitlikemiley/typesafe-sdk-rust)** — TypeSafe AI API 的 Rust SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · codeitlikemiley · `Rs`</sub>

- **[typesafe-sdk-swift](https://github.com/InsaneArts/typesafe-sdk-swift)** — TypeSafe AI 的 Swift SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · insanearts · `Swift`</sub>

- **[werr](https://github.com/pCwOrM/werr)** — 零记忆的 System-1 决策引擎，与 TypeSafe Jev 协议兼容的运行时，由“曼德博波动力学”驱动。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★3 · pcworm · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[agent-jev-tetris](https://github.com/Yasserbhb/Agent-JEV-Tetris)** — 用 JEV 玩俄罗斯方块。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · yasserbhb · `TS` · ⚠ `无许可证`</sub>

- **[ailerix](https://github.com/tylerjharden/ailerix)** — 类型安全的模型路由器：Jev 把每个请求归入一条类型化的目录路线。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · tylerjharden · `TS` · ⚠ `无许可证`</sub>

- **[auto-mode-for-paseo](https://github.com/obetomuniz/auto-mode-for-paseo)** — 一个 Paseo provider，用 Jev 路由 Codex 的每一轮。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · obetomuniz · `TS`</sub>

- **[barrunto](https://github.com/elpumberto/barrunto)** — Chrome 扩展：在你浏览 X 时用 Jev 分析帖子。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · elpumberto · `TS`</sub>

- **[bes-kelime-jev](https://github.com/mahmut-gundogdu/bes-kelime-jev)** — 无论你写什么，都只用五个词之一回答的聊天机器人（土耳其语）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · mahmut-gundogdu · `TS`</sub>

- **[btc-jev-signal](https://github.com/WebGrga/btc-jev-signal)** — 实验性的多周期 BTC 信号生成器，使用 Jev 概率与交易所数据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · webgrga · `TS` · ⚠ `无许可证`</sub>

- **[chat2jev](https://github.com/Chandler-Sun/chat2jev)** — 把传统的 chat completion API 请求转换为 TypeSafe Jev API 请求。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · chandler-sun · `TS`</sub>

- **[decisions-judge-mcp](https://github.com/clouatre-labs/decisions-judge-mcp)** — 把 AI 智能体的类型化决策做成一个 MCP 工具：是非概率（noul）、choice 和 score，一次快速请求完成。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · clouatre-labs · `JS`</sub>

- **[diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)** — 由 DiffusionGemma 与 SGLang 驱动的类 Jev 决策引擎——“长了眼睛的 Jev”。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★2 · hangzhi · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[emoji-jev](https://github.com/colinmcdermott/emoji-jev)** — 跟得上打字速度的 emoji 自动补全。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · colinmcdermott · `TS` · ⚠ `无许可证`</sub>

- **[git-jev-stage](https://github.com/ibrahemid/git-jev-stage)** — 用一句大白话描述来挑选要暂存的 Git 变更。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · ibrahemid · `TS`</sub>

- **[got-jev](https://github.com/phureewat29/jev-got)** — 以《权力的游戏》为素材的 Jev 概念验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · phureewat29 · `TS` · ⚠ `无许可证`</sub>

- **[ha-conversation-jev](https://github.com/luxus/ha-conversation-jev)** — Home Assistant 自定义组件：Jev 快路径加大模型兜底的对话智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · luxus · `Py` · ⚠ `无许可证`</sub>

- **[hermes-jev-curator](https://github.com/anpicasso/hermes-jev-curator)** — 为 Hermes Curator 提供带类型的 Jev 关系治理与安全的归档计划。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · anpicasso · `Py`</sub>

- **[jear](https://github.com/iJ03l/jear)** — 由 Jev 路由的 NEAR AI Cloud 推理与智能体客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · ij03l · `Rs`</sub>

- **[jeff-cli](https://github.com/saembit/jeff-cli)** — jeff：用 Go 写的 Jev 命令行工具。在 shell 脚本里给它 state 和一个固定选项的问题，就能拿回校准概率；支持排序命令和有意义的退出码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · saembit · `Go`</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — 在一个智能体失败归因基准上，把 Jev 与一个强 LLM 做对比测试。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · tokentrim · `Py`</sub>

- **[jev-blindspot](https://github.com/jsk4581/jev-blindspot)** — 一个侧边栏助手，帮你找出提示词中的盲点。适用于 Claude Code 与 Codex CLI。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · jsk4581 · `TS`</sub>

- **[jev-broadcast-lab](https://github.com/4anti/jev-broadcast-lab)** — Jev 的测试实验室。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · 4anti · `JS` · ⚠ `无许可证`</sub>

- **[jev-ci-selector](https://github.com/guilhem/jev-ci-selector)** — 为 GitHub Actions 做保守的 CI 任务选择：Jev 加一个纯策略引擎，默认以影子模式运行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · guilhem · `TS`</sub>

- **[jev-cloud-quiz](https://github.com/minorun365/jev-cloud-quiz)** — 一个演示：由 TypeSafe AI 的 System One 模型 Jev 带概率地判断某个功能名属于三大云中的哪一家。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · minorun365 · `TS`</sub>

- **[jev-codex-router-skill](https://github.com/455-dIAO/jev-codex-router-skill)** — 可移植的 Codex 技能：Jev 模型与推理强度路由，含安全安装。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · 455-diao · `Py` · ⚠ `无许可证`</sub>

- **[jev-connector](https://github.com/juanlentino/jev-connector)** — TypeSafe Jev 的 WordPress 连接器：带类型、带置信度分数的答案，你的代码可以据此分支。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · juanlentino · `PHP`</sub>

- **[jev-cvss](https://github.com/Red5d/jev-cvss)** — 从漏洞描述快速给出 CVSS 评分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · red5d · `Py`</sub>

- **[jev-freeform](https://github.com/kesku/jev-freeform)** — 完全由 Jev Choice 驱动的可观测逐字符聊天实验。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · kesku · `JS` · ⚠ `无许可证`</sub>

- **[jev-mcp](https://github.com/BYK/jev-mcp)** — 以评测为先的 TypeSafe Jev MCP 服务器；Jev 是 System One 模型，返回带概率的类型化判断（noul、choice、score），而不是生成文本。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · byk · `TS`</sub>

- **[jev-mcp](https://github.com/freepik-company/jev-mcp)** — 通过 OpenRouter 或 TypeSafe 调用 Jev / System One 做带类型决策的 MCP 服务器。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · freepik-company · `Go`</sub>

- **[jev-mcp](https://github.com/rajasekharponakala/jev-mcp)** — 封装 TypeSafe Jev System One 模型的 MCP 服务器——为 AI 智能体提供类型化的 noul/choice/score 判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · rajasekharponakala · `Py`</sub>

- **[jev-mcp-spring](https://github.com/Ashfaqbs/jev-mcp-spring)** — 面向 TypeSafe Jev 的 Java/Spring Boot MCP 服务器。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · ashfaqbs · `Java`</sub>

- **[jev-php-sdk](https://github.com/mzainzulifqar/jev-php-sdk)** — TypeSafe Jev 的 PHP SDK：发送文本和带类型的问题，得到带校准置信度的类型化答案。支持 PHP 8.1+。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · mzainzulifqar · `PHP`</sub>

- **[jev-pii-checker](https://github.com/coo-quack/jev-pii-checker)** — 用 Jev 在文本中定位 PII 的 CLI：存在性、敏感度与具体位置。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · coo-quack · `TS`</sub>

- **[jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment)** — 在 RouterArena 上把 Jev 当作低成本 LLM 路由器做基准测试。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · tokentrim · `Py`</sub>

- **[jev-sdk-java](https://github.com/luigivis/jev-sdk-java)** — 类型安全的 Java 21 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · luigivis · `Java`</sub>

- **[jev-x-kit](https://github.com/Kadihx/jev-x-kit)** — 面向编码智能体的离线决策层：Choice/Score/Noul 原语、置信度守门与超规划，另可接入 TypeSafe 原生提供方。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · kadihx · `TS`</sub>

- **[jev4mellea](https://github.com/SoundBlaster/Jev4Mellea)** — 给 Mellea 的 Jev 适配器。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★2 · soundblaster · `Py`</sub>

- **[jevclient](https://github.com/AboveColin/jevclient)** — Jev 的异步 Python 客户端：类型化问题进，概率与选择出，没有散文需要解析。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · abovecolin · `Py`</sub>

- **[jevgo](https://github.com/fgn/jevgo)** — System One API 的 Go 客户端，可选接入 Langfuse 观测。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · fgn · `Go`</sub>

- **[jevmem](https://github.com/Avinash-jetwani/jevmem)** — 为 Claude Code 提供自动的项目记忆，同样适用于 Cursor 和 Codex。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · avinash-jetwani · `TS`</sub>

- **[jevslop](https://github.com/TKY-27/JevSlop)** — 用 Jev 判定 note 文章是否为 AI 水文的站点。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · tky-27 · `TS`</sub>

- **[jevtok](https://github.com/LabGuy94/jevtok)** — Jev 的精确 token 计数与请求成本预测（tiktoken 风格）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · labguy94 · `Py`</sub>

- **[kojev](https://github.com/ItisNoMatter/kojev)** — Jev 的 Kotlin 多平台客户端：返回你自己的枚举／密封类型，而不是字符串。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · itisnomatter · `Kt`</sub>

- **[n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev)** — 面向 Jev 结构化 AI 决策的 n8n 社区节点。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · n3ndor · `TS`</sub>

- **[research_desk](https://github.com/0xnairb/research_desk)** — 用 Jev 做快速分析的演示。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · 0xnairb · `Py` · ⚠ `无许可证`</sub>

- **[s1_ruby](https://github.com/innocentdiaz/s1_ruby)** — 把 S1 模型的“测量”（以及随之而来的坍缩）变成 Ruby 的一个基本操作。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · innocentdiaz · `Rb`</sub>

- **[skill-router](https://github.com/lomeshdutta/skill-router)** — 用 Jev 告诉 Claude Code 当前会话需要哪个已安装技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · lomeshdutta · `Py`</sub>

- **[tempo-jev-demo](https://github.com/mychaelangelo/tempo-jev-demo)** — 自然语言任务工作区，横向对比多个 AI 模型的表现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · mychaelangelo · `TS`</sub>

- **[typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground)** — 围绕 Jev 做实验的 playground。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · markjaquith · `Rs`</sub>

- **[typesafe-go](https://github.com/zhirschtritt/typesafe-go)** — 地道的 Go SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · zhirschtritt · `Go`</sub>

- **[typesafe-jev-examples](https://github.com/rajivkuriakose/typesafe-jev-examples)** — Jev 的实战示例，今天就能通过 OpenRouter 跑起来。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · rajivkuriakose · `Py`</sub>

- **[typesafe-jev-mcp](https://github.com/anasbekheit/typesafe-jev-mcp)** — 把 Jev 暴露成类型化 evaluate 工具的 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · anasbekheit · `Rs`</sub>

- **[typesafe-sdk](https://github.com/typesafe-sdk-csharp/typesafe-sdk)** — TypeSafe AI 的非官方 .NET SDK，发布在 NuGet 上，提供确定性的问题构建与高吞吐的验证。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · typesafe-sdk-csharp · `C#`</sub>

- **[typesafeai.net](https://github.com/Hawxy/TypeSafeAI.Net)** — 面向 TypeSafe AI 平台的 .NET SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · hawxy · `C#`</sub>

- **[wellposed](https://github.com/suraj-phanindra/wellposed)** — 在 jev 请求自信地给出错误答案之前，先对请求本身做检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · suraj-phanindra · `JS`</sub>

- **[your-signal](https://github.com/MithrilMan/your-signal)** — 开源的自带密钥 Chrome 扩展：个人化、可撤销的 X 时间线过滤。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · mithrilman · `JS`</sub>

- **[antigravity-mcp-semantic-search-with-typesafeai](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)** — 给 AI 编程助手的快速语义代码搜索与 diff 合理性审查。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · greenyamao · `Py` · ⚠ `无许可证`</sub>

- **[askjev](https://github.com/pZacca/askjev)** — 非官方的 Jev MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · pzacca · `TS`</sub>

- **[audio-jevlike](https://github.com/alperiox/audio-jevlike)** — Prosodia：原生面向音频、形似 Jev 的决策模型——直接从语音给出校准的类型化决策，无需语音识别。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★1 · alperiox · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[can-jev-bayes](https://github.com/TomRichner/can-jev-bayes)** — Jev 会贝叶斯吗？把 TypeSafe AI 的 Jev 与贝叶斯最优策略对比，并测试它能否有效使用贝叶斯推理。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · tomrichner · `Py`</sub>

- **[codex-jev-preflight](https://github.com/wellkilo/codex-jev-preflight)** — 失败时放行的 Codex 钩子，在提交提示时注入 Jev 的任务前路由元数据。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · wellkilo · `Py`</sub>

- **[commentcop](https://github.com/ntedvs/commentcop)** — 审判你的代码注释，由 Jev 主持。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ntedvs · `TS`</sub>

- **[decido](https://github.com/yairshy/decido)** — 给 Python 的概率式决策：可用 Jev 也可自带 provider，配合 Playwright 抓取。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★1 · yairshy · `Py`</sub>

- **[decision-bench](https://github.com/Hanno-Labs/decision-bench)** — 面向基于文档的决策模型的开放基准运行框架。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · hanno-labs · `Py`</sub>

- **[decision-circuits](https://github.com/Barneyjm/decision-circuits)** — 决策电路：向 System One 模型提出带类型的问题，拿回校准概率，关卡写在代码里。零依赖。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · barneyjm · `Py`</sub>

- **[harden-jev-decides](https://github.com/tylerjharden/harden-jev-decides)** — 由 JEV 挑选哪个直播创意成为最小可行产品的决策看板。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · tylerjharden · `TS` · ⚠ `无许可证`</sub>

- **[hunch-js](https://github.com/steven-shoemaker/hunch-js)** — 把 Jev 判断变成作用于数组的 TypeScript 函数：classify、score、check、where、extract、pick、rank、verify。LLM 提议，Jev 决定。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · steven-shoemaker · `TS`</sub>

- **[jev](https://github.com/anilsenay/jev)** — TypeSafe System One API 及其模型 Jev 的非官方 Go 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · anilsenay · `Go`</sub>

- **[jev](https://github.com/kataras/jev)** — TypeSafe AI System One API 及其模型 Jev 的 Go 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · kataras · `Go`</sub>

- **[jev-demo](https://github.com/sawzhang/jev-demo)** — Jev 学习与实测：概念文档、5 个可运行 demo 与可复现压测 —— 实测扇出几乎免费。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · sawzhang · `TS` · ⚠ `无许可证`</sub>

- **[jev-demo](https://github.com/PenglongHuang/jev-demo)** — TypeSafe Jev（System One 决策模型）零依赖网页体验台：浏览器操作 / 意图识别 / Agent 上下文裁剪三大预设场景，发送状态与类型化问题，拿到带校准概率的结构化答案
  <sub>`开源项目` · ★1 · penglonghuang · `JS`</sub>

- **[jev-eyes](https://github.com/LeddoEngano/jev-eyes)** — 给 Jev 装上眼睛 —— 为纯文本的 System One 模型提供诚实的本地图像感知。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · leddoengano · `Py`</sub>

- **[jev-go](https://github.com/guillemus/jev-go)** — 非官方的 Jev Go SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · guillemus · `Go` · ⚠ `无许可证`</sub>

- **[jev-go-sdk](https://github.com/ajayk/jev-go-sdk)** — 无依赖的 Go 客户端，面向 TypeSafe AI 的 System One API 与 Jev 模型。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · ajayk · `Go`</sub>

- **[jev-lab](https://github.com/llt22/jev-lab)** — TypeSafe Jev（System One 模型）的动手研究实验室：对 Noul/Choice/Score 原语的可复现基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · llt22 · `Py` · ⚠ `无许可证`</sub>

- **[jev-lab](https://github.com/danielhirt/jev-lab)** — 通过 OpenRouter 对 TypeSafe Jev（System One 决策模型）做的实验：可重复性、扰动敏感性与 LLM 基线对比。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · danielhirt · `TS` · ⚠ `无许可证`</sub>

- **[jev-playground](https://github.com/wustep/jev-playground)** — System One 模型能否指挥音乐？Jev 只选方案（纯枚举），由代码渲染乐谱与音频。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · wustep · `TS` · ⚠ `无许可证`</sub>

- **[jev-playground](https://github.com/Little-Planet-Labs/jev-playground)** — 一个用来试验 TypeSafe AI Jev 模型（System One）的小型 Next.js 应用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · little-planet-labs · `TS` · ⚠ `无许可证`</sub>

- **[jev-practice-speed](https://github.com/tubone24/jev-practice-speed)** — WebGL 演示：与一个大脑是 Jev 的 CPU 玩快速纸牌。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · tubone24 · `JS` · ⚠ `无许可证`</sub>

- **[jev-research](https://github.com/sherajdev/jev-research)** — 把 TypeSafe Jev 与 Herdr 以及 Claude、Codex、Hermes 和浏览器智能体结合使用的实用指南。 <sub>(机翻)</sub>
  <sub>`教程` · ★1 · sherajdev · `TS`</sub>

- **[jev-sim](https://github.com/dashbi1/jev-sim)** — 从 LLM logits 读出类型化决策的 Jev 兼容 /v1/systemone 服务，带基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · dashbi1 · `Py`</sub>

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)** — Claude Code 插件：询问 Jev 哪个已安装技能适配当前提示，并记录答案（先影子运行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · shimo4228 · `Py`</sub>

- **[jev-skills](https://github.com/WanLanglin/jev-skills)** — 由 TypeSafe System One 模型 Jev 驱动的 Claude Code 与 Codex 技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · wanlanglin · `Py` · ⚠ `无许可证`</sub>

- **[jev-skills](https://github.com/laguagu/jev-skills)** — 用 Jev 构建应用的实用智能体技能与示例：API 配置、路由、排序与证据检查。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · laguagu · `JS`</sub>

- **[jev-snake](https://github.com/iammusham/jev-snake)** — 实验性贪吃蛇环境：游戏引擎掌管确定性规则，Jev 负责决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · iammusham · `Py` · ⚠ `无许可证`</sub>

- **[jev-symfony-bundle](https://github.com/vbcherepanov/jev-symfony-bundle)** — TypeSafe AI Jev 的非官方 Symfony bundle：带类型的客户端、校验约束、Messenger、Workflow 守卫等。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · vbcherepanov · `PHP`</sub>

- **[jev2048](https://github.com/KyleKreuter/jev2048)** — 让 Jev 解 2048。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · kylekreuter · `TS` · ⚠ `无许可证`</sub>

- **[jevals](https://github.com/dayhaysoos/jevals)** — TypeSafe Jev 的本地评估工作台。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · dayhaysoos · `TS`</sub>

- **[jevcode](https://github.com/miounet11/jevcode)** — JevCode — Jev (TypeSafe System One) 技术解决方案与最佳实践 · https://www.jevcode.ai
  <sub>`开源项目` · ★1 · miounet11 · `TS` · ⚠ `无许可证`</sub>

- **[Jevometry](https://github.com/Kunyanli230/Jevometry)** — 面向任意 System One（Jev 及类 Jev）智能体系统的信息几何分析工具包。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · kunyanli230 · `Py`</sub>

- **[jevsbistro](https://github.com/andrewsilber/JevsBistro)** — 用于低延迟决策模型基准测试的 3D 餐厅服务模拟器。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · andrewsilber · `TS`</sub>

- **[JevTape](https://github.com/Hugo-DDT/JevTape)** — Jev 决策的 Record / Replay 工具：CLI + 本地代理 + JSON 磁带，回放彻底离线。
  <sub>`开源项目` · ★1 · hugo-ddt · `Java`</sub>

- **[openpoke-meets-jev](https://github.com/0xShin0221/openpoke-meets-jev)** — 某助手产品的开源实现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · 0xshin0221 · `Py`</sub>

- **[r2r-jev](https://github.com/Thneoly/r2r-jev)** — 面向 AI 智能体的持久化治理——用 R2R 把 Jev 的判断变成可回放的关系状态。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · thneoly · `Rs`</sub>

- **[risc-jev](https://github.com/i2cjak/RISC-jeV)** — 我把 Jev 折腾成了一个 RISC-V CPU。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · i2cjak · `Py` · ⚠ `无许可证`</sub>

- **[second-thought](https://github.com/KNambiarDJsc/second-thought)** — 从 System One 模型（Laya，以及你自带的类型化决策服务）学习带类型概率决策的基础设施。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · knambiardjsc · `Py`</sub>

- **[typesafe](https://github.com/mattneel/typesafe)** — 地道的 Elixir 版 TypeSafe AI API 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · mattneel · `Ex`</sub>

- **[typesafe-client](https://github.com/JedimEmO/typesafe-client)** — 非官方的类型化异步 Rust 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · jedimemo · `Rs`</sub>

- **[typesafe-go](https://github.com/cole-gillespie/typesafe-go)** — TypeSafe AI 的非官方 Go SDK，支持带类型的答案、重试和 context。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · cole-gillespie · `Go`</sub>

- **[typesafe-jev-tools](https://github.com/wotai-dev/typesafe-jev-tools)** — 一个 Claude Code 钩子：判断你正在写的这个决策到底需不需要模型。附带一份实测的 149 行对比。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · wotai-dev · `TS`</sub>

- **[typesafe-rs](https://github.com/AbdelStark/typesafe-rs)** — 以延迟为先的 System One Rust SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · abdelstark · `Rs`</sub>

- **[typesafe-sdk](https://github.com/binnash/typesafe-sdk)** — 面向 TypeSafe AI JEV 模型系列的 PHP 与 Laravel SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · binnash · `PHP` · ⚠ `无许可证`</sub>

- **[typesafe-sdk-go](https://github.com/SergeAx/typesafe-sdk-go)** — TypeSafe.AI 的 Go SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · sergeax · `Go`</sub>

- **[typesafe-sdk-go](https://github.com/dwisiswant0/typesafe-sdk-go)** — TypeSafe AI 的 Go SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · dwisiswant0 · `Go`</sub>

- **[typesafe-sdk-ruby](https://github.com/afurm/typesafe-sdk-ruby)** — TypeSafe AI API（Jev 模型）的非官方 Ruby SDK：带类型的问题、重试与类型化错误。社区移植版。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · afurm · `Rb`</sub>

- **[typesafe-sdk-swift](https://github.com/marandaneto/typesafe-sdk-swift)** — typesafe-sdk-js 与 typesafe-sdk-python 的 Swift 移植版。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · marandaneto · `Swift`</sub>

- **[typesafe_sdk_ex](https://github.com/vinnie357/typesafe_sdk_ex)** — 基于 Req 的 Elixir 版 TypeSafe AI SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · vinnie357 · `Ex`</sub>

- **[typesafeai-cli](https://github.com/maddygoround/typesafeai-cli)** — 给你的 AI 智能体配一个能访问 TypeSafe AI Jev 的命令行伙伴。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · maddygoround · `Py`</sub>

- **[typesafeai-go](https://github.com/chez-shanpu/typesafeai-go)** — TypeSafe AI API 的 Go SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · chez-shanpu · `Go`</sub>

- **[what-is-jev](https://github.com/g0runmezadam/what-is-jev)** — 关于 TypeSafe AI Jev（System One）的独立、有来源的研究，包含对 947 个公开仓库的评分。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · g0runmezadam · `Py`</sub>

- **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)** — 直连 TypeSafe 的 AI SDK provider 包，示例覆盖三种问题类型以及嵌套的 criteria 写法。
  <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)** — 一个个人 Rust AI 网关，内置 TypeSafe provider，用真实响应体测试了用量提取与别名解析。
  <sub>`开源项目` · ★0 · dvjn · `Rs` · ⚠ `代码未实测` `无许可证`</sub>

- **[AskJev-MCP](https://github.com/cbruyndoncx/AskJev-MCP)** — TypeSafe System One API（Jev）的 MCP 服务器：带校准概率的类型化 choice/noul/score 判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · cbruyndoncx · `JS` · ⚠ `无许可证`</sub>

- **[beatjev](https://github.com/lambertsj/beatjev)** — 来试试能不能赢过 Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · lambertsj · `JS` · ⚠ `无许可证`</sub>

- **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)** — 标题误导：它并没有在跑 Jev，而是用开源 LLM 加受约束的 next-token 打分，自己搭一个 Jev-like 决策引擎。
  <sub>`Jev 替代实现` · DataScience Nexus · `Py` · ⚠ `并非 Jev 本身` `代码未实测` `付费墙`</sub>

- **[cartshield](https://github.com/ndolinschi/cartshield)** — CartShield：中小商户结账反欺诈判定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[cyber-breach-jev](https://github.com/rchovatiya88/cyber-breach-jev)** — 由 Jev 驱动的赛博朋克竞技场战斗游戏。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · rchovatiya88 · `JS` · ⚠ `无许可证`</sub>

- **[dgp](https://github.com/numerous-com/dgp)** — Numerous ApS 的决策图协议（DGP）：面向决策型 AI 智能体的开源契约，由 TypeSafe Jev 编排。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · numerous-com · `Py`</sub>

- **[extremely-specific-council](https://github.com/cbetz/extremely-specific-council)** — 十二个成员、零资质：一个带动画投票的趣味 AI 议会。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · cbetz · `TS`</sub>

- **[financialpredictionjev](https://github.com/thodoh1/FinancialPredictionJev)** — 用 Jev 测试它预测金融市场的能力。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · thodoh1 · `Py` · ⚠ `无许可证`</sub>

- **[frost](https://github.com/marcus/frost)** — 灵活可配置的 CLI 模型路由器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · marcus · `Go`</sub>

- **[functions](https://github.com/TrainLCD/Functions)** — 某移动应用的 Cloudflare Workers 后端。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · trainlcd · `TS` · ⚠ `无许可证`</sub>

- **[hiresignal](https://github.com/ndolinschi/hiresignal)** — HireSignal：简历初筛与面试匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)** — 第三方解读文章，给了一张有用的架构草图，还罕见地诚实列出了「不该用决策模型」的场景。
  <sub>`文章` · `Py` · ⚠ `代码未实测`</sub>

- **[jev-acento](https://github.com/marcosmartinez/jev-acento)** — Jev 听得懂你的口音吗？一项预先注册的、针对 TypeSafe AI Jev 西班牙语表现的审计——准确率、校准与 token 成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · marcosmartinez · `Py`</sub>

- **[jev-acp](https://github.com/formulahendry/jev-acp)** — 在任意 ACP（Agent Client Protocol）客户端或 IDE 里使用 Jev 类型化决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · formulahendry · `TS`</sub>

- **[jev-anotacao-sentencas](https://github.com/lab-dados/jev-anotacao-sentencas)** — Jev 与两个大模型在结构化句子标注上的对比（葡萄牙语）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · lab-dados · `Py` · ⚠ `无许可证`</sub>

- **[jev-bun1](https://github.com/heiwa4126/jev-bun1)** — 用 TypeScript SDK 上手 Jev 的第一步（日语）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · heiwa4126 · `TS` · ⚠ `无许可证`</sub>

- **[jev-calculator](https://github.com/pc418/jev-calculator)** — 由 Jev 驱动的概率化 AI 计算器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · pc418 · `TS`</sub>

- **[jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)** — TypeSafe 的 Jev 在俄语上能保持准确率与校准吗？一项独立的俄英对照审计（ECE、可靠性图）。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · ahtoooxa · `Py`</sub>

- **[jev-evaluation](https://github.com/willkelly/jev-evaluation)** — 对 Jev 的对抗性评测：九个实验与 28 条预测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · willkelly · `Py`</sub>

- **[jev-games](https://github.com/shantanugoel/jev-games)** — 面向多种游戏与模拟器平台的可视化 Jev 实验室。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shantanugoel · `Py` · ⚠ `无许可证`</sub>

- **[jev-jp-address](https://github.com/smasato/jev-jp-address)** — Jev 性能评测项目：以日本邮政地址库为基准，检验它在地址模糊匹配上的可用性。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · smasato · `TS` · ⚠ `无许可证`</sub>

- **[jev-lab](https://github.com/Menny1337/jev-lab)** — 针对 TypeSafe Jev 模型的 TypeScript 实验、评测与延迟基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · menny1337 · `TS` · ⚠ `无许可证`</sub>

- **[jev-measured](https://github.com/WallerChen/jev-measured)** — 在多个场景上实测 Jev 线上 API 的成本、延迟与原始输出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · wallerchen · `Py`</sub>

- **[jev-no-enem](https://github.com/patryckalves/jev-no-enem)** — 在巴西 2025 年 ENEM 标准化考试上评测 TypeSafe AI Jev（System One 范式）的可复现基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · patryckalves · `Py` · ⚠ `无许可证`</sub>

- **[jev-pick-and-place-study](https://github.com/tryaksh/jev-pick-and-place-study)** — 小而可复现的 MuJoCo 试点：对比 Jev、某轻量 LLM 与反应式规则的抓取表现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · tryaksh · `Py` · ⚠ `无许可证`</sub>

- **[jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner)** — 由 Jev 模型来玩 Chrome 恐龙小游戏。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · joshlarsen · `JS`</sub>

- **[jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales)** — 由 Jev 裁判的擂台式动物锦标赛，本地游戏。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · hectorlcastro09 · `TS`</sub>

- **[jevai.org community site](https://www.jevai.org/)** — 一个与官方无关的社区站：有 playground、预设决策 API、MCP 服务、可下载技能，以及一个社区应用展示廊。
  <sub>`开源项目` · `sh` · ⚠ `需第三方密钥` `宣称未核实`</sub>

- **[jevscope](https://github.com/jeiel85/jevscope)** — 本地优先的可视化决策调试器与回归测试台，面向 TypeSafe AI Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jeiel85 · `TS`</sub>

- **[kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev)** — System One API 的 Rust 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · kunobi-ninja · `Rs`</sub>

- **[labs](https://github.com/kiarina/labs)** — 用于实验、研究与调查的小型独立项目集。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kiarina · `Py`</sub>

- **[magic-jev-ball](https://github.com/mikecann/magic-jev-ball)** — 一个魔术 8 号球：不随机挑答案，而是去问 Jev。基于 Convex、AI Gateway 与 three.js。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · mikecann · `TS`</sub>

- **[mcpmatch](https://github.com/ndolinschi/mcpmatch)** — 用两段式流程把用户目标匹配到 MCP 目录。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[mimicry](https://github.com/jxucoder/mimicry)** — 用有界反馈循环把 AI 草稿改写成你自己的语气。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jxucoder · `Py` · ⚠ `无许可证`</sub>

- **[n8n-nodes-typesafe](https://github.com/Biztactix/n8n-nodes-typesafe)** — 用于 n8n 的 TypeSafe AI 节点。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · biztactix · `TS`</sub>

- **[open-jev-bridge](https://github.com/louis-szeto/open-jev-bridge)** — 把类 Jev 的 System One API（本地托管或 TypeSafe Jev）接入 Codex 和 Claude Code 的 MCP 插件，用于决策任务。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · louis-szeto · `JS`</sub>

- **[pi-agent-foreman](https://github.com/alexshpunt/pi-agent-foreman)** — 当 Pi 智能体在活没干完时停下，把它赶回去继续。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · alexshpunt · `TS`</sub>

- **[pi-typesafe](https://github.com/twilwa/pi-typesafe)** — 基于 TypeSafe AI System One API（Jev）构建的 Pi 编码智能体扩展。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · twilwa · `TS` · ⚠ `无许可证`</sub>

- **[pong-jev](https://github.com/safzanpirani/pong-jev)** — 让 Jev 玩雅达利乒乓：每帧一个类型化 Choice 问题，不发送坐标。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · safzanpirani · `TS` · ⚠ `无许可证`</sub>

- **[river-run-typesafe](https://github.com/ashaazami/river-run-typesafe)** — Python 写的河流射击游戏，由 AI 飞行员驾驶。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ashaazami · `Py`</sub>

- **[scam-shield](https://github.com/ShupingR/scam-shield)** — 由 Jev 驱动的诈骗短信过滤器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shupingr · `TS` · ⚠ `无许可证`</sub>

- **[search-function-test](https://github.com/Shifros/Search-Function-Test)** — 基于 Jev 的试验项目，目标是给博客做搜索功能。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shifros · `JS` · ⚠ `无许可证`</sub>

- **[system-one-adapter-rust](https://github.com/codeitlikemiley/system-one-adapter-rust)** — 官方 system-one-adapter 的 Rust 移植（用 LLM 支撑 system_one 评估）。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★0 · codeitlikemiley · `Rs`</sub>

- **[tinyjevclient](https://github.com/tinyhumansai/tinyjevclient)** — Rust 版的 Jev 集成。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★0 · tinyhumansai · `Rs`</sub>

- **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)** — 目前唯一有 Jev 专用可观测性的平台：一个 OpenInference instrumentor，通过 OpenTelemetry 追踪每次决策调用。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul`</sub>

- **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)** — Vercel 在 AI Gateway 上线 Jev 的公告，附 experimental_evaluate 示例，模型串为 typesafe-ai/jev。
  <sub>`平台集成` · `TS` · `noul`</sub>

- **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)** — Pydantic AI 的一方支持：用 typesafe:jev-latest 这个模型串、配 output_type=bool 建 Agent。
  <sub>`平台集成` · `Py`</sub>

- **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)** — 通过 LiteLLM 代理 Jev，统一密钥与成本追踪，/typesafe/ 下的任意路径都直接透传。
  <sub>`平台集成` · `sh`</sub>

- **[typesafe-ai-ruby](https://github.com/hnegishi/typesafe-ai-ruby)** — System One API 的 Ruby 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · hnegishi · `Rb`</sub>

- **[typesafe-chess](https://github.com/TholeG/typesafe-chess)** — 双方都是 Jev 的国际象棋：每一步都是一次类型化 Choice。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · tholeg · `JS`</sub>

- **[typesafe-comment](https://github.com/Hexdigest123/typesafe-comment)** — 用若干启发式规则评估代码注释的小型 Python 包。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · hexdigest123 · `Py`</sub>

- **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)** — 只改一个 baseURL 就能把官方 TypeSafe SDK 指向 Vercel，也可以直接用 cURL 调网关的 systemone 端点。
  <sub>`平台集成` · `TS` · `sh` · `noul`</sub>

- **[typesafe-go](https://github.com/Nibir1/typesafe-go)** — 零依赖的社区 Go SDK，还带一个静态分析器，能在编译期指出设计不良的问题。
  <sub>`SDK` · ★0 · Nibir1 · `Go` · `choice` · `score` · `noul` · ⚠ `代码未实测`</sub>

- **[typesafe-go](https://github.com/Shubham510/typesafe-go)** — TypeSafe AI System One API（Jev）的非官方 Go SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · shubham510 · `Go`</sub>

- **[typesafe-sdk-go](https://github.com/valksor/typesafe-sdk-go)** — TypeSafe AI System One API 的非官方 Go SDK，与官方 JS 和 Python SDK 一一对应，与 TypeSafe AI 无关。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · valksor · `Go`</sub>

- **[typesafe-sdk-kotlin](https://github.com/ufec/typesafe-sdk-kotlin)** — TypeSafe AI 的 Kotlin SDK，移植自官方 JavaScript SDK，并记录了与原版的差异；针对一段文本提出带类型的问题，得到带类型的答案。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · ufec · `Kt`</sub>

- **[typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php)** — TypeSafe AI System One API 的非官方 PHP SDK，与官方 JS 和 Python SDK 一一对应，与 TypeSafe AI 无关。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · valksor · `PHP`</sub>

- **[typesafe-sdk-php](https://github.com/Fox-Islam/typesafe-sdk-php)** — TypeSafe API 的非官方 PHP 库。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · fox-islam · `PHP`</sub>

- **[typesafe_ai](https://github.com/typesend/typesafe_ai)** — 面向 TypeSafe AI 及其 Jev System One 模型的带类型 Elixir 客户端，提供离线测试桩、并发扇出与原子化结果。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · typesend · `Ex`</sub>

- **[typesafe_ai](https://github.com/hfiguera/typesafe_ai)** — TypeSafe AI 的 Elixir 客户端，提供带类型的响应和有界并发。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · hfiguera · `Ex`</sub>

- **[typesafe_chess_eval](https://github.com/AliceRoselia/Typesafe_chess_eval)** — 对 Jev 下棋能力的评测 —— 结论是它下得并不好。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · aliceroselia · `Py`</sub>

- **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)** — 目前这个领域里 star 数最高的同类目录。
  <sub>`开源项目` · ★1,530 · ⚠ `无许可证`</sub>

- **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)** — 唯一一篇引用了开发者一手说法（而非厂商数字）的发布报道，其中还提醒：解释阈值的责任现在落在你自己头上。
  <sub>`文章` · Tim Fernholz</sub>

- **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)** — 重点落在可解释性的缺失 —— 模型不给出语言层面的理由 —— 以及所有已公布基准都出自厂商自己。
  <sub>`文章` · Tomislav Bezmalinović</sub>

- **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)** — 发布讨论帖，也是质疑最集中的地方：RLCD 缺乏支撑材料、延迟对比不对等、以及官方刻意不公开基准。
  <sub>`讨论`</sub>

- **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))** — 最大价值在于当索引用：它的参考文献列表是找到值得读的报道的最快路径。
  <sub>`文章`</sub>

- **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)** — 从智能体开发者角度，讲决策模型在智能体技术栈里的位置。
  <sub>`文章` · ⚠ `营销内容`</sub>

- **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)** — 主流媒体对这次发布、以及各家网关上线速度的报道。
  <sub>`文章` · Josipa Majic Predin · ⚠ `厂商自报数据` `付费墙`</sub>

- **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)** — 一篇把限制直接写进标题、而不是藏在正文里的评测。
  <sub>`视频` · Gary Explains</sub>

- **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)** — 唯一的长篇创始人访谈：为什么 RLHF 是错的优化目标、为什么不公开基准、以及全合成数据的路线。
  <sub>`讨论` · Latent Space</sub>

- **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)** — 对架构、宣称的基准和定价的中立综述，并明确指出当时还没有出现大规模的独立复现。
  <sub>`文章` · Matt Crabtree</sub>

- **[jevai.org community app gallery](https://www.jevai.org/apps)** — 从社交帖子里策展的 36 个社区作品：浏览器智能体、表格工具、按意图搜邮箱、会判断的广告拦截、游戏与机器人。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

- **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)** — 一份独立整理，其最有价值的结论是否定性的：RLCD 没有论文、没有奖励函数、没有数据集说明、也没有可复现的评测。
  <sub>`文章`</sub>

- **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)** — 最具怀疑视角的主流报道：它质疑「不会幻觉」的说法 —— 格式正确的答案不等于正确的答案。
  <sub>`文章` · Thomas Claburn</sub>

- **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)** — OpenRouter 上的 Jev 条目，有自己的模型 id，以及「输入收费、输出免费」这种少见的定价结构。
  <sub>`平台集成`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
