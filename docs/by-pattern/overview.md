# Overview

<sub>[awesome-jev](../../README.md) · [中文](overview.zh-CN.md)</sub>

_Surveys the model or the space rather than one pattern._

Every catalogued example of this decision — 451 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#overview); [the site](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=en) can filter them further by language, primitive and kind.

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐ — Installs a TypeSafe skill into Claude Code so an agent can write correct Jev calls without you pasting the API shape each time.
  <sub>`Official docs` · ★2,036 · `sh`</sub>

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐ — The official agent-skills repository behind the Claude Code plugin, holding the SKILL.md that teaches an agent the System One API.
  <sub>`Plugin` · ★2,036 · `sh`</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐ — A drop-in TypeSafeClient replacement backed by ordinary LLM APIs, so you can run Jev-shaped code without Jev access.
  <sub>`SDK` · ★285 · `Py`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐ — The official TypeScript client. Ships ESM, CJS and type declarations, with lowercase choice()/score()/noul() helper factories.
  <sub>`SDK` · ★232 · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐ — The official Python client. Sync and async clients, retry policy with retry-after support, and Choice/Score/Noul helper classes.
  <sub>`SDK` · ★219 · `Py` · `choice` · `score` · `noul`</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐ — The one endpoint, POST /v1/systemone, with the exact request and answer shapes for all three question types.
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐ — The authoritative sheet: jev-1.13.0, $0.042 per Mtok input with output free, 64k context, 32k for state plus the longest question, text input only.
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐ — What each primitive is for and how to write criteria, including the 255-option cap on Choice and the 2-10 level range on Score.
  <sub>`Official docs` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐ — The launch post: what a System One model is, why decisions were split from generation, and the vendor's latency and cost claims.
  <sub>`Article` · Diogo Almeida · ⚠ `vendor numbers`</sub>

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐ — The vendor's own list of where the model fails: literal reading, arithmetic and counting, date comparison, indirection, large noisy states, adversarial content.
  <sub>`Official docs`</sub>

- **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐ — The vendor's own taxonomy: five headline categories, nineteen industry groups, and ten decision shapes from classification through to structured data extraction.
  <sub>`Official docs`</sub>

- **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)** — A coding agent whose hosted gateway resells Jev, including a free tier model id.
  <sub>`Integration` · ★209,715 · `TS`</sub>

- **[langchain](https://github.com/langchain-ai/langchain)** — The agent engineering platform.
  <sub>`Project` · ★146,958 · langchain-ai · `Py`</sub>

- **[litellm](https://github.com/BerriAI/litellm)** — The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM]
  <sub>`Integration` · ★59,514 · berriai · `Py`</sub>

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)** — ⌥ Coding agent with the IDE wired in
  <sub>`Project` · ★33,049 · can1357 · `TS`</sub>

- **[ai](https://github.com/vercel/ai)** — The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents
  <sub>`SDK` · ★26,922 · vercel · `TS`</sub>

- **[openwork](https://github.com/different-ai/openwork)** — The open-source alternative to Claude Cowork (powered by opencode)
  <sub>`Jev-like alternative` · ★23,715 · different-ai · `TS` · ⚠ `not Jev itself`</sub>

- **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)** — Wraps the sync and async clients so every system_one call is recorded as a traced span.
  <sub>`Project` · ★22,211 · `Py`</sub>

- **[laya](https://github.com/NandhaKishorM/laya)** — Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ languages, with a router that picks the right checkpoint per request.
  <sub>`Jev-like alternative` · ★21,147 · nandhakishorm · `Py` · ⚠ `not Jev itself`</sub>

- **[pydantic-ai](https://github.com/pydantic/pydantic-ai)** — How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.
  <sub>`Project` · ★20,133 · pydantic · `Py`</sub>

- **[eliza](https://github.com/elizaOS/eliza)** — Open source agentic operating system
  <sub>`Project` · ★19,474 · elizaos · `TS`</sub>

- **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)** — Implements Effect's DecisionModel interface over Jev, with an unusually candid caveat about unverified rounding behaviour.
  <sub>`Integration` · ★16,195 · `TS` · `choice` · `score` · `noul`</sub>

- **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)** — A Rust integration with compile-time-checked option counts, so an over-255 Choice fails to build rather than at runtime.
  <sub>`Integration` · ★8,713 · `Rs` · `choice` · `score` · `noul`</sub>

- **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)** — A Go gateway provider that passes the native API through one-to-one, so the official SDKs work by changing only the base URL.
  <sub>`Project` · ★8,300 · `Go`</sub>

- **[deep-searcher](https://github.com/zilliztech/deep-searcher)** — Open Source Deep Research Alternative to Reason and Search on Private Data. Written in Python.
  <sub>`Jev-like alternative` · ★8,282 · zilliztech · `Py` · ⚠ `not Jev itself`</sub>

- **[kev](https://github.com/jaredpalmer/kev)** — A trainable, self-hostable family of Jev-like decision models with a System One compatible API, so the official SDK can point at your own server.
  <sub>`Jev-like alternative` · ★6,236 · Jared Palmer · `Py` · `choice` · `score` · `noul` · ⚠ `not Jev itself`</sub>

- **[laya-mlx](https://github.com/mizorewww/laya-mlx)** — Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text generation, PyTorch, or cloud API.
  <sub>`Project` · ★6,048 · mizorewww · `Py`</sub>

- **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)** — A JSON-Schema-to-question compiler wired into the adapter registry, with an honest note on what it cannot serve.
  <sub>`Integration` · ★5,079 · `Py` · `choice` · `score` · `noul`</sub>

- **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)** — A Ruby provider with a dedicated System One protocol, the main route into Jev from Ruby.
  <sub>`Integration` · ★4,404 · `Rb` · `choice` · `score` · `noul`</sub>

- **[SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev)** — An independent semantic-if implementation that states up front it is unaffiliated with Jev or TypeSafe.
  <sub>`Jev-like alternative` · ★4,125 · `Py` · ⚠ `not Jev itself`</sub>

- **[ax](https://github.com/ax-llm/ax)** — The pretty much "official" DSPy framework for Typescript
  <sub>`Project` · ★2,946 · ax-llm · `TS`</sub>

- **[memsearch](https://github.com/zilliztech/memsearch)** — A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus.
  <sub>`Plugin` · ★2,649 · zilliztech · `Py`</sub>

- **[NanoJev](https://github.com/TianyuCodings/NanoJev)** — A self-described nano replica of Jev, for reading rather than for production.
  <sub>`Jev-like alternative` · ★2,137 · `Py` · ⚠ `not Jev itself`</sub>

- **[vellum-assistant](https://github.com/vellum-ai/vellum-assistant)** — An AI Assistant that’s easy to setup, does your work 24/7, knows your preferences and gets better over time.
  <sub>`Project` · ★1,313 · vellum-ai · `TS`</sub>

- **[jevlike](https://github.com/vinnylarouge/jevlike)** — An independent, trainable model with the same input and output shape as Jev: text plus N options in, one probability per option out, in a single pass.
  <sub>`Jev-like alternative` · ★1,274 · vinnylarouge · `Py` · ⚠ `not Jev itself`</sub>

- **[celesto](https://github.com/CelestoAI/celesto)** — Secure and persistent computer for AI agents -- build your own Grokbot, and Muse.
  <sub>`Project` · ★972 · celestoai · `Py`</sub>

- **[awesome-jev (heyjunpenn)](https://github.com/heyjunpenn/awesome-jev)** — The broadest sibling directory: hundreds of projects in six languages, with a README that is itself the parsed data source.
  <sub>`Project` · ★782 · heyjunpenn · `TS`</sub>

- **[localjev](https://github.com/githubnext/localjev)** — GitHub Next's local, Jev-compatible POST /v1/systemone API in TypeScript, reading probabilities from a DiffusionGemma model through a one-step structured read on a patched vLLM. It reimplements the wire, not the model.
  <sub>`Jev-like alternative` · ★739 · githubnext · `TS` · ⚠ `not Jev itself`</sub>

- **[distill](https://github.com/samuelfaj/distill)** — Get FAR MORE done with FAR FEWER tokens 🔥
  <sub>`Project` · ★688 · samuelfaj · `Rs`</sub>

- **[aiavatarkit](https://github.com/uezo/aiavatarkit)** — 🥰 Building AI-based conversational avatars lightning fast ⚡️💬
  <sub>`Project` · ★678 · uezo · `Py`</sub>

- **[kody](https://github.com/kentcdodds/kody)** — 🐨 Your assistant's home — the memory, keys, code, and automations your AI agent keeps, portable across every MCP host. Built on Cloudflare Workers.
  <sub>`Plugin` · ★672 · kentcdodds · `TS`</sub>

- **[von](https://github.com/wfzyx/von)** — The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.
  <sub>`Jev-like alternative` · ★601 · wfzyx · `Py` · ⚠ `not Jev itself`</sub>

- **[req_llm](https://github.com/agentjido/req_llm)** — Composable Elixir library for LLM interactions built on Req and Finch
  <sub>`Project` · ★582 · agentjido · `Ex`</sub>

- **[simple-jev](https://github.com/featherless-ai/simple-jev)** — Turns any open-weights model into a Jev-shaped endpoint by reading next-token logits, with the server constructing the JSON rather than the model generating it.
  <sub>`Jev-like alternative` · ★505 · `Py` · ⚠ `not Jev itself`</sub>

- **[jev-chat-windows](https://github.com/jev-chat/jev-chat-windows)** — 微信（Windows 4.x）旁挂的回复辅助：窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动
  <sub>`Project` · ★469 · jev-chat · `Py`</sub>

- **[jev-skill](https://github.com/wuyoscar/jev-skill)** — An agent skill plus CLI that validates all three primitives, requires explicit consent before a billed call, and forbids inventing output when simulating.
  <sub>`Plugin` · ★464 · `Py` · `choice` · `score` · `noul`</sub>

- **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)** — A sibling directory aiming at ecosystem breadth with commit-pinned sources, four README languages and a generated site.
  <sub>`Project` · ★461 · logicrw · `JS`</sub>

- **[smithers](https://github.com/smithersai/smithers)** — Smithers is an agentic workflow framework for defining workflows in simple TypeScript configuration files and executing them quickly, durably, and reliably
  <sub>`Project` · ★421 · smithersai · `TS`</sub>

- **[rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow)** — The open, local take on Jev: typed decisions from an LLM, without generating a single token
  <sub>`Jev-like alternative` · ★395 · rizzo-ai-academy · `Py` · ⚠ `not Jev itself`</sub>

- **[jev-experiments](https://github.com/dabit3/jev-experiments)** — Nader Dabit's collection of small Jev experiments, one per folder: a commit reviewer, a shell guard, a send guard, a log sentinel, instant search, reranking, a voice-turn detector and more.
  <sub>`Project` · ★378 · dabit3 · `TS` · ⚠ `no licence`</sub>

- **[openjev](https://github.com/razorback16/openjev)** — A Jev-compatible decision server on an open diffusion model.
  <sub>`Jev-like alternative` · ★378 · razorback16 · `Py` · ⚠ `not Jev itself`</sub>

- **[laya](https://github.com/receptron/laya)** — Run Laya, the open-source Jev-compatible System-1 decision model, from Node.js / TypeScript via ONNX Runtime
  <sub>`Project` · ★371 · receptron · `TS`</sub>

- **[decider](https://github.com/Mapika/decider)** — A family of System One-style models fine-tuned from an open base for one-pass typed decisions.
  <sub>`Jev-like alternative` · ★342 · mapika · `Py` · ⚠ `not Jev itself`</sub>

- **[jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac)** — 微信消息意图识别悬浮窗（macOS）：看屏 + 本地小模型判断意图和风险，再按话术生成回复候选。纯只读、不注入微信。
  <sub>`Project` · ★333 · jev-chat · `Py`</sub>

- **[openjev-sglang](https://github.com/ekzhang/openjev-sglang)** — A Jev-compatible endpoint served from open models, prefill only.
  <sub>`Jev-like alternative` · ★307 · ekzhang · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[Open-Jev](https://github.com/Zefan-Cai/Open-Jev)** — Open-Jev-27B, an open-weight model that returns typed probabilities for a context, questions and candidates without generating an answer — a Jev-style decision model you can run yourself.
  <sub>`Jev-like alternative` · ★295 · zefan-cai · `Py` · ⚠ `not Jev itself`</sub>

- **[typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)** — The easiest first step once you have a key: registers Jev into Claude Code, Claude Desktop, Codex and Pi with one command.
  <sub>`Plugin` · ★287 · `Go` · `choice` · `score` · `noul`</sub>

- **[third-hand](https://github.com/shhivv/third-hand)** — computer-use assistant w/ decision models
  <sub>`Project` · ★286 · shhivv · `Swift`</sub>

- **[orchestkit](https://github.com/yonatangross/orchestkit)** — The Complete AI Development Toolkit for Claude Code. 106 skills, 36 agents, 171 hooks. Install `ork` for stable (v9.x), or `ork-alpha` for the v10 line, which ships daily.
  <sub>`Plugin` · ★283 · yonatangross · `TS`</sub>

- **[pi-fabric](https://github.com/monotykamary/pi-fabric)** — A programmable tool and agent runtime for Pi
  <sub>`Project` · ★258 · monotykamary · `TS`</sub>

- **[jeff](https://github.com/logan-markewich/jeff)** — A self-hosted drop-in replacement for TypeSafe's jev, powered by GliFormer.
  <sub>`Jev-like alternative` · ★233 · logan-markewich · `Py` · ⚠ `not Jev itself`</sub>

- **[crush-monitor](https://github.com/FerryCorleone/crush-monitor)** — Crush 好感监控器：用 Jev 分析微信聊天的情绪、意图和回复表现。本机部署，使用自己的 API Key。
  <sub>`Project` · ★207 · ferrycorleone · `TS`</sub>

- **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)** — A sibling directory whose submissions are reviewed by Jev itself, with a notably thorough list of multi-language community clients.
  <sub>`Project` · ★203 · fatwang2 · `JS`</sub>

- **[djev-spark](https://github.com/mmastrac/djev-spark)** — DiffusionGemma NVFP4 structured decisions on a DGX Spark: container recipe
  <sub>`Project` · ★189 · mmastrac · `TS` · ⚠ `no licence`</sub>

- **[openwhisper](https://github.com/Knuckles92/OpenWhisper)** — Local speech-to-text, dictation, and meetings with Whisper and OpenAI API. Optional Windows x64 engines: Parakeet, Qwen3-ASR, Nemotron Streaming, and Moonshine.
  <sub>`Project` · ★188 · knuckles92 · `Py`</sub>

- **[Jevmind](https://github.com/dealerdefi/Jevmind)** — An agent's decisions pulled out of its prose into one place: typed answers with a confidence, behind a gate written in code, sealed in a ledger, graded and learned from. Runs offline on a local rules brain; Jev can be swapped in with one flag.
  <sub>`Project` · ★166 · dealerdefi · `Py`</sub>

- **[runline](https://github.com/Michaelliv/runline)** — ⚡ Code mode for agents
  <sub>`Project` · ★164 · michaelliv · `TS` · ⚠ `no licence`</sub>

- **[laya-ultrafast](https://github.com/ipenywis/laya-ultrafast)** — Same as jev-ultrafast but using Laya
  <sub>`Project` · ★145 · ipenywis · `Py`</sub>

- **[webctl](https://github.com/dorkitude/webctl)** — Smart web search CLI for agents, backed by Jev. Saves a lot of tokens.
  <sub>`Project` · ★139 · dorkitude · `Go`</sub>

- **[dasheng](https://github.com/wquguru/dasheng)** — 大声读 — R2T2 流式 ASR 听，Jev 逐词判，英文朗读评分
  <sub>`Project` · ★138 · wquguru · `JS` · ⚠ `no licence`</sub>

- **[OpenJev](https://github.com/SiliconLabAI/OpenJev)** — OpenSource Jev
  <sub>`Jev-like alternative` · ★121 · siliconlabai · `TS` · ⚠ `not Jev itself`</sub>

- **[stanley-code](https://github.com/devagrawal09/stanley-code)** — Bounded TypeSafe Jev workflows for coding agents.
  <sub>`Project` · ★114 · devagrawal09 · `TS`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open.
  <sub>`Benchmark` · ★107 · fstandhartinger · `Py`</sub>

- **[open-jev](https://github.com/daseinlabs/open-jev)** — Open Jev implementation with custom finetuning
  <sub>`Jev-like alternative` · ★107 · daseinlabs · `Py` · ⚠ `not Jev itself`</sub>

- **[laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev)** — Laya vs Jev: local MLX and hosted AI decisions playing T-Rex side by side, with live metrics and replay recording
  <sub>`Project` · ★94 · virajbhartiya · `Py`</sub>

- **[advocaat](https://github.com/pithings/advocaat)** — A small typed client for asking questions about your own data.
  <sub>`SDK` · ★91 · pithings · `TS`</sub>

- **[jevchat](https://github.com/kyle-pena-nlp/jevchat)** — Turns Jev into a chatbot
  <sub>`Project` · ★90 · kyle-pena-nlp · `Py` · ⚠ `no licence`</sub>

- **[jev-voice](https://github.com/kevinbadi/jev-voice)** — Talk to your Mac. Local whisper.cpp + one Jev (TypeSafe) call per command + macOS automation.
  <sub>`Project` · ★84 · kevinbadi · `Py`</sub>

- **[jev-leftpad](https://github.com/f/jev-leftpad)** — Left-pad strings with TypeSafe AI's Jev. For reasons.
  <sub>`Project` · ★83 · f · `JS`</sub>

- **[james_library](https://github.com/topherchris420/james_library)** — R.A.I.N. Lab is an experimental scientific-agent architecture that separates fast local judgment, independent probabilistic evaluation, multi-agent deliberation, evidence, and authorization into distinct computational layers.🐙(Predates Karpathy's AutoResearch)
  <sub>`Project` · ★74 · topherchris420 · `Rs`</sub>

- **[captaincore](https://github.com/CaptainCore/captaincore)** — 👨🏽‍💻 CaptainCore is a command line application for automating WordPress maintenance.
  <sub>`Project` · ★71 · captaincore · `Go`</sub>

- **[agent-router](https://github.com/nidhi-singh02/agent-router)** — CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr
  <sub>`Plugin` · ★70 · nidhi-singh02 · `TS`</sub>

- **[djev](https://github.com/mmastrac/djev)** — Jev-style structured decisions on DiffusionGemma: the example server from vLLM PR 57250
  <sub>`Jev-like alternative` · ★68 · mmastrac · `Py` · ⚠ `not Jev itself`</sub>

- **[dspy-typesafeify](https://github.com/typesafeainate/dspy-typesafeify)** — Add a decorator for dspy Signatures that automatically uses TypeSafe where relevant
  <sub>`Project` · ★63 · typesafeainate · `Py`</sub>

- **[jevk5](https://github.com/allebee/jevk5)** — JevK5: open-weight alternative to TypeSafe Jev. Typed decisions with probabilities in one forward pass; Apache-2.0 weights and code.
  <sub>`Jev-like alternative` · ★61 · allebee · `Py` · ⚠ `not Jev itself`</sub>

- **[jev-paint](https://github.com/achimala/jev-paint)** — Use Jev to make art!
  <sub>`Project` · ★56 · achimala · `JS`</sub>

- **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)** — An open-source semantic decision engine running a local zero-shot model, with a FastAPI server proven wire-compatible with the official SDK.
  <sub>`Jev-like alternative` · ★56 · deepanwadhwa · `Py` · `choice` · `score` · `noul` · ⚠ `not Jev itself`</sub>

- **[ruby_decision_model](https://github.com/obie/ruby_decision_model)** — Ruby client for decision models such as Typesafe Jev
  <sub>`SDK` · ★50 · obie · `Rb`</sub>

- **[jev-rules](https://github.com/EliaAlberti/jev-rules)** — Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter.
  <sub>`Project` · ★49 · eliaalberti · `JS`</sub>

- **[system-one](https://github.com/iamaamir/system-one)** — Provider-neutral System One runtime for TypeScript and Pi
  <sub>`SDK` · ★48 · iamaamir · `TS` · ⚠ `no licence`</sub>

- **[jeview](https://github.com/andududu/jeview)** — An unofficial local visualizer for Jev (TypeSafe): a live view of every call your code makes. Not affiliated with TypeSafe AI.
  <sub>`Project` · ★47 · andududu · `JS`</sub>

- **[jev-seo](https://github.com/AkashPriyadarshii/jev-seo)** — 100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One https://akashpriyadarshii.github.io/jev-seo/
  <sub>`Plugin` · ★43 · akashpriyadarshii · `Rs`</sub>

- **[litjev](https://github.com/zhengxuyu/litjev)** — Turn any off-the-shelf LLM into a Jev -like decision layer
  <sub>`Jev-like alternative` · ★43 · zhengxuyu · `Py` · ⚠ `not Jev itself`</sub>

- **[openthai-systemone](https://github.com/iapp-technology/openthai-systemone)** — OpenThai-SystemOne: open Thai + English System One decision model (0.8B, 256-way slot head, Apache-2.0)
  <sub>`Project` · ★43 · iapp-technology · `Py`</sub>

- **[jev-foundation-models](https://github.com/peterfriese/jev-foundation-models)** — A lightweight, native Swift 6 bridge integrating TypeSafe AI's Jev System One decision model into Apple's Foundation Models framework.
  <sub>`Project` · ★42 · peterfriese · `Swift`</sub>

- **[jev-mcp](https://github.com/burnigtm/jev-mcp)** — MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client
  <sub>`Plugin` · ★42 · burnigtm · `TS`</sub>

- **[call-coach-ai](https://github.com/ZeroGold/call-coach-ai)** — Jev powered call coach
  <sub>`Project` · ★41 · zerogold · `TS`</sub>

- **[cultivar](https://github.com/pinecone-io/cultivar)** — Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents.
  <sub>`Project` · ★41 · pinecone-io · `Py`</sub>

- **[laya-server](https://github.com/1Panel-dev/laya-server)** — A self-hosted API and web interface for Laya’s structured decision models, compatible with the TypeSafe Jev API format.
  <sub>`Jev-like alternative` · ★41 · 1panel-dev · `TS` · ⚠ `not Jev itself`</sub>

- **[solar-mini4-jev](https://github.com/hunkim/solar-mini4-jev)** — A drop-in wrapper that exposes Upstage's Solar models through the Jev System One API shape — noul, choice and score with the same schema — with a hosted bring-your-own-key endpoint.
  <sub>`Jev-like alternative` · ★41 · hunkim · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill)** — Skill for Hermes, and other agents, to ask typesafe's jev
  <sub>`Plugin` · ★39 · shantanugoel · `Py`</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)** — A gateway that mimics the structured-output shape, used to benchmark against it.
  <sub>`Benchmark` · ★38 · iammrduncan · `TS`</sub>

- **[jev-tree](https://github.com/Chuf-H/jev-tree)** — Jev-native probability tree and graph runtime for verifiable multi-step decision making.
  <sub>`Project` · ★37 · chuf-h · `Py`</sub>

- **[jev-spring-boot-starter](https://github.com/danvega/jev-spring-boot-starter)** — A simple Spring Boot 4 starter for TypeSafe Jev using Spring MVC and RestClient
  <sub>`Plugin` · ★36 · danvega · `Java` · ⚠ `no licence`</sub>

- **[jevify](https://github.com/fidecastro/jevify)** — Supersimple way to serve LLMs as a Jev-like endpoint
  <sub>`Jev-like alternative` · ★36 · fidecastro · `Py` · ⚠ `not Jev itself`</sub>

- **[jev_local](https://github.com/Argos1111/jev_local)** — Replicating Jev with a local LLM
  <sub>`Jev-like alternative` · ★35 · argos1111 · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[OpenSourceJev](https://github.com/sabeel111/OpenSourceJev)** — Turning an LLM model into a Jev like System.
  <sub>`Jev-like alternative` · ★33 · sabeel111 · `Py` · ⚠ `not Jev itself`</sub>

- **[pijev](https://github.com/TypeLLM/pijev)** — Averages Jev's answers over option orderings — all permutations in one request — with Brier score and log loss guaranteed no worse than the average across the orderings included. A one-line import change.
  <sub>`SDK` · ★33 · typellm · `Py`</sub>

- **[clash-jev](https://github.com/bytelabs-oss/clash-jev)** — A Clash Royale bot with no trained policy: Jev (TypeSafe System One) makes every decision from the live game state
  <sub>`Project` · ★32 · bytelabs-oss · `Py`</sub>

- **[is-jeven](https://github.com/wobsoriano/is-jeven)** — Is it even? Ask Jev.
  <sub>`Project` · ★32 · wobsoriano · `JS`</sub>

- **[jev (Elixir/OTP)](https://github.com/dannote/jev)** — Jev as an OTP process: reply from a GenServer and pattern match on the answer.
  <sub>`SDK` · ★32 · dannote · `Ex`</sub>

- **[jev-skill-suggester](https://github.com/win4r/jev-skill-suggester)** — 用 TypeSafe Jev 推荐已安装 Skill / Bounded installed-skill recommendations with TypeSafe Jev. Python CLI, Codex skill, bilingual docs and live examples.
  <sub>`Plugin` · ★32 · win4r · `Py`</sub>

- **[refgarden](https://github.com/AlbionaHoti/refgarden)** — A spatial reference explorer for creators. Local Jev query choices, metadata highlights and source-linked collections.
  <sub>`Jev-like alternative` · ★30 · albionahoti · `TS` · ⚠ `not Jev itself`</sub>

- **[st-jeved](https://github.com/mossyfield/ST-jeved)** — SillyTavern extension that measures each reply and instructs the narrator only when a rule matches.
  <sub>`Plugin` · ★30 · mossyfield · `JS`</sub>

- **[sys1](https://github.com/alvarobartt/sys1)** — System One compatible API for open decision models, e.g. Laya, written in Rust.
  <sub>`Jev-like alternative` · ★30 · alvarobartt · `Rs` · ⚠ `not Jev itself`</sub>

- **[jev-explained](https://github.com/davila7/jev-explained)** — Jev Explained
  <sub>`Tutorial` · ★29 · davila7 · `TS`</sub>

- **[jev-trades](https://github.com/zadescoxp/Jev-Trades)** — Trading bot with the all new TypeSafe AI's first system one model named as Jev
  <sub>`Project` · ★29 · zadescoxp · `Py`</sub>

- **[laya-vs-jev-arena](https://github.com/PromptEngineer48/laya-vs-jev-arena)** — Laya (open source, local) vs TypeSafe Jev (API): two AI models race in Snake and fight in a Mortal-Kombat-style arena. Every move is a real model decision.
  <sub>`Project` · ★29 · promptengineer48 · `JS`</sub>

- **[Jev-Quantum](https://github.com/karminski/Jev-Quantum)** — A Jev-protocol random baseline: it speaks noul, choice and score but reads no prompt, answering from a fast pseudo-random generator — a mock, and a lower bound for routing evaluations.
  <sub>`Jev-like alternative` · ★28 · karminski · `Rs` · ⚠ `not Jev itself`</sub>

- **[jevify](https://github.com/altryne/jevify)** — An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent community experiments.
  <sub>`Plugin` · ★27 · altryne · `Py`</sub>

- **[typesafe](https://github.com/krzyzanowskim/TypeSafe)** — TypeSafe SDK in Swift
  <sub>`SDK` · ★27 · krzyzanowskim · `Swift`</sub>

- **[jev-register-tool](https://github.com/2951461586/Jev-Register-Tool)** — TypeSafe（Jev / System One）申请 → 确认邮件 → 获批 → 注册 → 建 API Key 全链路工具，纯 HTTP 无浏览器
  <sub>`Project` · ★26 · 2951461586 · `Py` · ⚠ `no licence`</sub>

- **[loki](https://github.com/wundercorp/loki)** — The agent that evolves with you 𖤍
  <sub>`Project` · ★26 · wundercorp · `Py`</sub>

- **[OpenJev](https://github.com/zhangcy122/OpenJev)** — OpenJev: Open-source alternative to TypeSafe Jev. Typed probabilistic decision API (Choice, Noul, Score) powered by open LLMs & constrained logprob calibration.
  <sub>`Jev-like alternative` · ★26 · zhangcy122 · `Py` · ⚠ `not Jev itself`</sub>

- **[jev-cli](https://github.com/shaharia-lab/jev-cli)** — Command-line tool for TypeSafe AI's Jev model. Ask yes/no, multiple-choice and rubric questions about any text and get calibrated probabilities back. Answers become exit codes for shells and CI, JSON for scripts, and MCP tools for AI agents.
  <sub>`Project` · ★25 · shaharia-lab · `Rs`</sub>

- **[duckdb-jev](https://github.com/colliber/duckdb-jev)** — DuckDB extension: typed Jev answers as real SQL types
  <sub>`Plugin` · ★24 · colliber · `C++`</sub>

- **[jev-judge-mcp](https://github.com/PyModel/jev-judge-mcp)** — Typed judgment tools for MCP agents. TypeSafe's Jev model as verify, screen, find, classify, rerank, decide, compare, extract, review, gate, and score: the model judges, policy decides auto, review, or escalate.
  <sub>`Plugin` · ★24 · pymodel · `Py`</sub>

- **[jev-playground](https://github.com/mizchi/jev-playground)** — A playground for calling Jev from MoonBit, with a CLI per question type (score, choice, noul) and measured reports on which composition patterns win.
  <sub>`Project` · ★23 · mizchi · `TS` · ⚠ `no licence`</sub>

- **[typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground)** — Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts, A/B comparisons and a mobile-friendly UI.
  <sub>`Project` · ★20 · typesafeai · `TS`</sub>

- **[fastjev](https://github.com/chengyongru/fastjev)** — SDK-first, independently maintained SemIf fork for fast, self-hosted semantic decisions.
  <sub>`Jev-like alternative` · ★19 · chengyongru · `Py` · ⚠ `not Jev itself`</sub>

- **[jot](https://github.com/runta-dev/jot)** — The first general-purpose System One agent for Jev
  <sub>`Project` · ★19 · runta-dev · `TS` · ⚠ `no licence`</sub>

- **[ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)** — A structured-output provider for a Ruby LLM library.
  <sub>`Integration` · ★19 · kieranklaassen · `Rb`</sub>

- **[Jev](https://github.com/mayank953/Jev)** — Six live, side-by-side demos of Jev deciding while an LLM writes the words and code owns the control flow; the LLM side switches between Claude and Kimi models.
  <sub>`Project` · ★18 · mayank953 · `JS`</sub>

- **[jev-to-answer](https://github.com/csskrtao/jev-to-answer)** — A Book of Answers toy: ask a question and Jev picks the answer.
  <sub>`Project` · ★18 · csskrtao · `JS` · ⚠ `no licence`</sub>

- **[notjev](https://github.com/9pings/notjev)** — Super fast Jev like server, model agnostic, working with any OpenAI compatible endpoint
  <sub>`Jev-like alternative` · ★18 · 9pings · `JS` · ⚠ `not Jev itself`</sub>

- **[jevcore](https://github.com/PerryLink/jevcore)** — TypeSafe Jev for DeepSeek Harness, the Model Context Protocol, and plain Node: typed judgments instead of prose, offline by default.
  <sub>`SDK` · ★17 · perrylink · `TS`</sub>

- **[jevgraph](https://github.com/chenmingtang830/jevgraph)** — Evidence-backed knowledge graph construction with typed Jev relation decisions
  <sub>`Project` · ★17 · chenmingtang830 · `Py`</sub>

- **[jevloop](https://github.com/zjunlp/JevLoop)** — The agent loop where decisions don't cost a large language model call. Zero deps, runs offline, no API key needed.
  <sub>`Project` · ★17 · zjunlp · `TS`</sub>

- **[jevocks](https://github.com/unicodeveloper/jevocks)** — Everyday Stocks Status with Jev
  <sub>`Project` · ★17 · unicodeveloper · `TS` · ⚠ `no licence`</sub>

- **[snap](https://github.com/emnlmn/snap)** — Typed decisions from unstructured state: one forward pass, zero generated text. Local, deterministic, Jev-compatible. Not affiliated with typesafe.ai.
  <sub>`Jev-like alternative` · ★17 · emnlmn · `Rs` · ⚠ `not Jev itself` `no licence`</sub>

- **[go-jev](https://github.com/mattn/go-jev)** — Go SDK and CLI for TypeSafe Jev: typed decisions (yes/no, choice, score) from a model
  <sub>`SDK` · ★16 · mattn · `Go`</sub>

- **[jev-vs-ml](https://github.com/QuicqDev/Jev-vs-ML)** — Jev-vs-ML
  <sub>`Project` · ★16 · quicqdev · `Py` · ⚠ `no licence`</sub>

- **[hunch](https://github.com/carldaws/hunch)** — Probabilistic control flow for Ruby and Rails - powered by TypeSafe's Jev
  <sub>`SDK` · ★15 · carldaws · `Rb`</sub>

- **[jev](https://github.com/BorisLeMeec/jev)** — A claude code plugin for jev
  <sub>`Plugin` · ★15 · borislemeec · `Go`</sub>

- **[jev-studio](https://github.com/utk2103/jev-studio)** — if you're experimenting with jev it will be easier from here
  <sub>`Project` · ★15 · utk2103 · `Py`</sub>

- **[jevvy](https://github.com/PanAchy/jevvy)** — Jev-powered plugins for coding agents
  <sub>`Plugin` · ★15 · panachy · `TS`</sub>

- **[open-spark-jev](https://github.com/abhishek085/open-spark-jev)** — Open-source, local decision models inspired by TypeSafe’s Jev and System One - built on Qwen3 for NVIDIA DGX Spark.
  <sub>`Project` · ★15 · abhishek085 · `Py`</sub>

- **[swift-typesafe](https://github.com/ainame/swift-typesafe)** — Unofficial Swift SDK for TypeSafe
  <sub>`SDK` · ★15 · ainame · `Swift`</sub>

- **[jev-tetris](https://github.com/trungdq88/jev-tetris)** — Jev play Tetris in real-time against other AI models
  <sub>`Project` · ★14 · trungdq88 · `JS` · ⚠ `no licence`</sub>

- **[typesafe-sdk-go](https://github.com/atharvamhaske/typesafe-sdk-go)** — unofficial go sdk for typesafe ai. not affiliated with or endorsed by typesafe ai. a side project built to fill the missing go sdk gap, for the community to use.
  <sub>`SDK` · ★14 · atharvamhaske · `Go`</sub>

- **[jev_stock](https://github.com/sosopop/jev_stock)** — An experimental JEV-powered framework for forecasting short-term stock price direction from structured market data.
  <sub>`Project` · ★13 · sosopop · `Py` · ⚠ `no licence`</sub>

- **[llm-typesafe](https://github.com/simonw/llm-typesafe)** — LLM plugin for accessing Jev and other TypeSafe AI models
  <sub>`Plugin` · ★13 · simonw · `Py`</sub>

- **[typesafe-playground](https://github.com/kavehmz/typesafe-playground)** — Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.
  <sub>`Project` · ★13 · kavehmz · `JS` · ⚠ `no licence`</sub>

- **[typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router)** — TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.
  <sub>`Plugin` · ★13 · decrux9812 · `Py`</sub>

- **[jev-cli](https://github.com/tumf/jev-cli)** — Small dependency-free CLI for TypeSafe Jev
  <sub>`SDK` · ★12 · tumf · `Py`</sub>

- **[jevper](https://github.com/zhulinchng/jevper)** — Jev-shaped (TypeSafe System One) classification wrapper over OpenAI-like clients: probabilities and confidence instead of prose
  <sub>`Jev-like alternative` · ★12 · zhulinchng · `Py` · ⚠ `not Jev itself`</sub>

- **[jevthoven](https://github.com/cocktailpeanut/jevthoven)** — AI Music (MIDI) generator powered by Jev
  <sub>`Project` · ★12 · cocktailpeanut · `TS`</sub>

- **[snapjudge](https://github.com/Micha0827/snapjudge)** — Typed decisions (choice / score / yes-no) from local Qwen models on Apple Silicon. Probabilities come straight from the logits, no text generation. TypeSafe-compatible HTTP API, runs on MLX.
  <sub>`Jev-like alternative` · ★12 · micha0827 · `Py` · ⚠ `not Jev itself`</sub>

- **[typesafe-ai](https://github.com/Twister915/typesafe-ai)** — Typed TypeSafe AI clients for Rust, with async and blocking backends and observable retries.
  <sub>`SDK` · ★12 · twister915 · `Rs`</sub>

- **[jev-chat-for-twitch](https://github.com/ethanplusai/jev-chat-for-twitch)** — Filter any live Twitch chat with Jev: a bring-your-own-key Chrome extension
  <sub>`Plugin` · ★11 · ethanplusai · `JS`</sub>

- **[pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)** — TypeSafe Jev as the pi coding agent's quiet decision layer
  <sub>`Project` · ★11 · hyunjunjeon · `TS`</sub>

- **[swift-jev](https://github.com/d-date/swift-jev)** — A Swift client for TypeSafe AI's Jev — typed judgements, not text
  <sub>`SDK` · ★11 · d-date · `Swift`</sub>

- **[xtags](https://github.com/manifoldor/xtags)** — 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型。
  <sub>`Project` · ★11 · manifoldor · `JS`</sub>

- **[jev](https://github.com/okooo5km/jev)** — Typed decisions from the shell: an unofficial stdlib-Python CLI and Agent Skill for TypeSafe's Jev model, via the TypeSafe API (default) or OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode.
  <sub>`Plugin` · ★10 · okooo5km · `Py`</sub>

- **[jev-recipes](https://github.com/agencyenterprise/jev-recipes)** — 80+ composable TypeScript recipes powered by Jev for AI agents, retrieval, answer verification, and conversation workflows.
  <sub>`Project` · ★10 · agencyenterprise · `TS`</sub>

- **[JevAny](https://github.com/weitianxin/JevAny)** — JevAny: a calibrated decision layer for RL, agents and model harnesses that returns typed answers and option probabilities in one prefill pass — an open 27B model on a Qwen backbone, not Jev.
  <sub>`Jev-like alternative` · ★10 · weitianxin · `Py` · ⚠ `not Jev itself`</sub>

- **[jevernetes](https://github.com/sunil-sadasivan/jevernetes)** — Live Kubernetes log analysis, contextual investigation, and agent handoff powered by Jev.
  <sub>`Project` · ★10 · sunil-sadasivan · `Py`</sub>

- **[jev_project_context](https://github.com/poiuyjie/jev_project_context)** — Evidence-first long-term experiment memory skill for AI coding agents, with optional Jev decision-model layers
  <sub>`Plugin` · ★9 · poiuyjie · `Py`</sub>

- **[jpp](https://github.com/Towow-ai/jpp)** — J++: an experimental language with standalone source and a Rust runtime. Compose questions and methods. 独立源码，组合问题与方法。
  <sub>`Project` · ★9 · towow-ai · `Rs`</sub>

- **[typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go)** — Go SDK for the TypeSafe AI API — typed questions in, probability distributions out.
  <sub>`SDK` · ★9 · tangerg · `Go`</sub>

- **[edgejev](https://github.com/yzfly/edgejev)** — 离线可用的本地类型化决策：4 核 CPU 单题 15.6ms。Local & offline Jev / System One inference on CPU — ONNX + INT8, no torch at runtime. 支持 laya / kev / PlayJev
  <sub>`Project` · ★8 · yzfly · `Py`</sub>

- **[jeq](https://github.com/cristianoliveira/jeq)** — What happens when jev meets jq? Intelligence you can pipe for quick experimentation and scripts
  <sub>`Project` · ★8 · cristianoliveira · `Go`</sub>

- **[jev-minesweeper](https://github.com/comoc/jev-minesweeper)** — TypeSafe Jev (System One) にブラウザ上のマインスイーパーを解かせるデモ
  <sub>`Project` · ★8 · comoc · `JS` · ⚠ `no licence`</sub>

- **[laya-jev-lab](https://github.com/yibie/laya-jev-lab)** — Independent measurements of typed-decision models: Jev (TypeSafe API) vs Laya (open weights), and a local-first cascade that matches Jev's accuracy at 1.8x the speed
  <sub>`Project` · ★8 · yibie · `Py`</sub>

- **[trade-jev](https://github.com/justinhe16/trade-jev)** — Backtest Jev (TypeSafe) as a BUY/SELL/HOLD trader on NQ L10 order-book data
  <sub>`Project` · ★8 · justinhe16 · `Py`</sub>

- **[typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk)** — Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.
  <sub>`SDK` · ★8 · saibimajdi · `C#`</sub>

- **[jev-grand-prix](https://github.com/enoyola/jev-grand-prix)** — An F1 racing game where TypeSafe's Jev picks the racing line and the pedals, and learns each corner's limit between laps
  <sub>`Project` · ★7 · enoyola · `JS`</sub>

- **[jev-mcp](https://github.com/rashedInt32/jev-mcp)** — MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.
  <sub>`Plugin` · ★7 · rashedint32 · `TS`</sub>

- **[jev-mcp](https://github.com/arunav25/jev-mcp)** — Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.
  <sub>`Plugin` · ★7 · arunav25 · `JS`</sub>

- **[jev_jsonschema](https://github.com/Kiln-AI/jev_jsonschema)** — Run a JSON Schema through TypeSafe's Jev API, and get JSON back.
  <sub>`Project` · ★7 · kiln-ai · `Py`</sub>

- **[jevgo](https://github.com/devbackend/jevgo)** — Unofficial Go client for the TypeSafe AI System One API (Jev) — typed questions in, calibrated answers out.
  <sub>`SDK` · ★7 · devbackend · `Go`</sub>

- **[switchboard](https://github.com/ruban-24/switchboard)** — An open-source, model-agnostic decision router for Claude Code and Codex.
  <sub>`Plugin` · ★7 · ruban-24 · `TS`</sub>

- **[typesafe-sdk](https://github.com/joshmn/typesafe-sdk)** — Ruby client for typesafe.ai
  <sub>`SDK` · ★7 · joshmn · `Rb`</sub>

- **[awesome-jev](https://github.com/daftAI2026/awesome-jev)** — TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)
  <sub>`Project` · ★6 · daftai2026 · `TS` · ⚠ `no licence`</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs
  <sub>`Benchmark` · ★6 · wondertwins · `Py`</sub>

- **[jev-canvas](https://github.com/gaborishka/jev-canvas)** — Draw on a tldraw canvas with your voice and a pointing finger. Jev (TypeSafe System One) decides action, target and place in ~350 ms per spoken word.
  <sub>`Project` · ★6 · gaborishka · `JS`</sub>

- **[jev-chat-windows-deepseek-jev](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev)** — Windows 微信回复助手：DeepSeek 官方生成话术，TypeSafe JEV 官方判断排序，支持可取消的 3 秒自动发送。
  <sub>`Project` · ★6 · aimark-dai · `Py`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — Reproducible early-access evaluation of Jev on Korean understanding and medical text, with runtime and cost evidence
  <sub>`Benchmark` · ★6 · mahlernim · `Py` · ⚠ `no licence`</sub>

- **[jev-search](https://github.com/larguesa/jev-search)** — Experimental semantic line search with TypeSafe Jev via OpenRouter. Python CLI with no runtime dependencies.
  <sub>`Project` · ★6 · larguesa · `Py`</sub>

- **[jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver)** — A Chrome extension that covers distracting YouTube videos with Jev. Show anyway whenever you want.
  <sub>`Plugin` · ★6 · jaibhasin · `JS` · ⚠ `no licence`</sub>

- **[jevtest](https://github.com/joshhu/jevtest)** — 情緒測謊器：嘴上說「好」，心裡真的好嗎？用 TypeSafe Jev（System One 模型）透過 OpenRouter 即時判斷，並與一般 LLM 對照
  <sub>`Project` · ★6 · joshhu · `TS` · ⚠ `no licence`</sub>

- **[learn-jev-end-to-end](https://github.com/harshithsunku/learn-jev-end-to-end)** — Learn Jev end to end: a free hands-on course. Build 13 AI agent use cases with a fast brain (Jev) and a slow brain (LLM). One OpenRouter key.
  <sub>`Tutorial` · ★6 · harshithsunku · `Py`</sub>

- **[mcts-agent](https://github.com/lhemerly/mcts-agent)** — Discriminative Monte Carlo Tree Search using TypeSafe Jev System One Primitives and Gemini
  <sub>`Project` · ★6 · lhemerly · `Py`</sub>

- **[midscene-jev-runner](https://github.com/KiritoKing/midscene-jev-runner)** — Community-maintained JEV runner integration for Midscene Test
  <sub>`Integration` · ★6 · kiritoking · `TS`</sub>

- **[ruling](https://github.com/bradAGI/ruling)** — Typed, calibrated decisions from a local model. No text generated.
  <sub>`Jev-like alternative` · ★6 · bradagi · `Py` · ⚠ `not Jev itself` `unverified claims`</sub>

- **[secondlayer](https://github.com/ryanwaits/secondlayer)** — Decoded Stacks data in your own database. Self-hosted.
  <sub>`Project` · ★6 · ryanwaits · `TS`</sub>

- **[ai-elo-ranker](https://github.com/opaielsheikh/ai-elo-ranker)** — High-speed recursive AI Elo tournament engine powered by Jev and Swiss matchmaking
  <sub>`Project` · ★5 · opaielsheikh · `Py` · ⚠ `no licence`</sub>

- **[jev-2048](https://github.com/ARCJ137442/jev-2048)** — An instrumented 2048 web lab where every move is a Jev (TypeSafe AI System One) Choice, with no heuristic fallback \| 用 Jev 决策模型驱动每一步的 2048 网页实验台，概率、置信度、延迟与成本全部摊开可见，且刻意不做启发式兜底
  <sub>`Project` · ★5 · arcj137442 · `TS`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — A show-and-tell capability study for Jev, TypeSafe's System One decision model.
  <sub>`Benchmark` · ★5 · lbotinelly · `TS`</sub>

- **[jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon)** — Playing Pokemon Red using TypeSafe Jev
  <sub>`Project` · ★5 · milanboers · `Py`</sub>

- **[jev-system-one](https://github.com/haseeb-heaven/jev-system-one)** — A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports
  <sub>`Project` · ★5 · haseeb-heaven · `Py`</sub>

- **[jev4k](https://github.com/pambrose/jev4k)** — A Kotlin DSL and client for TypeSafe's Jev model
  <sub>`SDK` · ★5 · pambrose · `Kt`</sub>

- **[Jev_Ontology](https://github.com/dagfinndybvig/Jev_Ontology)** — Trying to combine Jev with ontology
  <sub>`Project` · ★5 · dagfinndybvig · `Py` · ⚠ `no licence`</sub>

- **[jevlang](https://github.com/sumanmichael/jevlang)** — The simplest way to write decision workflows in Python. Python with a smart if.
  <sub>`SDK` · ★5 · sumanmichael · `Py`</sub>

- **[jevplayspokemon](https://github.com/anxkhn/JevPlaysPokemon)** — Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM.
  <sub>`Project` · ★5 · anxkhn · `TS`</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD benchmark alpha and official evaluation workflows
  <sub>`Benchmark` · ★5 · johnhughes3 · `Py`</sub>

- **[OpenJev](https://github.com/xingwudao/OpenJev)** — OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.
  <sub>`Jev-like alternative` · ★5 · xingwudao · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs)** — Independent async and blocking Rust SDK for the TypeSafe AI System One API
  <sub>`SDK` · ★5 · gilljon · `Rs`</sub>

- **[typesafe-ui](https://github.com/TypeSafeAI/typesafe-ui)** — shadcn-style reusable components and blocks for using TypeSafe AI.
  <sub>`Project` · ★5 · bunsdev · `TS` · ⚠ `no licence`</sub>

- **[typesafe_sdk (Elixir)](https://github.com/nshkrdotcom/typesafe_sdk)** — An Elixir port of the official SDK.
  <sub>`SDK` · ★5 · nshkrdotcom · `Ex`</sub>

- **[dohnuts.cpp](https://github.com/DreamBlooms/dohnuts.cpp)** — The same decisions, on CPU. System One model that can run on your Personal Computer.
  <sub>`Jev-like alternative` · ★4 · dreamblooms · `C++` · ⚠ `not Jev itself`</sub>

- **[jcm-router](https://github.com/adarshmishra07/jcm-router)** — Local proxy that picks the Claude model and effort per message using TypeSafe Jev. Routes subagents, leaves your cached main chat alone.
  <sub>`Project` · ★4 · adarshmishra07 · `TS`</sub>

- **[jev-android](https://github.com/dougsong/jev-android)** — A Kotlin Android SDK for UI automation powered by TypeSafe Jev, with an accessibility runtime and sample app.
  <sub>`SDK` · ★4 · dougsong · `Kt`</sub>

- **[jev-arena-nanojev](https://github.com/liao96312/jev-arena-nanojev)** — 完全本地的 NanoJev 网格决策游戏实验场，支持中文 Pygame、多关卡与 GTX 1660S 训练
  <sub>`Project` · ★4 · liao96312 · `Py` · ⚠ `no licence`</sub>

- **[jev-bot](https://github.com/nssmd/jev-bot)** — Self-hosted Jev decision workbench and Feishu bot: automatic choices, probabilities, and experimental word/character writing.
  <sub>`Project` · ★4 · nssmd · `JS`</sub>

- **[jev-chat](https://github.com/adhyaay-karnwal/jev-chat)** — A chatbot from typed Jev decisions: hierarchical speculative decoding over System One probabilities.
  <sub>`Project` · ★4 · adhyaay-karnwal · `Py`</sub>

- **[jev-cookbook](https://github.com/paramjeetn/jev-cookbook)** — The complete cookbook for Jev by TypeSafe AI — 120+ use cases, 10 runnable examples, 4 composition patterns, and first-principles theory for the world's first System One AI model.
  <sub>`Tutorial` · ★4 · paramjeetn · `Py`</sub>

- **[jev-docs-zh](https://github.com/Bald0Wang/jev-docs-zh)** — Jev 模型（TypeSafe AI）官方使用文档的中文翻译 \| Unofficial Chinese translation of the official Jev (TypeSafe AI) docs — https://docs.typesafe.ai
  <sub>`Project` · ★4 · bald0wang · `Py` · ⚠ `no licence`</sub>

- **[jev-go](https://github.com/Gaurav-Gosain/jev-go)** — Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text
  <sub>`SDK` · ★4 · gaurav-gosain · `Go`</sub>

- **[jev-grug](https://github.com/mkotlikov/jev-grug)** — Helping JEV speak <3
  <sub>`Project` · ★4 · mkotlikov · `TS`</sub>

- **[jev-realtime-trading](https://github.com/rthomas24/jev-realtime-trading)** — Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.
  <sub>`Project` · ★4 · rthomas24 · `TS`</sub>

- **[jev-trip](https://github.com/liaoyuhua/jev-trip)** — Two Minds, One Trip. https://jev-trip.vercel.app/
  <sub>`Project` · ★4 · liaoyuhua · `TS`</sub>

- **[jev-wingman](https://github.com/1104480426-hash/jev-wingman)** — 基于 Jev 的聊天决策辅助，不挑 App（QQ / 微信 / 飞书皆可）· An on-device chat co-pilot that returns typed verdicts instead of prose, built on Jev
  <sub>`Project` · ★4 · 1104480426-hash · `Java`</sub>

- **[jevopt](https://github.com/Ramneet-Singh/jevopt)** — Making intelligent compiler optimisation decisions with Jev
  <sub>`Project` · ★4 · ramneet-singh · `Py`</sub>

- **[jevseek](https://github.com/blingdivinity/jevseek)** — DeepSeek proposes the next token, TypeSafe's Jev chooses it: a decision model used as a sampler
  <sub>`Project` · ★4 · blingdivinity · `Py`</sub>

- **[OpenJev](https://github.com/GPT-AGI/OpenJev)** — Jev-compatible System 开源Jev
  <sub>`Jev-like alternative` · ★4 · gpt-agi · `Py` · ⚠ `not Jev itself`</sub>

- **[rubikjev](https://github.com/0xtrou/rubikjev)** — Challenge the Jev's intelligence in Rubik Cube puzzles
  <sub>`Project` · ★4 · 0xtrou · `TS` · ⚠ `no licence`</sub>

- **[rust-sysone](https://github.com/zcoder-run/rust-sysone)** — System One TypeSafe AI Rust Client (unofficial)
  <sub>`Project` · ★4 · zcoder-run · `Rs`</sub>

- **[soupbase](https://github.com/spoonnotfound/soupbase)** — Jev x 海龟汤
  <sub>`Project` · ★4 · spoonnotfound · `TS`</sub>

- **[sysone-bench](https://github.com/instax-dutta/sysone-bench)** — First independent head-to-head benchmark of System One decision models (Laya vs Jev) on byte-identical inputs
  <sub>`Benchmark` · ★4 · instax-dutta · `Py`</sub>

- **[typesafe-ai-go](https://github.com/kisshan13/typesafe-ai-go)** — Community-maintained Go SDK for the TypeSafe AI System One evaluation API, with typed questions, fluent builders, retries, and examples.
  <sub>`SDK` · ★4 · kisshan13 · `Go`</sub>

- **[typesafe-ai-java](https://github.com/jamilxt/typesafe-ai-java)** — Community-maintained Java SDK for the TypeSafe AI System One (Jev) API. Not an official TypeSafe product.
  <sub>`SDK` · ★4 · jamilxt · `Java` · ⚠ `no licence`</sub>

- **[typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift)** — Unofficial Swift library for the TypeSafe API
  <sub>`SDK` · ★4 · alterhq · `Swift`</sub>

- **[alphaoptimizer](https://github.com/alpha-tales/alphaoptimizer)** — Jev-powered output optimization for Codex, built to keep large tool results concise and usable.
  <sub>`Plugin` · ★3 · alpha-tales · `TS`</sub>

- **[awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases)** — Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.
  <sub>`Project` · ★3 · seeapi · `Py`</sub>

- **[cairn-jev-lab](https://github.com/Cairn-ink/cairn-jev-lab)** — Test what your AI should remember. An experimental, source-aware memory admission evaluator powered by Jev, with editable cases and inspectable results.
  <sub>`Project` · ★3 · cairn-ink · `JS`</sub>

- **[cu-Jev](https://github.com/dtunai/cu-Jev)** — cuda-Jev — a CUDA-native Jev System One decision inference engine. Jev compatible API, examples, and reproducible benchmarks.
  <sub>`Jev-like alternative` · ★3 · dtunai · `C` · ⚠ `not Jev itself`</sub>

- **[dbt_jev](https://github.com/smithclay/dbt_jev)** — use jev in dbt
  <sub>`Plugin` · ★3 · smithclay · `Py`</sub>

- **[everything-about-jev](https://github.com/qingshungLI/everything-about-jev)** — tell you everything about jev,TypeSafe AI's System One model for typed decisions.
  <sub>`Project` · ★3 · qingshungli · `Py`</sub>

- **[go-system-one](https://github.com/rcarmo/go-system-one)** — when a gopher met Jev
  <sub>`SDK` · ★3 · rcarmo · `Go`</sub>

- **[Jev](https://github.com/cobusgreyling/Jev)** — Unofficial TypeSafe Jev showcase — System One decisions, not chat.
  <sub>`Project` · ★3 · cobusgreyling · `Py`</sub>

- **[jev-cli](https://github.com/jtsang4/jev-cli)** — CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out
  <sub>`Project` · ★3 · jtsang4 · `TS`</sub>

- **[jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)** — Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.
  <sub>`Benchmark` · ★3 · kantahayashiai · `JS`</sub>

- **[jev-gomoku](https://github.com/XieChengYuan/jev-gomoku)** — 弈瞬：双 Jev 五子棋九宫格输入实验台，逐手查看模型决策，支持真实对局回放与实时对战。
  <sub>`Project` · ★3 · xiechengyuan · `JS` · ⚠ `no licence`</sub>

- **[jev-java](https://github.com/Olti1947/jev-java)** — Idiomatic Java SDK for TypeSafe AI Jev System One decision engine
  <sub>`SDK` · ★3 · olti1947 · `Java` · ⚠ `no licence`</sub>

- **[jev-java](https://github.com/gudcks0305/jev-java)** — Unofficial Java SDK for TypeSafe Jev and Vercel AI Gateway, with Spring Boot and WebClient support
  <sub>`SDK` · ★3 · gudcks0305 · `Java`</sub>

- **[jev-resume-disqualifier](https://github.com/AiPersonacademy/jev-resume-disqualifier)** — Jev Resume Disqualifier: Sub-25ms automated resume knockout engine powered by TypeSafe Jev System One decision intelligence. Eliminates 80% of unqualified applicants with deterministic date math & EEOC-safe rejection notices.
  <sub>`Project` · ★3 · aipersonacademy · `Py`</sub>

- **[jev-rs](https://github.com/abeldzan/jev-rs)** — Async-first Rust SDK for the TypeSafe AI API
  <sub>`SDK` · ★3 · abeldzan · `Rs`</sub>

- **[jevtown](https://github.com/gaborishka/jevtown)** — Jevtown: a social network where people write and 10,000 AI personas react
  <sub>`Project` · ★3 · gaborishka · `JS`</sub>

- **[n8n-nodes-jev](https://github.com/vibe-with-me-tools/n8n-nodes-jev)** — Helper n8n community node for Jev by TypeSafe. Classify, route, and score text with questions you define, and get a probability for every answer so unsure items can go to review.
  <sub>`Plugin` · ★3 · vibe-with-me-tools · `TS`</sub>

- **[new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe)** — TypeSafe AI System One (Jev) task plugin for QuantumNous/new-api — native /v1/systemone, synchronous evaluation, token billing
  <sub>`Plugin` · ★3 · ffattiger · `JS`</sub>

- **[origin-civilization](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)** — AI life-and-civilization simulation: TypeSafe Jev makes every decision (typed, probabilistic, auditable); LLMs plan — OpenAI-compatible APIs, local models (Ollama, LM Studio), Claude Code, Codex.
  <sub>`Benchmark` · ★3 · jacquesgariepy · `TS`</sub>

- **[pydantic-jev-examples](https://github.com/adtyavrdhn/pydantic-jev-examples)** — Pydantic AI capabilities made stronger with Jev: small runnable demos, one file each
  <sub>`Project` · ★3 · adtyavrdhn · `Py` · ⚠ `no licence`</sub>

- **[should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all)** — We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.
  <sub>`Project` · ★3 · hellogumbo · `JS`</sub>

- **[sqlite3-jev](https://github.com/mattn/sqlite3-jev)** — SQLite extension that calls TypeSafe Jev (or tensai serve) from SQL
  <sub>`Plugin` · ★3 · mattn · `C`</sub>

- **[system-one-chess](https://github.com/dperezcabrera/system-one-chess)** — Chess against Jev, TypeSafe AI's System One model, through OpenRouter. Built with the pico framework.
  <sub>`Project` · ★3 · dperezcabrera · `Py`</sub>

- **[systemone-lite](https://github.com/fritzprix/systemone-lite)** — Toy local System One–style decision API (Jev-shaped). Not affiliated with TypeSafe.
  <sub>`Project` · ★3 · fritzprix · `Py`</sub>

- **[SystemOneDotNet](https://github.com/JabbaKadabra/SystemOneDotNet)** — .NET client for TypeSafe System One (Jev) — typed questions in, typed answers with probabilities and confidence out. No prompt engineering, no output parsing.
  <sub>`SDK` · ★3 · jabbakadabra · `C#`</sub>

- **[tinyjev](https://github.com/ankit-aglawe/tinyjev)** — A tiny jev-like model that answers Choice, Score and Noul questions in one forward pass and returns calibrated probabilities. MLX or PyTorch, fully offline, System One compatible.
  <sub>`Jev-like alternative` · ★3 · ankit-aglawe · `Py` · ⚠ `not Jev itself`</sub>

- **[typesafe-ai-rails](https://github.com/GenieRobot/typesafe-ai-rails)** — Community Rails integration for TypeSafe AI's System One API on the community typesafe-sdk gem: Rails configuration, persisted usage and cost telemetry, and an opt-in confidence policy for Choice and Score answers.
  <sub>`SDK` · ★3 · genierobot · `Rb`</sub>

- **[typesafe-assist](https://github.com/JanOstrowka/typesafe-assist)** — Home Assistant Assist conversation agent powered by TypeSafe's Jev (System One) model
  <sub>`Project` · ★3 · janostrowka · `Py` · ⚠ `no licence`</sub>

- **[typesafe-sdk-dotnet](https://github.com/hardkoded/typesafe-sdk-dotnet)** — Unofficial .NET port of the TypeSafe AI client SDK (typed questions & answers)
  <sub>`SDK` · ★3 · hardkoded · `C#`</sub>

- **[typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java)** — Community Java client for the TypeSafe System One API (unofficial)
  <sub>`SDK` · ★3 · premo-cloud · `Java`</sub>

- **[typesafe-sdk-rust](https://github.com/codeitlikemiley/typesafe-sdk-rust)** — Rust SDK for the TypeSafe AI API
  <sub>`SDK` · ★3 · codeitlikemiley · `Rs`</sub>

- **[typesafe-sdk-swift](https://github.com/InsaneArts/typesafe-sdk-swift)** — Swift SDK for TypeSafe AI
  <sub>`SDK` · ★3 · insanearts · `Swift`</sub>

- **[werr](https://github.com/pCwOrM/werr)** — Zero-memory System-1 decision engine & TypeSafe Jev wire-compatible runtime powered by Mandelbrot wave dynamics (The Zero-VRAM Gauntlet).
  <sub>`Jev-like alternative` · ★3 · pcworm · `Py` · ⚠ `not Jev itself`</sub>

- **[agent-jev-tetris](https://github.com/Yasserbhb/Agent-JEV-Tetris)** — using the new model JEV to play the game tetris
  <sub>`Project` · ★2 · yasserbhb · `TS` · ⚠ `no licence`</sub>

- **[ailerix](https://github.com/tylerjharden/ailerix)** — Type-safe model router. Jev (System One) banks each request to a typed catalog route.
  <sub>`Project` · ★2 · tylerjharden · `TS` · ⚠ `no licence`</sub>

- **[auto-mode-for-paseo](https://github.com/obetomuniz/auto-mode-for-paseo)** — A Paseo provider that uses TypeSafe Jev to route each Codex turn.
  <sub>`Plugin` · ★2 · obetomuniz · `TS`</sub>

- **[barrunto](https://github.com/elpumberto/barrunto)** — A Chrome extension that brings TypeSafe's Jev to X.com to analyze posts as you browse
  <sub>`Plugin` · ★2 · elpumberto · `TS`</sub>

- **[bes-kelime-jev](https://github.com/mahmut-gundogdu/bes-kelime-jev)** — Ne yazarsanız yazın, beş kelimeden biriyle cevap veren sohbet botu. Kelimeyi TypeSafe AI'ın Jev evaluation modeli seçer.
  <sub>`Project` · ★2 · mahmut-gundogdu · `TS`</sub>

- **[btc-jev-signal](https://github.com/WebGrga/btc-jev-signal)** — Experimental multi-horizon BTC signal generator using TypeSafe Jev probabilities and Binance market data.
  <sub>`Project` · ★2 · webgrga · `TS` · ⚠ `no licence`</sub>

- **[chat2jev](https://github.com/Chandler-Sun/chat2jev)** — Convert legacy chat completion API request to Typesafe jev API
  <sub>`SDK` · ★2 · chandler-sun · `TS`</sub>

- **[decisions-judge-mcp](https://github.com/clouatre-labs/decisions-judge-mcp)** — Typed decisions for AI agents as an MCP tool: yes/no probability (noul), choice, and score in one fast request. Backed by the TypeSafe System One model.
  <sub>`Plugin` · ★2 · clouatre-labs · `JS`</sub>

- **[diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)** — A Jev-like decision engine powered by DiffusionGemma and SGLang. Jev with eyes.
  <sub>`Jev-like alternative` · ★2 · hangzhi · `Py` · ⚠ `not Jev itself`</sub>

- **[emoji-jev](https://github.com/colinmcdermott/emoji-jev)** — Emoji autocomplete at the speed of typing. TypeSafe AI Jev on a Whop-hosted TanStack Start app.
  <sub>`Project` · ★2 · colinmcdermott · `TS` · ⚠ `no licence`</sub>

- **[git-jev-stage](https://github.com/ibrahemid/git-jev-stage)** — Select Git changes for staging with a plain-language description.
  <sub>`Project` · ★2 · ibrahemid · `TS`</sub>

- **[got-jev](https://github.com/phureewat29/jev-got)** — Jev (TypeSafe AI) PoC through Game of Thrones
  <sub>`Project` · ★2 · phureewat29 · `TS` · ⚠ `no licence`</sub>

- **[ha-conversation-jev](https://github.com/luxus/ha-conversation-jev)** — Home Assistant custom component: Conversation agent with Jev fast-path + Grok fallback
  <sub>`Project` · ★2 · luxus · `Py` · ⚠ `no licence`</sub>

- **[hermes-jev-curator](https://github.com/anpicasso/hermes-jev-curator)** — Typed Jev relation governance and safe archive plans for Hermes Curator
  <sub>`Project` · ★2 · anpicasso · `Py`</sub>

- **[jear](https://github.com/iJ03l/jear)** — Jev-routed client for NEAR AI Cloud inference and IronClaw agents.
  <sub>`SDK` · ★2 · ij03l · `Rs`</sub>

- **[jeff-cli](https://github.com/saembit/jeff-cli)** — jeff, a Go CLI for Jev: from a shell script, give it state and a question with fixed answers and get calibrated probabilities back, with a rank command and meaningful exit codes.
  <sub>`Project` · ★2 · saembit · `Go`</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset).
  <sub>`Benchmark` · ★2 · tokentrim · `Py`</sub>

- **[jev-blindspot](https://github.com/jsk4581/jev-blindspot)** — A side-panel assistant that finds the blind spots in your prompts. For Claude Code and Codex CLI.
  <sub>`Plugin` · ★2 · jsk4581 · `TS`</sub>

- **[jev-broadcast-lab](https://github.com/4anti/jev-broadcast-lab)** — Testing Lab for Jev AI
  <sub>`Project` · ★2 · 4anti · `JS` · ⚠ `no licence`</sub>

- **[jev-ci-selector](https://github.com/guilhem/jev-ci-selector)** — Conservative CI task selection for GitHub Actions with Jev, a pure policy engine, and shadow mode by default.
  <sub>`Project` · ★2 · guilhem · `TS`</sub>

- **[jev-cloud-quiz](https://github.com/minorun365/jev-cloud-quiz)** — A demo in which Jev judges, with probabilities, which of the three big clouds a feature name belongs to.
  <sub>`Project` · ★2 · minorun365 · `TS`</sub>

- **[jev-codex-router-skill](https://github.com/455-dIAO/jev-codex-router-skill)** — Portable Codex Skill for Jev model and reasoning-effort routing, with safe installation and Chinese usage guides
  <sub>`Plugin` · ★2 · 455-diao · `Py` · ⚠ `no licence`</sub>

- **[jev-connector](https://github.com/juanlentino/jev-connector)** — WordPress connector for TypeSafe Jev: typed, confidence-scored answers your code can branch on.
  <sub>`Plugin` · ★2 · juanlentino · `PHP`</sub>

- **[jev-cvss](https://github.com/Red5d/jev-cvss)** — Fast CVSS scoring from vulnerability descriptions using Typesafe Jev
  <sub>`Project` · ★2 · red5d · `Py`</sub>

- **[jev-freeform](https://github.com/kesku/jev-freeform)** — An observable raw-character chat experiment powered entirely by TypeSafe Jev Choice
  <sub>`Project` · ★2 · kesku · `JS` · ⚠ `no licence`</sub>

- **[jev-mcp](https://github.com/BYK/jev-mcp)** — An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.
  <sub>`Plugin` · ★2 · byk · `TS`</sub>

- **[jev-mcp](https://github.com/freepik-company/jev-mcp)** — MCP server for typed decisions with Jev / System One via OpenRouter or TypeSafe
  <sub>`Plugin` · ★2 · freepik-company · `Go`</sub>

- **[jev-mcp](https://github.com/rajasekharponakala/jev-mcp)** — MCP server wrapping TypeSafe's Jev System One models — typed noul/choice/score judgments for AI agents
  <sub>`Plugin` · ★2 · rajasekharponakala · `Py`</sub>

- **[jev-mcp-spring](https://github.com/Ashfaqbs/jev-mcp-spring)** — Java/Spring Boot MCP server for TypeSafe Jev
  <sub>`Plugin` · ★2 · ashfaqbs · `Java`</sub>

- **[jev-php-sdk](https://github.com/mzainzulifqar/jev-php-sdk)** — PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13.
  <sub>`SDK` · ★2 · mzainzulifqar · `PHP`</sub>

- **[jev-pii-checker](https://github.com/coo-quack/jev-pii-checker)** — CLI that finds PII in text with TypeSafe Jev: presence, sensitivity, and located spans
  <sub>`Project` · ★2 · coo-quack · `TS`</sub>

- **[jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment)** — Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena
  <sub>`Benchmark` · ★2 · tokentrim · `Py`</sub>

- **[jev-sdk-java](https://github.com/luigivis/jev-sdk-java)** — Type-safe Java 21 client for the TypeSafe AI Jev (System One) decision API
  <sub>`SDK` · ★2 · luigivis · `Java`</sub>

- **[jev-x-kit](https://github.com/Kadihx/jev-x-kit)** — Offline $0 decision layer for coding agents: Choice/Score/Noul primitives, BELKI confidence gatekeeper, ultra-planning, red-teaming, research and RLVR self-improvement -- as an MCP server + CLI + Claude Code skill.
  <sub>`Project` · ★2 · kadihx · `TS`</sub>

- **[jev4mellea](https://github.com/SoundBlaster/Jev4Mellea)** — Jev adapter for Mellea
  <sub>`Integration` · ★2 · soundblaster · `Py`</sub>

- **[jevclient](https://github.com/AboveColin/jevclient)** — Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.
  <sub>`SDK` · ★2 · abovecolin · `Py`</sub>

- **[jevgo](https://github.com/fgn/jevgo)** — Go client for TypeSafe AI's System One API (Jev), with optional Langfuse instrumentation
  <sub>`SDK` · ★2 · fgn · `Go`</sub>

- **[jevmem](https://github.com/Avinash-jetwani/jevmem)** — Automatic project memory for Claude Code. Also works with Cursor and Codex.
  <sub>`Plugin` · ★2 · avinash-jetwani · `TS`</sub>

- **[jevslop](https://github.com/TKY-27/JevSlop)** — Jevによるnote記事のAI Slop判定サイト
  <sub>`Project` · ★2 · tky-27 · `TS`</sub>

- **[jevtok](https://github.com/LabGuy94/jevtok)** — Exact token counting and request-cost prediction for TypeSafe's Jev (tiktoken-style)
  <sub>`Project` · ★2 · labguy94 · `Py`</sub>

- **[kojev](https://github.com/ItisNoMatter/kojev)** — Kotlin Multiplatform client for Jev that returns your own enum/sealed types instead of string keys.
  <sub>`SDK` · ★2 · itisnomatter · `Kt`</sub>

- **[n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev)** — n8n community node for TypeSafe Jev structured AI decisions
  <sub>`Project` · ★2 · n3ndor · `TS`</sub>

- **[research_desk](https://github.com/0xnairb/research_desk)** — TypeSafe Jev demonstration for new analyzation — experimenting with Jev for fast analysis of news and tickers
  <sub>`Project` · ★2 · 0xnairb · `Py` · ⚠ `no licence`</sub>

- **[s1_ruby](https://github.com/innocentdiaz/s1_ruby)** — Makes S1-model 'measurement' (and the collapse that follows it) a Ruby primitive.
  <sub>`SDK` · ★2 · innocentdiaz · `Rb`</sub>

- **[skill-router](https://github.com/lomeshdutta/skill-router)** — Tell Claude Code which installed skill a session needs, using Jev (TypeSafe AI) for the decision and skills.sh for discovery.
  <sub>`Plugin` · ★2 · lomeshdutta · `Py`</sub>

- **[tempo-jev-demo](https://github.com/mychaelangelo/tempo-jev-demo)** — A natural-language task workspace comparing performance across AI models (TypeSafe's Jev, GPT-5.6 Luna, and Gemini 3.8 Flash)
  <sub>`Project` · ★2 · mychaelangelo · `TS`</sub>

- **[typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground)** — A playground for experiments around Jev, TypeSafe's System One model.
  <sub>`Project` · ★2 · markjaquith · `Rs`</sub>

- **[typesafe-go](https://github.com/zhirschtritt/typesafe-go)** — Idiomatic Go SDK for the TypeSafe AI API
  <sub>`SDK` · ★2 · zhirschtritt · `Go`</sub>

- **[typesafe-jev-examples](https://github.com/rajivkuriakose/typesafe-jev-examples)** — Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter
  <sub>`Project` · ★2 · rajivkuriakose · `Py`</sub>

- **[typesafe-jev-mcp](https://github.com/anasbekheit/typesafe-jev-mcp)** — MCP server exposing TypeSafe's Jev model as a typed evaluate tool.
  <sub>`Plugin` · ★2 · anasbekheit · `Rs`</sub>

- **[typesafe-sdk](https://github.com/typesafe-sdk-csharp/typesafe-sdk)** — An unofficial .NET SDK for TypeSafe AI, published on NuGet, with deterministic question building and high-throughput verification.
  <sub>`SDK` · ★2 · typesafe-sdk-csharp · `C#`</sub>

- **[typesafeai.net](https://github.com/Hawxy/TypeSafeAI.Net)** — .NET SDK for the TypeSafe AI platform
  <sub>`SDK` · ★2 · hawxy · `C#`</sub>

- **[wellposed](https://github.com/suraj-phanindra/wellposed)** — Lint your jev requests before they come back confidently wrong.
  <sub>`Project` · ★2 · suraj-phanindra · `JS`</sub>

- **[your-signal](https://github.com/MithrilMan/your-signal)** — Open-source BYOK Chrome extension for personal, reversible X timeline filters.
  <sub>`Plugin` · ★2 · mithrilman · `JS`</sub>

- **[antigravity-mcp-semantic-search-with-typesafeai](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)** — Fast semantic code search & diff sanity auditor for AI coding assistants (Antigravity, Cursor, Claude Code) powered by TypeSafe System One.
  <sub>`Benchmark` · ★1 · greenyamao · `Py` · ⚠ `no licence`</sub>

- **[askjev](https://github.com/pZacca/askjev)** — Unofficial MCP server for Jev (Typesafe AI)
  <sub>`Plugin` · ★1 · pzacca · `TS`</sub>

- **[audio-jevlike](https://github.com/alperiox/audio-jevlike)** — Prosodia: an audio-native Jev-shaped decision model — typed calibrated decisions from speech, no ASR
  <sub>`Jev-like alternative` · ★1 · alperiox · `Py` · ⚠ `not Jev itself` `no licence`</sub>

- **[can-jev-bayes](https://github.com/TomRichner/can-jev-bayes)** — Jev Bayes, No? Testing TypeSafe AI's Jev against Bayesian-optimal strategies, and testing if Jev can effectivly use Bayesian priors.
  <sub>`Benchmark` · ★1 · tomrichner · `Py`</sub>

- **[codex-jev-preflight](https://github.com/wellkilo/codex-jev-preflight)** — Fail-open Codex UserPromptSubmit hook that injects TypeSafe Jev pre-task routing metadata.
  <sub>`Plugin` · ★1 · wellkilo · `Py`</sub>

- **[commentcop](https://github.com/ntedvs/commentcop)** — Put your code comments on trial. Powered by Jev.
  <sub>`Project` · ★1 · ntedvs · `TS`</sub>

- **[decido](https://github.com/yairshy/decido)** — Probabilistic decisions for Python. Use Jev or bring your own provider; crawl with Playwright.
  <sub>`Integration` · ★1 · yairshy · `Py`</sub>

- **[decision-bench](https://github.com/Hanno-Labs/decision-bench)** — Open benchmark runtime for document-grounded decision models
  <sub>`Benchmark` · ★1 · hanno-labs · `Py`</sub>

- **[decision-circuits](https://github.com/Barneyjm/decision-circuits)** — Decision circuits: typed questions to a System One model, calibrated probabilities back, gates in code. Zero-dependency Python SDK with LangChain, OpenAI Agents, and Claude Agent SDK integrations.
  <sub>`SDK` · ★1 · barneyjm · `Py`</sub>

- **[harden-jev-decides](https://github.com/tylerjharden/harden-jev-decides)** — JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.
  <sub>`Project` · ★1 · tylerjharden · `TS` · ⚠ `no licence`</sub>

- **[hunch-js](https://github.com/steven-shoemaker/hunch-js)** — Jev judgments as TypeScript functions over arrays: classify, score, check, where, extract, pick, rank, verify. LLMs propose, Jev decides.
  <sub>`SDK` · ★1 · steven-shoemaker · `TS`</sub>

- **[jev](https://github.com/anilsenay/jev)** — Unofficial Go client for TypeSafe's System One API and its model, Jev.
  <sub>`SDK` · ★1 · anilsenay · `Go`</sub>

- **[jev](https://github.com/kataras/jev)** — A Go client for the TypeSafe AI's System One API and its model, Jev.
  <sub>`SDK` · ★1 · kataras · `Go`</sub>

- **[jev-demo](https://github.com/sawzhang/jev-demo)** — Jev (TypeSafe System One) 学习与实测：概念文档 + 5 个可运行 demo + 可复现压测。实测 jev-1.13.0：扇出几乎免费，40 问与 1 问等延迟。
  <sub>`Project` · ★1 · sawzhang · `TS` · ⚠ `no licence`</sub>

- **[jev-demo](https://github.com/PenglongHuang/jev-demo)** — A zero-dependency web bench for TypeSafe Jev with three presets — browser actions, intent recognition and agent context pruning: send state and typed questions, get calibrated structured answers.
  <sub>`Project` · ★1 · penglonghuang · `JS`</sub>

- **[jev-eyes](https://github.com/LeddoEngano/jev-eyes)** — Give Jev eyes — honest, local image perception for TypeSafe's text-only System One model. OCR + spatial layout → Jev state. CLI, MCP server, agent skill.
  <sub>`Plugin` · ★1 · leddoengano · `Py`</sub>

- **[jev-go](https://github.com/guillemus/jev-go)** — Unofficial Go SDK for TypeSafe AI's Jev API
  <sub>`SDK` · ★1 · guillemus · `Go` · ⚠ `no licence`</sub>

- **[jev-go-sdk](https://github.com/ajayk/jev-go-sdk)** — Dependency-free Go client for TypeSafe AI's System One API and the Jev model
  <sub>`SDK` · ★1 · ajayk · `Go`</sub>

- **[jev-lab](https://github.com/llt22/jev-lab)** — Hands-on research lab for TypeSafe's Jev (System One model): reproducible benchmarks of Noul/Choice/Score primitives, confidence gating, fan-out latency, agent control — plus a living audit of the Jev ecosystem.
  <sub>`Benchmark` · ★1 · llt22 · `Py` · ⚠ `no licence`</sub>

- **[jev-lab](https://github.com/danielhirt/jev-lab)** — Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison
  <sub>`Benchmark` · ★1 · danielhirt · `TS` · ⚠ `no licence`</sub>

- **[jev-playground](https://github.com/wustep/jev-playground)** — Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.
  <sub>`Project` · ★1 · wustep · `TS` · ⚠ `no licence`</sub>

- **[jev-playground](https://github.com/Little-Planet-Labs/jev-playground)** — A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)
  <sub>`Project` · ★1 · little-planet-labs · `TS` · ⚠ `no licence`</sub>

- **[jev-practice-speed](https://github.com/tubone24/jev-practice-speed)** — A WebGL demo where you play the card game Speed against a CPU whose brain is TypeSafe AI's Jev. The whole point of the app is to measure and show Jev's decision speed and decision accuracy in real time.
  <sub>`Project` · ★1 · tubone24 · `JS` · ⚠ `no licence`</sub>

- **[jev-research](https://github.com/sherajdev/jev-research)** — Practical guide to using TypeSafe Jev with Herdr and Claude, Codex, Hermes, and browser agents.
  <sub>`Tutorial` · ★1 · sherajdev · `TS`</sub>

- **[jev-sim](https://github.com/dashbi1/jev-sim)** — Jev-compatible /v1/systemone server reading typed decisions from LLM logits, benchmarked against TypeSafe's Jev on the same items via JevBench
  <sub>`Benchmark` · ★1 · dashbi1 · `Py`</sub>

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)** — Claude Code plugin: asks TypeSafe Jev which installed skill fits each prompt and logs the answer (shadow-first). A working reference for the skill-suggestion cookbook on Claude Code — the README records why it is unlikely to help a strong model as a router.
  <sub>`Plugin` · ★1 · shimo4228 · `Py`</sub>

- **[jev-skills](https://github.com/WanLanglin/jev-skills)** — Claude Code & Codex skills powered by Jev, TypeSafe's System One model. 256 calibrated judgements for $0.0005 in 0.72s — 360x cheaper than Claude Opus 5. Includes the first published Jev calibration curve, measured on 4,995 real agent decisions.
  <sub>`Plugin` · ★1 · wanlanglin · `Py` · ⚠ `no licence`</sub>

- **[jev-skills](https://github.com/laguagu/jev-skills)** — Practical agent skills and examples for building with Jev. API setup, routing, ranking, and evidence checks.
  <sub>`Plugin` · ★1 · laguagu · `JS`</sub>

- **[jev-snake](https://github.com/iammusham/jev-snake)** — An experimental Snake environment where the game engine owns deterministic rules and TypeSafe AI's Jev makes the movement decision from structured state on every tick.
  <sub>`Project` · ★1 · iammusham · `Py` · ⚠ `no licence`</sub>

- **[jev-symfony-bundle](https://github.com/vbcherepanov/jev-symfony-bundle)** — Unofficial Symfony bundle for TypeSafe AI's Jev: typed client, validator constraints, Messenger, Workflow guards and profiler panel
  <sub>`SDK` · ★1 · vbcherepanov · `PHP`</sub>

- **[jev2048](https://github.com/KyleKreuter/jev2048)** — Let Jev (TypeSafeAI) solve 2048
  <sub>`Project` · ★1 · kylekreuter · `TS` · ⚠ `no licence`</sub>

- **[jevals](https://github.com/dayhaysoos/jevals)** — Local evaluation workbench for TypeSafe Jev
  <sub>`Project` · ★1 · dayhaysoos · `TS`</sub>

- **[jevcode](https://github.com/miounet11/jevcode)** — JevCode: technical solutions and best practices for Jev (TypeSafe System One), with a companion website.
  <sub>`Project` · ★1 · miounet11 · `TS` · ⚠ `no licence`</sub>

- **[Jevometry](https://github.com/Kunyanli230/Jevometry)** — an Information-Geometric Analysis Toolkit for any System-one (Jev, Jevlike) agent systems
  <sub>`Project` · ★1 · kunyanli230 · `Py`</sub>

- **[jevsbistro](https://github.com/andrewsilber/JevsBistro)** — 3D restaurant service simulator for benchmarking low-latency decision models
  <sub>`Benchmark` · ★1 · andrewsilber · `TS`</sub>

- **[JevTape](https://github.com/Hugo-DDT/JevTape)** — A record-and-replay tool for Jev decisions: a CLI, a local proxy and JSON tapes, with replay fully offline.
  <sub>`Project` · ★1 · hugo-ddt · `Java`</sub>

- **[openpoke-meets-jev](https://github.com/0xShin0221/openpoke-meets-jev)** — Open source implementation of Poke
  <sub>`Project` · ★1 · 0xshin0221 · `Py`</sub>

- **[r2r-jev](https://github.com/Thneoly/r2r-jev)** — Persistent governance for AI agents — turn Jev judgments into replayable relation state with R2R.
  <sub>`Project` · ★1 · thneoly · `Rs`</sub>

- **[risc-jev](https://github.com/i2cjak/RISC-jeV)** — I tortured Jev into being a RISC-V CPU.
  <sub>`Project` · ★1 · i2cjak · `Py` · ⚠ `no licence`</sub>

- **[second-thought](https://github.com/KNambiarDJsc/second-thought)** — Learning infrastructure for typed probabilistic decisions from System One models (Laya, and typed-decision providers you bring yourself).
  <sub>`Project` · ★1 · knambiardjsc · `Py`</sub>

- **[typesafe](https://github.com/mattneel/typesafe)** — An idiomatic Elixir client for the TypeSafe AI API
  <sub>`SDK` · ★1 · mattneel · `Ex`</sub>

- **[typesafe-client](https://github.com/JedimEmO/typesafe-client)** — Unofficial typed async Rust client for the TypeSafe System One API
  <sub>`SDK` · ★1 · jedimemo · `Rs`</sub>

- **[typesafe-go](https://github.com/cole-gillespie/typesafe-go)** — unofficial go SDK for typesafe AI, with typed answers, retries, and context support
  <sub>`SDK` · ★1 · cole-gillespie · `Go`</sub>

- **[typesafe-jev-tools](https://github.com/wotai-dev/typesafe-jev-tools)** — A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5.
  <sub>`Plugin` · ★1 · wotai-dev · `TS`</sub>

- **[typesafe-rs](https://github.com/AbdelStark/typesafe-rs)** — Latency-first Rust SDK for TypeSafe System One.
  <sub>`SDK` · ★1 · abdelstark · `Rs`</sub>

- **[typesafe-sdk](https://github.com/binnash/typesafe-sdk)** — PHP & Laravel SDK for TypeSafe AI's JEV Model series
  <sub>`SDK` · ★1 · binnash · `PHP` · ⚠ `no licence`</sub>

- **[typesafe-sdk-go](https://github.com/SergeAx/typesafe-sdk-go)** — TypeSafe.AI Go SDK
  <sub>`SDK` · ★1 · sergeax · `Go`</sub>

- **[typesafe-sdk-go](https://github.com/dwisiswant0/typesafe-sdk-go)** — Go SDK for TypeSafe AI.
  <sub>`SDK` · ★1 · dwisiswant0 · `Go`</sub>

- **[typesafe-sdk-ruby](https://github.com/afurm/typesafe-sdk-ruby)** — Unofficial Ruby SDK for the TypeSafe AI API (Jev model) - typed questions, retries, and typed errors. Community port of typesafe-sdk-js.
  <sub>`SDK` · ★1 · afurm · `Rb`</sub>

- **[typesafe-sdk-swift](https://github.com/marandaneto/typesafe-sdk-swift)** — typesafe-sdk-js and typesafe-sdk-python port for swift
  <sub>`SDK` · ★1 · marandaneto · `Swift`</sub>

- **[typesafe_sdk_ex](https://github.com/vinnie357/typesafe_sdk_ex)** — Typesafe AI SDK in Elixir using Req
  <sub>`SDK` · ★1 · vinnie357 · `Ex`</sub>

- **[typesafeai-cli](https://github.com/maddygoround/typesafeai-cli)** — Give your AI agent a CLI companion who has access to TypeSafe AI's Jev.
  <sub>`Project` · ★1 · maddygoround · `Py`</sub>

- **[typesafeai-go](https://github.com/chez-shanpu/typesafeai-go)** — Go SDK for TypeSafe AI API https://docs.typesafe.ai/api
  <sub>`SDK` · ★1 · chez-shanpu · `Go`</sub>

- **[what-is-jev](https://github.com/g0runmezadam/what-is-jev)** — Independent, source-linked research on TypeSafe AI's Jev (System One), with 947 rubric-scored public repositories, recurring patterns, datasets, and bilingual documentation.
  <sub>`Benchmark` · ★1 · g0runmezadam · `Py`</sub>

- **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)** — The AI SDK provider package for calling TypeSafe directly, with a sample covering all three question types and nested criteria shapes.
  <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)** — A personal Rust AI gateway with a TypeSafe provider, usage extraction and alias resolution tested against real response bodies.
  <sub>`Project` · ★0 · dvjn · `Rs` · ⚠ `code untested` `no licence`</sub>

- **[AskJev-MCP](https://github.com/cbruyndoncx/AskJev-MCP)** — MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence
  <sub>`Plugin` · ★0 · cbruyndoncx · `JS` · ⚠ `no licence`</sub>

- **[beatjev](https://github.com/lambertsj/beatjev)** — try to beat jev
  <sub>`Project` · ★0 · lambertsj · `JS` · ⚠ `no licence`</sub>

- **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)** — Despite the title, this does not run Jev. It builds a Jev-like decision engine from an open LLM using constrained next-token scoring.
  <sub>`Jev-like alternative` · DataScience Nexus · `Py` · ⚠ `not Jev itself` `code untested` `paywall`</sub>

- **[cartshield](https://github.com/ndolinschi/cartshield)** — CartShield — SMB checkout fraud disposition via TypeSafe Jev
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[cyber-breach-jev](https://github.com/rchovatiya88/cyber-breach-jev)** — Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model
  <sub>`Project` · ★0 · rchovatiya88 · `JS` · ⚠ `no licence`</sub>

- **[dgp](https://github.com/numerous-com/dgp)** — Decision Graph Protocol (DGP) by Numerous ApS: open-source contracts for decision-based AI agents, TypeSafe Jev orchestration, guarded actions, and assessment batching.
  <sub>`Project` · ★0 · numerous-com · `Py`</sub>

- **[extremely-specific-council](https://github.com/cbetz/extremely-specific-council)** — Twelve members. Zero qualifications. A playful TypeSafe AI council with animated votes, inspectable decisions, and shareable verdicts.
  <sub>`Project` · ★0 · cbetz · `TS`</sub>

- **[financialpredictionjev](https://github.com/thodoh1/FinancialPredictionJev)** — Using Jev to test how well it predicts financial markets(just like most llms as of september 2026, it doesnt do that good)
  <sub>`Project` · ★0 · thodoh1 · `Py` · ⚠ `no licence`</sub>

- **[frost](https://github.com/marcus/frost)** — A flexible and configurable CLI model router using TypeSafe Jev.
  <sub>`Project` · ★0 · marcus · `Go`</sub>

- **[functions](https://github.com/TrainLCD/Functions)** — 👷 Cloudflare Workers for the TrainLCD mobile app.
  <sub>`Project` · ★0 · trainlcd · `TS` · ⚠ `no licence`</sub>

- **[hiresignal](https://github.com/ndolinschi/hiresignal)** — HireSignal — resume first-pass fit+interview via TypeSafe Jev
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)** — A third-party explainer with a useful architecture sketch and an unusually honest list of cases where you should not use a decision model.
  <sub>`Article` · `Py` · ⚠ `code untested`</sub>

- **[jev-acento](https://github.com/marcosmartinez/jev-acento)** — ¿Jev entiende tu acento? Pre-registered audit of TypeSafe AI's Jev on Spanish — accuracy, calibration and token cost — plus a CLI to run the same comparison on your own labelled data.
  <sub>`Benchmark` · ★0 · marcosmartinez · `Py`</sub>

- **[jev-acp](https://github.com/formulahendry/jev-acp)** — Use Jev typed decisions from any ACP (Agent Client Protocol) client or IDE
  <sub>`Project` · ★0 · formulahendry · `TS`</sub>

- **[jev-anotacao-sentencas](https://github.com/lab-dados/jev-anotacao-sentencas)** — Jev (TypeSafe) vs. Gemini 3.8 Flash vs. GPT-5.6 Luna na anotação estruturada de sentenças do TJSP: qualidade, tempo e custo
  <sub>`Project` · ★0 · lab-dados · `Py` · ⚠ `no licence`</sub>

- **[jev-bun1](https://github.com/heiwa4126/jev-bun1)** — TypeSafe の Jev を TypeScript SDK で使ってみる最初の 1 歩
  <sub>`SDK` · ★0 · heiwa4126 · `TS` · ⚠ `no licence`</sub>

- **[jev-calculator](https://github.com/pc418/jev-calculator)** — A probabilistic AI calculator powered by Jev.
  <sub>`Project` · ★0 · pc418 · `TS`</sub>

- **[jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)** — Does TypeSafe's Jev keep its accuracy and calibration on Russian? Independent RU vs EN audit (ECE, reliability diagrams, paired bootstrap) on parallel human-labelled data.
  <sub>`Benchmark` · ★0 · ahtoooxa · `Py`</sub>

- **[jev-evaluation](https://github.com/willkelly/jev-evaluation)** — An adversarial evaluation of TypeSafe's jev decision model: nine experiments and 28 predictions fixed before any data was collected. 123,805 requests, $12.69.
  <sub>`Project` · ★0 · willkelly · `Py`</sub>

- **[jev-games](https://github.com/shantanugoel/jev-games)** — Visual Jev lab for multiple games and emulator platforms
  <sub>`Project` · ★0 · shantanugoel · `Py` · ⚠ `no licence`</sub>

- **[jev-jp-address](https://github.com/smasato/jev-jp-address)** — Jev (TypeSafe) 性能評価プロジェクト — 日本郵便 KEN_ALL をマスタに、AI SDK 経由の Jev が住所のあいまい一致にどこまで使えるかを検証
  <sub>`SDK` · ★0 · smasato · `TS` · ⚠ `no licence`</sub>

- **[jev-lab](https://github.com/Menny1337/jev-lab)** — TypeScript experiments, evaluations, and latency benchmarks for TypeSafe's Jev model
  <sub>`Benchmark` · ★0 · menny1337 · `TS` · ⚠ `no licence`</sub>

- **[jev-measured](https://github.com/WallerChen/jev-measured)** — Measured cost, latency and raw output from the live Jev API (TypeSafe AI System One model) across 8 use cases — reproducible
  <sub>`Project` · ★0 · wallerchen · `Py`</sub>

- **[jev-no-enem](https://github.com/patryckalves/jev-no-enem)** — Reproducible benchmark evaluating TypeSafe AI's Jev (System One paradigm) on Brazil's ENEM 2025 standardized exam. Evaluates typed decision-making, domain-specific accuracy, and RLCD uncertainty calibration against open LLM baselines with an interactive GitHub Pages dashboard.
  <sub>`Benchmark` · ★0 · patryckalves · `Py` · ⚠ `no licence`</sub>

- **[jev-pick-and-place-study](https://github.com/tryaksh/jev-pick-and-place-study)** — A small reproducible MuJoCo pilot comparing Jev, Claude Haiku, and reactive rules for pick-and-place.
  <sub>`Project` · ★0 · tryaksh · `Py` · ⚠ `no licence`</sub>

- **[jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner)** — Chrome dino game played by Typesafe AI Jev model
  <sub>`Project` · ★0 · joshlarsen · `JS`</sub>

- **[jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales)** — Winner-stays-on animal tournament refereed by Jev (TypeSafe System One): a local game to feel how fast typed decisions are. UI in Spanish.
  <sub>`Project` · ★0 · hectorlcastro09 · `TS`</sub>

- **[jevai.org community site](https://www.jevai.org/)** — An unaffiliated community site with a playground, a preset decision API, an MCP server, downloadable skills and a gallery of community apps.
  <sub>`Project` · `sh` · ⚠ `3rd-party key` `unverified claims`</sub>

- **[jevscope](https://github.com/jeiel85/jevscope)** — Local-first visual decision debugger and regression testbench for TypeSafe AI Jev
  <sub>`Project` · ★0 · jeiel85 · `TS`</sub>

- **[kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev)** — Rust client for the TypeSafe System One API (Jev)
  <sub>`SDK` · ★0 · kunobi-ninja · `Rs`</sub>

- **[labs](https://github.com/kiarina/labs)** — Small, independent projects for experiments, research, and investigations.
  <sub>`Project` · ★0 · kiarina · `Py`</sub>

- **[magic-jev-ball](https://github.com/mikecann/magic-jev-ball)** — A Magic 8 Ball that asks Jev instead of picking at random. Convex + AI Gateway + three.js.
  <sub>`Project` · ★0 · mikecann · `TS`</sub>

- **[mcpmatch](https://github.com/ndolinschi/mcpmatch)** — Match user goals to MCP catalog (two-stage) via TypeSafe Jev
  <sub>`Plugin` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[mimicry](https://github.com/jxucoder/mimicry)** — Rewrite AI drafts in your own voice with a bounded TypeSafe feedback loop.
  <sub>`Project` · ★0 · jxucoder · `Py` · ⚠ `no licence`</sub>

- **[n8n-nodes-typesafe](https://github.com/Biztactix/n8n-nodes-typesafe)** — Typesafe AI Node for N8N
  <sub>`Plugin` · ★0 · biztactix · `TS`</sub>

- **[open-jev-bridge](https://github.com/louis-szeto/open-jev-bridge)** — MCP plugin to connect jev-like system one API (local hosted or typesafe jev) to codex and claude code for decision tasks like compaction, verification judgement, etc.
  <sub>`Plugin` · ★0 · louis-szeto · `JS`</sub>

- **[pi-agent-foreman](https://github.com/alexshpunt/pi-agent-foreman)** — Send Pi agents back to work when they stop before the job is done.
  <sub>`Project` · ★0 · alexshpunt · `TS`</sub>

- **[pi-typesafe](https://github.com/twilwa/pi-typesafe)** — Pi coding-agent extension built on the TypeSafe AI System One API (Jev)
  <sub>`Plugin` · ★0 · twilwa · `TS` · ⚠ `no licence`</sub>

- **[pong-jev](https://github.com/safzanpirani/pong-jev)** — TypeSafe's Jev plays Atari Pong. One typed Choice question per frame, no coordinates sent to the model.
  <sub>`Project` · ★0 · safzanpirani · `TS` · ⚠ `no licence`</sub>

- **[river-run-typesafe](https://github.com/ashaazami/river-run-typesafe)** — River shooter game in Python, inspired by Atari's River Raid, played by a TypeSafe AI pilot
  <sub>`Project` · ★0 · ashaazami · `Py`</sub>

- **[scam-shield](https://github.com/ShupingR/scam-shield)** — Scam text message filter powered by TypeSafe's Jev model
  <sub>`Project` · ★0 · shupingr · `TS` · ⚠ `no licence`</sub>

- **[search-function-test](https://github.com/Shifros/Search-Function-Test)** — A test project based on Jev AI, the goal is to build a search function for a blog/article website that has 100s of articles to search from, So the user can actually use the search as chat to question anything and find related answers/articles
  <sub>`Project` · ★0 · shifros · `JS` · ⚠ `no licence`</sub>

- **[system-one-adapter-rust](https://github.com/codeitlikemiley/system-one-adapter-rust)** — Rust port of TypeSafe system-one-adapter (LLM-backed system_one evaluations)
  <sub>`Integration` · ★0 · codeitlikemiley · `Rs`</sub>

- **[tinyjevclient](https://github.com/tinyhumansai/tinyjevclient)** — An integration with jev by typesafe.ai in Rust
  <sub>`Integration` · ★0 · tinyhumansai · `Rs`</sub>

- **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)** — The only platform with dedicated Jev observability: an OpenInference instrumentor that traces every decision call over OpenTelemetry.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul`</sub>

- **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)** — Vercel's launch note for Jev on AI Gateway, with an experimental_evaluate sample using the model string typesafe-ai/jev.
  <sub>`Integration` · `TS` · `noul`</sub>

- **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)** — First-party Pydantic AI support: an Agent with output_type=bool over the typesafe:jev-latest model string.
  <sub>`Integration` · `Py`</sub>

- **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)** — Proxy Jev through LiteLLM for unified keys and cost tracking, with any path under /typesafe/ passed straight through.
  <sub>`Integration` · `sh`</sub>

- **[typesafe-ai-ruby](https://github.com/hnegishi/typesafe-ai-ruby)** — Ruby client for the TypeSafe AI(Jev) System One API
  <sub>`SDK` · ★0 · hnegishi · `Rb`</sub>

- **[typesafe-chess](https://github.com/TholeG/typesafe-chess)** — Chess where both players are TypeSafe's Jev model: every move is a typed Choice decision
  <sub>`Project` · ★0 · tholeg · `JS`</sub>

- **[typesafe-comment](https://github.com/Hexdigest123/typesafe-comment)** — Small Python package that uses typesafe.ai to evaluate code comments on certain heuristics
  <sub>`Project` · ★0 · hexdigest123 · `Py`</sub>

- **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)** — Point the official TypeSafe SDK at Vercel by changing one baseURL, or call the gateway's systemone endpoint directly with cURL.
  <sub>`Integration` · `TS` · `sh` · `noul`</sub>

- **[typesafe-go](https://github.com/Nibir1/typesafe-go)** — A zero-dependency community Go SDK, including a static analyser that flags poorly designed questions at compile time.
  <sub>`SDK` · ★0 · Nibir1 · `Go` · `choice` · `score` · `noul` · ⚠ `code untested`</sub>

- **[typesafe-go](https://github.com/Shubham510/typesafe-go)** — Unofficial Go SDK for TypeSafe AI's System One API (Jev).
  <sub>`SDK` · ★0 · shubham510 · `Go`</sub>

- **[typesafe-sdk-go](https://github.com/valksor/typesafe-sdk-go)** — Unofficial Go SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI.
  <sub>`SDK` · ★0 · valksor · `Go`</sub>

- **[typesafe-sdk-kotlin](https://github.com/ufec/typesafe-sdk-kotlin)** — A Kotlin SDK for TypeSafe AI, ported from the official JavaScript SDK with its deviations documented; ask typed questions about text and get typed answers back.
  <sub>`SDK` · ★0 · ufec · `Kt`</sub>

- **[typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php)** — Unofficial PHP SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI.
  <sub>`SDK` · ★0 · valksor · `PHP`</sub>

- **[typesafe-sdk-php](https://github.com/Fox-Islam/typesafe-sdk-php)** — Unofficial PHP library for the TypeSafe API
  <sub>`SDK` · ★0 · fox-islam · `PHP`</sub>

- **[typesafe_ai](https://github.com/typesend/typesafe_ai)** — Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.
  <sub>`SDK` · ★0 · typesend · `Ex`</sub>

- **[typesafe_ai](https://github.com/hfiguera/typesafe_ai)** — An Elixir client for TypeSafe AI with typed responses and bounded concurrency
  <sub>`SDK` · ★0 · hfiguera · `Ex`</sub>

- **[typesafe_chess_eval](https://github.com/AliceRoselia/Typesafe_chess_eval)** — An evaluation of typesafe AI chess. As it turns out, the AI isn't doing really well even though chess is not a particularly open-ended game. Still, it's only a prototype and this probably wasn't optimzied for games.
  <sub>`Project` · ★0 · aliceroselia · `Py`</sub>

- **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)** — Currently the most-starred sibling directory in this space.
  <sub>`Project` · ★1,530 · ⚠ `no licence`</sub>

- **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)** — The only launch coverage with first-hand developer quotes rather than vendor figures, including a caution that interpreting the thresholds is now your job.
  <sub>`Article` · Tim Fernholz</sub>

- **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)** — Focuses on the missing explainability — the model returns no reasoning in language — and on every published benchmark coming from the vendor.
  <sub>`Article` · Tomislav Bezmalinović</sub>

- **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)** — The launch thread, and the densest single collection of scepticism: unsupported RLCD claims, apples-to-oranges latency comparisons, and the deliberate absence of public benchmarks.
  <sub>`Discussion`</sub>

- **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))** — Most useful as an index: its reference list is a fast route to the coverage worth reading.
  <sub>`Article`</sub>

- **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)** — An agent-builder's framing of where a decision model sits in an agent stack.
  <sub>`Article` · ⚠ `marketing`</sub>

- **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)** — Mainstream coverage of the launch and the speed with which gateways added support.
  <sub>`Article` · Josipa Majic Predin · ⚠ `vendor numbers` `paywall`</sub>

- **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)** — A review that puts the limitation in the title rather than burying it.
  <sub>`Video` · Gary Explains</sub>

- **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)** — The only long-form founder interview: why RLHF was the wrong optimisation target, why public benchmarks were withheld, and the all-synthetic data approach.
  <sub>`Discussion` · Latent Space</sub>

- **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)** — A neutral survey of the architecture, the claimed benchmarks and the pricing, which states plainly that no large independent reproduction had surfaced.
  <sub>`Article` · Matt Crabtree</sub>

- **[jevai.org community app gallery](https://www.jevai.org/apps)** — Thirty-six community builds curated from social posts: browser agents, spreadsheet tooling, inbox search by intent, ad blocking with judgement, games and robotics.
  <sub>`Project` · ⚠ `unverified claims`</sub>

- **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)** — An independent write-up whose most useful finding is a negative one: there is no paper, no reward function, no dataset description and no reproducible evaluation for RLCD.
  <sub>`Article`</sub>

- **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)** — The most sceptical mainstream piece: it challenges the no-hallucination framing on the grounds that a well-formed answer is not the same as a correct one.
  <sub>`Article` · Thomas Claburn</sub>

- **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)** — OpenRouter's listing for Jev, with its own model ids and the unusual pricing shape of paid input and free output.
  <sub>`Integration`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
