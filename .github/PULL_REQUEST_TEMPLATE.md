## What this changes

<!-- One or two lines. A candidate from the `discovery` issue? Name the owner/name you claimed there. A row someone asked for in a new-entry issue? Write `Closes #<number>`, so the issue closes when the row lands. -->

## If you added or edited rows

<!-- Most pull requests only add a row, and these seven boxes are what one needs; the rest of the field rules are folded below, for the fields a row uses beyond these. Once CI has run, the lint run's summary holds a review card for each row you added or changed: fix what it marks ✗. It matches text; a maintainer still reads the call site. -->

- [ ] `python3 scripts/check.py --fix` passes: it sorts `catalog.json`, then runs every check CI runs
- [ ] Generated files (READMEs, `docs/by-pattern/`, `docs/measured*.md`, `docs/benchmarks*.md`, `docs/shape*.md`, `docs/assets/`, `examples/index.json`, generated numbers in docs) are either left out — a bot regenerates them on `main` after the merge — or exactly what `python3 scripts/check.py --fix` wrote, never edited by hand
- [ ] I opened every link I added and wrote the summaries from what was there; a row with code says in its summary (or `notes`) what it asks Jev to decide
- [ ] `question_types` reflects the call site I read, which `evidence` cites (or `evidence_none` says why it cannot: lint requires one when the repository is on GitHub), and I left `primitives_seen` to the weekly run (a script's text signal, never a substitute for reading the call)
- [ ] `summary_zh` is Chinese I wrote myself, or `zh_machine: true` is set because a model wrote or drafted it (kept even after my edits; a row claimed from `docs/zh-queue.md` then says in `notes` that a model translated it and who checked it)
- [ ] Caveats are flagged, and any flag needing an explanation has a `notes` line; `negative-result` only on a row that is not a benchmark, whose own author measured Jev and did not adopt it, with a `notes` line naming where they say so
- [ ] This is my own project (I wrote or maintain it): its row has a source `{"catalog": "author submission", "url": <this pull request, or the issue that proposed it>}` and `self-submitted` in `flags`. Leave unticked otherwise.

<details>
<summary>Every other field rule: tick the ones for fields your rows use</summary>

- [ ] Each `platforms` value is one `compat.json` lists in a surface's `catalog_platforms` or `taxonomy.json` lists in `platforms_without_surface` (lint checks), and says no more than the cited file shows (a project on Vercel's gateway is `vercel-ai-gateway`, whichever route it takes)
- [ ] `patterns_reviewed` is set only on rows whose `patterns` I read against `docs/patterns.md`, to the day I read them
- [ ] `evidence.kind` says what the cited file shows when it is not a call site: `wire-shape` for an `alternative` (lint requires it), `example-only` for an example
- [ ] A benchmark's `measurement` records only what its author's report states (no guessed `n`, dataset or direction; `direction` only where the author concludes in words), and `measurement.read_on` is set only if I read the report against every field
- [ ] An alternative's `wire` records only what the files in `wire.source` show, each copied value inside one of their `matched` strings (lint checks), and `read_on` is set on a source only if I read that file against every field
- [ ] Each `observed_thresholds` item is a constant the cited file compares a Jev answer with, its `source` copied exactly and also in `evidence.matched` (lint checks), `compares` naming Jev's answer rather than the project's variable, and `read_on` set only on items I read in the file myself
- [ ] `stars` / `repo_license` came from the GitHub API, not a badge, and I left `repo_created_at`, `repo_pushed_at` and `repo_commits` to the weekly refresh
- [ ] `sources` names where I found the row; I left the sibling-list citations (`{"catalog": "owner/name", …}` items) to the weekly refresh
- [ ] `summary_source` is `curated` if I wrote or rewrote the summary, `model-written` if a model wrote it and no person has rewritten it since, and left out if I pasted the repository's own GitHub description (the weekly refresh labels that)
- [ ] What a model read for me is recorded as a model's reading: `model_read_on` (on `evidence`, `measurement`, a `wire.source` file or a threshold) or `patterns_model_read_on`, never `read_on` or `patterns_reviewed`, which say a person read it (see CONTRIBUTING, *A model's reading*)
- [ ] A row started from a draft (`discover_candidates.py --drafts`, or the one posted on a new-entry issue): I read its call site myself, checked the `kind`, `patterns` and `languages` the script guessed, and deleted `_draft`. Leave unticked otherwise.

</details>

## If you added a pattern

- [ ] Schema enum, `patterns.json` (both languages, long and short blurb) and a `## key` section in `docs/patterns.md` and in `docs/patterns.zh-CN.md`, each ending with its `catalogued-<key>` markers, all updated
- [ ] There are at least two independent real examples of it

## If you edited picker.json

- [ ] Every step I changed cites, in `source_url`, the docs.typesafe.ai page and heading I read it on, and says no more than that page does (see CONTRIBUTING, *Editing the primitive picker*)

## If you touched any doc

- [ ] No catalogue count or range of thresholds typed by hand — reworded, or filled by `build_docs.py` (see CONTRIBUTING, *Numbers in prose*)

## If you added a runnable example

- [ ] The file states plainly whether it was run against the live API
- [ ] `examples/README.md` updated

## Anything you are unsure about

<!-- Say so here. An honest question costs nothing; a wrong row costs a reader's trust. -->
