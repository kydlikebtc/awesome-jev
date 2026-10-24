# Search & ranking

<sub>[awesome-jev](../../README.md) · [中文](search-ranking.zh-CN.md)</sub>

_Score or re-rank candidates from a cheaper retrieval step._

Every catalogued example of this decision — 65 of them. The same rows, with caveats, are in [the index](../../README.md#search--ranking); [the site](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#search-ranking): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 3 · call site 61 · wire shape 0 · example only 0 · independent reports 6 · negative results 1 · no file cited 4. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) <sub>`Official docs` · `Py`</sub>
- [Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find) <sub>`Official docs` · `Py` · `choice` · `noul`</sub>
- [Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) <sub>`Official docs` · `Py`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐ — Semantic search over a terms-of-service document: one request scores 218 line ids with a Choice, and a Noul checks whether the document answers at all.
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐ — Re-ranks 30-passage BM25 shortlists for 40 legal queries with one question per query-candidate pair, reporting large top-1 and top-10 gains.
  <sub>`Official docs` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★100k+ · `Py` · `choice` · `score` · `noul` · call site [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py), read 2026-09-22</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.
  <sub>`Project` · ★10k+ · `Py` · `choice` · `noul` · call site [`fastmcp_slim/fastmcp/experimental/transforms/jev_search.py`](https://github.com/PrefectHQ/fastmcp/blob/HEAD/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py), read 2026-09-22</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.
  <sub>`Project` · ★10k+ · `Rs` · `noul` · call site [`crates/jcode-base/src/jev.rs`](https://github.com/1jehuang/jcode/blob/HEAD/crates/jcode-base/src/jev.rs), read 2026-09-22</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)** — A vector-database reranker that asks one Noul per result and uses the yes-probability as an absolute relevance score, comparable across queries.
  <sub>`Project` · ★10k+ · `Py` · `noul` · call site [`python/python/lancedb/rerankers/typesafe.py`](https://github.com/lancedb/lancedb/blob/HEAD/python/python/lancedb/rerankers/typesafe.py), read 2026-09-22</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)** — One Noul per candidate document in a single batched request, with the yes-probability used directly as the relevance score.
  <sub>`Project` · ★10k+ · `Py` · `noul` · call site [`openviking/models/rerank/jev_rerank.py`](https://github.com/volcengine/OpenViking/blob/HEAD/openviking/models/rerank/jev_rerank.py), read 2026-09-22</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★1k+ · `Java` · `choice` · `score` · `noul` · call site [`app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/app/src/main/java/com/jev/probe/jev/JevQuestions.kt), read 2026-09-22</sub>

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)** — One Score per candidate file to pre-brief code review — measured twice, then removed: more billed input for essentially no wall-clock gain, and offline replay showed the candidate list could not reach where review findings land.
  <sub>`Benchmark` · ★1k+ · `Go` · `score` · author's conclusion: unfavourable (author-stated, not reproduced here)</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · call site [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql), read 2026-09-22</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends.
  <sub>`Project` · ★100+ · `TS` · `choice` · call site [`src/search.ts`](https://github.com/ellipsis-dev/blink/blob/HEAD/src/search.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.
  <sub>`Benchmark` · ★100+ · kitfunso · `TS` · call site [`src/rerankers/jev.ts`](https://github.com/kitfunso/hippo-memory/blob/HEAD/src/rerankers/jev.ts), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jegrep](https://github.com/can1357/jegrep)** — Semantic grep: find code by describing what you're looking for, powered by Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · can1357 · `Rs` · call site [`src/jev.rs`](https://github.com/can1357/jegrep/blob/HEAD/src/jev.rs), read 2026-09-22</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★100+ · `JS` · `choice` · `score` · `noul` · call site [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts), read 2026-09-22</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each.
  <sub>`Project` · ★100+ · `TS` · `choice` · `noul` · call site [`src/lib/typesafe.ts`](https://github.com/superagents-lab/jev-search/blob/HEAD/src/lib/typesafe.ts), read 2026-09-22</sub>

- **[jev-semgrep](https://github.com/uehaj/sys1grep)** — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · uehaj · `JS` · call site [`semgrep.mjs`](https://github.com/uehaj/sys1grep/blob/HEAD/semgrep.mjs), read 2026-09-22</sub>

- **[jev-shell-history](https://github.com/mrnugget/jev-shell-history)** — Fish-style zsh history autosuggestions, ranked by Jev rather than by recency.
  <sub>`Project` · ★100+ · mrnugget · `TS` · call site [`src/cli.ts`](https://github.com/mrnugget/jev-shell-history/blob/HEAD/src/cli.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jevgrep](https://github.com/nassim-arifette/jevgrep)** — Jev-powered semantic code search for coding agents — find behavior across repositories via CLI or MCP, with exact source excerpts and line numbers. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · nassim-arifette · `TS` · call site [`experiments/jev-contract/probe.mjs`](https://github.com/nassim-arifette/jevgrep/blob/HEAD/experiments/jev-contract/probe.mjs), read 2026-09-24</sub>

- **[jgrep](https://github.com/keltokhy/jgrep)** — grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · keltokhy · `Py` · call site [`bench/code_review.py`](https://github.com/keltokhy/jgrep/blob/HEAD/bench/code_review.py), read 2026-09-22</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following.
  <sub>`Project` · ★100+ · `Py` · `choice` · call site [`src/neo4jev/navigator.py`](https://github.com/jexp/neo4jev/blob/HEAD/src/neo4jev/navigator.py), read 2026-09-22</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — The pipe layer of an AI nervous system: one interface connecting provider neurons to an application, across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev or the open-weights Laya, not text.
  <sub>`Plugin` · ★100+ · juspay · `TS` · call site [`src/lib/providers/typesafe.ts`](https://github.com/juspay/neurolink/blob/HEAD/src/lib/providers/typesafe.ts), read 2026-09-22</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — Ranks an agent's skills for the next step using live session context, with Claude Code hooks.
  <sub>`Plugin` · ★100+ · dicklesworthstone · `Rs` · call site [`src/jev/endpoint.rs`](https://github.com/Dicklesworthstone/skillranker/blob/HEAD/src/jev/endpoint.rs), read 2026-09-22</sub>

- **[vector-graph-rag](https://github.com/zilliztech/vector-graph-rag)** — Graph RAG with pure vector search, achieving SOTA performance in multi-hop reasoning scenarios. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · zilliztech · `Py` · call site [`src/vector_graph_rag/llm/jev.py`](https://github.com/zilliztech/vector-graph-rag/blob/HEAD/src/vector_graph_rag/llm/jev.py), read 2026-09-22</sub>

- **[warrenduffer](https://github.com/arimanyus/warrenduffer)** — AI-driven intraday trading bot for Indian stocks. Jev ranks the Nifty 50 every 15s; code sizes each trade and places the stop; orders go live through Zerodha Kite or Kotak Neo. Day replay, kill switch, daily loss halt, terminal dashboard. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · arimanyus · `TS` · call site [`src/model/jev.ts`](https://github.com/arimanyus/warrenduffer/blob/HEAD/src/model/jev.ts), read 2026-09-24</sub>

- **[Cheshi](https://github.com/CheshiAI/Cheshi)** — Jev-powered conversation memory: find past sessions and revisit decisions with original sources. A macOS workspace for OpenAI Codex. Manage AI conversations and agents, explore code with CodeGraph, and work with Git, Ghostty terminals, and Apple Notes in one app. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · cheshiai · `C` · call site [`desktop/lib/typesafe-connection.mts`](https://github.com/CheshiAI/Cheshi/blob/HEAD/desktop/lib/typesafe-connection.mts), read 2026-09-24</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★10+ · keeltrace · `Py` · call site [`hermes_nerve/client.py`](https://github.com/keeltrace/hermes-nerve/blob/HEAD/hermes_nerve/client.py), read 2026-09-22</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · erendikmenn · `Py` · call site [`src/jev_rag_benchmark/rerankers.py`](https://github.com/erendikmenn/jev-rag-benchmark/blob/HEAD/src/jev_rag_benchmark/rerankers.py), read 2026-09-22 · author's conclusion: favourable (author-stated, not reproduced here)</sub>

- **[jev-recall](https://github.com/samdotmak/jev-recall)** — Retrieve by relevance, not resemblance: filter an AI assistant's memories with TypeSafe's Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · samdotmak · `TS` · call site [`src/jev_recall/core.py`](https://github.com/samdotmak/jev-recall/blob/HEAD/src/jev_recall/core.py), read 2026-09-22</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — An independent head-to-head against dedicated rerankers across fourteen datasets.
  <sub>`Benchmark` · ★10+ · anessbelbati · `Py` · call site [`rerankers/jev.py`](https://github.com/anessbelbati/jev-rerank-bench/blob/HEAD/rerankers/jev.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-reranker](https://github.com/hotchpotch/jev-reranker)** — Jev-powered relevance filtering and reranking for RAG in Python. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · hotchpotch · `Py` · call site [`src/jev_reranker/reranker.py`](https://github.com/hotchpotch/jev-reranker/blob/HEAD/src/jev_reranker/reranker.py), read 2026-09-24</sub>

- **[jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval)** — Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ★10+ · zhuyansen · `Py` · call site [`src/jse/openrouter.py`](https://github.com/zhuyansen/jev-search-rerank-eval/blob/HEAD/src/jse/openrouter.py), read 2026-09-24 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jevql](https://github.com/kylemclaren/jevql)** — Semantic SQL for Postgres, powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kylemclaren · `Go` · call site [`sdk/go/jevql.go`](https://github.com/kylemclaren/jevql/blob/HEAD/sdk/go/jevql.go), read 2026-09-22</sub>

- **[jevsearch](https://github.com/kylemclaren/jevsearch)** — A shadcn/ui ⌘K site-search block: a local keyword pass shows hits at once, then the top 20 go to Jev in one request (a Noul per candidate, a Choice for the best page, a Noul for whether any page answers) and are re-ordered or dropped; keyword order stands if TypeSafe is slow or down.
  <sub>`Project` · ★10+ · kylemclaren · `TS` · `noul` · `choice` · call site [`src/lib/jev-search-server.ts`](https://github.com/kylemclaren/jevsearch/blob/HEAD/src/lib/jev-search-server.ts), read 2026-09-23 · ⚠ `unverified claims` `self-submitted`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — grep for what code does: one Noul per code chunk, diff hunk or CSV row, printed as file:line hits with probabilities. --diff gates a PR in CI on a rule written in English (exit 0 match / 1 clean / 2 error); --tests lists the test files a diff can affect.
  <sub>`Project` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · call site [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts), read 2026-09-23 · ⚠ `unverified claims` `self-submitted`</sub>

- **[laya-jev-GraphRAG](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG)** — Agentic GraphRAG engine using swappable System One decision models (local Laya / cloud Jev). Features a complete 4-phase pipeline (Ingestion, Pre-Retrieval, Traversal, Post-Retrieval) and evaluation across Neo4j, Memgraph, Apache AGE, and Kùzu driven by a custom A* traversal algorithm.
  <sub>`Project` · ★10+ · bodepudimuneendra-netizen · `Py` · call site [`graphrag_neo4j_laya/graphrag/models/jev.py`](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG/blob/HEAD/graphrag_neo4j_laya/graphrag/models/jev.py), read 2026-09-24</sub>

- **[milvus-model](https://github.com/milvus-io/milvus-model)** — A library integrating embedding and reranker models from OpenAI, SentenceTransformers etc for semantic search in vector database. <sub>(upstream description)</sub>
  <sub>`Integration` · ★10+ · milvus-io · `Py` · call site [`src/pymilvus/model/reranker/jev.py`](https://github.com/milvus-io/milvus-model/blob/HEAD/src/pymilvus/model/reranker/jev.py), read 2026-09-24</sub>

- **[oko](https://github.com/bartlomein/oko)** — Code retrieval over MCP for Codex, Claude Code and OpenCode: hands an agent the relevant source snippets so it reads less irrelevant code.
  <sub>`Plugin` · ★10+ · bartlomein · `Rs` · call site [`scripts/benchmark-public/replay/replay.py`](https://github.com/bartlomein/oko/blob/HEAD/scripts/benchmark-public/replay/replay.py), read 2026-09-24 · ⚠ `unverified claims`</sub>

- **[pi-jev](https://github.com/madeye/pi-jev)** — Jev-assisted file retrieval and request caching for faster Pi workflows <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · madeye · `TS` · call site [`src/jev.ts`](https://github.com/madeye/pi-jev/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)** — Rank Pi Agent Skills for the current task with TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · safzanpirani · `TS` · call site [`extensions/jev.ts`](https://github.com/safzanpirani/pi-jev-skill-picker/blob/HEAD/extensions/jev.ts), read 2026-09-22</sub>

- **[transcript-lens](https://github.com/sensahin/transcript-lens)** — Explore YouTube transcripts by meaning: a Turkish interface, analysis by Jev, subtitle export and a Vercel deploy recipe.
  <sub>`Project` · ★10+ · sensahin · `TS` · call site [`src/lib/jev.ts`](https://github.com/sensahin/transcript-lens/blob/HEAD/src/lib/jev.ts), read 2026-09-24 · ⚠ `one commit`</sub>

- **[agent-seek](https://github.com/Gitmaxd/agent-seek)** — Agent Seek — precision web recall for agents. You.com discover + TypeSafe Jev ranking. MCP + REST. Live demo: https://agentseek.dev <sub>(upstream description)</sub>
  <sub>`Plugin` · gitmaxd · `Py` · call site [`packages/core/rank/jev.py`](https://github.com/Gitmaxd/agent-seek/blob/HEAD/packages/core/rank/jev.py), read 2026-09-24</sub>

- **[askgrep](https://github.com/fajarhide/askgrep)** — grep for the questions you cannot write as a pattern. Reads every function instead of sampling a few. Powered by Jev, TypeSafe AI's System One model. <sub>(upstream description)</sub>
  <sub>`Project` · fajarhide · `Rs` · call site [`src/jev.rs`](https://github.com/fajarhide/askgrep/blob/HEAD/src/jev.rs), read 2026-09-24</sub>

- **[clay-jev-people-ranker](https://github.com/promptgtm-shared/clay-jev-people-ranker)** — Agent Skill and Python workflow for Clay lead scoring, B2B prospect qualification, and people-search ranking with TypeSafe JEV. <sub>(upstream description)</sub>
  <sub>`Plugin` · promptgtm-shared · `Py` · call site [`scripts/rank_clay_people.py`](https://github.com/promptgtm-shared/clay-jev-people-ranker/blob/HEAD/scripts/rank_clay_people.py), read 2026-09-24</sub>

- **[every](https://github.com/sufianetaouil/every)** — Ask a yes/no question of every function in a codebase. Ranked answers in seconds, for cents. Grep whose pattern is a question, powered by TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · sufianetaouil · `Py` · call site [`reference/probe_jev.py`](https://github.com/sufianetaouil/every/blob/HEAD/reference/probe_jev.py), read 2026-09-22</sub>

- **[Jev RAG](https://github.com/aifabrice/jev-rag)** — Indexes local documents with SQLite FTS5/BM25, then asks one Jev Noul per candidate passage and sorts by the returned relevance probability before optionally generating a cited answer.
  <sub>`Project` · aifabrice · `Py` · `noul` · call site [`local_kb.py`](https://github.com/aifabrice/jev-rag/blob/HEAD/local_kb.py), read 2026-09-26 · ⚠ `3rd-party key` `AI-written` `self-submitted`</sub>

- **[jev-assist](https://github.com/glud123/jev-assist)** — Don't burn your expensive main model on grep-and-guess grunt work — let jev rank the whole repo, and save the main model for reading the right files and writing the right code.
  <sub>`Project` · glud123 · `JS` · call site [`scripts/jev.mjs`](https://github.com/glud123/jev-assist/blob/HEAD/scripts/jev.mjs), read 2026-09-22</sub>

- **[jev-bfs](https://github.com/komikat/jev-bfs)** — Wikipedia link races with direct Jev ranking and a live terminal display. <sub>(upstream description)</sub>
  <sub>`Project` · komikat · `Py` · call site [`jev_bfs/core.py`](https://github.com/komikat/jev-bfs/blob/HEAD/jev_bfs/core.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-nlgrep](https://github.com/YehuiTang0316/jev-nlgrep)** — Search code and text by meaning with natural-language grep, powered by Jev. <sub>(upstream description)</sub>
  <sub>`Project` · yehuitang0316 · `TS` · call site [`src/jev.ts`](https://github.com/YehuiTang0316/jev-nlgrep/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance. <sub>(upstream description)</sub>
  <sub>`Benchmark` · yodablocks · `Py` · call site [`harness/client.py`](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py), read 2026-09-22</sub>

- **[jev-reranker](https://github.com/shinpr/jev-reranker)** — Rerank, filter, and compress JSON search results with TypeSafe AI's Jev. <sub>(upstream description)</sub>
  <sub>`Project` · shinpr · `Rs` · call site [`src/http.rs`](https://github.com/shinpr/jev-reranker/blob/HEAD/src/http.rs), read 2026-09-22</sub>

- **[jev-retrieval](https://github.com/romeromarcelo/jev-retrieval)** — Semantic code and document search CLI — BM25 recall + TypeSafe Jev calibrated precision <sub>(upstream description)</sub>
  <sub>`Project` · romeromarcelo · `Rs` · call site [`src/jev/client.rs`](https://github.com/romeromarcelo/jev-retrieval/blob/HEAD/src/jev/client.rs), read 2026-09-24</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session. <sub>(upstream description)</sub>
  <sub>`Plugin` · shivampansuriya · `JS` · call site [`src/providers/typesafe.mjs`](https://github.com/ShivamPansuriya/jev-skill-gate/blob/HEAD/src/providers/typesafe.mjs), read 2026-09-24</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps. <sub>(upstream description)</sub>
  <sub>`Plugin` · hamakyo · `TS` · call site [`src/providers/jev-provider.ts`](https://github.com/hamakyo/jev-starter/blob/HEAD/src/providers/jev-provider.ts), read 2026-09-22</sub>

- **[jev.nvim](https://github.com/valentynkit/jev.nvim)** — Neovim: ask the buffer a question, get a quickfix list. Treesitter splits functions, Jev scores each one, probabilities land as virtual text <sub>(upstream description)</sub>
  <sub>`Plugin` · valentynkit · `Lua` · call site [`lua/jev/client.lua`](https://github.com/valentynkit/jev.nvim/blob/HEAD/lua/jev/client.lua), read 2026-09-24</sub>

- **[Jevflix](https://github.com/ArielBubis/Jevflix)** — Jev picks, you watch. A hybrid movie recommender: fast semantic + keyword search narrows 4,800 films to a shortlist, then TypeSafe Jev reads your constraints and picks the one film that fits - with a confidence score that decides whether to answer instantly or ask a follow-up. <sub>(upstream description)</sub>
  <sub>`Project` · arielbubis · `Py` · call site [`movie_rec/jev_client.py`](https://github.com/ArielBubis/Jevflix/blob/HEAD/movie_rec/jev_client.py), read 2026-09-24</sub>

- **[JevGPT: Thinking Fast and Slow in Autonomous Research](https://github.com/sunyasheng/JevGPT)** — Research agent from arXiv 2610.18272. GPT-5.5 plans searches and writes the answer; in BrowseComp-Plus QA, Jev answers a Choice over numbered source lines (where is the answer) and a Noul (does the region address it) per document region and query, in parallel. GPT gets the original lines.
  <sub>`Project` · sunyasheng · `TS` · `Py` · `choice` · `noul` · call site [`runtime/pi-serini/src/extensions/jev_find_v1.ts`](https://github.com/sunyasheng/JevGPT/blob/HEAD/runtime/pi-serini/src/extensions/jev_find_v1.ts) · ⚠ `3rd-party key` `unverified claims` `self-submitted`</sub>

- **[jevgrep](https://github.com/allebee/jevgrep)** — grep by meaning: pipe in any text, ask a yes/no question in plain English, get only the matching lines. Works behind tail -f, about $0.004 per 1,000 lines, powered by TypeSafe's Jev.
  <sub>`Project` · allebee · `Py` · call site [`src/jevgrep/judge.py`](https://github.com/allebee/jevgrep/blob/HEAD/src/jevgrep/judge.py), read 2026-09-22</sub>

- **[JevPDF](https://github.com/kylemclaren/jevpdf)** — Searches a PDF by meaning. pdf.js extracts each page's lines in the browser and Jev answers one Noul per line ("does this line answer the query?"), at most 16 lines per request with the page text as shared state. Lines at p ≥ 0.55 are highlighted in probability order; only text is sent to Jev.
  <sub>`Project` · kylemclaren · `TS` · `noul` · call site [`src/lib/jev-config.ts`](https://github.com/kylemclaren/jevpdf/blob/HEAD/src/lib/jev-config.ts), read 2026-09-23 · ⚠ `self-submitted`</sub>

- **[jfind](https://github.com/religa/jfind)** — Find files by describing them in plain English: find(1) with a semantic --like predicate, answered by TypeSafe.ai's jev model <sub>(upstream description)</sub>
  <sub>`Project` · religa · `Py` · call site [`src/jfind/matcher.py`](https://github.com/religa/jfind/blob/HEAD/src/jfind/matcher.py), read 2026-09-24</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
  <sub>`Project` · wiktorb2004 · `Py` · call site [`packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py`](https://github.com/WiktorB2004/llama-index-jev/blob/HEAD/packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py), read 2026-09-22</sub>

- **[pijev](https://github.com/tonyzdev/pijev)** — PiJev: a terminal coding agent with Jev in the loop — Jev ranks the repository's files before the first call, picks skills and triages failures; your coding model writes the code. Built on Pi. <sub>(upstream description)</sub>
  <sub>`Project` · tonyzdev · `TS` · call site [`src/jev.ts`](https://github.com/tonyzdev/pijev/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[sift](https://github.com/tylergibbs1/sift)** — Chrome extension that re-ranks Google results with TypeSafe Jev and folds away sales pages and SEO filler. <sub>(upstream description)</sub>
  <sub>`Plugin` · tylergibbs1 · `TS` · call site [`src/jev/client.ts`](https://github.com/tylergibbs1/sift/blob/HEAD/src/jev/client.ts), read 2026-09-24 · ⚠ `one commit`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — Unofficial community MCP plugin for Codex and Claude Code using TypeSafe Jev for bounded routing, ranking, extraction, verification, and escalation <sub>(upstream description)</sub>
  <sub>`Plugin` · e-fl · `JS` · call site [`server/judge.mjs`](https://github.com/E-FL/typesafe-as-a-judge/blob/HEAD/server/judge.mjs), read 2026-09-22</sub>

- **[typesafe-mod](https://github.com/BeLazy167/typesafe-mod)** — Claude Code mod that routes decisions to TypeSafe's Jev model: ranks installed skills per prompt, and answers the agent's own this-or-that questions when confident. <sub>(upstream description)</sub>
  <sub>`Plugin` · belazy167 · `TS` · call site [`hooks/suggest.ts`](https://github.com/BeLazy167/typesafe-mod/blob/HEAD/hooks/suggest.ts), read 2026-09-22</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
