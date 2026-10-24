# Recommendation

<sub>[awesome-jev](../../README.md) · [中文](recommendation.zh-CN.md)</sub>

_Choose what to surface next, fast enough for a live conversation._

Every catalogued example of this decision — 2 of them. The same rows, with caveats, are in [the index](../../README.md#recommendation); [the site](https://kydlikebtc.github.io/awesome-jev/?p=recommendation&lang=en) can filter them further by language, primitive and kind.

Design notes for this decision are in [docs/patterns.md](../patterns.md#recommendation): what it decides and which primitive shapes it, and, where one is written, when not to use a decision model for it.

Evidence recorded for this pattern's rows (reports counted, not a verdict; a row may count more than once): official documentation 0 · call site 2 · wire shape 0 · example only 0 · independent reports 0 · negative results 0 · no file cited 0. “Independent” = a benchmark not flagged vendor-reported, not reproduced by this repository. [Every pattern side by side](../shape.md#evidence-by-decision-pattern).

## Official material

The catalogue files nothing TypeSafe AI publishes under this pattern.

## Examples in this repository

This repository ships no example of this pattern; [`examples/`](../../examples/) has the ones it does.

## The full list

★ gives a repository's GitHub stars as a band — ★10+, ★100+, ★1k+, ★10k+ and ★100k+; rows with no repository or under 10 stars show no band. Rows run official first, then with code, then by band, then by title. A band is a popularity signal, not a quality verdict; the exact count, as last read from GitHub, is in [`catalog.json`](../../catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/?lang=en).

A *call site* link opens the one file a row cites (`evidence.path`) at `HEAD` of the repository's default branch; the date after it is the day a person last read that file (`evidence.read_on`) or, where it says *read by a model*, the day a model did (`evidence.model_read_on`): a reading, not a run of the code. A *cited file* link is the same for a file that shows the project speaking Jev's request shape rather than building on Jev, or only an example it ships (`evidence.kind`). Neither is pinned to a commit, so it opens the file as it is now, which may differ from what was read, and stops resolving once the file moves; the weekly claims check reports that.

- **[1 Million Emojis](https://github.com/cwdx/1-million-emojis)** — A shared 1,000 × 1,000 emoji canvas where Jev paints next to people: after each stroke one request asks a choice of emoji-and-placement options and a noul on whether the stroke looks unfinished, through Vercel AI Gateway with TypeSafe direct as fallback. <sub>(written by a model)</sub>
  <sub>`Project` · cwdx · `TS` · `choice` · `noul` · call site [`packages/jev/src/index.ts`](https://github.com/cwdx/1-million-emojis/blob/HEAD/packages/jev/src/index.ts), read by a model 2026-10-24 · ⚠ `self-submitted`</sub>

- **[Jevflix](https://github.com/ArielBubis/Jevflix)** — Jev picks, you watch. A hybrid movie recommender: fast semantic + keyword search narrows 4,800 films to a shortlist, then TypeSafe Jev reads your constraints and picks the one film that fits - with a confidence score that decides whether to answer instantly or ask a follow-up. <sub>(upstream description)</sub>
  <sub>`Project` · arielbubis · `Py` · call site [`movie_rec/jev_client.py`](https://github.com/ArielBubis/Jevflix/blob/HEAD/movie_rec/jev_client.py), read 2026-09-24</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file.</sub>
