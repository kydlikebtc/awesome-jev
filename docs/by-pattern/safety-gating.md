# Safety gating

<sub>[awesome-jev](../../README.md) · [中文](safety-gating.zh-CN.md)</sub>

_Decide whether an action is safe to run. Defence in depth, never a security boundary._

Every catalogued example of this decision — 139 of them. The same rows, with caveats, are in [the index](../../README.md#safety-gating); [the site](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#safety-gating): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 2 · call site 133 · wire shape 2 · example only 0 · independent reports 10 · negative results 0 · no file cited 4. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) <sub>`Official docs` · `Py`</sub>
- [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) <sub>`Official docs` · `Py` · `noul` · `score`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.
  <sub>`Integration` · ★10k+ · `TS` · `choice` · `score` · `noul` · call site [`libs/providers/langchain-typesafe/src/types.ts`](https://github.com/langchain-ai/langchainjs/blob/HEAD/libs/providers/langchain-typesafe/src/types.ts), read 2026-09-22</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · call site [`scripts/jev-spike.mjs`](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs), read 2026-09-22</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction.
  <sub>`Project` · ★10k+ · `Go` · `noul` · call site [`backend/internal/pkg/typesafe/client.go`](https://github.com/Wei-Shaw/sub2api/blob/HEAD/backend/internal/pkg/typesafe/client.go), read 2026-09-22</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)** — Three Score questions on a shared severity scale, blocking the request when two or more cross the line, and failing closed.
  <sub>`Project` · ★1k+ · `Rs` · `score` · call site [`examples/llm-guardrail-jev/guardrail.ts`](https://github.com/agentgateway/agentgateway/blob/HEAD/examples/llm-guardrail-jev/guardrail.ts), read 2026-09-22</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check.
  <sub>`Project` · ★1k+ · `TS` · `choice` · `noul` · call site [`src/shared/jevProtocol.ts`](https://github.com/ThinkInAIXYZ/deepchat/blob/HEAD/src/shared/jevProtocol.ts), read 2026-09-22</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, checks, and approval gates instead of hoping it follows your instructions.
  <sub>`Project` · ★100+ · bastani-inc · `TS` · call site [`packages/ai/src/decision-models.generated.ts`](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts), read 2026-09-24</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)** — Connect TypeSafe Jev to Grok Bot as a cheap decision layer - usage gates, skill template, examples <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · bodila51 · `Py` · call site [`src/jev_client.py`](https://github.com/Bodila51/grok-bot-jev/blob/HEAD/src/jev_client.py), read 2026-09-22</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation.
  <sub>`Project` · ★100+ · `JS` · `choice` · `noul` · call site [`scripts/jev-decide.mjs`](https://github.com/Sac-Y/Jev-cu/blob/HEAD/scripts/jev-decide.mjs), read 2026-09-22</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code.
  <sub>`Project` · ★100+ · `Py` · `choice` · `score` · `noul` · call site [`tactics.py`](https://github.com/RomanSlack/jev-drone/blob/HEAD/tactics.py), read 2026-09-22 · ⚠ `unverified claims`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — An easy way to use jev with your coding agent for tool calling reasoning <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · vinilana · `TS` · call site [`src/jev.ts`](https://github.com/vinilana/jev-gateway/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · leepokai · `JS` · call site [`src/jev.js`](https://github.com/leepokai/jev-guard/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts), read 2026-09-22</sub>

- **[jevals](https://github.com/openlayer-ai/jevals)** — Agent evals and guardrails as Jev decisions: one request per trace, a fraction of a cent, fast enough for the agent loop. Runs locally with Kev or Laya. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · openlayer-ai · `Py` · call site [`src/jevals/backends/typesafe.py`](https://github.com/openlayer-ai/jevals/blob/HEAD/src/jevals/backends/typesafe.py), read 2026-09-22</sub>

- **[mu](https://github.com/qybaihe/mu)** — Coding agent and desktop app built on pi that asks Jev at 38 decision points which tool-output chunks enter the context, which stale tool results to drop, whether a rule-flagged command was asked for and whether fetched pages or MCP output carry injected instructions.
  <sub>`Project` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · call site [`packages/kyrn-judge/src/providers/typesafe.ts`](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts) · ⚠ `self-submitted`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — A decision layer for a coding agent: a measured tool-call gate plus a typed ask for calibrated answers.
  <sub>`Plugin` · ★100+ · y0usaf · `TS` · call site [`src/client.ts`](https://github.com/y0usaf/pi-jev/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain, Jev for cheaper steps. Microduck, Open Duck Mini, LeRobot, XLeRobot, AlohaMini, ToddlerBot or any ROS base. Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM. Simulator, .d
  <sub>`Plugin` · ★100+ · rokbenko · `Py` · call site [`quackd/agent/decision/systemone.py`](https://github.com/rokbenko/quackd/blob/HEAD/quackd/agent/decision/systemone.py), read 2026-09-24</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · notque · `Py` · call site [`plugins/jev-auto-compact/hooks/jev-auto-compact.mjs`](https://github.com/notque/vexjoy-agent/blob/HEAD/plugins/jev-auto-compact/hooks/jev-auto-compact.mjs), read 2026-09-22</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — An AI coding agent that reads your code, edits files, runs commands, and reasons through bugs — across a terminal REPL, a full-screen TUI, and a browser UI, while you keep your hand on every permission. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · wrongstack · `TS` · call site [`packages/core/src/typesafe/client.ts`](https://github.com/WrongStack/WrongStack/blob/HEAD/packages/core/src/typesafe/client.ts), read 2026-09-22</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — Detect youtube sponsor segment with live audio and transcript powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · trungdq88 · `JS` · call site [`extension/lib/jev.js`](https://github.com/trungdq88/youtube-sponsor-detection/blob/HEAD/extension/lib/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★10+ · 24601 · `Py` · call site [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md), read 2026-09-24</sub>

- **[bluenoise](https://github.com/rokcso/bluenoise)** — Blur or hide noisy replies, posts & ads on X (Twitter), and clean up its interface with local, reversible keyword/account rules — no X API, no data collection, no account changes. 用本地可逆的关键词/账号规则模糊或隐藏 X（推特）上的嘈杂回复、帖子和广告，并整理界面——不调用 X API、不收集数据、不修改账号。 <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · rokcso · `TS` · call site [`src/contracts/ai.ts`](https://github.com/rokcso/bluenoise/blob/HEAD/src/contracts/ai.ts), read 2026-09-22</sub>

- **[dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)** — ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness — Jev-powered risk classification & evidence-gated auto-approval. Fail-closed by construction. dsh 生态第一个 System-1 决策插件 <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · asktheway · `TS` · call site [`scripts/smoke.mjs`](https://github.com/AskTheWay/dsh-jev-interceptor/blob/HEAD/scripts/smoke.mjs), read 2026-09-24</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gate completion claims inside DeepSeek Harness. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · horusjiang · `TS` · call site [`src/config.ts`](https://github.com/HorusJiang/dsh-jev-tools/blob/HEAD/src/config.ts), read 2026-09-24</sub>

- **[flue-jev-demo](https://github.com/matthewp/flue-jev-demo)** — Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · matthewp · `TS` · call site [`src/flue-jev.ts`](https://github.com/matthewp/flue-jev-demo/blob/HEAD/src/flue-jev.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★10+ · keeltrace · `Py` · call site [`hermes_nerve/client.py`](https://github.com/keeltrace/hermes-nerve/blob/HEAD/hermes_nerve/client.py), read 2026-09-22</sub>

- **[is-malicious](https://github.com/luantak/is-malicious)** — A codebase scanner that helps you not run malicous code <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · luantak · `TS` · call site [`src/jev.ts`](https://github.com/luantak/is-malicious/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails open on everything else <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · valentynkit · `JS` · call site [`belay.mjs`](https://github.com/valentynkit/jev-belay/blob/HEAD/belay.mjs), read 2026-09-24</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · abdelstark · `Py` · call site [`src/jev_benchmarks/adapters/jev.py`](https://github.com/AbdelStark/jev-benchmarks/blob/HEAD/src/jev_benchmarks/adapters/jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · jmanhype · `Py` · call site [`src/jev_dspy_lab/live.py`](https://github.com/jmanhype/jev-dspy-lab/blob/HEAD/src/jev_dspy_lab/live.py), read 2026-09-22</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — Claude Code PreToolUse gate: regex hard rules and a read-only allowlist first, then one Noul and one Choice decide allow, ask or deny, so clearly safe commands skip the permission prompt. Codex, Cursor and OpenCode adapters, plus a review-router GitHub Action.
  <sub>`Plugin` · ★10+ · eugeniughelbur · `Py` · `noul` · `choice` · call site [`jev_gate.py`](https://github.com/eugeniughelbur/jev-engineering/blob/HEAD/jev_gate.py), read 2026-09-28 · ⚠ `self-submitted`</sub>

- **[jev-guard](https://github.com/klauswg/jev-guard)** — Real-time risk triage gateway for exchange deposits and withdrawals — Jev (TypeSafe System One) handles triage only; adjudication stays in deterministic code. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · klauswg · `Java` · call site [`src/main/java/com/jevguard/eval/EvalRunner.java`](https://github.com/klauswg/jev-guard/blob/HEAD/src/main/java/com/jevguard/eval/EvalRunner.java), read 2026-09-24</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · antoniocoppe · `TS` · call site [`demos/proof/row-filter/run.ts`](https://github.com/AntonioCoppe/jev-harness/blob/HEAD/demos/proof/row-filter/run.ts), read 2026-09-22</sub>

- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)** — Zero-dependency System One decision harness: 5 semantic gates saving frontier AI agent tokens on trivial errors & doom loops. Python + TypeScript + Rust. MCP-compatible. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · ismaelsoilet · `Py` · call site [`src/jev_harness/client.py`](https://github.com/ismaelsoilet/jev-harness/blob/HEAD/src/jev_harness/client.py), read 2026-09-24</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jcpsimmons · `JS` · call site [`src/providers.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs), read 2026-09-22</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★10+ · brainstormity · `Py` · `choice` · `noul` · call site [`typesafe/__init__.py`](https://github.com/brainstormity/Jev-Moderation-Bot/blob/HEAD/typesafe/__init__.py), read 2026-09-22</sub>

- **[jev-runtime-security](https://github.com/ringzerosec/jev-runtime-security)** — Runtime security for AI coding agents: policy is enforced in the kernel at the system call, below the agent and anything it writes, with Jev judging the ambiguous cases.
  <sub>`Project` · ★10+ · ringzerosec · `Rs` · call site [`agent/src/scanner/jev_layer.rs`](https://github.com/ringzerosec/jev-runtime-security/blob/HEAD/agent/src/scanner/jev_layer.rs), read 2026-09-24</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 可疑行为 \| Review Agent Skills and MCP code with Jev, static evidence, and explicit coverage gaps <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · win4r · `Py` · call site [`scripts/jev_client.py`](https://github.com/win4r/jev-security-scan/blob/HEAD/scripts/jev_client.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-sentinel](https://github.com/harshwasan/jev-sentinel)** — Pi coding-agent extension: TypeSafe Jev checks for tool calls, tool outputs and replies (prompt injection, approvals, secret scrubbing, task pinning) <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · harshwasan · `TS` · call site [`src/guard.ts`](https://github.com/harshwasan/jev-sentinel/blob/HEAD/src/guard.ts), read 2026-09-24</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kenhuangus · `Py` · call site [`src/jev_usecases/client.py`](https://github.com/kenhuangus/jev-usecases/blob/HEAD/src/jev_usecases/client.py), read 2026-09-22</sub>

- **[jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot)** — Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · backmeupplz · `TS` · call site [`src/spam.ts`](https://github.com/backmeupplz/jev_antispam_bot/blob/HEAD/src/spam.ts), read 2026-09-22</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — PR Risk review, automated by Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · hexyedev · `Py` · call site [`src/JevPR/providers/jev.py`](https://github.com/HexyeDEV/JevPR/blob/HEAD/src/JevPR/providers/jev.py), read 2026-09-24</sub>

- **[muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook)** — Jev decision layer for Muse: a fast, cheap TypeSafe AI gate before expensive agent work — confidence policy, recipes, reference router, honest measurement. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · bodila51 · `Py` · call site [`src/jev_client.py`](https://github.com/Bodila51/muse-jev-playbook/blob/HEAD/src/jev_client.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action, pi package, and more. Built with Effect.
  <sub>`Project` · ★10+ · tyler-dot-earth · `TS` · call site [`apps/patdown/src/typesafe-judge.ts`](https://github.com/tyler-dot-earth/patdown/blob/HEAD/apps/patdown/src/typesafe-judge.ts), read 2026-09-22</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · mejiasd3v · `JS` · call site [`index.ts`](https://github.com/mejiasd3v/pi-jev-router/blob/HEAD/index.ts), read 2026-09-22</sub>

- **[pi-verdict](https://github.com/jesset/pi-verdict)** — A minimal permission gate for Pi in the style of Claude Code's auto mode <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · jesset · `TS` · call site [`extensions/jev-adapter.ts`](https://github.com/jesset/pi-verdict/blob/HEAD/extensions/jev-adapter.ts), read 2026-09-22</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Code hook <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★10+ · riskaversetech · `TS` · call site [`src/backends/typesafe.ts`](https://github.com/RiskAverseTech/toolgate/blob/HEAD/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)** — Open-source Jev tool-calling authorization gateway for AI agents: deterministic policy, exact-action single-use permits, MCP and HTTP enforcement. <sub>(upstream description)</sub>
  <sub>`Plugin` · omkarghugarkar007 · `TS` · call site [`packages/decision-provider/src/typesafe-jev.ts`](https://github.com/omkarghugarkar007/actiongate-jev/blob/HEAD/packages/decision-provider/src/typesafe-jev.ts), read 2026-09-22</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server: a decision layer for coding agents, built on TypeSafe Jev (System One model). Ship gates, risk checks, file triage that keeps files out of context, and a safe headless browser, with calibrated confidence. For Claude Code, Codex, Cursor. <sub>(upstream description)</sub>
  <sub>`Plugin` · abhishekswe · `TS` · call site [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts), read 2026-09-22</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — Reusable GitHub Action: agent fix loop gated by checks, an AI reviewer, and TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ripwords · `TS` · call site [`src/jev.ts`](https://github.com/Ripwords/agent-gate-loop/blob/HEAD/src/jev.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — An experimental protocol for evidence-aware agent handoffs, bounded worker continuation, and TypeSafe/Jev-assisted review, with reproducible evaluation. <sub>(earlier upstream description)</sub>
  <sub>`Benchmark` · zsoxi · `Py` · call site [`tools/build_benchmark_prompts.py`](https://github.com/zsoXi/agent-handoff-gate/blob/HEAD/tools/build_benchmark_prompts.py), read 2026-09-22 · ⚠ `one commit` `archived`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — AGI JEV Detection — local AI agent monitor: chain-level malicious-agent detection (TypeSafe Jev + Sentinel), escalate-only L1–L5 containment, Neo4j forensics, AngryRobot dashboard. HackSpain 2026. <sub>(upstream description)</sub>
  <sub>`Project` · carlosedm10 · `Py` · call site [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[AskJev](https://github.com/ranjan2829/AskJev)** — AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude) <sub>(upstream description)</sub>
  <sub>`Project` · ranjan2829 · `TS` · call site [`mcp/src/jev-client.ts`](https://github.com/ranjan2829/AskJev/blob/HEAD/mcp/src/jev-client.ts), read 2026-09-24</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full. <sub>(upstream description)</sub>
  <sub>`Project` · jourdanlabs · `Py` · call site [`harness/run.py`](https://github.com/jourdanlabs/assay-001/blob/HEAD/harness/run.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run.
  <sub>`Article` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `vendor numbers`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — A CLI and GitHub Action that assesses code-change risk using deterministic rules and TypeSafe Jev, recommending checks and reviewers before merge. <sub>(upstream description)</sub>
  <sub>`Project` · moezubair · `TS` · call site [`src/jev.ts`](https://github.com/moezubair/check-risk/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev)** — Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks <sub>(upstream description)</sub>
  <sub>`Plugin` · rahulbalakavi · `Py` · call site [`src/jev_auto_mode/cli.py`](https://github.com/RahulBalakavi/claude-code-jev/blob/HEAD/src/jev_auto_mode/cli.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[claude-jev-plugin](https://github.com/dr-dimitru/claude-jev-plugin)** — TypeSafe Jev semantic guardrails for Claude Code <sub>(upstream description)</sub>
  <sub>`Plugin` · dr-dimitru · `TS` · call site [`dist/client.d.ts`](https://github.com/dr-dimitru/claude-jev-plugin/blob/HEAD/dist/client.d.ts), read 2026-09-22</sub>

- **[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)** — Effect-based safety gate for AI coding agents' shell commands (OpenCode, Antigravity): fast structural rules, then TypeSafe's Jev or a chat model judges what a command does. Certified with Jev at zero dangerous commands allowed. <sub>(upstream description)</sub>
  <sub>`Plugin` · godspede · `TS` · call site [`src/classifier/jev-client.ts`](https://github.com/godspede/construct-auto-classifier/blob/HEAD/src/classifier/jev-client.ts), read 2026-09-24</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill <sub>(upstream description)</sub>
  <sub>`Plugin` · docxology · `Py` · call site [`src/daf_jev/client.py`](https://github.com/docxology/daf-jev/blob/HEAD/src/daf_jev/client.py), read 2026-09-22</sub>

- **[Decision Models as Guardrails](https://dm-as-guardrails.raxitlabs.com)** — Asks Jev 1.13.0, Jev 1.14.0 and 17 other systems, Bedrock Guardrails among them, the same 9,975 labelled guardrail checks in six suites. Jev answers each as a noul; 0.5 or more blocks, nothing tuned per model. Reports balanced accuracy with 95% intervals and USD per 1,000 checks at list price.
  <sub>`Benchmark` · raxIT Labs · `Py` · `noul` · `score` · call site [`benchmark/goldrails_bench/systemone.py`](https://github.com/raxITlabs/decision-models-as-guardrails/blob/HEAD/benchmark/goldrails_bench/systemone.py) · ⚠ `self-submitted`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — DiffJury — TypeSafe Jev PR risk router + code review coach <sub>(upstream description)</sub>
  <sub>`Project` · raihankhan-rk · `TS` · call site [`src/lib/review.ts`](https://github.com/raihankhan-rk/diffjury/blob/HEAD/src/lib/review.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrated probabilities (noul/choice/score) for routing/triage/guardrail judgments, no text generation. 把 TypeSafe Jev 决策模型注册为 DSH agent 工具 <sub>(upstream description)</sub>
  <sub>`Plugin` · nanami-0713 · `JS` · call site [`lib/index.js`](https://github.com/nanami-0713/dsh-jev-decide/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev drives your Ego Lite browser: one typed-choice request per step. Single-file, zero-dependency port of browser-use/jev-ultrafast with multi-model benchmarks and extra guardrails. Unofficial. <sub>(upstream description)</sub>
  <sub>`Benchmark` · shikaizhong-design · `JS` · call site [`jego.js`](https://github.com/shikaizhong-design/ego-jev-ultrafast/blob/HEAD/jego.js), read 2026-09-22</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — A verified browser agent: a cheap Jev guard (evidence-checked completions, a destructive gate) in front of any LLM browser driver, with Jev taking the mechanical steps in dual mode. Built on browser-use; every number pre-registered and measured. <sub>(upstream description)</sub>
  <sub>`Project` · tom-r-main · `Py` · call site [`jevdual/evals/runner.py`](https://github.com/Tom-R-Main/Footwork/blob/HEAD/jevdual/evals/runner.py), read 2026-09-24</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — This repository contains a GitHub issue classifier built on Jev, TypeSafe AI's System One model. It labels every new issue with typed values and calibrated confidence in milliseconds, labelling what it is sure about and escalating what it is not. Three guardrail layers guard every write, and a
  <sub>`Project` · kalyanm45 · `Py` · call site [`src/ghtriage/adapters/typesafe.py`](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/HEAD/src/ghtriage/adapters/typesafe.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard)** — A typed preflight and approval layer for Grok Bot: local policy owns the hard boundaries, Jev judges the ambiguous cases, and Grok Bot executes within the envelope it gets back.
  <sub>`Project` · 0xwhrari · `Py` · call site [`src/grok_jev_guard/jev.py`](https://github.com/0xwhrari/grok-jev-guard/blob/HEAD/src/grok_jev_guard/jev.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[guard-jev](https://github.com/NorbertBodziony/guard-jev)** — A text-moderation demo: one systemOne call screens seven Noul hazards and one severity Score in parallel, and the verdict is computed in code from policy thresholds.
  <sub>`Project` · norbertbodziony · `TS` · call site [`app/api/moderate/route.ts`](https://github.com/NorbertBodziony/guard-jev/blob/HEAD/app/api/moderate/route.ts), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world. <sub>(upstream description)</sub>
  <sub>`Project` · abdelstark · `TS` · call site [`apps/server/src/jev.ts`](https://github.com/AbdelStark/heist-one/blob/HEAD/apps/server/src/jev.ts), read 2026-09-22</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — Issue triage that stays quiet when it isn't sure. Calibrated labels, spam and duplicate detection — with abstention. <sub>(upstream description)</sub>
  <sub>`Project` · emreozyoruk · `JS` · call site [`src/jev.js`](https://github.com/emreozyoruk/hush/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.
  <sub>`Project` · Really Artificial · `JS` · `choice` · `score` · `noul` · call site [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs), read 2026-09-22 · ⚠ `AI-written`</sub>

- **[jev-agent-authorization](https://github.com/kinde-starter-kits/jev-agent-authorization)** — Jev agent authorization for MCP tool calls: Kinde identity and permissions plus Jev's typed, calibrated decisions, checked server-side before every call runs <sub>(upstream description)</sub>
  <sub>`Plugin` · kinde-starter-kits · `TS` · call site [`convex/jev/client.ts`](https://github.com/kinde-starter-kits/jev-agent-authorization/blob/HEAD/convex/jev/client.ts), read 2026-09-24</sub>

- **[jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper)** — Low-latency audio censorship POC using Jev typed decisions and ffmpeg. <sub>(upstream description)</sub>
  <sub>`Project` · santos-sanz · `TS` · call site [`index.ts`](https://github.com/santos-sanz/jev-audio-beeper/blob/HEAD/index.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-benchmark](https://github.com/themsquared/jev-benchmark)** — Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on. <sub>(upstream description)</sub>
  <sub>`Benchmark` · themsquared · `Py` · call site [`bench.py`](https://github.com/themsquared/jev-benchmark/blob/HEAD/bench.py), read 2026-09-24</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through. <sub>(upstream description)</sub>
  <sub>`Project` · ufec · `Kt` · call site [`app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt`](https://github.com/ufec/jev-block-android-ad/blob/HEAD/app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt), read 2026-09-22</sub>

- **[jev-carryforward](https://github.com/dharun-cohere/jev-carryforward)** — What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway. <sub>(upstream description)</sub>
  <sub>`Plugin` · dharundp6 · `TS` · call site [`src/gateway.ts`](https://github.com/dharun-cohere/jev-carryforward/blob/HEAD/src/gateway.ts), read 2026-09-22</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · nikkoxgonzales · `Py` · call site [`jev_certify/analysis.py`](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py), read 2026-09-22</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions-hermes)** — Jev Decisions Plugin for Hermes (and other AI Agents): tool risk reviews, human approval recommendations, evidence checks, and a local decision journal.
  <sub>`Plugin` · bojansandhaus · `Py` · call site [`jev_client.py`](https://github.com/bojansandhaus/jev-decisions-hermes/blob/HEAD/jev_client.py), read 2026-09-22</sub>

- **[jev-dev](https://github.com/n-yokomachi/jev-dev)** — 同じ発言を jev と LLM の両方に判定させ、感情の変動値のズレと応答速度を1画面で見比べるデモ（affectus + Vercel AI Gateway） <sub>(upstream description)</sub>
  <sub>`Project` · n-yokomachi · `TS` · call site [`scripts/probe-jev.ts`](https://github.com/n-yokomachi/jev-dev/blob/HEAD/scripts/probe-jev.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-gate](https://github.com/MongLong0214/jev-gate)** — Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary. <sub>(upstream description)</sub>
  <sub>`Plugin` · monglong0214 · `TS` · call site [`src/jev.ts`](https://github.com/MongLong0214/jev-gate/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves. <sub>(upstream description)</sub>
  <sub>`Plugin` · rashedint32 · `JS` · call site [`lib/jev.mjs`](https://github.com/rashedInt32/jev-gates/blob/HEAD/lib/jev.mjs), read 2026-09-22</sub>

- **[jev-guard](https://github.com/ClemensSchartmueller/jev-guard)** — A cross-agent safety gate for Claude Code, Codex CLI and Antigravity: intercepts shell runs, writes and patches, applies fast local boundary checks, then asks Jev about blast radius, reversibility and destructive potential.
  <sub>`Plugin` · clemensschartmueller · `Go` · call site [`pkg/evaluator/typesafe.go`](https://github.com/ClemensSchartmueller/jev-guard/blob/HEAD/pkg/evaluator/typesafe.go), read 2026-09-24</sub>

- **[jev-guard](https://github.com/CMaintz/jev-guard)** — Vets an LLM agent's tool calls through TypeSafe AI's Jev before they run — allow, block, or hold, failing safe on uncertainty. <sub>(upstream description)</sub>
  <sub>`Project` · cmaintz · `TS` · call site [`src/providers/typesafe.ts`](https://github.com/CMaintz/jev-guard/blob/HEAD/src/providers/typesafe.ts), read 2026-09-24 · ⚠ `archived`</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — Probability-scored guardrails for Claude Code: deny rule-breaking edits and unasked-for deploys, route your docs into each prompt, and check the final answer against the turn's own evidence. <sub>(upstream description)</sub>
  <sub>`Plugin` · muratcakmak · `TS` · call site [`scripts/jev-lint.ts`](https://github.com/muratcakmak/jev-guard/blob/HEAD/scripts/jev-lint.ts), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed. <sub>(upstream description)</sub>
  <sub>`Project` · jyatesdotdev · `Py` · call site [`logtriage/cli.py`](https://github.com/jyatesdotdev/jev-logtriage/blob/HEAD/logtriage/cli.py), read 2026-09-22</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — An OpenAI-compatible proxy that sits between your LLM and your users. It evaluates each sliding window of tokens while the response is still streaming and cuts the stream before a violating token can reach the screen. <sub>(upstream description)</sub>
  <sub>`Project` · thanh-mathieu95 · `JS` · call site [`evaluator.js`](https://github.com/Thanh-Mathieu95/jev-model-tokengate/blob/HEAD/evaluator.js), read 2026-09-22</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · scienthoon · `Py` · call site [`scripts/jev_eval.mjs`](https://github.com/scienthoon/jev-ood-calibration/blob/HEAD/scripts/jev_eval.mjs), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance. <sub>(upstream description)</sub>
  <sub>`Benchmark` · yodablocks · `Py` · call site [`harness/client.py`](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py), read 2026-09-22</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev-compatible decision endpoints <sub>(upstream description)</sub>
  <sub>`Project` · dtduc-git · `Py` · call site [`scripts/refresh.py`](https://github.com/dtduc-git/jev-packs/blob/HEAD/scripts/refresh.py), read 2026-09-22</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent. <sub>(upstream description)</sub>
  <sub>`Plugin` · krw82 · `TS` · call site [`src/jev/client.ts`](https://github.com/krw82/jev-playwright-mcp/blob/HEAD/src/jev/client.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — A bounded Jev risk check for Claude Code: eight risk axes, one request, one optional reinspection. <sub>(upstream description)</sub>
  <sub>`Plugin` · muse0509 · `Go` · call site [`internal/jev/client.go`](https://github.com/muse0509/jev-preflight/blob/HEAD/internal/jev/client.go), read 2026-09-22</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Plugin` · vicente-md · `Java` · call site [`src/main/java/ai/jev/resilience/client/dto/JevRequest.java`](https://github.com/Vicente-MD/jev-resilience/blob/HEAD/src/main/java/ai/jev/resilience/client/dto/JevRequest.java), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets <sub>(upstream description)</sub>
  <sub>`Benchmark` · teyhouse · `Py` · call site [`main.py`](https://github.com/teyhouse/jev-secret-detection/blob/HEAD/main.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-shield](https://github.com/vmendes90/jev-shield)** — Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · vmendes90 · `TS` · call site [`src/background/typesafe.ts`](https://github.com/vmendes90/jev-shield/blob/HEAD/src/background/typesafe.ts), read 2026-09-22</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session. <sub>(upstream description)</sub>
  <sub>`Plugin` · shivampansuriya · `JS` · call site [`src/providers/typesafe.mjs`](https://github.com/ShivamPansuriya/jev-skill-gate/blob/HEAD/src/providers/typesafe.mjs), read 2026-09-24</sub>

- **[jev-skillful](https://github.com/bestagentkits/jev-skillful)** — Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps. <sub>(upstream description)</sub>
  <sub>`Plugin` · bestagentkits · `TS` · call site [`packages/cli/src/core/jev/types.ts`](https://github.com/bestagentkits/jev-skillful/blob/HEAD/packages/cli/src/core/jev/types.ts), read 2026-09-22</sub>

- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** — Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines <sub>(upstream description)</sub>
  <sub>`Project` · bitnovus · `Py` · call site [`experiments/jev-context/evaluate.py`](https://github.com/bitnovus/jev-spam-eval/blob/HEAD/experiments/jev-context/evaluate.py), read 2026-09-22</sub>

- **[jev-switchboard](https://github.com/ZIJIAN004/jev-switchboard)** — A JEV-gated semantic communication layer for parallel coding agents. <sub>(upstream description)</sub>
  <sub>`Project` · zijian004 · `JS` · call site [`src/jev.mjs`](https://github.com/ZIJIAN004/jev-switchboard/blob/HEAD/src/jev.mjs), read 2026-09-22</sub>

- **[jev-tool-permissions](https://github.com/NicolasMontone/jev-tool-permissions)** — Jev-backed tool approval gate and tool-list pruning for the Vercel AI SDK <sub>(upstream description)</sub>
  <sub>`SDK` · nicolasmontone · `TS` · call site [`src/types.ts`](https://github.com/NicolasMontone/jev-tool-permissions/blob/HEAD/src/types.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer)** — See what Jev thinks about your SaaS website — powered by ReplyNodes web context and Vercel AI Gateway. <sub>(upstream description)</sub>
  <sub>`Project` · replynodes · `TS` · call site [`app/api/analyze/route.ts`](https://github.com/replynodes/jev-web-analyzer/blob/HEAD/app/api/analyze/route.ts), read 2026-09-22</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — Jevaluate: evaluate before you trust. Field notes, runnable scripts and an agent skill for TypeSafe Jev: gated evals, a browser loop, a product walk with DeepSeek vision, a UI text judge and a first-click tree test. Co-authored with Claude Fable 5.1. <sub>(upstream description)</sub>
  <sub>`Plugin` · elshinq · `JS` · call site [`scripts/jev.mjs`](https://github.com/ElshinQ/jevaluate/blob/HEAD/scripts/jev.mjs), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jevc](https://github.com/doronp/jevc)** — Compile agent policy prose into deterministic verdict programs: narrow evidence questions for the model, the verdict computed in code. Install: npm i -g jev-compiler <sub>(upstream description)</sub>
  <sub>`Project` · doronp · `TS` · call site [`src/runtime.ts`](https://github.com/doronp/jevc/blob/HEAD/src/runtime.ts), read 2026-09-24</sub>

- **[jevegis](https://github.com/0xArx/jevegis)** — Guardrails for LLM apps in one API call. Prompt injection, jailbreaks, leaks, unsafe content. Built on TypeSafe Jev. MIT. <sub>(upstream description)</sub>
  <sub>`Project` · 0xarx · `TS` · call site [`src/lib/typesafe.ts`](https://github.com/0xArx/jevegis/blob/HEAD/src/lib/typesafe.ts), read 2026-09-22</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — Code-review gate for CI and coding agents: asks TypeSafe Jev small typed questions about functions, files, tests and docs, and reports findings with locations and probabilities <sub>(upstream description)</sub>
  <sub>`Project` · tech-byte-frontier · `Rs` · call site [`src/auth/provider.rs`](https://github.com/Tech-Byte-Frontier/jevgate/blob/HEAD/src/auth/provider.rs), read 2026-09-24</sub>

- **[JevLang](https://github.com/TimMikeladze/JevLang)** — A policy engine for LLM decisions: declare routes, gates and actions once in TypeScript or Python, and every decision comes validated, explainable, replayable and audited. <sub>(upstream description)</sub>
  <sub>`SDK` · timmikeladze · `JS` · call site [`examples/entity-alignment.js`](https://github.com/TimMikeladze/JevLang/blob/HEAD/examples/entity-alignment.js), read 2026-09-24</sub>

- **[jevmod](https://github.com/ohernandezdev/jevmod)** — Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you own. Discord/Telegram/Reddit bots, CLI, Python, npm, HTTP API, MCP. <sub>(upstream description)</sub>
  <sub>`Plugin` · ohernandezdev · `Py` · call site [`jevmod/judge.py`](https://github.com/ohernandezdev/jevmod/blob/HEAD/jevmod/judge.py), read 2026-09-24</sub>

- **[jevnav](https://github.com/dtduc-git/jevnav)** — Page truth for browser agents — and decisions that replay, test and audit. Jev picks the element, risky actions are gated, every run replays offline in CI. <sub>(upstream description)</sub>
  <sub>`Project` · dtduc-git · `Py` · call site [`src/jevnav/decide.py`](https://github.com/dtduc-git/jevnav/blob/HEAD/src/jevnav/decide.py), read 2026-09-24</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — Sub-100ms security gate for AI agent tool calls, powered by TypeSafe's Jev (System-1) decision model. Single-request Choice/Noul/Score evaluation, dual-factor blocking matrix, calibrated-confidence routing, fail-closed parsing, zero-config local fallback. LangChain-ready. <sub>(upstream description)</sub>
  <sub>`Project` · lgy1027 · `Py` · call site [`jevshield/client.py`](https://github.com/lgy1027/jevshield/blob/HEAD/jevshield/client.py), read 2026-09-22</sub>

- **[jit-context](https://github.com/wojciechwiesner/jit-context)** — Architectural Moat: JIT-JEV Context OS — Epistemic runtime & JEV System 1 context gate for AI agents (L0 SQLite WAL <3ms, Epistemic Invariants I1–I10, CERN Zenodo DOI: 10.5281/zenodo.22649542) <sub>(upstream description)</sub>
  <sub>`Project` · wojciechwiesner · `Py` · call site [`src/cognitive/jev_engine.py`](https://github.com/wojciechwiesner/jit-context/blob/HEAD/src/cognitive/jev_engine.py), read 2026-09-24</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

- **[last-exit](https://github.com/0x963D/last-exit)** — A cyberpunk border encounter powered by TypeSafe Jev. Bluff the guard. Inspect the receipts. <sub>(upstream description)</sub>
  <sub>`Project` · 0x963d · `JS` · call site [`lib/hosted.mjs`](https://github.com/0x963D/last-exit/blob/HEAD/lib/hosted.mjs), read 2026-09-22</sub>

- **[macos-computer-use-kit](https://github.com/Sur-Cai/macos-computer-use-kit)** — AX-first computer use for AI agents on macOS with optional Jev (TypeSafe System One) semantic guards: calibrated target/input judgments before an irreversible action, decisions kept in code. Accessibility-tree targeting, window-scoped input, clipboard-safe paste, read-back verification…
  <sub>`Plugin` · sur-cai · `Py` · call site [`src/macos_computer_use/jev.py`](https://github.com/Sur-Cai/macos-computer-use-kit/blob/HEAD/src/macos_computer_use/jev.py), read 2026-09-24</sub>

- **[mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation)** — Input moderation for Mastra agents on TypeSafe Jev — one file <sub>(upstream description)</sub>
  <sub>`Project` · codealive-ai · `TS` · call site [`jev-moderation.ts`](https://github.com/CodeAlive-AI/mastra-jev-moderation/blob/HEAD/jev-moderation.ts), read 2026-09-22</sub>

- **[nachalnik](https://github.com/ljedrz/nachalnik)** — A transparent agent runtime in Rust: context, tools, permissions and requests as explicit state. Plus an MCP bridge and a terminal agent. <sub>(upstream description)</sub>
  <sub>`Plugin` · ljedrz · `Rs` · call site [`kamchatka/src/args.rs`](https://github.com/ljedrz/nachalnik/blob/HEAD/kamchatka/src/args.rs), read 2026-09-24</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — Jev-powered model-judged permission gate for OMP (TypeSafe System One) <sub>(upstream description)</sub>
  <sub>`Project` · strml · `TS` · call site [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts), read 2026-09-22 · ⚠ `archived`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — Binary approval gate for Codex and Claude Code — every intercepted tool call is reviewed by TypeSafe JEV and composed through a versioned local policy, with scoped authorization. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · alexj11324 · `Go` · cited file [`internal/jev/client.go`](https://github.com/alexj11324/open-jev-approvals/blob/HEAD/internal/jev/client.go), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — Optional typed TypeSafe AI Jev decisions for OpenClaw, with SecretRef credentials and strict API validation. <sub>(upstream description)</sub>
  <sub>`Project` · olli0103 · `TS` · call site [`src/client.ts`](https://github.com/Olli0103/openclaw-typesafe-ai/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[opencode-jev-guard](https://github.com/CogFlux/opencode-jev-guard)** — OpenCode 2 plugin that sends every shell command (local or via FarHand) to TypeSafe's Jev and asks you first when it leaves files outside the project, installs software globally, changes global settings, is harmful or exposes private data <sub>(upstream description)</sub>
  <sub>`Plugin` · cogflux · `TS` · call site [`jev-guard.ts`](https://github.com/CogFlux/opencode-jev-guard/blob/HEAD/jev-guard.ts), read 2026-09-24</sub>

- **[openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp)** — High-speed System One Jev AI decision gateway and MCP server powered by OpenRouter <sub>(upstream description)</sub>
  <sub>`Plugin` · ctmx · `Py` · call site [`examples/demo_typesafe_sdk.py`](https://github.com/ctmx/openrouter-jev-mcp/blob/HEAD/examples/demo_typesafe_sdk.py), read 2026-09-22</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — Single-agent Pi coding coprocessor with Jev semantic gates, baseline-to-current diff review, and append-only observability telemetry. <sub>(upstream description)</sub>
  <sub>`Project` · kamilpostrozny · `TS` · call site [`src/index.ts`](https://github.com/KamilPostrozny/pi-jev-code/blob/HEAD/src/index.ts), read 2026-09-22</sub>

- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** — A Jev (TypeSafe System One) permission gate for the Pi coding agent: judges every bash / write / edit call before it runs <sub>(upstream description)</sub>
  <sub>`Project` · kurihada · `TS` · call site [`src/jev.ts`](https://github.com/kurihada/pi-jev-permit/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[pkg-gate](https://github.com/hemanth/pkg-gate)** — Pre-install security gate for npm lifecycle scripts using TypeSafe System One. <sub>(upstream description)</sub>
  <sub>`Project` · hemanth · `JS` · call site [`src/gate.js`](https://github.com/hemanth/pkg-gate/blob/HEAD/src/gate.js), read 2026-09-22</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — Detect semantic stagnation in AI agent loops <sub>(upstream description)</sub>
  <sub>`Project` · ashutoshvjti · `TS` · call site [`experiments/jev-client.ts`](https://github.com/AshutoshVJTI/progressgate/blob/HEAD/experiments/jev-client.ts), read 2026-09-22</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One Search: navigate and trace code with TypeSafe judgments and repository evidence <sub>(upstream description)</sub>
  <sub>`Project` · cpaczek · `TS` · call site [`src/client.ts`](https://github.com/cpaczek/s1s/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[shade-arena-jev-monitor](https://github.com/nican2018/shade-arena-jev-monitor)** — Evaluating TypeSafe's Jev as a fast monitor and action gate for agent sabotage in SHADE-Arena, compared with Gemini 2.5 Flash/Pro. <sub>(upstream description)</sub>
  <sub>`Project` · nican2018 · `Py` · call site [`llms/typesafe_llm.py`](https://github.com/nican2018/shade-arena-jev-monitor/blob/HEAD/llms/typesafe_llm.py), read 2026-09-22</sub>

- **[shady-town](https://github.com/tpaulshippy/shady-town)** — Shady Town: social-deduction party game for the living room TV, moderated by TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · tpaulshippy · `Rb` · call site [`lib/shady_town/evaluator.rb`](https://github.com/tpaulshippy/shady-town/blob/HEAD/lib/shady_town/evaluator.rb), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[siege](https://github.com/vnmoorthy/siege)** — SIEGE: 200 people vs one agent. A typed action gate (TypeSafe System One) that learns from every breach, evaluated by W&B Weave, hardened by a defender loop. Built at CoreWeave Hacks: Agent Loops 2026. <sub>(upstream description)</sub>
  <sub>`Project` · vnmoorthy · `TS` · call site [`backend/app/gate.py`](https://github.com/vnmoorthy/siege/blob/HEAD/backend/app/gate.py), read 2026-09-22</sub>

- **[sloppy-jevs-extension](https://github.com/neddes/sloppy-jevs-extension)** — Open-source Chrome extension that filters AI-generated prose and ads with Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · neddes · `JS` · call site [`background.js`](https://github.com/neddes/sloppy-jevs-extension/blob/HEAD/background.js), read 2026-09-22</sub>

- **[solvi](https://github.com/solvi-ai/solvi)** — Python runtime with a System One API adapter: Jev, an LLM or a local checkpoint proposes typed answers; hard checks, rules and calibrated thresholds decide, abstain or escalate to a person, and every decision is a hash-chained replayable trace.
  <sub>`SDK` · mxkuzn · `Py` · `choice` · `noul` · call site [`src/solvi/core/deciders/systemone.py`](https://github.com/solvi-ai/solvi/blob/HEAD/src/solvi/core/deciders/systemone.py), read 2026-10-23 · ⚠ `self-submitted`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — Every tool call your agent makes, checked before it runs. A Claude Code plugin that uses TypeSafe AI's Jev to verify each pending tool call against the session plan, then allows it, asks you, or blocks it. Proof of concept <sub>(upstream description)</sub>
  <sub>`Plugin` · getexcited · `TS` · call site [`lib/jev.ts`](https://github.com/getexcited/stepwarden/blob/HEAD/lib/jev.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** — Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python. <sub>(upstream description)</sub>
  <sub>`Project` · aniruddh-krovvidi · `Py` · call site [`jev.py`](https://github.com/aniruddh-krovvidi/switchboard/blob/HEAD/jev.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[toolgate](https://github.com/ndolinschi/toolgate)** — Agent tool/MCP call gate — allow / ask_human / deny via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/toolgate/blob/HEAD/src/lib/jev.ts), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[trustgate](https://github.com/ndolinschi/trustgate)** — TrustGate — indie media T&S gate via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/trustgate/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model) <sub>(upstream description)</sub>
  <sub>`Project` · opaielsheikh · `TS` · call site [`lib/typesafe.ts`](https://github.com/opaielsheikh/typesafe-migration-guard/blob/HEAD/lib/typesafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — Three composable judgment pipelines on TypeSafe's Jev: support-ticket triage, observability alert triage, and a deploy-risk gate. <sub>(upstream description)</sub>
  <sub>`Project` · shivam2003-dev · `Py` · call site [`src/triage/mock.py`](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/HEAD/src/triage/mock.py), read 2026-09-22</sub>

- **[wakegate](https://github.com/shitianfang/wakegate)** — Ask Jev whether a sleeping agent's wakeup is worth a full LLM turn before you resume it. A fail-open wake gate for long-running agents on Workers, Durable Objects and Node. <sub>(upstream description)</sub>
  <sub>`Project` · shitianfang · `TS` · call site [`src/index.ts`](https://github.com/shitianfang/wakegate/blob/HEAD/src/index.ts), read 2026-09-22</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — A local decision layer in Jev's shape: yes/no, choice and rubric questions read off one token's logprobs from a local model, with a Claude Code permission gate measured on held-out command sets.
  <sub>`Jev-like alternative` · Xinyu Liu · `TS` · `noul` · `choice` · `score` · cited file [`src/gate.ts`](https://github.com/liu-x27/XavierJev/blob/HEAD/src/gate.ts), read 2026-09-25 · ⚠ `not Jev itself` `AI-written`</sub>

- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** — Typed judgment layer for coding agents — gates from PRD to ship. Jev-ready, provider-agnostic. <sub>(upstream description)</sub>
  <sub>`Integration` · zahrannnn · `TS` · call site [`src/backends/jev.ts`](https://github.com/Zahrannnn/zcode-jev/blob/HEAD/src/backends/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
