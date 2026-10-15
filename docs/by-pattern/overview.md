# Overview

<sub>[awesome-jev](../../README.md) · [中文](overview.zh-CN.md)</sub>

_Surveys the model or the space rather than one pattern._

Every catalogued example of this decision — 453 of them. The same rows, with caveats, are in [the index](../../README.md#overview); [the site](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=en) can filter them further by language, primitive and kind.

What `overview` means in this catalogue, and why a project with code filed only under it counts as not yet indexed by pattern: [docs/patterns.md](../patterns.md#overview).

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 6 · call site 370 · wire shape 46 · example only 0 · independent reports 23 · negative results 1 · no file cited 37. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill) <sub>`Official docs` · `sh`</sub>
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) <sub>`Plugin` · `sh`</sub>
- [@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js) <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) <sub>`SDK` · `Py`</sub>
- [typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python) <sub>`SDK` · `Py` · `choice` · `score` · `noul`</sub>
- [API reference](https://docs.typesafe.ai/api) <sub>`Official docs` · `sh` · `Py` · `TS`</sub>
- [Models, pricing and limits](https://docs.typesafe.ai/models) <sub>`Official docs` · `sh` · `Py` · `TS`</sub>
- [Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives) <sub>`Official docs` · `Py` · `TS` · `choice` · `score` · `noul`</sub>
- [Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) <sub>`Article` · ⚠ `vendor numbers`</sub>
- [Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) <sub>`Official docs`</sub>
- [Use case map](https://docs.typesafe.ai/concepts/use-case-map) <sub>`Official docs`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

*Author's conclusion* is the direction a benchmark's own author states for Jev on the task they measured (`measurement.direction`: favourable, mixed, unfavourable or inconclusive), indexed from the author's report: author-stated, not reproduced here, and absent where the author states none in words. [docs/benchmarks.md](../benchmarks.md) sets every benchmark's measurement side by side.

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐ — Installs a TypeSafe skill into Claude Code so an agent can write correct Jev calls without you pasting the API shape each time.
  <sub>`Official docs` · ★1k+ · `sh`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐ — The official TypeScript client. Ships ESM, CJS and type declarations, with lowercase choice()/score()/noul() helper factories.
  <sub>`SDK` · ★100+ · `TS` · `JS` · `choice` · `score` · `noul` · call site [`src/types.ts`](https://github.com/typesafe-ai/typesafe-sdk-js/blob/HEAD/src/types.ts), read 2026-09-22</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐ — A drop-in TypeSafeClient replacement backed by ordinary LLM APIs, so you can run Jev-shaped code without Jev access.
  <sub>`SDK` · ★100+ · `Py` · cited file [`src/system_one_adapter/_client.py`](https://github.com/typesafe-ai/system-one-adapter-python/blob/HEAD/src/system_one_adapter/_client.py)</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐ — The official Python client. Sync and async clients, retry policy with retry-after support, and Choice/Score/Noul helper classes.
  <sub>`SDK` · ★100+ · `Py` · `choice` · `score` · `noul` · call site [`src/typesafe_sdk/_core/client/aio/client.py`](https://github.com/typesafe-ai/typesafe-sdk-python/blob/HEAD/src/typesafe_sdk/_core/client/aio/client.py), read 2026-09-22</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐ — POST /v1/systemone request and response shapes for the core Choice, Score and Noul questions, plus request validation and HTTP error handling.
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐ — Native Jev 1.14/1.13 IDs, aliases, pricing and limits: $0.042/Mtok input, free output, 64k tokens per request and 32k per question by default. Text is the default; images and 262k long context require experimental opt-ins.
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐ — How to choose and combine the core Choice, Score and Noul question types and define their criteria. Choice supports up to 255 options and Score 2-10 levels.
  <sub>`Official docs` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐ — The launch post: what a System One model is, why decisions were split from generation, and the vendor's latency and cost claims.
  <sub>`Article` · Diogo Almeida · ⚠ `vendor numbers`</sub>

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐ — The vendor's Jev 1.13 limitations: literal reading, arithmetic and counting, date comparison, indirection, large noisy states and adversarial content.
  <sub>`Official docs`</sub>

- **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐ — The vendor's own taxonomy: five headline categories, nineteen industry groups, and ten decision shapes from classification through to structured data extraction.
  <sub>`Official docs`</sub>

- **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)** — A coding agent whose hosted gateway resells Jev, including a free tier model id.
  <sub>`Integration` · ★100k+ · `TS` · call site [`packages/console/app/src/routes/zen/util/provider/systemone.ts`](https://github.com/anomalyco/opencode/blob/HEAD/packages/console/app/src/routes/zen/util/provider/systemone.ts)</sub>

- **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)** — Implements Effect's DecisionModel interface over Jev, with an unusually candid caveat about unverified rounding behaviour.
  <sub>`Integration` · ★10k+ · `TS` · `choice` · `score` · `noul` · call site [`packages/ai/typesafe/src/TypeSafeDecisionModel.ts`](https://github.com/Effect-TS/effect/blob/HEAD/packages/ai/typesafe/src/TypeSafeDecisionModel.ts), read 2026-09-22</sub>

- **[ai](https://github.com/vercel/ai)** — The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents <sub>(upstream description)</sub>
  <sub>`SDK` · ★10k+ · vercel · `TS` · call site [`examples/ai-functions/src/evaluate/typesafe-ai/basic.ts`](https://github.com/vercel/ai/blob/HEAD/examples/ai-functions/src/evaluate/typesafe-ai/basic.ts), read 2026-09-22</sub>

- **[laya](https://github.com/NandhaKishorM/laya)** — Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ languages, with a router that picks the right checkpoint per request. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10k+ · nandhakishorm · `Py` · cited file [`laya-ts/src/shortlist.ts`](https://github.com/NandhaKishorM/laya/blob/HEAD/laya-ts/src/shortlist.ts), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[litellm](https://github.com/BerriAI/litellm)** — The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM] <sub>(upstream description)</sub>
  <sub>`Integration` · ★10k+ · berriai · `Py` · call site [`litellm/proxy/guardrails/guardrail_hooks/typesafe/typesafe.py`](https://github.com/BerriAI/litellm/blob/HEAD/litellm/proxy/guardrails/guardrail_hooks/typesafe/typesafe.py), read 2026-09-22</sub>

- **[openwork](https://github.com/different-ai/openwork)** — The open-source alternative to Claude Cowork (powered by opencode) <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10k+ · different-ai · `TS` · cited file [`.github/scripts/jev-test-coverage-review.mjs`](https://github.com/different-ai/openwork/blob/HEAD/.github/scripts/jev-test-coverage-review.mjs), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[decider](https://github.com/Mapika/decider)** — A family of System One-style models fine-tuned from an open base for one-pass typed decisions.
  <sub>`Jev-like alternative` · ★1k+ · mapika · `Py` · cited file [`decider/bench/loadtest.py`](https://github.com/Mapika/decider/blob/HEAD/decider/bench/loadtest.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[deep-searcher](https://github.com/zilliztech/deep-searcher)** — Open Source Deep Research Alternative to Reason and Search on Private Data. Written in Python. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★1k+ · zilliztech · `Py` · cited file [`evaluation/jev_stopping/run_full100.py`](https://github.com/zilliztech/deep-searcher/blob/HEAD/evaluation/jev_stopping/run_full100.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[jevlike](https://github.com/vinnylarouge/jevlike)** — An independent, trainable model with the same input and output shape as Jev: text plus N options in, one probability per option out, in a single pass.
  <sub>`Jev-like alternative` · ★1k+ · vinnylarouge · `Py` · ⚠ `not Jev itself`</sub>

- **[kev](https://github.com/jaredpalmer/kev)** — A trainable, self-hostable family of Jev-like decision models with a System One compatible API, so the official SDK can point at your own server.
  <sub>`Jev-like alternative` · ★1k+ · Jared Palmer · `Py` · `choice` · `score` · `noul` · cited file [`playground/scripts/jev-evaluate.mjs`](https://github.com/jaredpalmer/kev/blob/HEAD/playground/scripts/jev-evaluate.mjs), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)** — A JSON-Schema-to-question compiler wired into the adapter registry, with an honest note on what it cannot serve.
  <sub>`Integration` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`libs/core/kiln_ai/adapters/jev/jev_client.py`](https://github.com/Kiln-AI/Kiln/blob/HEAD/libs/core/kiln_ai/adapters/jev/jev_client.py), read 2026-09-22</sub>

- **[NanoJev](https://github.com/TianyuCodings/NanoJev)** — A self-described nano replica of Jev, for reading rather than for production.
  <sub>`Jev-like alternative` · ★1k+ · `Py` · cited file [`scripts/jev_probe.mjs`](https://github.com/TianyuCodings/NanoJev/blob/HEAD/scripts/jev_probe.mjs) · ⚠ `not Jev itself`</sub>

- **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)** — A Rust integration with compile-time-checked option counts, so an over-255 Choice fails to build rather than at runtime.
  <sub>`Integration` · ★1k+ · `Rs` · `choice` · `score` · `noul` · call site [`crates/rig-typesafeai/src/wire.rs`](https://github.com/0xPlaygrounds/rig/blob/HEAD/crates/rig-typesafeai/src/wire.rs), read 2026-09-22</sub>

- **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)** — A Ruby provider with a dedicated System One protocol, the main route into Jev from Ruby.
  <sub>`Integration` · ★1k+ · `Rb` · `choice` · `score` · `noul` · call site [`lib/ruby_llm/providers/typesafe.rb`](https://github.com/crmne/ruby_llm/blob/HEAD/lib/ruby_llm/providers/typesafe.rb), read 2026-09-22</sub>

- **[SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev)** — An independent semantic-if implementation that states up front it is unaffiliated with Jev or TypeSafe.
  <sub>`Jev-like alternative` · ★1k+ · `Py` · ⚠ `not Jev itself`</sub>

- **[djev](https://github.com/mmastrac/djev)** — Jev-style structured decisions on DiffusionGemma: the example server from vLLM PR 57250 <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · mmastrac · `Py` · cited file [`structured_server.py`](https://github.com/mmastrac/djev/blob/HEAD/structured_server.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[jeff](https://github.com/logan-markewich/jeff)** — A self-hosted drop-in replacement for TypeSafe's jev, powered by GliFormer. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · logan-markewich · `Py` · cited file [`bench/jevbench.py`](https://github.com/logan-markewich/jeff/blob/HEAD/bench/jevbench.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open. <sub>(earlier upstream description)</sub>
  <sub>`Benchmark` · ★100+ · fstandhartinger · `Py` · call site [`jevbench/adapters/typesafe.py`](https://github.com/fstandhartinger/jevbench/blob/HEAD/jevbench/adapters/typesafe.py), read 2026-09-22</sub>

- **[jevcore](https://github.com/PerryLink/jevcore)** — TypeSafe Jev for DeepSeek Harness, the Model Context Protocol, and plain Node: typed judgments instead of prose, offline by default. <sub>(upstream description)</sub>
  <sub>`SDK` · ★100+ · perrylink · `TS` · call site [`packages/cli/src/runtime.ts`](https://github.com/PerryLink/jevcore/blob/HEAD/packages/cli/src/runtime.ts), read 2026-09-24</sub>

- **[jevk5](https://github.com/allebee/jevk5)** — JevK5: open-weight alternative to TypeSafe Jev. Typed decisions with probabilities in one forward pass; Apache-2.0 weights and code. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · allebee · `Py` · cited file [`jevk5/prompt.py`](https://github.com/allebee/jevk5/blob/HEAD/jevk5/prompt.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[laya-server](https://github.com/1Panel-dev/laya-server)** — A self-hosted API and web interface for Laya’s structured decision models, compatible with the TypeSafe Jev API format. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · 1panel-dev · `TS` · cited file [`backend/server/main.py`](https://github.com/1Panel-dev/laya-server/blob/HEAD/backend/server/main.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[localjev](https://github.com/githubnext/localjev)** — GitHub Next's local, Jev-compatible POST /v1/systemone API in TypeScript, reading probabilities from a DiffusionGemma model through a one-step structured read on a patched vLLM. It reimplements the wire, not the model.
  <sub>`Jev-like alternative` · ★100+ · githubnext · `TS` · cited file [`src/server.ts`](https://github.com/githubnext/localjev/blob/HEAD/src/server.ts), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[open-jev](https://github.com/daseinlabs/open-jev)** — Open Jev implementation with custom finetuning <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · daseinlabs · `Py` · cited file [`openjev/server.py`](https://github.com/daseinlabs/open-jev/blob/HEAD/openjev/server.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[Open-Jev](https://github.com/Zefan-Cai/Open-Jev)** — Open-Jev-27B, an open-weight model that returns typed probabilities for a context, questions and candidates without generating an answer — a Jev-style decision model you can run yourself.
  <sub>`Jev-like alternative` · ★100+ · zefan-cai · `Py` · cited file [`jev/eval_frontier.py`](https://github.com/Zefan-Cai/Open-Jev/blob/HEAD/jev/eval_frontier.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[openjev](https://github.com/razorback16/openjev)** — A Jev-compatible decision server on an open diffusion model.
  <sub>`Jev-like alternative` · ★100+ · razorback16 · `Py` · cited file [`openjev/api.py`](https://github.com/razorback16/openjev/blob/HEAD/openjev/api.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[OpenJev](https://github.com/SiliconLabAI/OpenJev)** — OpenSource Jev <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · siliconlabai · `TS` · cited file [`src/App.tsx`](https://github.com/SiliconLabAI/OpenJev/blob/HEAD/src/App.tsx), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[openjev-sglang](https://github.com/ekzhang/openjev-sglang)** — A Jev-compatible endpoint served from open models, prefill only.
  <sub>`Jev-like alternative` · ★100+ · ekzhang · `Py` · cited file [`src/openjev/api.py`](https://github.com/ekzhang/openjev-sglang/blob/HEAD/src/openjev/api.py), read 2026-09-22 · ⚠ `not Jev itself` `no licence` `archived`</sub>

- **[rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow)** — The open, local take on Jev: typed decisions from an LLM, without generating a single token <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · rizzo-ai-academy · `Py` · cited file [`src/rizzo_flow/compat.py`](https://github.com/Rizzo-AI-Academy/rizzo-flow/blob/HEAD/src/rizzo_flow/compat.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[simple-jev](https://github.com/featherless-ai/simple-jev)** — Turns any open-weights model into a Jev-shaped endpoint by reading next-token logits, with the server constructing the JSON rather than the model generating it.
  <sub>`Jev-like alternative` · ★100+ · `Py` · cited file [`hf-server/hf_server.py`](https://github.com/featherless-ai/simple-jev/blob/HEAD/hf-server/hf_server.py) · ⚠ `not Jev itself`</sub>

- **[von](https://github.com/wfzyx/von)** — The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★100+ · wfzyx · `Py` · cited file [`js/src/client.ts`](https://github.com/wfzyx/von/blob/HEAD/js/src/client.ts), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[advocaat](https://github.com/pithings/advocaat)** — A small typed client for asking questions about your own data.
  <sub>`SDK` · ★10+ · pithings · `TS` · call site [`src/api.ts`](https://github.com/pithings/advocaat/blob/HEAD/src/api.ts), read 2026-09-22</sub>

- **[diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)** — A Jev-like decision engine powered by DiffusionGemma and SGLang. Jev with eyes. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · hangzhi · `Py` · cited file [`scripts/compare_jevbench.py`](https://github.com/Hangzhi/diffusion-jev-sglang/blob/HEAD/scripts/compare_jevbench.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[dohnuts.cpp](https://github.com/DreamBlooms/dohnuts.cpp)** — The same decisions, on CPU. System One model that can run on your Personal Computer. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · dreamblooms · `C++` · cited file [`scripts/compare/ref_decider.py`](https://github.com/DreamBlooms/dohnuts.cpp/blob/HEAD/scripts/compare/ref_decider.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[fastjev](https://github.com/chengyongru/fastjev)** — SDK-first, independently maintained SemIf fork for fast, self-hosted semantic decisions. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · chengyongru · `Py` · cited file [`demo/jev-ultrafast/record.py`](https://github.com/chengyongru/fastjev/blob/HEAD/demo/jev-ultrafast/record.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[go-jev](https://github.com/mattn/go-jev)** — Go SDK and CLI for TypeSafe Jev: typed decisions (yes/no, choice, score) from a model <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · mattn · `Go` · call site [`jev.go`](https://github.com/mattn/go-jev/blob/HEAD/jev.go), read 2026-09-24</sub>

- **[hunch](https://github.com/carldaws/hunch)** — Probabilistic control flow for Ruby and Rails - powered by TypeSafe's Jev <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · carldaws · `Rb` · call site [`lib/hunch/configuration.rb`](https://github.com/carldaws/hunch/blob/HEAD/lib/hunch/configuration.rb), read 2026-09-24</sub>

- **[jev (Elixir/OTP)](https://github.com/dannote/jev)** — Jev as an OTP process: reply from a GenServer and pattern match on the answer.
  <sub>`SDK` · ★10+ · dannote · `Ex` · call site [`lib/jev/http.ex`](https://github.com/dannote/jev/blob/HEAD/lib/jev/http.ex), read 2026-09-22</sub>

- **[jev-cli](https://github.com/tumf/jev-cli)** — Small dependency-free CLI for TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · tumf · `Py` · call site [`src/jev_cli/__init__.py`](https://github.com/tumf/jev-cli/blob/HEAD/src/jev_cli/__init__.py), read 2026-09-22</sub>

- **[jev-explained](https://github.com/davila7/jev-explained)** — Jev Explained <sub>(upstream description)</sub>
  <sub>`Tutorial` · ★10+ · davila7 · `TS` · call site [`src/lib/providers.ts`](https://github.com/davila7/jev-explained/blob/HEAD/src/lib/providers.ts), read 2026-09-24</sub>

- **[Jev-Quantum](https://github.com/karminski/Jev-Quantum)** — A Jev-protocol random baseline: it speaks noul, choice and score but reads no prompt, answering from a fast pseudo-random generator — a mock, and a lower bound for routing evaluations.
  <sub>`Jev-like alternative` · ★10+ · karminski · `Rs` · cited file [`crates/jev-quantum-bench/src/config.rs`](https://github.com/karminski/Jev-Quantum/blob/HEAD/crates/jev-quantum-bench/src/config.rs), read 2026-09-24 · ⚠ `not Jev itself` `one commit`</sub>

- **[jev4k](https://github.com/pambrose/jev4k)** — A Kotlin DSL and client for TypeSafe's Jev model <sub>(earlier upstream description)</sub>
  <sub>`SDK` · ★10+ · pambrose · `Kt` · call site [`src/main/kotlin/com/pambrose/jev4k/JevConfig.kt`](https://github.com/pambrose/jev4k/blob/HEAD/src/main/kotlin/com/pambrose/jev4k/JevConfig.kt), read 2026-09-22</sub>

- **[jev_local](https://github.com/Argos1111/jev_local)** — Replicating Jev with a local LLM <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · argos1111 · `Py` · cited file [`tools/verify_api.py`](https://github.com/Argos1111/jev_local/blob/HEAD/tools/verify_api.py), read 2026-09-24 · ⚠ `not Jev itself` `no licence`</sub>

- **[JevAny](https://github.com/SimpleJev/JevAny)** — JevAny: a calibrated decision layer for RL, agents and model harnesses that returns typed answers and option probabilities in one prefill pass — an open 27B model on a Qwen backbone, not Jev.
  <sub>`Jev-like alternative` · ★10+ · weitianxin · `Py` · cited file [`jevany/api.py`](https://github.com/SimpleJev/JevAny/blob/HEAD/jevany/api.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[jevify](https://github.com/fidecastro/jevify)** — Supersimple way to serve LLMs as a Jev-like endpoint <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · fidecastro · `Py` · cited file [`jevify/api/app.py`](https://github.com/fidecastro/jevify/blob/HEAD/jevify/api/app.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[jevper](https://github.com/zhulinchng/jevper)** — Jev-shaped (TypeSafe System One) classification wrapper over OpenAI-like clients: probabilities and confidence instead of prose
  <sub>`Jev-like alternative` · ★10+ · zhulinchng · `Py` · cited file [`src/jevper/types.py`](https://github.com/zhulinchng/jevper/blob/HEAD/src/jevper/types.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[learn-jev-end-to-end](https://github.com/harshithsunku/learn-jev-end-to-end)** — Learn Jev end to end: a free hands-on course. Build 13 AI agent use cases with a fast brain (Jev) and a slow brain (LLM). One OpenRouter key. <sub>(upstream description)</sub>
  <sub>`Tutorial` · ★10+ · harshithsunku · `Py` · call site [`app.py`](https://github.com/harshithsunku/learn-jev-end-to-end/blob/HEAD/app.py), read 2026-09-24</sub>

- **[litjev](https://github.com/zhengxuyu/litjev)** — Turn any off-the-shelf LLM into a Jev -like decision layer <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · zhengxuyu · `Py` · cited file [`src/litjev/api.py`](https://github.com/zhengxuyu/litjev/blob/HEAD/src/litjev/api.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[midscene-jev-runner](https://github.com/KiritoKing/midscene-jev-runner)** — Community-maintained JEV runner integration for Midscene Test <sub>(upstream description)</sub>
  <sub>`Integration` · ★10+ · kiritoking · `TS` · call site [`src/constants.ts`](https://github.com/KiritoKing/midscene-jev-runner/blob/HEAD/src/constants.ts), read 2026-09-22</sub>

- **[notjev](https://github.com/9pings/notjev)** — Super fast Jev like server, model agnostic, working with any OpenAI compatible endpoint <sub>(earlier upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · 9pings · `JS` · cited file [`bin/notjev.js`](https://github.com/9pings/notjev/blob/HEAD/bin/notjev.js), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)** — An open-source semantic decision engine running a local zero-shot model, with a FastAPI server proven wire-compatible with the official SDK.
  <sub>`Jev-like alternative` · ★10+ · deepanwadhwa · `Py` · `choice` · `score` · `noul` · cited file [`examples/m3_typesafe_sdk_demo.py`](https://github.com/deepanwadhwa/OpenDecision/blob/HEAD/examples/m3_typesafe_sdk_demo.py), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[OpenJev](https://github.com/GPT-AGI/OpenJev)** — Jev-compatible System 开源Jev
  <sub>`Jev-like alternative` · ★10+ · gpt-agi · `Py` · cited file [`src/openjev/core/primitives.py`](https://github.com/GPT-AGI/OpenJev/blob/HEAD/src/openjev/core/primitives.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[OpenJev](https://github.com/zhangcy122/OpenJev)** — OpenJev: Open-source alternative to TypeSafe Jev. Typed probabilistic decision API (Choice, Noul, Score) powered by open LLMs & constrained logprob calibration.
  <sub>`Jev-like alternative` · ★10+ · zhangcy122 · `Py` · cited file [`examples/benchmark_jev_vs_ollama.py`](https://github.com/zhangcy122/OpenJev/blob/HEAD/examples/benchmark_jev_vs_ollama.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[OpenSourceJev](https://github.com/sabeel111/OpenSourceJev)** — Turning an LLM model into a Jev like System. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · sabeel111 · `Py` · cited file [`app/main.py`](https://github.com/sabeel111/OpenSourceJev/blob/HEAD/app/main.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[pijev](https://github.com/TypeLLM/pijev)** — Averages Jev's answers over option orderings — all permutations in one request — with Brier score and log loss guaranteed no worse than the average across the orderings included. A one-line import change.
  <sub>`SDK` · ★10+ · typellm · `Py` · call site [`pijev/__init__.py`](https://github.com/TypeLLM/pijev/blob/HEAD/pijev/__init__.py), read 2026-09-24</sub>

- **[refgarden](https://github.com/AlbionaHoti/refgarden)** — A spatial reference explorer for creators. Local Jev query choices, metadata highlights and source-linked collections. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · albionahoti · `TS` · cited file [`src/jev-connection.ts`](https://github.com/AlbionaHoti/refgarden/blob/HEAD/src/jev-connection.ts), read 2026-09-22 · ⚠ `not Jev itself`</sub>

- **[ruby_decision_model](https://github.com/obie/ruby_decision_model)** — Ruby client for decision models such as Typesafe Jev <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · obie · `Rb` · call site [`lib/ruby_decision_model/providers/typesafe.rb`](https://github.com/obie/ruby_decision_model/blob/HEAD/lib/ruby_decision_model/providers/typesafe.rb), read 2026-09-22</sub>

- **[ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)** — A structured-output provider for a Ruby LLM library.
  <sub>`Integration` · ★10+ · kieranklaassen · `Rb` · call site [`lib/ruby_llm/providers/typesafe.rb`](https://github.com/kieranklaassen/ruby_llm-typesafe/blob/HEAD/lib/ruby_llm/providers/typesafe.rb), read 2026-09-22</sub>

- **[ruling](https://github.com/bradAGI/ruling)** — Typed, calibrated decisions from a local model. No text generated. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · bradagi · `Py` · cited file [`ruling/against.py`](https://github.com/bradAGI/ruling/blob/HEAD/ruling/against.py), read 2026-09-24 · ⚠ `not Jev itself` `unverified claims`</sub>

- **[snap](https://github.com/emnlmn/snap)** — Typed decisions from unstructured state: one forward pass, zero generated text. Local, deterministic, Jev-compatible. Not affiliated with typesafe.ai. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · emnlmn · `Rs` · cited file [`src/api.rs`](https://github.com/emnlmn/snap/blob/HEAD/src/api.rs), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[snapjudge](https://github.com/Micha0827/snapjudge)** — Typed decisions (choice / score / yes-no) from local Qwen models on Apple Silicon. Probabilities come straight from the logits, no text generation. TypeSafe-compatible HTTP API, runs on MLX. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · micha0827 · `Py` · cited file [`eval/extern/typesafe_public.py`](https://github.com/Micha0827/snapjudge/blob/HEAD/eval/extern/typesafe_public.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[solar-mini4-jev](https://github.com/hunkim/solar-mini4-jev)** — A drop-in wrapper that exposes Upstage's Solar models through the Jev System One API shape — noul, choice and score with the same schema — with a hosted bring-your-own-key endpoint.
  <sub>`Jev-like alternative` · ★10+ · hunkim · `Py` · cited file [`jev_ref.py`](https://github.com/hunkim/solar-mini4-jev/blob/HEAD/jev_ref.py), read 2026-09-24 · ⚠ `not Jev itself` `no licence`</sub>

- **[swift-jev](https://github.com/d-date/swift-jev)** — A Swift client for TypeSafe AI's Jev — typed judgements, not text <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · d-date · `Swift` · call site [`Sources/Jev/Transport.swift`](https://github.com/d-date/swift-jev/blob/HEAD/Sources/Jev/Transport.swift), read 2026-09-24</sub>

- **[swift-typesafe](https://github.com/ainame/swift-typesafe)** — Unofficial Swift SDK for TypeSafe <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · ainame · `Swift` · call site [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/ainame/swift-typesafe/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift), read 2026-09-22</sub>

- **[sys1](https://github.com/alvarobartt/sys1)** — System One compatible API for open decision models, e.g. Laya, written in Rust.
  <sub>`Jev-like alternative` · ★10+ · alvarobartt · `Rs` · cited file [`src/api.rs`](https://github.com/alvarobartt/sys1/blob/HEAD/src/api.rs), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[system-one](https://github.com/iamaamir/system-one)** — Provider-neutral System One runtime for TypeScript and Pi <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · iamaamir · `TS` · call site [`pi-system-one/src/tool.ts`](https://github.com/iamaamir/system-one/blob/HEAD/pi-system-one/src/tool.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[tinyjev](https://github.com/ankit-aglawe/tinyjev)** — A tiny jev-like model that answers Choice, Score and Noul questions in one forward pass and returns calibrated probabilities. MLX or PyTorch, fully offline, System One compatible. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · ★10+ · ankit-aglawe · `Py` · cited file [`tinyjev/cli.py`](https://github.com/ankit-aglawe/tinyjev/blob/HEAD/tinyjev/cli.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[typesafe](https://github.com/krzyzanowskim/TypeSafe)** — TypeSafe SDK in Swift <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · krzyzanowskim · `Swift` · call site [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/krzyzanowskim/TypeSafe/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift), read 2026-09-22</sub>

- **[typesafe-ai](https://github.com/Twister915/typesafe-ai)** — Typed TypeSafe AI clients for Rust, with async and blocking backends and observable retries. <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · twister915 · `Rs` · call site [`examples/tsg/main.rs`](https://github.com/Twister915/typesafe-ai/blob/HEAD/examples/tsg/main.rs), read 2026-09-22</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/inference-benchmarks)** — A gateway that mimics the structured-output shape, used to benchmark against it.
  <sub>`Benchmark` · ★10+ · iammrduncan · `TS` · call site [`packages/demos/lib/jev.ts`](https://github.com/iammrduncan/inference-benchmarks/blob/HEAD/packages/demos/lib/jev.ts), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[typesafe-sdk-go](https://github.com/atharvamhaske/typesafe-sdk-go)** — unofficial go sdk for typesafe ai. not affiliated with or endorsed by typesafe ai. a side project built to fill the missing go sdk gap, for the community to use. <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · atharvamhaske · `Go` · call site [`typesafe.go`](https://github.com/atharvamhaske/typesafe-sdk-go/blob/HEAD/typesafe.go), read 2026-09-24</sub>

- **[typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java)** — Community Java client for the TypeSafe System One API (unofficial)
  <sub>`SDK` · ★10+ · premo-cloud · `Java` · call site [`typesafe-sdk/src/main/java/io/github/premocloud/typesafe/TypeSafeClient.java`](https://github.com/Premo-Cloud/typesafe-sdk-java/blob/HEAD/typesafe-sdk/src/main/java/io/github/premocloud/typesafe/TypeSafeClient.java), read 2026-09-22</sub>

- **[typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk)** — Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`SDK` · ★10+ · saibimajdi · `C#` · call site [`examples/TypeSafe.BureauOfBadIdeas/Program.cs`](https://github.com/saibimajdi/typesafeai-dotnet-sdk/blob/HEAD/examples/TypeSafe.BureauOfBadIdeas/Program.cs), read 2026-09-22</sub>

- **[WaterSheep](https://github.com/SamratDuttaOfficial/WaterSheep)** — Open, Apache-2.0 alternative to Jev: a ModernBERT fine-tune served locally on POST /v1/systemone that answers noul, choice and score questions, plus multi-label ones, with a probability for every option.
  <sub>`Jev-like alternative` · ★10+ · SamratDuttaOfficial · `Py` · cited file [`watersheep/cli.py`](https://github.com/SamratDuttaOfficial/WaterSheep/blob/HEAD/watersheep/cli.py), read 2026-10-03 · ⚠ `not Jev itself` `self-submitted`</sub>

- **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)** — The AI SDK provider package for calling TypeSafe directly, with a sample covering all three question types and nested criteria shapes.
  <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[antigravity-mcp-semantic-search-with-typesafeai](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)** — Fast semantic code search & diff sanity auditor for AI coding assistants (Antigravity, Cursor, Claude Code) powered by TypeSafe System One. <sub>(upstream description)</sub>
  <sub>`Benchmark` · greenyamao · `Py` · call site [`mcp_server.py`](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi/blob/HEAD/mcp_server.py), read 2026-09-22</sub>

- **[audio-jevlike](https://github.com/alperiox/audio-jevlike)** — Prosodia: an audio-native Jev-shaped decision model — typed calibrated decisions from speech, no ASR <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · alperiox · `Py` · cited file [`space/prosodia/evaluation/baselines.py`](https://github.com/alperiox/audio-jevlike/blob/HEAD/space/prosodia/evaluation/baselines.py), read 2026-09-24 · ⚠ `not Jev itself` `no licence`</sub>

- **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)** — Despite the title, this does not run Jev. It builds a Jev-like decision engine from an open LLM using constrained next-token scoring.
  <sub>`Jev-like alternative` · DataScience Nexus · `Py` · ⚠ `not Jev itself` `code untested` `paywall`</sub>

- **[can-jev-bayes](https://github.com/TomRichner/can-jev-bayes)** — Jev Bayes, No? Testing TypeSafe AI's Jev against Bayesian-optimal strategies, and testing if Jev can effectivly use Bayesian priors. <sub>(upstream description)</sub>
  <sub>`Benchmark` · tomrichner · `Py` · call site [`src/jevbandits/client.py`](https://github.com/TomRichner/can-jev-bayes/blob/HEAD/src/jevbandits/client.py), read 2026-09-24</sub>

- **[chat2jev](https://github.com/Chandler-Sun/chat2jev)** — Convert legacy chat completion API request to Typesafe jev API <sub>(upstream description)</sub>
  <sub>`SDK` · chandler-sun · `TS` · call site [`src/lib/typesafe.ts`](https://github.com/Chandler-Sun/chat2jev/blob/HEAD/src/lib/typesafe.ts), read 2026-09-24</sub>

- **[cu-Jev](https://github.com/dtunai/cu-Jev)** — cuda-Jev — a CUDA-native Jev System One decision inference engine. Jev compatible API, examples, and reproducible benchmarks. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · dtunai · `C` · cited file [`python/cujev/systemone.py`](https://github.com/dtunai/cu-Jev/blob/HEAD/python/cujev/systemone.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[decido](https://github.com/yairshy/decido)** — Probabilistic decisions for Python. Use Jev or bring your own provider; crawl with Playwright. <sub>(upstream description)</sub>
  <sub>`Integration` · yairshy · `Py` · call site [`src/decido/providers/typesafe.py`](https://github.com/yairshy/decido/blob/HEAD/src/decido/providers/typesafe.py), read 2026-09-22</sub>

- **[decision-bench](https://github.com/Hanno-Labs/decision-bench)** — Open benchmark runtime for document-grounded decision models <sub>(upstream description)</sub>
  <sub>`Benchmark` · hanno-labs · `Py` · call site [`src/decision_bench/models/jev_openrouter.py`](https://github.com/Hanno-Labs/decision-bench/blob/HEAD/src/decision_bench/models/jev_openrouter.py), read 2026-09-24</sub>

- **[decision-circuits](https://github.com/Barneyjm/decision-circuits)** — Decision circuits: typed questions to a System One model, calibrated probabilities back, gates in code. Zero-dependency Python SDK with LangChain, OpenAI Agents, and Claude Agent SDK integrations. <sub>(upstream description)</sub>
  <sub>`SDK` · barneyjm · `Py` · call site [`examples/02_jev_backend.py`](https://github.com/Barneyjm/decision-circuits/blob/HEAD/examples/02_jev_backend.py), read 2026-09-24</sub>

- **[go-system-one](https://github.com/rcarmo/go-system-one)** — when a gopher met Jev <sub>(upstream description)</sub>
  <sub>`SDK` · rcarmo · `Go` · call site [`docs/benchmarks/data/jevbench-public-20260923/protocol/aggregate.py`](https://github.com/rcarmo/go-system-one/blob/HEAD/docs/benchmarks/data/jevbench-public-20260923/protocol/aggregate.py), read 2026-09-24</sub>

- **[hunch-js](https://github.com/steven-shoemaker/hunch-js)** — Jev judgments as TypeScript functions over arrays: classify, score, check, where, extract, pick, rank, verify. LLMs propose, Jev decides. <sub>(upstream description)</sub>
  <sub>`SDK` · steven-shoemaker · `TS` · call site [`src/gateway.ts`](https://github.com/steven-shoemaker/hunch-js/blob/HEAD/src/gateway.ts), read 2026-09-24</sub>

- **[jear](https://github.com/iJ03l/jear)** — Jev-routed client for NEAR AI Cloud inference and IronClaw agents. <sub>(upstream description)</sub>
  <sub>`SDK` · ij03l · `Rs` · call site [`src/jev_wire.rs`](https://github.com/iJ03l/jear/blob/HEAD/src/jev_wire.rs), read 2026-09-22</sub>

- **[jev](https://github.com/anilsenay/jev)** — Unofficial Go client for TypeSafe's System One API and its model, Jev. <sub>(upstream description)</sub>
  <sub>`SDK` · anilsenay · `Go` · call site [`client.go`](https://github.com/anilsenay/jev/blob/HEAD/client.go), read 2026-09-24</sub>

- **[jev](https://github.com/kataras/jev)** — A Go client for the TypeSafe AI's System One API and its model, Jev. <sub>(upstream description)</sub>
  <sub>`SDK` · kataras · `Go` · call site [`client.go`](https://github.com/kataras/jev/blob/HEAD/client.go), read 2026-09-24 · ⚠ `one commit`</sub>

- **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)** — A third-party explainer with a useful architecture sketch and an unusually honest list of cases where you should not use a decision model.
  <sub>`Article` · `Py` · ⚠ `code untested`</sub>

- **[jev-acento](https://github.com/marcosmartinez/jev-acento)** — ¿Jev entiende tu acento? Pre-registered audit of TypeSafe AI's Jev on Spanish — accuracy, calibration and token cost — plus a CLI to run the same comparison on your own labelled data. <sub>(upstream description)</sub>
  <sub>`Benchmark` · marcosmartinez · `Py` · call site [`src/jev_acento/providers.py`](https://github.com/marcosmartinez/jev-acento/blob/HEAD/src/jev_acento/providers.py), read 2026-09-24</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset). <sub>(upstream description)</sub>
  <sub>`Benchmark` · tokentrim · `Py` · call site [`src/jevbench/backends/jev.py`](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/HEAD/src/jevbench/backends/jev.py), read 2026-09-22</sub>

- **[jev-android](https://github.com/dougsong/jev-android)** — A Kotlin Android SDK for UI automation powered by TypeSafe Jev, with an accessibility runtime and sample app. <sub>(upstream description)</sub>
  <sub>`SDK` · dougsong · `Kt` · call site [`sdk/src/main/kotlin/io/github/jevandroid/JevProvider.kt`](https://github.com/dougsong/jev-android/blob/HEAD/sdk/src/main/kotlin/io/github/jevandroid/JevProvider.kt), read 2026-09-22</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs <sub>(upstream description)</sub>
  <sub>`Benchmark` · wondertwins · `Py` · call site [`jevcommon/client.py`](https://github.com/wondertwins/jev-benchmark/blob/HEAD/jevcommon/client.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here)</sub>

- **[jev-bun1](https://github.com/heiwa4126/jev-bun1)** — TypeSafe の Jev を TypeScript SDK で使ってみる最初の 1 歩 <sub>(upstream description)</sub>
  <sub>`SDK` · heiwa4126 · `TS` · call site [`src/ex0.ts`](https://github.com/heiwa4126/jev-bun1/blob/HEAD/src/ex0.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-cookbook](https://github.com/paramjeetn/jev-cookbook)** — The complete cookbook for Jev by TypeSafe AI — 120+ use cases, 10 runnable examples, 4 composition patterns, and first-principles theory for the world's first System One AI model. <sub>(upstream description)</sub>
  <sub>`Tutorial` · paramjeetn · `Py` · call site [`examples/01-customer-support-triage/triage.py`](https://github.com/paramjeetn/jev-cookbook/blob/HEAD/examples/01-customer-support-triage/triage.py), read 2026-09-24</sub>

- **[jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)** — Does TypeSafe's Jev keep its accuracy and calibration on Russian? Independent RU vs EN audit (ECE, reliability diagrams, paired bootstrap) on parallel human-labelled data. <sub>(upstream description)</sub>
  <sub>`Benchmark` · ahtoooxa · `Py` · call site [`src/jev_cyrillic_audit/run.py`](https://github.com/AHTOOOXA/jev-cyrillic-audit/blob/HEAD/src/jev_cyrillic_audit/run.py), read 2026-09-24</sub>

- **[jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)** — Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation. <sub>(upstream description)</sub>
  <sub>`Benchmark` · kantahayashiai · `JS` · call site [`src/run.mjs`](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/HEAD/src/run.mjs), read 2026-09-24</sub>

- **[jev-go](https://github.com/guillemus/jev-go)** — Unofficial Go SDK for TypeSafe AI's Jev API <sub>(upstream description)</sub>
  <sub>`SDK` · guillemus · `Go` · call site [`jev.go`](https://github.com/guillemus/jev-go/blob/HEAD/jev.go), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-go](https://github.com/Gaurav-Gosain/jev-go)** — Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text <sub>(upstream description)</sub>
  <sub>`SDK` · gaurav-gosain · `Go` · call site [`client.go`](https://github.com/Gaurav-Gosain/jev-go/blob/HEAD/client.go), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jev-go-sdk](https://github.com/ajayk/jev-go-sdk)** — Dependency-free Go client for TypeSafe AI's System One API and the Jev model <sub>(upstream description)</sub>
  <sub>`SDK` · ajayk · `Go` · call site [`client.go`](https://github.com/ajayk/jev-go-sdk/blob/HEAD/client.go), read 2026-09-24</sub>

- **[jev-java](https://github.com/Olti1947/jev-java)** — Idiomatic Java SDK for TypeSafe AI Jev System One decision engine <sub>(upstream description)</sub>
  <sub>`SDK` · olti1947 · `Java` · call site [`src/main/java/io/github/Olti1947/jev/JevClient.java`](https://github.com/Olti1947/jev-java/blob/HEAD/src/main/java/io/github/Olti1947/jev/JevClient.java), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-java](https://github.com/gudcks0305/jev-java)** — Unofficial Java SDK for TypeSafe Jev and Vercel AI Gateway, with Spring Boot and WebClient support <sub>(upstream description)</sub>
  <sub>`SDK` · gudcks0305 · `Java` · call site [`jev-cloudflare/src/main/java/io/github/gudcks0305/jev/cloudflare/CloudflareJevClient.java`](https://github.com/gudcks0305/jev-java/blob/HEAD/jev-cloudflare/src/main/java/io/github/gudcks0305/jev/cloudflare/CloudflareJevClient.java), read 2026-09-24</sub>

- **[jev-jp-address](https://github.com/smasato/jev-jp-address)** — Jev (TypeSafe) 性能評価プロジェクト — 日本郵便 KEN_ALL をマスタに、AI SDK 経由の Jev が住所のあいまい一致にどこまで使えるかを検証 <sub>(upstream description)</sub>
  <sub>`SDK` · smasato · `TS` · call site [`src/jev.ts`](https://github.com/smasato/jev-jp-address/blob/HEAD/src/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — Reproducible early-access evaluation of Jev on Korean understanding and medical text, with runtime and cost evidence <sub>(upstream description)</sub>
  <sub>`Benchmark` · mahlernim · `Py` · call site [`jevbench/medqa_run.py`](https://github.com/mahlernim/jev-korean-benchmark/blob/HEAD/jevbench/medqa_run.py), read 2026-09-22 · author's conclusion: mixed (author-stated, not reproduced here) · ⚠ `no licence`</sub>

- **[jev-lab](https://github.com/danielhirt/jev-lab)** — Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison <sub>(upstream description)</sub>
  <sub>`Benchmark` · danielhirt · `TS` · call site [`packages/codenames/src/judge.ts`](https://github.com/danielhirt/jev-lab/blob/HEAD/packages/codenames/src/judge.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-lab](https://github.com/llt22/jev-lab)** — Hands-on research lab for TypeSafe's Jev (System One model): reproducible benchmarks of Noul/Choice/Score primitives, confidence gating, fan-out latency, agent control — plus a living audit of the Jev ecosystem. <sub>(upstream description)</sub>
  <sub>`Benchmark` · llt22 · `Py` · call site [`experiments/json-render-jev/src/demo.tsx`](https://github.com/llt22/jev-lab/blob/HEAD/experiments/json-render-jev/src/demo.tsx), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-lab](https://github.com/Menny1337/jev-lab)** — TypeScript experiments, evaluations, and latency benchmarks for TypeSafe's Jev model <sub>(upstream description)</sub>
  <sub>`Benchmark` · menny1337 · `TS` · call site [`src/client.ts`](https://github.com/Menny1337/jev-lab/blob/HEAD/src/client.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — A show-and-tell capability study for Jev, TypeSafe's System One decision model. <sub>(upstream description)</sub>
  <sub>`Benchmark` · lbotinelly · `TS` · call site [`demo/js/jev-monitor.mjs`](https://github.com/lbotinelly/jev-little-airways/blob/HEAD/demo/js/jev-monitor.mjs), read 2026-09-22</sub>

- **[jev-no-enem](https://github.com/patryckalves/jev-no-enem)** — Reproducible benchmark evaluating TypeSafe AI's Jev (System One paradigm) on Brazil's ENEM 2025 standardized exam. Evaluates typed decision-making, domain-specific accuracy, and RLCD uncertainty calibration against open LLM baselines with an interactive GitHub Pages dashboard. <sub>(upstream description)</sub>
  <sub>`Benchmark` · patryckalves · `Py` · call site [`src/evaluate_jev.py`](https://github.com/patryckalves/jev-no-enem/blob/HEAD/src/evaluate_jev.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-php-sdk](https://github.com/mzainzulifqar/jev-php-sdk)** — PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13. <sub>(upstream description)</sub>
  <sub>`SDK` · mzainzulifqar · `PHP` · call site [`src/Jev.php`](https://github.com/mzainzulifqar/jev-php-sdk/blob/HEAD/src/Jev.php), read 2026-09-24</sub>

- **[jev-research](https://github.com/sherajdev/jev-research)** — Practical guide to using TypeSafe Jev with Herdr and Claude, Codex, Hermes, and browser agents. <sub>(upstream description)</sub>
  <sub>`Tutorial` · sherajdev · `TS` · call site [`jev-router.ts`](https://github.com/sherajdev/jev-research/blob/HEAD/jev-router.ts), read 2026-09-24</sub>

- **[jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment)** — Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena <sub>(upstream description)</sub>
  <sub>`Benchmark` · tokentrim · `Py` · call site [`jev_router/jev.py`](https://github.com/TokenTrim/jev-routing-experiment/blob/HEAD/jev_router/jev.py), read 2026-09-22</sub>

- **[jev-rs](https://github.com/abeldzan/jev-rs)** — Async-first Rust SDK for the TypeSafe AI API <sub>(upstream description)</sub>
  <sub>`SDK` · abeldzan · `Rs` · call site [`src/response.rs`](https://github.com/abeldzan/jev-rs/blob/HEAD/src/response.rs), read 2026-09-24</sub>

- **[jev-sdk-java](https://github.com/luigivis/jev-sdk-java)** — Type-safe Java 21 client for the TypeSafe AI Jev (System One) decision API <sub>(upstream description)</sub>
  <sub>`SDK` · luigivis · `Java` · call site [`src/main/java/com/luigivismara/jev/JevClient.java`](https://github.com/luigivis/jev-sdk-java/blob/HEAD/src/main/java/com/luigivismara/jev/JevClient.java), read 2026-09-22</sub>

- **[jev-sim](https://github.com/dashbi1/jev-sim)** — Jev-compatible /v1/systemone server reading typed decisions from LLM logits, benchmarked against TypeSafe's Jev on the same items via JevBench <sub>(upstream description)</sub>
  <sub>`Benchmark` · dashbi1 · `Py` · call site [`jev_sim/cli.py`](https://github.com/dashbi1/jev-sim/blob/HEAD/jev_sim/cli.py), read 2026-09-22</sub>

- **[jev-symfony-bundle](https://github.com/vbcherepanov/jev-symfony-bundle)** — Unofficial Symfony bundle for TypeSafe AI's Jev: typed client, validator constraints, Messenger, Workflow guards and profiler panel <sub>(upstream description)</sub>
  <sub>`SDK` · vbcherepanov · `PHP` · call site [`src/Client/JevClientInterface.php`](https://github.com/vbcherepanov/jev-symfony-bundle/blob/HEAD/src/Client/JevClientInterface.php), read 2026-09-24</sub>

- **[jev4mellea](https://github.com/SoundBlaster/Jev4Mellea)** — Jev adapter for Mellea <sub>(upstream description)</sub>
  <sub>`Integration` · soundblaster · `Py` · call site [`src/mellea_jev/providers/typesafe.py`](https://github.com/SoundBlaster/Jev4Mellea/blob/HEAD/src/mellea_jev/providers/typesafe.py), read 2026-09-22</sub>

- **[jevclient](https://github.com/AboveColin/jevclient)** — Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse. <sub>(upstream description)</sub>
  <sub>`SDK` · abovecolin · `Py` · call site [`jevclient/const.py`](https://github.com/AboveColin/jevclient/blob/HEAD/jevclient/const.py), read 2026-09-22</sub>

- **[jevgo](https://github.com/fgn/jevgo)** — Go client for TypeSafe AI's System One API (Jev), with optional Langfuse instrumentation <sub>(upstream description)</sub>
  <sub>`SDK` · fgn · `Go` · call site [`client.go`](https://github.com/fgn/jevgo/blob/HEAD/client.go), read 2026-09-22</sub>

- **[jevgo](https://github.com/devbackend/jevgo)** — Unofficial Go client for the TypeSafe AI System One API (Jev) — typed questions in, calibrated answers out. <sub>(upstream description)</sub>
  <sub>`SDK` · devbackend · `Go` · call site [`client.go`](https://github.com/devbackend/jevgo/blob/HEAD/client.go), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jevlang](https://github.com/sumanmichael/jevlang)** — The simplest way to write decision workflows in Python. Python with a smart if. <sub>(upstream description)</sub>
  <sub>`SDK` · sumanmichael · `Py` · call site [`jevlang/backend.py`](https://github.com/sumanmichael/jevlang/blob/HEAD/jevlang/backend.py), read 2026-09-24 · ⚠ `one commit`</sub>

- **[jevsbistro](https://github.com/andrewsilber/JevsBistro)** — 3D restaurant service simulator for benchmarking low-latency decision models <sub>(upstream description)</sub>
  <sub>`Benchmark` · andrewsilber · `TS` · call site [`src/jev/protocol.ts`](https://github.com/andrewsilber/JevsBistro/blob/HEAD/src/jev/protocol.ts), read 2026-09-22</sub>

- **[kojev](https://github.com/ItisNoMatter/kojev)** — Kotlin Multiplatform client for Jev that returns your own enum/sealed types instead of string keys. <sub>(upstream description)</sub>
  <sub>`SDK` · itisnomatter · `Kt` · call site [`src/commonTest/kotlin/io/github/itisnomatter/kojev/JevClientTest.kt`](https://github.com/ItisNoMatter/kojev/blob/HEAD/src/commonTest/kotlin/io/github/itisnomatter/kojev/JevClientTest.kt), read 2026-09-22</sub>

- **[kunobi-jev](https://github.com/kunobi-ninja/kunobi-decision)** — Rust client for the TypeSafe System One API (Jev) <sub>(upstream description)</sub>
  <sub>`SDK` · kunobi-ninja · `Rs` · call site [`src/client/mod.rs`](https://github.com/kunobi-ninja/kunobi-decision/blob/HEAD/src/client/mod.rs), read 2026-09-22</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD benchmark alpha and official evaluation workflows <sub>(upstream description)</sub>
  <sub>`Benchmark` · johnhughes3 · `Py` · call site [`legalforecast/jev/execution.py`](https://github.com/johnhughes3/LegalForecastBench/blob/HEAD/legalforecast/jev/execution.py), read 2026-09-22</sub>

- **[OpenJev](https://github.com/xingwudao/OpenJev)** — OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · xingwudao · `Py` · cited file [`sdk/python/openjev/__init__.py`](https://github.com/xingwudao/OpenJev/blob/HEAD/sdk/python/openjev/__init__.py), read 2026-09-24 · ⚠ `not Jev itself` `no licence`</sub>

- **[origin-civilization](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)** — AI life-and-civilization simulation: TypeSafe Jev makes every decision (typed, probabilistic, auditable); LLMs plan — OpenAI-compatible APIs, local models (Ollama, LM Studio), Claude Code, Codex. <sub>(upstream description)</sub>
  <sub>`Benchmark` · jacquesgariepy · `TS` · call site [`legacy/source/providers.js`](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION/blob/HEAD/legacy/source/providers.js), read 2026-09-22</sub>

- **[s1_ruby](https://github.com/innocentdiaz/s1_ruby)** — Makes S1-model 'measurement' (and the collapse that follows it) a Ruby primitive. <sub>(upstream description)</sub>
  <sub>`SDK` · innocentdiaz · `Rb` · call site [`lib/s1/providers/typesafe.rb`](https://github.com/innocentdiaz/s1_ruby/blob/HEAD/lib/s1/providers/typesafe.rb), read 2026-09-24 · ⚠ `one commit`</sub>

- **[sysone-bench](https://github.com/instax-dutta/sysone-bench)** — First independent head-to-head benchmark of System One decision models (Laya vs Jev) on byte-identical inputs <sub>(upstream description)</sub>
  <sub>`Benchmark` · instax-dutta · `Py` · call site [`runners/jev_runner.py`](https://github.com/instax-dutta/sysone-bench/blob/HEAD/runners/jev_runner.py), read 2026-09-22</sub>

- **[system-one-adapter-rust](https://github.com/codeitlikemiley/system-one-adapter-rust)** — Rust port of TypeSafe system-one-adapter (LLM-backed system_one evaluations) <sub>(upstream description)</sub>
  <sub>`Integration` · codeitlikemiley · `Rs` · call site [`src/client.rs`](https://github.com/codeitlikemiley/system-one-adapter-rust/blob/HEAD/src/client.rs), read 2026-09-22</sub>

- **[SystemOneDotNet](https://github.com/JabbaKadabra/SystemOneDotNet)** — .NET client for TypeSafe System One (Jev) — typed questions in, typed answers with probabilities and confidence out. No prompt engineering, no output parsing. <sub>(upstream description)</sub>
  <sub>`SDK` · jabbakadabra · `C#` · call site [`samples/SystemOneDotNet.Sample/Program.cs`](https://github.com/JabbaKadabra/SystemOneDotNet/blob/HEAD/samples/SystemOneDotNet.Sample/Program.cs), read 2026-09-24</sub>

- **[tinyjevclient](https://github.com/tinyhumansai/tinydecisionmodels)** — An integration with jev by typesafe.ai in Rust
  <sub>`Integration` · tinyhumansai · `Rs` · call site [`crates/tinyjevclient/src/client/test.rs`](https://github.com/tinyhumansai/tinydecisionmodels/blob/HEAD/crates/tinyjevclient/src/client/test.rs), read 2026-09-22 · ⚠ `archived`</sub>

- **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)** — The only platform with dedicated Jev observability: an OpenInference instrumentor that traces every decision call over OpenTelemetry.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul`</sub>

- **[typesafe](https://github.com/mattneel/typesafe)** — An idiomatic Elixir client for the TypeSafe AI API <sub>(upstream description)</sub>
  <sub>`SDK` · mattneel · `Ex` · call site [`lib/typesafe/req.ex`](https://github.com/mattneel/typesafe/blob/HEAD/lib/typesafe/req.ex), read 2026-09-24</sub>

- **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)** — Vercel's launch note for Jev on AI Gateway, with an experimental_evaluate sample using the model string typesafe-ai/jev.
  <sub>`Integration` · `TS` · `noul`</sub>

- **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)** — First-party Pydantic AI support: an Agent with output_type=bool over the typesafe:jev-latest model string.
  <sub>`Integration` · `Py`</sub>

- **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)** — Proxy Jev through LiteLLM for unified keys and cost tracking, with any path under /typesafe/ passed straight through.
  <sub>`Integration` · `sh`</sub>

- **[typesafe-ai-go](https://github.com/kisshan13/typesafe-ai-go)** — Community-maintained Go SDK for the TypeSafe AI System One evaluation API, with typed questions, fluent builders, retries, and examples. <sub>(upstream description)</sub>
  <sub>`SDK` · kisshan13 · `Go` · call site [`types.go`](https://github.com/kisshan13/typesafe-ai-go/blob/HEAD/types.go), read 2026-09-24 · ⚠ `one commit`</sub>

- **[typesafe-ai-java](https://github.com/jamilxt/typesafe-ai-java)** — Community-maintained Java SDK for the TypeSafe AI System One (Jev) API. Not an official TypeSafe product. <sub>(upstream description)</sub>
  <sub>`SDK` · jamilxt · `Java` · call site [`typesafe-ai-java-core/src/main/java/ai/typesafe/TypeSafeClient.java`](https://github.com/jamilxt/typesafe-ai-java/blob/HEAD/typesafe-ai-java-core/src/main/java/ai/typesafe/TypeSafeClient.java), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe-ai-rails](https://github.com/GenieRobot/typesafe-ai-rails)** — Community Rails integration for TypeSafe AI's System One API on the community typesafe-sdk gem: Rails configuration, persisted usage and cost telemetry, and an opt-in confidence policy for Choice and Score answers.
  <sub>`SDK` · genierobot · `Rb` · call site [`lib/typesafe/rails/client.rb`](https://github.com/GenieRobot/typesafe-ai-rails/blob/HEAD/lib/typesafe/rails/client.rb), read 2026-09-24</sub>

- **[typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs)** — Independent async and blocking Rust SDK for the TypeSafe AI System One API <sub>(upstream description)</sub>
  <sub>`SDK` · gilljon · `Rs` · call site [`src/lib.rs`](https://github.com/gilljon/typesafe-ai-rs/blob/HEAD/src/lib.rs), read 2026-09-22</sub>

- **[typesafe-ai-ruby](https://github.com/hnegishi/typesafe-ai-ruby)** — Ruby client for the TypeSafe AI(Jev) System One API <sub>(upstream description)</sub>
  <sub>`SDK` · hnegishi · `Rb` · call site [`lib/typesafe/constants.rb`](https://github.com/hnegishi/typesafe-ai-ruby/blob/HEAD/lib/typesafe/constants.rb), read 2026-09-22</sub>

- **[typesafe-client](https://github.com/JedimEmO/typesafe-client)** — Unofficial typed async Rust client for the TypeSafe System One API <sub>(upstream description)</sub>
  <sub>`SDK` · jedimemo · `Rs` · call site [`crates/typesafe-client/src/client/mod.rs`](https://github.com/JedimEmO/typesafe-client/blob/HEAD/crates/typesafe-client/src/client/mod.rs), read 2026-09-22 · ⚠ `one commit`</sub>

- **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)** — Point the official TypeSafe SDK at Vercel by changing one baseURL, or call the gateway's systemone endpoint directly with cURL.
  <sub>`Integration` · `TS` · `sh` · `noul`</sub>

- **[typesafe-go](https://github.com/zhirschtritt/typesafe-go)** — Idiomatic Go SDK for the TypeSafe AI API <sub>(upstream description)</sub>
  <sub>`SDK` · zhirschtritt · `Go` · call site [`client.go`](https://github.com/zhirschtritt/typesafe-go/blob/HEAD/client.go), read 2026-09-22</sub>

- **[typesafe-go](https://github.com/cole-gillespie/typesafe-go)** — unofficial go SDK for typesafe AI, with typed answers, retries, and context support <sub>(upstream description)</sub>
  <sub>`SDK` · cole-gillespie · `Go` · call site [`client.go`](https://github.com/cole-gillespie/typesafe-go/blob/HEAD/client.go), read 2026-09-24 · ⚠ `one commit`</sub>

- **[typesafe-go](https://github.com/Nibir1/typesafe-go)** — A zero-dependency community Go SDK, including a static analyser that flags poorly designed questions at compile time.
  <sub>`SDK` · Nibir1 · `Go` · `choice` · `score` · `noul` · call site [`cmd/typesafe/main.go`](https://github.com/Nibir1/typesafe-go/blob/HEAD/cmd/typesafe/main.go), read 2026-09-22 · ⚠ `code untested`</sub>

- **[typesafe-go](https://github.com/Shubham510/typesafe-go)** — Unofficial Go SDK for TypeSafe AI's System One API (Jev). <sub>(upstream description)</sub>
  <sub>`SDK` · shubham510 · `Go` · call site [`client.go`](https://github.com/Shubham510/typesafe-go/blob/HEAD/client.go), read 2026-09-24</sub>

- **[typesafe-rs](https://github.com/AbdelStark/typesafe-rs)** — Latency-first Rust SDK for TypeSafe System One. <sub>(upstream description)</sub>
  <sub>`SDK` · abdelstark · `Rs` · call site [`crates/typesafe-rs-mock/src/lib.rs`](https://github.com/AbdelStark/typesafe-rs/blob/HEAD/crates/typesafe-rs-mock/src/lib.rs), read 2026-09-22</sub>

- **[typesafe-sdk](https://github.com/joshmn/typesafe-sdk)** — Ruby client for typesafe.ai <sub>(upstream description)</sub>
  <sub>`SDK` · joshmn · `Rb` · call site [`lib/typesafe/sdk.rb`](https://github.com/joshmn/typesafe-sdk/blob/HEAD/lib/typesafe/sdk.rb), read 2026-09-22</sub>

- **[typesafe-sdk](https://github.com/binnash/typesafe-sdk)** — PHP & Laravel SDK for TypeSafe AI's JEV Model series <sub>(upstream description)</sub>
  <sub>`SDK` · binnash · `PHP` · call site [`config/typesafe.php`](https://github.com/binnash/typesafe-sdk/blob/HEAD/config/typesafe.php), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe-sdk](https://github.com/typesafe-sdk-csharp/typesafe-sdk)** — An unofficial .NET SDK for TypeSafe AI, published on NuGet, with deterministic question building and high-throughput verification.
  <sub>`SDK` · typesafe-sdk-csharp · `C#` · call site [`src/TypeSafe.AI/TypeSafeClientOptions.cs`](https://github.com/typesafe-sdk-csharp/typesafe-sdk/blob/HEAD/src/TypeSafe.AI/TypeSafeClientOptions.cs), read 2026-09-24</sub>

- **[typesafe-sdk-dotnet](https://github.com/hardkoded/typesafe-sdk-dotnet)** — Unofficial .NET port of the TypeSafe AI client SDK (typed questions & answers) <sub>(upstream description)</sub>
  <sub>`SDK` · hardkoded · `C#` · call site [`src/TypeSafe.AI.Sdk/TypeSafeClient.cs`](https://github.com/hardkoded/typesafe-sdk-dotnet/blob/HEAD/src/TypeSafe.AI.Sdk/TypeSafeClient.cs), read 2026-09-24</sub>

- **[typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go)** — Go SDK for the TypeSafe AI API — typed questions in, probability distributions out. <sub>(upstream description)</sub>
  <sub>`SDK` · tangerg · `Go` · call site [`client.go`](https://github.com/Tangerg/typesafe-sdk-go/blob/HEAD/client.go), read 2026-09-22</sub>

- **[typesafe-sdk-go](https://github.com/dwisiswant0/typesafe-sdk-go)** — Go SDK for TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`SDK` · dwisiswant0 · `Go` · call site [`client.go`](https://github.com/dwisiswant0/typesafe-sdk-go/blob/HEAD/client.go), read 2026-09-24 · ⚠ `one commit`</sub>

- **[typesafe-sdk-go](https://github.com/SergeAx/typesafe-sdk-go)** — TypeSafe.AI Go SDK <sub>(upstream description)</sub>
  <sub>`SDK` · sergeax · `Go` · call site [`config.go`](https://github.com/SergeAx/typesafe-sdk-go/blob/HEAD/config.go), read 2026-09-24</sub>

- **[typesafe-sdk-go](https://github.com/valksor/typesafe-sdk-go)** — Unofficial Go SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`SDK` · valksor · `Go` · call site [`client.go`](https://github.com/valksor/typesafe-sdk-go/blob/HEAD/client.go), read 2026-09-24</sub>

- **[typesafe-sdk-kotlin](https://github.com/ufec/typesafe-sdk-kotlin)** — A Kotlin SDK for TypeSafe AI, ported from the official JavaScript SDK with its deviations documented; ask typed questions about text and get typed answers back.
  <sub>`SDK` · ufec · `Kt` · call site [`src/commonMain/kotlin/me/ethanxu/typesafe/sdk/TypeSafeClient.kt`](https://github.com/ufec/typesafe-sdk-kotlin/blob/HEAD/src/commonMain/kotlin/me/ethanxu/typesafe/sdk/TypeSafeClient.kt), read 2026-09-24</sub>

- **[typesafe-sdk-php](https://github.com/Fox-Islam/typesafe-sdk-php)** — Unofficial PHP library for the TypeSafe API <sub>(upstream description)</sub>
  <sub>`SDK` · fox-islam · `PHP` · call site [`src/TypeSafe.php`](https://github.com/Fox-Islam/typesafe-sdk-php/blob/HEAD/src/TypeSafe.php), read 2026-09-24</sub>

- **[typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php)** — Unofficial PHP SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`SDK` · valksor · `PHP` · call site [`src/Client.php`](https://github.com/valksor/typesafe-sdk-php/blob/HEAD/src/Client.php), read 2026-09-24</sub>

- **[typesafe-sdk-ruby](https://github.com/afurm/typesafe-sdk-ruby)** — Unofficial Ruby SDK for the TypeSafe AI API (Jev model) - typed questions, retries, and typed errors. Community port of typesafe-sdk-js. <sub>(upstream description)</sub>
  <sub>`SDK` · afurm · `Rb` · call site [`lib/typesafe/sdk/client.rb`](https://github.com/afurm/typesafe-sdk-ruby/blob/HEAD/lib/typesafe/sdk/client.rb), read 2026-09-24</sub>

- **[typesafe-sdk-rust](https://github.com/codeitlikemiley/typesafe-sdk-rust)** — Rust SDK for the TypeSafe AI API <sub>(upstream description)</sub>
  <sub>`SDK` · codeitlikemiley · `Rs` · call site [`src/client.rs`](https://github.com/codeitlikemiley/typesafe-sdk-rust/blob/HEAD/src/client.rs), read 2026-09-22</sub>

- **[typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift)** — Unofficial Swift library for the TypeSafe API <sub>(upstream description)</sub>
  <sub>`SDK` · alterhq · `Swift` · call site [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/alterhq/typesafe-sdk-swift/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift), read 2026-09-22 · ⚠ `one commit`</sub>

- **[typesafe-sdk-swift](https://github.com/InsaneArts/typesafe-sdk-swift)** — Swift SDK for TypeSafe AI <sub>(upstream description)</sub>
  <sub>`SDK` · insanearts · `Swift` · call site [`Sources/TypeSafe/Client.swift`](https://github.com/InsaneArts/typesafe-sdk-swift/blob/HEAD/Sources/TypeSafe/Client.swift), read 2026-09-24</sub>

- **[typesafe-sdk-swift](https://github.com/marandaneto/typesafe-sdk-swift)** — typesafe-sdk-js and typesafe-sdk-python port for swift <sub>(upstream description)</sub>
  <sub>`SDK` · marandaneto · `Swift` · call site [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/marandaneto/typesafe-sdk-swift/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift), read 2026-09-24</sub>

- **[typesafe_ai](https://github.com/hfiguera/typesafe_ai)** — An Elixir client for TypeSafe AI with typed responses and bounded concurrency <sub>(upstream description)</sub>
  <sub>`SDK` · hfiguera · `Ex` · call site [`bench/recorded/tail-investigation/versions/async-timers/lib/typesafe/client.ex`](https://github.com/hfiguera/typesafe_ai/blob/HEAD/bench/recorded/tail-investigation/versions/async-timers/lib/typesafe/client.ex), read 2026-09-24</sub>

- **[typesafe_ai](https://github.com/typesend/typesafe_ai)** — Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers. <sub>(upstream description)</sub>
  <sub>`SDK` · typesend · `Ex` · call site [`lib/typesafe_api/client.ex`](https://github.com/typesend/typesafe_ai/blob/HEAD/lib/typesafe_api/client.ex), read 2026-09-24</sub>

- **[typesafe_sdk (Elixir)](https://github.com/nshkrdotcom/typesafe_sdk)** — An Elixir port of the official SDK.
  <sub>`SDK` · nshkrdotcom · `Ex` · call site [`codegen/typesafe_sdk/codegen/source/openapi.ex`](https://github.com/nshkrdotcom/typesafe_sdk/blob/HEAD/codegen/typesafe_sdk/codegen/source/openapi.ex), read 2026-09-22</sub>

- **[typesafe_sdk_ex](https://github.com/vinnie357/typesafe_sdk_ex)** — Typesafe AI SDK in Elixir using Req <sub>(upstream description)</sub>
  <sub>`SDK` · vinnie357 · `Ex` · call site [`lib/type_safe.ex`](https://github.com/vinnie357/typesafe_sdk_ex/blob/HEAD/lib/type_safe.ex), read 2026-09-22</sub>

- **[typesafeai-go](https://github.com/chez-shanpu/typesafeai-go)** — Go SDK for TypeSafe AI API https://docs.typesafe.ai/api <sub>(upstream description)</sub>
  <sub>`SDK` · chez-shanpu · `Go` · call site [`systemone.go`](https://github.com/chez-shanpu/typesafeai-go/blob/HEAD/systemone.go), read 2026-09-22</sub>

- **[typesafeai.net](https://github.com/Hawxy/TypeSafeAI.Net)** — .NET SDK for the TypeSafe AI platform <sub>(upstream description)</sub>
  <sub>`SDK` · hawxy · `C#` · call site [`src/TypeSafeAI.Extensions.AI/Evaluation/TypeSafeEvaluator.cs`](https://github.com/Hawxy/TypeSafeAI.Net/blob/HEAD/src/TypeSafeAI.Extensions.AI/Evaluation/TypeSafeEvaluator.cs), read 2026-09-22</sub>

- **[werr](https://github.com/pCwOrM/werr)** — Zero-memory System-1 decision engine & TypeSafe Jev wire-compatible runtime powered by Mandelbrot wave dynamics (The Zero-VRAM Gauntlet). <sub>(upstream description)</sub>
  <sub>`Jev-like alternative` · pcworm · `Py` · cited file [`werr/server.py`](https://github.com/pCwOrM/werr/blob/HEAD/werr/server.py), read 2026-09-24 · ⚠ `not Jev itself`</sub>

- **[what-is-jev](https://github.com/g0runmezadam/what-is-jev)** — Independent, source-linked research on TypeSafe AI's Jev (System One), with 947 rubric-scored public repositories, recurring patterns, datasets, and bilingual documentation. <sub>(upstream description)</sub>
  <sub>`Benchmark` · g0runmezadam · `Py`</sub>

- **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)** — Currently the most-starred sibling directory in this space.
  <sub>`Project` · ★1k+ · ⚠ `no licence`</sub>

- **[awesome-jev (heyjunpenn)](https://github.com/heyjunpenn/awesome-jev)** — The broadest sibling directory: hundreds of projects in six languages, with a README that is itself the parsed data source.
  <sub>`Project` · ★100+ · heyjunpenn</sub>

- **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)** — A sibling directory aiming at ecosystem breadth with commit-pinned sources, four README languages and a generated site.
  <sub>`Project` · ★100+ · logicrw</sub>

- **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)** — The only launch coverage with first-hand developer quotes rather than vendor figures, including a caution that interpreting the thresholds is now your job.
  <sub>`Article` · Tim Fernholz</sub>

- **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)** — Focuses on the missing explainability — the model returns no reasoning in language — and on every published benchmark coming from the vendor.
  <sub>`Article` · Tomislav Bezmalinović</sub>

- **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)** — The launch thread, and the densest single collection of scepticism: unsupported RLCD claims, apples-to-oranges latency comparisons, and the deliberate absence of public benchmarks.
  <sub>`Discussion`</sub>

- **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))** — Most useful as an index: its reference list is a fast route to the coverage worth reading.
  <sub>`Article`</sub>

- **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)** — An agent-builder's framing of where a decision model sits in an agent stack.
  <sub>`Article` · ⚠ `marketing`</sub>

- **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)** — Mainstream coverage of the launch and the speed with which gateways added support.
  <sub>`Article` · Josipa Majic Predin · ⚠ `vendor numbers` `paywall`</sub>

- **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)** — A review that puts the limitation in the title rather than burying it.
  <sub>`Video` · Gary Explains</sub>

- **[Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216)** — The first data-driven survey and analysis of Jev's application ecosystem examines 2,170 public GitHub projects, documenting rapid early growth, application domains, and decision-use patterns.
  <sub>`Article` · Guoming Ling, Muen Xue, and Zijian Ye</sub>

- **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)** — The only long-form founder interview: why RLHF was the wrong optimisation target, why public benchmarks were withheld, and the all-synthetic data approach.
  <sub>`Discussion` · Latent Space</sub>

- **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)** — A neutral survey of the architecture, the claimed benchmarks and the pricing, which states plainly that no large independent reproduction had surfaced.
  <sub>`Article` · Matt Crabtree</sub>

- **[jevai.org community app gallery](https://www.jevai.org/apps)** — Thirty-six community builds curated from social posts: browser agents, spreadsheet tooling, inbox search by intent, ad blocking with judgement, games and robotics.
  <sub>`Project` · ⚠ `unverified claims`</sub>

- **[jevai.org community site](https://www.jevai.org/)** — An unaffiliated community site with a playground, a preset decision API, an MCP server, downloadable skills and a gallery of community apps.
  <sub>`Project` · ⚠ `3rd-party key` `unverified claims`</sub>

- **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)** — An independent write-up whose most useful finding is a negative one: there is no paper, no reward function, no dataset description and no reproducible evaluation for RLCD.
  <sub>`Article`</sub>

- **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)** — The most sceptical mainstream piece: it challenges the no-hallucination framing on the grounds that a well-formed answer is not the same as a correct one.
  <sub>`Article` · Thomas Claburn</sub>

- **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)** — OpenRouter's listing for Jev, with its own model ids and the unusual pricing shape of paid input and free output.
  <sub>`Integration`</sub>

<a name="unindexed"></a>

## Not yet indexed by pattern

Projects and plugins with code, 252 of them, whose only pattern is `overview` and whose rows record no `patterns_reviewed`. `overview` is also where the keyword rules put a description they could not place, so these rows may never have been placed at all. A row leaves this list when a person gives it a pattern, or reads it against [the patterns](../patterns.md#overview) and records the date in `patterns_reviewed`. The [review queue](../review-queue.md#unsorted-overview) lists them with the rules' suggestion.

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐ — The official agent-skills repository behind the Claude Code plugin, holding the SKILL.md that teaches an agent the System One API.
  <sub>`Plugin` · ★1k+ · `sh`</sub>

- **[langchain](https://github.com/langchain-ai/langchain)** — The agent engineering platform. <sub>(upstream description)</sub>
  <sub>`Project` · ★100k+ · langchain-ai · `Py` · call site [`libs/partners/typesafe/langchain_typesafe/classifier.py`](https://github.com/langchain-ai/langchain/blob/HEAD/libs/partners/typesafe/langchain_typesafe/classifier.py), read 2026-09-22</sub>

- **[eliza](https://github.com/elizaOS/eliza)** — Open source agentic operating system <sub>(upstream description)</sub>
  <sub>`Project` · ★10k+ · elizaos · `TS` · call site [`packages/agent/src/services/typesafe/client.ts`](https://github.com/elizaOS/eliza/blob/HEAD/packages/agent/src/services/typesafe/client.ts), read 2026-09-22</sub>

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)** — ⌥ Coding agent with the IDE wired in
  <sub>`Project` · ★10k+ · can1357 · `TS` · call site [`packages/ai/src/judgment/typesafe.ts`](https://github.com/can1357/oh-my-pi/blob/HEAD/packages/ai/src/judgment/typesafe.ts), read 2026-09-22</sub>

- **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)** — Wraps the sync and async clients so every system_one call is recorded as a traced span.
  <sub>`Project` · ★10k+ · `Py` · call site [`sdks/python/src/opik/integrations/typesafe/opik_tracker.py`](https://github.com/comet-ml/opik/blob/HEAD/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)</sub>

- **[pydantic-ai](https://github.com/pydantic/pydantic-ai)** — How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end. <sub>(upstream description)</sub>
  <sub>`Project` · ★10k+ · pydantic · `Py` · call site [`pydantic_ai_slim/pydantic_ai/models/typesafe.py`](https://github.com/pydantic/pydantic-ai/blob/HEAD/pydantic_ai_slim/pydantic_ai/models/typesafe.py), read 2026-09-22</sub>

- **[ax](https://github.com/ax-llm/ax)** — The pretty much "official" DSPy framework for Typescript <sub>(upstream description)</sub>
  <sub>`Project` · ★1k+ · ax-llm · `TS` · call site [`src/ax/ai/typesafe/client.ts`](https://github.com/ax-llm/ax/blob/HEAD/src/ax/ai/typesafe/client.ts), read 2026-09-22</sub>

- **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)** — A Go gateway provider that passes the native API through one-to-one, so the official SDKs work by changing only the base URL.
  <sub>`Project` · ★1k+ · `Go` · call site [`core/providers/typesafe/typesafe.go`](https://github.com/maximhq/bifrost/blob/HEAD/core/providers/typesafe/typesafe.go)</sub>

- **[celesto](https://github.com/CelestoAI/celesto)** — Secure and persistent computer for AI agents -- build your own Grokbot, and Muse.
  <sub>`Project` · ★1k+ · celestoai · `Py` · call site [`examples/pr-review-jev/models.py`](https://github.com/CelestoAI/celesto/blob/HEAD/examples/pr-review-jev/models.py), read 2026-09-22</sub>

- **[laya-mlx](https://github.com/mizorewww/laya-mlx)** — Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text generation, PyTorch, or cloud API. <sub>(upstream description)</sub>
  <sub>`Project` · ★1k+ · mizorewww · `Py` · call site [`laya_mlx/agent.py`](https://github.com/mizorewww/laya-mlx/blob/HEAD/laya_mlx/agent.py), read 2026-09-22</sub>

- **[memsearch](https://github.com/zilliztech/memsearch)** — A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★1k+ · zilliztech · `Py` · call site [`src/memsearch/jev_reranker.py`](https://github.com/zilliztech/memsearch/blob/HEAD/src/memsearch/jev_reranker.py), read 2026-09-22</sub>

- **[vellum-assistant](https://github.com/vellum-ai/vellum-assistant)** — An AI Assistant that’s easy to setup, does your work 24/7, knows your preferences and gets better over time. <sub>(upstream description)</sub>
  <sub>`Project` · ★1k+ · vellum-ai · `TS` · call site [`assistant/src/providers/jev/client.ts`](https://github.com/vellum-ai/vellum-assistant/blob/HEAD/assistant/src/providers/jev/client.ts), read 2026-09-22</sub>

- **[agent-router](https://github.com/nidhi-singh02/agent-router)** — CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · nidhi-singh02 · `TS` · call site [`packages/router/src/semantic/typesafe-client.ts`](https://github.com/nidhi-singh02/agent-router/blob/HEAD/packages/router/src/semantic/typesafe-client.ts), read 2026-09-22</sub>

- **[aiavatarkit](https://github.com/uezo/aiavatarkit)** — 🥰 Building AI-based conversational avatars lightning fast ⚡️💬 <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · uezo · `Py` · call site [`aiavatar/sts/vad/turn_end_gates/jev.py`](https://github.com/uezo/aiavatarkit/blob/HEAD/aiavatar/sts/vad/turn_end_gates/jev.py), read 2026-09-22</sub>

- **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)** — A sibling directory whose submissions are reviewed by Jev itself, with a notably thorough list of multi-language community clients.
  <sub>`Project` · ★100+ · fatwang2 · `JS` · call site [`.github/workflows/jev-review.yml`](https://github.com/fatwang2/awesome-jev/blob/HEAD/.github/workflows/jev-review.yml)</sub>

- **[crush-monitor](https://github.com/FerryCorleone/crush-monitor)** — Crush 好感监控器：用 Jev 分析微信聊天的情绪、意图和回复表现。本机部署，使用自己的 API Key。 <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · ferrycorleone · `TS` · call site [`server/provider-config.ts`](https://github.com/FerryCorleone/crush-monitor/blob/HEAD/server/provider-config.ts), read 2026-09-24</sub>

- **[dasheng](https://github.com/wquguru/dasheng)** — 大声读 — R2T2 流式 ASR 听，Jev 逐词判，英文朗读评分 <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · wquguru · `JS` · call site [`lib/jev.js`](https://github.com/wquguru/dasheng/blob/HEAD/lib/jev.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[distill](https://github.com/samuelfaj/distill)** — Get FAR MORE done with FAR FEWER tokens 🔥 <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · samuelfaj · `Rs` · call site [`crates/codegen/distill-workspace/src/jev/client.rs`](https://github.com/samuelfaj/distill/blob/HEAD/crates/codegen/distill-workspace/src/jev/client.rs), read 2026-09-22</sub>

- **[djev-spark](https://github.com/mmastrac/djev-spark)** — DiffusionGemma NVFP4 structured decisions on a DGX Spark: container recipe <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · mmastrac · `TS` · call site [`scripts/long-context-probe.py`](https://github.com/mmastrac/djev-spark/blob/HEAD/scripts/long-context-probe.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Jev](https://github.com/cobusgreyling/Jev)** — Unofficial TypeSafe Jev showcase — System One decisions, not chat. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · cobusgreyling · `Py` · call site [`jev_lab/client.py`](https://github.com/cobusgreyling/Jev/blob/HEAD/jev_lab/client.py), read 2026-09-24</sub>

- **[jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac)** — 微信消息意图识别悬浮窗（macOS）：看屏 + 本地小模型判断意图和风险，再按话术生成回复候选。纯只读、不注入微信。
  <sub>`Project` · ★100+ · jev-chat · `Py` · call site [`src/judge_jev.py`](https://github.com/jev-chat/jev-chat-jarvis-mac/blob/HEAD/src/judge_jev.py), read 2026-09-22</sub>

- **[jev-chat-windows](https://github.com/jev-chat/jev-chat-windows)** — 微信（Windows 4.x）旁挂的回复辅助：窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动
  <sub>`Project` · ★100+ · jev-chat · `Py` · call site [`core/jev_client.py`](https://github.com/jev-chat/jev-chat-windows/blob/HEAD/core/jev_client.py), read 2026-09-22</sub>

- **[jev-docs-zh](https://github.com/datawhalechina/jev-cookbook)** — Jev 模型（TypeSafe AI）官方使用文档的中文翻译 \| Unofficial Chinese translation of the official Jev (TypeSafe AI) docs — https://docs.typesafe.ai
  <sub>`Project` · ★100+ · bald0wang · `Py` · call site [`dist/assets/search-index.js`](https://github.com/datawhalechina/jev-cookbook/blob/HEAD/dist/assets/search-index.js), read 2026-09-22</sub>

- **[jev-experiments](https://github.com/dabit3/jev-experiments)** — Nader Dabit's collection of small Jev experiments, one per folder: a commit reviewer, a shell guard, a send guard, a log sentinel, instant search, reranking, a voice-turn detector and more.
  <sub>`Project` · ★100+ · dabit3 · `TS` · call site [`commit-sentry/src/jev.ts`](https://github.com/dabit3/jev-experiments/blob/HEAD/commit-sentry/src/jev.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-foundation-models](https://github.com/peterfriese/system-one-foundation-models)** — A lightweight, native Swift 6 bridge integrating TypeSafe AI's Jev System One decision model into Apple's Foundation Models framework. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · peterfriese · `Swift` · call site [`Sources/JevFoundationModels/JevLanguageModel.swift`](https://github.com/peterfriese/system-one-foundation-models/blob/HEAD/Sources/JevFoundationModels/JevLanguageModel.swift), read 2026-09-22</sub>

- **[jev-skill](https://github.com/wuyoscar/jev-skill)** — An agent skill plus CLI that validates all three primitives, requires explicit consent before a billed call, and forbids inventing output when simulating.
  <sub>`Plugin` · ★100+ · `Py` · `choice` · `score` · `noul` · call site [`skills/jev/scripts/jev.py`](https://github.com/wuyoscar/jev-skill/blob/HEAD/skills/jev/scripts/jev.py), read 2026-09-22</sub>

- **[jev-voice](https://github.com/kevinbadi/jev-voice)** — Talk to your Mac. Local whisper.cpp + one Jev (TypeSafe) call per command + macOS automation. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · kevinbadi · `Py` · call site [`jev_voice/config.py`](https://github.com/kevinbadi/jev-voice/blob/HEAD/jev_voice/config.py), read 2026-09-22</sub>

- **[jevmem](https://github.com/Avinash-jetwani/jevmem)** — Automatic project memory for Claude Code. Also works with Cursor and Codex. <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★100+ · avinash-jetwani · `TS` · call site [`src/jev.ts`](https://github.com/Avinash-jetwani/jevmem/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[Jevmind](https://github.com/dealerdefi/Jevmind)** — An agent's decisions pulled out of its prose into one place: typed answers with a confidence, behind a gate written in code, sealed in a ledger, graded and learned from. Runs offline on a local rules brain; Jev can be swapped in with one flag.
  <sub>`Project` · ★100+ · dealerdefi · `Py` · call site [`src/jevmind/brain.py`](https://github.com/dealerdefi/Jevmind/blob/HEAD/src/jevmind/brain.py), read 2026-09-24</sub>

- **[kody](https://github.com/kentcdodds/kody)** — 🐨 Your assistant's home — the memory, keys, code, and automations your AI agent keeps, portable across every MCP host. Built on Cloudflare Workers. <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★100+ · kentcdodds · `TS` · call site [`packages/worker/src/mcp/tools/search-jev-rerank.ts`](https://github.com/kentcdodds/kody/blob/HEAD/packages/worker/src/mcp/tools/search-jev-rerank.ts), read 2026-09-22</sub>

- **[laya](https://github.com/receptron/laya)** — Run Laya, the open-source Jev-compatible System-1 decision model, from Node.js / TypeScript via ONNX Runtime <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · receptron · `TS` · call site [`src/laya.ts`](https://github.com/receptron/laya/blob/HEAD/src/laya.ts), read 2026-09-22</sub>

- **[laya-ultrafast](https://github.com/ipenywis/laya-ultrafast)** — Same as jev-ultrafast but using Laya <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · ipenywis · `Py` · call site [`laya_ultrafast/model.py`](https://github.com/ipenywis/laya-ultrafast/blob/HEAD/laya_ultrafast/model.py), read 2026-09-22</sub>

- **[laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev)** — Laya vs Jev: local MLX and hosted AI decisions playing T-Rex side by side, with live metrics and replay recording <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · virajbhartiya · `Py` · call site [`laya_mlx/agent.py`](https://github.com/virajbhartiya/laya-vs-jev/blob/HEAD/laya_mlx/agent.py), read 2026-09-22</sub>

- **[openwhisper](https://github.com/Knuckles92/OpenWhisper)** — Local speech-to-text, dictation, and meetings with Whisper and OpenAI API. Optional Windows x64 engines: Parakeet, Qwen3-ASR, Nemotron Streaming, and Moonshine.
  <sub>`Project` · ★100+ · knuckles92 · `Py` · call site [`benchmarks/typesafe_experiments.py`](https://github.com/Knuckles92/OpenWhisper/blob/HEAD/benchmarks/typesafe_experiments.py), read 2026-09-22</sub>

- **[orchestkit](https://github.com/yonatangross/orchestkit)** — The Complete AI Development Toolkit for Claude Code. 106 skills, 36 agents, 171 hooks. Install `ork` for stable (v9.x), or `ork-alpha` for the v10 line, which ships daily. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★100+ · yonatangross · `TS` · call site [`docs/audits/jev-session-category-heldout-2026-09-17/run_jev_b.mjs`](https://github.com/yonatangross/orchestkit/blob/HEAD/docs/audits/jev-session-category-heldout-2026-09-17/run_jev_b.mjs), read 2026-09-22</sub>

- **[pi-fabric](https://github.com/fabric-runtime/pi-fabric)** — A programmable tool and agent runtime for Pi <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · monotykamary · `TS` · call site [`src/jev/routes.ts`](https://github.com/fabric-runtime/pi-fabric/blob/HEAD/src/jev/routes.ts), read 2026-09-22</sub>

- **[req_llm](https://github.com/agentjido/req_llm)** — Composable Elixir library for LLM interactions built on Req and Finch <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · agentjido · `Ex` · call site [`lib/req_llm/providers/typesafe.ex`](https://github.com/agentjido/req_llm/blob/HEAD/lib/req_llm/providers/typesafe.ex), read 2026-09-22</sub>

- **[runline](https://github.com/Michaelliv/runline)** — ⚡ Code mode for agents <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · michaelliv · `TS` · call site [`packages/runline-plugins/typesafe/src/shared.ts`](https://github.com/Michaelliv/runline/blob/HEAD/packages/runline-plugins/typesafe/src/shared.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[smithers](https://github.com/smithersai/smithers)** — Smithers is an agentic workflow framework for defining workflows in simple TypeScript configuration files and executing them quickly, durably, and reliably <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · smithersai · `TS` · call site [`apps/server/src/jev.ts`](https://github.com/smithersai/smithers/blob/HEAD/apps/server/src/jev.ts), read 2026-09-22</sub>

- **[stanley-code](https://github.com/devagrawal09/stanley-code)** — Bounded TypeSafe Jev workflows for coding agents. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · devagrawal09 · `TS` · call site [`src/adapters/jev.ts`](https://github.com/devagrawal09/stanley-code/blob/HEAD/src/adapters/jev.ts), read 2026-09-22</sub>

- **[third-hand](https://github.com/shhivv/third-hand)** — computer-use assistant w/ decision models <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · shhivv · `Swift` · call site [`Sources/ThirdHand/JevClient.swift`](https://github.com/shhivv/third-hand/blob/HEAD/Sources/ThirdHand/JevClient.swift), read 2026-09-22</sub>

- **[typesafe-mcp](https://github.com/itsmostafa/system-one-connector)** — The easiest first step once you have a key: registers Jev into Claude Code, Claude Desktop, Codex and Pi with one command.
  <sub>`Plugin` · ★100+ · `Go` · `choice` · `score` · `noul` · call site [`cmd/evaluate/main.go`](https://github.com/itsmostafa/system-one-connector/blob/HEAD/cmd/evaluate/main.go), read 2026-09-22</sub>

- **[webctl](https://github.com/dorkitude/webctl)** — Smart web search CLI for agents, backed by Jev. Saves a lot of tokens. <sub>(upstream description)</sub>
  <sub>`Project` · ★100+ · dorkitude · `Go` · call site [`internal/jev/client.go`](https://github.com/dorkitude/webctl/blob/HEAD/internal/jev/client.go), read 2026-09-22</sub>

- **[ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill)** — Skill for Hermes, and other agents, to ask typesafe's jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · shantanugoel · `Py` · call site [`scripts/askjev.py`](https://github.com/shantanugoel/ask-jev-skill/blob/HEAD/scripts/askjev.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[awesome-jev](https://github.com/daftAI2026/awesome-jev)** — TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)
  <sub>`Project` · ★10+ · daftai2026 · `TS` · call site [`scripts/jev-client.ts`](https://github.com/daftAI2026/awesome-jev/blob/HEAD/scripts/jev-client.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[call-coach-ai](https://github.com/ZeroGold/call-coach-ai)** — Jev powered call coach <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · zerogold · `TS` · call site [`server.mjs`](https://github.com/ZeroGold/call-coach-ai/blob/HEAD/server.mjs), read 2026-09-22</sub>

- **[captaincore](https://github.com/CaptainCore/captaincore)** — 👨🏽‍💻 CaptainCore is a command line application for automating WordPress maintenance. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · captaincore · `Go` · call site [`typesafe/client.go`](https://github.com/CaptainCore/captaincore/blob/HEAD/typesafe/client.go), read 2026-09-22</sub>

- **[clash-jev](https://github.com/bytelabs-oss/clash-jev)** — A Clash Royale bot with no trained policy: Jev (TypeSafe System One) makes every decision from the live game state <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · bytelabs-oss · `Py` · call site [`clash_jev/policy.py`](https://github.com/bytelabs-oss/clash-jev/blob/HEAD/clash_jev/policy.py), read 2026-09-22</sub>

- **[cultivar](https://github.com/pinecone-io/cultivar)** — Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · pinecone-io · `Py` · call site [`evals/framework/typesafe_grader.py`](https://github.com/pinecone-io/cultivar/blob/HEAD/evals/framework/typesafe_grader.py), read 2026-09-22</sub>

- **[dspy-typesafeify](https://github.com/typesafeainate/dspy-typesafeify)** — Add a decorator for dspy Signatures that automatically uses TypeSafe where relevant <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · typesafeainate · `Py` · call site [`examples/typesafe_dspy_ticket_triage/run_demo.py`](https://github.com/typesafeainate/dspy-typesafeify/blob/HEAD/examples/typesafe_dspy_ticket_triage/run_demo.py), read 2026-09-22</sub>

- **[duckdb-jev](https://github.com/colliber/duckdb-jev)** — DuckDB extension: typed Jev answers as real SQL types <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · colliber · `C++` · call site [`src/include/jev_secret.hpp`](https://github.com/colliber/duckdb-jev/blob/HEAD/src/include/jev_secret.hpp), read 2026-09-24</sub>

- **[edgejev](https://github.com/yzfly/edgejev)** — 离线可用的本地类型化决策：4 核 CPU 单题 15.6ms。Local & offline Jev / System One inference on CPU — ONNX + INT8, no torch at runtime. 支持 laya / kev / PlayJev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · yzfly · `Py` · call site [`edgejev/serve.py`](https://github.com/yzfly/edgejev/blob/HEAD/edgejev/serve.py), read 2026-09-22</sub>

- **[is-jeven](https://github.com/wobsoriano/is-jeven)** — Is it even? Ask Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · wobsoriano · `JS` · call site [`index.js`](https://github.com/wobsoriano/is-jeven/blob/HEAD/index.js), read 2026-09-24</sub>

- **[james_library](https://github.com/topherchris420/james_library)** — R.A.I.N. Lab is an experimental scientific-agent architecture that separates fast local judgment, independent probabilistic evaluation, multi-agent deliberation, evidence, and authorization into distinct computational layers.🐙(Predates Karpathy's AutoResearch) <sub>(earlier upstream description)</sub>
  <sub>`Project` · ★10+ · topherchris420 · `Rs` · call site [`james_library/judgment/typesafe.py`](https://github.com/topherchris420/james_library/blob/HEAD/james_library/judgment/typesafe.py), read 2026-09-24 · ⚠ `archived`</sub>

- **[jeq](https://github.com/cristianoliveira/jeq)** — What happens when jev meets jq? Intelligence you can pipe for quick experimentation and scripts <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · cristianoliveira · `Go` · call site [`internal/infra/typesafeapi/client.go`](https://github.com/cristianoliveira/jeq/blob/HEAD/internal/infra/typesafeapi/client.go), read 2026-09-24</sub>

- **[jev](https://github.com/BorisLeMeec/jev)** — A claude code plugin for jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · borislemeec · `Go` · call site [`internal/typesafe/client.go`](https://github.com/BorisLeMeec/jev/blob/HEAD/internal/typesafe/client.go), read 2026-09-22</sub>

- **[Jev](https://github.com/mayank953/Jev)** — Six live, side-by-side demos of Jev deciding while an LLM writes the words and code owns the control flow; the LLM side switches between Claude and Kimi models.
  <sub>`Project` · ★10+ · mayank953 · `JS` · call site [`src/jev.ts`](https://github.com/mayank953/Jev/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[jev](https://github.com/okooo5km/jev)** — Typed decisions from the shell: an unofficial stdlib-Python CLI and Agent Skill for TypeSafe's Jev model, via the TypeSafe API (default) or OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · okooo5km · `Py` · call site [`jev/scripts/jev`](https://github.com/okooo5km/jev/blob/HEAD/jev/scripts/jev), read 2026-09-24</sub>

- **[jev-blindspot](https://github.com/jsk4581/jev-blindspot)** — A side-panel assistant that finds the blind spots in your prompts. For Claude Code and Codex CLI. <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★10+ · jsk4581 · `TS` · call site [`scripts/gate-tune.mjs`](https://github.com/jsk4581/jev-blindspot/blob/HEAD/scripts/gate-tune.mjs), read 2026-09-24</sub>

- **[jev-canvas](https://github.com/gaborishka/jev-canvas)** — Draw on a tldraw canvas with your voice and a pointing finger. Jev (TypeSafe System One) decides action, target and place in ~350 ms per spoken word. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · gaborishka · `JS` · call site [`server/decide.js`](https://github.com/gaborishka/jev-canvas/blob/HEAD/server/decide.js), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-chat-for-twitch](https://github.com/ethanplusai/jev-chat-for-twitch)** — Filter any live Twitch chat with Jev: a bring-your-own-key Chrome extension <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · ethanplusai · `JS` · call site [`extension/jev.mjs`](https://github.com/ethanplusai/jev-chat-for-twitch/blob/HEAD/extension/jev.mjs), read 2026-09-22</sub>

- **[jev-chat-windows-deepseek-jev](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev)** — Windows 微信回复助手：DeepSeek 官方生成话术，TypeSafe JEV 官方判断排序，支持可取消的 3 秒自动发送。
  <sub>`Project` · ★10+ · aimark-dai · `Py` · call site [`core/typesafe_client.py`](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev/blob/HEAD/core/typesafe_client.py), read 2026-09-22</sub>

- **[jev-cli](https://github.com/shaharia-lab/jev-cli)** — Command-line tool for TypeSafe AI's Jev model. Ask yes/no, multiple-choice and rubric questions about any text and get calibrated probabilities back. Answers become exit codes for shells and CI, JSON for scripts, and MCP tools for AI agents. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · shaharia-lab · `Rs` · call site [`crates/jev-cli/src/cli.rs`](https://github.com/shaharia-lab/jev-cli/blob/HEAD/crates/jev-cli/src/cli.rs), read 2026-09-24</sub>

- **[jev-judge-mcp](https://github.com/PyModel/jev-judge-mcp)** — Typed judgment tools for MCP agents. TypeSafe's Jev model as verify, screen, find, classify, rerank, decide, compare, extract, review, gate, and score: the model judges, policy decides auto, review, or escalate. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · pymodel · `Py` · call site [`src/jev_judge_mcp/domain/questions.py`](https://github.com/PyModel/jev-judge-mcp/blob/HEAD/src/jev_judge_mcp/domain/questions.py), read 2026-09-24</sub>

- **[jev-leftpad](https://github.com/f/jev-leftpad)** — Left-pad strings with TypeSafe AI's Jev. For reasons. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · f · `JS` · call site [`src/index.js`](https://github.com/f/jev-leftpad/blob/HEAD/src/index.js), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-mcp](https://github.com/burnigtm/jev-mcp)** — MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · burnigtm · `TS` · call site [`src/typesafe.ts`](https://github.com/burnigtm/jev-mcp/blob/HEAD/src/typesafe.ts), read 2026-09-24</sub>

- **[jev-paint](https://github.com/achimala/jev-paint)** — Use Jev to make art! <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · achimala · `JS` · call site [`web/jev.mjs`](https://github.com/achimala/jev-paint/blob/HEAD/web/jev.mjs), read 2026-09-22</sub>

- **[jev-playground](https://github.com/mizchi/jev-playground)** — A playground for calling Jev from MoonBit, with a CLI per question type (score, choice, noul) and measured reports on which composition patterns win.
  <sub>`Project` · ★10+ · mizchi · `TS` · call site [`experiments/agent-questions/src/spec.ts`](https://github.com/mizchi/jev-playground/blob/HEAD/experiments/agent-questions/src/spec.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-recipes](https://github.com/agencyenterprise/jev-recipes)** — 80+ composable TypeScript recipes powered by Jev for AI agents, retrieval, answer verification, and conversation workflows.
  <sub>`Project` · ★10+ · agencyenterprise · `TS` · call site [`examples/checkers/ai.mjs`](https://github.com/agencyenterprise/jev-recipes/blob/HEAD/examples/checkers/ai.mjs), read 2026-09-24</sub>

- **[jev-register-tool](https://github.com/2951461586/Jev-Register-Tool)** — TypeSafe（Jev / System One）申请 → 确认邮件 → 获批 → 注册 → 建 API Key 全链路工具，纯 HTTP 无浏览器 <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · 2951461586 · `Py` · call site [`src/typesafe.py`](https://github.com/2951461586/Jev-Register-Tool/blob/HEAD/src/typesafe.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-rules](https://github.com/EliaAlberti/jev-rules)** — Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · eliaalberti · `JS` · call site [`plugins/jev-rules/hooks/lib/jev.mjs`](https://github.com/EliaAlberti/jev-rules/blob/HEAD/plugins/jev-rules/hooks/lib/jev.mjs), read 2026-09-22</sub>

- **[jev-seo](https://github.com/AkashPriyadarshii/jev-seo)** — 100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One https://akashpriyadarshii.github.io/jev-seo/
  <sub>`Plugin` · ★10+ · akashpriyadarshii · `Rs` · call site [`src/engine.rs`](https://github.com/AkashPriyadarshii/jev-seo/blob/HEAD/src/engine.rs), read 2026-09-24</sub>

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)** — Claude Code plugin: asks TypeSafe Jev which installed skill fits each prompt and logs the answer (shadow-first). A working reference for the skill-suggestion cookbook on Claude Code — the README records why it is unlikely to help a strong model as a router. <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★10+ · shimo4228 · `Py` · call site [`scripts/jev_client.py`](https://github.com/shimo4228/jev-skill-router/blob/HEAD/scripts/jev_client.py), read 2026-09-22 · ⚠ `measured, not adopted`</sub>

- **[jev-skill-suggester](https://github.com/win4r/jev-skill-suggester)** — 用 TypeSafe Jev 推荐已安装 Skill / Bounded installed-skill recommendations with TypeSafe Jev. Python CLI, Codex skill, bilingual docs and live examples. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · win4r · `Py` · call site [`scripts/jev_client.py`](https://github.com/win4r/jev-skill-suggester/blob/HEAD/scripts/jev_client.py), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-spring-boot-starter](https://github.com/danvega/jev-spring-boot-starter)** — A simple Spring Boot 4 starter for TypeSafe Jev using Spring MVC and RestClient <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · danvega · `Java` · call site [`src/main/java/dev/danvega/jev/autoconfigure/JevProperties.java`](https://github.com/danvega/jev-spring-boot-starter/blob/HEAD/src/main/java/dev/danvega/jev/autoconfigure/JevProperties.java), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jev-studio](https://github.com/utk2103/jev-studio)** — if you're experimenting with jev it will be easier from here <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · utk2103 · `Py` · call site [`jev_studio/cli/provider.py`](https://github.com/utk2103/jev-studio/blob/HEAD/jev_studio/cli/provider.py), read 2026-09-22</sub>

- **[jev-tetris](https://github.com/trungdq88/jev-tetris)** — Jev play Tetris in real-time against other AI models <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · trungdq88 · `JS` · call site [`lib/typesafe.mjs`](https://github.com/trungdq88/jev-tetris/blob/HEAD/lib/typesafe.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-to-answer](https://github.com/csskrtao/jev-to-answer)** — A Book of Answers toy: ask a question and Jev picks the answer.
  <sub>`Project` · ★10+ · csskrtao · `JS` · call site [`src/jev.js`](https://github.com/csskrtao/jev-to-answer/blob/HEAD/src/jev.js), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-trades](https://github.com/zadescoxp/Jev-Trades)** — Trading bot with the all new TypeSafe AI's first system one model named as Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · zadescoxp · `Py` · call site [`pipeline/paper_trader.py`](https://github.com/zadescoxp/Jev-Trades/blob/HEAD/pipeline/paper_trader.py), read 2026-09-22</sub>

- **[jev-tree](https://github.com/Chuf-H/jev-tree)** — Jev-native probability tree and graph runtime for verifiable multi-step decision making. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · chuf-h · `Py` · call site [`src/jevtree/providers.py`](https://github.com/Chuf-H/jev-tree/blob/HEAD/src/jevtree/providers.py), read 2026-09-24</sub>

- **[jev-trip](https://github.com/liaoyuhua/jev-trip)** — Two Minds, One Trip. https://jev-trip.vercel.app/ <sub>(earlier upstream description)</sub>
  <sub>`Project` · ★10+ · liaoyuhua · `TS` · call site [`lib/providers/jev.ts`](https://github.com/liaoyuhua/jev-trip/blob/HEAD/lib/providers/jev.ts), read 2026-09-24</sub>

- **[jev-vs-ml](https://github.com/QuicqDev/Jev-vs-ML)** — Jev-vs-ML <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · quicqdev · `Py` · call site [`jevbench_v4/providers.py`](https://github.com/QuicqDev/Jev-vs-ML/blob/HEAD/jevbench_v4/providers.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[Jev_Ontology](https://github.com/dagfinndybvig/Jev_Ontology)** — Trying to combine Jev with ontology <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · dagfinndybvig · `Py` · call site [`mvp_jev_ontology.py`](https://github.com/dagfinndybvig/Jev_Ontology/blob/HEAD/mvp_jev_ontology.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev_stock](https://github.com/sosopop/jev_stock)** — An experimental JEV-powered framework for forecasting short-term stock price direction from structured market data. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · sosopop · `Py` · call site [`jev_hk_predict.py`](https://github.com/sosopop/jev_stock/blob/HEAD/jev_hk_predict.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevchat](https://github.com/kyle-pena-nlp/jevchat)** — Turns Jev into a chatbot <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kyle-pena-nlp · `Py` · call site [`jevchat/client.py`](https://github.com/kyle-pena-nlp/jevchat/blob/HEAD/jevchat/client.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jevernetes](https://github.com/sunil-sadasivan/jevernetes)** — Live Kubernetes log analysis, contextual investigation, and agent handoff powered by Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · sunil-sadasivan · `Py` · call site [`jevernetes/jev.py`](https://github.com/sunil-sadasivan/jevernetes/blob/HEAD/jevernetes/jev.py), read 2026-09-22</sub>

- **[jevgraph](https://github.com/chenmingtang830/jevgraph)** — Evidence-backed knowledge graph construction with typed Jev relation decisions <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · chenmingtang830 · `Py` · call site [`src/jevgraph/benchmark.py`](https://github.com/chenmingtang830/jevgraph/blob/HEAD/src/jevgraph/benchmark.py), read 2026-09-22</sub>

- **[jeview](https://github.com/andududu/jeview)** — An unofficial local visualizer for Jev (TypeSafe): a live view of every call your code makes. Not affiliated with TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · andududu · `JS` · call site [`jeview.ts`](https://github.com/andududu/jeview/blob/HEAD/jeview.ts), read 2026-09-22</sub>

- **[jevify](https://github.com/altryne/jevify)** — An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent community experiments. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · altryne · `Py` · call site [`scripts/jev_client.py`](https://github.com/altryne/jevify/blob/HEAD/scripts/jev_client.py), read 2026-09-22</sub>

- **[jevloop](https://github.com/zjunlp/JevLoop)** — The agent loop where decisions don't cost a large language model call. Zero deps, runs offline, no API key needed. <sub>(earlier upstream description)</sub>
  <sub>`Project` · ★10+ · zjunlp · `TS` · call site [`bench/compare.ts`](https://github.com/zjunlp/JevLoop/blob/HEAD/bench/compare.ts), read 2026-09-22</sub>

- **[jevocks](https://github.com/unicodeveloper/jevocks)** — Everyday Stocks Status with Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · unicodeveloper · `TS` · call site [`src/lib/classify.ts`](https://github.com/unicodeveloper/jevocks/blob/HEAD/src/lib/classify.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevplayspokemon](https://github.com/anxkhn/JevPlaysPokemon)** — Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · anxkhn · `TS` · call site [`jev.js`](https://github.com/anxkhn/JevPlaysPokemon/blob/HEAD/jev.js), read 2026-09-22</sub>

- **[jevthoven](https://github.com/cocktailpeanut/jevthoven)** — AI Music (MIDI) generator powered by Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · cocktailpeanut · `TS` · call site [`app/scripts/live-smoke.mjs`](https://github.com/cocktailpeanut/jevthoven/blob/HEAD/app/scripts/live-smoke.mjs), read 2026-09-22</sub>

- **[jevtown](https://github.com/gaborishka/jevtown)** — Jevtown: a social network where people write and 10,000 AI personas react <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · gaborishka · `JS` · call site [`public/shared/jev.js`](https://github.com/gaborishka/jevtown/blob/HEAD/public/shared/jev.js), read 2026-09-22</sub>

- **[jevvy](https://github.com/PanAchy/jevvy)** — Jev-powered plugins for coding agents <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · panachy · `TS` · call site [`packages/core/src/typesafe.ts`](https://github.com/PanAchy/jevvy/blob/HEAD/packages/core/src/typesafe.ts), read 2026-09-22</sub>

- **[jot](https://github.com/runta-dev/jot)** — The first general-purpose System One agent for Jev <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · runta-dev · `TS` · call site [`packages/jev-core/src/typesafe.ts`](https://github.com/runta-dev/jot/blob/HEAD/packages/jev-core/src/typesafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jpp](https://github.com/Towow-ai/jpp)** — J++: an experimental language with standalone source and a Rust runtime. Compose questions and methods. 独立源码，组合问题与方法。 <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · towow-ai · `Rs` · call site [`src/foundation/clients/eye_client.py`](https://github.com/Towow-ai/jpp/blob/HEAD/src/foundation/clients/eye_client.py), read 2026-09-24</sub>

- **[laya-jev-lab](https://github.com/yibie/laya-jev-lab)** — Independent measurements of typed-decision models: Jev (TypeSafe API) vs Laya (open weights), and a local-first cascade that matches Jev's accuracy at 1.8x the speed <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · yibie · `Py` · call site [`cascade/run2-jev.mjs`](https://github.com/yibie/laya-jev-lab/blob/HEAD/cascade/run2-jev.mjs), read 2026-09-22 · ⚠ `one commit`</sub>

- **[laya-vs-jev-arena](https://github.com/PromptEngineer48/laya-vs-jev-arena)** — Laya (open source, local) vs TypeSafe Jev (API): two AI models race in Snake and fight in a Mortal-Kombat-style arena. Every move is a real model decision. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · promptengineer48 · `JS` · call site [`server.py`](https://github.com/PromptEngineer48/laya-vs-jev-arena/blob/HEAD/server.py), read 2026-09-22</sub>

- **[llm-typesafe](https://github.com/simonw/llm-typesafe)** — LLM plugin for accessing Jev and other TypeSafe AI models <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · simonw · `Py` · call site [`llm_typesafe.py`](https://github.com/simonw/llm-typesafe/blob/HEAD/llm_typesafe.py), read 2026-09-24</sub>

- **[loki](https://github.com/wundercorp/loki)** — The agent that evolves with you 𖤍 <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · wundercorp · `Py` · call site [`agent/typesafe_client.py`](https://github.com/wundercorp/loki/blob/HEAD/agent/typesafe_client.py), read 2026-09-22</sub>

- **[open-spark-jev](https://github.com/abhishek085/open-spark-jev)** — Open-source, local decision models inspired by TypeSafe’s Jev and System One - built on Qwen3 for NVIDIA DGX Spark. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · abhishek085 · `Py` · call site [`open_spark_jev/eval/speed_vs_generation.py`](https://github.com/abhishek085/open-spark-jev/blob/HEAD/open_spark_jev/eval/speed_vs_generation.py), read 2026-09-22</sub>

- **[openthai-systemone](https://github.com/iapp-technology/openthai-systemone)** — OpenThai-SystemOne: open Thai + English System One decision model (0.8B, 256-way slot head, Apache-2.0) <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · iapp-technology · `Py` · call site [`openthai_systemone/server.py`](https://github.com/iapp-technology/openthai-systemone/blob/HEAD/openthai_systemone/server.py), read 2026-09-22</sub>

- **[pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)** — TypeSafe Jev as the pi coding agent's quiet decision layer <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · hyunjunjeon · `TS` · call site [`bench/src/jev_bench/providers/jev.py`](https://github.com/HyunjunJeon/pi-quiet-ask/blob/HEAD/bench/src/jev_bench/providers/jev.py), read 2026-09-22</sub>

- **[st-jeved](https://github.com/mossyfield/ST-jeved)** — SillyTavern extension that measures each reply and instructs the narrator only when a rule matches. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · mossyfield · `JS` · call site [`src/classifier.js`](https://github.com/mossyfield/ST-jeved/blob/HEAD/src/classifier.js), read 2026-09-22</sub>

- **[switchboard](https://github.com/ruban-24/switchboard)** — An open-source, model-agnostic decision router for Claude Code and Codex. <sub>(earlier upstream description)</sub>
  <sub>`Plugin` · ★10+ · ruban-24 · `TS` · call site [`src/jev.ts`](https://github.com/ruban-24/switchboard/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[trade-jev](https://github.com/justinhe16/trade-jev)** — Backtest Jev (TypeSafe) as a BUY/SELL/HOLD trader on NQ L10 order-book data <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · justinhe16 · `Py` · call site [`src/trade_jev/policies.py`](https://github.com/justinhe16/trade-jev/blob/HEAD/src/trade_jev/policies.py), read 2026-09-22</sub>

- **[typesafe-chess](https://github.com/TholeG/typesafe-chess)** — Chess where both players are TypeSafe's Jev model: every move is a typed Choice decision <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · tholeg · `JS` · call site [`jev-player.js`](https://github.com/TholeG/typesafe-chess/blob/HEAD/jev-player.js), read 2026-09-22</sub>

- **[typesafe-playground](https://github.com/kavehmz/typesafe-playground)** — Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · kavehmz · `JS` · call site [`demo01/server.mjs`](https://github.com/kavehmz/typesafe-playground/blob/HEAD/demo01/server.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground)** — Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts, A/B comparisons and a mobile-friendly UI. <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · typesafeai · `TS` · call site [`lib/callJev.ts`](https://github.com/TypeSafeAI/typesafe-playground/blob/HEAD/lib/callJev.ts), read 2026-09-24</sub>

- **[typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router)** — TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn. <sub>(upstream description)</sub>
  <sub>`Plugin` · ★10+ · decrux9812 · `Py` · call site [`typesafe_router/client.py`](https://github.com/DECRUX9812/typesafe-skill-router/blob/HEAD/typesafe_router/client.py), read 2026-09-22</sub>

- **[xtags](https://github.com/manifoldor/xtags)** — 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型。 <sub>(upstream description)</sub>
  <sub>`Project` · ★10+ · manifoldor · `JS` · call site [`extension/service.js`](https://github.com/manifoldor/xtags/blob/HEAD/extension/service.js), read 2026-09-22</sub>

- **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)** — A personal Rust AI gateway with a TypeSafe provider, usage extraction and alias resolution tested against real response bodies.
  <sub>`Project` · dvjn · `Rs` · call site [`src/providers.rs`](https://github.com/dvjn/aegis/blob/HEAD/src/providers.rs) · ⚠ `code untested` `no licence`</sub>

- **[agent-jev-tetris](https://github.com/Yasserbhb/Agent-JEV-Tetris)** — using the new model JEV to play the game tetris <sub>(upstream description)</sub>
  <sub>`Project` · yasserbhb · `TS` · call site [`server.mjs`](https://github.com/Yasserbhb/Agent-JEV-Tetris/blob/HEAD/server.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[ai-elo-ranker](https://github.com/opaielsheikh/ai-elo-ranker)** — High-speed recursive AI Elo tournament engine powered by Jev and Swiss matchmaking <sub>(upstream description)</sub>
  <sub>`Project` · opaielsheikh · `Py` · call site [`elo_ranker/judge.py`](https://github.com/opaielsheikh/ai-elo-ranker/blob/HEAD/elo_ranker/judge.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[ailerix](https://github.com/tylerjharden/ailerix)** — Type-safe model router. Jev (System One) banks each request to a typed catalog route. <sub>(upstream description)</sub>
  <sub>`Project` · tylerjharden · `TS` · call site [`src/app/docs/page.tsx`](https://github.com/tylerjharden/ailerix/blob/HEAD/src/app/docs/page.tsx), read 2026-09-22 · ⚠ `no licence`</sub>

- **[alphaoptimizer](https://github.com/alpha-tales/alphaoptimizer)** — Jev-powered output optimization for Codex, built to keep large tool results concise and usable. <sub>(upstream description)</sub>
  <sub>`Plugin` · alpha-tales · `TS` · call site [`dist/src/providers/jev.js`](https://github.com/alpha-tales/alphaoptimizer/blob/HEAD/dist/src/providers/jev.js), read 2026-09-22</sub>

- **[askjev](https://github.com/pZacca/askjev)** — Unofficial MCP server for Jev (Typesafe AI) <sub>(upstream description)</sub>
  <sub>`Plugin` · pzacca · `TS` · call site [`src/jev.ts`](https://github.com/pZacca/askjev/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[AskJev-MCP](https://github.com/cbruyndoncx/AskJev-MCP)** — MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence <sub>(upstream description)</sub>
  <sub>`Plugin` · cbruyndoncx · `JS` · call site [`src/index.ts`](https://github.com/cbruyndoncx/AskJev-MCP/blob/HEAD/src/index.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[auto-mode-for-paseo](https://github.com/obetomuniz/auto-mode-for-paseo)** — A Paseo provider that uses TypeSafe Jev to route each Codex turn.
  <sub>`Plugin` · obetomuniz · `TS` · call site [`server/jev.ts`](https://github.com/obetomuniz/auto-mode-for-paseo/blob/HEAD/server/jev.ts), read 2026-09-22</sub>

- **[awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases)** — Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI. <sub>(upstream description)</sub>
  <sub>`Project` · seeapi · `Py` · call site [`recipes/model-routing/run.py`](https://github.com/SeeAPI/awesome-jev-use-cases/blob/HEAD/recipes/model-routing/run.py), read 2026-09-24</sub>

- **[barrunto](https://github.com/elpumberto/barrunto)** — A Chrome extension that brings TypeSafe's Jev to X.com to analyze posts as you browse <sub>(upstream description)</sub>
  <sub>`Plugin` · elpumberto · `TS` · call site [`src/jev/real.ts`](https://github.com/elpumberto/barrunto/blob/HEAD/src/jev/real.ts), read 2026-09-22</sub>

- **[beatjev](https://github.com/lambertsj/beatjev)** — try to beat jev <sub>(upstream description)</sub>
  <sub>`Project` · lambertsj · `JS` · call site [`src/worker.js`](https://github.com/lambertsj/beatjev/blob/HEAD/src/worker.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[bes-kelime-jev](https://github.com/mahmut-gundogdu/bes-kelime-jev)** — Ne yazarsanız yazın, beş kelimeden biriyle cevap veren sohbet botu. Kelimeyi TypeSafe AI'ın Jev evaluation modeli seçer. <sub>(upstream description)</sub>
  <sub>`Project` · mahmut-gundogdu · `TS` · call site [`src/jev.ts`](https://github.com/mahmut-gundogdu/bes-kelime-jev/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[btc-jev-signal](https://github.com/WebGrga/btc-jev-signal)** — Experimental multi-horizon BTC signal generator using TypeSafe Jev probabilities and Binance market data. <sub>(earlier upstream description)</sub>
  <sub>`Project` · webgrga · `TS` · call site [`src/experiment-jev.ts`](https://github.com/WebGrga/btc-jev-signal/blob/HEAD/src/experiment-jev.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[cairn-jev-lab](https://github.com/Cairn-ink/cairn-jev-lab)** — Test what your AI should remember. An experimental, source-aware memory admission evaluator powered by Jev, with editable cases and inspectable results. <sub>(upstream description)</sub>
  <sub>`Project` · cairn-ink · `JS` · call site [`src/jev.mjs`](https://github.com/Cairn-ink/cairn-jev-lab/blob/HEAD/src/jev.mjs), read 2026-09-22</sub>

- **[cartshield](https://github.com/ndolinschi/cartshield)** — CartShield — SMB checkout fraud disposition via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/cartshield/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[codex-jev-preflight](https://github.com/wellkilo/codex-jev-preflight)** — Fail-open Codex UserPromptSubmit hook that injects TypeSafe Jev pre-task routing metadata. <sub>(upstream description)</sub>
  <sub>`Plugin` · wellkilo · `Py` · call site [`configure_jev.py`](https://github.com/wellkilo/codex-jev-preflight/blob/HEAD/configure_jev.py), read 2026-09-22</sub>

- **[commentcop](https://github.com/ntedvs/commentcop)** — Put your code comments on trial. Powered by Jev. <sub>(upstream description)</sub>
  <sub>`Project` · ntedvs · `TS` · call site [`src/judge.ts`](https://github.com/ntedvs/commentcop/blob/HEAD/src/judge.ts), read 2026-09-22</sub>

- **[cyber-breach-jev](https://github.com/rchovatiya88/cyber-breach-jev)** — Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model <sub>(upstream description)</sub>
  <sub>`Project` · rchovatiya88 · `JS` · call site [`backend/jev_client.py`](https://github.com/rchovatiya88/cyber-breach-jev/blob/HEAD/backend/jev_client.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[dbt_jev](https://github.com/smithclay/dbt_jev)** — use jev in dbt <sub>(upstream description)</sub>
  <sub>`Plugin` · smithclay · `Py` · call site [`src/dbt_jev/runtime.py`](https://github.com/smithclay/dbt_jev/blob/HEAD/src/dbt_jev/runtime.py), read 2026-09-24</sub>

- **[decisions-judge-mcp](https://github.com/clouatre-labs/decisions-judge-mcp)** — Typed decisions for AI agents as an MCP tool: yes/no probability (noul), choice, and score in one fast request. Backed by the TypeSafe System One model. <sub>(upstream description)</sub>
  <sub>`Plugin` · clouatre-labs · `JS` · call site [`providers/typesafe-api.mjs`](https://github.com/clouatre-labs/decisions-judge-mcp/blob/HEAD/providers/typesafe-api.mjs), read 2026-09-24</sub>

- **[dgp](https://github.com/numerous-com/dgp)** — Decision Graph Protocol (DGP) by Numerous ApS: open-source contracts for decision-based AI agents, TypeSafe Jev orchestration, guarded actions, and assessment batching. <sub>(upstream description)</sub>
  <sub>`Project` · numerous-com · `Py` · call site [`dgp_demo/providers.py`](https://github.com/numerous-com/dgp/blob/HEAD/dgp_demo/providers.py), read 2026-09-24</sub>

- **[emoji-jev](https://github.com/colinmcdermott/emoji-jev)** — Emoji autocomplete at the speed of typing. TypeSafe AI Jev on a Whop-hosted TanStack Start app. <sub>(upstream description)</sub>
  <sub>`Project` · colinmcdermott · `TS` · call site [`src/jev.ts`](https://github.com/colinmcdermott/emoji-jev/blob/HEAD/src/jev.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[everything-about-jev](https://github.com/qingshungLI/everything-about-jev)** — tell you everything about jev,TypeSafe AI's System One model for typed decisions. <sub>(upstream description)</sub>
  <sub>`Project` · qingshungli · `Py` · call site [`demos/python/jev_demo.py`](https://github.com/qingshungLI/everything-about-jev/blob/HEAD/demos/python/jev_demo.py), read 2026-09-22</sub>

- **[extremely-specific-council](https://github.com/cbetz/extremely-specific-council)** — Twelve members. Zero qualifications. A playful TypeSafe AI council with animated votes, inspectable decisions, and shareable verdicts. <sub>(upstream description)</sub>
  <sub>`Project` · cbetz · `TS` · call site [`lib/engine.ts`](https://github.com/cbetz/extremely-specific-council/blob/HEAD/lib/engine.ts), read 2026-09-22</sub>

- **[financialpredictionjev](https://github.com/thodoh1/FinancialPredictionJev)** — Using Jev to test how well it predicts financial markets(just like most llms as of september 2026, it doesnt do that good) <sub>(upstream description)</sub>
  <sub>`Project` · thodoh1 · `Py` · call site [`untitled15.py`](https://github.com/thodoh1/FinancialPredictionJev/blob/HEAD/untitled15.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[frost](https://github.com/marcus/frost)** — A flexible and configurable CLI model router using TypeSafe Jev. <sub>(upstream description)</sub>
  <sub>`Project` · marcus · `Go` · call site [`internal/analyzer/typesafe/typesafe.go`](https://github.com/marcus/frost/blob/HEAD/internal/analyzer/typesafe/typesafe.go), read 2026-09-22</sub>

- **[functions](https://github.com/TrainLCD/Functions)** — 👷 Cloudflare Workers for the TrainLCD mobile app. <sub>(upstream description)</sub>
  <sub>`Project` · trainlcd · `TS` · call site [`src/cli/typesafe-triage-spike.ts`](https://github.com/TrainLCD/Functions/blob/HEAD/src/cli/typesafe-triage-spike.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[git-jev-stage](https://github.com/ibrahemid/git-jev-stage)** — Select Git changes for staging with a plain-language description. <sub>(upstream description)</sub>
  <sub>`Project` · ibrahemid · `TS` · call site [`src/core/jevClient.ts`](https://github.com/ibrahemid/git-jev-stage/blob/HEAD/src/core/jevClient.ts), read 2026-09-22</sub>

- **[got-jev](https://github.com/phureewat29/jev-got)** — Jev (TypeSafe AI) PoC through Game of Thrones <sub>(upstream description)</sub>
  <sub>`Project` · phureewat29 · `TS` · call site [`src/core/providers/TypeSafe.ts`](https://github.com/phureewat29/jev-got/blob/HEAD/src/core/providers/TypeSafe.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[ha-conversation-jev](https://github.com/luxus/ha-conversation-jev)** — Home Assistant custom component: Conversation agent with Jev fast-path + Grok fallback <sub>(upstream description)</sub>
  <sub>`Project` · luxus · `Py` · call site [`custom_components/jev_assist/jev_client.py`](https://github.com/luxus/ha-conversation-jev/blob/HEAD/custom_components/jev_assist/jev_client.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[harden-jev-decides](https://github.com/tylerjharden/harden-jev-decides)** — JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board. <sub>(upstream description)</sub>
  <sub>`Project` · tylerjharden · `TS` · call site [`src/lib/jev/run.ts`](https://github.com/tylerjharden/harden-jev-decides/blob/HEAD/src/lib/jev/run.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[hermes-jev-curator](https://github.com/anpicasso/hermes-jev-curator)** — Typed Jev relation governance and safe archive plans for Hermes Curator <sub>(upstream description)</sub>
  <sub>`Project` · anpicasso · `Py` · call site [`plugin/transport.py`](https://github.com/anpicasso/hermes-jev-curator/blob/HEAD/plugin/transport.py), read 2026-09-24</sub>

- **[hiresignal](https://github.com/ndolinschi/hiresignal)** — HireSignal — resume first-pass fit+interview via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/hiresignal/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jcm-router](https://github.com/adarshmishra07/jcm-router)** — Local proxy that picks the Claude model and effort per message using TypeSafe Jev. Routes subagents, leaves your cached main chat alone. <sub>(upstream description)</sub>
  <sub>`Project` · adarshmishra07 · `TS` · call site [`src/jev.ts`](https://github.com/adarshmishra07/jcm-router/blob/HEAD/src/jev.ts), read 2026-09-22</sub>

- **[jeff-cli](https://github.com/saembit/jeff-cli)** — jeff, a Go CLI for Jev: from a shell script, give it state and a question with fixed answers and get calibrated probabilities back, with a rank command and meaningful exit codes.
  <sub>`Project` · saembit · `Go` · call site [`pkg/jev/client.go`](https://github.com/saembit/jeff-cli/blob/HEAD/pkg/jev/client.go), read 2026-09-24</sub>

- **[jev-2048](https://github.com/ARCJ137442/jev-2048)** — An instrumented 2048 web lab where every move is a Jev (TypeSafe AI System One) Choice, with no heuristic fallback \| 用 Jev 决策模型驱动每一步的 2048 网页实验台，概率、置信度、延迟与成本全部摊开可见，且刻意不做启发式兜底 <sub>(upstream description)</sub>
  <sub>`Project` · arcj137442 · `TS` · call site [`src/client/api.ts`](https://github.com/ARCJ137442/jev-2048/blob/HEAD/src/client/api.ts), read 2026-09-22</sub>

- **[jev-acp](https://github.com/formulahendry/jev-acp)** — Use Jev typed decisions from any ACP (Agent Client Protocol) client or IDE <sub>(upstream description)</sub>
  <sub>`Project` · formulahendry · `TS` · call site [`src/engine.ts`](https://github.com/formulahendry/jev-acp/blob/HEAD/src/engine.ts), read 2026-09-22</sub>

- **[jev-anotacao-sentencas](https://github.com/lab-dados/jev-anotacao-sentencas)** — Jev (TypeSafe) vs. Gemini 3.8 Flash vs. GPT-5.6 Luna na anotação estruturada de sentenças do TJSP: qualidade, tempo e custo <sub>(upstream description)</sub>
  <sub>`Project` · lab-dados · `Py` · call site [`src/jevtest/clientes.py`](https://github.com/lab-dados/jev-anotacao-sentencas/blob/HEAD/src/jevtest/clientes.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jev-arena-nanojev](https://github.com/liao96312/jev-arena-nanojev)** — 完全本地的 NanoJev 网格决策游戏实验场，支持中文 Pygame、多关卡与 GTX 1660S 训练 <sub>(upstream description)</sub>
  <sub>`Project` · liao96312 · `Py` · call site [`nanojev_adapter/typesafe_client.py`](https://github.com/liao96312/jev-arena-nanojev/blob/HEAD/nanojev_adapter/typesafe_client.py), read 2026-09-22</sub>

- **[jev-bot](https://github.com/nssmd/jev-bot)** — Self-hosted Jev decision workbench and Feishu bot: automatic choices, probabilities, and experimental word/character writing. <sub>(upstream description)</sub>
  <sub>`Project` · nssmd · `JS` · call site [`gateway.mjs`](https://github.com/nssmd/jev-bot/blob/HEAD/gateway.mjs), read 2026-09-22 · ⚠ `one commit`</sub>

- **[jev-broadcast-lab](https://github.com/4anti/jev-broadcast-lab)** — Testing Lab for Jev AI <sub>(upstream description)</sub>
  <sub>`Project` · 4anti · `JS` · call site [`web/shared/jev-client.js`](https://github.com/4anti/jev-broadcast-lab/blob/HEAD/web/shared/jev-client.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-calculator](https://github.com/pc418/jev-calculator)** — A probabilistic AI calculator powered by Jev.
  <sub>`Project` · pc418 · `TS` · call site [`shared/protocol.ts`](https://github.com/pc418/jev-calculator/blob/HEAD/shared/protocol.ts), read 2026-09-24</sub>

- **[jev-chat](https://github.com/adhyaay-karnwal/jev-chat)** — A chatbot from typed Jev decisions: hierarchical speculative decoding over System One probabilities. <sub>(upstream description)</sub>
  <sub>`Project` · adhyaay-karnwal · `Py` · call site [`src/jevchat/client.py`](https://github.com/adhyaay-karnwal/jev-chat/blob/HEAD/src/jevchat/client.py), read 2026-09-22</sub>

- **[jev-ci-selector](https://github.com/guilhem/jev-ci-selector)** — CI task selection for GitHub Actions with Jev and a pure policy engine; current selection is applied by default, with an explicit shadow mode for observation.
  <sub>`Project` · guilhem · `TS` · call site [`src/jev.ts`](https://github.com/guilhem/jev-ci-selector/blob/HEAD/src/jev.ts), read 2026-09-24</sub>

- **[jev-cli](https://github.com/jtsang4/jev-cli)** — CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out <sub>(upstream description)</sub>
  <sub>`Project` · jtsang4 · `TS` · call site [`src/providers/jev.ts`](https://github.com/jtsang4/jev-cli/blob/HEAD/src/providers/jev.ts), read 2026-09-24</sub>

- **[jev-cloud-quiz](https://github.com/minorun365/jev-cloud-quiz)** — A demo in which Jev judges, with probabilities, which of the three big clouds a feature name belongs to.
  <sub>`Project` · minorun365 · `TS` · call site [`server/server.mjs`](https://github.com/minorun365/jev-cloud-quiz/blob/HEAD/server/server.mjs), read 2026-09-24</sub>

- **[jev-codex-router-skill](https://github.com/455-dIAO/jev-codex-router-skill)** — Portable Codex Skill for Jev model and reasoning-effort routing, with safe installation and Chinese usage guides <sub>(upstream description)</sub>
  <sub>`Plugin` · 455-diao · `Py` · call site [`jev-codex-router/scripts/route.py`](https://github.com/455-dIAO/jev-codex-router-skill/blob/HEAD/jev-codex-router/scripts/route.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-connector](https://github.com/juanlentino/jev-connector)** — WordPress connector for TypeSafe Jev: typed, confidence-scored answers your code can branch on. <sub>(upstream description)</sub>
  <sub>`Plugin` · juanlentino · `PHP` · call site [`includes/class-client.php`](https://github.com/juanlentino/jev-connector/blob/HEAD/includes/class-client.php), read 2026-09-24</sub>

- **[jev-cvss](https://github.com/Red5d/jev-cvss)** — Fast CVSS scoring from vulnerability descriptions using Typesafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · red5d · `Py` · call site [`cvss31_jev.py`](https://github.com/Red5d/jev-cvss/blob/HEAD/cvss31_jev.py), read 2026-09-22</sub>

- **[jev-demo](https://github.com/sawzhang/jev-demo)** — Jev (TypeSafe System One) 学习与实测：概念文档 + 5 个可运行 demo + 可复现压测。实测 jev-1.13.0：扇出几乎免费，40 问与 1 问等延迟。 <sub>(upstream description)</sub>
  <sub>`Project` · sawzhang · `TS` · call site [`demo/jev_lite.py`](https://github.com/sawzhang/jev-demo/blob/HEAD/demo/jev_lite.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-demo](https://github.com/PenglongHuang/jev-demo)** — A zero-dependency web bench for TypeSafe Jev with three presets — browser actions, intent recognition and agent context pruning: send state and typed questions, get calibrated structured answers.
  <sub>`Project` · penglonghuang · `JS` · call site [`public/js/app.js`](https://github.com/PenglongHuang/jev-demo/blob/HEAD/public/js/app.js), read 2026-09-24</sub>

- **[jev-evaluation](https://github.com/willkelly/jev-evaluation)** — An adversarial evaluation of TypeSafe's jev decision model: nine experiments and 28 predictions fixed before any data was collected. 123,805 requests, $12.69. <sub>(upstream description)</sub>
  <sub>`Project` · willkelly · `Py` · call site [`jeveval/config.py`](https://github.com/willkelly/jev-evaluation/blob/HEAD/jeveval/config.py), read 2026-09-22</sub>

- **[jev-eyes](https://github.com/LeddoEngano/jev-eyes)** — Give Jev eyes — honest, local image perception for TypeSafe's text-only System One model. OCR + spatial layout → Jev state. CLI, MCP server, agent skill. <sub>(upstream description)</sub>
  <sub>`Plugin` · leddoengano · `Py` · call site [`benchmarks/jev_accuracy.py`](https://github.com/LeddoEngano/jev-eyes/blob/HEAD/benchmarks/jev_accuracy.py), read 2026-09-22</sub>

- **[jev-freeform](https://github.com/kesku/jev-freeform)** — An observable raw-character chat experiment powered entirely by TypeSafe Jev Choice <sub>(upstream description)</sub>
  <sub>`Project` · kesku · `JS` · call site [`main.mjs`](https://github.com/kesku/jev-freeform/blob/HEAD/main.mjs), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-games](https://github.com/shantanugoel/jev-games)** — Visual Jev lab for multiple games and emulator platforms <sub>(upstream description)</sub>
  <sub>`Project` · shantanugoel · `Py` · call site [`src/jev_games/games/mario/policy.py`](https://github.com/shantanugoel/jev-games/blob/HEAD/src/jev_games/games/mario/policy.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-gomoku](https://github.com/XieChengYuan/jev-gomoku)** — 弈瞬：双 Jev 五子棋九宫格输入实验台，逐手查看模型决策，支持真实对局回放与实时对战。 <sub>(upstream description)</sub>
  <sub>`Project` · xiechengyuan · `JS` · call site [`server.mjs`](https://github.com/XieChengYuan/jev-gomoku/blob/HEAD/server.mjs), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jev-grand-prix](https://github.com/enoyola/jev-grand-prix)** — An F1 racing game where TypeSafe's Jev picks the racing line and the pedals, and learns each corner's limit between laps <sub>(upstream description)</sub>
  <sub>`Project` · enoyola · `JS` · call site [`server.py`](https://github.com/enoyola/jev-grand-prix/blob/HEAD/server.py), read 2026-09-22</sub>

- **[jev-grug](https://github.com/mkotlikov/jev-grug)** — Helping JEV speak <3 <sub>(upstream description)</sub>
  <sub>`Project` · mkotlikov · `TS` · call site [`lib/jev.ts`](https://github.com/mkotlikov/jev-grug/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[jev-mcp](https://github.com/arunav25/jev-mcp)** — Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy. <sub>(upstream description)</sub>
  <sub>`Plugin` · arunav25 · `JS` · call site [`eval/adapters/jev.js`](https://github.com/arunav25/jev-mcp/blob/HEAD/eval/adapters/jev.js), read 2026-09-24</sub>

- **[jev-mcp](https://github.com/BYK/jev-mcp)** — An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text. <sub>(upstream description)</sub>
  <sub>`Plugin` · byk · `TS` · call site [`src/typesafe.ts`](https://github.com/BYK/jev-mcp/blob/HEAD/src/typesafe.ts), read 2026-09-24</sub>

- **[jev-mcp](https://github.com/freepik-company/jev-mcp)** — MCP server for typed decisions with Jev / System One via OpenRouter or TypeSafe <sub>(upstream description)</sub>
  <sub>`Plugin` · freepik-company · `Go` · call site [`internal/config/config.go`](https://github.com/freepik-company/jev-mcp/blob/HEAD/internal/config/config.go), read 2026-09-24</sub>

- **[jev-mcp](https://github.com/rajasekharponakala/jev-mcp)** — MCP server wrapping TypeSafe's Jev System One models — typed noul/choice/score judgments for AI agents <sub>(upstream description)</sub>
  <sub>`Plugin` · rajasekharponakala · `Py` · call site [`server.py`](https://github.com/rajasekharponakala/jev-mcp/blob/HEAD/server.py), read 2026-09-24</sub>

- **[jev-mcp](https://github.com/rashedInt32/jev-mcp)** — MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin. <sub>(upstream description)</sub>
  <sub>`Plugin` · rashedint32 · `TS` · call site [`src/index.ts`](https://github.com/rashedInt32/jev-mcp/blob/HEAD/src/index.ts), read 2026-09-24</sub>

- **[jev-mcp-spring](https://github.com/Ashfaqbs/jev-mcp-spring)** — Java/Spring Boot MCP server for TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ashfaqbs · `Java` · call site [`src/main/java/dev/ashfaqbs/jevmcp/tools/JevTools.java`](https://github.com/Ashfaqbs/jev-mcp-spring/blob/HEAD/src/main/java/dev/ashfaqbs/jevmcp/tools/JevTools.java), read 2026-09-24</sub>

- **[jev-measured](https://github.com/WallerChen/jev-measured)** — Measured cost, latency and raw output from the live Jev API (TypeSafe AI System One model) across 8 use cases — reproducible <sub>(earlier upstream description)</sub>
  <sub>`Project` · wallerchen · `Py` · call site [`bench/accuracy.py`](https://github.com/WallerChen/jev-measured/blob/HEAD/bench/accuracy.py), read 2026-09-22</sub>

- **[jev-minesweeper](https://github.com/comoc/jev-minesweeper)** — TypeSafe Jev (System One) にブラウザ上のマインスイーパーを解かせるデモ <sub>(upstream description)</sub>
  <sub>`Project` · comoc · `JS` · call site [`lib/typesafe.mjs`](https://github.com/comoc/jev-minesweeper/blob/HEAD/lib/typesafe.mjs), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jev-pick-and-place-study](https://github.com/tryaksh/jev-pick-and-place-study)** — A small reproducible MuJoCo pilot comparing Jev, Claude Haiku, and reactive rules for pick-and-place. <sub>(upstream description)</sub>
  <sub>`Project` · tryaksh · `Py` · call site [`compare.py`](https://github.com/tryaksh/jev-pick-and-place-study/blob/HEAD/compare.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jev-pii-checker](https://github.com/coo-quack/jev-pii-checker)** — CLI that finds PII in text with TypeSafe Jev: presence, sensitivity, and located spans <sub>(upstream description)</sub>
  <sub>`Project` · coo-quack · `TS` · call site [`src/judge.ts`](https://github.com/coo-quack/jev-pii-checker/blob/HEAD/src/judge.ts), read 2026-09-22</sub>

- **[jev-playground](https://github.com/wustep/jev-playground)** — Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI. <sub>(upstream description)</sub>
  <sub>`Project` · wustep · `TS` · call site [`src/planner/jev/systemOne.ts`](https://github.com/wustep/jev-playground/blob/HEAD/src/planner/jev/systemOne.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-playground](https://github.com/Little-Planet-Labs/jev-playground)** — A small Next.js app for experimenting with TypeSafe AI's Jev model (System One) <sub>(upstream description)</sub>
  <sub>`Project` · little-planet-labs · `TS` · call site [`src/app/api/evaluate/route.ts`](https://github.com/Little-Planet-Labs/jev-playground/blob/HEAD/src/app/api/evaluate/route.ts), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon)** — Playing Pokemon Red using TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · milanboers · `Py` · call site [`jev_plays_pokemon/agent.py`](https://github.com/milanboers/jev-plays-pokemon/blob/HEAD/jev_plays_pokemon/agent.py), read 2026-09-22</sub>

- **[jev-practice-speed](https://github.com/tubone24/jev-practice-speed)** — A WebGL demo where you play the card game Speed against a CPU whose brain is TypeSafe AI's Jev. The whole point of the app is to measure and show Jev's decision speed and decision accuracy in real time. <sub>(upstream description)</sub>
  <sub>`Project` · tubone24 · `JS` · call site [`src/core/jev-core.js`](https://github.com/tubone24/jev-practice-speed/blob/HEAD/src/core/jev-core.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-realtime-trading](https://github.com/rthomas24/jev-realtime-trading)** — Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app. <sub>(earlier upstream description)</sub>
  <sub>`Project` · rthomas24 · `TS` · call site [`src/core/realtime/jev.ts`](https://github.com/rthomas24/jev-realtime-trading/blob/HEAD/src/core/realtime/jev.ts), read 2026-09-22</sub>

- **[jev-resume-disqualifier](https://github.com/AiPersonacademy/jev-resume-disqualifier)** — Jev Resume Disqualifier: Sub-25ms automated resume knockout engine powered by TypeSafe Jev System One decision intelligence. Eliminates 80% of unqualified applicants with deterministic date math & EEOC-safe rejection notices. <sub>(upstream description)</sub>
  <sub>`Project` · aipersonacademy · `Py` · call site [`engine/decision_gateway.py`](https://github.com/AiPersonacademy/jev-resume-disqualifier/blob/HEAD/engine/decision_gateway.py), read 2026-09-22</sub>

- **[jev-search](https://github.com/larguesa/jev-search)** — Experimental semantic line search with TypeSafe Jev via OpenRouter. Python CLI with no runtime dependencies. <sub>(upstream description)</sub>
  <sub>`Project` · larguesa · `Py` · call site [`jev_search.py`](https://github.com/larguesa/jev-search/blob/HEAD/jev_search.py), read 2026-09-22</sub>

- **[jev-skills](https://github.com/laguagu/jev-skills)** — Practical agent skills and examples for building with Jev. API setup, routing, ranking, and evidence checks. <sub>(upstream description)</sub>
  <sub>`Plugin` · laguagu · `JS` · call site [`examples/decisions/run.mjs`](https://github.com/laguagu/jev-skills/blob/HEAD/examples/decisions/run.mjs), read 2026-09-24</sub>

- **[jev-skills](https://github.com/WanLanglin/jev-skills)** — Claude Code & Codex skills powered by Jev, TypeSafe's System One model. 256 calibrated judgements for $0.0005 in 0.72s — 360x cheaper than Claude Opus 5. Includes the first published Jev calibration curve, measured on 4,995 real agent decisions. <sub>(upstream description)</sub>
  <sub>`Plugin` · wanlanglin · `Py` · call site [`scripts/jev.py`](https://github.com/WanLanglin/jev-skills/blob/HEAD/scripts/jev.py), read 2026-09-24 · ⚠ `no licence`</sub>

- **[jev-snake](https://github.com/iammusham/jev-snake)** — An experimental Snake environment where the game engine owns deterministic rules and TypeSafe AI's Jev makes the movement decision from structured state on every tick. <sub>(upstream description)</sub>
  <sub>`Project` · iammusham · `Py` · call site [`snake_game/jev_agent.py`](https://github.com/iammusham/jev-snake/blob/HEAD/snake_game/jev_agent.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[jev-system-one](https://github.com/haseeb-heaven/jev-system-one)** — A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports <sub>(upstream description)</sub>
  <sub>`Project` · haseeb-heaven · `Py` · call site [`src/jev_system_one/jev.py`](https://github.com/haseeb-heaven/jev-system-one/blob/HEAD/src/jev_system_one/jev.py), read 2026-09-22</sub>

- **[jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner)** — Chrome dino game played by Typesafe AI Jev model <sub>(upstream description)</sub>
  <sub>`Project` · joshlarsen · `JS` · call site [`server/decision-service.mjs`](https://github.com/joshlarsen/jev-t-rex-runner/blob/HEAD/server/decision-service.mjs), read 2026-09-22</sub>

- **[jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales)** — Winner-stays-on animal tournament refereed by Jev (TypeSafe System One): a local game to feel how fast typed decisions are. UI in Spanish. <sub>(upstream description)</sub>
  <sub>`Project` · hectorlcastro09 · `TS` · call site [`motor.py`](https://github.com/hectorlcastro09/jev-torneo-animales/blob/HEAD/motor.py), read 2026-09-22</sub>

- **[jev-wingman](https://github.com/1104480426-hash/jev-wingman)** — 基于 Jev 的聊天决策辅助，不挑 App（QQ / 微信 / 飞书皆可）· An on-device chat co-pilot that returns typed verdicts instead of prose, built on Jev
  <sub>`Project` · 1104480426-hash · `Java` · call site [`app/src/ai/jev/assist/Prefs.java`](https://github.com/1104480426-hash/jev-wingman/blob/HEAD/app/src/ai/jev/assist/Prefs.java), read 2026-09-22</sub>

- **[jev-x-kit](https://github.com/Kadihx/jev-x-kit)** — Offline $0 decision layer for coding agents: Choice/Score/Noul primitives, BELKI confidence gatekeeper, ultra-planning, red-teaming, research and RLVR self-improvement -- as an MCP server + CLI + Claude Code skill. <sub>(upstream description)</sub>
  <sub>`Project` · kadihx · `TS` · call site [`src/core/providers/typesafe-native.ts`](https://github.com/Kadihx/jev-x-kit/blob/HEAD/src/core/providers/typesafe-native.ts), read 2026-09-24</sub>

- **[jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver)** — A Chrome extension that covers distracting YouTube videos with Jev. Show anyway whenever you want. <sub>(upstream description)</sub>
  <sub>`Plugin` · jaibhasin · `JS` · call site [`background/background.js`](https://github.com/jaibhasin/jev-yt-time-saver/blob/HEAD/background/background.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev2048](https://github.com/KyleKreuter/jev2048)** — Let Jev (TypeSafeAI) solve 2048 <sub>(upstream description)</sub>
  <sub>`Project` · kylekreuter · `TS` · call site [`backend/jev.py`](https://github.com/KyleKreuter/jev2048/blob/HEAD/backend/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev_jsonschema](https://github.com/Kiln-AI/jev_jsonschema)** — Run a JSON Schema through TypeSafe's Jev API, and get JSON back. <sub>(upstream description)</sub>
  <sub>`Project` · kiln-ai · `Py` · call site [`src/jev_jsonschema/client.py`](https://github.com/Kiln-AI/jev_jsonschema/blob/HEAD/src/jev_jsonschema/client.py), read 2026-09-22</sub>

- **[jev_project_context](https://github.com/poiuyjie/jev_project_context)** — Evidence-first long-term experiment memory skill for AI coding agents, with optional Jev decision-model layers <sub>(upstream description)</sub>
  <sub>`Plugin` · poiuyjie · `Py` · call site [`scripts/jev_client.py`](https://github.com/poiuyjie/jev_project_context/blob/HEAD/scripts/jev_client.py), read 2026-09-22</sub>

- **[jevals](https://github.com/dayhaysoos/jevals)** — Local evaluation workbench for TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Project` · dayhaysoos · `TS` · call site [`src/server.ts`](https://github.com/dayhaysoos/jevals/blob/HEAD/src/server.ts), read 2026-09-24</sub>

- **[jevcode](https://github.com/miounet11/jevcode)** — JevCode: technical solutions and best practices for Jev (TypeSafe System One), with a companion website.
  <sub>`Project` · miounet11 · `TS` · call site [`scripts/build-jev-cards.mjs`](https://github.com/miounet11/jevcode/blob/HEAD/scripts/build-jev-cards.mjs), read 2026-09-24 · ⚠ `no licence`</sub>

- **[Jevometry](https://github.com/Kunyanli230/Jevometry)** — an Information-Geometric Analysis Toolkit for any System-one (Jev, Jevlike) agent systems <sub>(upstream description)</sub>
  <sub>`Project` · kunyanli230 · `Py` · call site [`src/jevometry/adapters/typesafe.py`](https://github.com/Kunyanli230/Jevometry/blob/HEAD/src/jevometry/adapters/typesafe.py), read 2026-09-24</sub>

- **[jevopt](https://github.com/Ramneet-Singh/jevopt)** — Making intelligent compiler optimisation decisions with Jev <sub>(upstream description)</sub>
  <sub>`Project` · ramneet-singh · `Py` · call site [`src/jevopt/cli.py`](https://github.com/Ramneet-Singh/jevopt/blob/HEAD/src/jevopt/cli.py), read 2026-09-22</sub>

- **[jevscope](https://github.com/jeiel85/jevscope)** — Local-first visual decision debugger and regression testbench for TypeSafe AI Jev <sub>(upstream description)</sub>
  <sub>`Project` · jeiel85 · `TS` · call site [`packages/provider-typesafe/src/index.ts`](https://github.com/jeiel85/jevscope/blob/HEAD/packages/provider-typesafe/src/index.ts), read 2026-09-24</sub>

- **[jevseek](https://github.com/blingdivinity/jevseek)** — DeepSeek proposes the next token, TypeSafe's Jev chooses it: a decision model used as a sampler <sub>(upstream description)</sub>
  <sub>`Project` · blingdivinity · `Py` · call site [`src/jevseek/jev.py`](https://github.com/blingdivinity/jevseek/blob/HEAD/src/jevseek/jev.py), read 2026-09-24</sub>

- **[jevslop](https://github.com/TKY-27/JevSlop)** — Jevによるnote記事のAI Slop判定サイト <sub>(upstream description)</sub>
  <sub>`Project` · tky-27 · `TS` · call site [`lib/jev.ts`](https://github.com/TKY-27/JevSlop/blob/HEAD/lib/jev.ts), read 2026-09-22</sub>

- **[JevTape](https://github.com/Hugo-DDT/JevTape)** — A record-and-replay tool for Jev decisions: a CLI, a local proxy and JSON tapes, with replay fully offline.
  <sub>`Project` · hugo-ddt · `Java` · call site [`src/main/java/io/jevtape/cassette/RecordedRequest.java`](https://github.com/Hugo-DDT/JevTape/blob/HEAD/src/main/java/io/jevtape/cassette/RecordedRequest.java), read 2026-09-24</sub>

- **[jevtest](https://github.com/joshhu/jevtest)** — 情緒測謊器：嘴上說「好」，心裡真的好嗎？用 TypeSafe Jev（System One 模型）透過 OpenRouter 即時判斷，並與一般 LLM 對照 <sub>(upstream description)</sub>
  <sub>`Project` · joshhu · `TS` · call site [`main.py`](https://github.com/joshhu/jevtest/blob/HEAD/main.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jevtok](https://github.com/LabGuy94/jevtok)** — Exact token counting and request-cost prediction for TypeSafe's Jev (tiktoken-style) <sub>(upstream description)</sub>
  <sub>`Project` · labguy94 · `Py` · call site [`src/jevtok/cli.py`](https://github.com/LabGuy94/jevtok/blob/HEAD/src/jevtok/cli.py), read 2026-09-22</sub>

- **[labs](https://github.com/kiarina/labs)** — Small, independent projects for experiments, research, and investigations. <sub>(upstream description)</sub>
  <sub>`Project` · kiarina · `Py` · call site [`2026/09/17/typesafe-jev-evaluation/client.py`](https://github.com/kiarina/labs/blob/HEAD/2026/09/17/typesafe-jev-evaluation/client.py), read 2026-09-22</sub>

- **[magic-jev-ball](https://github.com/mikecann/magic-jev-ball)** — A Magic 8 Ball that asks Jev instead of picking at random. Convex + AI Gateway + three.js. <sub>(upstream description)</sub>
  <sub>`Project` · mikecann · `TS` · call site [`convex/jev.ts`](https://github.com/mikecann/magic-jev-ball/blob/HEAD/convex/jev.ts), read 2026-09-24</sub>

- **[mcpmatch](https://github.com/ndolinschi/mcpmatch)** — Match user goals to MCP catalog (two-stage) via TypeSafe Jev <sub>(upstream description)</sub>
  <sub>`Plugin` · ndolinschi · `TS` · call site [`src/lib/jev.ts`](https://github.com/ndolinschi/mcpmatch/blob/HEAD/src/lib/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[mcts-agent](https://github.com/lhemerly/mcts-agent)** — Discriminative Monte Carlo Tree Search using TypeSafe Jev System One Primitives and Gemini
  <sub>`Project` · lhemerly · `Py` · call site [`agent/system_one.py`](https://github.com/lhemerly/mcts-agent/blob/HEAD/agent/system_one.py), read 2026-09-22</sub>

- **[mimicry](https://github.com/jxucoder/mimicry)** — Rewrite AI drafts in your own voice with a bounded TypeSafe feedback loop. <sub>(upstream description)</sub>
  <sub>`Project` · jxucoder · `Py` · call site [`src/mimicry/engine.py`](https://github.com/jxucoder/mimicry/blob/HEAD/src/mimicry/engine.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[n8n-nodes-jev](https://github.com/vibe-with-me-tools/n8n-nodes-jev)** — Helper n8n community node for Jev by TypeSafe. Classify, route, and score text with questions you define, and get a probability for every answer so unsure items can go to review. <sub>(upstream description)</sub>
  <sub>`Plugin` · vibe-with-me-tools · `TS` · call site [`nodes/Jev/shared/descriptions.ts`](https://github.com/vibe-with-me-tools/n8n-nodes-jev/blob/HEAD/nodes/Jev/shared/descriptions.ts), read 2026-09-24</sub>

- **[n8n-nodes-typesafe](https://github.com/Biztactix/n8n-nodes-typesafe)** — Typesafe AI Node for N8N <sub>(upstream description)</sub>
  <sub>`Plugin` · biztactix · `TS` · call site [`nodes/TypeSafe/TypeSafe.node.ts`](https://github.com/Biztactix/n8n-nodes-typesafe/blob/HEAD/nodes/TypeSafe/TypeSafe.node.ts), read 2026-09-24</sub>

- **[n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev)** — n8n community node for TypeSafe Jev structured AI decisions <sub>(upstream description)</sub>
  <sub>`Project` · n3ndor · `TS` · call site [`nodes/TypeSafeJev/transport.ts`](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/HEAD/nodes/TypeSafeJev/transport.ts), read 2026-09-22</sub>

- **[new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe)** — TypeSafe AI System One (Jev) task plugin for QuantumNous/new-api — native /v1/systemone, synchronous evaluation, token billing <sub>(upstream description)</sub>
  <sub>`Plugin` · ffattiger · `JS` · call site [`plugins/tasks/typesafe/1.1.0/plugin.js`](https://github.com/FFatTiger/new-api-plugin-typesafe/blob/HEAD/plugins/tasks/typesafe/1.1.0/plugin.js), read 2026-09-22</sub>

- **[open-jev-bridge](https://github.com/louis-szeto/open-jev-bridge)** — MCP plugin to connect jev-like system one API (local hosted or typesafe jev) to codex and claude code for decision tasks like compaction, verification judgement, etc. <sub>(upstream description)</sub>
  <sub>`Plugin` · louis-szeto · `JS` · call site [`bin/open-jev-bridge.mjs`](https://github.com/louis-szeto/open-jev-bridge/blob/HEAD/bin/open-jev-bridge.mjs), read 2026-09-24</sub>

- **[openpoke-meets-jev](https://github.com/0xShin0221/openpoke-meets-jev)** — Open source implementation of Poke <sub>(upstream description)</sub>
  <sub>`Project` · 0xshin0221 · `Py` · call site [`server/jev/client.py`](https://github.com/0xShin0221/openpoke-meets-jev/blob/HEAD/server/jev/client.py), read 2026-09-22</sub>

- **[pi-agent-foreman](https://github.com/alexshpunt/pi-agent-foreman)** — Send Pi agents back to work when they stop before the job is done. <sub>(upstream description)</sub>
  <sub>`Project` · alexshpunt · `TS` · call site [`src/typesafe.ts`](https://github.com/alexshpunt/pi-agent-foreman/blob/HEAD/src/typesafe.ts), read 2026-09-22</sub>

- **[pi-typesafe](https://github.com/twilwa/pi-typesafe)** — Pi coding-agent extension built on the TypeSafe AI System One API (Jev) <sub>(upstream description)</sub>
  <sub>`Plugin` · twilwa · `TS` · call site [`scripts/jev-bench.ts`](https://github.com/twilwa/pi-typesafe/blob/HEAD/scripts/jev-bench.ts), read 2026-09-24</sub>

- **[pong-jev](https://github.com/safzanpirani/pong-jev)** — TypeSafe's Jev plays Atari Pong. One typed Choice question per frame, no coordinates sent to the model. <sub>(upstream description)</sub>
  <sub>`Project` · safzanpirani · `TS` · call site [`src/jev.ts`](https://github.com/safzanpirani/pong-jev/blob/HEAD/src/jev.ts), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[pydantic-jev-examples](https://github.com/adtyavrdhn/pydantic-jev-examples)** — Pydantic AI capabilities made stronger with Jev: small runnable demos, one file each <sub>(upstream description)</sub>
  <sub>`Project` · adtyavrdhn · `Py` · call site [`flappy_bird/jev_player.py`](https://github.com/adtyavrdhn/pydantic-jev-examples/blob/HEAD/flappy_bird/jev_player.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[r2r-jev](https://github.com/Thneoly/r2r-jev)** — Persistent governance for AI agents — turn Jev judgments into replayable relation state with R2R. <sub>(upstream description)</sub>
  <sub>`Project` · thneoly · `Rs` · call site [`src/jev.rs`](https://github.com/Thneoly/r2r-jev/blob/HEAD/src/jev.rs), read 2026-09-24</sub>

- **[research_desk](https://github.com/0xnairb/research_desk)** — TypeSafe Jev demonstration for new analyzation — experimenting with Jev for fast analysis of news and tickers <sub>(upstream description)</sub>
  <sub>`Project` · 0xnairb · `Py` · call site [`app/desk/pipeline.py`](https://github.com/0xnairb/research_desk/blob/HEAD/app/desk/pipeline.py), read 2026-09-22 · ⚠ `one commit` `no licence`</sub>

- **[risc-jev](https://github.com/i2cjak/RISC-jeV)** — I tortured Jev into being a RISC-V CPU. <sub>(upstream description)</sub>
  <sub>`Project` · i2cjak · `Py` · call site [`jev.py`](https://github.com/i2cjak/RISC-jeV/blob/HEAD/jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[river-run-typesafe](https://github.com/ashaazami/river-run-typesafe)** — River shooter game in Python, inspired by Atari's River Raid, played by a TypeSafe AI pilot <sub>(upstream description)</sub>
  <sub>`Project` · ashaazami · `Py` · call site [`typesafe_pilot/pilot.py`](https://github.com/ashaazami/river-run-typesafe/blob/HEAD/typesafe_pilot/pilot.py), read 2026-09-22</sub>

- **[rubikjev](https://github.com/0xtrou/rubikjev)** — Challenge the Jev's intelligence in Rubik Cube puzzles <sub>(upstream description)</sub>
  <sub>`Project` · 0xtrou · `TS` · call site [`src/server/jev-engine.ts`](https://github.com/0xtrou/rubikjev/blob/HEAD/src/server/jev-engine.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[rust-sysone](https://github.com/zcoder-run/rust-sysone)** — System One TypeSafe AI Rust Client (unofficial) <sub>(upstream description)</sub>
  <sub>`Project` · zcoder-run · `Rs` · call site [`src/client.rs`](https://github.com/zcoder-run/rust-sysone/blob/HEAD/src/client.rs), read 2026-09-22</sub>

- **[scam-shield](https://github.com/ShupingR/scam-shield)** — Scam text message filter powered by TypeSafe's Jev model <sub>(upstream description)</sub>
  <sub>`Project` · shupingr · `TS` · call site [`src/server/check.ts`](https://github.com/ShupingR/scam-shield/blob/HEAD/src/server/check.ts), read 2026-09-22 · ⚠ `no licence`</sub>

- **[search-function-test](https://github.com/Shifros/Search-Function-Test)** — A test project based on Jev AI, the goal is to build a search function for a blog/article website that has 100s of articles to search from, So the user can actually use the search as chat to question anything and find related answers/articles <sub>(upstream description)</sub>
  <sub>`Project` · shifros · `JS` · call site [`htr-hero/src/lib/typesafeSearch.js`](https://github.com/Shifros/Search-Function-Test/blob/HEAD/htr-hero/src/lib/typesafeSearch.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[second-thought](https://github.com/KNambiarDJsc/second-thought)** — Learning infrastructure for typed probabilistic decisions from System One models (Laya, and typed-decision providers you bring yourself). <sub>(upstream description)</sub>
  <sub>`Project` · knambiardjsc · `Py` · call site [`src/second_thought/adapters/jev.py`](https://github.com/KNambiarDJsc/second-thought/blob/HEAD/src/second_thought/adapters/jev.py), read 2026-09-24</sub>

- **[secondlayer](https://github.com/ryanwaits/secondlayer)** — Decoded Stacks data in your own database. Self-hosted. <sub>(earlier upstream description)</sub>
  <sub>`Project` · ryanwaits · `TS` · call site [`scripts/ops/jev-fault-triage.ts`](https://github.com/ryanwaits/secondlayer/blob/HEAD/scripts/ops/jev-fault-triage.ts), read 2026-09-22</sub>

- **[should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all)** — We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines. <sub>(upstream description)</sub>
  <sub>`Project` · hellogumbo · `JS` · call site [`functions/api/verdict.js`](https://github.com/hellogumbo/should-ai-kill-us-all/blob/HEAD/functions/api/verdict.js), read 2026-09-22</sub>

- **[skill-router](https://github.com/lomeshdutta/skill-router)** — Tell Claude Code which installed skill a session needs, using Jev (TypeSafe AI) for the decision and skills.sh for discovery. <sub>(upstream description)</sub>
  <sub>`Plugin` · lomeshdutta · `Py` · call site [`src/skill_router/router.py`](https://github.com/lomeshdutta/skill-router/blob/HEAD/src/skill_router/router.py), read 2026-09-22</sub>

- **[soupbase](https://github.com/spoonnotfound/soupbase)** — Jev x 海龟汤 <sub>(upstream description)</sub>
  <sub>`Project` · spoonnotfound · `TS` · call site [`src/server/providers.ts`](https://github.com/spoonnotfound/soupbase/blob/HEAD/src/server/providers.ts), read 2026-09-24</sub>

- **[sqlite3-jev](https://github.com/mattn/sqlite3-jev)** — SQLite extension that calls TypeSafe Jev (or tensai serve) from SQL <sub>(upstream description)</sub>
  <sub>`Plugin` · mattn · `C` · call site [`jev.c`](https://github.com/mattn/sqlite3-jev/blob/HEAD/jev.c), read 2026-09-24 · ⚠ `one commit`</sub>

- **[system-one-chess](https://github.com/dperezcabrera/ai-chess-lab)** — Chess against Jev, TypeSafe AI's System One model, through OpenRouter. Built with the pico framework. <sub>(upstream description)</sub>
  <sub>`Project` · dperezcabrera · `Py` · call site [`system_one_chess/jev.py`](https://github.com/dperezcabrera/ai-chess-lab/blob/HEAD/system_one_chess/jev.py), read 2026-09-22</sub>

- **[systemone-lite](https://github.com/fritzprix/systemone-lite)** — Toy local System One–style decision API (Jev-shaped). Not affiliated with TypeSafe. <sub>(upstream description)</sub>
  <sub>`Project` · fritzprix · `Py` · call site [`scripts/jevbench_eval.py`](https://github.com/fritzprix/systemone-lite/blob/HEAD/scripts/jevbench_eval.py), read 2026-09-22</sub>

- **[tempo-jev-demo](https://github.com/mychaelangelo/tempo-jev-demo)** — A natural-language task workspace comparing performance across AI models (TypeSafe's Jev, GPT-5.6 Luna, and Gemini 3.8 Flash) <sub>(upstream description)</sub>
  <sub>`Project` · mychaelangelo · `TS` · call site [`src/server/providers/typesafe.ts`](https://github.com/mychaelangelo/tempo-jev-demo/blob/HEAD/src/server/providers/typesafe.ts), read 2026-09-22</sub>

- **[typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground)** — A playground for experiments around Jev, TypeSafe's System One model. <sub>(upstream description)</sub>
  <sub>`Project` · markjaquith · `Rs` · call site [`src/typesafe.rs`](https://github.com/markjaquith/typesafe-ai-playground/blob/HEAD/src/typesafe.rs), read 2026-09-22</sub>

- **[typesafe-assist](https://github.com/JanOstrowka/typesafe-assist)** — Home Assistant Assist conversation agent powered by TypeSafe's Jev (System One) model <sub>(upstream description)</sub>
  <sub>`Project` · janostrowka · `Py` · call site [`custom_components/typesafe_conversation/api.py`](https://github.com/JanOstrowka/typesafe-assist/blob/HEAD/custom_components/typesafe_conversation/api.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[typesafe-comment](https://github.com/Hexdigest123/typesafe-comment)** — Small Python package that uses typesafe.ai to evaluate code comments on certain heuristics <sub>(upstream description)</sub>
  <sub>`Project` · hexdigest123 · `Py` · call site [`typesafe_comment/client.py`](https://github.com/Hexdigest123/typesafe-comment/blob/HEAD/typesafe_comment/client.py), read 2026-09-22 · ⚠ `archived`</sub>

- **[typesafe-jev-examples](https://github.com/rajivkuriakose/typesafe-jev-examples)** — Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter <sub>(upstream description)</sub>
  <sub>`Project` · rajivkuriakose · `Py` · call site [`src/jevx/client.py`](https://github.com/rajivkuriakose/typesafe-jev-examples/blob/HEAD/src/jevx/client.py), read 2026-09-22</sub>

- **[typesafe-jev-mcp](https://github.com/anasbekheit/typesafe-jev-mcp)** — MCP server exposing TypeSafe's Jev model as a typed evaluate tool. <sub>(upstream description)</sub>
  <sub>`Plugin` · anasbekheit · `Rs` · call site [`src/jev.rs`](https://github.com/anasbekheit/typesafe-jev-mcp/blob/HEAD/src/jev.rs), read 2026-09-22</sub>

- **[typesafe-jev-tools](https://github.com/wotai-dev/typesafe-jev-tools)** — A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5. <sub>(upstream description)</sub>
  <sub>`Plugin` · wotai-dev · `TS` · call site [`hooks/typesafe-check.sh`](https://github.com/wotai-dev/typesafe-jev-tools/blob/HEAD/hooks/typesafe-check.sh), read 2026-09-24</sub>

- **[typesafe-ui](https://github.com/TypeSafeAI/typesafe-ui)** — shadcn-style reusable components and blocks for using TypeSafe AI. <sub>(upstream description)</sub>
  <sub>`Project` · bunsdev · `TS` · call site [`apps/web/components/demos.tsx`](https://github.com/TypeSafeAI/typesafe-ui/blob/HEAD/apps/web/components/demos.tsx), read 2026-09-24 · ⚠ `no licence`</sub>

- **[typesafe_chess_eval](https://github.com/AliceRoselia/Typesafe_chess_eval)** — An evaluation of typesafe AI chess. As it turns out, the AI isn't doing really well even though chess is not a particularly open-ended game. Still, it's only a prototype and this probably wasn't optimzied for games. <sub>(upstream description)</sub>
  <sub>`Project` · aliceroselia · `Py` · call site [`Chess.py`](https://github.com/AliceRoselia/Typesafe_chess_eval/blob/HEAD/Chess.py), read 2026-09-22</sub>

- **[typesafeai-cli](https://github.com/maddygoround/typesafeai-cli)** — Give your AI agent a CLI companion who has access to TypeSafe AI's Jev. <sub>(upstream description)</sub>
  <sub>`Project` · maddygoround · `Py` · call site [`src/typesafe_cli/client.py`](https://github.com/maddygoround/typesafeai-cli/blob/HEAD/src/typesafe_cli/client.py), read 2026-09-24</sub>

- **[wellposed](https://github.com/suraj-phanindra/wellposed)** — Lint your jev requests before they come back confidently wrong.
  <sub>`Project` · suraj-phanindra · `JS` · call site [`skills/wellposed/scripts/semantic.mjs`](https://github.com/suraj-phanindra/wellposed/blob/HEAD/skills/wellposed/scripts/semantic.mjs), read 2026-09-24</sub>

- **[your-signal](https://github.com/MithrilMan/your-signal)** — Open-source BYOK Chrome extension for personal, reversible X timeline filters. <sub>(upstream description)</sub>
  <sub>`Plugin` · mithrilman · `JS` · call site [`eval/run.py`](https://github.com/MithrilMan/your-signal/blob/HEAD/eval/run.py), read 2026-09-22</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
