# ML feature extraction

<sub>[awesome-jev](../../README.md) · [中文](feature-extraction.zh-CN.md)</sub>

_Turn free text into numeric features for a classical downstream model._

Every catalogued example of this decision — 8 of them. The same rows, with caveats, are in [the index](../../README.md#ml-feature-extraction); [the site](https://kydlikebtc.github.io/awesome-jev/?p=feature-extraction&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#feature-extraction): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 1 · call site 7 · wire shape 0 · example only 0 · independent reports 0 · negative results 0 · no file cited 1. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

What TypeSafe AI publishes itself (rows marked `official`), filed under this pattern. Each is also listed below, with its summary.

- [Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) <sub>`Official docs` · `Py`</sub>

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

- **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐ — An autoresearch loop that proposes questions, turns free text into numeric features, and uses model error to improve a supervised gradient-boosting regressor.
  <sub>`Official docs` · `Py`</sub>

- **[nimble](https://github.com/bespokelabsai/nimble)** — Data, recipe and serving code for Bespoke-Nimble-9B, an open decision model inspired by Jev: a Qwen3.5-9B LoRA that answers choice and true-or-false questions about a text with probabilities. On 324 held-out examples it matched 90.1% of reference labels; scored alike, Jev 1.13.0 matched 93.2%. <sub>(written by a model)</sub>
  <sub>`Project` · ★1k+ · bespokelabsai · `Py` · call site [`nimble/evaluation/evaluate_public_jev.py`](https://github.com/bespokelabsai/nimble/blob/HEAD/nimble/evaluation/evaluate_public_jev.py), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — Builds calibrated decision functions from human feedback.
  <sub>`Project` · ★100+ · sutro-sh · `Py` · call site [`src/jev_align/jev.py`](https://github.com/sutro-sh/jev-align/blob/HEAD/src/jev_align/jev.py), read 2026-09-22</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy.
  <sub>`Project` · ★100+ · `TS` · `choice` · `score` · call site [`engine/jev-service.ts`](https://github.com/irfndi/prism-liquidity-agent/blob/HEAD/engine/jev-service.ts), read 2026-09-22</sub>

- **[JEV Sees](https://github.com/CharlesFeng0314/JEV_sees)** — Gives Jev vision: local Florence-2 and CLIP models find the objects in an image, video or RGB-D frame and keep their IDs across frames, then Jev answers a choice, noul or score about each relevant object (bus colour, pedestrian risk, animal motion). <sub>(written by a model)</sub>
  <sub>`Project` · charlesfeng0314 · `Py` · `choice` · `noul` · `score` · call site [`jev_sees/session.py`](https://github.com/CharlesFeng0314/JEV_sees/blob/HEAD/jev_sees/session.py), read by a model 2026-10-24</sub>

- **[jev-board-lab](https://github.com/WebGrga/jev-board-lab)** — Password-protected browser workbench that turns CSV rows into Jev judgments: you write at most 20 noul, choice or score questions and run them on at most 25 selected rows, each row sent as one state through a Cloudflare Worker that holds the key. The CSV stays in the browser. <sub>(written by a model)</sub>
  <sub>`Project` · webgrga · `JS` · call site [`worker/src/index.js`](https://github.com/WebGrga/jev-board-lab/blob/HEAD/worker/src/index.js), read 2026-09-22 · ⚠ `no licence`</sub>

- **[jev-calibrated-narrative-coding](https://github.com/pozapas/jev-calibrated-narrative-coding)** — Code, question schema and aggregated results of a paper that sent 5,018,080 Texas police crash narratives (2017–2025) to Jev as noul, choice and score questions, checked their calibration against coded fields and a human gold set, and turned it into how many flagged records people must review. <sub>(written by a model)</sub>
  <sub>`Project` · pozapas · `Py` · call site [`src/jev_runner.py`](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/HEAD/src/jev_runner.py), read 2026-09-24</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — Model router that starts each request on the cheapest tier and lifts it only when Jev's signals (multi-step reasoning, difficulty, stakes, safety) cross a YAML policy. On its author's 120 prompts it matched the flagship's quality at 40% less cost; the fast model alone did as well at 3% of the cost. <sub>(written by a model)</sub>
  <sub>`Project` · iamvatsalpatel · `TS` · call site [`bench/experiments/gate-experiment.ts`](https://github.com/iamvatsalpatel/tiershift/blob/HEAD/bench/experiments/gate-experiment.ts), read 2026-09-22</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
