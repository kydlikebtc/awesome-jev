# Tool selection

<sub>[awesome-jev](../../README.md) · [中文](tool-selection.zh-CN.md)</sub>

_Which tool or action the agent should call next._

Every catalogued example of this decision — 161 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#tool-selection); [the site](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=en) can filter them further by language, primitive and kind.

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐ — Maps natural-language trading requests onto ordinary typed functions by turning function names and closed-set arguments into confidence-aware questions.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐ — Picks at most one skill out of 182 for an agent turn: one request ranks every skill and asks whether the turn needs one at all, a second reads the top three.
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — Runnable demo code for a smart home assistant that evaluates user requests with typed decisions.
  <sub>`Official docs` · `Py`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★31,582 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.
  <sub>`Project` · ★30,300 · `Py` · `choice`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.
  <sub>`Project` · ★27,886 · `Py` · `choice` · `noul`</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)** — Computer-use action selection in Python and TypeScript: Jev picks the next browser action from an immutable candidate set, with reobserve and abstain as reserved options.
  <sub>`Project` · ★26,164 · `Py` · `TS` · `choice`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed.
  <sub>`Project` · ★19,261 · Browser Use · `Py` · `choice` · ⚠ `vendor numbers`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.
  <sub>`Project` · ★18,204 · Vercel Labs · `TS` · `choice`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check.
  <sub>`Project` · ★6,341 · `TS` · `choice` · `noul`</sub>

- **[jev-trader](https://github.com/jarrodwatts/jev-trader)** — High-frequency market making on a test network, deciding buy or sell from spread and trade direction.
  <sub>`Project` · ★2,214 · `TS` · `choice` · ⚠ `unverified claims`</sub>

- **[agent-desktop](https://github.com/lahfir/agent-desktop)** — Desktop automation that reads the system accessibility tree and decides which button, menu or field to act on next.
  <sub>`Project` · ★1,607 · `Rs` · `choice` · `noul`</sub>

- **[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)** — Computer use on macOS: OCR the screen, classify the next action, click. Costs a fraction of a cent per step.
  <sub>`Project` · ★933 · awlevin · `Py`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★718 · `Py` · `choice` · `score` · `noul`</sub>

- **[tiptour-macos](https://github.com/milind-soni/tiptour-macos)** — Open-Source fast local computer use
  <sub>`Project` · ★662 · milind-soni · `Swift`</sub>

- **[agent](https://github.com/AgentiLoop/Agent)** — AgentiLoop Agent! An Autonomous Agentic Agent for Mac, and exclusive Apple only harnesss. Supports automation, scripting, coding, build anything and more. Powered by 21 LLM providers across local and cloud platforms. Dark or Light Mode UI.
  <sub>`Integration` · ★632 · agentiloop · `Swift`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation.
  <sub>`Project` · ★591 · `JS` · `choice` · `noul`</sub>

- **[foreman](https://github.com/thruwire/foreman)** — A software-factory foreman that uses Jev to decide what an agent pipeline should do next.
  <sub>`Project` · ★538 · thruwire · `Py`</sub>

- **[omg.dev](https://github.com/BennyKok/omg.dev)** — omg.dev — Remote control for claude, codex, cursor, opencode, pi, grok, jcocde with mobile client
  <sub>`Plugin` · ★537 · bennykok · `TS`</sub>

- **[jev-browser-use](https://github.com/wy-coliney/jev-browser-use)** — Splits the loop: Jev clicks, a reasoning model thinks and verifies.
  <sub>`Project` · ★444 · wy-coliney · `JS`</sub>

- **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)** — Plays Super Mario Bros. from structured emulator RAM rather than screenshots, deciding run, jump and dodge.
  <sub>`Project` · ★379 · `Py` · `choice` · `score` · `noul` · ⚠ `code untested` `one commit` `no licence`</sub>

- **[mobile-jev](https://github.com/droidrun/mobile-jev)** — Mobile computer use: Jev picks the next on-screen action on a phone.
  <sub>`Project` · ★377 · droidrun · `JS`</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — An AI coding agent that reads your code, edits files, runs commands, and reasons through bugs — across a terminal REPL, a full-screen TUI, and a browser UI, while you keep your hand on every permission.
  <sub>`Project` · ★335 · wrongstack · `TS`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — Voice-driven browser control where target criteria are rebuilt per request from the live element list, always including a none option.
  <sub>`Project` · ★269 · `JS` · `choice` · `score` · `noul`</sub>

- **[jev-browser](https://github.com/jkudish/jev-browser)** — Browser automation where Jev chooses the next action.
  <sub>`Project` · ★253 · jkudish · `TS`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain, Jev for cheaper steps. Microduck, Open Duck Mini, LeRobot, XLeRobot, AlohaMini, ToddlerBot or any ROS base. Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM. Simulator, .d
  <sub>`Plugin` · ★231 · rokbenko · `Py`</sub>

- **[embodied-jev](https://github.com/FBddcz/embodied-jev)** — EmbodiedJev: MuJoCo robot decision workbench with MiniCPM5-2B, Jev and compatible model APIs
  <sub>`Project` · ★219 · fbddcz · `Py`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — An easy way to use jev with your coding agent for tool calling reasoning
  <sub>`Project` · ★202 · vinilana · `TS`</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — An AI video editor routing an editing instruction to an operation, a target clip and a track, with a keyword router as fallback.
  <sub>`Project` · ★193 · `TS` · `choice` · `noul` · ⚠ `no licence`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — A router for models, tools and subagents.
  <sub>`Project` · ★189 · billionsbobby · `TS`</sub>

- **[jevharness](https://github.com/TianyuCodings/JevHarness)** — LLM-authored task-specific Jev harnesses with optional full-trajectory reward reflection and GEPA evolution.
  <sub>`Project` · ★184 · tianyucodings · `Py` · ⚠ `no licence`</sub>

- **[jevpilot](https://github.com/standardagents/jevpilot)** — A driving simulator autopilot asking two choices per tick, which short-circuits single-option questions locally instead of paying to send them.
  <sub>`Project` · ★182 · `JS` · `choice` · ⚠ `no licence`</sub>

- **[interlinked-cli](https://github.com/QuentinCody/interlinked-cli)** — The harness for your harness. Local hooks, taste enforcement, and developer observability for AI coding agents (Claude Code, Codex, Cursor, Copilot CLI).
  <sub>`Plugin` · ★178 · quentincody · `TS`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code.
  <sub>`Project` · ★164 · `Py` · `choice` · `score` · `noul` · ⚠ `unverified claims`</sub>

- **[jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision)** — Jev DSH 决策引擎｜面向 Agent Harness 的结构化决策插件。原生支持 DeepSeek Harness，通过 iPolloWork 支持 OpenCode、Codex Harness。
  <sub>`Plugin` · ★157 · devin-axis · `JS` · ⚠ `no licence`</sub>

- **[systemoneharness](https://github.com/HarnessRouter/SystemOneHarness)** — The system one Harness for system one models
  <sub>`Project` · ★157 · harnessrouter · `Py`</sub>

- **[macbrow](https://github.com/timpratim/macbrow)** — Hands free Mac and Browser control powered by Gradium
  <sub>`Project` · ★142 · timpratim · `Py`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — A decision layer for a coding agent: a measured tool-call gate plus a typed ask for calibrated answers.
  <sub>`Plugin` · ★142 · y0usaf · `TS`</sub>

- **[jev-trade](https://github.com/aowang-ai/jev-trade)** — Live Jev trader on Hyperliquid
  <sub>`Project` · ★130 · aowang-ai · `TS`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following.
  <sub>`Project` · ★126 · `Py` · `choice`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — Ranks an agent's skills for the next step using live session context, with Claude Code hooks.
  <sub>`Plugin` · ★116 · dicklesworthstone · `Rs`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim in an answer cites a quote from the page.
  <sub>`Project` · ★100 · agent-labs-dev · `Py`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.
  <sub>`Project` · ★94 · `TS` · `choice` · `noul`</sub>

- **[jev-use](https://github.com/savka777/jev-use)** — Say it, and your Mac does it. A computer-use harness on Jev that reads the screen through Accessibility. Fast, no vision model
  <sub>`Project` · ★92 · savka777 · `Swift`</sub>

- **[jev-browser](https://github.com/Ying-Kai-Liao/jev-browser)** — Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.
  <sub>`Project` · ★82 · ying-kai-liao · `JS`</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — A WebMCP benchmark, measures WebMCP against other browser-agent interfaces.
  <sub>`Benchmark` · ★80 · nekuda-ai · `TS`</sub>

- **[jev-desktop](https://github.com/yikangy873-gif/jev-desktop)** — TypeSafe Jev action selection inside Codex Computer Use
  <sub>`Plugin` · ★67 · yikangy873-gif · `JS`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks.
  <sub>`Project` · ★64 · dimweaker · `Py`</sub>

- **[jev-mem](https://github.com/libingzheren/Jev-Mem)** — Jev-Mem: System-One Controlled Agentic Memory
  <sub>`Project` · ★56 · libingzheren · `Py`</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — Read-only Instagram, TikTok and LinkedIn research: Jev routes the platform and selects each bounded socai CLI action from fresh browser evidence; code validates targets and preserves source links.
  <sub>`Project` · ★53 · socai-io · `JS` · `choice` · ⚠ `3rd-party key`</sub>

- **[pi-jev](https://github.com/TheoOliveira/pi-jev)** — Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev
  <sub>`Plugin` · ★46 · theooliveira · `TS`</sub>

- **[jev-robot-control](https://github.com/openroboto-ai/jev-robot-control)** — Jev against two LLMs on direct Cartesian control of an xArm7 in MuJoCo — intent, movement and gripper each step — with recorded responses, trajectories and replays. One seed-0 trial per controller, not a success rate.
  <sub>`Benchmark` · ★44 · openroboto-ai · `Py`</sub>

- **[robojev](https://github.com/lykycy123/RoboJEV)** — Two-stage JEV control of a Franka Panda in MuJoCo
  <sub>`Project` · ★42 · lykycy123 · `Py`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay i
  <sub>`Project` · ★33 · choxos · `JS`</sub>

- **[JevScout](https://github.com/hqman/JevScout)** — A coding-agent skill that hunts jobs on real company sites: Chrome sees and acts, Jev scores every link and posting, and the host LLM never picks what to click.
  <sub>`Plugin` · ★33 · hqman · `Py` · ⚠ `no licence`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP.
  <sub>`Plugin` · ★30 · leepokai · `JS`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — A browser 1v1 FPS where every decision tick judges movement, view angle, aim, fire and jump.
  <sub>`Project` · ★30 · `TS` · `choice` · ⚠ `code untested` `no licence`</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — A chatbot built on a model that cannot generate text (TypeSafe AI's Jev, driven autoregressively)
  <sub>`Project` · ★26 · bewinxed · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — An agent plugin that hands steps needing no text output to Jev instead of the main model.
  <sub>`Plugin` · ★25 · shitianfang · `JS`</sub>

- **[tsai-sc](https://github.com/phyous/tsai-sc)** — Drives a 1990s real-time strategy game through keyboard and mouse, recording the action probabilities.
  <sub>`Project` · ★24 · phyous · `Py`</sub>

- **[pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode)** — Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.
  <sub>`Project` · ★23 · jomatsu · `TS`</sub>

- **[jev-for-chrome](https://github.com/chy4pro/jev-for-chrome)** — Jev for Chrome: drives the tab you are looking at with TypeSafe Jev, a sub-second decision model. Community port of browser-use/jev-ultrafast, not affiliated with TypeSafe.
  <sub>`Project` · ★21 · chy4pro · `TS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.
  <sub>`Project` · ★21 · jcpsimmons · `JS`</sub>

- **[agent-chaperone](https://github.com/agent-chaperone/agent-chaperone)** — Screens an AI agent's tool calls before they run and tool results before the agent reads them. An MCP proxy plus a hooks adapter for a client's built-in tools.
  <sub>`Plugin` · ★20 · agent-chaperone · `TS`</sub>

- **[jcr](https://github.com/NiazMorshed2007/jcr)** — A Jev-powered resolver for agent harnesses to find deterministic commands and their context in a nested capability tree.
  <sub>`Project` · ★19 · niazmorshed2007 · `JS`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow.
  <sub>`Project` · ★19 · ray-hughes · `Rb`</sub>

- **[jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)** — Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.
  <sub>`Project` · ★17 · khordoo · `TS`</sub>

- **[live-jev](https://github.com/vinilana/live-jev)** — 2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model
  <sub>`Project` · ★17 · vinilana · `JS` · ⚠ `no licence`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven.
  <sub>`Project` · ★16 · parth-kp · `Py`</sub>

- **[jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp)** — Hand a whole browser task off in one call: a decision model drives the page server-side, so a flow costs one call, not a turn per click. Ref-based element tables, code-checked assertions, zero-model macro replay, over the Chrome DevTools Protocol.
  <sub>`Plugin` · ★15 · jiawei686 · `Py`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — Software, by reflex. A sentence becomes a call of a small program, chosen by Jev, TypeSafe AI's classifier, and run only when it is sure enough. Reflexes are recipes anyone can write, share and improve. A CLI you talk to, a package manager for reflexes from git, and a TypeScript SDK.
  <sub>`Project` · ★14 · evoke-build · `Rs`</sub>

- **[azdaja](https://github.com/kubet/azdaja)** — Minimal harness-agnostic recursive language model layer — one binary, Python + llm()
  <sub>`Project` · ★13 · kubet · `Py`</sub>

- **[discern](https://github.com/doeixd/discern)** — Craft Type-Safe Uncertainty-aware semantic pattern matching, control flow, and smart procedures for Effect DecisionModel and Jev
  <sub>`Project` · ★12 · doeixd · `TS`</sub>

- **[jev-doom-agent](https://github.com/lukaske/jev-doom-agent)** — A browser-native Doom agent experiment with structured spatial state, composable AI controls, live decision telemetry, and a Chocolate Doom WebAssembly runtime.
  <sub>`Project` · ★12 · lukaske · `TS` · ⚠ `no licence`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.
  <sub>`Project` · ★12 · antoniocoppe · `TS`</sub>

- **[jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm)** — Zero-shot English goals on a sim Franka. Jev chains hardcoded primitives.
  <sub>`Project` · ★11 · taruntomar122 · `Py`</sub>

- **[super-jev](https://github.com/Kevthetech143/super-jev)** — A small, extensible decision-to-action harness for TypeSafe Jev
  <sub>`Project` · ★11 · kevthetech143 · `Py`</sub>

- **[browserclaw](https://github.com/GoldenLoaf24h/browserclaw)** — BrowserClaw - High-efficiency Chrome browser automation MCP server
  <sub>`Plugin` · ★10 · goldenloaf24h · `TS`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and safe orchestration.
  <sub>`Project` · ★10 · forvela · `JS`</sub>

- **[jev-autopilot](https://github.com/arielweinberger/jev-autopilot)** — This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01.
  <sub>`Project` · ★10 · arielweinberger · `TS` · ⚠ `no licence`</sub>

- **[hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)** — Autonomous multi-source rental search powered by TypeSafe Jev
  <sub>`Project` · ★9 · nancy-chauhan · `JS`</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.
  <sub>`SDK` · ★8 · himomohi · `Py`</sub>

- **[AskJev](https://github.com/ranjan2829/AskJev)** — AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)
  <sub>`Project` · ★8 · ranjan2829 · `TS`</sub>

- **[jevscape](https://github.com/Skyvern-AI/jevscape)** — RuneBench harness for TypeSafe's Jev: bounded action catalog, tick-mode controller and a live dashboard
  <sub>`Project` · ★8 · skyvern-ai · `TS` · ⚠ `no licence`</sub>

- **[gg-friggin-ez](https://github.com/ItisShikhar/gg-friggin-ez)** — Fast, drop-in multilingual profanity and toxicity screener for Node.js, powered by System 1 models like TypeSafe AI Jev and Laya. Catches leetspeak, character spacing, and romanized profanity across languages including Kannada, Telugu, Tamil, Hindi, and Bengali. ~50-500ms latency.
  <sub>`Project` · ★7 · itisshikhar · `TS`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world.
  <sub>`Project` · ★7 · abdelstark · `TS`</sub>

- **[jev-browser](https://github.com/tontoko/jev-browser)** — One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.
  <sub>`Project` · ★7 · tontoko · `JS`</sub>

- **[laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent)** — Local, open-source Jev alternative: browser agent decisions with Laya (System One model) on your own machine. No cloud, no API key. Playwright/CDP, MCP-friendly.
  <sub>`Jev-like alternative` · ★7 · chenneyzhuang · `Py` · ⚠ `not Jev itself`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev.
  <sub>`Project` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[ui-generator-instinct-jev](https://github.com/joevidev/ui-generator-instinct-jev)** — Jev as a UI generator: describe a case in free text and Jev answers only typed questions over real option sets, picking and configuring an actual shadcn/ui component or page block. It never writes code or copy.
  <sub>`Project` · ★7 · joevidev · `TS` · ⚠ `no licence`</sub>

- **[bicameral](https://github.com/AbdelStark/bicameral)** — Hybrid coding harness: System 2 writes, System 1 (Jev) runs reflexes.
  <sub>`Project` · ★6 · abdelstark · `TS`</sub>

- **[jev-lab](https://github.com/jammaru/jev-lab)** — 100 AI NPCs live in a tiny town. Jev chooses the next action; the world writes the story.
  <sub>`Project` · ★6 · jammaru · `TS`</sub>

- **[jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red)** — Pokemon Red on PyBoy: code owns the route and the arithmetic, Jev picks at branches in about 100 ms, calibration measured instead of assumed
  <sub>`Project` · ★6 · valentynkit · `Py`</sub>

- **[jev-tool-router](https://github.com/jackbarunz/jev-tool-router)** — Jev-powered MCP tool routing for Codex
  <sub>`Plugin` · ★6 · jackbarunz · `JS`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — Screen a folder of CVs with the TypeSafe Jev decision model: typed judgments, an editable policy, free re-scoring.
  <sub>`Project` · ★6 · gtaras7 · `TS`</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — A pre-compaction advisor for DeepSeek Harness. Runs before the standard `compaction-basic` backend, using TypeSafe JEV to safely prune low-value tool results from model context. Original session events stay in the append-only log; only the model-visible view is replaced with compact markers or
  <sub>`Project` · ★5 · wjw66 · `TS`</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic
  <sub>`Project` · ★5 · kenhuangus · `Py`</sub>

- **[jevonly](https://github.com/buluoray/JevOnly)** — Pure Jev that can "type" and drive towards task completion.
  <sub>`Project` · ★5 · buluoray · `Py`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — AGI JEV Detection — local AI agent monitor: chain-level malicious-agent detection (TypeSafe Jev + Sentinel), escalate-only L1–L5 containment, Neo4j forensics, AngryRobot dashboard. HackSpain 2026.
  <sub>`Project` · ★4 · carlosedm10 · `Py` · ⚠ `no licence`</sub>

- **[computer-use-jev](https://github.com/paulsmith/computer-use-jev)** — macOS computer use driven by Jev (TypeSafe System One) as the decision maker
  <sub>`Project` · ★4 · paulsmith · `Go`</sub>

- **[ego-jev](https://github.com/jiangkoumo/ego-jev)** — Drive the ego lite browser with Jev (TypeSafe System One): one indexed element table in, one operation + target out, single process. ~2x faster than a per-step LLM loop in our measurements.
  <sub>`Project` · ★4 · jiangkoumo · `JS`</sub>

- **[jev-mobile](https://github.com/Friedjof/jev-mobile)** — Fast structured Android control loops with TypeSafe Jev and Mobile MCP
  <sub>`Plugin` · ★4 · friedjof · `Py`</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — An OpenAI-compatible proxy that sits between your LLM and your users. It evaluates each sliding window of tokens while the response is still streaming and cuts the stream before a violating token can reach the screen.
  <sub>`Project` · ★4 · thanh-mathieu95 · `JS`</sub>

- **[jev-ra](https://github.com/brnyxx/jev-ra)** — Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.
  <sub>`Plugin` · ★4 · brnyxx · `Py`</sub>

- **[jev-robotics-demo](https://github.com/FazalAAli/jev-robotics-demo)** — Jev (TypeSafe System One) vs Claude Opus 5 driving a simulated robot arm in MuJoCo
  <sub>`Project` · ★4 · fazalaali · `Py`</sub>

- **[jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control)** — Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app.
  <sub>`Project` · ★4 · chris-wozniczek · `Swift`</sub>

- **[otto](https://github.com/NobleSpartan6/otto)** — Open-source native computer use for macOS and Windows: TypeSafe Jev, local OCR, and selective planning.
  <sub>`Project` · ★4 · noblespartan6 · `TS`</sub>

- **[slidepilot](https://github.com/harshil1712/slidepilot)** — Voice-driven semantic auto-advance for Slidev, powered by Cloudflare Agents and TypeSafe AI Jev
  <sub>`Project` · ★4 · harshil1712 · `TS`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server: a decision layer for coding agents, built on TypeSafe Jev (System One model). Ship gates, risk checks, file triage that keeps files out of context, and a safe headless browser, with calibrated confidence. For Claude Code, Codex, Cursor.
  <sub>`Plugin` · ★3 · abhishekswe · `TS`</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — Jev-judged context compaction for DeepSeek Harness: semantic tool-result pruning + deterministic receipt compaction
  <sub>`Project` · ★3 · yangyu666 · `JS`</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev drives your Ego Lite browser: one typed-choice request per step. Single-file, zero-dependency port of browser-use/jev-ultrafast with multi-model benchmarks and extra guardrails. Unofficial.
  <sub>`Benchmark` · ★3 · shikaizhong-design · `JS`</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM summaries with fast keep/truncate/drop decisions from jev-latest; everything kept stays verbatim. Port of tamaratran/fast-jev-compaction.
  <sub>`Project` · ★3 · kolawong · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verification.
  <sub>`Project` · ★3 · rinnecoder · `Py`</sub>

- **[jev-browser-control](https://github.com/nexibeo/jev-browser-control)** — Let Claude code, chatgpt codex or control your own Chrome. Chrome extension + MCP server: Jev, TypeSafe's decision model, picks each click in ~0.5 s for a fraction of a cent. MIT, bring your own OpenRouter key.
  <sub>`Plugin` · ★3 · nexibeo · `JS`</sub>

- **[jev-builder](https://github.com/collapseindex/jev-builder)** — A browser form for building requests to TypeSafe's Jev: pick a template, fill in the blanks, copy the request. No JSON, no install, runs locally.
  <sub>`Project` · ★3 · collapseindex · `JS`</sub>

- **[jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** — Smart Codex overlay with JEV model routing, context optimization & Kanban automation. Reduce tokens, keep control
  <sub>`Plugin` · ★3 · charlyhno-eng · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — Context compaction for Hermes sessions that never summarises: every tool call is scored by TypeSafe's Jev model, stale calls are dropped, everything kept stays verbatim.
  <sub>`Project` · ★3 · picaye · `JS`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.
  <sub>`Project` · ★3 · foadsf · `Py`</sub>

- **[jevdroid](https://github.com/antiyro/jevdroid)** — A typed Python framework for controlling Android over ADB with Jev.
  <sub>`Project` · ★3 · antiyro · `Py`</sub>

- **[langchain-skill-router](https://github.com/deyna256/langchain-skill-router)** — Per-turn skill selection for LangChain and deepagents agents: a fast judge picks the few skills a turn needs, so a catalog of hundreds stays out of the prompt.
  <sub>`Plugin` · ★3 · deyna256 · `Py`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — Binary approval gate for Codex and Claude Code — every intercepted tool call is reviewed by TypeSafe JEV and composed through a versioned local policy, with scoped authorization.
  <sub>`Jev-like alternative` · ★3 · alexj11324 · `Go` · ⚠ `not Jev itself`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.
  <sub>`Plugin` · ★3 · legacybridge-tech · `TS`</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification.
  <sub>`Project` · ★2 · aidil2105 · `Py`</sub>

- **[jev-browser-skill](https://github.com/zurfyx/jev-browser-skill)** — Let Jev, TypeSafe's ~100ms decision model, drive your browser. A plug-and-play skill for Claude Code and Codex.
  <sub>`Plugin` · ★2 · zurfyx · `JS`</sub>

- **[jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa)** — Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo.
  <sub>`Project` · ★2 · nainish-rai · `Py` · ⚠ `no licence`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev
  <sub>`Plugin` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-layer](https://github.com/typakon4/jev-layer)** — Portable System-1 decision layer for agent harnesses with host-owned routing, receipts, replay, and fail-open integrations.
  <sub>`Integration` · ★2 · typakon4 · `JS`</sub>

- **[jev-physical-ai](https://github.com/robokrunch/jev-physical-ai)** — Putting TypeSafe's Jev to work on robots, fleets, and edge hardware — real measured numbers, honestly caveated.
  <sub>`Project` · ★2 · robokrunch · `Py`</sub>

- **[jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong)** — Jev plays browser table tennis in real time: structured telemetry, typed decisions, ordinary Chrome inputs, and auditable evidence.
  <sub>`Benchmark` · ★2 · icohen007 · `JS`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.
  <sub>`Plugin` · ★2 · hamakyo · `TS`</sub>

- **[jev-turbo](https://github.com/sightmap/jev-turbo)** — Jev-powered semantic browser use
  <sub>`Project` · ★2 · sightmap · `Go`</sub>

- **[jevarena](https://github.com/raihankhan-rk/jevarena)** — JevArena — two Jev agents duel in click-only browser games (Browser Use + TypeSafe Jev)
  <sub>`Project` · ★2 · raihankhan-rk · `TS`</sub>

- **[jevloop](https://github.com/parkavenue9639/jevloop)** — A Jev-driven general-purpose agent harness for faster, lower-cost execution, with built-in side-by-side experiments against LLM-only agents.
  <sub>`Project` · ★2 · parkavenue9639 · `Py`</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — Sub-100ms security gate for AI agent tool calls, powered by TypeSafe's Jev (System-1) decision model. Single-request Choice/Noul/Score evaluation, dual-factor blocking matrix, calibrated-confidence routing, fail-closed parsing, zero-config local fallback. LangChain-ready.
  <sub>`Project` · ★2 · lgy1027 · `Py`</sub>

- **[robo-harness](https://github.com/grmkris/robo-harness)** — SO-101 robot-arm agent workbench: Bun/Effect coordinator, React workbench, Python LeRobot motor owner
  <sub>`Project` · ★2 · grmkris · `TS` · ⚠ `no licence`</sub>

- **[tsai-civ2](https://github.com/phyous/tsai-civ2)** — TypeSafe Jev plays original Civilization II in a browser, with live action probabilities. Experimental full-game harness.
  <sub>`Project` · ★2 · phyous · `Py`</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — Shadow-mode validation harness for a pre-execution firewall on AI agent tool calls (TypeSafe/Jev). Real run, findings in report.md.
  <sub>`Project` · ★2 · anshchoudhary · `Py` · ⚠ `no licence`</sub>

- **[zerosweep](https://github.com/sysadarsh/zerosweep)** — Autonomous System-One Triage Engine & Benchmark powered by TypeSafe AI (Jev). 75ms inference, $0 output tokens, and RLCD epistemic safety gates.
  <sub>`Benchmark` · ★2 · sysadarsh · `TS` · ⚠ `no licence`</sub>

- **[datajev](https://github.com/zzz1YAO/DataJev)** — ⚡ DataJev LLM → Analyze Jev → Continue / Switch / Verify / Stop System-1 control for System-2 data agents
  <sub>`Project` · ★1 · zzz1yao · `Py`</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design.
  <sub>`Benchmark` · ★1 · xienda · `JS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — The decision layer for AI agents. Typed, calibrated decisions in ~400ms for two hundredths of a cent: gate tool calls, route models, rank options. With the 300-call injection test that found what breaks.
  <sub>`Project` · ★1 · eugeniughelbur · `Py`</sub>

- **[jev-routing](https://github.com/nekowasabi/jev-routing)** — Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.
  <sub>`Plugin` · ★1 · nekowasabi · `Go`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — Jevaluate: evaluate before you trust. Field notes, runnable scripts and an agent skill for TypeSafe Jev: gated evals, a browser loop, a product walk with DeepSeek vision, a UI text judge and a first-click tree test. Co-authored with Claude Fable 5.1.
  <sub>`Plugin` · ★1 · elshinq · `JS`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — Snake controlled by parallel Jev assessments, with one API call per game tick.
  <sub>`Project` · ★1 · siroccomask · `Py`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — Every tool call your agent makes, checked before it runs. A Claude Code plugin that uses TypeSafe AI's Jev to verify each pending tool call against the session plan, then allows it, asks you, or blocks it. Proof of concept
  <sub>`Plugin` · ★1 · getexcited · `TS`</sub>

- **[typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo)** — Three.js drone simulator with a Python backend and live TypeSafe Jev navigation
  <sub>`Project` · ★1 · kxzk · `Py` · ⚠ `no licence`</sub>

- **[browser-use-olympics](https://github.com/eriestra/browser-use-olympics)** — Browser Use Olympics by Almond: one prompt, five events, one clock. Plus fast loop, a ~200-line browser computer-use agent (Chrome DevTools + TypeSafe Jev).
  <sub>`Project` · ★0 · eriestra · `TS`</sub>

- **[casse-brique-typesafe](https://github.com/Para-FR/casse-brique-typesafe)** — A Next.js brick breaker whose paddle is controlled in real time by TypeSafe AI's Jev model. Built with Claude Code.
  <sub>`Plugin` · ★0 · para-fr · `TS` · ⚠ `no licence`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — Asks for an operation plus a target for each operation it might have picked, so a browser step never needs a second round trip.
  <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>

- **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)** — Pairs a choice over tools with a separate noul on whether a tool is needed at all, because those are different questions.
  <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — Judge agent steps — ok / retry / escalate / stop via TypeSafe Jev
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能
  <sub>`Plugin` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — Benchmark-driven Jev router and judge for cost-aware, reliable LLM coding workflows
  <sub>`Benchmark` · ★0 · erendikmenn · `Py`</sub>

- **[jev-playground](https://github.com/hegargarcia/jev-playground)** — Benchmarks Jev against other evaluation models in games with explicit states and legal actions: code owns the rules and transitions, each model picks the next action, and outcomes are measured.
  <sub>`Benchmark` · ★0 · hegargarcia · `TS` · ⚠ `no licence`</sub>

- **[ps2-ai-agent](https://github.com/opaielsheikh/ps2-ai-agent)** — Autonomous PlayStation 2 AI Agent with real-time visual telemetry HUD powered by TypeSafe Jev System One
  <sub>`Project` · ★0 · opaielsheikh · `Py` · ⚠ `no licence`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One Search: navigate and trace code with TypeSafe judgments and repository evidence
  <sub>`Project` · ★0 · cpaczek · `TS`</sub>

- **[swarmrouter](https://github.com/ndolinschi/swarmrouter)** — Route tasks to research/code/browser/support/writer agents via TypeSafe Jev
  <sub>`Project` · ★0 · ndolinschi · `TS` · ⚠ `no licence`</sub>

- **[terrarium](https://github.com/TheGali/terrarium)** — A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.
  <sub>`Project` · ★0 · thegali · `JS`</sub>

- **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)** — Wires Jev into Browser Use to drive a browser automation agent.
  <sub>`Video` · AICodeKing · ⚠ `unverified claims`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
