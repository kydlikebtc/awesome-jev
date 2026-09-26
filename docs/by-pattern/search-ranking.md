# Search & ranking

<sub>[awesome-jev](../../README.md) · [中文](search-ranking.zh-CN.md)</sub>

_Score or re-rank candidates from a cheaper retrieval step._

Every catalogued example of this decision — 64 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#search--ranking); [the site](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=en) can filter them further by language, primitive and kind.

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐ — Semantic search over a terms-of-service document: one request scores 218 line ids with a Choice, and a Noul checks whether the document answers at all.
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐ — Re-ranks 30-passage BM25 shortlists for 40 legal queries with one question per query-candidate pair, reporting large top-1 and top-10 gains.
  <sub>`Official docs` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)** — One Noul per candidate document in a single batched request, with the yes-probability used directly as the relevance score.
  <sub>`Project` · ★38,571 · `Py` · `noul`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.
  <sub>`Project` · ★27,886 · `Py` · `choice` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.
  <sub>`Project` · ★20,069 · `Rs` · `noul`</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)** — A vector-database reranker that asks one Noul per result and uses the yes-probability as an absolute relevance score, comparable across queries.
  <sub>`Project` · ★11,513 · `Py` · `noul`</sub>

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)** — One Score per candidate file to pre-brief code review — measured twice, then removed: more billed input for essentially no wall-clock gain, and offline replay showed the candidate list could not reach where review findings land.
  <sub>`Benchmark` · ★8,617 · `Go` · `score`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★5,414 · `Java` · `choice` · `score` · `noul`</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.
  <sub>`Benchmark` · ★756 · kitfunso · `TS`</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each.
  <sub>`Project` · ★443 · `TS` · `choice` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★324 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[vector-graph-rag](https://github.com/zilliztech/vector-graph-rag)** — Graph RAG with pure vector search, achieving SOTA performance in multi-hop reasoning scenarios.
  <sub>`Project` · ★248 · zilliztech · `Py`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — The pipe layer of an AI nervous system: one interface connecting provider neurons to an application, across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev or the open-weights Laya, not text.
  <sub>`Plugin` · ★139 · juspay · `TS`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる
  <sub>`Project` · ★134 · uehaj · `JS`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following.
  <sub>`Project` · ★126 · `Py` · `choice`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — Ranks an agent's skills for the next step using live session context, with Claude Code hooks.
  <sub>`Plugin` · ★116 · dicklesworthstone · `Rs`</sub>

- **[jev-shell-history](https://github.com/mrnugget/jev-shell-history)** — Fish-style zsh history autosuggestions, ranked by Jev rather than by recency.
  <sub>`Project` · ★108 · mrnugget · `TS` · ⚠ `no licence`</sub>

- **[jegrep](https://github.com/can1357/jegrep)** — Semantic grep: find code by describing what you're looking for, powered by Jev.
  <sub>`Project` · ★87 · can1357 · `Rs`</sub>

- **[warrenduffer](https://github.com/arimanyus/warrenduffer)** — AI-driven intraday trading bot for Indian stocks. Jev ranks the Nifty 50 every 15s; code sizes each trade and places the stop; orders go live through Zerodha Kite or Kotak Neo. Day replay, kill switch, daily loss halt, terminal dashboard.
  <sub>`Project` · ★86 · arimanyus · `TS`</sub>

- **[jgrep](https://github.com/keltokhy/jgrep)** — grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.
  <sub>`Project` · ★74 · keltokhy · `Py`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends.
  <sub>`Project` · ★69 · `TS` · `choice` · ⚠ `no licence`</sub>

- **[jevgrep](https://github.com/nassim-arifette/jevgrep)** — Jev-powered semantic code search for coding agents — find behavior across repositories via CLI or MCP, with exact source excerpts and line numbers.
  <sub>`Plugin` · ★62 · nassim-arifette · `TS`</sub>

- **[milvus-model](https://github.com/milvus-io/milvus-model)** — A library integrating embedding and reranker models from OpenAI, SentenceTransformers etc for semantic search in vector database.
  <sub>`Integration` · ★60 · milvus-io · `Py`</sub>

- **[jev-recall](https://github.com/samdotmak/jev-recall)** — Retrieve by relevance, not resemblance: filter an AI assistant's memories with TypeSafe's Jev
  <sub>`Project` · ★33 · samdotmak · `TS`</sub>

- **[pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)** — Rank Pi Agent Skills for the current task with TypeSafe Jev
  <sub>`Plugin` · ★30 · safzanpirani · `TS`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — grep for what code does: one Noul per code chunk, diff hunk or CSV row, printed as file:line hits with probabilities. --diff gates a PR in CI on a rule written in English (exit 0 match / 1 clean / 2 error); --tests lists the test files a diff can affect.
  <sub>`Project` · ★24 · kyu1204 · `TS` · `noul` · `choice` · `score` · ⚠ `unverified claims`</sub>

- **[laya-jev-GraphRAG](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG)** — Agentic GraphRAG engine using swappable System One decision models (local Laya / cloud Jev). Features a complete 4-phase pipeline (Ingestion, Pre-Retrieval, Traversal, Post-Retrieval) and evaluation across Neo4j, Memgraph, Apache AGE, and Kùzu driven by a custom A* traversal algorithm.
  <sub>`Project` · ★22 · bodepudimuneendra-netizen · `Py`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★20 · keeltrace · `Py`</sub>

- **[jev-reranker](https://github.com/hotchpotch/jev-reranker)** — Jev-powered relevance filtering and reranking for RAG in Python.
  <sub>`Project` · ★20 · hotchpotch · `Py`</sub>

- **[Cheshi](https://github.com/CheshiAI/Cheshi)** — Jev-powered conversation memory: find past sessions and revisit decisions with original sources. A macOS workspace for OpenAI Codex. Manage AI conversations and agents, explore code with CodeGraph, and work with Git, Ghostty terminals, and Apple Notes in one app.
  <sub>`Plugin` · ★18 · cheshiai · `C`</sub>

- **[transcript-lens](https://github.com/sensahin/transcript-lens)** — Explore YouTube transcripts by meaning: a Turkish interface, analysis by Jev, subtitle export and a Vercel deploy recipe.
  <sub>`Project` · ★17 · sensahin · `TS`</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG
  <sub>`Benchmark` · ★14 · erendikmenn · `Py`</sub>

- **[jevql](https://github.com/kylemclaren/jevql)** — Semantic SQL for Postgres, powered by Jev
  <sub>`Project` · ★12 · kylemclaren · `Go`</sub>

- **[pi-jev](https://github.com/madeye/pi-jev)** — Jev-assisted file retrieval and request caching for faster Pi workflows
  <sub>`Plugin` · ★11 · madeye · `TS`</sub>

- **[every](https://github.com/sufianetaouil/every)** — Ask a yes/no question of every function in a codebase. Ranked answers in seconds, for cents. Grep whose pattern is a question, powered by TypeSafe Jev.
  <sub>`Project` · ★7 · sufianetaouil · `Py`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — An independent head-to-head against dedicated rerankers across fourteen datasets.
  <sub>`Benchmark` · ★7 · anessbelbati · `Py`</sub>

- **[jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval)** — Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured.
  <sub>`Benchmark` · ★6 · zhuyansen · `Py`</sub>

- **[oko](https://github.com/bartlomein/oko)** — Code retrieval over MCP for Codex, Claude Code and OpenCode: hands an agent the relevant source snippets so it reads less irrelevant code.
  <sub>`Plugin` · ★6 · bartlomein · `Rs` · ⚠ `unverified claims`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session.
  <sub>`Plugin` · ★5 · shivampansuriya · `JS`</sub>

- **[jev.nvim](https://github.com/valentynkit/jev.nvim)** — Neovim: ask the buffer a question, get a quickfix list. Treesitter splits functions, Jev scores each one, probabilities land as virtual text
  <sub>`Plugin` · ★5 · valentynkit · `Lua`</sub>

- **[jevsearch](https://github.com/kylemclaren/jevsearch)** — A shadcn/ui ⌘K site-search block: a local keyword pass shows hits at once, then the top 20 go to Jev in one request (a Noul per candidate, a Choice for the best page, a Noul for whether any page answers) and are re-ordered or dropped; keyword order stands if TypeSafe is slow or down.
  <sub>`Project` · ★5 · kylemclaren · `TS` · `noul` · `choice` · ⚠ `unverified claims`</sub>

- **[askgrep](https://github.com/fajarhide/askgrep)** — grep for the questions you cannot write as a pattern. Reads every function instead of sampling a few. Powered by Jev, TypeSafe AI's System One model.
  <sub>`Project` · ★4 · fajarhide · `Rs`</sub>

- **[jev-nlgrep](https://github.com/YehuiTang0316/jev-nlgrep)** — Search code and text by meaning with natural-language grep, powered by Jev.
  <sub>`Project` · ★4 · yehuitang0316 · `TS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
  <sub>`Project` · ★4 · wiktorb2004 · `Py`</sub>

- **[pijev](https://github.com/tonyzdev/pijev)** — PiJev: a terminal coding agent with Jev in the loop — Jev ranks the repository's files before the first call, picks skills and triages failures; your coding model writes the code. Built on Pi.
  <sub>`Project` · ★4 · tonyzdev · `TS`</sub>

- **[jev-assist](https://github.com/glud123/jev-assist)** — Don't burn your expensive main model on grep-and-guess grunt work — let jev rank the whole repo, and save the main model for reading the right files and writing the right code.
  <sub>`Project` · ★3 · glud123 · `JS`</sub>

- **[jev-reranker](https://github.com/shinpr/jev-reranker)** — Rerank, filter, and compress JSON search results with TypeSafe AI's Jev.
  <sub>`Project` · ★3 · shinpr · `Rs`</sub>

- **[typesafe-mod](https://github.com/BeLazy167/typesafe-mod)** — Claude Code mod that routes decisions to TypeSafe's Jev model: ranks installed skills per prompt, and answers the agent's own this-or-that questions when confident.
  <sub>`Plugin` · ★3 · belazy167 · `TS`</sub>

- **[agent-seek](https://github.com/Gitmaxd/agent-seek)** — Agent Seek — precision web recall for agents. You.com discover + TypeSafe Jev ranking. MCP + REST. Live demo: https://agentseek.dev
  <sub>`Plugin` · ★2 · gitmaxd · `Py`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.
  <sub>`Plugin` · ★2 · hamakyo · `TS`</sub>

- **[JevPDF](https://github.com/kylemclaren/jevpdf)** — Searches a PDF by meaning. pdf.js extracts each page's lines in the browser and Jev answers one Noul per line ("does this line answer the query?"), at most 16 lines per request with the page text as shared state. Lines at p ≥ 0.55 are highlighted in probability order; only text is sent to Jev.
  <sub>`Project` · ★2 · kylemclaren · `TS` · `noul`</sub>

- **[jfind](https://github.com/religa/jfind)** — Find files by describing them in plain English: find(1) with a semantic --like predicate, answered by TypeSafe.ai's jev model
  <sub>`Project` · ★2 · religa · `Py`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — Unofficial community MCP plugin for Codex and Claude Code using TypeSafe Jev for bounded routing, ranking, extraction, verification, and escalation
  <sub>`Plugin` · ★2 · e-fl · `JS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — The decision layer for AI agents. Typed, calibrated decisions in ~400ms for two hundredths of a cent: gate tool calls, route models, rank options. With the 300-call injection test that found what breaks.
  <sub>`Project` · ★1 · eugeniughelbur · `Py`</sub>

- **[jevgrep](https://github.com/allebee/jevgrep)** — grep by meaning: pipe in any text, ask a yes/no question in plain English, get only the matching lines. Works behind tail -f, about $0.004 per 1,000 lines, powered by TypeSafe's Jev.
  <sub>`Project` · ★1 · allebee · `Py`</sub>

- **[clay-jev-people-ranker](https://github.com/promptgtm-shared/clay-jev-people-ranker)** — Agent Skill and Python workflow for Clay lead scoring, B2B prospect qualification, and people-search ranking with TypeSafe JEV.
  <sub>`Plugin` · ★0 · promptgtm-shared · `Py`</sub>

- **[jev-bfs](https://github.com/komikat/jev-bfs)** — Wikipedia link races with direct Jev ranking and a live terminal display.
  <sub>`Project` · ★0 · komikat · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jev-retrieval](https://github.com/romeromarcelo/jev-retrieval)** — Semantic code and document search CLI — BM25 recall + TypeSafe Jev calibrated precision
  <sub>`Project` · ★0 · romeromarcelo · `Rs`</sub>

- **[Jevflix](https://github.com/ArielBubis/Jevflix)** — Jev picks, you watch. A hybrid movie recommender: fast semantic + keyword search narrows 4,800 films to a shortlist, then TypeSafe Jev reads your constraints and picks the one film that fits - with a confidence score that decides whether to answer instantly or ask a follow-up.
  <sub>`Project` · ★0 · arielbubis · `Py`</sub>

- **[sift](https://github.com/tylergibbs1/sift)** — Chrome extension that re-ranks Google results with TypeSafe Jev and folds away sales pages and SEO filler.
  <sub>`Plugin` · ★0 · tylergibbs1 · `TS`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
