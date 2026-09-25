# Safety gating

<sub>[awesome-jev](../../README.md) · [中文](safety-gating.zh-CN.md)</sub>

_Decide whether an action is safe to run. Defence in depth, never a security boundary._

Every catalogued example of this decision — 139 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#safety-gating); [the site](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=en) can filter them further by language, primitive and kind.

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction.
  <sub>`Project` · ★42,557 · `Go` · `noul`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★31,582 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.
  <sub>`Integration` · ★18,223 · `TS` · `choice` · `score` · `noul`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check.
  <sub>`Project` · ★6,341 · `TS` · `choice` · `noul`</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)** — Three Score questions on a shared severity scale, blocking the request when two or more cross the line, and failing closed.
  <sub>`Project` · ★5,017 · `Rs` · `score`</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, checks, and approval gates instead of hoping it follows your instructions.
  <sub>`Project` · ★820 · bastani-inc · `TS`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation.
  <sub>`Project` · ★591 · `JS` · `choice` · `noul`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.
  <sub>`Project` · ★425 · notque · `Py`</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — An AI coding agent that reads your code, edits files, runs commands, and reasons through bugs — across a terminal REPL, a full-screen TUI, and a browser UI, while you keep your hand on every permission.
  <sub>`Project` · ★335 · wrongstack · `TS`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain, Jev for cheaper steps. Microduck, Open Duck Mini, LeRobot, XLeRobot, AlohaMini, ToddlerBot or any ROS base. Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM. Simulator, .d
  <sub>`Plugin` · ★231 · rokbenko · `Py`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — An easy way to use jev with your coding agent for tool calling reasoning
  <sub>`Project` · ★202 · vinilana · `TS`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code.
  <sub>`Project` · ★164 · `Py` · `choice` · `score` · `noul` · ⚠ `unverified claims`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — A decision layer for a coding agent: a measured tool-call gate plus a typed ask for calibrated answers.
  <sub>`Plugin` · ★142 · y0usaf · `TS`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — Detect youtube sponsor segment with live audio and transcript powered by Jev
  <sub>`Project` · ★95 · trungdq88 · `JS` · ⚠ `no licence`</sub>

- **[bluenoise](https://github.com/rokcso/bluenoise)** — Blur or hide noisy replies, posts & ads on X (Twitter), and clean up its interface with local, reversible keyword/account rules — no X API, no data collection, no account changes. 用本地可逆的关键词/账号规则模糊或隐藏 X（推特）上的嘈杂回复、帖子和广告，并整理界面——不调用 X API、不收集数据、不修改账号。
  <sub>`Project` · ★90 · rokcso · `TS`</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)** — Connect TypeSafe Jev to Grok Bot as a cheap decision layer - usage gates, skill template, examples
  <sub>`Plugin` · ★77 · bodila51 · `Py`</sub>

- **[jevals](https://github.com/openlayer-ai/jevals)** — Agent evals and guardrails as Jev decisions: one request per trace, a fraction of a cent, fast enough for the agent loop. Runs locally with Kev or Laya.
  <sub>`Project` · ★77 · openlayer-ai · `Py`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★44 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-guard](https://github.com/klauswg/jev-guard)** — Real-time risk triage gateway for exchange deposits and withdrawals — Jev (TypeSafe System One) handles triage only; adjudication stays in deterministic code.
  <sub>`Project` · ★35 · klauswg · `Java`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP.
  <sub>`Plugin` · ★30 · leepokai · `JS`</sub>

- **[is-malicious](https://github.com/luantak/is-malicious)** — A codebase scanner that helps you not run malicous code
  <sub>`Project` · ★23 · luantak · `TS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.
  <sub>`Project` · ★21 · jcpsimmons · `JS`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★20 · keeltrace · `Py`</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails open on everything else
  <sub>`Plugin` · ★18 · valentynkit · `JS`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.
  <sub>`Benchmark` · ★17 · abdelstark · `Py`</sub>

- **[muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook)** — Jev decision layer for Muse: a fast, cheap TypeSafe AI gate before expensive agent work — confidence policy, recipes, reference router, honest measurement.
  <sub>`Plugin` · ★16 · bodila51 · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action, pi package, and more. Built with Effect.
  <sub>`Project` · ★14 · tyler-dot-earth · `TS`</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway
  <sub>`Project` · ★13 · mejiasd3v · `JS`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.
  <sub>`Project` · ★12 · antoniocoppe · `TS`</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 可疑行为 \| Review Agent Skills and MCP code with Jev, static evidence, and explicit coverage gaps
  <sub>`Plugin` · ★10 · win4r · `Py`</sub>

- **[pi-verdict](https://github.com/jesset/pi-verdict)** — A minimal permission gate for Pi in the style of Claude Code's auto mode
  <sub>`Plugin` · ★10 · jesset · `TS`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★9 · 24601 · `Py`</sub>

- **[flue-jev-demo](https://github.com/matthewp/flue-jev-demo)** — Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway
  <sub>`Project` · ★9 · matthewp · `TS` · ⚠ `no licence`</sub>

- **[jev-sentinel](https://github.com/harshwasan/jev-sentinel)** — Pi coding-agent extension: TypeSafe Jev checks for tool calls, tool outputs and replies (prompt injection, approvals, secret scrubbing, task pinning)
  <sub>`Plugin` · ★9 · harshwasan · `TS`</sub>

- **[jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot)** — Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev
  <sub>`Project` · ★9 · backmeupplz · `TS`</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — PR Risk review, automated by Jev
  <sub>`Project` · ★9 · hexyedev · `Py`</sub>

- **[AskJev](https://github.com/ranjan2829/AskJev)** — AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)
  <sub>`Project` · ★8 · ranjan2829 · `TS`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — DiffJury — TypeSafe Jev PR risk router + code review coach
  <sub>`Project` · ★7 · raihankhan-rk · `TS` · ⚠ `no licence`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world.
  <sub>`Project` · ★7 · abdelstark · `TS`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows
  <sub>`Benchmark` · ★7 · jmanhype · `Py`</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — Probability-scored guardrails for Claude Code: deny rule-breaking edits and unasked-for deploys, route your docs into each prompt, and check the final answer against the turn's own evidence.
  <sub>`Plugin` · ★7 · muratcakmak · `TS`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill
  <sub>`Plugin` · ★6 · docxology · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through.
  <sub>`Project` · ★6 · ufec · `Kt`</sub>

- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)** — Zero-dependency System One decision harness: 5 semantic gates saving frontier AI agent tokens on trivial errors & doom loops. Python + TypeScript + Rust. MCP-compatible.
  <sub>`Plugin` · ★6 · ismaelsoilet · `Py`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · ★6 · scienthoon · `Py`</sub>

- **[jevc](https://github.com/doronp/jevc)** — Compile agent policy prose into deterministic verdict programs: narrow evidence questions for the model, the verdict computed in code. Install: npm i -g jev-compiler
  <sub>`Project` · ★6 · doronp · `TS`</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gate completion claims inside DeepSeek Harness.
  <sub>`Plugin` · ★5 · horusjiang · `TS`</sub>

- **[jev-agent-authorization](https://github.com/kinde-starter-kits/jev-agent-authorization)** — Jev agent authorization for MCP tool calls: Kinde identity and permissions plus Jev's typed, calibrated decisions, checked server-side before every call runs
  <sub>`Plugin` · ★5 · kinde-starter-kits · `TS`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session.
  <sub>`Plugin` · ★5 · shivampansuriya · `JS`</sub>

- **[jev-tool-permissions](https://github.com/NicolasMontone/jev-tool-permissions)** — Jev-backed tool approval gate and tool-list pruning for the Vercel AI SDK
  <sub>`SDK` · ★5 · nicolasmontone · `TS` · ⚠ `no licence`</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic
  <sub>`Project` · ★5 · kenhuangus · `Py`</sub>

- **[jit-context](https://github.com/wojciechwiesner/jit-context)** — Architectural Moat: JIT-JEV Context OS — Epistemic runtime & JEV System 1 context gate for AI agents (L0 SQLite WAL <3ms, Epistemic Invariants I1–I10, CERN Zenodo DOI: 10.5281/zenodo.22649542)
  <sub>`Project` · ★5 · wojciechwiesner · `Py`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — AGI JEV Detection — local AI agent monitor: chain-level malicious-agent detection (TypeSafe Jev + Sentinel), escalate-only L1–L5 containment, Neo4j forensics, AngryRobot dashboard. HackSpain 2026.
  <sub>`Project` · ★4 · carlosedm10 · `Py` · ⚠ `no licence`</sub>

- **[claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev)** — Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks
  <sub>`Plugin` · ★4 · rahulbalakavi · `Py`</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — An OpenAI-compatible proxy that sits between your LLM and your users. It evaluates each sliding window of tokens while the response is still streaming and cuts the stream before a violating token can reach the screen.
  <sub>`Project` · ★4 · thanh-mathieu95 · `JS`</sub>

- **[jev-shield](https://github.com/vmendes90/jev-shield)** — Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev
  <sub>`Plugin` · ★4 · vmendes90 · `TS`</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — Code-review gate for CI and coding agents: asks TypeSafe Jev small typed questions about functions, files, tests and docs, and reports findings with locations and probabilities
  <sub>`Project` · ★4 · tech-byte-frontier · `Rs`</sub>

- **[macos-computer-use-kit](https://github.com/Sur-Cai/macos-computer-use-kit)** — AX-first computer use for AI agents on macOS with optional Jev (TypeSafe System One) semantic guards: calibrated target/input judgments before an irreversible action, decisions kept in code. Accessibility-tree targeting, window-scoped input, clipboard-safe paste, read-back verification…
  <sub>`Plugin` · ★4 · sur-cai · `Py`</sub>

- **[nachalnik](https://github.com/ljedrz/nachalnik)** — A transparent agent runtime in Rust: context, tools, permissions and requests as explicit state. Plus an MCP bridge and a terminal agent.
  <sub>`Plugin` · ★4 · ljedrz · `Rs`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server: a decision layer for coding agents, built on TypeSafe Jev (System One model). Ship gates, risk checks, file triage that keeps files out of context, and a safe headless browser, with calibrated confidence. For Claude Code, Codex, Cursor.
  <sub>`Plugin` · ★3 · abhishekswe · `TS`</sub>

- **[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)** — Effect-based safety gate for AI coding agents' shell commands (OpenCode, Antigravity): fast structural rules, then TypeSafe's Jev or a chat model judges what a command does. Certified with Jev at zero dangerous commands allowed.
  <sub>`Plugin` · ★3 · godspede · `TS`</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev drives your Ego Lite browser: one typed-choice request per step. Single-file, zero-dependency port of browser-use/jev-ultrafast with multi-model benchmarks and extra guardrails. Unofficial.
  <sub>`Benchmark` · ★3 · shikaizhong-design · `JS`</sub>

- **[jev-gate](https://github.com/MongLong0214/jev-gate)** — Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.
  <sub>`Plugin` · ★3 · monglong0214 · `TS` · ⚠ `no licence`</sub>

- **[jev-guard](https://github.com/ClemensSchartmueller/jev-guard)** — A cross-agent safety gate for Claude Code, Codex CLI and Antigravity: intercepts shell runs, writes and patches, applies fast local boundary checks, then asks Jev about blast radius, reversibility and destructive potential.
  <sub>`Plugin` · ★3 · clemensschartmueller · `Go`</sub>

- **[jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer)** — See what Jev thinks about your SaaS website — powered by ReplyNodes web context and Vercel AI Gateway.
  <sub>`Project` · ★3 · replynodes · `TS`</sub>

- **[mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation)** — Input moderation for Mastra agents on TypeSafe Jev — one file
  <sub>`Project` · ★3 · codealive-ai · `TS`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — Binary approval gate for Codex and Claude Code — every intercepted tool call is reviewed by TypeSafe JEV and composed through a versioned local policy, with scoped authorization.
  <sub>`Jev-like alternative` · ★3 · alexj11324 · `Go` · ⚠ `not Jev itself`</sub>

- **[rh-guard](https://github.com/24601/rh-guard)** — Reward-hack radar for coding agents: structural denies + TypeSafe Jev System One sidecar for Claude Code & Cursor hooks
  <sub>`Plugin` · ★3 · 24601 · `TS`</sub>

- **[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)** — Open-source Jev tool-calling authorization gateway for AI agents: deterministic policy, exact-action single-use permits, MCP and HTTP enforcement.
  <sub>`Plugin` · ★2 · omkarghugarkar007 · `TS`</sub>

- **[claude-jev-plugin](https://github.com/dr-dimitru/claude-jev-plugin)** — TypeSafe Jev semantic guardrails for Claude Code
  <sub>`Plugin` · ★2 · dr-dimitru · `TS`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrated probabilities (noul/choice/score) for routing/triage/guardrail judgments, no text generation. 把 TypeSafe Jev 决策模型注册为 DSH agent 工具
  <sub>`Plugin` · ★2 · nanami-0713 · `JS`</sub>

- **[grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard)** — A typed preflight and approval layer for Grok Bot: local policy owns the hard boundaries, Jev judges the ambiguous cases, and Grok Bot executes within the envelope it gets back.
  <sub>`Project` · ★2 · 0xwhrari · `Py`</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — Issue triage that stays quiet when it isn't sure. Calibrated labels, spam and duplicate detection — with abstention.
  <sub>`Project` · ★2 · emreozyoruk · `JS`</sub>

- **[jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper)** — Low-latency audio censorship POC using Jev typed decisions and ffmpeg.
  <sub>`Project` · ★2 · santos-sanz · `TS` · ⚠ `no licence`</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions)** — Jev Decisions Plugin for Hermes (and other AI Agents): tool risk reviews, human approval recommendations, evidence checks, and a local decision journal.
  <sub>`Plugin` · ★2 · bojansandhaus · `Py`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev
  <sub>`Plugin` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev.
  <sub>`Plugin` · ★2 · vicente-md · `Java` · ⚠ `no licence`</sub>

- **[jev-skillful](https://github.com/bestagentkits/jev-skillful)** — Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.
  <sub>`Plugin` · ★2 · bestagentkits · `TS`</sub>

- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** — Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines
  <sub>`Project` · ★2 · bitnovus · `Py`</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — Sub-100ms security gate for AI agent tool calls, powered by TypeSafe's Jev (System-1) decision model. Single-request Choice/Noul/Score evaluation, dual-factor blocking matrix, calibrated-confidence routing, fail-closed parsing, zero-config local fallback. LangChain-ready.
  <sub>`Project` · ★2 · lgy1027 · `Py`</sub>

- **[opencode-jev-guard](https://github.com/CogFlux/opencode-jev-guard)** — OpenCode 2 plugin that sends every shell command (local or via FarHand) to TypeSafe's Jev and asks you first when it leaves files outside the project, installs software globally, changes global settings, is harmful or exposes private data
  <sub>`Plugin` · ★2 · cogflux · `TS`</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Code hook
  <sub>`Plugin` · ★2 · riskaversetech · `TS`</sub>

- **[toolgate](https://github.com/ndolinschi/toolgate)** — Agent tool/MCP call gate — allow / ask_human / deny via TypeSafe Jev
  <sub>`Plugin` · ★2 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)
  <sub>`Project` · ★2 · opaielsheikh · `TS` · ⚠ `no licence`</sub>

- **[zerosweep](https://github.com/sysadarsh/zerosweep)** — Autonomous System-One Triage Engine & Benchmark powered by TypeSafe AI (Jev). 75ms inference, $0 output tokens, and RLCD epistemic safety gates.
  <sub>`Benchmark` · ★2 · sysadarsh · `TS` · ⚠ `no licence`</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness — Jev-powered risk classification & evidence-gated auto-approval. Fail-closed by construction. dsh 生态第一个 System-1 决策插件
  <sub>`Plugin` · ★1 · asktheway · `TS`</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — A verified browser agent: a cheap Jev guard (evidence-checked completions, a destructive gate) in front of any LLM browser driver, with Jev taking the mechanical steps in dual mode. Built on browser-use; every number pre-registered and measured.
  <sub>`Project` · ★1 · tom-r-main · `Py`</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — A text-moderation demo: one systemOne call screens seven Noul hazards and one severity Score in parallel, and the verdict is computed in code from policy thresholds.
  <sub>`Project` · ★1 · norbertbodziony · `TS` · ⚠ `no licence`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.
  <sub>`Project` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `one commit` `AI-written`</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.
  <sub>`Benchmark` · ★1 · themsquared · `Py`</sub>

- **[jev-carryforward](https://github.com/Dharundp6/jev-carryforward)** — What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway.
  <sub>`Plugin` · ★1 · dharundp6 · `TS`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed.
  <sub>`Project` · ★1 · jyatesdotdev · `Py`</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.
  <sub>`Plugin` · ★1 · krw82 · `TS`</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — A bounded Jev risk check for Claude Code: eight risk axes, one request, one optional reinspection.
  <sub>`Plugin` · ★1 · muse0509 · `Go`</sub>

- **[jev-runtime-security](https://github.com/ringzerosec/jev-runtime-security)** — Runtime security for AI coding agents: policy is enforced in the kernel at the system call, below the agent and anything it writes, with Jev judging the ambiguous cases.
  <sub>`Project` · ★1 · ringzerosec · `Rs`</sub>

- **[jev-screen-mcp](https://github.com/jiawei686/jev-screen-mcp)** — Single-purpose MCP server (one tool, one job): a content-moderation gate powered by TypeSafe Jev (System One decision model).
  <sub>`Plugin` · ★1 · jiawei686 · `TS`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets
  <sub>`Benchmark` · ★1 · teyhouse · `Py` · ⚠ `no licence`</sub>

- **[jev-switchboard](https://github.com/ZIJIAN004/jev-switchboard)** — A JEV-gated semantic communication layer for parallel coding agents.
  <sub>`Project` · ★1 · zijian004 · `JS`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — Jevaluate: evaluate before you trust. Field notes, runnable scripts and an agent skill for TypeSafe Jev: gated evals, a browser loop, a product walk with DeepSeek vision, a UI text judge and a first-click tree test. Co-authored with Claude Fable 5.1.
  <sub>`Plugin` · ★1 · elshinq · `JS`</sub>

- **[jevegis](https://github.com/0xArx/jevegis)** — Guardrails for LLM apps in one API call. Prompt injection, jailbreaks, leaks, unsafe content. Built on TypeSafe Jev. MIT.
  <sub>`Project` · ★1 · 0xarx · `TS`</sub>

- **[JevLang](https://github.com/TimMikeladze/JevLang)** — A policy engine for LLM decisions: declare routes, gates and actions once in TypeScript or Python, and every decision comes validated, explainable, replayable and audited.
  <sub>`SDK` · ★1 · timmikeladze · `JS`</sub>

- **[jevnav](https://github.com/dtduc-git/jevnav)** — Page truth for browser agents — and decisions that replay, test and audit. Jev picks the element, risky actions are gated, every run replays offline in CI.
  <sub>`Project` · ★1 · dtduc-git · `Py`</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — A Jev (TypeSafe System One) permission gate for the Pi coding agent: judges every bash / write / edit call before it runs
  <sub>`Project` · ★1 · kurihada · `TS`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — Every tool call your agent makes, checked before it runs. A Claude Code plugin that uses TypeSafe AI's Jev to verify each pending tool call against the session plan, then allows it, asks you, or blocks it. Proof of concept
  <sub>`Plugin` · ★1 · getexcited · `TS`</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — A local decision layer in Jev's shape: yes/no, choice and rubric questions read off one token's logprobs from a local model, with a Claude Code permission gate measured on held-out command sets.
  <sub>`Jev-like alternative` · ★1 · Xinyu Liu · `TS` · `noul` · `choice` · `score` · ⚠ `not Jev itself` `AI-written`</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — Reusable GitHub Action: agent fix loop gated by checks, an AI reviewer, and TypeSafe Jev
  <sub>`Project` · ★0 · ripwords · `TS` · ⚠ `no licence`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — An experimental protocol for evidence-aware agent handoffs, bounded worker continuation, and TypeSafe/Jev-assisted review, with reproducible evaluation.
  <sub>`Benchmark` · ★0 · zsoxi · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full.
  <sub>`Project` · ★0 · jourdanlabs · `Py` · ⚠ `no licence`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run.
  <sub>`Article` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `vendor numbers`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — A CLI and GitHub Action that assesses code-change risk using deterministic rules and TypeSafe Jev, recommending checks and reviewers before merge.
  <sub>`Project` · ★0 · moezubair · `TS`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — This repository contains a GitHub issue classifier built on Jev, TypeSafe AI's System One model. It labels every new issue with typed values and calibrated confidence in milliseconds, labelling what it is sure about and escalating what it is not. Three guardrail layers guard every write, and a
  <sub>`Project` · ★0 · kalyanm45 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-dev](https://github.com/n-yokomachi/jev-dev)** — 同じ発言を jev と LLM の両方に判定させ、感情の変動値のズレと応答速度を1画面で見比べるデモ（affectus + Vercel AI Gateway）
  <sub>`Project` · ★0 · n-yokomachi · `TS` · ⚠ `no licence`</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves.
  <sub>`Plugin` · ★0 · rashedint32 · `JS`</sub>

- **[jev-guard](https://github.com/CMaintz/jev-guard)** — Vets an LLM agent's tool calls through TypeSafe AI's Jev before they run — allow, block, or hold, failing safe on uncertainty.
  <sub>`Project` · ★0 · cmaintz · `TS`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev-compatible decision endpoints
  <sub>`Project` · ★0 · dtduc-git · `Py`</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you own. Discord/Telegram/Reddit bots, CLI, Python, npm, HTTP API, MCP.
  <sub>`Plugin` · ★0 · ohernandezdev · `Py`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

- **[last-exit](https://github.com/0x963D/last-exit)** — A cyberpunk border encounter powered by TypeSafe Jev. Bluff the guard. Inspect the receipts.
  <sub>`Project` · ★0 · 0x963d · `JS`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — Jev-powered model-judged permission gate for OMP (TypeSafe System One)
  <sub>`Project` · ★0 · strml · `TS` · ⚠ `archived`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — Optional typed TypeSafe AI Jev decisions for OpenClaw, with SecretRef credentials and strict API validation.
  <sub>`Project` · ★0 · olli0103 · `TS`</sub>

- **[openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp)** — High-speed System One Jev AI decision gateway and MCP server powered by OpenRouter
  <sub>`Plugin` · ★0 · ctmx · `Py`</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — Single-agent Pi coding coprocessor with Jev semantic gates, baseline-to-current diff review, and append-only observability telemetry.
  <sub>`Project` · ★0 · kamilpostrozny · `TS`</sub>

- **[pkg-gate](https://github.com/hemanth/pkg-gate)** — Pre-install security gate for npm lifecycle scripts using TypeSafe System One.
  <sub>`Project` · ★0 · hemanth · `JS`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — Detect semantic stagnation in AI agent loops
  <sub>`Project` · ★0 · ashutoshvjti · `TS`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One Search: navigate and trace code with TypeSafe judgments and repository evidence
  <sub>`Project` · ★0 · cpaczek · `TS`</sub>

- **[shade-arena-jev-monitor](https://github.com/nican2018/shade-arena-jev-monitor)** — Evaluating TypeSafe's Jev as a fast monitor and action gate for agent sabotage in SHADE-Arena, compared with Gemini 2.5 Flash/Pro.
  <sub>`Project` · ★0 · nican2018 · `Py`</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town: social-deduction party game for the living room TV, moderated by TypeSafe Jev
  <sub>`Project` · ★0 · tpaulshippy · `Rb` · ⚠ `no licence`</sub>

- **[siege](https://github.com/vnmoorthy/siege)** — SIEGE: 200 people vs one agent. A typed action gate (TypeSafe System One) that learns from every breach, evaluated by W&B Weave, hardened by a defender loop. Built at CoreWeave Hacks: Agent Loops 2026.
  <sub>`Project` · ★0 · vnmoorthy · `TS`</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — Open-source Chrome extension that filters AI-generated prose and ads with Jev
  <sub>`Plugin` · ★0 · neddes · `JS`</sub>

- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** — Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.
  <sub>`Project` · ★0 · aniruddh-krovvidi · `Py` · ⚠ `no licence`</sub>

- **[trustgate](https://github.com/ndolinschi/trustgate)** — TrustGate — indie media T&S gate via TypeSafe Jev
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — Three composable judgment pipelines on TypeSafe's Jev: support-ticket triage, observability alert triage, and a deploy-risk gate.
  <sub>`Project` · ★0 · shivam2003-dev · `Py`</sub>

- **[wakegate](https://github.com/shitianfang/wakegate)** — Ask Jev whether a sleeping agent's wakeup is worth a full LLM turn before you resume it. A fail-open wake gate for long-running agents on Workers, Durable Objects and Node.
  <sub>`Project` · ★0 · shitianfang · `TS`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — Typed judgment layer for coding agents — gates from PRD to ship. Jev-ready, provider-agnostic.
  <sub>`Integration` · ★0 · zahrannnn · `TS` · ⚠ `no licence`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
