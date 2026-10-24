# Output validation

<sub>[awesome-jev](../../README.md) · [中文](output-validation.zh-CN.md)</sub>

_Check a model's output against a rubric before it reaches a user._

Every catalogued example of this decision — 134 of them. The same rows, with caveats, are in [the index](../../README.md#output-validation); [the site](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#output-validation): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 2 · call site 129 · wire shape 1 · example only 0 · independent reports 11 · negative results 0 · no file cited 4. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) <sub>`Official docs` · `Py` · `noul` · `score`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[latitude-llm](https://github.com/latitude-dev/latitude-llm)** — Open-source observability for AI agents. Find where your agents fail, dispatch your coding agent to fix it, and verify the fix against real traces. <sub>(upstream description)</sub>
  <sub>`Project` · ★1k+ · latitude-dev · `TS` · call site [`packages/platform/ai-jev/src/jev-shadow-decision-provider.ts`](https://github.com/latitude-dev/latitude-llm/blob/HEAD/packages/platform/ai-jev/src/jev-shadow-decision-provider.ts), read 2026-09-22</sub>

- **[reticle](https://github.com/reticlehq/reticle)** — AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications. <sub>(upstream description)</sub>
  <sub>`Project` · ★1k+ · reticlehq · `TS` · call site [`bench/harness/jev.mjs`](https://github.com/reticlehq/reticle/blob/HEAD/bench/harness/jev.mjs), read 2026-09-24</sub>

- **[abide](https://github.com/coldteadotai/abide)** — Make your coding agent abide by all your project rules <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · coldteadotai · `TS` · call site [`packages/cli/src/lib/jev.ts`](https://github.com/coldteadotai/abide/blob/HEAD/packages/cli/src/lib/jev.ts), read 2026-09-24</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, checks, and approval gates instead of hoping it follows your instructions.
  <sub>`Project` · ★100+ · bastani-inc · `TS` · call site [`packages/ai/src/decision-models.generated.ts`](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts), read 2026-09-24</sub>

- **[Canny](https://github.com/qkal/Canny)** — Guards against a coding agent claiming it finished: reads tool output, the diff and test results, then judges whether the completion claim holds.
  <sub>`Project` · ★100+ · `TS` · `noul` · `score` · call site [`src/jev.ts`](https://github.com/qkal/Canny/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim in an answer cites a quote from the page. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · agent-labs-dev · `Py` · call site [`src/fastbrowse/clients/typesafe.py`](https://github.com/agent-labs-dev/fastbrowse/blob/HEAD/src/fastbrowse/clients/typesafe.py), read 2026-09-22</sub>

- **[formanator](https://github.com/timrogers/formanator)** — Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) clients, with support for AI-powered receipt analysis with an LLM or Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · timrogers · `Rs` · call site [`src/typesafe.rs`](https://github.com/timrogers/formanator/blob/HEAD/src/typesafe.rs), read 2026-09-22</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — An agent that routes evaluation work through typed decisions.
  <sub>`Project` · ★100+ · vinilana · `TS` · call site [`agent/lib/jev-router.ts`](https://github.com/vinilana/jev-eval-agent/blob/HEAD/agent/lib/jev-router.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · leepokai · `JS` · call site [`src/jev.js`](https://github.com/leepokai/jev-guard/blob/HEAD/src/jev.js), read 2026-09-22</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — lint text in code by jev scorerer <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · mizchi · `TS` · call site [`src/jev.ts`](https://github.com/mizchi/jev-lint/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts), read 2026-09-22</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — A local-first MCP plugin for continuous code-quality review by coding agents.
  <sub>`Plugin` · ★100+ · niazmorshed2007 · `TS` · call site [`src/jev/client.ts`](https://github.com/NiazMorshed2007/jev-review/blob/HEAD/src/jev/client.ts), read 2026-09-22</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js), read 2026-09-22</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — Code quality and coverage judgements for coding agents, in Rust.
  <sub>`Project` · ★100+ · supercorp-ai · `Rs` · call site [`crates/supercov-cli/src/quality.rs`](https://github.com/supercorp-ai/supercov/blob/HEAD/crates/supercov-cli/src/quality.rs), read 2026-09-22</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · notque · `Py` · call site [`plugins/jev-auto-compact/hooks/jev-auto-compact.mjs`](https://github.com/notque/vexjoy-agent/blob/HEAD/plugins/jev-auto-compact/hooks/jev-auto-compact.mjs), read 2026-09-22</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★10+ · 24601 · `Py` · call site [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md), read 2026-09-24</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · marissafamularo · `JS` · call site [`src/lib/typesafe.js`](https://github.com/MarissaFamularo/citation-verifier/blob/HEAD/src/lib/typesafe.js), read 2026-09-22</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code plugin: Jev for rule checks, verbatim compaction, and prompt routing <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · 0x7067 · `Py` · call site [`scripts/jev.py`](https://github.com/0x7067/claude-jev/blob/HEAD/scripts/jev.py), read 2026-09-22</sub>

- **[cmd-mod-jev-nudge](https://github.com/CommandCodeAI/cmd-mod-jev-nudge)** — Command Code mod: nudges the agent to keep going when it stops with work left, judged by Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · commandcodeai · `TS` · call site [`src/protocol.ts`](https://github.com/CommandCodeAI/cmd-mod-jev-nudge/blob/HEAD/src/protocol.ts), read 2026-09-24</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gate completion claims inside DeepSeek Harness. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · horusjiang · `TS` · call site [`src/config.ts`](https://github.com/HorusJiang/dsh-jev-tools/blob/HEAD/src/config.ts), read 2026-09-24</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★10+ · keeltrace · `Py` · call site [`hermes_nerve/client.py`](https://github.com/keeltrace/hermes-nerve/blob/HEAD/hermes_nerve/client.py), read 2026-09-22</sub>

- **[hermes-jev-plugin](https://github.com/ajensenwaud/hermes-jev-plugin)** — TypeSafe Jev (System One) decision tools for Hermes Agent: jev_check / jev_route / jev_score / jev_evaluate <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · ajensenwaud · `Py` · call site [`client.py`](https://github.com/ajensenwaud/hermes-jev-plugin/blob/HEAD/client.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[invalidate](https://github.com/chopratejas/invalidate)** — The invalidation layer for AI memory. Every fact gets a lease; new evidence ends it. Built on TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · chopratejas · `Py` · call site [`evals/screen_matrix.py`](https://github.com/chopratejas/invalidate/blob/HEAD/evals/screen_matrix.py), read 2026-09-22</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails open on everything else <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · valentynkit · `JS` · call site [`belay.mjs`](https://github.com/valentynkit/jev-belay/blob/HEAD/belay.mjs), read 2026-09-24</sub>

- **[jev-browser](https://github.com/tontoko/jev-browser)** — One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · tontoko · `JS` · call site [`src/decision.ts`](https://github.com/tontoko/jev-browser/blob/HEAD/src/decision.ts), read 2026-09-24</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and OpenCode: typed classify, check, score, rank, and ask, plus one-command setup. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · francoischastel · `TS` · call site [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts), read 2026-09-22</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · goodrahstar · `JS` · call site [`lib/racers.mjs`](https://github.com/goodrahstar/jev-column-race/blob/HEAD/lib/racers.mjs), read 2026-09-22</sub>

- **[jev-commit](https://github.com/valentynkit/jev-commit)** — A pre-commit hook: one call judges whether the commit message matches the diff.
  <sub>`Project` · ★10+ · valentynkit · `Py` · call site [`jev_commit/jev.py`](https://github.com/valentynkit/jev-commit/blob/HEAD/jev_commit/jev.py), read 2026-09-22</sub>

- **[jev-cua](https://github.com/ronadin2002/jev-cua)** — Voice and text control for macOS. One floating bar, live UI action selection with Jev, and a continuous observe–act–verify loop. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · ronadin2002 · `Swift` · call site [`Sources/Core.swift`](https://github.com/ronadin2002/jev-cua/blob/HEAD/Sources/Core.swift), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-e2e](https://github.com/perixtar/jev-e2e)** — Natural-language end-to-end tests for web apps, powered by Jev and Playwright. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · perixtar · `TS` · call site [`src/runner.ts`](https://github.com/perixtar/jev-e2e/blob/HEAD/src/runner.ts), read 2026-09-24</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered by Jev
  <sub>`Project` · ★10+ · qew7 · `Rb` · call site [`lib/jev/client.rb`](https://github.com/Qew7/jev-feels/blob/HEAD/lib/jev/client.rb), read 2026-09-22</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · dimweaker · `Py` · call site [`src/jev_libero/client.py`](https://github.com/Dimweaker/jev-libero/blob/HEAD/src/jev_libero/client.py), read 2026-09-22</sub>

- **[jev-pref](https://github.com/doeixd/jev-pref)** — Turn your AGENTS.md preferences into a fast, Jev-powered AI linter. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · doeixd · `JS` · call site [`packages/jev-pref/src/config.js`](https://github.com/doeixd/jev-pref/blob/HEAD/packages/jev-pref/src/config.js), read 2026-09-22</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · erendikmenn · `Py` · call site [`src/jev_rag_benchmark/rerankers.py`](https://github.com/erendikmenn/jev-rag-benchmark/blob/HEAD/src/jev_rag_benchmark/rerankers.py), read 2026-09-22 · author's conclusion: favourable (author-stated, not reproduced here)</sub>

- **[jev-recruiter](https://github.com/skeptrunedev/jev-recruiter)** — A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence against your hiring brief. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · skeptrunedev · `Py` · call site [`jev_ultrafast/decision_provider.py`](https://github.com/skeptrunedev/jev-recruiter/blob/HEAD/jev_ultrafast/decision_provider.py), read 2026-09-22</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay i
  <sub>`Project` · ★10+ · choxos · `JS` · call site [`docs/jev.js`](https://github.com/choxos/jev-reviewer/blob/HEAD/docs/jev.js), read 2026-09-22</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 可疑行为 \| Review Agent Skills and MCP code with Jev, static evidence, and explicit coverage gaps <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · win4r · `Py` · call site [`scripts/jev_client.py`](https://github.com/win4r/jev-security-scan/blob/HEAD/scripts/jev_client.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-spec](https://github.com/nozomi-koborinai/jev-spec)** — ⚡ Catch spec drift on every commit: check your code against your Markdown specs with TypeSafe AI's Jev model. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · nozomi-koborinai · `TS` · call site [`src/evaluator/jev-evaluator.ts`](https://github.com/nozomi-koborinai/jev-spec/blob/HEAD/src/evaluator/jev-evaluator.ts), read 2026-09-22</sub>

- **[jev-suite](https://github.com/klauswg/jev-suite)** — Four decision-quality tools on Jev (TypeSafe System One): Jev answers structured questions, deterministic code keeps the final say. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · klauswg · `Java` · call site [`jev-fidelity/src/main/java/com/jevsuite/fidelity/eval/EvalRunner.java`](https://github.com/klauswg/jev-suite/blob/HEAD/jev-fidelity/src/main/java/com/jevsuite/fidelity/eval/EvalRunner.java), read 2026-09-24</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · huntedman · `TS` · call site [`src/jev-client.ts`](https://github.com/iamtoomas/JevLint/blob/HEAD/src/jev-client.ts), read 2026-09-22</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — PR Risk review, automated by Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · hexyedev · `Py` · call site [`src/JevPR/providers/jev.py`](https://github.com/HexyeDEV/JevPR/blob/HEAD/src/JevPR/providers/jev.py), read 2026-09-24</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — grep for what code does: one Noul per code chunk, diff hunk or CSV row, printed as file:line hits with probabilities. --diff gates a PR in CI on a rule written in English (exit 0 match / 1 clean / 2 error); --tests lists the test files a diff can affect.
  <sub>`Project` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · call site [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts), read 2026-09-23 · ⚠ `unverified claims` `self-submitted`</sub>

- **[lejudge-jev-jepa](https://github.com/AbdelStark/lejudge-jev-jepa)** — Natural-language constraints for JEPA world-model planning, judged by a decision model instead of an LLM. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · abdelstark · `Py` · call site [`lejudge/judge/jev.py`](https://github.com/AbdelStark/lejudge-jev-jepa/blob/HEAD/lejudge/judge/jev.py), read 2026-09-24</sub>

- **[lintus](https://github.com/virolea/lintus)** — A linter whose rules are written in plain language. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · virolea · `Rs` · call site [`crates/jev/src/client.rs`](https://github.com/virolea/lintus/blob/HEAD/crates/jev/src/client.rs), read 2026-09-24</sub>

- **[oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev)** — An oxlint rule that is a yes/no question about a function, call, JSX element or file: each match goes to Jev, and the plugin reports an error when the yes-probability clears your cutoff.
  <sub>`Plugin` · ★10+ · wobsoriano · `TS` · call site [`src/jev.ts`](https://github.com/wobsoriano/oxlint-plugin-jev/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action, pi package, and more. Built with Effect.
  <sub>`Project` · ★10+ · tyler-dot-earth · `TS` · call site [`apps/patdown/src/typesafe-judge.ts`](https://github.com/tyler-dot-earth/patdown/blob/HEAD/apps/patdown/src/typesafe-judge.ts), read 2026-09-22</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · nyarlathoteppppp · `TS` · call site [`bench/jev-lab.ts`](https://github.com/Nyarlathoteppppp/pi-heed/blob/HEAD/bench/jev-lab.ts), read 2026-09-22</sub>

- **[Sedum (npm: sedum-cli)](https://github.com/sedum-dev/sedum)** — Plain-English browser end-to-end tests next to Playwright code. In goal mode a Jev Choice picks each next operation (click, type, done or blocked) and its target; authored steps use a Choice per sentence; each verify claim is two Nouls (holds, contradicted). Playwright acts; code applies thresholds.
  <sub>`Project` · ★10+ · sedum-dev · `TS` · `choice` · `noul` · call site [`packages/provider-typesafe/src/index.ts`](https://github.com/sedum-dev/sedum/blob/HEAD/packages/provider-typesafe/src/index.ts), read 2026-09-30 · ⚠ `unverified claims` `self-submitted`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · myc0576 · `Py` · call site [`src/smartmoney_cub_harness/jev/direct.py`](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · danrwilloughby · `TS` · call site [`src/jev.ts`](https://github.com/DanRWilloughby/snifftest/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[taste-lint](https://github.com/mblode/taste-lint)** — Catch AI slop before you ship. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · mblode · `TS` · call site [`src/map/jev.ts`](https://github.com/mblode/taste-lint/blob/HEAD/src/map/jev.ts), read 2026-09-22</sub>

- **[typed_evals](https://github.com/TrustifAI/typed_evals)** — Fast, typed, calibrated evaluations for LLM and agent outputs, powered by Jev — with simple, framework-agnostic Python APIs <sub>(earlier upstream description)</sub>
  <sub>`Project` · ★10+ · trustifai · `Py` · call site [`typed_evals/backends/jev.py`](https://github.com/TrustifAI/typed_evals/blob/HEAD/typed_evals/backends/jev.py), read 2026-09-24</sub>

- **[vibecheck](https://github.com/RafalWilinski/vibecheck)** — Chrome extension: vibe-check your X posts with TypeSafe's Jev before you hit Post <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · rafalwilinski · `JS` · call site [`background.js`](https://github.com/RafalWilinski/vibecheck/blob/HEAD/background.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · compozy · `TS` · call site [`benchmarks/jev-calibrate.ts`](https://github.com/compozy/yoshi/blob/HEAD/benchmarks/jev-calibrate.ts), read 2026-09-22</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — Reusable GitHub Action: agent fix loop gated by checks, an AI reviewer, and TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ripwords · `TS` · call site [`src/jev.ts`](https://github.com/Ripwords/agent-gate-loop/blob/HEAD/src/jev.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — An experimental protocol for evidence-aware agent handoffs, bounded worker continuation, and TypeSafe/Jev-assisted review, with reproducible evaluation. <sub>(earlier upstream description)</sub>
  <sub>`Benchmark` · zsoxi · `Py` · call site [`tools/build_benchmark_prompts.py`](https://github.com/zsoXi/agent-handoff-gate/blob/HEAD/tools/build_benchmark_prompts.py), read 2026-09-22 · ⚠ `one commit` `archived`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full. <sub>(upstream description)</sub>
  <sub>`Project` · jourdanlabs · `Py` · call site [`harness/run.py`](https://github.com/jourdanlabs/assay-001/blob/HEAD/harness/run.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — A CLI and GitHub Action that assesses code-change risk using deterministic rules and TypeSafe Jev, recommending checks and reviewers before merge. <sub>(upstream description)</sub>
  <sub>`Project` · moezubair · `TS` · call site [`src/jev.ts`](https://github.com/moezubair/check-risk/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop hook that checks an AI assistant's claims against what it actually read this session, using TypeSafe's Jev as the judge <sub>(upstream description)</sub>
  <sub>`Plugin` · vladyslavhontar · `Py` · call site [`stop_verify.py`](https://github.com/VladyslavHontar/clear-head/blob/HEAD/stop_verify.py), read 2026-09-22</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — DiffJury — TypeSafe Jev PR risk router + code review coach <sub>(upstream description)</sub>
  <sub>`Project` · raihankhan-rk · `TS` · call site [`src/lib/review.ts`](https://github.com/raihankhan-rk/diffjury/blob/HEAD/src/lib/review.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[dinostomp](https://github.com/collapseindex/dinostomp)** — A verification layer for AI evaluations. Checks the instrument, not just the score: data, scorer, runs, numbers, claims, and itself. <sub>(upstream description)</sub>
  <sub>`Project` · collapseindex · `Py` · call site [`audits/xstest-refusal-guards/compare.py`](https://github.com/collapseindex/dinostomp/blob/HEAD/audits/xstest-refusal-guards/compare.py), read 2026-09-24</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (choice/score/noul) and jev_verify, honest by design. <sub>(earlier upstream description)</sub>
  <sub>`Benchmark` · xienda · `JS` · call site [`lib/index.js`](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js), read 2026-09-22</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — A verified browser agent: a cheap Jev guard (evidence-checked completions, a destructive gate) in front of any LLM browser driver, with Jev taking the mechanical steps in dual mode. Built on browser-use; every number pre-registered and measured. <sub>(upstream description)</sub>
  <sub>`Project` · tom-r-main · `Py` · call site [`jevdual/evals/runner.py`](https://github.com/Tom-R-Main/Footwork/blob/HEAD/jevdual/evals/runner.py), read 2026-09-24</sub>

- **[human-compiler](https://github.com/asfarsadewa/human-compiler)** — A compiler for human language. Paste text, get diagnostics. Measured by TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · asfarsadewa · `TS` · call site [`src/worker/index.ts`](https://github.com/asfarsadewa/human-compiler/blob/HEAD/src/worker/index.ts), read 2026-09-22</sub>

- **[hunch](https://github.com/Kelbie/hunch)** — Semantic code review with Jev, plain-English rules and Agent Skills. <sub>(upstream description)</sub>
  <sub>`Project` · kelbie · `TS` · call site [`packages/core/src/jev.ts`](https://github.com/Kelbie/hunch/blob/HEAD/packages/core/src/jev.ts), read 2026-09-22</sub>

- **[jackalope](https://github.com/Jackalope-Dev/jackalope)** — A desktop workspace for coding agents, parallel Git worktrees, and code review. <sub>(upstream description)</sub>
  <sub>`Project` · jackalope-dev · `Rs` · call site [`apps/desktop/src-tauri/src/commands/jev.rs`](https://github.com/Jackalope-Dev/jackalope/blob/HEAD/apps/desktop/src-tauri/src/commands/jev.rs), read 2026-09-22</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.
  <sub>`Project` · Really Artificial · `JS` · `choice` · `score` · `noul` · call site [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs), read 2026-09-22 · ⚠ `AI-written`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能 <sub>(upstream description)</sub>
  <sub>`Plugin` · yuyang2230 · `Py` · call site [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py), read 2026-09-22</sub>

- **[jev-align](https://github.com/caiovicentino/jev-align)** — Calibrated alignment verifier for LLM responses and agent plans — powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · caiovicentino · `JS` · call site [`src/jev.mjs`](https://github.com/caiovicentino/jev-align/blob/HEAD/src/jev.mjs), read 2026-09-24</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local Responses proxy, with independent task verification. <sub>(upstream description)</sub>
  <sub>`Plugin` · minilv · `TS` · call site [`src/jev-adapter.ts`](https://github.com/miniLV/Jev-Auto-Router/blob/HEAD/src/jev-adapter.ts), read 2026-09-22</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verification. <sub>(upstream description)</sub>
  <sub>`Project` · rinnecoder · `Py` · call site [`behavior_study.py`](https://github.com/RINNECODER/jev-behavior-study/blob/HEAD/behavior_study.py), read 2026-09-22</sub>

- **[jev-bench](https://github.com/TheWayWithin/jev-bench)** — Does the cited source actually say it? A 42-claim benchmark: Jev (TypeSafe System One) against GPT-5.4, Claude Sonnet 5 and Gemini 3.1 Pro. <sub>(upstream description)</sub>
  <sub>`Benchmark` · thewaywithin · `Py` · call site [`run.py`](https://github.com/TheWayWithin/jev-bench/blob/HEAD/run.py), read 2026-09-24</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through. <sub>(upstream description)</sub>
  <sub>`Project` · ufec · `Kt` · call site [`app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt`](https://github.com/ufec/jev-block-android-ad/blob/HEAD/app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt), read 2026-09-22</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification. <sub>(upstream description)</sub>
  <sub>`Project` · aidil2105 · `Py` · call site [`src/jev_pilot/providers/jev.py`](https://github.com/aidil2105/jev-browser-pilot/blob/HEAD/src/jev_pilot/providers/jev.py), read 2026-09-22</sub>

- **[jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark)** — Comparing Jev, Gemini Flash, and Claude Fable on Python code review rules: cost, speed, accuracy, and consistency. Includes results, charts, and reproducible experiments. <sub>(upstream description)</sub>
  <sub>`Benchmark` · gemanor · `Py` · call site [`determinest/clients.py`](https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/determinest/clients.py), read 2026-09-24 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-codes](https://github.com/Kushwho/jev-codes)** — Audit your git diff against YAML coding-standards packs using TypeSafe's Jev model, from a CLI or your AI agent's command/skill. <sub>(upstream description)</sub>
  <sub>`Project` · kushwho · `TS` · call site [`src/scorer/jev.ts`](https://github.com/Kushwho/jev-codes/blob/HEAD/src/scorer/jev.ts), read 2026-09-24</sub>

- **[jev-debtgate](https://github.com/smlayero/jev-debtgate)** — Jev-powered technical debt gate for coding agents and CI. Bring your own TypeSafe API key. <sub>(upstream description)</sub>
  <sub>`Project` · smlayero · `TS` · call site [`src/jev.ts`](https://github.com/smlayero/jev-debtgate/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions-hermes)** — Jev Decisions Plugin for Hermes (and other AI Agents): tool risk reviews, human approval recommendations, evidence checks, and a local decision journal.
  <sub>`Plugin` · bojansandhaus · `Py` · call site [`jev_client.py`](https://github.com/bojansandhaus/jev-decisions-hermes/blob/HEAD/jev_client.py), read 2026-09-22</sub>

- **[jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric)** — Architecture for running many semantic decisions through one validated path, with a labelled 111-case benchmark comparing TypeSafe Jev against a Claude baseline, and a dashboard for inspecting any single decision. Experimental, not production. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ghubnab99 · `C#` · call site [`src/DecisionFabric.TypeSafe/TypeSafeClientOptions.cs`](https://github.com/ghubnab99/jev-enterprise-decision-fabric/blob/HEAD/src/DecisionFabric.TypeSafe/TypeSafeClientOptions.cs), read 2026-09-22</sub>

- **[jev-exploration](https://github.com/SamuelSacco/jev-exploration)** — Jev (TypeSafe) exploratory thread: claim audit, live demos, and runnable code <sub>(upstream description)</sub>
  <sub>`Benchmark` · samuelsacco · `Py` · call site [`jevlab/client.py`](https://github.com/SamuelSacco/jev-exploration/blob/HEAD/jevlab/client.py), read 2026-09-22</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies. <sub>(upstream description)</sub>
  <sub>`Project` · foadsf · `Py` · call site [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/HEAD/jev.py), read 2026-09-22</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves. <sub>(upstream description)</sub>
  <sub>`Plugin` · rashedint32 · `JS` · call site [`lib/jev.mjs`](https://github.com/rashedInt32/jev-gates/blob/HEAD/lib/jev.mjs), read 2026-09-22</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — Probability-scored guardrails for Claude Code: deny rule-breaking edits and unasked-for deploys, route your docs into each prompt, and check the final answer against the turn's own evidence. <sub>(upstream description)</sub>
  <sub>`Plugin` · muratcakmak · `TS` · call site [`scripts/jev-lint.ts`](https://github.com/muratcakmak/jev-guard/blob/HEAD/scripts/jev-lint.ts), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-labs](https://github.com/copyleftdev/jev-labs)** — Never confidently wrong: a TLA+-verified consensus kernel around TypeSafe's Jev, run through 1,680 chaos-tested pharmacy decisions with zero wrong verdicts. Film, code, and every captured call. <sub>(upstream description)</sub>
  <sub>`Project` · copyleftdev · `Py` · call site [`consensus/rust/consensus-kernel/src/jev.rs`](https://github.com/copyleftdev/jev-labs/blob/HEAD/consensus/rust/consensus-kernel/src/jev.rs), read 2026-09-22</sub>

- **[jev-lint](https://github.com/ckorhonen/jev-lint)** — Fuzzy linter for coding agents: after an agent writes a file, each of the team's plain-language rules is asked as a Jev noul, and about 0.3 s later the agent hears which rules it broke. Can generate rules from the repository; Cloudflare and OpenAI judges as alternatives.
  <sub>`Plugin` · ckorhonen · `TS` · `noul` · call site [`src/jev.ts`](https://github.com/ckorhonen/jev-lint/blob/HEAD/src/jev.ts)</sub>

- **[jev-lm](https://github.com/y0usaf/jev-lm)** — A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval <sub>(upstream description)</sub>
  <sub>`Project` · y0usaf · `TS` · call site [`python/jev_lm/api.py`](https://github.com/y0usaf/jev-lm/blob/HEAD/python/jev_lm/api.py), read 2026-09-22</sub>

- **[jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel)** — Catch breaking API behavior hidden in OpenAPI prose with deterministic checks and TypeSafe JEV System One semantic review. <sub>(upstream description)</sub>
  <sub>`Project` · shuhansun · `Py` · call site [`src/jev_oas_sentinel/jev.py`](https://github.com/ShuhanSun/jev-oas-sentinel/blob/HEAD/src/jev_oas_sentinel/jev.py), read 2026-09-22</sub>

- **[jev-pr-judge](https://github.com/juanegido/jev-pr-judge)** — Typed verdicts on pull requests with TypeSafe System One (Jev): one parallel call, policy in code, usable as a GitHub Action <sub>(upstream description)</sub>
  <sub>`Project` · juanegido · `TS` · call site [`dist/action/index.js`](https://github.com/juanegido/jev-pr-judge/blob/HEAD/dist/action/index.js), read 2026-09-24</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — A bounded Jev risk check for Claude Code: eight risk axes, one request, one optional reinspection. <sub>(upstream description)</sub>
  <sub>`Plugin` · muse0509 · `Go` · call site [`internal/jev/client.go`](https://github.com/muse0509/jev-preflight/blob/HEAD/internal/jev/client.go), read 2026-09-22</sub>

- **[jev-reasoning-navigator](https://github.com/AndreuVM/praxeon)** — JEV Reasoning Navigator: Cognitive supervision, loop prevention, and anti-hallucination engine for autonomous LLM agents using TypeSafe AI
  <sub>`Project` · andreuvm · `Py` · call site [`jev_navigator/core/typesafe_client.py`](https://github.com/AndreuVM/praxeon/blob/HEAD/jev_navigator/core/typesafe_client.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-resume-analyzer](https://github.com/awun8191/jev-resume-analyzer)** — CV diagnostics and job alignment with TypeSafe Jev, React and FastAPI <sub>(upstream description)</sub>
  <sub>`Project` · awun8191 · `Py` · call site [`backend/app/gateways/typesafe.py`](https://github.com/awun8191/jev-resume-analyzer/blob/HEAD/backend/app/gateways/typesafe.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-review](https://github.com/thiago-ss/jev-review)** — Autonomous Jev pull-request review with typed decisions, calibrated approval gates, and trusted-owner escalation <sub>(upstream description)</sub>
  <sub>`Project` · thiago-ss · `Py` · call site [`jev_review/provider.py`](https://github.com/thiago-ss/jev-review/blob/HEAD/jev_review/provider.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model. <sub>(upstream description)</sub>
  <sub>`Project` · fatwang2 · `JS` · call site [`src/jev.mjs`](https://github.com/fatwang2/jev-review-action/blob/HEAD/src/jev.mjs), read 2026-09-22</sub>

- **[jev-rust-review](https://github.com/kindintelligence/jev-rust-review)** — Rust-aware code review for Claude Code and coding agents, powered by TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · kindintelligence · `Rs` · call site [`src/jev.rs`](https://github.com/kindintelligence/jev-rust-review/blob/HEAD/src/jev.rs), read 2026-09-22</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — A small second eval for shadcn-ui/lint that uses TypeSafe's Jev to judge the linter's own output. <sub>(upstream description)</sub>
  <sub>`Project` · blas0 · `JS` · call site [`run-rule-cases.mjs`](https://github.com/blas0/jev-shadcn-lint-eval/blob/HEAD/run-rule-cases.mjs), read 2026-09-22</sub>

- **[jev-subtitle-translator](https://github.com/GeekLinkDev/jev-subtitle-translator)** — Translate SRT subtitles with structured LLM output and check every translation with Jev. <sub>(upstream description)</sub>
  <sub>`Project` · geeklinkdev · `Py` · call site [`src/jev_subtitle_translator/cli.py`](https://github.com/GeekLinkDev/jev-subtitle-translator/blob/HEAD/src/jev_subtitle_translator/cli.py), read 2026-09-24</sub>

- **[jev-the-janitor](https://github.com/kylehovance-ai/jev-the-janitor)** — A janitor for markdown vaults powered by TypeSafe Jev: Jev votes on each note, your code files it, you review the low-confidence pile.
  <sub>`Project` · kylehovance-ai · `Py` · call site [`janitor/client.py`](https://github.com/kylehovance-ai/jev-the-janitor/blob/HEAD/janitor/client.py), read 2026-09-22</sub>

- **[jev-verify](https://github.com/stillmarcus24/jev-verify)** — Check whether a published Jev output was actually produced by Jev. Implements the Yurin confidence identity; flags published fixtures that violate it. <sub>(upstream description)</sub>
  <sub>`Project` · stillmarcus24 · `JS` · call site [`scripts/live_confirm.cjs`](https://github.com/stillmarcus24/jev-verify/blob/HEAD/scripts/live_confirm.cjs), read 2026-09-24</sub>

- **[jevarena](https://github.com/chenmingtang830/jevarena)** — Open-source BYOK arena for Jev and other AI judges. Find failures, compare quality, cost, and latency. <sub>(upstream description)</sub>
  <sub>`Benchmark` · chenmingtang830 · `TS` · call site [`jevjudge/providers.py`](https://github.com/chenmingtang830/jevarena/blob/HEAD/jevjudge/providers.py), read 2026-09-24</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — Code-review gate for CI and coding agents: asks TypeSafe Jev small typed questions about functions, files, tests and docs, and reports findings with locations and probabilities <sub>(upstream description)</sub>
  <sub>`Project` · tech-byte-frontier · `Rs` · call site [`src/auth/provider.rs`](https://github.com/Tech-Byte-Frontier/jevgate/blob/HEAD/src/auth/provider.rs), read 2026-09-24</sub>

- **[jevguard](https://github.com/Jhonnyr97/JevGuard)** — Claude Code + Codex CLI plugin that verifies the agent follows project rules through a System One (Jev) model <sub>(upstream description)</sub>
  <sub>`Plugin` · jhonnyr97 · `TS` · call site [`dist/bin/jevguard-hook.js`](https://github.com/Jhonnyr97/JevGuard/blob/HEAD/dist/bin/jevguard-hook.js), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jevibe-check](https://github.com/sriganesh/jevibe-check)** — A live tone labeler for Bluesky posts and drafts, using TypeSafe's Jev API. <sub>(upstream description)</sub>
  <sub>`Project` · sriganesh · `JS` · call site [`extension/background.js`](https://github.com/sriganesh/jevibe-check/blob/HEAD/extension/background.js), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jevkit](https://github.com/ariel-frischer/jevkit)** — Fast Rust CLI for TypeSafe Jev: typed decisions, offline linting before you pay <sub>(upstream description)</sub>
  <sub>`Project` · ariel-frischer · `Rs` · call site [`src/auth.rs`](https://github.com/ariel-frischer/jevkit/blob/HEAD/src/auth.rs), read 2026-09-22</sub>

- **[jevsume](https://github.com/unownone/jevsume)** — ATS-friendly resume review powered by Jev (TypeSafe System One). The frontend extracts resume text the way a parser would, then a Cloudflare Worker runs typed JEV questions and composes a JevScore. <sub>(upstream description)</sub>
  <sub>`Project` · unownone · `TS` · call site [`packages/jev/http.ts`](https://github.com/unownone/jevsume/blob/HEAD/packages/jev/http.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[JevTest](https://github.com/CorieW/JevTest)** — Bounded exploratory browser testing with Jev, deterministic assertions, and replayable evidence. <sub>(upstream description)</sub>
  <sub>`Project` · coriew · `TS` · call site [`src/jev.ts`](https://github.com/CorieW/JevTest/blob/HEAD/src/jev.ts), read 2026-09-24 · ⚠ `one commit` `no licence`</sub>

- **[jevtest](https://github.com/realZachi/jevtest)** — Semantic test matchers for Vitest and Jest, powered by TypeSafe's Jev model. Write expectations in plain English, get calibrated probabilities back. <sub>(upstream description)</sub>
  <sub>`SDK` · realzachi · `TS` · call site [`packages/jevtest/src/types.ts`](https://github.com/realZachi/jevtest/blob/HEAD/packages/jevtest/src/types.ts), read 2026-09-24</sub>

- **[jod](https://github.com/mateonunez/jod)** — Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers. <sub>(upstream description)</sub>
  <sub>`Project` · mateonunez · `TS` · call site [`e2e/support.ts`](https://github.com/mateonunez/jod/blob/HEAD/e2e/support.ts), read 2026-09-22</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — A Stop hook that stops your coding agent from stopping too early. Plain-language rules, judged by jev. <sub>(upstream description)</sub>
  <sub>`Plugin` · noplan-inc · `Py` · call site [`limpet.py`](https://github.com/noplan-inc/limpet/blob/HEAD/limpet.py), read 2026-09-22</sub>

- **[lossless-rewrite](https://github.com/dttfrancesco/lossless-rewrite)** — AI text rewriting and document summarization with Jev checks for missing ideas and automatic repair. Local editor and CLI. <sub>(earlier upstream description)</sub>
  <sub>`Project` · dttfrancesco · `TS` · call site [`lib/decision/client.ts`](https://github.com/dttfrancesco/lossless-rewrite/blob/HEAD/lib/decision/client.ts), read 2026-09-24</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — n8n community node for Jev by TypeSafe AI: classify, score and check text with calibrated probabilities. Parallel requests and multi-item batching. <sub>(upstream description)</sub>
  <sub>`Project` · khmuhtadin · `TS` · call site [`nodes/JevClassification/JevClassification.node.ts`](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/HEAD/nodes/JevClassification/JevClassification.node.ts), read 2026-09-22</sub>

- **[omp-typesafe](https://github.com/siddicky/omp-typesafe)** — TypeSafe AI (Jev) adversarial reviewer and typesafe_ask tool for the omp coding agent <sub>(upstream description)</sub>
  <sub>`Plugin` · siddicky · `TS` · call site [`src/client.ts`](https://github.com/siddicky/omp-typesafe/blob/HEAD/src/client.ts), read 2026-09-24</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — Binary approval gate for Codex and Claude Code — every intercepted tool call is reviewed by TypeSafe JEV and composed through a versioned local policy, with scoped authorization. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · alexj11324 · `Go` · cited file [`internal/jev/client.go`](https://github.com/alexj11324/open-jev-approvals/blob/HEAD/internal/jev/client.go), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — Optional typed TypeSafe AI Jev decisions for OpenClaw, with SecretRef credentials and strict API validation. <sub>(upstream description)</sub>
  <sub>`Project` · olli0103 · `TS` · call site [`src/client.ts`](https://github.com/Olli0103/openclaw-typesafe-ai/blob/HEAD/src/client.ts), read 2026-09-22</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — Single-agent Pi coding coprocessor with Jev semantic gates, baseline-to-current diff review, and append-only observability telemetry. <sub>(upstream description)</sub>
  <sub>`Project` · kamilpostrozny · `TS` · call site [`src/index.ts`](https://github.com/KamilPostrozny/pi-jev-code/blob/HEAD/src/index.ts), read 2026-09-22</sub>

- **[plotveil](https://github.com/Dearest/plotveil)** — A quiet spoiler blocker for YouTube comments. One typed Jev (TypeSafe System One) Noul decision per comment; covered while checked, still covered if the check fails. <sub>(upstream description)</sub>
  <sub>`Project` · dearest · `TS` · call site [`scripts/evaluate-jev.ts`](https://github.com/Dearest/plotveil/blob/HEAD/scripts/evaluate-jev.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[profanity-checker](https://github.com/4rays/profanity-checker)** — Cloudflare Worker to check for profanity using TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · 4rays · `TS` · call site [`src/endpoints/profanityCheck.ts`](https://github.com/4rays/profanity-checker/blob/HEAD/src/endpoints/profanityCheck.ts), read 2026-09-22</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — Semantic assertions for pytest: test what your LLM app's output means, judged by TypeSafe's Jev.
  <sub>`Plugin` · allebee · `Py` · call site [`src/pytest_jev/judge.py`](https://github.com/allebee/pytest-jev/blob/HEAD/src/pytest_jev/judge.py), read 2026-09-22</sub>

- **[riff](https://github.com/scale-venture-partners/riff)** — A small, fast prose linter: ruff-style rule codes for writing, backed by TypeSafe's Jev model <sub>(upstream description)</sub>
  <sub>`Project` · scale-venture-partners · `Py` · call site [`src/riff/jev.py`](https://github.com/scale-venture-partners/riff/blob/HEAD/src/riff/jev.py), read 2026-09-22</sub>

- **[semantic-assert](https://github.com/mondaychen/semantic-assert)** — Testing lib for asserting the real requirement. <sub>(upstream description)</sub>
  <sub>`SDK` · mondaychen · `TS` · call site [`packages/semantic-assert-typesafe/src/client.ts`](https://github.com/mondaychen/semantic-assert/blob/HEAD/packages/semantic-assert-typesafe/src/client.ts), read 2026-09-24</sub>

- **[solvi](https://github.com/solvi-ai/solvi)** — Python runtime with a System One API adapter: Jev, an LLM or a local checkpoint proposes typed answers; hard checks, rules and calibrated thresholds decide, abstain or escalate to a person, and every decision is a hash-chained replayable trace.
  <sub>`SDK` · mxkuzn · `Py` · `choice` · `noul` · call site [`src/solvi/core/deciders/systemone.py`](https://github.com/solvi-ai/solvi/blob/HEAD/src/solvi/core/deciders/systemone.py), read 2026-10-23 · ⚠ `self-submitted`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — Every tool call your agent makes, checked before it runs. A Claude Code plugin that uses TypeSafe AI's Jev to verify each pending tool call against the session plan, then allows it, asks you, or blocks it. Proof of concept <sub>(upstream description)</sub>
  <sub>`Plugin` · getexcited · `TS` · call site [`lib/jev.ts`](https://github.com/getexcited/stepwarden/blob/HEAD/lib/jev.ts), read 2026-09-22 · ⚠ `one commit`</sub>

- **[system-one-playground](https://github.com/DonaldMurillo/system-one-playground)** — Readable scripting, semantic code checks, a Go System One client, and Studio. <sub>(upstream description)</sub>
  <sub>`Project` · donaldmurillo · `Go` · call site [`typesafe/client.go`](https://github.com/DonaldMurillo/system-one-playground/blob/HEAD/typesafe/client.go), read 2026-09-22</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score / Noul questions, lint them, measure on labelled data, and put calibrated thresholds in code <sub>(upstream description)</sub>
  <sub>`Plugin` · simota · `TS` · call site [`skills/tenbin/scripts/evaluate.py`](https://github.com/simota/tenbin/blob/HEAD/skills/tenbin/scripts/evaluate.py), read 2026-09-22</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — Judge every LLM response before the user sees it. AI SDK middleware and OpenAI-compatible proxy. <sub>(upstream description)</sub>
  <sub>`Integration` · noelzappy · `TS` · call site [`src/judge/jev.ts`](https://github.com/noelzappy/tripwire/blob/HEAD/src/judge/jev.ts), read 2026-09-22</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — Shadow-mode validation harness for a pre-execution firewall on AI agent tool calls (TypeSafe/Jev). Real run, findings in report.md. <sub>(upstream description)</sub>
  <sub>`Project` · anshchoudhary · `Py` · call site [`firewall/judge.py`](https://github.com/AnshChoudhary/typesafe-ai-firewall/blob/HEAD/firewall/judge.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — Unofficial community MCP plugin for Codex and Claude Code using TypeSafe Jev for bounded routing, ranking, extraction, verification, and escalation <sub>(upstream description)</sub>
  <sub>`Plugin` · e-fl · `JS` · call site [`server/judge.mjs`](https://github.com/E-FL/typesafe-as-a-judge/blob/HEAD/server/judge.mjs), read 2026-09-22</sub>

- **[typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review)** — About calibrating Jev for code reviews <sub>(upstream description)</sub>
  <sub>`Benchmark` · selmar · `Py` · call site [`calibrate.py`](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review/blob/HEAD/calibrate.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model) <sub>(upstream description)</sub>
  <sub>`Project` · opaielsheikh · `TS` · call site [`lib/typesafe.ts`](https://github.com/opaielsheikh/typesafe-migration-guard/blob/HEAD/lib/typesafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — Using Typesafe.AI to generate diff reviews. <sub>(upstream description)</sub>
  <sub>`Project` · rbalch · `Py` · call site [`src/typesafe_review/ask.py`](https://github.com/rbalch/typesafeai-review/blob/HEAD/src/typesafe_review/ask.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[zod-jev](https://github.com/jomatsu/zod-jev)** — Zod validates the shape; Jev validates the meaning. Semantic checks on a schema — personal data present? price plausible? category matches? — go to Jev in one request and come back as probabilities that become Zod issues.
  <sub>`SDK` · jomatsu · `TS` · call site [`src/types.ts`](https://github.com/jomatsu/zod-jev/blob/HEAD/src/types.ts), read 2026-09-24</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.
  <sub>`Benchmark` · Near Here</sub>

- **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)** — Collects the third-party evaluations that exist so far and frames the question of where a decision model can stand in for an LLM judge.
  <sub>`Article` · Laurie Voss</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
