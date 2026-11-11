# Intent routing

<sub>[awesome-jev](../../README.md) · [中文](intent-routing.zh-CN.md)</sub>

_Classify what the user wants and send the request down the right branch._

Every catalogued example of this decision — 61 of them. The same rows, with caveats, are in [the index](../../README.md#intent-routing); [the site](https://kydlikebtc.github.io/awesome-jev/?p=intent-routing&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#intent-routing): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 3 · call site 50 · wire shape 0 · example only 0 · independent reports 4 · negative results 0 · no file cited 11. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [TypeSafe AI n8n node](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai) <sub>`Plugin` · `TS` · `choice` · `noul` · `score`</sub>
- [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home) <sub>`Official docs` · `Py`</sub>
- [Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) <sub>`Official docs` · `Py`</sub>
- [Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing) <sub>`Official docs` · `Py` · `choice`</sub>

## Examples in this repository

Code under this repository's [`examples/`](../../examples/) filed under this pattern. Each is also listed below, with its summary; [the examples' README](../../examples/README.md) says how far they have been checked.

- [Example: confidence-gated escalation](../../examples/02-confidence-gate/main.py) <sub>`Snippet` · `Py` · `choice` · ⚠ `code untested`</sub>

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[TypeSafe AI n8n node](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai)** ⭐ — TypeSafe's own n8n community node. Evaluate asks Jev typed questions about each item and adds the answers; Route sends each item to an output by one answer, with a fallback output for low-confidence choices and an uncertain one between two noul thresholds. AI Agents can use it as a tool. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · typesafe-ai · `TS` · `choice` · `noul` · `score` · call site [`nodes/TypeSafeAi/api.ts`](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/blob/HEAD/nodes/TypeSafeAi/api.ts), read by a model 2026-11-04</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — Runnable demo code for a smart home assistant that evaluates user requests with typed decisions.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★100k+ · `Py` · `choice` · `score` · `noul` · call site [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py), read 2026-09-22</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human.
  <sub>`Integration` · ★10k+ · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★10k+ · `TS` · `choice` · `noul` · call site [`apps/web/utils/decision-model/decision-model.ts`](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/decision-model.ts), read by a model 2026-11-05</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py), read 2026-09-22</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★1k+ · `Java` · `choice` · `score` · `noul` · call site [`cn/app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/cn/app/src/main/java/com/jev/probe/jev/JevQuestions.kt), read 2026-09-22</sub>

- **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)** — A teaching example with a deliberate control group: the same station-enquiry task written in plain Python that only accepts Y/N, next to a Noul that reads intent.
  <sub>`Tutorial` · ★1k+ · Real Python · `Py` · `noul` · call site [`hello-jev/jev_noul.py`](https://github.com/realpython/materials/blob/HEAD/hello-jev/jev_noul.py), read 2026-09-22</sub>

- **[shapeshift](https://github.com/anishfn/shapeshift)** — One text box that turns into the right card as you type (event, checklist, timer, bill split and more). With a TypeSafe key one Jev call answers 14 questions: which card, plus choices, nouls and scores such as urgency or video call; code parses dates and amounts. Offline, keyword rules answer. <sub>(written by a model)</sub>
  <sub>`Project` · ★1k+ · anishfn · `TS` · call site [`src/lib/jev/client.ts`](https://github.com/anishfn/shapeshift/blob/HEAD/src/lib/jev/client.ts), read 2026-09-24</sub>

- **[vellum-assistant](https://github.com/vellum-ai/vellum-assistant)** — Personal AI assistant with eight kinds of memory that works across apps and chat channels. Its experimental TypeSafe provider sends the conversation to Jev as state and by default asks one noul, whether the latest message asks for a specific action, replying with the answers as JSON. <sub>(written by a model)</sub>
  <sub>`Project` · ★1k+ · vellum-ai · `TS` · call site [`assistant/src/providers/jev/client.ts`](https://github.com/vellum-ai/vellum-assistant/blob/HEAD/assistant/src/providers/jev/client.ts), read 2026-09-22</sub>

- **[foreman](https://github.com/thruwire/foreman)** — A software-factory foreman that uses Jev to decide what an agent pipeline should do next.
  <sub>`Project` · ★100+ · thruwire · `Py` · call site [`src/foreman/decision_models/jev.py`](https://github.com/thruwire/foreman/blob/HEAD/src/foreman/decision_models/jev.py), read by a model 2026-11-05</sub>

- **[Hey Jev](https://github.com/henryklunaris/hey-jev)** — macOS voice assistant: local Whisper transcribes a command, then one Jev request asks every question at once (category, compound or not, target, app, action, volume level) as `choice`, `noul` and `score` questions; code runs the action through AppleScript, and only general questions reach an LLM. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · henryklunaris · `Py` · `choice` · `noul` · `score` · call site [`siri.py`](https://github.com/henryklunaris/hey-jev/blob/HEAD/siri.py), read by a model 2026-10-29 · ⚠ `no licence` `3rd-party key`</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — An AI video editor routing an editing instruction to an operation, a target clip and a track, with a keyword router as fallback.
  <sub>`Project` · ★100+ · `TS` · `choice` · `noul` · call site [`scripts/jev.js`](https://github.com/kevinbadi/hyperedit/blob/HEAD/scripts/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac)** — 微信消息意图识别悬浮窗（macOS）：看屏 + 本地小模型判断意图和风险，再按话术生成回复候选。纯只读、不注入微信。
  <sub>`Project` · ★100+ · jev-chat · `Py` · call site [`src/judge_jev.py`](https://github.com/jev-chat/jev-chat-jarvis-mac/blob/HEAD/src/judge_jev.py), read 2026-09-22</sub>

- **[jev-chat-windows](https://github.com/jev-chat/jev-chat-windows)** — 微信（Windows 4.x）旁挂的回复辅助：窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动
  <sub>`Project` · ★100+ · jev-chat · `Py` · call site [`core/jev_client.py`](https://github.com/jev-chat/jev-chat-windows/blob/HEAD/core/jev_client.py), read 2026-09-22</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.
  <sub>`Project` · ★100+ · `TS` · `choice` · `noul` · call site [`apps/server/src/jev/client.ts`](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts), read 2026-09-22</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each.
  <sub>`Project` · ★100+ · `TS` · `choice` · `noul` · call site [`src/lib/typesafe.ts`](https://github.com/superagents-lab/jev-search/blob/HEAD/src/lib/typesafe.ts), read 2026-09-22</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — Read-only Instagram, TikTok and LinkedIn research: Jev routes the platform and selects each bounded socai CLI action from fresh browser evidence; code validates targets and preserves source links.
  <sub>`Project` · ★100+ · socai-io · `JS` · `choice` · call site [`src/actions.js`](https://github.com/socai-io/jev-social/blob/HEAD/src/actions.js), read 2026-09-23 · ⚠ `3rd-party key`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — Voice-driven browser control where target criteria are rebuilt per request from the live element list, always including a none option.
  <sub>`Project` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/jev.js`](https://github.com/moritzkremb/jev-voice-browser/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[mu](https://github.com/qybaihe/mu)** — Coding agent and desktop app built on pi that asks Jev at 40 decision points which tool-output chunks enter the context, which stale tool results to drop, whether a rule-flagged command was asked for and whether fetched pages or MCP output carry injected instructions.
  <sub>`Project` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · call site [`packages/kyrn-judge/src/providers/typesafe.ts`](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts) · ⚠ `self-submitted`</sub>

- **[smithers](https://github.com/smithersai/smithers)** — Smithers is an agentic workflow framework for defining workflows in simple TypeScript configuration files and executing them quickly, durably, and reliably <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · smithersai · `TS` · call site [`packages/smithers/agent/model/src/Evaluator.ts`](https://github.com/smithersai/smithers/blob/HEAD/packages/smithers/agent/model/src/Evaluator.ts), read by a model 2026-11-05</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — Local-first work assistant that turns mail, chats and tickets into tasks your coding agents do, sending nothing until you approve. With a TypeSafe key, Jev triages: nouls asked as the owner would judge, with their profile and past verdicts in the state, such as whether to make an item a task. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★100+ · ldbumble · `Py` · call site [`taskuary/jev.py`](https://github.com/ldbumble/taskuary/blob/HEAD/taskuary/jev.py), read 2026-09-22</sub>

- **[狗头军师 Jev Chat](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat)** — Chat-reply assistant (desktop overlay, Android floating assistant, iOS keyboard) built on Jev Android. From the visible chat or a screenshot it asks Jev the literal question, the other person's intent, a danger level, whether to reply now and the best action, then has Jev pick among drafted replies. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · shengjidaguai-china · `Kt` · `choice` · `score` · `noul` · call site [`integrations/jev_android/app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat/blob/HEAD/integrations/jev_android/app/src/main/java/com/jev/probe/jev/JevQuestions.kt), read by a model 2026-10-26 · ⚠ `3rd-party key`</sub>

- **[DMB: decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — Benchmark of APIs that pick one option from a list with a confidence: Jev, LLMs with structured output and deterministic baselines, on accuracy, latency, cost, failures and confidence. The author reports jev-latest at 79.2% on Banking77, 88.6% on CLINC150 and 48.3% micro F1 on NLU++. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★10+ · nibzard · `Py` · `choice` · call site [`src/dmb/contenders/jev.py`](https://github.com/nibzard/decision-model-benchmark/blob/HEAD/src/dmb/contenders/jev.py), read by a model 2026-11-04 · ⚠ `no licence`</sub>

- **[Gatekeeper](https://github.com/AgriciDaniel/gatekeeper)** — Claude Code hook that decides which agent or skill should handle a prompt before the AI picks one: YAML rulebooks settle what code can, Jev answers which handler owns the rest as a Choice, and confidence bands turn that into route, suggest, confirm, escalate, block or allow. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · AgriciDaniel · `Py` · `choice` · `noul` · call site [`gatekeeper/jev.py`](https://github.com/AgriciDaniel/gatekeeper/blob/HEAD/gatekeeper/jev.py), read by a model 2026-11-01</sub>

- **[Gut](https://github.com/vinibrsl/gut)** — Elixir DSL for LLM decisions: Gut.feel(subject, question, choices) returns one of your Elixir values, such as the team that should handle a ticket. Its Jev adapter asks the question as one Choice through ReqLLM; other adapters use any ReqLLM model, Ollama or your own code. <sub>(written by a model)</sub>
  <sub>`SDK` · ★10+ · vinibrsl · `Ex` · `choice` · call site [`lib/gut/req_llm/jev.ex`](https://github.com/vinibrsl/gut/blob/HEAD/lib/gut/req_llm/jev.ex), read by a model 2026-11-02</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — A Home Assistant integration: typed answers about the house as sensors, noul, choice and score actions for automations, and a conversation agent.
  <sub>`Integration` · ★10+ · abovecolin · `Py` · `noul` · `choice` · `score` · call site [`custom_components/jev/services.py`](https://github.com/AboveColin/HA-Jev/blob/HEAD/custom_components/jev/services.py), read 2026-09-30 · ⚠ `AI-written` `self-submitted`</sub>

- **[hono-jev-router](https://github.com/yusukebe/hono-jev-router)** — Routes HTTP requests by meaning — a semantic router for a web framework.
  <sub>`Project` · ★10+ · yusukebe · `TS` · call site [`src/index.ts`](https://github.com/yusukebe/hono-jev-router/blob/HEAD/src/index.ts), read 2026-09-22</sub>

- **[Jev Chat Jarvis (iOS keyboard)](https://github.com/jev-chat/jev-chat-jarvis-ios)** — iOS keyboard version of Jev Chat Jarvis: copy a message in any chat app and the custom keyboard shows Jev's read of its intent (a `choice`) and risk (a `score`), plus drafted replies that Jev ranks with another `choice`; one tap inserts a reply. An optional extension reads the screen by local OCR. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · jev-chat · `Swift` · `choice` · `score` · call site [`Shared/JevJudge.swift`](https://github.com/jev-chat/jev-chat-jarvis-ios/blob/HEAD/Shared/JevJudge.swift), read by a model 2026-10-30 · ⚠ `3rd-party key`</sub>

- **[jev playground (deepdave98)](https://github.com/deepdave98/jev-playground)** — Weekly go-to-market experiments with Jev, each tested against Claude: lead triage and routing, deal risk, reply triage, MEDDPICC fields from call summaries, duplicate accounts and closed-lost reactivation, plus an MCP server. A shared client subtracts a measured score bias of 0.30 before rounding. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★10+ · deepdave98 · `Py` · `noul` · `choice` · `score` · call site [`common/jev.py`](https://github.com/deepdave98/jev-playground/blob/HEAD/common/jev.py), read by a model 2026-10-31 · ⚠ `no licence`</sub>

- **[Jev steer or queue](https://github.com/Larkspur-Wang/Jev_steer_or_queue)** — Hook for Claude Code (and, more loosely, the Codex CLI) that asks Jev what to do with a message sent while the agent is busy: steer the running task now, queue it as a separate request for when the turn ends, or interrupt and stop the turn. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · Larkspur-Wang · `Py` · `choice` · `noul` · call site [`claude-code/scripts/jev_router.py`](https://github.com/Larkspur-Wang/Jev_steer_or_queue/blob/HEAD/claude-code/scripts/jev_router.py), read by a model 2026-11-02</sub>

- **[jev-ai-sdk-form-router](https://github.com/vercel-labs/jev-ai-sdk-form-router)** — Route form submissions to the right people with Jev and AI SDK. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · vercel-labs · `TS` · call site [`components/routing-result.tsx`](https://github.com/vercel-labs/jev-ai-sdk-form-router/blob/HEAD/components/routing-result.tsx), read 2026-09-24</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · parth-kp · `Py` · call site [`jev_mail/providers/typesafe_direct.py`](https://github.com/parth-kp/jev-mail-classifier/blob/HEAD/jev_mail/providers/typesafe_direct.py), read 2026-09-22</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark. <sub>(earlier upstream description)</sub>
  <sub>`Benchmark` · ★10+ · anisselbd · `Py` · call site [`run_jev.py`](https://github.com/anisselbd/jev-phishing-bench/blob/HEAD/run_jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jevcache](https://github.com/kushals256/jevcache)** — Skip expensive LLM calls when TypeSafe Jev says same intent. OpenAI-compatible local cache proxy — npx @kushalicious/jevcache
  <sub>`Project` · ★10+ · kushals256 · `TS` · call site [`scripts/eval.ts`](https://github.com/kushals256/jevcache/blob/HEAD/scripts/eval.ts), read 2026-09-24</sub>

- **[jevyoumean](https://github.com/syumai/jevyoumean)** — Semantic "Did you mean?" for any CLI — wraps commands and uses TypeSafe's Jev to match subcommand typos by intent, not edit distance. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · syumai · `Go` · call site [`internal/jev/client.go`](https://github.com/syumai/jevyoumean/blob/HEAD/internal/jev/client.go), read 2026-09-22</sub>

- **[RoboDiag Harness](https://github.com/yuebit/robodiag-harness)** — Diagnostic harness for ROS 2 robots in which Jev sorts each request into query, diagnosis, action or chat and, for a diagnosis, picks the next read-only evidence tool. Code requires a health test and a live measurement before a diagnosis ends, and a chat model explains the evidence. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · yuebit · `Py` · `choice` · call site [`robodiag_jev.py`](https://github.com/yuebit/robodiag-harness/blob/HEAD/robodiag_jev.py), read by a model 2026-11-01</sub>

- **[typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow)** — A small async LangGraph workflow: each mocked email goes to Jev as a typed Choice (invoice or general) and the graph routes it to a demo handler. Classification makes real API calls; the handlers only set a destination.
  <sub>`Project` · ★10+ · giesn · `Py` · call site [`src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py`](https://github.com/GiesN/typesafe-jev-workflow/blob/HEAD/src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails.
  <sub>`Tutorial` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Apparite](https://github.com/dglazkov/jev2ui)** — Design tool that turns a text prompt into a clickable app mock painted by a DESIGN.md: Jev decides, in one request of choices and nouls, which sections, layout and icon a screen gets, and what each later message asks to change; a small Gemini model writes the words and code assembles the screen. <sub>(written by a model)</sub>
  <sub>`Project` · dglazkov · `TS` · `choice` · `noul` · `score` · call site [`src/server/plan.ts`](https://github.com/dglazkov/jev2ui/blob/HEAD/src/server/plan.ts), read by a model 2026-11-09 · ⚠ `3rd-party key`</sub>

- **[ComfyUI System One](https://github.com/dante01yoon/ComfyUI-SystemOne)** — ComfyUI custom nodes that branch a workflow on a typed judgement, such as which style a prompt wants, whether it is too graphic for children or whether it names a real person, with one dropdown switching the backend between Jev, Laya and Cloudflare's Clef. <sub>(written by a model)</sub>
  <sub>`Plugin` · dante01yoon · `Py` · `choice` · `noul` · `score` · call site [`systemone/backends.py`](https://github.com/dante01yoon/ComfyUI-SystemOne/blob/HEAD/systemone/backends.py), read by a model 2026-11-11</sub>

- **[ElBruno.AI.Decisions](https://github.com/elbruno/ElBruno.AI.Decisions)** — One .NET API on NuGet for classification, routing, rubric scoring and proposition checks that returns probability distributions, with a package that calls Jev's POST /v1/systemone natively beside packages for Microsoft's Foundry decision models and local models through Ollama. <sub>(written by a model)</sub>
  <sub>`SDK` · elbruno · `C#` · `choice` · `score` · `noul` · call site [`src/ElBruno.AI.Decisions.Jev/JevClient.cs`](https://github.com/elbruno/ElBruno.AI.Decisions/blob/HEAD/src/ElBruno.AI.Decisions.Jev/JevClient.cs), read by a model 2026-11-11</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — Routing with an act-or-escalate gate, where the policy function is deliberately left unimplemented because the thresholds are yours to choose.
  <sub>`Snippet` · `Py` · `choice` · call site [`examples/02-confidence-gate/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/02-confidence-gate/main.py), read 2026-09-22 · ⚠ `code untested`</sub>

- **[GoEventBus](https://github.com/protocol-lattice/goeventbus)** — High-performance Go event bus with an optional decision layer: when no deterministic rule or cached decision matches an event's state, Jev, reached through OpenRouter's Decisions API, picks which event type to run from a bounded candidate set, and execution stays inside the bus. <sub>(written by a model)</sub>
  <sub>`Project` · protocol-lattice · `Go` · `choice` · call site [`jev.go`](https://github.com/protocol-lattice/goeventbus/blob/HEAD/jev.go), read by a model 2026-11-06</sub>

- **[Harness](https://github.com/autonomous-ai/openharness)** — Command center that runs coding agents such as Claude Code and Codex side by side across machines. Its ⌘B router asks Jev 1.13 through OpenRouter's Decisions API, in one request of Choice questions, which session, project and agent a new task goes to. <sub>(written by a model)</sub>
  <sub>`Project` · autonomous-ai · `TS` · `choice` · call site [`cli/src/lib/jev/jevClient.ts`](https://github.com/autonomous-ai/openharness/blob/HEAD/cli/src/lib/jev/jevClient.ts), read by a model 2026-11-05</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice` · ⚠ `paywall`</sub>

- **[Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/)** — Zero-config access from a Netlify function: use the official SDK with no API key, base URL or provider setup, billed through Netlify credits.
  <sub>`Integration` · `TS` · `choice`</sub>

- **[jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval)** — A third-party check of Jev against two LLMs under identical conditions: routing booking inquiries to a photo-shoot service for tourists in Japan, sixty synthetic messages in four languages.
  <sub>`Benchmark` · shogo-nfrealmusic · `TS` · call site [`src/jev.ts`](https://github.com/Shogo-nfrealmusic/jev-eval/blob/HEAD/src/jev.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-inbox-queue](https://github.com/tusharck/jev-inbox-queue)** — Turn an inbox into a short action queue with Jev (TypeSafe System One) <sub>(upstream description)</sub>
  <sub>`Project` · tusharck · `Py` · call site [`inbox_queue/classify.py`](https://github.com/tusharck/jev-inbox-queue/blob/HEAD/inbox_queue/classify.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[JevT++](https://github.com/wiatrM/jevtpp)** — C++20 library that turns runtime text, JSON or objects into enums, booleans and scores through compile-time schemas, with full distributions and explicit abstention. Runs local Laya models in-process (ONNX Runtime or ggml) or Jev through an opt-in remote backend; latency metrics and a Mario demo. <sub>(written by a model)</sub>
  <sub>`SDK` · wiatrm · `C++` · call site [`include/jevt/remote.hpp`](https://github.com/wiatrM/jevtpp/blob/HEAD/include/jevt/remote.hpp), read by a model 2026-10-24</sub>

- **[lanebreak](https://github.com/ndolinschi/lanebreak)** — LaneBreak — support ticket priority+routing via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/lanebreak/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

- **[Orchvia](https://github.com/masonlee39/orchvia)** — Runs Claude Code and Codex agents as a team from your own application. Its optional routing layer asks a pluggable judge, Jev or plain rules, typed Choice, Noul and Score questions about which agent takes a request; below 0.85 confidence or a 0.2 margin the proposal waits for a person. <sub>(written by a model)</sub>
  <sub>`Project` · masonlee39 · `Py` · `choice` · `noul` · `score` · call site [`python/src/orchvia/routing.py`](https://github.com/masonlee39/orchvia/blob/HEAD/python/src/orchvia/routing.py), read by a model 2026-11-05</sub>

- **[question-kit](https://github.com/Engid/question-kit)** — TypeScript library of building blocks for Jev, with a Python port in preview, including a service agent: you describe a service as data, code runs the procedure, and Jev reads each customer turn for the intent, the values a step needs and the judgement calls, each behind a confidence gate. <sub>(written by a model)</sub>
  <sub>`SDK` · Engid · `TS` · `choice` · `noul` · `score` · call site [`packages/question-kit/core/typesafe.ts`](https://github.com/Engid/question-kit/blob/HEAD/packages/question-kit/core/typesafe.ts), read by a model 2026-11-11</sub>

- **[SpotAsk](https://github.com/shiquda/spotask)** — Mac menu bar app for quick questions with your own API key. Its External Ask can let a decision model such as Jev choose where a question goes (a web AI like ChatGPT or Perplexity, a local CLI agent, or a desktop app) with one choice question, then confirm inline or send above a threshold. <sub>(written by a model)</sub>
  <sub>`Project` · shiquda · `Swift` · `choice` · call site [`Sources/SpotAsk/Decision/DecisionRouting.swift`](https://github.com/shiquda/spotask/blob/HEAD/Sources/SpotAsk/Decision/DecisionRouting.swift), read by a model 2026-11-06</sub>

- **[TypeSafe Conversation for Home Assistant](https://github.com/the-sof/home-assistant-typesafe-conversation-agent)** — Home Assistant conversation agent that decides with a System One model instead of an LLM: device commands and questions about the home are resolved in code from Jev's typed answers on which intent, device and value is meant, and a doubtful answer asks or falls back instead of guessing. <sub>(written by a model)</sub>
  <sub>`Plugin` · the-sof · `Py` · `choice` · `noul` · call site [`custom_components/typesafe_conversation/system_one.py`](https://github.com/the-sof/home-assistant-typesafe-conversation-agent/blob/HEAD/custom_components/typesafe_conversation/system_one.py), read by a model 2026-11-07</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — The richest Vercel walkthrough: single and multi-question calls, probability-threshold routing, and unit tests with a mock evaluation model.
  <sub>`Tutorial` · `TS` · `noul` · `choice` · `score`</sub>

- **[Jev router: how model routing works, and 16 routers compared](https://madewithjev.com/jev-router)** — Explains a router that asks Jev which model, tool or skill the next turn needs before anything is spent, why routing down and back up can cost more than not routing, and compares 16 routers for Claude Code, Codex and OpenRouter.
  <sub>`Article` · Jon Kraayenbrink · ⚠ `self-submitted`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified claims`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
