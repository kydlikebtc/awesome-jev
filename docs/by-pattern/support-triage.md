# Support triage

<sub>[awesome-jev](../../README.md) · [中文](support-triage.zh-CN.md)</sub>

_Route support tickets and conversations by intent and urgency._

Every catalogued example of this decision — 9 of them. The same rows, with caveats, are in [the index](../../README.md#support-triage); [the site](https://kydlikebtc.github.io/awesome-jev/?p=support-triage&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#support-triage): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 1 · call site 4 · wire shape 0 · example only 0 · independent reports 1 · negative results 0 · no file cited 5. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Quickstart](https://docs.typesafe.ai/introduction/quickstart) <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

## Examples in this repository

Code under this repository's [`examples/`](../../examples/) filed under this pattern. Each is also listed below, with its summary; [the examples' README](../../examples/README.md) says how far they have been checked.

- [Example: three primitives in one request](../../examples/01-three-primitives/main.py) <sub>`Snippet` · `Py` · `choice` · `score` · `noul` · ⚠ `code untested`</sub>

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.
  <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★1k+ · `Py` · `choice` · `score` · `noul` · call site [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py), read 2026-09-22</sub>

- **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)** — A community Spring AI starter bringing typed decisions to Java, with a builder API over the three question types.
  <sub>`Integration` · ★10+ · `Java` · `choice` · `score` · `noul` · call site [`examples/src/main/java/org/springaicommunity/typesafe/demo/JevQuickstart.java`](https://github.com/spring-ai-community/spring-ai-typesafe/blob/HEAD/examples/src/main/java/org/springaicommunity/typesafe/demo/JevQuickstart.java), read 2026-09-22</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — A minimal first call asking a choice, a score and a noul together, annotated with the asymmetries that catch people out.
  <sub>`Snippet` · `Py` · `choice` · `score` · `noul` · call site [`examples/01-three-primitives/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/01-three-primitives/main.py), read 2026-09-22 · ⚠ `code untested`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice` · ⚠ `paywall`</sub>

- **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)** — Another gateway route, notable because its endpoint path and request envelope differ again from both the native API and Cloudflare's.
  <sub>`Integration` · `Py` · `noul` · `choice` · `score`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding and REST samples asking a noul, a choice and a score in one call, with the full response including per-answer confidence.
  <sub>`Integration` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[jev-triage](https://github.com/boldbug1/jev-triage)** — Go command-line tool that sorts messages by urgency: one Jev request per message asks a choice of kind (bug, billing, feature request, account, other), a 0–3 urgency score and a noul on whether the sender sounds frustrated. Below 0.8 category confidence a message goes to a review-by-hand list. <sub>(written by a model)</sub>
  <sub>`Project` · boldbug1 · `Go` · call site [`main.go`](https://github.com/boldbug1/jev-triage/blob/HEAD/main.go), read 2026-09-24</sub>

- **[Support-routing benchmark: 100 held-out cases](https://decisionmodelhub.com/benchmarks/support-routing)** — Compares Jev with Clef, Clef Flash, OpenAI's Decisions API and a GPT-6 Luna structured-output baseline on 100 held-out fictional support messages, each routed to one of five team labels; every case and recorded answer can be downloaded.
  <sub>`Benchmark` · DecisionModelHub · ⚠ `self-submitted`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
