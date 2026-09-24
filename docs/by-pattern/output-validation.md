# Output validation

<sub>[awesome-jev](../../README.md) · [中文](output-validation.zh-CN.md)</sub>

_Check a model's output against a rubric before it reaches a user._

Every catalogued example of this decision — 134 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#output-validation); [the site](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=en) can filter them further by language, primitive and kind.

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[latitude-llm](https://github.com/latitude-dev/latitude-llm)** — Open-source observability for AI agents. Find where your agents fail, dispatch your coding agent to fix it, and verify the fix against real traces.
  <sub>`Project` · ★4,672 · latitude-dev · `TS`</sub>

- **[reticle](https://github.com/reticlehq/reticle)** — AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications.
  <sub>`Project` · ★830 · reticlehq · `TS`</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, checks, and approval gates instead of hoping it follows your instructions.
  <sub>`Project` · ★820 · bastani-inc · `TS`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.
  <sub>`Project` · ★425 · notque · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[JevRev](https://github.com/Alex314618-create/JevRev)** — The decision layer beside an LLM: Jev filters plans, checks progress and keeps attention on work worth continuing, while the LLM supplies breadth and implementation.
  <sub>`Project` · ★303 · alex314618-create · `TS`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — A local-first MCP plugin for continuous code-quality review by coding agents.
  <sub>`Plugin` · ★217 · niazmorshed2007 · `TS`</sub>

- **[abide](https://github.com/coldteadotai/abide)** — Make your coding agent abide by all your project rules
  <sub>`Plugin` · ★211 · coldteadotai · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★173 · `JS` · `choice` · `score` · `noul`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — Code quality and coverage judgements for coding agents, in Rust.
  <sub>`Project` · ★109 · supercorp-ai · `Rs`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — An agent that routes evaluation work through typed decisions.
  <sub>`Project` · ★105 · vinilana · `TS` · ⚠ `no licence`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim in an answer cites a quote from the page.
  <sub>`Project` · ★100 · agent-labs-dev · `Py`</sub>

- **[formanator](https://github.com/timrogers/formanator)** — Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) clients, with support for AI-powered receipt analysis with an LLM or Jev
  <sub>`Plugin` · ★99 · timrogers · `Rs`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — lint text in code by jev scorerer
  <sub>`Project` · ★78 · mizchi · `TS`</sub>

- **[Canny](https://github.com/qkal/Canny)** — Guards against a coding agent claiming it finished: reads tool output, the diff and test results, then judges whether the completion claim holds.
  <sub>`Project` · ★74 · `TS` · `noul` · `score`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks.
  <sub>`Project` · ★64 · dimweaker · `Py`</sub>

- **[oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev)** — An oxlint rule that is a yes/no question about a function, call, JSX element or file: each match goes to Jev, and the plugin reports an error when the yes-probability clears your cutoff.
  <sub>`Plugin` · ★60 · wobsoriano · `TS`</sub>

- **[jev-recruiter](https://github.com/skeptrunedev/jev-recruiter)** — A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence against your hiring brief.
  <sub>`Project` · ★47 · skeptrunedev · `Py`</sub>

- **[vibecheck](https://github.com/RafalWilinski/vibecheck)** — Chrome extension: vibe-check your X posts with TypeSafe's Jev before you hit Post
  <sub>`Plugin` · ★47 · rafalwilinski · `JS` · ⚠ `no licence`</sub>

- **[jev-suite](https://github.com/klauswg/jev-suite)** — Four decision-quality tools on Jev (TypeSafe System One): Jev answers structured questions, deterministic code keeps the final say.
  <sub>`Project` · ★36 · klauswg · `Java`</sub>

- **[jev-cua](https://github.com/ronadin2002/jev-cua)** — Voice and text control for macOS. One floating bar, live UI action selection with Jev, and a continuous observe–act–verify loop.
  <sub>`Project` · ★34 · ronadin2002 · `Swift` · ⚠ `no licence`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay i
  <sub>`Project` · ★33 · choxos · `JS`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP.
  <sub>`Plugin` · ★30 · leepokai · `JS`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.
  <sub>`Project` · ★29 · danrwilloughby · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy
  <sub>`Plugin` · ★25 · compozy · `TS`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — grep for what code does: one Noul per code chunk, diff hunk or CSV row, printed as file:line hits with probabilities. --diff gates a PR in CI on a rule written in English (exit 0 match / 1 clean / 2 error); --tests lists the test files a diff can affect.
  <sub>`Project` · ★24 · kyu1204 · `TS` · `noul` · `choice` · `score` · ⚠ `unverified claims`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper
  <sub>`Project` · ★23 · goodrahstar · `JS`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★20 · keeltrace · `Py`</sub>

- **[invalidate](https://github.com/chopratejas/invalidate)** — The invalidation layer for AI memory. Every fact gets a lease; new evidence ends it. Built on TypeSafe Jev.
  <sub>`Project` · ★18 · chopratejas · `Py`</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails open on everything else
  <sub>`Plugin` · ★18 · valentynkit · `JS`</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and OpenCode: typed classify, check, score, rank, and ask, plus one-command setup.
  <sub>`Plugin` · ★15 · francoischastel · `TS`</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG
  <sub>`Benchmark` · ★14 · erendikmenn · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action, pi package, and more. Built with Effect.
  <sub>`Project` · ★14 · tyler-dot-earth · `TS`</sub>

- **[cmd-mod-jev-nudge](https://github.com/CommandCodeAI/cmd-mod-jev-nudge)** — Command Code mod: nudges the agent to keep going when it stops with work left, judged by Jev
  <sub>`Plugin` · ★13 · commandcodeai · `TS`</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code plugin: Jev for rule checks, verbatim compaction, and prompt routing
  <sub>`Plugin` · ★12 · 0x7067 · `Py`</sub>

- **[lintus](https://github.com/virolea/lintus)** — A linter whose rules are written in plain language.
  <sub>`Project` · ★12 · virolea · `Rs`</sub>

- **[jev-commit](https://github.com/valentynkit/jev-commit)** — A pre-commit hook: one call judges whether the commit message matches the diff.
  <sub>`Project` · ★11 · valentynkit · `Py`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.
  <sub>`Plugin` · ★11 · huntedman · `TS`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered by Jev
  <sub>`Project` · ★10 · qew7 · `Rb`</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 可疑行为 \| Review Agent Skills and MCP code with Jev, static evidence, and explicit coverage gaps
  <sub>`Plugin` · ★10 · win4r · `Py`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★9 · 24601 · `Py`</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — PR Risk review, automated by Jev
  <sub>`Project` · ★9 · hexyedev · `Py`</sub>

- **[lejudge-jev-jepa](https://github.com/AbdelStark/lejudge-jev-jepa)** — Natural-language constraints for JEPA world-model planning, judged by a decision model instead of an LLM.
  <sub>`Project` · ★9 · abdelstark · `Py`</sub>

- **[typed_evals](https://github.com/TrustifAI/typed_evals)** — Fast, typed, calibrated evaluations for LLM and agent outputs, powered by Jev — with simple, framework-agnostic Python APIs
  <sub>`Project` · ★8 · trustifai · `Py`</sub>

- **[zod-jev](https://github.com/jomatsu/zod-jev)** — Zod validates the shape; Jev validates the meaning. Semantic checks on a schema — personal data present? price plausible? category matches? — go to Jev in one request and come back as probabilities that become Zod issues.
  <sub>`SDK` · ★8 · jomatsu · `TS`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides.
  <sub>`Project` · ★7 · marissafamularo · `JS`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — DiffJury — TypeSafe Jev PR risk router + code review coach
  <sub>`Project` · ★7 · raihankhan-rk · `TS` · ⚠ `no licence`</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local Responses proxy, with independent task verification.
  <sub>`Plugin` · ★7 · minilv · `TS`</sub>

- **[jev-browser](https://github.com/tontoko/jev-browser)** — One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.
  <sub>`Project` · ★7 · tontoko · `JS`</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — Probability-scored guardrails for Claude Code: deny rule-breaking edits and unasked-for deploys, route your docs into each prompt, and check the final answer against the turn's own evidence.
  <sub>`Plugin` · ★7 · muratcakmak · `TS`</sub>

- **[jev-pref](https://github.com/doeixd/jev-pref)** — Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.
  <sub>`Project` · ★7 · doeixd · `JS`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev.
  <sub>`Project` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[dinostomp](https://github.com/collapseindex/dinostomp)** — A verification layer for AI evaluations. Checks the instrument, not just the score: data, scorer, runs, numbers, claims, and itself.
  <sub>`Project` · ★6 · collapseindex · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through.
  <sub>`Project` · ★6 · ufec · `Kt`</sub>

- **[jev-lm](https://github.com/y0usaf/jev-lm)** — A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval
  <sub>`Project` · ★6 · y0usaf · `TS`</sub>

- **[jev-spec](https://github.com/nozomi-koborinai/jev-spec)** — ⚡ Catch spec drift on every commit: check your code against your Markdown specs with TypeSafe AI's Jev model.
  <sub>`Project` · ★6 · nozomi-koborinai · `TS`</sub>

- **[riff](https://github.com/scale-venture-partners/riff)** — A small, fast prose linter: ruff-style rule codes for writing, backed by TypeSafe's Jev model
  <sub>`Project` · ★6 · scale-venture-partners · `Py`</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gate completion claims inside DeepSeek Harness.
  <sub>`Plugin` · ★5 · horusjiang · `TS`</sub>

- **[hermes-jev-plugin](https://github.com/ajensenwaud/hermes-jev-plugin)** — TypeSafe Jev (System One) decision tools for Hermes Agent: jev_check / jev_route / jev_score / jev_evaluate
  <sub>`Plugin` · ★5 · ajensenwaud · `Py`</sub>

- **[jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark)** — Comparing Jev, Gemini Flash, and Claude Fable on Python code review rules: cost, speed, accuracy, and consistency. Includes results, charts, and reproducible experiments.
  <sub>`Benchmark` · ★5 · gemanor · `Py`</sub>

- **[jev-e2e](https://github.com/perixtar/jev-e2e)** — Natural-language end-to-end tests for web apps, powered by Jev and Playwright.
  <sub>`Project` · ★5 · perixtar · `TS`</sub>

- **[hunch](https://github.com/Kelbie/hunch)** — Semantic code review with Jev, plain-English rules and Agent Skills.
  <sub>`Project` · ★4 · kelbie · `TS`</sub>

- **[jev-align](https://github.com/caiovicentino/jev-align)** — Calibrated alignment verifier for LLM responses and agent plans — powered by Jev
  <sub>`Project` · ★4 · caiovicentino · `JS`</sub>

- **[jev-codes](https://github.com/Kushwho/jev-codes)** — Audit your git diff against YAML coding-standards packs using TypeSafe's Jev model, from a CLI or your AI agent's command/skill.
  <sub>`Project` · ★4 · kushwho · `TS`</sub>

- **[jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel)** — Catch breaking API behavior hidden in OpenAPI prose with deterministic checks and TypeSafe JEV System One semantic review.
  <sub>`Project` · ★4 · shuhansun · `Py`</sub>

- **[jevarena](https://github.com/chenmingtang830/jevarena)** — Open-source BYOK arena for Jev and other AI judges. Find failures, compare quality, cost, and latency.
  <sub>`Benchmark` · ★4 · chenmingtang830 · `TS`</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — Code-review gate for CI and coding agents: asks TypeSafe Jev small typed questions about functions, files, tests and docs, and reports findings with locations and probabilities
  <sub>`Project` · ★4 · tech-byte-frontier · `Rs`</sub>

- **[semantic-assert](https://github.com/mondaychen/semantic-assert)** — Testing lib for asserting the real requirement.
  <sub>`SDK` · ★4 · mondaychen · `TS`</sub>

- **[taste-lint](https://github.com/mblode/taste-lint)** — Catch AI slop before you ship.
  <sub>`Project` · ★4 · mblode · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verification.
  <sub>`Project` · ★3 · rinnecoder · `Py`</sub>

- **[jev-exploration](https://github.com/SamuelSacco/jev-exploration)** — Jev (TypeSafe) exploratory thread: claim audit, live demos, and runnable code
  <sub>`Benchmark` · ★3 · samuelsacco · `Py` · ⚠ `no licence`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.
  <sub>`Project` · ★3 · foadsf · `Py`</sub>

- **[jevkit](https://github.com/ariel-frischer/jevkit)** — Fast Rust CLI for TypeSafe Jev: typed decisions, offline linting before you pay
  <sub>`Project` · ★3 · ariel-frischer · `Rs`</sub>

- **[jevsume](https://github.com/unownone/jevsume)** — ATS-friendly resume review powered by Jev (TypeSafe System One). The frontend extracts resume text the way a parser would, then a Cloudflare Worker runs typed JEV questions and composes a JevScore.
  <sub>`Project` · ★3 · unownone · `TS` · ⚠ `no licence`</sub>

- **[jevtest](https://github.com/realZachi/jevtest)** — Semantic test matchers for Vitest and Jest, powered by TypeSafe's Jev model. Write expectations in plain English, get calibrated probabilities back.
  <sub>`SDK` · ★3 · realzachi · `TS`</sub>

- **[jod](https://github.com/mateonunez/jod)** — Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.
  <sub>`Project` · ★3 · mateonunez · `TS`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — A Stop hook that stops your coding agent from stopping too early. Plain-language rules, judged by jev.
  <sub>`Plugin` · ★3 · noplan-inc · `Py`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — Binary approval gate for Codex and Claude Code — every intercepted tool call is reviewed by TypeSafe JEV and composed through a versioned local policy, with scoped authorization.
  <sub>`Jev-like alternative` · ★3 · alexj11324 · `Go` · ⚠ `not Jev itself`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score / Noul questions, lint them, measure on labelled data, and put calibrated thresholds in code
  <sub>`Plugin` · ★3 · simota · `TS`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — Judge every LLM response before the user sees it. AI SDK middleware and OpenAI-compatible proxy.
  <sub>`Integration` · ★3 · noelzappy · `TS`</sub>

- **[typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review)** — About calibrating Jev for code reviews
  <sub>`Benchmark` · ★3 · selmar · `Py` · ⚠ `no licence`</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop hook that checks an AI assistant's claims against what it actually read this session, using TypeSafe's Jev as the judge
  <sub>`Plugin` · ★2 · vladyslavhontar · `Py`</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification.
  <sub>`Project` · ★2 · aidil2105 · `Py`</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions)** — Jev Decisions Plugin for Hermes (and other AI Agents): tool risk reviews, human approval recommendations, evidence checks, and a local decision journal.
  <sub>`Plugin` · ★2 · bojansandhaus · `Py`</sub>

- **[jev-pr-judge](https://github.com/juanegido/jev-pr-judge)** — Typed verdicts on pull requests with TypeSafe System One (Jev): one parallel call, policy in code, usable as a GitHub Action
  <sub>`Project` · ★2 · juanegido · `TS`</sub>

- **[jev-rust-review](https://github.com/kindintelligence/jev-rust-review)** — Rust-aware code review for Claude Code and coding agents, powered by TypeSafe Jev
  <sub>`Plugin` · ★2 · kindintelligence · `Rs`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring
  <sub>`Project` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jevibe-check](https://github.com/sriganesh/jevibe-check)** — A live tone labeler for Bluesky posts and drafts, using TypeSafe's Jev API.
  <sub>`Project` · ★2 · sriganesh · `JS`</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — n8n community node for Jev by TypeSafe AI: classify, score and check text with calibrated probabilities. Parallel requests and multi-item batching.
  <sub>`Project` · ★2 · khmuhtadin · `TS`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — Semantic assertions for pytest: test what your LLM app's output means, judged by TypeSafe's Jev.
  <sub>`Plugin` · ★2 · allebee · `Py`</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — Shadow-mode validation harness for a pre-execution firewall on AI agent tool calls (TypeSafe/Jev). Real run, findings in report.md.
  <sub>`Project` · ★2 · anshchoudhary · `Py` · ⚠ `no licence`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — Unofficial community MCP plugin for Codex and Claude Code using TypeSafe Jev for bounded routing, ranking, extraction, verification, and escalation
  <sub>`Plugin` · ★2 · e-fl · `JS`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)
  <sub>`Project` · ★2 · opaielsheikh · `TS` · ⚠ `no licence`</sub>

- **[datajev](https://github.com/zzz1YAO/DataJev)** — ⚡ DataJev LLM → Analyze Jev → Continue / Switch / Verify / Stop System-1 control for System-2 data agents
  <sub>`Project` · ★1 · zzz1yao · `Py`</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design.
  <sub>`Benchmark` · ★1 · xienda · `JS`</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — A verified browser agent: a cheap Jev guard (evidence-checked completions, a destructive gate) in front of any LLM browser driver, with Jev taking the mechanical steps in dual mode. Built on browser-use; every number pre-registered and measured.
  <sub>`Project` · ★1 · tom-r-main · `Py`</sub>

- **[human-compiler](https://github.com/asfarsadewa/human-compiler)** — A compiler for human language. Paste text, get diagnostics. Measured by TypeSafe Jev.
  <sub>`Project` · ★1 · asfarsadewa · `TS`</sub>

- **[jackalope](https://github.com/Jackalope-Dev/jackalope)** — A desktop workspace for coding agents, parallel Git worktrees, and code review.
  <sub>`Project` · ★1 · jackalope-dev · `Rs`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.
  <sub>`Project` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `one commit` `AI-written`</sub>

- **[jev-bench](https://github.com/TheWayWithin/jev-bench)** — Does the cited source actually say it? A 42-claim benchmark: Jev (TypeSafe System One) against GPT-5.4, Claude Sonnet 5 and Gemini 3.1 Pro.
  <sub>`Benchmark` · ★1 · thewaywithin · `Py`</sub>

- **[jev-debtgate](https://github.com/smlayero/jev-debtgate)** — Jev-powered technical debt gate for coding agents and CI. Bring your own TypeSafe API key.
  <sub>`Project` · ★1 · smlayero · `TS`</sub>

- **[jev-labs](https://github.com/copyleftdev/jev-labs)** — Never confidently wrong: a TLA+-verified consensus kernel around TypeSafe's Jev, run through 1,680 chaos-tested pharmacy decisions with zero wrong verdicts. Film, code, and every captured call.
  <sub>`Project` · ★1 · copyleftdev · `Py`</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — A bounded Jev risk check for Claude Code: eight risk axes, one request, one optional reinspection.
  <sub>`Plugin` · ★1 · muse0509 · `Go`</sub>

- **[jev-reasoning-navigator](https://github.com/AndreuVM/jev-reasoning-navigator)** — JEV Reasoning Navigator: Cognitive supervision, loop prevention, and anti-hallucination engine for autonomous LLM agents using TypeSafe AI
  <sub>`Project` · ★1 · andreuvm · `Py` · ⚠ `no licence`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.
  <sub>`Project` · ★1 · fatwang2 · `JS`</sub>

- **[jev-subtitle-translator](https://github.com/GeekLinkDev/jev-subtitle-translator)** — Translate SRT subtitles with structured LLM output and check every translation with Jev.
  <sub>`Project` · ★1 · geeklinkdev · `Py`</sub>

- **[jevguard](https://github.com/Jhonnyr97/JevGuard)** — Claude Code + Codex CLI plugin that verifies the agent follows project rules through a System One (Jev) model
  <sub>`Plugin` · ★1 · jhonnyr97 · `TS`</sub>

- **[lossless-rewrite](https://github.com/dttfrancesco/lossless-rewrite)** — AI text rewriting and document summarization with Jev checks for missing ideas and automatic repair. Local editor and CLI.
  <sub>`Project` · ★1 · dttfrancesco · `TS`</sub>

- **[omp-typesafe](https://github.com/siddicky/omp-typesafe)** — TypeSafe AI (Jev) adversarial reviewer and typesafe_ask tool for the omp coding agent
  <sub>`Plugin` · ★1 · siddicky · `TS`</sub>

- **[plotveil](https://github.com/Dearest/plotveil)** — A quiet spoiler blocker for YouTube comments. One typed Jev (TypeSafe System One) Noul decision per comment; covered while checked, still covered if the check fails.
  <sub>`Project` · ★1 · dearest · `TS`</sub>

- **[profanity-checker](https://github.com/4rays/profanity-checker)** — Cloudflare Worker to check for profanity using TypeSafe Jev
  <sub>`Project` · ★1 · 4rays · `TS`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — Every tool call your agent makes, checked before it runs. A Claude Code plugin that uses TypeSafe AI's Jev to verify each pending tool call against the session plan, then allows it, asks you, or blocks it. Proof of concept
  <sub>`Plugin` · ★1 · getexcited · `TS`</sub>

- **[system-one-playground](https://github.com/DonaldMurillo/system-one-playground)** — Readable scripting, semantic code checks, a Go System One client, and Studio.
  <sub>`Project` · ★1 · donaldmurillo · `Go`</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — Reusable GitHub Action: agent fix loop gated by checks, an AI reviewer, and TypeSafe Jev
  <sub>`Project` · ★0 · ripwords · `TS` · ⚠ `no licence`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — An experimental protocol for evidence-aware agent handoffs, bounded worker continuation, and TypeSafe/Jev-assisted review, with reproducible evaluation.
  <sub>`Benchmark` · ★0 · zsoxi · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full.
  <sub>`Project` · ★0 · jourdanlabs · `Py` · ⚠ `no licence`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — A CLI and GitHub Action that assesses code-change risk using deterministic rules and TypeSafe Jev, recommending checks and reviewers before merge.
  <sub>`Project` · ★0 · moezubair · `TS`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能
  <sub>`Plugin` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric)** — Architecture for running many semantic decisions through one validated path, with a labelled 111-case benchmark comparing TypeSafe Jev against a Claude baseline, and a dashboard for inspecting any single decision. Experimental, not production.
  <sub>`Benchmark` · ★0 · ghubnab99 · `C#`</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves.
  <sub>`Plugin` · ★0 · rashedint32 · `JS`</sub>

- **[jev-resume-analyzer](https://github.com/awun8191/jev-resume-analyzer)** — CV diagnostics and job alignment with TypeSafe Jev, React and FastAPI
  <sub>`Project` · ★0 · awun8191 · `Py` · ⚠ `no licence`</sub>

- **[jev-review](https://github.com/thiago-ss/jev-review)** — Autonomous Jev pull-request review with typed decisions, calibrated approval gates, and trusted-owner escalation
  <sub>`Project` · ★0 · thiago-ss · `Py` · ⚠ `no licence`</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — A small second eval for shadcn-ui/lint that uses TypeSafe's Jev to judge the linter's own output.
  <sub>`Project` · ★0 · blas0 · `JS`</sub>

- **[jev-the-janitor](https://github.com/kylehovance-ai/jev-the-janitor)** — A janitor for markdown vaults powered by TypeSafe Jev: Jev votes on each note, your code files it, you review the low-confidence pile.
  <sub>`Project` · ★0 · kylehovance-ai · `Py`</sub>

- **[jev-verify](https://github.com/stillmarcus24/jev-verify)** — Check whether a published Jev output was actually produced by Jev. Implements the Yurin confidence identity; flags published fixtures that violate it.
  <sub>`Project` · ★0 · stillmarcus24 · `JS`</sub>

- **[JevTest](https://github.com/CorieW/JevTest)** — Bounded exploratory browser testing with Jev, deterministic assertions, and replayable evidence.
  <sub>`Project` · ★0 · coriew · `TS` · ⚠ `no licence`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — Optional typed TypeSafe AI Jev decisions for OpenClaw, with SecretRef credentials and strict API validation.
  <sub>`Project` · ★0 · olli0103 · `TS`</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — Single-agent Pi coding coprocessor with Jev semantic gates, baseline-to-current diff review, and append-only observability telemetry.
  <sub>`Project` · ★0 · kamilpostrozny · `TS`</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — Using Typesafe.AI to generate diff reviews.
  <sub>`Project` · ★0 · rbalch · `Py` · ⚠ `no licence`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.
  <sub>`Benchmark` · Near Here</sub>

- **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)** — Collects the third-party evaluations that exist so far and frames the question of where a decision model can stand in for an LLM judge.
  <sub>`Article` · Laurie Voss</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
