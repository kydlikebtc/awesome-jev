# Maintaining awesome-jev

What runs on its own, what a person does, and where the two meet. Written on
2026-10-30, when the owner approved the first month of the long-term plan
(one rolling pull request of drafted rows a week, merged on Fridays). Change
this file when the routine changes; the drafting tasks follow it.

Contributors want [CONTRIBUTING.md](CONTRIBUTING.md); this is the routine
behind it.

## The week (times in UTC)

| When | What runs | Reports through |
| --- | --- | --- |
| Monday 06:00 | `links.yml`: every row's link | an issue labelled `links`, only when a link is dead |
| Tuesday 06:00 | `claims.yml`: every cited file still holds its `evidence.matched` | issue #28 |
| Wednesday 06:00 | `metadata.yml`: stars, licences, repository dates, `.discover/facts.json`, history snapshots | its commit and issue #32 |
| Thursday 06:00 | `discover.yml`: new candidates from the sibling lists; rewrites the queue | issue #14 |
| Thursday 14:37 | weekly upkeep task: the judgement work #14, #28 and #32 leave, and at most 10 drafted rows | one draft pull request |
| Every day but Thursday, 00:33 | daily drafting task: at most 15 drafted rows | one rolling draft pull request a week |
| Every day 07:30 | `watchdog.yml`: every scheduled workflow succeeded within 8 days, and a row entered `catalog.json` within 10 | an issue labelled `watchdog` |
| Friday | the owner merges the week's two drafting pull requests | |

The two tasks are scheduled Claude Code tasks in the owner's Claude project,
not workflows: GitHub cannot see them, and the watchdog only notices them
through rows stopping (`scripts/watchdog.py`, `intake()`).

## What every drafted row is

A model read it, and every surface says so (the C2 tier, since 2026-10-24):

- `evidence.model_read_on` is the day the model read the cited file;
  `summary_source` is `model-written`; `zh_machine` is `true`;
  `patterns_model_read_on` only when the row was read against
  [docs/patterns.md](docs/patterns.md).
- Never `evidence.read_on`, `patterns_reviewed` or `summary_source: curated`.
  Those are a person's reading, and a model never sets them.
- `notes` and `notes_zh` end with the sentence saying an AI assistant drafted
  the row and no maintainer has read the call site yet.
- Stars and the other `repo_*` facts are left to Wednesday's refresh.

The tasks start each row with `python3 scripts/model_draft.py OWNER/NAME PATH`
and check it with `python3 scripts/model_draft.py --check FILE` before adding
it. The draft carries what a script knows; `--check` holds the finished row to
the schema, lint's rules, the tier above, and the cited file at HEAD.

A person who later reads a row's call site sets `evidence.read_on` (and may
rewrite the summary as `curated`); the row then leaves
[docs/review-queue.md#model-read](docs/review-queue.md#model-read).

## Candidates nobody can settle: docs/held.txt

When a run reads a candidate and cannot decide (no call site it can find, a
gateway it should not judge, a project that may not be in scope), it adds the
candidate to [docs/held.txt](docs/held.txt) with the reason, in the same pull
request. A held candidate moves out of "To read" in #14 into its own section,
so the next run does not read it again. The weekly upkeep does the same for a
catalogued row it doubts: a proposed path that is a test, a cited file gone.

Holding decides nothing. Every line is listed in
[docs/review-queue.md#needs-person](docs/review-queue.md#needs-person). A
person settles one with a row, a line in [docs/declined.txt](docs/declined.txt)
or nothing, and deletes the held line in the same pull request.

The queue also parks, without anyone reading them, candidates with two weak
facts and those still under 3 stars and 5 commits with no push in 28 days
(`scripts/discover_facts.py`). Parked is not declined: a candidate that grows
returns to "To read" by itself.

## Merging

1. The weekly upkeep's pull request first, then the daily rolling one. Both
   change `catalog.json`: after the first merge, the second needs main merged
   in. The daily task does that on its next run, or a person does it and runs
   `python3 scripts/check.py --fix`.
2. Merge only on green CI. A pull request from a fork gets no CI until its
   workflows are approved, so no red cross does not mean it passed: run
   `python3 scripts/lint.py` and
   `python3 scripts/review_pr.py --base origin/main --offline` on it first.
3. Nobody but the owner merges. The tasks never merge, close or approve a pull
   request, never push to main, and take no action outside this repository.

## When something stops

- The watchdog issue names what stopped. For a workflow, open its newest run,
  fix the cause and run it again from its Actions page.
- "No row has entered catalog.json in 10 days": look for drafting pull requests
  waiting to be merged first. If none are open, the tasks have stopped; check
  them in the Claude project.
- Main red: every pull request's lint fails with it, and `metadata.yml` cannot
  push. Fix main first, in one pull request, and let the drafting runs name it
  rather than fix it again.
- #14's "To read" count keeps growing: the drafting pace is below what
  discovery finds (about 120 candidates a week in October 2026). Each weekly
  snapshot in `history/` records the queue's counts, and the "Over time" table
  in [docs/shape.md](docs/shape.md) shows "Candidates to read" from them.

## When Jev ships a version

What PR #46 did by hand for Jev 1.14 (2026-10-15), as a list. Read the
vendor's announcement, [models](https://docs.typesafe.ai/models) and each
changed docs page first; write down only what they say, dated.

1. `compat.json`: add the new version to the `model` cell of each surface whose
   own docs name it, and say in `notes` what an alias points to and on which
   date it was read. Nothing else needs the version typed in: the call-site
   signals (`_github.version_signals`), the MCP server's model-string hint and
   the claims issue's "now pins" lines all read it from here
   (`tests/test_model_release.py`). Never add a gateway id because the native
   API has it.
2. Limits and opt-ins: the `limits` rows in `compat.json` and
   [docs/compatibility.md](docs/compatibility.md) for any new header, input
   or context size.
3. The prose that names versions: the README strings
   (`scripts/readme/strings.py`, both languages), `skills/awesome-jev/SKILL.md`,
   [docs/patterns.md](docs/patterns.md) and the examples under `examples/`.
4. A new question type: the three primitives (Choice, Score, Noul) are what
   the schema's `question_types`, the counts, the filters and the picker
   cover. A new one first goes in `experimental_seen`
   (`scripts/verify_claims.py`, `EXPERIMENTAL_SHAPES`, read from the official
   SDKs' types), as Box did on 2026-10-31, and is listed in
   [docs/review-queue.md#experimental](docs/review-queue.md#experimental).
   Making it a fourth primitive is a schema change across every surface:
   decide it when the vendor drops "experimental".
5. After the next Tuesday's claims run: rows whose cited file moved its pin
   are reported as `version-moved`, counted per version.
   `python3 scripts/verify_claims.py --propose-version-rewrite` prints their
   new `evidence.matched`; apply it without touching `read_on`.
6. `python3 scripts/check.py --fix`, then one pull request for all of it.

## Monthly and quarterly

- From 2026-12-03, on the first Thursday of each month, the weekly upkeep
  picks 20 model-read rows at random for the owner to mark agree or disagree
  (T1). The agreement rate goes into the next pull request, then
  [docs/status.md](docs/status.md).
- The plan is reviewed each quarter, first at the end of January 2027.

## What only the owner can do

Repository settings no task can reach: the PyPI publisher for
`awesome-jev-mcp`, approving workflow runs from forks, the repository
description (issue #26), and the optional `TRAFFIC_TOKEN` secret the weekly
traffic snapshot waits for.
