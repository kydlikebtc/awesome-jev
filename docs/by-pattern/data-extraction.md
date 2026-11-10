# Structured extraction

<sub>[awesome-jev](../../README.md) · [中文](data-extraction.zh-CN.md)</sub>

_Pull typed fields out of messy text by choosing among candidates rather than generating them._

Every catalogued example of this decision — 25 of them. The same rows, with caveats, are in [the index](../../README.md#structured-extraction); [the site](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#data-extraction): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 4 · call site 21 · wire shape 0 · example only 0 · independent reports 3 · negative results 0 · no file cited 4. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) <sub>`Official docs` · `Py`</sub>
- [Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) <sub>`Official docs` · `Py` · `choice`</sub>
- [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) <sub>`Official docs` · `Py`</sub>
- [Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) <sub>`Official docs` · `Py`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

- **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐ — Extracts absolute and relative dates by asking for the parts a document names, then resolving and validating them in code with confidence-based review.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐ — Regexes find candidate emails, phone numbers and amounts; the model selects the requested span so code can normalise a verbatim value.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost.
  <sub>`Official docs` · `Py`</sub>

- **[jev4pg](https://github.com/Sheltercosmo/jev4pg)** — Natural-language SQL and 41 semantic operators for PostgreSQL. Filtering, extraction, ranking, matching and verification go to Jev in bounded batches with validated answers; a choice option needs 0.55 and a noul 0.8 to count. The authors report 98% accuracy against 92% for pg-jev's request path. <sub>(written by a model)</sub>
  <sub>`Project` · ★100+ · Sheltercosmo · `Py` · `choice` · `noul` · call site [`sdd/generic/jev.py`](https://github.com/Sheltercosmo/jev4pg/blob/HEAD/sdd/generic/jev.py), read by a model 2026-10-26 · ⚠ `vendor numbers`</sub>

- **[jev playground (deepdave98)](https://github.com/deepdave98/jev-playground)** — Weekly go-to-market experiments with Jev, each tested against Claude: lead triage and routing, deal risk, reply triage, MEDDPICC fields from call summaries, duplicate accounts and closed-lost reactivation, plus an MCP server. A shared client subtracts a measured score bias of 0.30 before rounding. <sub>(written by a model)</sub>
  <sub>`Benchmark` · ★10+ · deepdave98 · `Py` · `noul` · `choice` · `score` · call site [`common/jev.py`](https://github.com/deepdave98/jev-playground/blob/HEAD/common/jev.py), read by a model 2026-10-31 · ⚠ `no licence`</sub>

- **[jev-apply](https://github.com/theadaply/jev-apply)** — Job-application skill for CLI agents with a memory of your answers: Jev picks which saved answer fills each field of a Greenhouse, Ashby or Lever form, with an explicit none-of-these exit, and below a confidence threshold the field goes back to you instead of being guessed. <sub>(written by a model)</sub>
  <sub>`Plugin` · ★10+ · theadaply · `JS` · `choice` · `noul` · call site [`src/jev/client.mjs`](https://github.com/theadaply/jev-apply/blob/HEAD/src/jev/client.mjs), read by a model 2026-11-03</sub>

- **[jev-design](https://github.com/bilune/jev-design)** — Experiment in having Jev design a dashboard: from a one-sentence brief like "an 18th century printed book", two staged requests of choice, score and yes/no questions pick every visual token (colour, type, radius, icons) from a catalog a person wrote, and an engine applies them to a Next.js console. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · bilune · `TS` · `choice` · `score` · `noul` · call site [`src/design/jev/generate.ts`](https://github.com/bilune/jev-design/blob/HEAD/src/design/jev/generate.ts), read by a model 2026-10-30 · ⚠ `no licence`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Computer-use agent for native macOS apps on Apple silicon: OmniParser CoreML, Apple Vision OCR and accessibility labels find a window's controls locally, and Jev picks the next action with a choice from the observed text, never pixels. Input is guarded, and benchmarks check results, not Jev's DONE. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · jcpsimmons · `JS` · call site [`src/providers.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs), read 2026-09-22</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — Text extraction with Jev: field extraction, PII detection and exact quotes, built on TypeSafe's Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · jkrup · `JS` · call site [`src/client.mjs`](https://github.com/jkrup/jeveryword/blob/HEAD/src/client.mjs), read 2026-09-22</sub>

- **[jevfill](https://github.com/imohitmayank/jevfill)** — A Chrome extension that fills web forms from unstructured notes with Jev: paste your details once as plain text, with no structured profile, then fill forms on demand.
  <sub>`Plugin` · ★10+ · imohitmayank · `TS` · call site [`src/jev/client.ts`](https://github.com/imohitmayank/jevfill/blob/HEAD/src/jev/client.ts), read 2026-09-24</sub>

- **[JevNext](https://github.com/bring-ai/jevnext)** — Gets numbers out of Jev with ordinary Choice calls: each call picks a sub-interval or the next decimal digit, walking a multiway tree down to a finite-precision value, with no training or logits. Demonstrated on arithmetic, token billing and continuous game control such as CarRacing and LunarLander. <sub>(written by a model)</sub>
  <sub>`Project` · ★10+ · bring-ai · `Py` · `choice` · call site [`src/jev_numeric/client.py`](https://github.com/bring-ai/jevnext/blob/HEAD/src/jev_numeric/client.py), read by a model 2026-11-04</sub>

- **[JevSpan](https://github.com/lzq-0529/jev-span)** — Zero-shot named entity recognition for Chinese and English: code enumerates candidate spans at punctuation, and Jev choice questions nominate a window per entity type, verify each nominee (type, none, mixed or partial) and pick its exact boundary, keeping each entity's probability.
  <sub>`Project` · ★10+ · lzq-0529 · `Py` · `choice` · call site [`src/jevspan/jev_client.py`](https://github.com/lzq-0529/jev-span/blob/HEAD/src/jevspan/jev_client.py), read 2026-09-30 · ⚠ `AI-written` `self-submitted`</sub>

- **[smart-paste](https://github.com/nomanjack/smart-paste)** — Fills form fields from pasted text: the form's heading, labels and your text go to TypeSafe, and it inserts the values it matches for you to review before submitting.
  <sub>`Plugin` · ★10+ · nomanjack · `JS` · call site [`worker.js`](https://github.com/nomanjack/smart-paste/blob/HEAD/worker.js), read 2026-09-24</sub>

- **[ask-jev](https://github.com/logicrw/ask-jev)** — Standard-library CLI that hands an agent's small judgments to Jev within a 280 ms advisory budget: choose (a choice), check (a noul on whether evidence shows a claim), score, a batch of at most 32, and purify, a noul per passage keeping only relevant original lines. Fails open; the agent decides. <sub>(written by a model)</sub>
  <sub>`Project` · logicrw · `Py` · call site [`scripts/jev_context.py`](https://github.com/logicrw/ask-jev/blob/HEAD/scripts/jev_context.py), read 2026-09-24</sub>

- **[ContextGem](https://github.com/shcherbak-ai/contextgem)** — Python framework that extracts structured data from documents with LLMs and decision models. Given a decision model such as Jev, it asks a yes/no question per paragraph to find each aspect's clauses and turns Boolean, label and rating concepts into noul, choice and score questions. <sub>(written by a model)</sub>
  <sub>`Project` · shcherbak-ai · `Py` · `noul` · `choice` · `score` · call site [`contextgem/internal/base/decision_models.py`](https://github.com/shcherbak-ai/contextgem/blob/HEAD/contextgem/internal/base/decision_models.py), read by a model 2026-11-06</sub>

- **[Jev × DimABSA](https://github.com/zhangyiqun018/jev-dimabsa)** — SemEval-2026 Task 3 (DimABSA) system built on Jev alone, without generation or fine-tuning: scores place each aspect's valence and arousal on a 1 to 9 scale, and choices and nouls pull out aspect, opinion and category triplets and quadruplets. <sub>(written by a model)</sub>
  <sub>`Benchmark` · zhangyiqun018 · `Py` · `score` · `choice` · `noul` · call site [`jev/client.py`](https://github.com/zhangyiqun018/jev-dimabsa/blob/HEAD/jev/client.py), read by a model 2026-11-10 · ⚠ `no licence`</sub>

- **[jev-data-questions](https://github.com/narulaskaran/jev-data-questions)** — Bring a dataset and see the right chart: the UI inspects the CSV's shape and proposes insights, and Jev fills in the values.
  <sub>`Project` · narulaskaran · `TS` · call site [`src/server/jev.ts`](https://github.com/narulaskaran/jev-data-questions/blob/HEAD/src/server/jev.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction)** — Parsing the PDF and extracting the relevant information <sub>(upstream description)</sub>
  <sub>`Project` · abhishekmamdapure · `Py` · call site [`backend/main.py`](https://github.com/abhishekmamdapure/jev-information-extraction/blob/HEAD/backend/main.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-mcp-dispatcher](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher)** — Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence. <sub>(upstream description)</sub>
  <sub>`Plugin` · abhishekashokvkumar · `Py` · call site [`jev_mcp_dispatcher.py`](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher/blob/HEAD/jev_mcp_dispatcher.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[JEVsnap](https://github.com/brainstormity/jevsnap)** — Screenshot hotkey for macOS, Linux and Windows that blacks out secrets and personal data before the image reaches the clipboard: after local rules, Jev answers nouls on which OCR lines and words to hide, and an optional check finds what is left with box questions. <sub>(written by a model)</sub>
  <sub>`Project` · brainstormity · `TS` · `noul` · `choice` · call site [`desktop/src/core/jevClient.ts`](https://github.com/brainstormity/jevsnap/blob/HEAD/desktop/src/core/jevClient.ts), read by a model 2026-11-10</sub>

- **[jevsume](https://github.com/unownone/jevsume)** — ATS-friendly resume review powered by Jev (TypeSafe System One). The frontend extracts resume text the way a parser would, then a Cloudflare Worker runs typed JEV questions and composes a JevScore. <sub>(upstream description)</sub>
  <sub>`Project` · unownone · `TS` · call site [`packages/jev/http.ts`](https://github.com/unownone/jevsume/blob/HEAD/packages/jev/http.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Natural Language Logic Interpreter](https://github.com/narphorium/nl-logic-interpreter)** — Step-through logic interpreter for facts and rules in plain English: it proves goals by SLD resolution as Prolog does, but Jev does the unification, with a choice on how two sentences relate, nouls on whether they state the same fact and choices that bind each variable to a phrase. <sub>(written by a model)</sub>
  <sub>`Project` · narphorium · `TS` · `choice` · `noul` · call site [`src/server/aiUnifier.ts`](https://github.com/narphorium/nl-logic-interpreter/blob/HEAD/src/server/aiUnifier.ts), read by a model 2026-11-08</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** — Synthetic smoking-history extraction benchmark comparing TypeSafe Jev and OpenAI structured outputs, with reproducible accuracy, cost, and latency results. <sub>(upstream description)</sub>
  <sub>`Benchmark` · vclic · `Py` · call site [`smoking_eval/providers.py`](https://github.com/vclic/smoking-extraction-benchmark/blob/HEAD/smoking_eval/providers.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[typesafe-ai-jev-example](https://github.com/ItBayMax/typesafe-ai-jev-example)** — Hands-on demos for TypeSafe's Jev (System One) model: six runnable examples and four field notes. Runs offline with no API key; samples/ holds real measured output from jev-1.13.0. <sub>(upstream description)</sub>
  <sub>`Project` · itbaymax · `Py` · call site [`lib/typesafe_client.py`](https://github.com/ItBayMax/typesafe-ai-jev-example/blob/HEAD/lib/typesafe_client.py), read 2026-09-22 · ⚠ `one commit`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
