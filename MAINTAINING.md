# Maintaining awesome-jev

What runs on its own, and where each run hands over to the next. Written on
2026-10-30, when the owner approved the first month of the long-term plan.
Since 2026-11-05, when the owner asked that the whole flow run with nothing
left for them to do by hand, no step waits for a person: each case that used
to wait has a rule below, and the two drafting tasks merge their own pull
requests. Change this file when the routine changes; the drafting tasks follow
it.

Contributors want [CONTRIBUTING.md](CONTRIBUTING.md); this is the routine
behind it.

## The week (times in UTC)

| When | What runs | Reports through |
| --- | --- | --- |
| Monday 00:05 | `launch-week.yml`: closes last week's launch board, opens this week's, then tells each launch's issue (again at 06:05 and 12:05, which do nothing when the first run did it all) | its commit, the vote posts, the launch issues |
| Monday 06:00 | `links.yml`: every row's link | an issue labelled `links`, only when a link is dead |
| Tuesday 06:00 | `claims.yml`: every cited file still holds its `evidence.matched` | issue #28 |
| Wednesday 06:00 | `metadata.yml`: stars, licences, repository dates, `.discover/facts.json`, history snapshots | its commit and issue #32 |
| Thursday 06:00 | `discover.yml`: new candidates from the sibling lists; rewrites the queue | issue #14 |
| Thursday 14:37 | weekly upkeep task: the judgement work #14, #28 and #32 leave, every line in `docs/held.txt`, the monthly items below, and at most 10 drafted rows | one pull request, which it merges once its checks pass |
| Friday 00:20 | `launch-collect.yml`: files next week's launches on `main` (again at 06:20 and 12:20, which change nothing when the first run did it) | its commit |
| Every day but Thursday, 00:33 | daily drafting task: what stopped, the repository's open issues and pull requests, the call sites of launches nobody has read, then at most 15 drafted rows | one pull request, which it merges once its checks pass |
| Every day 07:30 | `watchdog.yml`: every scheduled workflow succeeded within 8 days (32 for a monthly one), and a row entered `catalog.json` within 10 | an issue labelled `watchdog` |
| The 1st, 09:00 | `data-release.yml`: tags main `catalog-<YYYY-MM>` for the month that ended and publishes a Release with `catalog.json`, `retired.json` and the schema | the Release |
| The 15th, 09:00 | `award.yml`: once the board's year has ended (first on 2027-09-15), writes the year's decision award; otherwise does nothing | its commit |
| After a run on `main` fails | `retry.yml`: runs the failed jobs once more, three minutes later | the run's second attempt |

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
[docs/review-queue.md#model-read](docs/review-queue.md#model-read). Nothing
waits for that: it raises a row's tier, and the catalogue runs without it.

## Candidates a run cannot settle: docs/held.txt

When a daily run reads a candidate and cannot decide in its time (no call
site it can find, a gateway, a project that may not be in scope), it adds the
candidate to [docs/held.txt](docs/held.txt) with the reason, in its pull
request. A held candidate moves out of "To read" in #14 into its own section,
so the next run does not read it again. The weekly upkeep does the same for a
catalogued row it doubts: a proposed path that is a test, a cited file gone.

Holding decides nothing, and nothing stays held past the next weekly upkeep.
That run settles every line by the first of these rules that fits, writes the
decision and its reason where the rule says, and deletes the line in its pull
request:

1. **No call site found.** It searches the candidate's default branch for the
   call-site strings `scripts/_github.py` knows. A file that calls Jev: it
   drafts the row from that file. None: it declines the candidate in
   [docs/declined.txt](docs/declined.txt), "no Jev call site in its code
   (searched YYYY-MM-DD)".
2. **The same code as a catalogued row** (a fork, a mirror, a renamed copy, a
   package another row already carries): declined, "covered by the
   catalogued row `<slug>`".
3. **Speaks Jev's request shape without calling Jev**: it serves
   `/v1/systemone` itself, or sends Jev-shaped requests to another model by
   default, a gateway to other backends included. An `alternative` row,
   flagged `not-jev`.
4. **Calls Jev only to compare it with its own model.** A `benchmark` row
   when the comparison's results are published in the repository or a page
   it links; otherwise declined, "compares with Jev but publishes no
   results".
5. **A gateway that pools keys or offers anonymous access to the API**:
   declined, "a gateway that pools access to the API, not a decision
   example", as `antting/jev-accounts-hub` was.
6. **Neither calls Jev nor takes its request shape** (its own API, a local
   model with another interface, Jev named only as an inspiration):
   declined, "does not call Jev or take its request shape".
7. **A catalogued row whose cited file is gone or only a test**: the evidence
   moves to the file that now makes the call, as a model's reading; when no
   file calls Jev any more, the row is retired with that reason.
8. **Anything else**: the closest rule, with the reason written beside the
   decision. No line is held a second week.

A decline is not forever: a new-entry issue for a declined repository is read
again by the daily run, which adds the row and deletes the declined line when
the code now calls Jev.

The queue also parks, without anyone reading them, candidates with two weak
facts and those still under 3 stars and 5 commits with no push in 28 days
(`scripts/discover_facts.py`). Parked is not declined: a candidate that grows
returns to "To read" by itself.

## The launch board

Since 2026-11-03 the site has a launch board over the catalogue
([docs/launches.md](docs/launches.md)): a page per product and per maker, a
page per closed week, a README badge per product (listed, launching, then a
top-three place), and the board itself, which also lists the products whose
stars rose fastest between the two latest weekly refreshes (`history/`). The
pages are written with the others at deploy (`scripts/site_products.py`).

A week goes like this, with no step for a person:

1. **Any day:** someone opens a launch issue (the "Launch a product" form).
   `launch-intake.yml` answers it with a comment from
   `scripts/launch_intake.py`: ready for a week, with what the board's rules
   settled; not read yet, naming what GitHub did not answer, which Friday's
   filing reads again; or not launched and what to change. It only comments.
   The rules it applies (docs/launches.md, "The week"): a maker it cannot
   confirm launches as a hunter; an account younger than 30 days launches in
   the first week after it turns 30; a fork with fewer than 10 commits of its
   own, or a repository with no push for 60 days, does not launch until it
   has them, and editing the issue checks it again.
2. **Friday 00:20 UTC:** `launch-collect.yml` runs `python3
   scripts/launch_intake.py --collect next`, which takes every open launch
   issue, checks it again against today's catalogue with the facts its check
   comment recorded, reading GitHub for any it did not record (`--live`
   reads everything again), writes `launches/<week>.json` for the coming
   Monday's week, and adds a confirmed maker's login and line to their row. A
   launch whose week has passed goes on this one. It regenerates what the
   row change feeds, runs the checks on that commit and pushes it to `main`;
   if `main` moved and the rebase does not apply, it files the week again
   from the new `main`, up to three times.
3. **Friday to Sunday:** `python3 scripts/launch_intake.py --unread` lists the
   products about to launch whose call site nobody has read; the daily task
   reads those first, so each launch opens with at least a model's reading.
   When the code turns out not to call Jev, the same pull request flags the
   row `not-jev` (an `alternative` when it speaks Jev's request shape), sets
   the launch to `removed` with that reason in the week's file, and the task
   tells the launch's issue why.
4. **Monday 00:05 UTC:** `launch-week.yml` runs `scripts/launch_week.py
   --monday`. It closes last week (reads the votes, counts under rules v2
   the votes of a launch that look like a ring of new accounts as nothing and
   marks its result, ranks the launches, writes the counts and how many
   accounts voted and came back) and opens this week (one vote post per
   launch in the `Launches` category, and who had read each call site), then
   pushes the week files to `main`, checks first, running the week again from
   the new `main` if it moved, and rebuilds the site. Once the files are on
   `main`, `--tell` comments on each launch's issue: this week's get the link
   to their vote post and are closed, last week's get their result (and a top
   three the line for its badge). Each issue is told once per stage, so a
   rerun tells nobody twice, and a comment GitHub refuses never fails the
   week. With nothing on file it does nothing and still succeeds, so the
   watchdog sees it run.

What the board is measured by (docs/launches.md, "How the board is
measured") is counted when a week opens and closes and shown on the board,
the week's page and the monthly report; nothing else needs doing for it.

`launch-votes.yml` (Run workflow, with a Discussion's number) reads one post's
votes into the job summary and writes nothing else: the check, before the
first week, that the workflow's token can read reactions and account ages
(passed 2026-11-03 on #82). `launch-probe.yml` (Run workflow) starts one
discussion in `Launches` and deletes it at once: the check that the same
token may post where only maintainers may. Neither is part of a week; both
are there for a question about the token. The Monday run only takes a post
for a launch's vote post when `github-actions` or the owner started it, so
posts others start there are never counted.

**The award.** On the 15th of each month `award.yml` runs `python3
scripts/award.py --due`, which, once the board's year has ended (15
September, from 2027), writes `docs/award/<year>.md`: per pattern, the first
of its shortlist, by rank and then counted votes among products whose call
site a person or a model read. Nobody picks it; a year already written is
left alone.

Every rule of the board is in `scripts/launches.py`, and
`python3 scripts/check_launches.py` holds `launches/` and `makers/` to them
in every check run. A closed week's results are never edited by hand: a wrong
result is fixed by a new rule version or by removing the launch with its
reason.

## Merging

1. Each task merges its own pull request once its checks pass, with a merge
   commit. The weekly upkeep's and the daily one both change
   `catalog.json`: a pull request that conflicts with `main` gets `main`
   merged in, `python3 scripts/check.py --fix`, and a push, and is merged
   when its checks pass again. A run that ends before its checks finish
   leaves the pull request open, and the next run of either task merges it
   first.
2. Merge only on green CI. A red check is fixed in the same pull request, the
   cause and not the symptom; no test is skipped or weakened to get there.
3. Pull requests from others: the daily run reads each open one. One that
   changes only rows (`catalog.json`, and what regenerates from it) and passes
   `python3 scripts/lint.py` and
   `python3 scripts/review_pr.py --base origin/main --offline`, with a call
   site the run read itself, is merged by the run; otherwise the run comments
   what to change. A pull request from a fork may get no CI until GitHub's
   approval for a contributor new to GitHub, so no red cross does not mean it
   passed: the run checks it locally either way. A pull request from someone
   else that changes scripts, workflows, `src/` or `tests/` is never merged by
   a task, because merged code runs with this repository's tokens: the run
   says so in a comment and leaves it open for the owner, whenever they like.
4. The tasks never push to `main`, force-push anything, approve a pull
   request, or act outside this repository. They comment on this
   repository's issues and pull requests, and close an issue only when what
   it asked for has landed or its comment says why not.

## When something stops

- A run on `main` fails: `retry.yml` runs its failed jobs once more, three
  minutes later. The Monday and Friday runs have two more schedules the same
  day as well. A run that fails a second time is left failed for the daily
  task, which starts each run by reading the newest runs of the workflows on
  `main`: it reads the failed run's log, fixes the cause in its pull request,
  and the next scheduled run picks up the fix.
- The watchdog issue names what stopped; the daily task reads it first. "No
  row has entered catalog.json in 10 days": the tasks' pull requests are not
  merging, or the tasks have stopped. A run of either task that finds this
  fixes its pull requests first; if neither task is running, nothing in
  GitHub can start them, and the issue stays open until they do.
- Main red: every pull request's lint fails with it, and `metadata.yml` cannot
  push. The daily task fixes main first, in its own pull request, and the
  weekly upkeep names it rather than fixes it again.
- A `regenerate/*` or `metadata/refresh-*` branch: `lint.yml` and
  `metadata.yml` leave their commit there when `main` moved under them and
  the rebase failed. The daily task opens a pull request from it, merges it on
  green (or closes it when `main` already has what it holds), and deletes the
  branch.
- #14's "To read" count keeps growing: the drafting pace is below what
  discovery finds (about 120 candidates a week in October 2026). Each weekly
  snapshot in `history/` records the queue's counts, and the "Over time" table
  in [docs/shape.md](docs/shape.md) shows "Candidates to read" from them.

## When Jev ships a version

What PR #46 did by hand for Jev 1.14 (2026-10-15), as a list. Each Thursday
the weekly upkeep reads the vendor's [models](https://docs.typesafe.ai/models)
page and its changelog; when a version is new, it does this list in its pull
request. Read the vendor's announcement and each changed docs page first;
write down only what they say, dated.

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
   Making it a fourth primitive is a schema change across every surface,
   made when the vendor drops "experimental".
5. After the next Tuesday's claims run: rows whose cited file moved its pin
   are reported as `version-moved`, counted per version.
   `python3 scripts/verify_claims.py --propose-version-rewrite` prints their
   new `evidence.matched`; apply it without touching `read_on`.
6. `python3 scripts/check.py --fix`, then one pull request for all of it.

## Monthly and quarterly

- **Every week, overview rows (K2).** The weekly upkeep files a batch of twenty
  overview rows from [docs/review-queue.md#unsorted-overview](docs/review-queue.md#unsorted-overview)
  under their patterns, reading each cited file, and records it as a model's
  reading (`patterns_model_read_on`, never `patterns_reviewed`). A row it
  cannot place stays `overview`.
- **The report (D1).** On the first Thursday of a month, from 2026-11-05, the
  weekly upkeep writes the month before's report,
  `python3 scripts/build_monthly.py --month <YYYY-MM>`, into
  [docs/monthly/](docs/monthly/README.md) and puts it in its pull request. A
  report is written once from the snapshots in `history/` and never
  regenerated. It is published in the repository and nowhere else.
- **The data release (D2).** On the 1st, `data-release.yml` tags and
  publishes the month's data on its own. A month already tagged is left
  alone; a failed run is retried by `retry.yml`.
- **The model check (T1).** From 2026-12-03, on the first Thursday of each
  month, the weekly upkeep runs `python3 scripts/model_sample.py --month
  <YYYY-MM>` and checks each row it prints (a sample of those only a model
  has read) with a second reading: for each row it reads the cited file first,
  writes down what the file does, and only then compares that with the row's
  summary, patterns and primitives, marking agree or disagree with a note
  for each disagreement. The answers go into
  [docs/model-checks.json](docs/model-checks.json) as `"checker": "model"`
  (`--check` validates it), and [docs/status.md](docs/status.md) shows the
  newest month's count and that a model checked it. A disagreement is fixed
  in the same pull request. An agreement is not a reading: a row gets
  `evidence.read_on` only when a person says they read the file. Below 18
  of 20, drafting pauses: that run changes the drafting rules here and in
  `scripts/model_draft.py` for what the disagreements share, and drafting
  resumes the next day.
- **Practice reviews (K1).** [docs/practice/](docs/practice/README.md) has one
  review per pattern written so far, its prose a model's and labelled so, its
  tables generated by `scripts/build_practice.py`. When a recommended row
  leaves the catalogue or its pattern, the build fails and the weekly upkeep
  makes a new pick from the pattern's rows.
- The plan is reviewed each quarter, first at the end of January 2027.

## Set up once

These were the owner's to turn on, because no task can reach a repository
setting. Each is done, or is optional; none recurs.

- Discussions (Settings, General, Features) with a category named `Launches`
  in the Announcement format, where only maintainers start a discussion and
  anyone can react: the launch board's vote posts go there, and opening a
  week fails without it (both turned on 2026-11-03).
- The repository description: `_stats.pitch_public()`, which states no count
  since 2026-11-05, so it changes only when its wording does. When it does,
  `description.yml` keeps one issue with the `gh repo edit` command.
- Approval for workflow runs from forks: GitHub asks for it only for
  contributors new to GitHub (Settings, Actions, General), so most first pull
  requests run their checks at once.
- Optional: the PyPI publisher for `awesome-jev-mcp` (`publish.yml`, Trusted
  Publishing), and the `TRAFFIC_TOKEN` secret the weekly traffic snapshot
  waits for. Nothing else depends on either.
