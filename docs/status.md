# Ecosystem status

This page has two halves that age differently. The first is regenerated from
`catalog.json` by `scripts/build_docs.py` on every build, so it is current by
construction. The second is a dated snapshot, written at **2026-09-22** — a week
after the model entered early access on 2026-09-15 — and is meant to age; that
is the point of dating it. Its last section, the questions it left open, is a
table regenerated like the first half, each reading in it dated on its own.

## The catalogue, now

<!-- shape:start -->
|  |  |
| --- | --- |
| Entries | 1211 |
| Carrying code | 1183 |
| Official (TypeSafe AI's own) | 36 |
| Links with a dated 2xx response record | 1207 |
| Most recent successful link-check date (dates vary by row) | 2026-09-30 |
| Rows whose latest successful check is on that date | 1202 of 1211 |
| Rows citing a file where the project calls Jev (`evidence`; not a CI pass count) | 1077 |
| Rows citing a file that speaks Jev's request shape rather than building on Jev (`evidence.kind` `wire-shape`) | 56 |
| Rows citing only an example the project ships (`evidence.kind` `example-only`) | 0 |
| Rows with code citing no file and giving no reason (neither `evidence` nor `evidence_none`) | 0 |
| Rows naming the primitives a person read the code calling (`question_types`) | 105 |
| Machine text signal: rows whose cited file contains a primitive's request or answer shape (`primitives_seen`; not a reading, never counted as `question_types`) | 684 |
| Of those, rows with no `question_types`: the text signal is all that is recorded about their primitives | 632 |
| Machine signal: evidence under an examples directory, not yet judged ([review queue](review-queue.md#examples-dir)) | 22 |
| Machine signal: evidence resting on one model name or the API host ([review queue](review-queue.md#single-model-name)) | 76 |
| Machine signal: `tool-selection` suggested only by keyword-rule words dropped on 2026-09-27 ([review queue](review-queue.md#tool-selection-broad-words)) | 65 |
| Machine signal: rows with code, not TypeSafe AI's own, whose summary names nothing about Jev and that carry no `notes` ([review queue](review-queue.md#generic-summary)) | 101 |
| Benchmark rows indexing their own author's measurement (`measurement`: task, datasets, comparators, the author's direction; author-stated, not reproduced here; [side by side](benchmarks.md)) | 25 |
| Machine signal: of those, measurements no person has read against the author's report ([review queue](review-queue.md#measurement-unread)) | 25 |
| Rows recording thresholds their cited file compares a Jev answer with (`observed_thresholds`: each a constant written in that file; what one project chose, not a recommendation) | 32 |
| Machine signal: of those, rows with a threshold no person has read in the file ([review queue](review-queue.md#thresholds-unread)) | 32 |
| Negative results: rows whose own author measured Jev for the use and concluded against it (a benchmark's `measurement.direction` unfavourable, the `negative-result` flag on any other row; author-stated, not reproduced here; [listed below](#negative-results)) | 5 |
| Patterns covered | 18 of 18 |
| Rows whose `patterns` are exactly what the keyword rules suggest for their summary (agreement with the rules, not a review: any review of these rows was not recorded) | 759 of 1211 |
| Rows whose patterns a person recorded reading (`patterns_reviewed`) | 1 |
| Overview rows that are projects or plugins with code, listed apart as not yet indexed by pattern ([review queue](review-queue.md#unsorted-overview)) | 252 |
| Summaries that are the project's own GitHub description (`summary_source` `upstream-description`) | 882 of 1211 |
| Summaries taken from that description that no longer match it (`upstream-description-stale`) | 9 |
| Summaries marked as written for this catalogue (`curated`) | 3 |
| Chinese summaries hand-written | 195 of 1211 |
| Rows recording GitHub's creation date, last push and default-branch commit count for their repository (`repo_created_at`, `repo_pushed_at`, `repo_commits`; GitHub's facts at the last weekly refresh, not a judgement of upkeep) | 1137 of 1211 |
| Rows flagged `single-commit`: one commit on the default branch (the refresh sets and clears it from `repo_commits`) | 91 |
| Rows with a GitHub repository that at least one sibling directory links (`sources` citations, from the lists' READMEs at the last weekly read; a count of mentions, not a review) | 1130 of 1140 |
| Retired links | 2 |
<!-- shape:end -->

### When each repository was last pushed

GitHub's `pushed_at` for every row that records one (`repo_pushed_at`), as the
weekly refresh last read it, grouped by calendar month in UTC. A month says
when someone last pushed to any branch, not whether a project is maintained or
works; nothing here turns it into a verdict. The creation dates and commit
counts behind the same refresh are on the site and in the MCP server's rows.

<!-- pushed:start -->
| Month of the last push (UTC) | Rows |
| --- | --- |
| 2026-09 | 1137 |
<!-- pushed:end -->

### How many sibling directories link each repository

Every row with a GitHub repository, by how many of the sibling directories in
[`docs/sibling-lists.txt`](sibling-lists.txt) link that repository in their
README, as the weekly refresh last read them (`scripts/attribute_sources.py`
records each one in the row's `sources`). The lists copy from each other, so
this counts how widely a project is mentioned. It is not a review of the
project, and a repository no list links is not thereby worse.

<!-- cited-by:start -->
| Sibling directories linking the repository | Rows |
| --- | --- |
| 0 | 10 |
| 1 | 25 |
| 2 | 97 |
| 3–5 | 489 |
| 6–10 | 321 |
| 11–20 | 144 |
| 21 or more | 54 |
<!-- cited-by:end -->

### Negative results

Rows whose own author measured Jev for the use and concluded against it: a
`kind: benchmark` row records that in its `measurement` (direction
`unfavourable`), any other row carries the `negative-result` flag. Each is the
author's conclusion, not reproduced here. They are the rows to read before the
positive examples, and the README's "Measured, not claimed",
[`measured.md`](measured.md), the site (`?neg=1`) and the MCP server
(`search_examples(outcome="negative")`) list them first or on request.

<!-- negative:start -->
- [Hermes Agent: Jev compaction evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-agent-jev-evaluation) (`benchmark`): its measurement's direction is `unfavourable`; author-stated, not reproduced here.
- [worldmonitor: news threat classification](https://kydlikebtc.github.io/awesome-jev/?lang=en#worldmonitor-shadow-mode) (`benchmark`; caveats: `shadow-mode-only`): its measurement's direction is `unfavourable`; author-stated, not reproduced here.
- [no-mistakes: Jev review pre-brief, measured and retired](https://kydlikebtc.github.io/awesome-jev/?lang=en#no-mistakes-review-context) (`benchmark`): its measurement's direction is `unfavourable`; author-stated, not reproduced here.
- [hermes-jev-skills](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-jev-skills) (`plugin`): flagged `negative-result` (measured, not adopted); author-stated, not reproduced here.
- [jev-skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-router) (`plugin`): flagged `negative-result` (measured, not adopted); author-stated, not reproduced here.
<!-- negative:end -->

### Coverage gaps

<!-- gaps:start -->
Every pattern has at least one entry.

Empty kinds:

- **`case-study`**. The catalogue has no case study documenting both cost and observed outcomes.

Thin — under 2.5% of the catalogue:

- `recommendation` (1 of 1211) — The first example is a movie recommender: retrieval narrows the field, and Jev parses the request and chooses from the shortlist.
- `retry-control` (7 of 1211) — Most apparent matches are false positives: an HTTP client advertising "observable retries" is not a retry decision. The first real one was a semantic circuit breaker asking whether an HTTP 200 is a silent failure.
- `feature-extraction` (8 of 1211)
- `support-triage` (8 of 1211)
- `data-extraction` (17 of 1211)
- `document-triage` (20 of 1211)
<!-- gaps:end -->

Two holes are in the research rather than the ecosystem: **Reddit** produced
nothing verifiable across four retrieval routes, and **X/Twitter** is barely
represented for the same reason. Both are gaps, not judgements.

The breakdown by language, by how rows reach Jev, by star band per kind and by
language per pattern is on [the catalogue's shape](shape.md);
`python3 scripts/counts.py` prints it as text.

Link counts describe dated response records, and evidence counts describe saved
citations. They are not a count of successful current CI checks. The latest
successful link-check date can differ from an individual row's date. Catalogue
coverage does not imply that this repository ran the code or reproduced the
linked performance measurements; see [the review limits](vetting.md).

## Snapshot at 2026-09-22: what week one looked like

**The official material is the best material.** The cookbooks and pattern pages
in the vendor's docs are more useful than almost anything written about them,
and they are primary sources. If you only read five things, read those.

**Adoption was unusually fast.** First-class integrations landed within days
across the AI SDK, LangChain in both languages, Pydantic AI, LiteLLM, Effect,
Pydantic, Rig, ruby_llm and more, plus four or more hosted gateways. Production
integrations exist in repositories with six-figure star counts.

**Almost every number in circulation is vendor-reported.** The widely-quoted
speed and cost multiples come from the vendor's own workflow evaluations, whose
reference answers were derived from other models' judgements rather than human
ground truth. The vendor's launch post itself describes the headline figures as
an upper bound.

**Independent measurement is scarce, and the honest ones are the most useful
thing in this catalog.** A handful of projects published results that did not
flatter the model:

- A large agent framework ported the compaction approach, measured it, and
  concluded not to adopt it — recall came out below their existing summariser,
  and at a matched context budget it tied plain recency ordering.
- A news classifier found the model merely tied their incumbent on blind-judged
  headlines, and kept it in shadow mode rather than shipping it.
- A code-review tool measured materially more billed input for essentially no
  wall-clock gain, and recommended keeping the feature off by default.
- An independent tester found that reversing option order shifted a probability
  enough to cross a 0.9 threshold.

Cost was consistently the clear win. Quality was frequently a wash. Both of those
are useful to know before you build.

**A large fraction of "Jev projects" are not Jev.** Independent
reimplementations with a compatible wire format are among the most-starred
repositories mentioning the model, and are routinely miscatalogued as usage
examples. They are `kind: alternative` here with a `not-jev` flag. A compatible
API does not imply compatible calibration.

**Popularity and substance have not had time to correlate.** Four-figure star
counts sit on single commits; several notable projects declare no licence;
at least two ship the integration deliberately inert. Hence the `single-commit`,
`no-license` and `shadow-mode-only` flags.

**Nothing about the training method is published.** There is no paper, no reward
function, no dataset description and no reproducible evaluation for RLCD. An
unrelated 2023 paper abbreviates to the same four letters, which is a reliable
source of confusion.

## What to watch

The questions the snapshot above left open, and what can be said about each
since. A number in the table is counted from `catalog.json` when the page is
regenerated; a status is a reading of its source, dated and marked as a
person's or a model's. A recent change is counted from the snapshot before the
newest in [`history/`](../history/) (the newest is the latest weekly refresh's
own), or, until there are two, over the newest week of `first_seen` dates, and
either way names its dates. The questions, how each is tracked and the dated
readings live in [`watch.json`](../watch.json); `scripts/build_watch.py`
writes the table.

<!-- watch:start -->
| Question | Now | Recent change | How it is tracked |
| --- | --- | --- | --- |
| Whether independent benchmarks accumulate, and whether they keep landing on "cheap but comparable" rather than "better". | **71** independent reports ([on the site](https://kydlikebtc.github.io/awesome-jev/?indep=1&lang=en)); directions their authors state, not reproduced here: favourable 1, mixed 13, unfavourable 3, inconclusive 1, none recorded 53; 18 of these 18 directions not yet read against the report by a person ([review queue](review-queue.md#measurement-unread)) | +26 first seen 2026-09-24 to 2026-09-30 (history/ does not yet hold this count from two snapshots) | Benchmark rows not flagged vendor-reported, and the directions their authors state in the rows' measurement: author-stated, not reproduced here. A row without a measurement, or whose measurement states none, counts as none recorded. |
| Whether the option-ordering sensitivity reproduces. If it does, option order becomes part of everyone's prompt-freezing discipline. | [Probing Jev's behaviour with repeated API calls](https://kydlikebtc.github.io/awesome-jev/?lang=en#ahastudio-til-jev-probing) (caveats: `no-license`, `unverified-claims`), [pijev](https://kydlikebtc.github.io/awesome-jev/?lang=en#pijev-typellm). No independent reproduction is recorded: one listed row reports the effect, the other averages answers over option orderings to guard against it. (read by a model, not yet by a person, 2026-09-28) | — (a reading, dated in the cell before) | Rows listed in watch.json as reporting or addressing option-order sensitivity; no field in the catalogue records it, so a new such row counts only once someone adds it there. |
| Whether a paper appears. | None linked: the documentation's index links no paper, and its AI primer names the training path (RLCD) without linking one. (read by a model, not yet by a person, 2026-09-28; [source](https://docs.typesafe.ai/introduction/machine-learning-primer)) | — (a reading, dated in the cell before) | A reading at the source: whether the vendor's documentation links a paper on the training method. |
| Whether the alternatives converge on the wire format well enough that patterns really do become portable, calibration aside. | **37** of the 55 alternatives citing a file ([on the site](https://kydlikebtc.github.io/awesome-jev/?k=alternative&lang=en)) | +25 first seen 2026-09-24 to 2026-09-30 (history/ does not yet hold this count from two snapshots) | A proxy: of the kind: alternative rows citing a file, those whose evidence.matched strings include /v1/systemone. It says the endpoint path is the same, not that the request or answer shapes match, and nothing about calibration. |
| Whether rate limits and pricing settle. | Not yet: the models page still warns that rate limits are adjusting dynamically and can change without notice. (read by a model, not yet by a person, 2026-09-28; [source](https://docs.typesafe.ai/models)) | — (a reading, dated in the cell before) | A reading at the source: whether the vendor's models page still says its limits can change without notice. |
<!-- watch:end -->
