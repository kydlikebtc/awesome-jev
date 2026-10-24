# Context compaction

<sub>[awesome-jev](../../README.md) · [中文](context-compaction.zh-CN.md)</sub>

_Decide which tool calls and results still matter so stale context can be dropped._

Every catalogued example of this decision — 36 of them. The same rows, with caveats, are in [the index](../../README.md#context-compaction); [the site](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#context-compaction): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 0 · call site 36 · wire shape 0 · example only 0 · independent reports 2 · negative results 2 · no file cited 0. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

The catalogue files nothing TypeSafe AI publishes under this pattern.

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it.
  <sub>`Benchmark` · ★100k+ · `Py` · `noul` · call site [`evals/compaction/jev_arm.py`](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/jev_arm.py), read 2026-09-22 · author's conclusion: unfavourable (author-stated, not reproduced here)</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.
  <sub>`Project` · ★10k+ · `Rs` · `noul` · call site [`crates/jcode-base/src/jev.rs`](https://github.com/1jehuang/jcode/blob/HEAD/crates/jcode-base/src/jev.rs), read 2026-09-22</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** — A Claude Code plugin that replaces the compaction summary with per-item decisions: stale tool calls are dropped or truncated, everything kept stays verbatim.
  <sub>`Plugin` · ★1k+ · tamaratran · `TS` · `noul` · call site [`src/request.ts`](https://github.com/tamaratran/fast-jev-compaction/blob/HEAD/src/request.ts), read 2026-09-22</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`jevkit/client.py`](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py), read 2026-09-22 · ⚠ `measured, not adopted`</sub>

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)** — "Work appears completed or recorded. Run /compact to save tokens." <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · kunchenguid · `TS` · call site [`packages/claude-mod/lib/judge.ts`](https://github.com/kunchenguid/compact-adviser/blob/HEAD/packages/claude-mod/lib/judge.ts), read 2026-09-22</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)** — Trims long shell output before the model sees it, asking one Noul per chunk.
  <sub>`Plugin` · ★100+ · tamaratran · `TS` · `noul` · call site [`src/jev.ts`](https://github.com/tamaratran/jev-pruner/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[mu](https://github.com/qybaihe/mu)** — Coding agent and desktop app built on pi that asks Jev at 38 decision points which tool-output chunks enter the context, which stale tool results to drop, whether a rule-flagged command was asked for and whether fetched pages or MCP output carry injected instructions.
  <sub>`Project` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · call site [`packages/kyrn-judge/src/providers/typesafe.ts`](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts) · ⚠ `self-submitted`</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)** — Context garbage collection for Claude Code: when Read, Bash or Grep dump a wall of output, each chunk is judged for relevance to the current task.
  <sub>`Plugin` · ★100+ · `Py` · `noul` · call site [`sidecar/src/winnow/judge.py`](https://github.com/GhalebDweikat/winnow/blob/HEAD/sidecar/src/winnow/judge.py), read 2026-09-22</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code plugin: Jev for rule checks, verbatim compaction, and prompt routing <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · 0x7067 · `Py` · call site [`scripts/jev.py`](https://github.com/0x7067/claude-jev/blob/HEAD/scripts/jev.py), read 2026-09-22</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gate completion claims inside DeepSeek Harness. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · horusjiang · `TS` · call site [`src/config.ts`](https://github.com/HorusJiang/dsh-jev-tools/blob/HEAD/src/config.ts), read 2026-09-24</sub>

- **[fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)** — Codex plugin: verbatim Jev-guided context restoration around session compaction. Port of tamaratran/fast-jev-compaction to Codex lifecycle hooks. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · leonaaardob · `TS` · call site [`src/request.ts`](https://github.com/leonaaardob/fast-dev-compaction/blob/HEAD/src/request.ts), read 2026-09-24</sub>

- **[jev-compact](https://github.com/fatelei/jev-compact)** — Jev-scored context compaction for OpenAI Codex CLI — scores every tool call before compaction and restores critical tool outputs verbatim after it <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · fatelei · `TS` · call site [`plugins/jev-compact/dist/fast-jev.mjs`](https://github.com/fatelei/jev-compact/blob/HEAD/plugins/jev-compact/dist/fast-jev.mjs), read 2026-09-24</sub>

- **[lcc](https://github.com/lucasmartins-ai/lcc)** — Local Context Compiler (lcc): clean, dedupe and compact prompt context before it reaches the model, then report every block dropped, the cache tokens a pass invalidates and when pruning pays off. Runs offline with a local 1K decision model. MIT, no API key, zero telemetry. <sub>(earlier upstream description)</sub>
  <sub>`Project` · ★10+ · lucasmartins-ai · `Py` · call site [`src/lcc/relevance/jev.py`](https://github.com/lucasmartins-ai/lcc/blob/HEAD/src/lcc/relevance/jev.py), read 2026-09-24</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jerryfane · `TS` · call site [`src/vendor/fast-jev/request.ts`](https://github.com/jerryfane/omp-jev-compaction/blob/HEAD/src/vendor/fast-jev/request.ts), read 2026-09-22</sub>

- **[pi-jev](https://github.com/iefnaf/pi-jev)** — Pi extension suite powered by Jev: selective context compaction and model routing <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · iefnaf · `TS` · call site [`src/vendor/fast-jev-compaction/request.ts`](https://github.com/iefnaf/pi-jev/blob/HEAD/src/vendor/fast-jev-compaction/request.ts), read 2026-09-24</sub>

- **[pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context)** — Model performance first. Token savings second. A Pi extension with freshness-aware read dedupe, Jev log filtering, and searchable verbatim recall. Keeps existing message history intact. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · nyarlathoteppppp · `TS` · call site [`bench/experimental/jev.ts`](https://github.com/Nyarlathoteppppp/pi-jev-context/blob/HEAD/bench/experimental/jev.ts), read 2026-09-22</sub>

- **[save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean)** — Portable, Jev-guided context compaction for coding agents: instead of an LLM rewriting old context into a lossy summary, Jev decides which tool calls and results still matter, and user and assistant text is kept verbatim.
  <sub>`Plugin` · ★10+ · iamunbounded · `TS` · call site [`src/cli.ts`](https://github.com/IAmUnbounded/save-token-jev-clean/blob/HEAD/src/cli.ts), read 2026-09-24</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · compozy · `TS` · call site [`benchmarks/jev-calibrate.ts`](https://github.com/compozy/yoshi/blob/HEAD/benchmarks/jev-calibrate.ts), read 2026-09-22</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — A pre-compaction advisor for DeepSeek Harness. Runs before the standard `compaction-basic` backend, using TypeSafe JEV to safely prune low-value tool results from model context. Original session events stay in the append-only log; only the model-visible view is replaced with compact markers or
  <sub>`Project` · wjw66 · `TS` · call site [`src/jev/protocol.ts`](https://github.com/wjw66/deepseek-harness-jev-pre-compaction/blob/HEAD/src/jev/protocol.ts), read 2026-09-22</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — Jev-judged context compaction for DeepSeek Harness: semantic tool-result pruning + deterministic receipt compaction <sub>(upstream description)</sub>
  <sub>`Project` · yangyu666 · `JS` · call site [`jev.js`](https://github.com/yangyu666/dsh-jev-prune/blob/HEAD/jev.js), read 2026-09-22</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM summaries with fast keep/truncate/drop decisions from jev-latest; everything kept stays verbatim. Port of tamaratran/fast-jev-compaction. <sub>(upstream description)</sub>
  <sub>`Project` · kolawong · `TS` · call site [`src/jev.ts`](https://github.com/kolawong/fast-compaction-dsh/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — Ten runnable JavaScript agent decisions, one file each: reconciling a new memory against a stored one, gating whether an HTTP 200 really satisfied the task, retry vs. reconcile after an uncertain write, scoring context against a budget, checking a handoff for dropped prohibitions.
  <sub>`Project` · Really Artificial · `JS` · `choice` · `score` · `noul` · call site [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs), read 2026-09-22 · ⚠ `AI-written`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — Context compaction for Hermes sessions that never summarises: every tool call is scored by TypeSafe's Jev model, stale calls are dropped, everything kept stays verbatim. <sub>(upstream description)</sub>
  <sub>`Project` · picaye · `JS` · call site [`hermes-compact.mjs`](https://github.com/picaye/jev-compaction/blob/HEAD/hermes-compact.mjs), read 2026-09-22</sub>

- **[jev-compaction](https://github.com/Waxmell114514/jev-compaction)** — A context compactor that can only score, never write — so an agent's memory can't hold a fact the transcript never contained. Working demo, runs offline. <sub>(upstream description)</sub>
  <sub>`Project` · waxmell114514 · `Py` · call site [`jevctx/jev.py`](https://github.com/Waxmell114514/jev-compaction/blob/HEAD/jevctx/jev.py), read 2026-09-24</sub>

- **[jev-docs](https://github.com/chenrui333/jev-docs)** — Community-maintained history of Jev / TypeSafe System One APIs, SDKs, agent guidance, and engineering best practices. <sub>(upstream description)</sub>
  <sub>`SDK` · chenrui333 · `Py` · call site [`src/jev_docs/sync.py`](https://github.com/chenrui333/jev-docs/blob/HEAD/src/jev_docs/sync.py), read 2026-09-22</sub>

- **[jevprune](https://github.com/ibrahemid/jevprune)** — Filter command output for coding agents using a task description. <sub>(upstream description)</sub>
  <sub>`Project` · ibrahemid · `TS` · call site [`src/typesafe-client.ts`](https://github.com/ibrahemid/jevprune/blob/HEAD/src/typesafe-client.ts), read 2026-09-24</sub>

- **[jit-context](https://github.com/wojciechwiesner/jit-context)** — Architectural Moat: JIT-JEV Context OS — Epistemic runtime & JEV System 1 context gate for AI agents (L0 SQLite WAL <3ms, Epistemic Invariants I1–I10, CERN Zenodo DOI: 10.5281/zenodo.22649542) <sub>(upstream description)</sub>
  <sub>`Project` · wojciechwiesner · `Py` · call site [`src/cognitive/jev_engine.py`](https://github.com/wojciechwiesner/jit-context/blob/HEAD/src/cognitive/jev_engine.py), read 2026-09-24</sub>

- **[jselect](https://github.com/keltokhy/jselect)** — Useful evidence for your AI, within a token budget. A fast, source-linked context selector for files, records, and agents. <sub>(upstream description)</sub>
  <sub>`Project` · keltokhy · `Py` · call site [`src/jselect/judge.py`](https://github.com/keltokhy/jselect/blob/HEAD/src/jselect/judge.py), read 2026-09-22</sub>

- **[pi-fast-jev-compaction](https://github.com/KamilPostrozny/pi-fast-jev-compaction)** — Fast JEV compaction extension for pi <sub>(upstream description)</sub>
  <sub>`Plugin` · kamilpostrozny · `TS` · call site [`extensions/fast-jev-core.ts`](https://github.com/KamilPostrozny/pi-fast-jev-compaction/blob/HEAD/extensions/fast-jev-core.ts), read 2026-09-22</sub>

- **[pi-fast-jev-compaction](https://github.com/QuentinDanblon/pi-fast-jev-compaction)** — Verbatim context pruning for the pi coding agent, scored by TypeSafe Jev: stale tool calls and results are dropped or truncated, everything kept stays verbatim. <sub>(upstream description)</sub>
  <sub>`Plugin` · quentindanblon · `TS` · call site [`vendor/fast-jev-compaction/dist/request.d.ts`](https://github.com/QuentinDanblon/pi-fast-jev-compaction/blob/HEAD/vendor/fast-jev-compaction/dist/request.d.ts), read 2026-09-24</sub>

- **[pi-jev-compact](https://github.com/ilkerulusoy/pi-jev-compact)** — Selective, verbatim context compaction for Pi: Jev scores every tool call and result, unneeded calls are dropped and the rest stays verbatim, with no LLM-written summary.
  <sub>`Plugin` · ilkerulusoy · `TS` · call site [`src/core/jev.ts`](https://github.com/ilkerulusoy/pi-jev-compact/blob/HEAD/src/core/jev.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[pi-jev-compaction](https://github.com/nourhelmi/pi-jev-compaction)** — Automatic Jev context clearing for Pi. Keep the conversation, prune stale tool output, retrieve originals without rerunning commands. <sub>(upstream description)</sub>
  <sub>`Plugin` · nourhelmi · `TS` · call site [`src/pruning.ts`](https://github.com/nourhelmi/pi-jev-compaction/blob/HEAD/src/pruning.ts), read 2026-09-24</sub>

- **[pi-jev-context](https://github.com/kevinpita/pi-jev-context)** — Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history. <sub>(upstream description)</sub>
  <sub>`Plugin` · kevinpita · `TS` · call site [`src/jev.ts`](https://github.com/kevinpita/pi-jev-context/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[pi-jev-context-curator](https://github.com/Shashank-H/pi-jev-context-curator)** — A Jev based context curator for pi <sub>(upstream description)</sub>
  <sub>`Plugin` · shashank-h · `TS` · call site [`extensions/curator-jev/config.ts`](https://github.com/Shashank-H/pi-jev-context-curator/blob/HEAD/extensions/curator-jev/config.ts), read 2026-09-24</sub>

- **[Quicksilver](https://github.com/UditAkhourii/quicksilver)** — Claude Code skill that hands relevance calls to Jev: one noul per file, log line or ticket ('which of these files handle auth?'), asked in parallel and sorted by probability, so Claude gets a shortlist with confidences instead of reading everything.
  <sub>`Plugin` · uditakhourii · `JS` · `noul` · call site [`skills/quicksilver/scripts/qs.mjs`](https://github.com/UditAkhourii/quicksilver/blob/HEAD/skills/quicksilver/scripts/qs.mjs)</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** — Synthetic smoking-history extraction benchmark comparing TypeSafe Jev and OpenAI structured outputs, with reproducible accuracy, cost, and latency results. <sub>(upstream description)</sub>
  <sub>`Benchmark` · vclic · `Py` · call site [`smoking_eval/providers.py`](https://github.com/vclic/smoking-extraction-benchmark/blob/HEAD/smoking_eval/providers.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
