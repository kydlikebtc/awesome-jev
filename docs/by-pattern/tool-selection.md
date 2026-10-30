# Tool selection

<sub>[awesome-jev](../../README.md) · [中文](tool-selection.zh-CN.md)</sub>

_Which tool or action the agent should call next._

Every catalogued example of this decision — 241 of them. The same rows, with caveats, are in [the index](../../README.md#tool-selection); [the site](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#tool-selection): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 3 · call site 233 · wire shape 4 · example only 0 · independent reports 11 · negative results 1 · no file cited 4. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) <sub>`Official docs` · `Py` · `choice` · `noul`</sub>
- [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home) <sub>`Official docs` · `Py`</sub>

## Examples in this repository

Code under this repository's [`examples/`](../../examples/) filed under this pattern. Each is also listed below, with its summary; [the examples' README](../../examples/README.md) says how far they have been checked.

- [Example: speculative fan-out](../../examples/03-fan-out/main.py) <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>
- [Example: tool selection with a none option](../../examples/04-tool-selection/main.py) <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐ — Maps natural-language trading requests onto ordinary typed functions by turning function names and closed-set arguments into confidence-aware questions.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐ — Picks at most one skill out of 182 for an agent turn: one request ranks every skill and asks whether the turn needs one at all, a second reads the top three.
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — Runnable demo code for a smart home assistant that evaluates user requests with typed decisions.
  <sub>`Official docs` · `Py`</sub>

- **[ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)** — Educational paper-trading and backtesting app whose investor-persona agents turn a financial snapshot into a bullish, bearish or neutral signal. With TypeSafe as provider, one Jev request per agent asks a choice of direction and a five-level score of each case's strength, mapped to the agents' JSON. <sub>(written by a model)</sub>
  <sub>`Integration` · ★10k+ · virattt · `Py` · call site [`hedge_fund/llm/client.py`](https://github.com/virattt/ai-hedge-fund/blob/HEAD/hedge_fund/llm/client.py), read 2026-09-24</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · call site [`scripts/jev-spike.mjs`](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs), read 2026-09-22</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.
  <sub>`Project` · ★10k+ · `Py` · `choice` · call site [`python/providers/typesafe/composio_typesafe/provider.py`](https://github.com/ComposioHQ/composio/blob/HEAD/python/providers/typesafe/composio_typesafe/provider.py), read 2026-09-22</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)** — Computer-use action selection in Python and TypeScript: Jev picks the next browser action from an immutable candidate set, with reobserve and abstain as reserved options.
  <sub>`Project` · ★10k+ · `Py` · `TS` · `choice` · call site [`libs/cua-driver/examples/jev-use/python/jev_adapter.py`](https://github.com/trycua/cua/blob/HEAD/libs/cua-driver/examples/jev-use/python/jev_adapter.py), read 2026-09-22</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.
  <sub>`Project` · ★10k+ · `Py` · `choice` · `noul` · call site [`fastmcp_slim/fastmcp/experimental/transforms/jev_search.py`](https://github.com/PrefectHQ/fastmcp/blob/HEAD/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py), read 2026-09-22</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed.
  <sub>`Project` · ★10k+ · Browser Use · `Py` · `choice` · call site [`jev_ultrafast/model.py`](https://github.com/browser-use/jev-ultrafast/blob/HEAD/jev_ultrafast/model.py), read 2026-09-22 · ⚠ `vendor numbers`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.
  <sub>`Project` · ★10k+ · Vercel Labs · `TS` · `choice` · call site [`apps/web/lib/jev/compose.ts`](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts), read 2026-09-22</sub>

- **[agent-desktop](https://github.com/lahfir/agent-desktop)** — Desktop automation that reads the system accessibility tree and decides which button, menu or field to act on next.
  <sub>`Project` · ★1k+ · `Rs` · `choice` · `noul` · call site [`scripts/jev/policy.mjs`](https://github.com/lahfir/agent-desktop/blob/HEAD/scripts/jev/policy.mjs), read 2026-09-24</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check.
  <sub>`Project` · ★1k+ · `TS` · `choice` · `noul` · call site [`src/shared/jevProtocol.ts`](https://github.com/ThinkInAIXYZ/deepchat/blob/HEAD/src/shared/jevProtocol.ts), read 2026-09-22</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`jevkit/client.py`](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py), read 2026-09-22 · ⚠ `measured, not adopted`</sub>

- **[jev-browser-use](https://github.com/wy-coliney/jev-browser-use)** — Splits the loop: Jev clicks, a reasoning model thinks and verifies.
  <sub>`Project` · ★1k+ · wy-coliney · `JS` · call site [`skills/jev-browser-use/bridge.mjs`](https://github.com/wy-coliney/jev-browser-use/blob/HEAD/skills/jev-browser-use/bridge.mjs), read 2026-09-22</sub>

- **[jev-trader](https://github.com/jarrodwatts/jev-trader)** — High-frequency market making on a test network, deciding buy or sell from spread and trade direction.
  <sub>`Project` · ★1k+ · `TS` · `choice` · call site [`src/config.ts`](https://github.com/jarrodwatts/jev-trader/blob/HEAD/src/config.ts), read 2026-09-22 · ⚠ `unverified claims`</sub>

- **[reticle](https://github.com/reticlehq/reticle)** — Checks an agent's "done" by driving the running app and returning pass, fail or cannot tell. Its benchmark harness asks Jev, in one call on captured evidence, five nouls (did the intended consequence happen, is the capture clean, did the app error), a pass/fail/unknown choice and a severity score. <sub>(written by a model)</sub>
  <sub>`Project` · ★1k+ · reticlehq · `TS` · call site [`bench/harness/jev.mjs`](https://github.com/reticlehq/reticle/blob/HEAD/bench/harness/jev.mjs), read 2026-09-24</sub>

- **[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)** — Computer use on macOS: OCR the screen, classify the next action, click. Costs a fraction of a cent per step.
  <sub>`Project` · ★1k+ · awlevin · `Py` · call site [`typesafe_computer_use/decide.py`](https://github.com/awlevin/typesafe-computer-use/blob/HEAD/typesafe_computer_use/decide.py), read 2026-09-22</sub>

- **[agent](https://github.com/AgentiLoop/Agent)** — AgentiLoop Agent! An Autonomous Agentic Agent for Mac, and exclusive Apple only harnesss. Supports automation, scripting, coding, build anything and more. Powered by 21 LLM providers across local and cloud platforms. Dark or Light Mode UI.
  <sub>`Integration` · ★100+ · agentiloop · `Swift` · call site [`TypeSafeKit/Sources/TypeSafeKit/TypeSafeClient.swift`](https://github.com/AgentiLoop/Agent/blob/HEAD/TypeSafeKit/Sources/TypeSafeKit/TypeSafeClient.swift), read 2026-09-22</sub>

- **[beebots](https://github.com/imikerussell/beebots)** — Three trading bots race on OKX perpetual futures, paper trading by default: Jev (or Gemini) picks each move as a choice from the legal actions plus a score for conviction, with a deterministic fallback, a plain-code risk layer and a live dashboard. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · imikerussell · `TS` · `choice` · `score` · call site [`src/jev.ts`](https://github.com/imikerussell/beebots/blob/HEAD/src/jev.ts), read by a model 2026-10-24</sub>

- **[embodied-jev](https://github.com/FBddcz/embodied-jev)** — MuJoCo workbench where a model drives a Franka arm through carry, stack and obstacle tasks. With Jev, each step is a choice among the controller's actions, given text state and detected coordinates; physics judges success. Two Jev carry runs ended in 89 and 88 steps, both dropping the block. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · fbddcz · `Py` · call site [`src/embodied_jev/policies.py`](https://github.com/FBddcz/embodied-jev/blob/HEAD/src/embodied_jev/policies.py), read 2026-09-22</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — Browser agent: each page is indexed into candidate controls and Jev chooses the next one, so it cannot click what is not there; a Gemini Flash LLM plans and reads, and answers cite the page. Its maintainer recorded 99.2% on 46 tasks against 97.8% for hosted Browser Use, at under a tenth of the cost. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · agent-labs-dev · `Py` · call site [`src/fastbrowse/clients/typesafe.py`](https://github.com/agent-labs-dev/fastbrowse/blob/HEAD/src/fastbrowse/clients/typesafe.py), read 2026-09-22</sub>

- **[foreman](https://github.com/thruwire/foreman)** — A software-factory foreman that uses Jev to decide what an agent pipeline should do next.
  <sub>`Project` · ★100+ · thruwire · `Py` · call site [`src/foreman/foreman/jev.py`](https://github.com/thruwire/foreman/blob/HEAD/src/foreman/foreman/jev.py), read 2026-09-22</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — An AI video editor routing an editing instruction to an operation, a target clip and a track, with a keyword router as fallback.
  <sub>`Project` · ★100+ · `TS` · `choice` · `noul` · call site [`scripts/jev.js`](https://github.com/kevinbadi/hyperedit/blob/HEAD/scripts/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[interlinked-cli](https://github.com/QuentinCody/interlinked-cli)** — Local guard for AI coding agents (Claude Code, Codex) that checks each tool hook against deterministic rules and blocks dangerous ones. Jev is an optional scoring signal: its answers can only tighten a verdict, never gate alone, and any failure or the $0.25 spend ceiling counts as not measured. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · quentincody · `TS` · call site [`src/harness/jev/client.ts`](https://github.com/QuentinCody/interlinked-cli/blob/HEAD/src/harness/jev/client.ts), read 2026-09-22</sub>

- **[Jev Plays Pokémon Red](https://github.com/christianmat/jev-pokemon)** — Harness in which Jev beat Pokémon Red: it reads the emulator's memory, lists the legal options with facts (type matchups, damage estimates, distance to the objective) and Jev picks one. 16,150 decisions over 37 h 40 m for about $1.65, via the AI SDK on Vercel AI Gateway. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · christianmat · `TS` · call site [`src/jev/gateway.ts`](https://github.com/christianmat/jev-pokemon/blob/HEAD/src/jev/gateway.ts), read by a model 2026-10-24 · ⚠ `unverified claims`</sub>

- **[jev-browser](https://github.com/jkudish/jev-browser)** — Browser automation where Jev chooses the next action.
  <sub>`Project` · ★100+ · jkudish · `TS` · call site [`src/index.ts`](https://github.com/jkudish/jev-browser/blob/HEAD/src/index.ts), read 2026-09-24</sub>

- **[jev-browser](https://github.com/Ying-Kai-Liao/jev-browser)** — Browser automation where an LLM plans and Jev decides: one ~300 ms request per round asks which element, action and value, and if the step is done, blocked, showing an error or about to do something irreversible; Playwright acts. Author's run: 40 of 42 live-site tasks right, 0 false done claims. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · ying-kai-liao · `JS` · call site [`src/jev.mjs`](https://github.com/Ying-Kai-Liao/jev-browser/blob/HEAD/src/jev.mjs), read 2026-09-24</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.
  <sub>`Project` · ★100+ · `TS` · `choice` · `noul` · call site [`apps/server/src/jev/client.ts`](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts), read 2026-09-22</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation.
  <sub>`Project` · ★100+ · `JS` · `choice` · `noul` · call site [`scripts/jev-decide.mjs`](https://github.com/Sac-Y/Jev-cu/blob/HEAD/scripts/jev-decide.mjs), read 2026-09-22</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code.
  <sub>`Project` · ★100+ · `Py` · `choice` · `score` · `noul` · call site [`tactics.py`](https://github.com/RomanSlack/jev-drone/blob/HEAD/tactics.py), read 2026-09-22 · ⚠ `unverified claims`</sub>

- **[jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision)** — Plugin for DeepSeek Harness, and through iPolloWork for OpenCode and Codex Harness, that lets the agent ask Jev which available tool, skill or agent fits a task, whether a capability is needed and how well a result meets stated criteria. It returns choices and probabilities and acts on none. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · devin-axis · `JS` · call site [`service/jev.mjs`](https://github.com/Devin-AXIS/jev-dsh-decision/blob/HEAD/service/jev.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — Local gateway for coding agents such as Codex, Claude Code and OpenCode. Each turn it asks Jev which offered tool fits; when Jev is confident it steers the LLM to that tool, otherwise the request passes through unchanged. If Jev is down, slow or misconfigured, requests go straight to the LLM. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · vinilana · `TS` · call site [`src/jev.ts`](https://github.com/vinilana/jev-gateway/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Security hook for coding agents: before each tool call Jev judges how much harm it could do, whether the user asked for it and whether it follows untrusted text, and code denies, asks or allows; afterwards Jev scans the result for prompt injection. For Claude Code, Codex, Cursor and more. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · leepokai · `JS` · call site [`src/jev.js`](https://github.com/leepokai/jev-guard/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[jev-mem](https://github.com/libingzheren/Jev-Mem)** — Agent memory where Jev, or a local Laya, makes the frequent decisions as nouls and choices: which relations to draw between memories, which graph view to search, when enough evidence is found; an LLM writes the answer. On LoCoMo the paper reports 11.0% better answers and 36.7% lower latency. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · libingzheren · `Py` · call site [`memory/jev_client.py`](https://github.com/libingzheren/Jev-Mem/blob/HEAD/memory/jev_client.py), read 2026-09-22</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — Read-only Instagram, TikTok and LinkedIn research: Jev routes the platform and selects each bounded socai CLI action from fresh browser evidence; code validates targets and preserves source links.
  <sub>`Project` · ★100+ · socai-io · `JS` · `choice` · call site [`src/actions.js`](https://github.com/socai-io/jev-social/blob/HEAD/src/actions.js), read 2026-09-23 · ⚠ `3rd-party key`</sub>

- **[jev-trade](https://github.com/aowang-ai/jev-trade)** — Trading bot on Hyperliquid running five coins from five wallets. Every tick Jev reads the order book and position and answers choices: long or short; open, close or hold; and the cross leverage. The bot places the order, and hold sends none. Without a wallet key it is a dry run with simulated fills. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · aowang-ai · `TS` · call site [`src/model.ts`](https://github.com/aowang-ai/jev-trade/blob/HEAD/src/model.ts), read 2026-09-24</sub>

- **[jev-use](https://github.com/savka777/jev-use)** — Voice and typed computer use for macOS: the app reads the front window's Accessibility tree instead of screenshots, and each step one Jev request chooses an operation and a numbered target, typed text being a span of your sentence, with nouls on whether more steps remain or the effect already shows. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · savka777 · `Swift` · call site [`Sources/JevCore/Decision.swift`](https://github.com/savka777/jev-use/blob/HEAD/Sources/JevCore/Decision.swift), read 2026-09-24</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — Voice-driven browser control where target criteria are rebuilt per request from the live element list, always including a none option.
  <sub>`Project` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/jev.js`](https://github.com/moritzkremb/jev-voice-browser/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension)** — Chrome side panel turning a page's WebMCP tools into Jev questions as you type: a choice over the tools plus "none of these", enums as choices, booleans as nouls, free text as a choice over spans of your words, an "is it stated?" noul per optional field. Only confident read-only calls run unasked. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · sdras · `JS` · call site [`src/jev.js`](https://github.com/sdras/jev-webmcp-extension/blob/HEAD/src/jev.js), read 2026-09-24</sub>

- **[jevharness](https://github.com/TianyuCodings/JevHarness)** — An LLM writes a task-specific harness in which code computes features, asks Jev questions and turns the answers into actions; rewards and full traces can then revise it. In the author's Pokémon run, five rounds of reflection lifted the eval win rate from 3 of 12 games to 9 of 12. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · tianyucodings · `Py` · call site [`auto_jev/providers.py`](https://github.com/TianyuCodings/JevHarness/blob/HEAD/auto_jev/providers.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevpilot](https://github.com/standardagents/jevpilot)** — A driving simulator autopilot asking two choices per tick, which short-circuits single-option questions locally instead of paying to send them.
  <sub>`Project` · ★100+ · `JS` · `choice` · call site [`server/jev.js`](https://github.com/standardagents/jevpilot/blob/HEAD/server/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — A router for models, tools and subagents.
  <sub>`Project` · ★100+ · billionsbobby · `TS` · call site [`functions/api/jev.js`](https://github.com/BillionsBobby/JevRouter/blob/HEAD/functions/api/jev.js), read 2026-09-22</sub>

- **[Jevry](https://github.com/michaelswissa/jevry)** — Open-source desktop browser that works through websites from a plain-language task: a text model plans, Jev picks each action as a choice among what the browser can actually execute (never generated JavaScript or selectors), and Chromium acts with visible steps and stop controls. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · michaelswissa · `TS` · `choice` · call site [`desktop/jev-direct-plan.ts`](https://github.com/michaelswissa/jevry/blob/HEAD/desktop/jev-direct-plan.ts), read by a model 2026-10-24</sub>

- **[macbrow](https://github.com/timpratim/macbrow)** — Voice control for a Mac and Chrome. One Jev request, about 300 ms, routes each utterance: a choice among the tools for the open apps, plus chat or new action, with argument choices alongside; high confidence runs, middling asks. A noul checks each script an LLM writes for a new tool. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · timpratim · `Py` · call site [`macbrow/generator.py`](https://github.com/timpratim/macbrow/blob/HEAD/macbrow/generator.py), read 2026-09-22</sub>

- **[mobile-jev](https://github.com/droidrun/mobile-jev)** — Mobile computer use: Jev picks the next on-screen action on a phone.
  <sub>`Project` · ★100+ · droidrun · `JS` · call site [`apps/jev-studio/app/components/use-studio.ts`](https://github.com/droidrun/mobile-jev/blob/HEAD/apps/jev-studio/app/components/use-studio.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following.
  <sub>`Project` · ★100+ · `Py` · `choice` · call site [`src/neo4jev/navigator.py`](https://github.com/jexp/neo4jev/blob/HEAD/src/neo4jev/navigator.py), read 2026-09-22</sub>

- **[omg.dev](https://github.com/BennyKok/omg.dev)** — Phone remote for Claude Code, Codex and other coding agents running on your computer or a hosted one. Its mobile end-to-end tests use Jev as the decision layer: given the screen's accessibility tree, nouls ask whether a step is done or a dead end and a choice picks the element to tap next. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · bennykok · `TS` · call site [`mobile/scripts/jev.ts`](https://github.com/BennyKok/omg.dev/blob/HEAD/mobile/scripts/jev.ts), read 2026-09-22</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — A decision layer for a coding agent: a measured tool-call gate plus a typed ask for calibrated answers.
  <sub>`Plugin` · ★100+ · y0usaf · `TS` · call site [`src/client.ts`](https://github.com/y0usaf/pi-jev/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain, Jev for cheaper steps. Microduck, Open Duck Mini, LeRobot, XLeRobot, AlohaMini, ToddlerBot or any ROS base. Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM. Simulator, .d
  <sub>`Plugin` · ★100+ · rokbenko · `Py` · call site [`quackd/agent/decision/systemone.py`](https://github.com/rokbenko/quackd/blob/HEAD/quackd/agent/decision/systemone.py), read 2026-09-24</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — Ranks an agent's skills for the next step using live session context, with Claude Code hooks.
  <sub>`Plugin` · ★100+ · dicklesworthstone · `Rs` · call site [`src/jev/endpoint.rs`](https://github.com/Dicklesworthstone/skillranker/blob/HEAD/src/jev/endpoint.rs), read 2026-09-22</sub>

- **[system1-agents](https://github.com/ThinkFlowLab/system1-agents)** — Prebuilt agents for browser use, computer use, games and robotics whose decisions go to a System 1 model, Jev, Laya or Cua-S1, as typed choices. In the author's runs Jev matched a chat model's score while being 1.41 to 6.39 times faster and 5.3 to 25.3 times cheaper per scenario. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · thinkflowlab · `Py` · call site [`s1a/decision_models/wire.py`](https://github.com/ThinkFlowLab/system1-agents/blob/HEAD/s1a/decision_models/wire.py), read 2026-09-24</sub>

- **[systemoneharness](https://github.com/HarnessRouter/SystemOneHarness)** — The system one Harness for system one models
  <sub>`Project` · ★100+ · harnessrouter · `Py` · call site [`systemone_harness/provider.py`](https://github.com/HarnessRouter/SystemOneHarness/blob/HEAD/systemone_harness/provider.py), read 2026-09-22</sub>

- **[tiptour-macos](https://github.com/milind-soni/tiptour-macos)** — macOS menu-bar assistant that clicks for you. In its default Jev mode you type a task; each step, a Jev choice picks one of the controls detected on screen and TipTour clicks it, with no confidence cutoff, until Jev picks none or reports the task done, or after 12 actions. Screenshots stay local. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · milind-soni · `Swift` · call site [`TipTour/Jev/JevClient.swift`](https://github.com/milind-soni/tiptour-macos/blob/HEAD/TipTour/Jev/JevClient.swift), read 2026-09-22</sub>

- **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)** — Plays Super Mario Bros. from structured emulator RAM rather than screenshots, deciding run, jump and dodge.
  <sub>`Project` · ★100+ · `Py` · `choice` · `score` · `noul` · call site [`src/typesafe_mario/policy.py`](https://github.com/fhshaik/typesafe-mario/blob/HEAD/src/typesafe_mario/policy.py), read 2026-09-22 · ⚠ `code untested` `one commit` `no licence`</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — Open-source coding agent with its own kernel, memory, multi-agent fleet and permission policy, run from a terminal, TUI or browser. An opt-in TypeSafe service asks Jev typed choice, noul and score questions to suggest skills and classify dispatch, and the agent can call Jev as a tool. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · wrongstack · `TS` · call site [`packages/core/src/typesafe/client.ts`](https://github.com/WrongStack/WrongStack/blob/HEAD/packages/core/src/typesafe/client.ts), read 2026-09-22</sub>

- **[agent-chaperone](https://github.com/agent-chaperone/agent-chaperone)** — Screens an AI agent's tool calls before they run and tool results before the agent reads them. An MCP proxy plus a hooks adapter for a client's built-in tools. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · agent-chaperone · `TS` · call site [`src/backends/typesafe.ts`](https://github.com/agent-chaperone/agent-chaperone/blob/HEAD/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[azdaja](https://github.com/kubet/azdaja)** — Minimal harness-agnostic recursive language model layer — one binary, Python + llm() <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kubet · `Py` · call site [`bench/jev/adapter.py`](https://github.com/kubet/azdaja/blob/HEAD/bench/jev/adapter.py), read 2026-09-22</sub>

- **[browserclaw](https://github.com/GoldenLoaf24h/browserpaw)** — BrowserClaw - High-efficiency Chrome browser automation MCP server <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★10+ · goldenloaf24h · `TS` · call site [`app/native-server/src/jev/jev-client.ts`](https://github.com/GoldenLoaf24h/browserpaw/blob/HEAD/app/native-server/src/jev/jev-client.ts), read 2026-09-22</sub>

- **[CUA-JEV](https://github.com/ZJU-REAL/CUA-JEV)** — Jev for Computer Use <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · zju-real · `Py` · call site [`src/cua_jev/cost.py`](https://github.com/ZJU-REAL/CUA-JEV/blob/HEAD/src/cua_jev/cost.py), read 2026-09-24</sub>

- **[dejevu](https://github.com/idovmamane/dejevu)** — Jev? Déjà vu. Browser agents that run on instinct, no Jev needed. One look at the page, one call to any open model, one action. Faster than the Jev demo on Google Flights. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · idovmamane · `Py` · cited file [`dejevu/policy.py`](https://github.com/idovmamane/dejevu/blob/HEAD/dejevu/policy.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[discern](https://github.com/doeixd/discern)** — Craft Type-Safe Uncertainty-aware semantic pattern matching, control flow, and smart procedures for Effect DecisionModel and Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · doeixd · `TS` · call site [`examples/headline.ts`](https://github.com/doeixd/discern/blob/HEAD/examples/headline.ts), read 2026-09-22</sub>

- **[dsh-jev](https://github.com/buberlo/dsh-jev)** — Jev-powered decision layer for DeepSeek Harness <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · buberlo · `TS` · call site [`packages/dsh-jev/src/config.ts`](https://github.com/buberlo/dsh-jev/blob/HEAD/packages/dsh-jev/src/config.ts), read 2026-09-24 · ⚠ `archived`</sub>

- **[dsh-jev](https://github.com/zhangxaochen/dsh-jev)** — Jev (System One decision model) plugin suite for DeepSeek Harness (dsh) <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · zhangxaochen · `TS` · call site [`lib/typesafe-client.d.ts`](https://github.com/zhangxaochen/dsh-jev/blob/HEAD/lib/typesafe-client.d.ts), read 2026-09-24</sub>

- **[ego-jev](https://github.com/jiangkoumo/ego-decision-layer)** — Drive the ego lite browser with Jev (TypeSafe System One): one indexed element table in, one operation + target out, single process. ~2x faster than a per-step LLM loop in our measurements.
  <sub>`Project` · ★10+ · jiangkoumo · `JS` · call site [`scripts/decider-loop.mjs`](https://github.com/jiangkoumo/ego-decision-layer/blob/HEAD/scripts/decider-loop.mjs), read 2026-09-22</sub>

- **[ego-jev](https://github.com/ZephyrDeng/ego-jev)** — Jev (TypeSafe System One) inner loop for ego-browser — one ~0.4s typed decision per DOM step instead of an LLM turn. Agent skill for ego lite.
  <sub>`Plugin` · ★10+ · zephyrdeng · `JS` · call site [`skills/ego-jev/scripts/jev-loop.ts`](https://github.com/ZephyrDeng/ego-jev/blob/HEAD/skills/ego-jev/scripts/jev-loop.ts), read 2026-09-24</sub>

- **[eutrya](https://github.com/hellozenstrategist-lab/eutrya)** — Jev-native AI security harness for autonomous research, multi-agent swarms, persistent hunt boards, and long-running agent workflows. CLI-first, open source, and built for authorized security research. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · hellozenstrategist-lab · `JS` · call site [`bin/eutrya.mjs`](https://github.com/hellozenstrategist-lab/eutrya/blob/HEAD/bin/eutrya.mjs), read 2026-09-24</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — Software, by reflex. A sentence becomes a call of a small program, chosen by Jev, TypeSafe AI's classifier, and run only when it is sure enough. Reflexes are recipes anyone can write, share and improve. A CLI you talk to, a package manager for reflexes from git, and a TypeScript SDK.
  <sub>`Project` · ★10+ · evoke-build · `Rs` · call site [`crates/evoke-adapters/src/systemone.rs`](https://github.com/evoke-build/evoke/blob/HEAD/crates/evoke-adapters/src/systemone.rs), read 2026-09-24</sub>

- **[Flick](https://github.com/bgivenb/flick-computer-use)** — Local stdio MCP server that runs whole browser and macOS goals: each observe-decide-act step asks Jev a choice over actions keyed by observed element IDs, plus choices for which field and value to fill. Playwright browser driver and a Swift Accessibility driver. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · bgivenb · `TS` · `Swift` · `choice` · `noul` · call site [`src/providers/typesafe.ts`](https://github.com/bgivenb/flick-computer-use/blob/HEAD/src/providers/typesafe.ts), read by a model 2026-10-24</sub>

- **[Harness Router](https://github.com/Protocol-Lattice/harness-router)** — Picks the next tool inside an existing agent loop: given a goal, observation and tool list, Jev returns a tool choice with confidence or a fallback to the host planner. Caches reusable choices, offers optional MCTS, and hooks into Codex and other harnesses or runs as an MCP server. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · protocol-lattice · `Py` · `choice` · call site [`src/harness_router/config.py`](https://github.com/Protocol-Lattice/harness-router/blob/HEAD/src/harness_router/config.py), read by a model 2026-10-24</sub>

- **[hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)** — Autonomous multi-source rental search powered by TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · nancy-chauhan · `JS` · call site [`jev_ultrafast/model.py`](https://github.com/Nancy-Chauhan/hearth-jev-rental-search/blob/HEAD/jev_ultrafast/model.py), read 2026-09-22</sub>

- **[jcr](https://github.com/NiazMorshed2007/jcr)** — A Jev-powered resolver for agent harnesses to find deterministic commands and their context in a nested capability tree. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · niazmorshed2007 · `JS` · call site [`src/jcr/jev.ts`](https://github.com/NiazMorshed2007/jcr/blob/HEAD/src/jcr/jev.ts), read 2026-09-22</sub>

- **[Jev Browser Bridge](https://github.com/lexmount/jev-browser-bridge)** — Runs a Jev browser agent on any CDP browser, even ones that never draw a page: it reads the DOM rather than positions and asks Jev one choice for the operation and one for its target. The author reports 59–65% on 172 MiniWoB++ episodes across six browsers, against 24–31% for a position reader. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · lexmount · `Py` · `choice` · call site [`jev_browser_bridge/model.py`](https://github.com/lexmount/jev-browser-bridge/blob/HEAD/jev_browser_bridge/model.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and safe orchestration. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · forvela · `JS` · call site [`src/decision.js`](https://github.com/forvela/jev-agent-browser/blob/HEAD/src/decision.js), read 2026-09-22</sub>

- **[Jev-as-Policy](https://github.com/YuanKJing/Jev-as-Policy)** — The highly anticipated open-source repository for JEV as Policy enables one-click setup of the simulation environment. Evaluations of Astra + JEV on benchmarks such as RoboTwin will also be released soon. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · yuankjing · `Py` · call site [`jev_policy.py`](https://github.com/YuanKJing/Jev-as-Policy/blob/HEAD/jev_policy.py), read 2026-09-24</sub>

- **[jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm)** — Zero-shot English goals on a sim Franka. Jev chains hardcoded primitives. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · taruntomar122 · `Py` · call site [`jev_robotics/common.py`](https://github.com/TarunTomar122/jev-askable-arm/blob/HEAD/jev_robotics/common.py), read 2026-09-22</sub>

- **[jev-autopilot](https://github.com/arielweinberger/jev-autopilot)** — This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · arielweinberger · `TS` · call site [`server/pilot.ts`](https://github.com/arielweinberger/jev-autopilot/blob/HEAD/server/pilot.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-bot](https://github.com/bl888m/jev-bot)** — JEV-powered market decision bot for stocks, crypto and memes. State in, BUY/SELL/HOLD/AVOID out, paper by default <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · bl888m · `Py` · call site [`jev_bot/jev.py`](https://github.com/bl888m/jev-bot/blob/HEAD/jev_bot/jev.py), read 2026-09-24</sub>

- **[jev-browser](https://github.com/tontoko/jev-browser)** — One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · tontoko · `JS` · call site [`src/decision.ts`](https://github.com/tontoko/jev-browser/blob/HEAD/src/decision.ts), read 2026-09-24</sub>

- **[jev-browser-skill](https://github.com/hqman/jev-browser-skill)** — An isolated Playwright Chromium driven by Jev: a coding agent runs a narrowly scoped browser goal and Jev chooses the in-page actions, through the Vercel AI Gateway by default or TypeSafe's API directly.
  <sub>`Plugin` · ★10+ · hqman · `TS` · call site [`src/jev-model.ts`](https://github.com/hqman/jev-browser-skill/blob/HEAD/src/jev-model.ts), read 2026-09-24</sub>

- **[jev-code](https://github.com/rhighs/jev-code)** — Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · rhighs · `TS` · call site [`src/bash-ast.ts`](https://github.com/rhighs/jev-code/blob/HEAD/src/bash-ast.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-cua](https://github.com/ronadin2002/jev-cua)** — Voice and text control for macOS. One floating bar, live UI action selection with Jev, and a continuous observe–act–verify loop. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ronadin2002 · `Swift` · call site [`Sources/Core.swift`](https://github.com/ronadin2002/jev-cua/blob/HEAD/Sources/Core.swift), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-desktop](https://github.com/yikangy873-gif/jev-desktop)** — TypeSafe Jev action selection inside Codex Computer Use <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · yikangy873-gif · `JS` · call site [`plugins/jev-desktop/scripts/bridge-server.mjs`](https://github.com/yikangy873-gif/jev-desktop/blob/HEAD/plugins/jev-desktop/scripts/bridge-server.mjs), read 2026-09-22</sub>

- **[jev-doom-agent](https://github.com/lukaske/jev-doom-agent)** — A browser-native Doom agent experiment with structured spatial state, composable AI controls, live decision telemetry, and a Chocolate Doom WebAssembly runtime. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · lukaske · `TS` · call site [`server/typesafe.ts`](https://github.com/lukaske/jev-doom-agent/blob/HEAD/server/typesafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-for-chrome](https://github.com/chy4pro/jev-for-chrome)** — Jev for Chrome: drives the tab you are looking at with TypeSafe Jev, a sub-second decision model. Community port of browser-use/jev-ultrafast, not affiliated with TypeSafe. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · chy4pro · `TS` · call site [`src/shared/providers/typesafe.ts`](https://github.com/chy4pro/jev-for-chrome/blob/HEAD/src/shared/providers/typesafe.ts), read 2026-09-22</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · antoniocoppe · `TS` · call site [`demos/proof/row-filter/run.ts`](https://github.com/AntonioCoppe/jev-harness/blob/HEAD/demos/proof/row-filter/run.ts), read 2026-09-22</sub>

- **[jev-harness](https://github.com/TypeSafeAI/jev-harness)** — A custom coding harness for TypeSafe AI's Jev: an LLM proposes, Jev answers narrow questions, code decides, every step leaves a receipt. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · typesafeai · `TS` · call site [`examples/host/jev-choice.ts`](https://github.com/TypeSafeAI/jev-harness/blob/HEAD/examples/host/jev-choice.ts), read 2026-09-24</sub>

- **[jev-kit](https://github.com/jonathanavis96/jev-kit)** — Claude Code kit: a PreToolUse guard where a free pre-filter passes about 93% of tool calls and Jev judges the rest (allow, warn, rewrite or block; fails open), sub-agent sizing, and Jev wired into file search, browsing and review. The author reports 9/9 browser runs at 0.0008 USD of Claude spend. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · jonathanavis96 · `Py` · `choice` · `noul` · call site [`vendor/jev-ultrafast/jev_ultrafast/model.py`](https://github.com/jonathanavis96/jev-kit/blob/HEAD/vendor/jev-ultrafast/jev_ultrafast/model.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · dimweaker · `Py` · call site [`src/jev_libero/client.py`](https://github.com/Dimweaker/jev-libero/blob/HEAD/src/jev_libero/client.py), read 2026-09-22</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Computer-use agent for native macOS apps on Apple silicon: OmniParser CoreML, Apple Vision OCR and accessibility labels find a window's controls locally, and Jev picks the next action with a choice from the observed text, never pixels. Input is guarded, and benchmarks check results, not Jev's DONE. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · jcpsimmons · `JS` · call site [`src/providers.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs), read 2026-09-22</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · parth-kp · `Py` · call site [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py), read 2026-09-22</sub>

- **[jev-mobile](https://github.com/Friedjof/jev-mobile)** — Fast structured Android control loops with TypeSafe Jev and Mobile MCP <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · friedjof · `Py` · call site [`src/jev_mobile/cli.py`](https://github.com/Friedjof/jev-mobile/blob/HEAD/src/jev_mobile/cli.py), read 2026-09-22</sub>

- **[jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)** — Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.
  <sub>`Project` · ★10+ · khordoo · `TS` · call site [`lib/reflex/jev-server.ts`](https://github.com/khordoo/jev-reflex-autonomy-lab/blob/HEAD/lib/reflex/jev-server.ts), read 2026-09-22</sub>

- **[jev-robot-control](https://github.com/openroboto-ai/jev-robot-control)** — Jev against two LLMs on direct Cartesian control of an xArm7 in MuJoCo — intent, movement and gripper each step — with recorded responses, trajectories and replays. One seed-0 trial per controller, not a success rate.
  <sub>`Benchmark` · ★10+ · openroboto-ai · `Py` · call site [`incremental-comparisons/20260919-193012-198478-0/sources/incremental_policy.py`](https://github.com/openroboto-ai/jev-robot-control/blob/HEAD/incremental-comparisons/20260919-193012-198478-0/sources/incremental_policy.py), read 2026-09-24 · author's conclusion: inconclusive (author-stated, not reproduced here) · ⚠ `one commit`</sub>

- **[jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp)** — Hand a whole browser task off in one call: a decision model drives the page server-side, so a flow costs one call, not a turn per click. Ref-based element tables, code-checked assertions, zero-model macro replay, over the Chrome DevTools Protocol. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · jiawei686 · `Py` · call site [`jev_ultrafast_mcp/config.py`](https://github.com/jiawei686/jev-ultrafast-mcp/blob/HEAD/jev_ultrafast_mcp/config.py), read 2026-09-24</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — An agent plugin that hands steps needing no text output to Jev instead of the main model.
  <sub>`Plugin` · ★10+ · shitianfang · `JS` · call site [`src/backends/typesafe.ts`](https://github.com/shitianfang/jev-use/blob/HEAD/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kenhuangus · `Py` · call site [`src/jev_usecases/client.py`](https://github.com/kenhuangus/jev-usecases/blob/HEAD/src/jev_usecases/client.py), read 2026-09-22</sub>

- **[Jev_Star](https://github.com/sc2musa/Jev_Star)** — StarCraft II macro and micro with Jev selecting actions and optional LLM planning, with a paper and full recorded winning games.
  <sub>`Project` · ★10+ · sc2musa · `Py` · call site [`macro/sc2_rl_agent/starcraftenv_test/agent/jev_agent.py`](https://github.com/sc2musa/Jev_Star/blob/HEAD/macro/sc2_rl_agent/starcraftenv_test/agent/jev_agent.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ray-hughes · `Rb` · call site [`lib/jevalyn/configuration.rb`](https://github.com/Ray-Hughes/jevalyn/blob/HEAD/lib/jevalyn/configuration.rb), read 2026-09-22</sub>

- **[Jevbridge](https://github.com/tacticocc/Jevbridge)** — ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · gamesonrblx · `TS` · call site [`src/types.ts`](https://github.com/tacticocc/Jevbridge/blob/HEAD/src/types.ts), read 2026-09-24</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — A chatbot built on a model that cannot generate text (TypeSafe AI's Jev, driven autoregressively) <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · bewinxed · `TS` · call site [`src/jevgpt/sampler.py`](https://github.com/Bewinxed/jevgpt/blob/HEAD/src/jevgpt/sampler.py), read 2026-09-22</sub>

- **[jevloop](https://github.com/parkavenue9639/jevloop)** — A Jev-driven general-purpose agent harness for faster, lower-cost execution, with built-in side-by-side experiments against LLM-only agents. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · parkavenue9639 · `Py` · call site [`backend/jevloop/decision/model.py`](https://github.com/parkavenue9639/jevloop/blob/HEAD/backend/jevloop/decision/model.py), read 2026-09-24</sub>

- **[jevscape](https://github.com/Skyvern-AI/jevscape)** — RuneBench harness for TypeSafe's Jev: bounded action catalog, tick-mode controller and a live dashboard <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · skyvern-ai · `TS` · call site [`agents/jev/jev-client.ts`](https://github.com/Skyvern-AI/jevscape/blob/HEAD/agents/jev/jev-client.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[JevScout](https://github.com/hqman/JevScout)** — A coding-agent skill that hunts jobs on real company sites: Chrome sees and acts, Jev scores every link and posting, and the host LLM never picks what to click.
  <sub>`Plugin` · ★10+ · hqman · `Py` · call site [`jev_job_hunter/jev.py`](https://github.com/hqman/JevScout/blob/HEAD/jev_job_hunter/jev.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent)** — Local, open-source Jev alternative: browser agent decisions with Laya (System One model) on your own machine. No cloud, no API key. Playwright/CDP, MCP-friendly. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · chenneyzhuang · `Py` · cited file [`examples/diagnostics/jev_flow_h2h.py`](https://github.com/ChenneyZhuang/laya-browser-agent/blob/HEAD/examples/diagnostics/jev_flow_h2h.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[laya-jev-GraphRAG](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG)** — Agentic GraphRAG engine using swappable System One decision models (local Laya / cloud Jev). Features a complete 4-phase pipeline (Ingestion, Pre-Retrieval, Traversal, Post-Retrieval) and evaluation across Neo4j, Memgraph, Apache AGE, and Kùzu driven by a custom A* traversal algorithm.
  <sub>`Project` · ★10+ · bodepudimuneendra-netizen · `Py` · call site [`graphrag_neo4j_laya/graphrag/models/jev.py`](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG/blob/HEAD/graphrag_neo4j_laya/graphrag/models/jev.py), read 2026-09-24</sub>

- **[live-jev](https://github.com/vinilana/live-jev)** — 2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · vinilana · `JS` · call site [`server.js`](https://github.com/vinilana/live-jev/blob/HEAD/server.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[live-jev](https://github.com/okinaaudio/live-jev)** — Control Ableton Live with one short sentence (Japanese / English). Summon with ⌘⇧Space, type or dictate, done. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · okinaaudio · `Py` · call site [`daemon.py`](https://github.com/okinaaudio/live-jev/blob/HEAD/daemon.py), read 2026-09-24</sub>

- **[mario-jev](https://github.com/shantanugoel/mario-jev)** — A prototype that plays Super Mario Bros.: Jev reads structured RAM observations and answers focused questions about moving and jumping, and code turns the answers into controller buttons.
  <sub>`Project` · ★10+ · shantanugoel · `Py` · call site [`src/mario_jev/policy.py`](https://github.com/shantanugoel/mario-jev/blob/HEAD/src/mario_jev/policy.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[OmniJev](https://github.com/shapsider/OmniJev)** — OmniJev — multimodal finite-choice decision interface and MuJoCo embodied workbench: trajectory replays, decision probes, benchmark panels, 60s walkthrough. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · shapsider · `Py` · call site [`embodied/src/embodied_jev/policies.py`](https://github.com/shapsider/OmniJev/blob/HEAD/embodied/src/embodied_jev/policies.py), read 2026-09-24</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — A browser 1v1 FPS where every decision tick judges movement, view angle, aim, fire and jump.
  <sub>`Project` · ★10+ · `TS` · `choice` · call site [`server/src/jev.ts`](https://github.com/emrickgarrett/OneVOneJev/blob/HEAD/server/src/jev.ts), read 2026-09-22 · ⚠ `code untested` `no licence`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · nyarlathoteppppp · `TS` · call site [`bench/jev-lab.ts`](https://github.com/Nyarlathoteppppp/pi-heed/blob/HEAD/bench/jev-lab.ts), read 2026-09-22</sub>

- **[pi-jev](https://github.com/TheoOliveira/pi-jev)** — Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · theooliveira · `TS` · call site [`src/jev.ts`](https://github.com/TheoOliveira/pi-jev/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode)** — Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jomatsu · `TS` · call site [`src/jev/transport.ts`](https://github.com/jomatsu/pi-jev-auto-mode/blob/HEAD/src/jev/transport.ts), read 2026-09-22</sub>

- **[playjev](https://github.com/filedcom/playjev)** — Fast, typed browser automation powered by Jev and Playwright <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · filedcom · `TS` · call site [`src/jev/client.ts`](https://github.com/filedcom/playjev/blob/HEAD/src/jev/client.ts), read 2026-09-24</sub>

- **[public-browser](https://github.com/Silbercue/public-browser)** — Lets Claude Code and Cursor drive Chrome. Browse your real profile: -30% tokens, -25% cost, -41% tool calls, -34% tool defs, +40% faster. Direct CDP, a11y-tree refs, server-side plan executor. MIT, no paid tier.
  <sub>`Plugin` · ★10+ · silbercue · `TS` · call site [`examples/jev-loop.mjs`](https://github.com/Silbercue/public-browser/blob/HEAD/examples/jev-loop.mjs), read 2026-09-24 · ⚠ `unverified claims`</sub>

- **[robojev](https://github.com/lykycy123/RoboJEV)** — Two-stage JEV control of a Franka Panda in MuJoCo <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · lykycy123 · `Py` · call site [`src/jev_vla_sim/config.py`](https://github.com/lykycy123/RoboJEV/blob/HEAD/src/jev_vla_sim/config.py), read 2026-09-22</sub>

- **[Sedum (npm: sedum-cli)](https://github.com/sedum-dev/sedum)** — Plain-English browser end-to-end tests next to Playwright code. In goal mode a Jev Choice picks each next operation (click, type, done or blocked) and its target; authored steps use a Choice per sentence; each verify claim is two Nouls (holds, contradicted). Playwright acts; code applies thresholds.
  <sub>`Project` · ★10+ · sedum-dev · `TS` · `choice` · `noul` · call site [`packages/provider-typesafe/src/index.ts`](https://github.com/sedum-dev/sedum/blob/HEAD/packages/provider-typesafe/src/index.ts), read 2026-09-30 · ⚠ `unverified claims` `self-submitted`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · myc0576 · `Py` · call site [`src/smartmoney_cub_harness/jev/direct.py`](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[super-jev](https://github.com/Kevthetech143/super-jev)** — A small, extensible decision-to-action harness for TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kevthetech143 · `Py` · call site [`skills/super-jev/superjev.py`](https://github.com/Kevthetech143/super-jev/blob/HEAD/skills/super-jev/superjev.py), read 2026-09-22</sub>

- **[tsai-sc](https://github.com/phyous/tsai-sc)** — Drives a 1990s real-time strategy game through keyboard and mouse, recording the action probabilities.
  <sub>`Project` · ★10+ · phyous · `Py` · call site [`tsai_sc/typesafe.py`](https://github.com/phyous/tsai-sc/blob/HEAD/tsai_sc/typesafe.py), read 2026-09-22</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — Screen a folder of CVs with the TypeSafe Jev decision model: typed judgments, an editable policy, free re-scoring. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · gtaras7 · `TS` · call site [`cv-screen/src/cli.ts`](https://github.com/gtaras7/typesafe-jev/blob/HEAD/cv-screen/src/cli.ts), read 2026-09-22</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — A WebMCP benchmark, measures WebMCP against other browser-agent interfaces. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · nekuda-ai · `TS` · call site [`experiments/jev/frozen/arms/decision-providers.mjs`](https://github.com/nekuda-ai/WindTunnel/blob/HEAD/experiments/jev/frozen/arms/decision-providers.mjs), read 2026-09-22</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server: a decision layer for coding agents, built on TypeSafe Jev (System One model). Ship gates, risk checks, file triage that keeps files out of context, and a safe headless browser, with calibrated confidence. For Claude Code, Codex, Cursor. <sub>(upstream description)</sub>
  <sub>`Plugin` · abhishekswe · `TS` · call site [`packages/provider-typesafe/src/client.ts`](https://github.com/abhishekswe/agent-fastpath/blob/HEAD/packages/provider-typesafe/src/client.ts), read 2026-09-22</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — AGI JEV Detection — local AI agent monitor: chain-level malicious-agent detection (TypeSafe Jev + Sentinel), escalate-only L1–L5 containment, Neo4j forensics, AngryRobot dashboard. HackSpain 2026. <sub>(upstream description)</sub>
  <sub>`Project` · carlosedm10 · `Py` · call site [`backend/app/classification/jev.py`](https://github.com/carlosedm10/agi-jev-containment/blob/HEAD/backend/app/classification/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[arc-cua](https://github.com/shhivv/arc-cua)** — macOS action loop for computer-use agents: a planner hands off a bounded desktop subtask, and Jev picks each next UI operation and target from what the window exposes, as `choice` questions, with one more `choice` per success criterion; literal text only ever comes from the planner. <sub>(written by a model)</sub>
  <sub>`Project` · shhivv · `Py` · `choice` · call site [`src/arc_cua/policies/typesafe.py`](https://github.com/shhivv/arc-cua/blob/HEAD/src/arc_cua/policies/typesafe.py), read by a model 2026-10-29</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime. <sub>(upstream description)</sub>
  <sub>`SDK` · himomohi · `Py` · call site [`src/aside_jev/jev.py`](https://github.com/himomohi/aside-jev/blob/HEAD/src/aside_jev/jev.py), read 2026-09-22</sub>

- **[AskJev](https://github.com/ranjan2829/AskJev)** — AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude) <sub>(upstream description)</sub>
  <sub>`Project` · ranjan2829 · `TS` · call site [`mcp/src/jev-client.ts`](https://github.com/ranjan2829/AskJev/blob/HEAD/mcp/src/jev-client.ts), read 2026-09-24</sub>

- **[bicameral](https://github.com/AbdelStark/bicameral)** — Hybrid coding harness: System 2 writes, System 1 (Jev) runs reflexes. <sub>(upstream description)</sub>
  <sub>`Project` · abdelstark · `TS` · call site [`packages/s1-runtime/src/backends/typesafe.ts`](https://github.com/AbdelStark/bicameral/blob/HEAD/packages/s1-runtime/src/backends/typesafe.ts), read 2026-09-22</sub>

- **[browser-use-olympics](https://github.com/eriestra/browser-use-olympics)** — Browser Use Olympics by Almond: one prompt, five events, one clock. Plus fast loop, a ~200-line browser computer-use agent (Chrome DevTools + TypeSafe Jev). <sub>(upstream description)</sub>
  <sub>`Project` · eriestra · `TS` · call site [`almond-fastloop.mjs`](https://github.com/eriestra/browser-use-olympics/blob/HEAD/almond-fastloop.mjs), read 2026-09-22</sub>

- **[casse-brique-typesafe](https://github.com/Para-FR/casse-brique-typesafe)** — A Next.js brick breaker whose paddle is controlled in real time by TypeSafe AI's Jev model. Built with Claude Code. <sub>(upstream description)</sub>
  <sub>`Plugin` · para-fr · `TS` · call site [`src/app/api/paddle/route.ts`](https://github.com/Para-FR/casse-brique-typesafe/blob/HEAD/src/app/api/paddle/route.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[computer-use-jev](https://github.com/paulsmith/computer-use-jev)** — macOS computer use driven by Jev (TypeSafe System One) as the decision maker <sub>(upstream description)</sub>
  <sub>`Project` · paulsmith · `Go` · call site [`typesafe/client.go`](https://github.com/paulsmith/computer-use-jev/blob/HEAD/typesafe/client.go), read 2026-09-22</sub>

- **[deepseek-harness-jev (luobosibing2)](https://github.com/luobosibing2/dsh-jev-plugin)** — DeepSeek Harness plugin with twelve opt-in features using Jev as the judgment model: skill selection and glob-result ranking (one `noul` per candidate), completion and goal checks, drift reminders, interjection routing, tool-output and test-log filtering, and approval of single workspace operations. <sub>(written by a model)</sub>
  <sub>`Plugin` · luobosibing2 · `TS` · `noul` · call site [`packages/jev/src/selection.ts`](https://github.com/luobosibing2/dsh-jev-plugin/blob/HEAD/packages/jev/src/selection.ts), read by a model 2026-10-28</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — A pre-compaction advisor for DeepSeek Harness. Runs before the standard `compaction-basic` backend, using TypeSafe JEV to safely prune low-value tool results from model context. Original session events stay in the append-only log; only the model-visible view is replaced with compact markers or
  <sub>`Project` · wjw66 · `TS` · call site [`src/jev/protocol.ts`](https://github.com/wjw66/deepseek-harness-jev-pre-compaction/blob/HEAD/src/jev/protocol.ts), read 2026-09-22</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — Jev-judged context compaction for DeepSeek Harness: semantic tool-result pruning + deterministic receipt compaction <sub>(upstream description)</sub>
  <sub>`Project` · yangyu666 · `JS` · call site [`src/jev.js`](https://github.com/yangyu666/dsh-jev-prune/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design. <sub>(earlier upstream description)</sub>
  <sub>`Benchmark` · xienda · `JS` · call site [`lib/index.js`](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev drives your Ego Lite browser: one typed-choice request per step. Single-file, zero-dependency port of browser-use/jev-ultrafast with multi-model benchmarks and extra guardrails. Unofficial. <sub>(upstream description)</sub>
  <sub>`Benchmark` · shikaizhong-design · `JS` · call site [`jego.js`](https://github.com/shikaizhong-design/ego-jev-ultrafast/blob/HEAD/jego.js), read 2026-09-22</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — Asks for an operation plus a target for each operation it might have picked, so a browser step never needs a second round trip.
  <sub>`Snippet` · `Py` · `choice` · `noul` · call site [`examples/03-fan-out/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/03-fan-out/main.py), read 2026-09-22 · ⚠ `code untested`</sub>

- **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)** — Pairs a choice over tools with a separate noul on whether a tool is needed at all, because those are different questions.
  <sub>`Snippet` · `Py` · `choice` · `noul` · call site [`examples/04-tool-selection/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/04-tool-selection/main.py), read 2026-09-22 · ⚠ `code untested`</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM summaries with fast keep/truncate/drop decisions from jev-latest; everything kept stays verbatim. Port of tamaratran/fast-jev-compaction. <sub>(upstream description)</sub>
  <sub>`Project` · kolawong · `TS` · call site [`src/jev.ts`](https://github.com/kolawong/fast-compaction-dsh/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[gg-friggin-ez](https://github.com/ItisShikhar/gg-friggin-ez)** — Fast, drop-in multilingual profanity and toxicity screener for Node.js, powered by System 1 models like TypeSafe AI Jev and Laya. Catches leetspeak, character spacing, and romanized profanity across languages including Kannada, Telugu, Tamil, Hindi, and Bengali. ~50-500ms latency. <sub>(upstream description)</sub>
  <sub>`Project` · itisshikhar · `TS` · call site [`demo/js/models.js`](https://github.com/ItisShikhar/gg-friggin-ez/blob/HEAD/demo/js/models.js), read 2026-09-22</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — Web app for agent builders: paste the trace of one agent step and Jev judges it as ok, retry, escalate or stop. Without a TYPESAFE_API_KEY, local heuristics return answers of the same shape, labelled as demo mode. <sub>(written by a model)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/harnessjudge/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world. <sub>(upstream description)</sub>
  <sub>`Project` · abdelstark · `TS` · call site [`apps/server/src/jev.ts`](https://github.com/AbdelStark/heist-one/blob/HEAD/apps/server/src/jev.ts), read 2026-09-22</sub>

- **[jet](https://github.com/arczhi/jet)** — A TypeSafe-native (Jev) coding agent built on Recursive LLM Context Decomposition (RLCD), with a native macOS client <sub>(upstream description)</sub>
  <sub>`Project` · arczhi · `Py` · call site [`src/jet/providers/typesafe_judge.py`](https://github.com/arczhi/jet/blob/HEAD/src/jet/providers/typesafe_judge.py), read 2026-09-24</sub>

- **[Jev Civilizations](https://github.com/JonesSteven/jev_civilization)** — Small strategy game with a live demo: four tribes run their own lives while you only change the environment. Each turn Jev picks one action per tribe as a choice over the moves that are actually legal, a plain game engine works out the results, and an inspector shows what Jev was told. <sub>(written by a model)</sub>
  <sub>`Project` · jonessteven · `TS` · `choice` · call site [`scripts/probe-jev.ts`](https://github.com/JonesSteven/jev_civilization/blob/HEAD/scripts/probe-jev.ts), read by a model 2026-10-24</sub>

- **[Jev GUI Delegate](https://github.com/YUTA-fywoo/jev-gui-delegate)** — Windows and Chrome GUI delegation prototype for Codex: a local controller runs a task contract step by step, and when a control must be picked by meaning it asks Jev one `choice` over the observed controls plus no_match, wait, reobserve and ask_astra exits, then checks the result. <sub>(written by a model)</sub>
  <sub>`Project` · YUTA-fywoo · `Py` · `choice` · call site [`gui_delegate/controller.py`](https://github.com/YUTA-fywoo/jev-gui-delegate/blob/HEAD/gui_delegate/controller.py), read by a model 2026-10-29 · ⚠ `no licence` `vendor numbers`</sub>

- **[jev-A-share-trader](https://github.com/Eric-Zhou-0302/jev-A-share-trader)** — A Jev-powered technical analysis workspace for China A-shares, supporting AKShare/Tushare, market scans, and Buy/Hold/Sell assessments with time horizons and traceable evidence. <sub>(upstream description)</sub>
  <sub>`Project` · eric-zhou-0302 · `Py` · call site [`src/jev_trader/jev.py`](https://github.com/Eric-Zhou-0302/jev-A-share-trader/blob/HEAD/src/jev_trader/jev.py), read 2026-09-24</sub>

- **[jev-agent-design-with-topk-logits-choices](https://github.com/6Mikao9/jev-native-agent-with-extended-options)** — Research design for a Jev-native agent system: tool integration, speculative parameter proposals, external helper logits Top-k proposals with Jev-controlled fallback ,decision-aware hierarchical memory…
  <sub>`Project` · 6mikao9 · `Py` · call site [`benchmarks/benchmark_jev_latency_breakdown.py`](https://github.com/6Mikao9/jev-native-agent-with-extended-options/blob/HEAD/benchmarks/benchmark_jev_latency_breakdown.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能 <sub>(upstream description)</sub>
  <sub>`Plugin` · yuyang2230 · `Py` · call site [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py), read 2026-09-22</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verification. <sub>(upstream description)</sub>
  <sub>`Project` · rinnecoder · `Py` · call site [`behavior_study.py`](https://github.com/RINNECODER/jev-behavior-study/blob/HEAD/behavior_study.py), read 2026-09-22</sub>

- **[jev-browse](https://github.com/danielnc/jev-browse)** — Helpers for browser-harness that let Claude Code or Codex hand off a whole website sub-task in one fast_run call, with each step decided by Jev and a typed reason returned when it must stop. A port of browser-use/jev-ultrafast; the author reports 1.6–3.0x faster and 2.1–5.3x cheaper runs. <sub>(written by a model)</sub>
  <sub>`Project` · danielnc · `Py` · call site [`jev_browse/config.py`](https://github.com/danielnc/jev-browse/blob/HEAD/jev_browse/config.py), read by a model 2026-10-24 · ⚠ `vendor numbers`</sub>

- **[jev-browse](https://github.com/0x7067/jev-browse)** — Browser automation with Jev (TypeSafe) as decision model <sub>(upstream description)</sub>
  <sub>`Project` · 0x7067 · `JS` · call site [`bundled/cli.mjs`](https://github.com/0x7067/jev-browse/blob/HEAD/bundled/cli.mjs), read 2026-09-24</sub>

- **[jev-browse](https://github.com/kyrylosyzonenko/jev-browse)** — Drives a real browser with Jev making every decision — each click, which of your texts goes in which box, and when the goal is reached — while agent-browser performs the actions.
  <sub>`Project` · kyrylosyzonenko · `JS` · call site [`jev-browse.mjs`](https://github.com/kyrylosyzonenko/jev-browse/blob/HEAD/jev-browse.mjs), read 2026-09-24</sub>

- **[jev-browser](https://github.com/KesavanKing/jev-browser)** — Local browser automation UI that uses TypeSafe Jev to choose bounded page actions and a text model only for field values. <sub>(upstream description)</sub>
  <sub>`Project` · kesavanking · `Py` · call site [`jev_browser/model.py`](https://github.com/KesavanKing/jev-browser/blob/HEAD/jev_browser/model.py), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[jev-browser](https://github.com/MahmoudAdelbghany/jev-browser)** — Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included. <sub>(upstream description)</sub>
  <sub>`Plugin` · mahmoudadelbghany · `JS` · call site [`src/jev.mjs`](https://github.com/MahmoudAdelbghany/jev-browser/blob/HEAD/src/jev.mjs), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-browser](https://github.com/openqa-cn/jev-browser)** — Jev Browser — indexed browser automation. Jev chooses the control, Playwright acts. A CodexQA skill. <sub>(upstream description)</sub>
  <sub>`Plugin` · openqa-cn · `TS` · call site [`src/jev.ts`](https://github.com/openqa-cn/jev-browser/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[jev-browser](https://github.com/vinilana/jev-browser)** — A hybrid browser harness: an OpenRouter LLM turns goals into verifiable subgoals, Jev chooses each action and form field, the LLM writes text only when a field needs it, and Playwright acts.
  <sub>`Project` · vinilana · `TS` · call site [`src/infrastructure/models/jev.ts`](https://github.com/vinilana/jev-browser/blob/HEAD/src/infrastructure/models/jev.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-browser-control](https://github.com/nexibeo/jev-browser-control)** — Let Claude code, chatgpt codex or control your own Chrome. Chrome extension + MCP server: Jev, TypeSafe's decision model, picks each click in ~0.5 s for a fraction of a cent. MIT, bring your own OpenRouter key. <sub>(upstream description)</sub>
  <sub>`Plugin` · nexibeo · `JS` · call site [`extension/lib/provider.js`](https://github.com/nexibeo/jev-browser-control/blob/HEAD/extension/lib/provider.js), read 2026-09-22</sub>

- **[jev-browser-local](https://github.com/rorshopping/jev-browser-local)** — Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard, measured benchmarks, run traces. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · rorshopping · `Py` · cited file [`jev-browser-fork/dist/provider.js`](https://github.com/rorshopping/jev-browser-local/blob/HEAD/jev-browser-fork/dist/provider.js), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification. <sub>(upstream description)</sub>
  <sub>`Project` · aidil2105 · `Py` · call site [`src/jev_pilot/providers/jev.py`](https://github.com/aidil2105/jev-browser-pilot/blob/HEAD/src/jev_pilot/providers/jev.py), read 2026-09-22</sub>

- **[jev-browser-skill](https://github.com/zurfyx/jev-browser-skill)** — Let Jev, TypeSafe's ~100ms decision model, drive your browser. A plug-and-play skill for Claude Code and Codex. <sub>(upstream description)</sub>
  <sub>`Plugin` · zurfyx · `JS` · call site [`scripts/jev.mjs`](https://github.com/zurfyx/jev-browser-skill/blob/HEAD/scripts/jev.mjs), read 2026-09-22</sub>

- **[jev-browser-skill](https://github.com/ChenYCL/jev-browser-skill)** — Browser use & computer use for coding agents, powered by TypeSafe Jev: calibrated judgments from a System One model, control loop in code. ego lite / Chrome / Safari · CLI + MCP <sub>(upstream description)</sub>
  <sub>`Plugin` · chenycl · `JS` · call site [`skills/jev-browser/lib/typesafe.mjs`](https://github.com/ChenYCL/jev-browser-skill/blob/HEAD/skills/jev-browser/lib/typesafe.mjs), read 2026-09-24</sub>

- **[jev-builder](https://github.com/collapseindex/jev-builder)** — A browser form for building requests to TypeSafe's Jev: pick a template, fill in the blanks, copy the request. No JSON, no install, runs locally. <sub>(upstream description)</sub>
  <sub>`Project` · collapseindex · `JS` · call site [`jev-builder-core.js`](https://github.com/collapseindex/jev-builder/blob/HEAD/jev-builder-core.js), read 2026-09-22</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · nikkoxgonzales · `Py` · call site [`jev_certify/analysis.py`](https://github.com/nikkoxgonzales/jev-certify/blob/HEAD/jev_certify/analysis.py), read 2026-09-22</sub>

- **[jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** — Smart Codex overlay with JEV model routing, context optimization & Kanban automation. Reduce tokens, keep control
  <sub>`Plugin` · charlyhno-eng · `TS` · `choice` · `score` · `noul` · call site [`src/core/hooks/jev-client.ts`](https://github.com/Charlyhno-eng/jev-codex-pilot/blob/HEAD/src/core/hooks/jev-client.ts), read 2026-09-24</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — Context compaction for Hermes sessions that never summarises: every tool call is scored by TypeSafe's Jev model, stale calls are dropped, everything kept stays verbatim. <sub>(upstream description)</sub>
  <sub>`Project` · picaye · `JS` · call site [`hermes-compact.mjs`](https://github.com/picaye/jev-compaction/blob/HEAD/hermes-compact.mjs), read 2026-09-22</sub>

- **[jev-connect4](https://github.com/hazlema/jev-connect4)** — Connect 4, Jev vs. Human or Jev vs. Jev <sub>(upstream description)</sub>
  <sub>`Project` · hazlema · `TS` · call site [`src/jev-client.ts`](https://github.com/hazlema/jev-connect4/blob/HEAD/src/jev-client.ts), read 2026-09-24</sub>

- **[jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks)** — JEV decision benchmark results on MetaTool, When2Call, and BFCL V4, with bilingual tables and reproducible reports. <sub>(upstream description)</sub>
  <sub>`Benchmark` · baibizhe · `Py` · call site [`scripts/build_tables.py`](https://github.com/baibizhe/jev-decision-benchmarks/blob/HEAD/scripts/build_tables.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-flappy-bird](https://github.com/hosseintoussi/jev-flappy-bird)** — A live demo of TypeSafe's Jev model playing Flappy Bird, one flap-or-wait decision at a time. <sub>(upstream description)</sub>
  <sub>`Project` · hosseintoussi · `TS` · call site [`server/jev.ts`](https://github.com/hosseintoussi/jev-flappy-bird/blob/HEAD/server/jev.ts), read 2026-09-24</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies. <sub>(upstream description)</sub>
  <sub>`Project` · foadsf · `Py` · call site [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/HEAD/jev.py), read 2026-09-22</sub>

- **[jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa)** — Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo. <sub>(upstream description)</sub>
  <sub>`Project` · nainish-rai · `Py` · call site [`src/jev_frontend_qa/core/model_client.py`](https://github.com/Nainish-Rai/jev-frontend-qa/blob/HEAD/src/jev_frontend_qa/core/model_client.py), read 2026-09-22</sub>

- **[jev-harness-router](https://github.com/JoacoMarc/jev-harness-router)** — Per-turn router for agent harnesses: one 350ms Jev call picks the model tier, effort, tools and skill, behind a hard deadline with a regex fallback. Claude Agent SDK adapter included. <sub>(upstream description)</sub>
  <sub>`SDK` · joacomarc · `TS` · call site [`src/jev.ts`](https://github.com/JoacoMarc/jev-harness-router/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[jev-in-codex](https://github.com/teempai/jev-in-codex)** — Jev-powered tool and skill selection, context search, and output triage for Codex via MCP <sub>(upstream description)</sub>
  <sub>`Plugin` · teempai · `TS` · call site [`src/labelling.ts`](https://github.com/teempai/jev-in-codex/blob/HEAD/src/labelling.ts), read 2026-09-24</sub>

- **[jev-lab](https://github.com/jammaru/jev-lab)** — 100 AI NPCs live in a tiny town. Jev chooses the next action; the world writes the story. <sub>(upstream description)</sub>
  <sub>`Project` · jammaru · `TS` · call site [`apps/shogi-server/src/jev.ts`](https://github.com/jammaru/jev-lab/blob/HEAD/apps/shogi-server/src/jev.ts), read 2026-09-22</sub>

- **[jev-layer](https://github.com/typakon4/jev-layer)** — Portable System-1 decision layer for agent harnesses with host-owned routing, receipts, replay, and fail-open integrations. <sub>(upstream description)</sub>
  <sub>`Integration` · typakon4 · `JS` · call site [`src/providers/typesafe.mjs`](https://github.com/typakon4/jev-layer/blob/HEAD/src/providers/typesafe.mjs), read 2026-09-22</sub>

- **[jev-life](https://github.com/ARCJ137442/jev-life)** — The Chess of Life × Jev — an experimental game: write a new ruleset, then watch a decision model play it. \| 生命棋 × Jev：实验性游戏设计——写一套新规则，然后看 Jev 怎么玩 <sub>(upstream description)</sub>
  <sub>`Project` · arcj137442 · `TS` · call site [`src/client/api.ts`](https://github.com/ARCJ137442/jev-life/blob/HEAD/src/client/api.ts), read 2026-09-24</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — Benchmark-driven Jev router and judge for cost-aware, reliable LLM coding workflows <sub>(upstream description)</sub>
  <sub>`Benchmark` · erendikmenn · `Py` · call site [`src/jev_router/providers/review.py`](https://github.com/erendikmenn/jev-llm-router-benchmark/blob/HEAD/src/jev_router/providers/review.py), read 2026-09-22</sub>

- **[jev-market-reflex](https://github.com/zzsong1023/jev-market-reflex)** — Fast typed AI decisions on live crypto markets using TypeSafe AI Jev. <sub>(upstream description)</sub>
  <sub>`Project` · zzsong1023 · `TS` · call site [`src/jev.ts`](https://github.com/zzsong1023/jev-market-reflex/blob/HEAD/src/jev.ts), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-mobile](https://github.com/xinwang-nwpu/jev-mobile)** — One TypeSafe Jev decision per step over the A11Y tree, executed via ADB. No screenshots and ultra fast! <sub>(upstream description)</sub>
  <sub>`Project` · xinwang-nwpu · `Py` · call site [`jev_mobile/model.py`](https://github.com/xinwang-nwpu/jev-mobile/blob/HEAD/jev_mobile/model.py), read 2026-09-24</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — An OpenAI-compatible proxy that sits between your LLM and your users. It evaluates each sliding window of tokens while the response is still streaming and cuts the stream before a violating token can reach the screen. <sub>(upstream description)</sub>
  <sub>`Project` · thanh-mathieu95 · `JS` · call site [`evaluator.js`](https://github.com/Thanh-Mathieu95/jev-model-tokengate/blob/HEAD/evaluator.js), read 2026-09-22</sub>

- **[jev-physical-ai](https://github.com/robokrunch/jev-physical-ai)** — Putting TypeSafe's Jev to work on robots, fleets, and edge hardware — real measured numbers, honestly caveated. <sub>(upstream description)</sub>
  <sub>`Project` · robokrunch · `Py` · call site [`code/demo-a.py`](https://github.com/robokrunch/jev-physical-ai/blob/HEAD/code/demo-a.py), read 2026-09-22</sub>

- **[jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong)** — Jev plays browser table tennis in real time: structured telemetry, typed decisions, ordinary Chrome inputs, and auditable evidence. <sub>(upstream description)</sub>
  <sub>`Benchmark` · icohen007 · `JS` · call site [`src/typesafe.mjs`](https://github.com/Icohen007/jev-play-ping-pong/blob/HEAD/src/typesafe.mjs), read 2026-09-22</sub>

- **[jev-playground](https://github.com/hegargarcia/jev-playground)** — Benchmarks Jev against other evaluation models in games with explicit states and legal actions: code owns the rules and transitions, each model picks the next action, and outcomes are measured.
  <sub>`Benchmark` · hegargarcia · `TS` · call site [`src/app/api/connect-four/move/route.ts`](https://github.com/hegargarcia/jev-playground/blob/HEAD/src/app/api/connect-four/move/route.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-plays](https://github.com/mansicer/jev-plays)** — A System One model plays Craftax while an LLM sets the goals: five agents on the same map, from Jev on raw actions to an LLM controlling every step, compared in logged episodes.
  <sub>`Benchmark` · mansicer · `Py` · call site [`craftax_agent/jev_policy.py`](https://github.com/mansicer/jev-plays/blob/HEAD/craftax_agent/jev_policy.py), read 2026-09-24</sub>

- **[jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red)** — Pokemon Red on PyBoy: code owns the route and the arithmetic, Jev picks at branches in about 100 ms, calibration measured instead of assumed <sub>(upstream description)</sub>
  <sub>`Project` · valentynkit · `Py` · call site [`src/jpp/policy.py`](https://github.com/valentynkit/jev-plays-pokemon-red/blob/HEAD/src/jpp/policy.py), read 2026-09-24</sub>

- **[jev-pong](https://github.com/ably-labs/jev-pong)** — Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and agent on an Ably channel. <sub>(upstream description)</sub>
  <sub>`Project` · ably-labs · `TS` · call site [`lib/compare/compare-models.ts`](https://github.com/ably-labs/jev-pong/blob/HEAD/lib/compare/compare-models.ts), read 2026-09-24</sub>

- **[jev-ra](https://github.com/brnyxx/jev-ra)** — Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms. <sub>(upstream description)</sub>
  <sub>`Plugin` · brnyxx · `Py` · call site [`jev_ra/config.py`](https://github.com/brnyxx/jev-ra/blob/HEAD/jev_ra/config.py), read 2026-09-22</sub>

- **[jev-robotics-demo](https://github.com/FazalAAli/jev-robotics-demo)** — Jev (TypeSafe System One) vs Claude Opus 5 driving a simulated robot arm in MuJoCo <sub>(upstream description)</sub>
  <sub>`Project` · fazalaali · `Py` · call site [`jev_agent.py`](https://github.com/FazalAAli/jev-robotics-demo/blob/HEAD/jev_agent.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-routing](https://github.com/nekowasabi/jev-routing)** — Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server. <sub>(upstream description)</sub>
  <sub>`Plugin` · nekowasabi · `Go` · call site [`internal/jev/jev.go`](https://github.com/nekowasabi/jev-routing/blob/HEAD/internal/jev/jev.go), read 2026-09-22 · ⚠ `archived`</sub>

- **[jev-skill-router](https://github.com/himomohi/jev-skill-router)** — Keep skill catalogs outside the main LLM context. Jev selects relevant skills through one read-only MCP tool. <sub>(upstream description)</sub>
  <sub>`Plugin` · himomohi · `Py` · call site [`src/jev_skill_router/jev.py`](https://github.com/himomohi/jev-skill-router/blob/HEAD/src/jev_skill_router/jev.py), read 2026-09-24</sub>

- **[jev-skill-scout](https://github.com/karanb192/jev-skill-scout)** — Finds the turns where Claude Code should have loaded one of your skills and did not, judged by TypeSafe's Jev. Audit CLI plus the mod that fixes it live. <sub>(upstream description)</sub>
  <sub>`Project` · karanb192 · `JS` · call site [`lib/scout.js`](https://github.com/karanb192/jev-skill-scout/blob/HEAD/lib/scout.js), read 2026-09-24</sub>

- **[jev-skills](https://github.com/eran-broder/jev-skills)** — Skills without the context tax. Claude Code and Codex plugin: TypeSafe's Jev decides on every turn which skills the model sees. Always-on context cost: 0 tokens. <sub>(upstream description)</sub>
  <sub>`Plugin` · eran-broder · `TS` · call site [`src/jev/client.ts`](https://github.com/eran-broder/jev-skills/blob/HEAD/src/jev/client.ts), read 2026-09-24</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps. <sub>(upstream description)</sub>
  <sub>`Plugin` · hamakyo · `TS` · call site [`src/providers/jev-provider.ts`](https://github.com/hamakyo/jev-starter/blob/HEAD/src/providers/jev-provider.ts), read 2026-09-22</sub>

- **[jev-table-tennis](https://github.com/LiuHao-1443/jev-table-tennis)** — Table tennis vs. TypeSafe's Jev (System One). Every paddle move on the right is a live model decision — no local prediction, just a lookup table and a servo. <sub>(upstream description)</sub>
  <sub>`Project` · liuhao-1443 · `Py` · call site [`jev_eval_compare.py`](https://github.com/LiuHao-1443/jev-table-tennis/blob/HEAD/jev_eval_compare.py), read 2026-09-24</sub>

- **[jev-tetris](https://github.com/MachineLearning-Nerd/jev-tetris)** — A visual TypeSafe demo where Jev chooses verified Tetris placements. <sub>(upstream description)</sub>
  <sub>`Project` · machinelearning-nerd · `Py` · call site [`courtroom.py`](https://github.com/MachineLearning-Nerd/jev-tetris/blob/HEAD/courtroom.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-tetris](https://github.com/thelau/jev-tetris)** — A Tetris that a judgment model plays. The code finds every way the piece can land and writes each one as a sentence; JEV reads them and points at one. The board glows with its whole distribution before the piece falls. <sub>(upstream description)</sub>
  <sub>`Project` · thelau · `JS` · call site [`src/jev.js`](https://github.com/thelau/jev-tetris/blob/HEAD/src/jev.js), read 2026-09-24</sub>

- **[jev-tool-router](https://github.com/jackbarunz/jev-tool-router)** — Jev-powered MCP tool routing for Codex <sub>(upstream description)</sub>
  <sub>`Plugin` · jackbarunz · `JS` · call site [`scripts/setup-codex.mjs`](https://github.com/jackbarunz/jev-tool-router/blob/HEAD/scripts/setup-codex.mjs), read 2026-09-22</sub>

- **[jev-turbo](https://github.com/sightmap/jev-turbo)** — Jev-powered semantic browser use <sub>(upstream description)</sub>
  <sub>`Project` · sightmap · `Go` · call site [`explore/jev.go`](https://github.com/sightmap/jev-turbo/blob/HEAD/explore/jev.go), read 2026-09-22</sub>

- **[jev-ui-test](https://github.com/buer2233/jev-ui-test)** — UI test framework, a fork of jev-ultrafast: natural-language YAML cases run by pytest, Jev picks each step's action and target, and semantic assertions ask one `noul` per atomic claim about the page, with thresholds left in test code. The author reports a 458 ms median per action decision. <sub>(written by a model)</sub>
  <sub>`Project` · buer2233 · `Py` · `noul` · call site [`jev_ultrafast/framework/judge.py`](https://github.com/buer2233/jev-ui-test/blob/HEAD/jev_ultrafast/framework/judge.py), read by a model 2026-10-28 · ⚠ `vendor numbers`</sub>

- **[jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control)** — Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app. <sub>(upstream description)</sub>
  <sub>`Project` · chris-wozniczek · `Swift` · call site [`Sources/JevVoice/Agent/JevStepPlanner.swift`](https://github.com/chris-wozniczek/jev-voice-control/blob/HEAD/Sources/JevVoice/Agent/JevStepPlanner.swift), read 2026-09-22</sub>

- **[jev-windows-voice](https://github.com/mstf-svndk/jev-windows-voice)** — Control a Windows 10/11 PC by talking in Turkish or English: OpenAI Realtime, local Whisper, Jev and UI Automation together.
  <sub>`Project` · mstf-svndk · `JS` · call site [`src/jev.js`](https://github.com/mstf-svndk/jev-windows-voice/blob/HEAD/src/jev.js), read 2026-09-24</sub>

- **[jev-zork](https://github.com/Resadan-dev/jev-zork)** — Jev (TypeSafe System One) plays Zork I: one Choice per move over Jericho's valid actions, with its confidence on display. French dashboard. <sub>(upstream description)</sub>
  <sub>`Project` · resadan-dev · `Py` · call site [`src/jev_zork/judges.py`](https://github.com/Resadan-dev/jev-zork/blob/HEAD/src/jev_zork/judges.py), read 2026-09-24</sub>

- **[jev2048](https://github.com/erhanmeydan/jev2048)** — TypeSafe's Jev decision model plays a real online 2048 site: one API call per move, one key.
  <sub>`Project` · erhanmeydan · `Py` · call site [`jev2048/model.py`](https://github.com/erhanmeydan/jev2048/blob/HEAD/jev2048/model.py), read 2026-09-24</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — Jevaluate: evaluate before you trust. Field notes, runnable scripts and an agent skill for TypeSafe Jev: gated evals, a browser loop, a product walk with DeepSeek vision, a UI text judge and a first-click tree test. Co-authored with Claude Fable 5.1. <sub>(upstream description)</sub>
  <sub>`Plugin` · elshinq · `JS` · call site [`scripts/jev.mjs`](https://github.com/ElshinQ/jevaluate/blob/HEAD/scripts/jev.mjs), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jevarena](https://github.com/raihankhan-rk/jevarena)** — JevArena — two Jev agents duel in click-only browser games (Browser Use + TypeSafe Jev) <sub>(upstream description)</sub>
  <sub>`Project` · raihankhan-rk · `TS` · call site [`lib/server/jev.ts`](https://github.com/raihankhan-rk/jevarena/blob/HEAD/lib/server/jev.ts), read 2026-09-22</sub>

- **[jevball](https://github.com/atarikcaliskan/jevball)** — 22 Jev models, one ball: a 3D football match where every player is its own Jev (TypeSafe AI System One) decision. Watch, or take over the number 9. <sub>(upstream description)</sub>
  <sub>`Project` · atarikcaliskan · `JS` · call site [`server/jev.js`](https://github.com/atarikcaliskan/jevball/blob/HEAD/server/jev.js), read 2026-09-24</sub>

- **[jevcumber](https://github.com/RubyBrewsday/jevcumber)** — Write Cucumber tests with just the .feature file. No step definitions — Jev (TypeSafe AI) resolves each Gherkin step and Playwright runs it. <sub>(upstream description)</sub>
  <sub>`Project` · rubybrewsday · `TS` · call site [`src/resolver.ts`](https://github.com/RubyBrewsday/jevcumber/blob/HEAD/src/resolver.ts), read 2026-09-24</sub>

- **[jevdroid](https://github.com/antiyro/jevdroid)** — A typed Python framework for controlling Android over ADB with Jev. <sub>(upstream description)</sub>
  <sub>`Project` · antiyro · `Py` · call site [`src/jevdroid/providers/http.py`](https://github.com/antiyro/jevdroid/blob/HEAD/src/jevdroid/providers/http.py), read 2026-09-22</sub>

- **[jevex](https://github.com/jvsteiner/jevex)** — A minimal agent in which Jev directs the loop and a LangChain chat model writes only argument values and the final reply, over three local MCP servers with twelve working tools.
  <sub>`Project` · jvsteiner · `Py` · call site [`src/jevex/benchmark.py`](https://github.com/jvsteiner/jevex/blob/HEAD/src/jevex/benchmark.py), read 2026-09-24</sub>

- **[jevnav](https://github.com/dtduc-git/jevnav)** — Page truth for browser agents — and decisions that replay, test and audit. Jev picks the element, risky actions are gated, every run replays offline in CI. <sub>(upstream description)</sub>
  <sub>`Project` · dtduc-git · `Py` · call site [`src/jevnav/decide.py`](https://github.com/dtduc-git/jevnav/blob/HEAD/src/jevnav/decide.py), read 2026-09-24</sub>

- **[jevonly](https://github.com/buluoray/JevOnly)** — Pure Jev that can "type" and drive towards task completion. <sub>(upstream description)</sub>
  <sub>`Project` · buluoray · `Py` · call site [`src/jevonly/core/jev.py`](https://github.com/buluoray/JevOnly/blob/HEAD/src/jevonly/core/jev.py), read 2026-09-22</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — Sub-100ms security gate for AI agent tool calls, powered by TypeSafe's Jev (System-1) decision model. Single-request Choice/Noul/Score evaluation, dual-factor blocking matrix, calibrated-confidence routing, fail-closed parsing, zero-config local fallback. LangChain-ready. <sub>(upstream description)</sub>
  <sub>`Project` · lgy1027 · `Py` · call site [`jevshield/client.py`](https://github.com/lgy1027/jevshield/blob/HEAD/jevshield/client.py), read 2026-09-22</sub>

- **[JevTest](https://github.com/CorieW/JevTest)** — Bounded exploratory browser testing with Jev, deterministic assertions, and replayable evidence. <sub>(upstream description)</sub>
  <sub>`Project` · coriew · `TS` · call site [`src/jev.ts`](https://github.com/CorieW/JevTest/blob/HEAD/src/jev.ts), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[langchain-skill-router](https://github.com/deyna256/langchain-skill-router)** — Per-turn skill selection for LangChain and deepagents agents: a fast judge picks the few skills a turn needs, so a catalog of hundreds stays out of the prompt. <sub>(upstream description)</sub>
  <sub>`Plugin` · deyna256 · `Py` · call site [`src/langchain_skill_router/providers/jev.py`](https://github.com/deyna256/langchain-skill-router/blob/HEAD/src/langchain_skill_router/providers/jev.py), read 2026-09-24</sub>

- **[LLM Debugger](https://github.com/mohsen1/llm-debugger-vscode-extension)** — VS Code extension that debugs by running the code. At each pause Jev picks the next action as a `choice` (step, continue, breakpoint, evaluate, finish) and answers two `noul`s: is the faulty line found, and is it this one. A generation model supplies only locations, expressions and the fix. <sub>(written by a model)</sub>
  <sub>`Plugin` · mohsen1 · `TS` · `choice` · `noul` · call site [`src/agent/strategies/jev.ts`](https://github.com/mohsen1/llm-debugger-vscode-extension/blob/HEAD/src/agent/strategies/jev.ts), read by a model 2026-10-28 · ⚠ `3rd-party key` `vendor numbers`</sub>

- **[macos-computer-use-kit](https://github.com/Sur-Cai/macos-computer-use-kit)** — AX-first computer use for AI agents on macOS with optional Jev (TypeSafe System One) semantic guards: calibrated target/input judgments before an irreversible action, decisions kept in code. Accessibility-tree targeting, window-scoped input, clipboard-safe paste, read-back verification…
  <sub>`Plugin` · sur-cai · `Py` · call site [`src/macos_computer_use/jev.py`](https://github.com/Sur-Cai/macos-computer-use-kit/blob/HEAD/src/macos_computer_use/jev.py), read 2026-09-24</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — Binary approval gate for Codex and Claude Code — every intercepted tool call is reviewed by TypeSafe JEV and composed through a versioned local policy, with scoped authorization. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · alexj11324 · `Go` · cited file [`internal/jev/client.go`](https://github.com/alexj11324/open-jev-approvals/blob/HEAD/internal/jev/client.go), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[optim-jev](https://github.com/Oqura-ai/optim-jev)** — Claude Code plugin (Codex too) with three Jev tools: jev-compacter asks which stale tool calls and outputs can be dropped when context is compacted, jev-router picks a model and effort for each subagent, and jev-skills sends a short relevant skill list per prompt instead of the whole catalog. <sub>(written by a model)</sub>
  <sub>`Plugin` · Oqura-ai · `Py` · `noul` · call site [`src/optim_jev/tools/jev_compacter/jev.py`](https://github.com/Oqura-ai/optim-jev/blob/HEAD/src/optim_jev/tools/jev_compacter/jev.py), read by a model 2026-10-30</sub>

- **[otto](https://github.com/NobleSpartan6/otto)** — Open-source native computer use for macOS and Windows: TypeSafe Jev, local OCR, and selective planning. <sub>(upstream description)</sub>
  <sub>`Project` · noblespartan6 · `TS` · call site [`core/typesafe.ts`](https://github.com/NobleSpartan6/otto/blob/HEAD/core/typesafe.ts), read 2026-09-22</sub>

- **[pi-Jev-browser](https://github.com/laihenyi/pi-Jev-browser)** — Browser and macOS desktop agent for pi: Jev (TypeSafe System One) chooses each action from a structured observation in a bounded, surface-agnostic loop. Isolated Playwright tools, an allow-listed accessibility-tree tool, deterministic selectors, four-tier benchmarks. <sub>(upstream description)</sub>
  <sub>`Plugin` · laihenyi · `TS` · call site [`src/policy.ts`](https://github.com/laihenyi/pi-Jev-browser/blob/HEAD/src/policy.ts), read 2026-09-24</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions. <sub>(upstream description)</sub>
  <sub>`Plugin` · legacybridge-tech · `TS` · call site [`src/client.ts`](https://github.com/legacybridge-tech/pi-typesafe-jev/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[pijev](https://github.com/tonyzdev/pijev)** — PiJev: a terminal coding agent with Jev in the loop — Jev ranks the repository's files before the first call, picks skills and triages failures; your coding model writes the code. Built on Pi. <sub>(upstream description)</sub>
  <sub>`Project` · tonyzdev · `TS` · call site [`src/jev.ts`](https://github.com/tonyzdev/pijev/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[ps2-ai-agent](https://github.com/opaielsheikh/ps2-ai-agent)** — Autonomous PlayStation 2 AI Agent with real-time visual telemetry HUD powered by TypeSafe Jev System One <sub>(upstream description)</sub>
  <sub>`Project` · opaielsheikh · `Py` · call site [`agent_bridge.py`](https://github.com/opaielsheikh/ps2-ai-agent/blob/HEAD/agent_bridge.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[reflex](https://github.com/kaustav1996/reflex)** — A coding agent and personal assistant with System One reflexes (TypeSafe Jev) on top of the Pi coding agent <sub>(upstream description)</sub>
  <sub>`Plugin` · kaustav1996 · `TS` · call site [`src/extensions/typesafe/provider.ts`](https://github.com/kaustav1996/reflex/blob/HEAD/src/extensions/typesafe/provider.ts), read 2026-09-24</sub>

- **[robo-harness](https://github.com/grmkris/robo-harness)** — SO-101 robot-arm agent workbench: Bun/Effect coordinator, React workbench, Python LeRobot motor owner <sub>(upstream description)</sub>
  <sub>`Project` · grmkris · `TS` · call site [`apps/server/src/decision/jev.ts`](https://github.com/grmkris/robo-harness/blob/HEAD/apps/server/src/decision/jev.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[roverlab](https://github.com/juancamiloqhz/roverlab)** — A 3D planetary rover sandbox for experimenting with autonomous decisions using TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`Project` · juancamiloqhz · `TS` · call site [`server/decisions.ts`](https://github.com/juancamiloqhz/roverlab/blob/HEAD/server/decisions.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[rpg-jev](https://github.com/lmvdz/rpg-jev)** — A living-world RPG whose NPCs are decided by TypeSafe's Jev judge model; code owns rules, numbers and state. <sub>(upstream description)</sub>
  <sub>`Project` · lmvdz · `TS` · call site [`spikes/m0-jev/src/run.ts`](https://github.com/lmvdz/rpg-jev/blob/HEAD/spikes/m0-jev/src/run.ts), read 2026-09-24 · ⚠ `no licence` `archived`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One Search: navigate and trace code with TypeSafe judgments and repository evidence <sub>(upstream description)</sub>
  <sub>`Project` · cpaczek · `TS` · call site [`src/client.ts`](https://github.com/cpaczek/s1s/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[slidepilot](https://github.com/harshil1712/slidepilot)** — Voice-driven semantic auto-advance for Slidev, powered by Cloudflare Agents and TypeSafe AI Jev <sub>(upstream description)</sub>
  <sub>`Project` · harshil1712 · `TS` · call site [`apps/worker/src/decision.ts`](https://github.com/harshil1712/slidepilot/blob/HEAD/apps/worker/src/decision.ts), read 2026-09-22</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — Snake controlled by parallel Jev assessments, with one API call per game tick. <sub>(upstream description)</sub>
  <sub>`Project` · siroccomask · `Py` · call site [`jev_controller.py`](https://github.com/siroccomask/snake-jev/blob/HEAD/jev_controller.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — Every tool call your agent makes, checked before it runs. A Claude Code plugin that uses TypeSafe AI's Jev to verify each pending tool call against the session plan, then allows it, asks you, or blocks it. Proof of concept <sub>(upstream description)</sub>
  <sub>`Plugin` · getexcited · `TS` · call site [`lib/jev.ts`](https://github.com/getexcited/stepwarden/blob/HEAD/lib/jev.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[swarmrouter](https://github.com/ndolinschi/swarmrouter)** — Route tasks to research/code/browser/support/writer agents via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/swarmrouter/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[terrarium](https://github.com/TheGali/terrarium)** — A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world. <sub>(upstream description)</sub>
  <sub>`Project` · thegali · `JS` · call site [`bench/run-jev.mjs`](https://github.com/TheGali/terrarium/blob/HEAD/bench/run-jev.mjs), read 2026-09-22</sub>

- **[tictacjev](https://github.com/darthblanc/tictacjev)** — A tic-tac-toe app where one player is Jev, TypeSafe AI's System One Model with live confidence scores and probabilities. <sub>(upstream description)</sub>
  <sub>`Project` · darthblanc · `TS` · call site [`backend/app/jev_client.py`](https://github.com/darthblanc/tictacjev/blob/HEAD/backend/app/jev_client.py), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[tsai-civ2](https://github.com/phyous/tsai-civ2)** — TypeSafe Jev plays original Civilization II in a browser, with live action probabilities. Experimental full-game harness. <sub>(upstream description)</sub>
  <sub>`Project` · phyous · `Py` · call site [`civ2/typesafe.py`](https://github.com/phyous/tsai-civ2/blob/HEAD/civ2/typesafe.py), read 2026-09-22</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — Shadow-mode validation harness for a pre-execution firewall on AI agent tool calls (TypeSafe/Jev). Real run, findings in report.md. <sub>(upstream description)</sub>
  <sub>`Project` · anshchoudhary · `Py` · call site [`firewall/judge.py`](https://github.com/AnshChoudhary/typesafe-ai-firewall/blob/HEAD/firewall/judge.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-ai-trading-showcase](https://github.com/JordiParraCrespo/typesafe-ai-trading-showcase)** — Live BTC, ETH and XRP prices with a shared TypeSafe buy-or-wait demonstration over the last minute of real trades. No trades are placed.
  <sub>`Project` · jordiparracrespo · `TS` · call site [`lib/market.ts`](https://github.com/JordiParraCrespo/typesafe-ai-trading-showcase/blob/HEAD/lib/market.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe-chess](https://github.com/Dimesio/typesafe-chess)** — FUn little experiment with Typesafe AI Jev Model playing chess against stockfish :) <sub>(upstream description)</sub>
  <sub>`Project` · dimesio · `JS` · call site [`server/jev.js`](https://github.com/Dimesio/typesafe-chess/blob/HEAD/server/jev.js), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo)** — Three.js drone simulator with a Python backend and live TypeSafe Jev navigation <sub>(upstream description)</sub>
  <sub>`Project` · kxzk · `Py` · call site [`backend/jev.py`](https://github.com/kxzk/typesafe-jev-drone-demo/blob/HEAD/backend/jev.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[typesafe-minecraft-demo](https://github.com/ellistev/typesafe-minecraft-demo)** — A Minecraft Java player controlled by TypeSafe AI, with live decisions, Canadian flag building, and a side-by-side dashboard. <sub>(upstream description)</sub>
  <sub>`Project` · ellistev · `JS` · call site [`src/decisions.cjs`](https://github.com/ellistev/typesafe-minecraft-demo/blob/HEAD/src/decisions.cjs), read 2026-09-24 · ⚠ `no licence`</sub>

- **[ui-generator-instinct-jev](https://github.com/joevidev/ui-generator-instinct-jev)** — Jev as a UI generator: describe a case in free text and Jev answers only typed questions over real option sets, picking and configuring an actual shadcn/ui component or page block. It never writes code or copy.
  <sub>`Project` · joevidev · `TS` · call site [`lib/typesafe-client.ts`](https://github.com/joevidev/ui-generator-instinct-jev/blob/HEAD/lib/typesafe-client.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)** — Wires Jev into Browser Use to drive a browser automation agent.
  <sub>`Video` · AICodeKing · ⚠ `unverified claims`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
