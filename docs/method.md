# Data and method

How the first build of this catalog was produced, what was checked, and where it
is weakest. If you want to reproduce or audit it, this is the page.

## Pipeline

1. **Establish the primary facts first.** The official docs serve raw Markdown at
   `<page>.md`, so the API reference, primitives, confidence, models and
   limitations pages were fetched and read directly rather than summarised. Every
   claim about the model in this repo traces to one of those.
2. **Sweep in parallel, along four axes.** Official sources; platform and
   framework integrations; open-source projects and packages; articles, videos
   and discussion. Four passes, each required to cite a URL per claim and to mark
   anything it could not confirm.
3. **Verify code entries at the call site.** For every row claiming code, the
   actual calling file was read to confirm which primitives are used. This is
   where README descriptions and reality diverge most often.
4. **Verify repository metadata from the API.** Stars, licence, creation date and
   last push came from the GitHub API on 2026-09-22, not from badges. Only
   stars and licence were stored in the rows then; creation date and last push
   are stored since 2026-09-27, re-read every week (see *Why a status code is
   not a verdict*).
5. **Reject aggressively.** See "What was excluded".
6. **Write both summaries by hand**, English and Chinese, from what the page
   actually said.
7. **Validate and generate.** `scripts/lint.py` then `scripts/build_readme.py`.

## What the first build checked, and what it found

- **148 entries**, 124 carrying code, 36 official.
- **Two agent reports contradicted each other twice**, and both conflicts were
  resolved by direct inspection rather than by majority:
  - A Discord moderation bot was called a name collision by one pass. Reading
    `moderator.py` showed a real `typesafe` import and `jev-latest` default. It
    stayed in.
  - A widely-starred repository was catalogued by the community site as a visual
    inference tool using Jev. Scanning all 52 of its files found **zero**
    references to the API. Its own README says it is a research starter, not a
    copy. It was reclassified as `alternative` with a `not-jev` flag.
- **A fabricated integration was found and excluded**: a skills repository
  documenting a Jev API that does not exist, with primitives' meanings inverted,
  linking to a repository that returns 404.
- **The linter caught a bug in its own rule.** The `official` check originally
  accepted only `typesafe.ai` hosts, which wrongly rejected the vendor's own
  GitHub org. The rule was widened to the org and no further.

## Call-site text is re-checked separately from human review

A row carrying `question_types` asserts which primitives a project's code calls.
That was true when a person read the call site, and nothing stopped it going
stale — an upstream refactor could remove the integration entirely and this
catalog would keep claiming it.

Readable repository sources record `evidence`: the file the claim was read in,
strings from that file, and the reported reading date in `read_on`.
`scripts/verify_claims.py` fetches
each one from the repository's default branch and asserts those strings are
still there. A scheduled job runs it weekly and opens an issue on failure,
rather than failing the build — a moved file needs a reviewer to distinguish a
rename from a removed integration.

The evidence count is the number of stored citations, not the number that passed
the latest job. A successful string match establishes only that those strings
remain in the fetched file. It does not execute a call path, check API
compatibility, reproduce performance, or renew the human review date. The
workflow report and any resulting issue must be read to assess its latest run.

Deliberately unpinned to a commit. Pinning would verify a historical snapshot
forever and never notice a removal, which defeats the purpose.

The first backfill was machine-assisted and human-reviewed: a `--discover` mode
reads each repository and proposes a path, then a person checks it. That review
mattered — the discoverer favoured test files over implementations in seven
cases, and proposed the same file for all four of this repo's own examples. It
also caught a mistake in the review itself: one hand-written override cited a
file that did not contain the strings claimed, and the verifier failed it on the
first real run.

Rows whose source is not a readable repository file — a docs page, a video, a
paywalled article — carry `evidence_none` saying which, rather than a fabricated
citation.

Since 2026-09-27, a pull request's rows are checked before the merge, not only
by the weekly jobs after it. Until then a pull request's own checkboxes were
all that said its call site had been read, its stars and licence taken from the
API, and whether it was its author's own project. `lint`'s `review` job now
runs `scripts/review_pr.py`, which compares `catalog.json` with the merge base
and, for each row added (and each changed field one of its checks reads),
re-reads the cited file with the function `claims` uses; compares
`repo_license` and the `archived` flag with the GitHub API exactly, and `stars`
within five or a tenth of GitHub's count, since stars move every day; notes a
repository with a single commit and no `single-commit` flag; requests the link;
compares the pull request's author with the repository's owner and the row's
recorded author, so an undisclosed self-submission is marked; checks that the
flags needing a reason have `notes`; and says where the discovery script's
keyword rules would have classified the row differently, as a hint. The result
is a card in the run's summary, with each finding also marked on its line of
`catalog.json`. These are the same grades of evidence as the weekly jobs — a
text match and a comparison of facts — and the card is not a review: it
neither replaces nor records anyone reading the call site. It runs the base
branch's copy of `scripts/` against the pull request's data, from a separate
checkout of the base commit, so a pull request cannot soften the checks that
judge it by editing them (it can still edit the workflow, which its diff
shows). The card is advisory at first: it exits 0 whatever it finds, and the
step cannot fail the job. Once a fortnight of cards has shown no systematic
false alarm, `--blocking` and the removal of the step's `continue-on-error`
make an error fail the pull request. Run against the five pull requests open
that day, it marked three rows whose authors own the repositories without the
`self-submitted` flag, one repository with a single commit, and one star count
a sixth below GitHub's. The same day `lint.py` made a row with `question_types`
and neither `evidence` nor `evidence_none` an error instead of a warning; no
row in either file broke the rule, and `not-yet-backfilled` remains an honest
way to satisfy it.

Since 2026-09-27, a citation records what the cited file shows, and the counts
keep the kinds apart. Until then every `evidence` record was published as a
call-site citation, one number of 1,121, although 52 of those rows were
`kind: alternative`: projects that by definition are not built on Jev, whose
files matched strings such as `/v1/systemone` because they serve Jev's request
shape or send it to Jev to compare against. `evidence.kind` is now `call-site` (the default when absent), `wire-shape`
(the file shows a project speaking Jev's request shape rather than building on Jev: a
reimplementation, a compatible server, an adapter backed by other models, or a
comparison script) or `example-only` (an example the project ships, not its own
integration). The 52 alternative rows were marked `wire-shape` mechanically,
since the row's own kind already says it; nothing else was inferred, and
`lint.py` now fails an alternative whose evidence says anything else. The
README, `docs/status.md`, `llms.txt`, the README cover and the site's preview
card now print the call-site count (1,069 once the 52 were set apart), with the
other two beside it where there is room, and the site labels a wire-shape or
example-only citation as what it is. Two weaker signals are machine judgements rather than facts, so
they are neither written into `catalog.json` nor raised as one lint warning per
row: a cited file under an `examples/` directory with no `evidence.kind`
recorded (22 rows; an SDK's examples are often its clearest call site, and only
a reader can tell), and a citation whose only matched string is a model name or
the API host (76 rows; any file configuring Jev contains one, whether or not it
calls it). `_stats` counts both, `docs/status.md` publishes the counts, and the
generated `docs/review-queue.md` lists the rows, one section per signal, with
what a reader records to take a row off.

Since 2026-09-27, a row with code in a GitHub repository needs `evidence` or
`evidence_none`, as a row claiming primitives already did. Keyed on
`question_types`, which 100 rows set, the rule had missed 34 rows with code
that carried neither. Each was read the same day and given one or the other:
16 documentation pages (the vendor's cookbooks and reference pages, LiteLLM's
and Pydantic AI's pages, the official agent skill's page and the repository
behind it, whose skill file is prose pointing at the docs) got `docs-page`; two
blog posts `not-a-repository`; one paywalled article `paywalled`. Eight got a
cited file whose strings `verify_claims.py` then found on the default branch:
five call sites (aegis, Bifrost, Opik, the gateway behind OpenCode Zen, and one
sibling list whose submissions a Jev review workflow judges) and three
`wire-shape` (NanoJev's probe of the real model, simple-jev's server, and
TypeSafe's own adapter backed by other models). Three got a new value,
`no-jev-call-site`, for code that neither calls Jev nor speaks its request
shape: two independent reimplementations with their own interface and one
research repository. Four had `has_code` turned off, and their `languages`
with it, because the link holds no code to adapt: two sibling lists, the
community site whose notes already say not to copy its code, and a notes
repository whose note on probing Jev contains no code. The new `evidence`
records carry no `read_on`, since an agent session read those files, not a
person. `verify_claims.py --discover` now proposes a file for these rows as
well, labelled `wire-shape` for an alternative, and the review card marks the
same case. A retired row is exempt: its repository is gone. The schema's
descriptions of `evidence` and `evidence_none` no longer tie them to
`question_types`, and `_stats` counts rows with code citing nothing and giving
no reason on any host (none that day), which `docs/status.md` publishes.

Since 2026-09-27, the weekly refresh also records which primitives' request or
answer shapes each cited file contains, as `primitives_seen`, and every surface
keeps it apart from `question_types`. A person's reading named the primitives
of 100 rows (72 of them citing a file), while the claims job fetched 1,129
cited files every week and kept nothing but a substring test. The file of every
claim that still holds is now searched for five written forms: the request's
`type` field (`"type": "choice"` in JSON, a Python dict or a JS object,
`type: 'noul'` in a TS type, `"type" => "score"` in Ruby, PHP or Elixir, also
inside an escaped JSON string), the `Choice(`, `Score(` and `Noul(`
constructors (not `click.Choice(`), the TypeScript SDK's `choice(`, `score(`
and `noul(` helpers when the file imports them from `@typesafe-ai/sdk`, and
`.noul`. The bare words, `.choice`, `.score`, `type="noul"` as a keyword
argument (the test doubles that build fake answers), a Go struct's `Type:`
field, a Kotlin map's `put("type", …)` and Vercel's `boolean` do not count.
Reading all 1,129 files from the raw host takes under two minutes and asks the
API 13 times. 686 rows got a signal (choice in 488, score in 241, noul in 495),
637 of them rows with no `question_types`, and 25 of them alternatives whose
file speaks the shape without building on Jev; the first run, before review
added the TypeScript SDK's helpers, had given 52 of those rows fewer primitives
or none. Against the 72 cited readings it agreed exactly on 32, showed fewer
primitives on 8, none on 23 (a wrapper that passes questions through or builds
them from variables, or a form the list leaves out), and more on 9: TypeScript
types declaring all three, a helper, test fixtures in the cited file, and on
three rows a `noul` question built or its answer read where the reading records
no `noul` — rows for a person to re-read, since the signal never corrects
`question_types`. That is why it is a signal about a file and not about what
the code calls. The
field is written only by `verify_claims.py --write-signals` in the metadata run
(a read the rate limit stops leaves a row as it was; a file that no longer holds
its claim loses the signal); lint allows it only beside `evidence`; and nothing
that asks what a row claims reads it: lint's rules, the site's search, the MCP
server's `question_type` filter and the published claim counts read
`question_types` alone. The README's primitives figure, `docs/status.md`,
`llms.txt` and the site show the two side by side under separate names, read by
a person and text signal only, and never add them.

Since 2026-09-27, the READMEs and the pattern pages link each row's cited file,
as the site already did. A README row such as ai-hedge-fund's, whose summary is
the project's own description ("An AI Hedge Fund Team"), said nothing about what
the project does with Jev, while the catalogue held the exact file
(`hedge_fund/llm/client.py`). The link is named for what `evidence.kind` says
the file shows (*call site*, or *cited file* for a wire-shape or example-only
file) and followed by `read_on`, the day a person last read it, so it reads as
a dated reading and never as a check that passed; a row with no dated reading
gets the link alone. The pattern pages also print the path. Like the weekly text
check, the link is deliberately unpinned: it opens the file at `HEAD`, as it is
now, and returns 404 once the file moves. `scripts/evidence_url.py` builds it
the way `site/catalog-core.mjs` does in the browser, following the URL
Standard's parsing of an https address; one file of cases is run by both test
suites, and a test runs the site's own function beside the Python one over every
row and 4,000 made-up addresses, which agreed on all of them.
`docs/review-queue.md` now links cited files the same way (no link changed). The
cost is size, almost all of it the URL: README.md grew from 99,377 to 120,440
bytes (+21%), README.zh-CN.md from 96,326 to 117,979 (+22%), and the 36 pattern
pages from 900,394 to 1,322,000 (+47%; the largest, overview, 118,534 to 175,946).
The link alone, without the date, would have been about 18% on README.md.

Two text signals about what a row says came with it, and neither is a finding.
A row with code, not TypeSafe AI's own, with no `notes` and an English summary
that names none of jev, typesafe, System One, choice, score, noul, decision and
confidence is listed in the review queue: 102 rows when it was added, 75 of
them the project's own GitHub description, 13 at ★1k+, led by langchain ("The
agent engineering platform.") and litellm; every one cites a file, which the
queue links. At over a hundred rows, a lint warning each would be noise, so
lint does not warn. A cited path naming a shadow or a dry run on a row without
`shadow-mode-only` is a lint warning instead: it matched one row, latitude-llm,
whose cited file is `jev-shadow-decision-provider.ts`. Official rows are left
out of the first signal because `official` is held to the vendor's own hosts,
so the row is about Jev whatever its summary says.

Since 2026-09-27 the README's "Measured, not claimed" section prints ten of the
independent measurement reports rather than all of them: first the picks of the
curated `measured` path in `collections.json`, in that path's order, then the
first of the others in list order, as each pattern shows its first ten. Every
report is on `docs/measured.md` and `docs/measured.zh-CN.md`, generated with
the READMEs, with every note and caveat tag. Printed whole, the 70 reports of
that day took 350 of the README's 1,442 lines, all of them ahead of "By
decision pattern", the section the README calls its primary index. README.md
went from 120,440 to 94,523 bytes and README.zh-CN.md from 117,979 to 93,454,
with the sections in the same order.

Since 2026-09-28 a `kind: benchmark` row may carry `measurement`: what its own
author measured, indexed field by field from the author's report. The task;
named datasets and comparators, as the author names them; kinds of metric
(`taxonomy.json` lists eleven, from accuracy to tokens); the main set's size
`n` where the report gives one number; the model string, which `lint` holds to
`compat.json`; the measurement's date `as_of`, required when the row has no
`published` because a measurement is of the model served that day; whether
per-item data is published and whether the protocol was fixed first; and
`direction`, the author's own conclusion about Jev for that task (favourable,
mixed, unfavourable or inconclusive), which every surface shows as
author-stated, not reproduced here. Nothing in it was measured here. Until
then, what a benchmark compared Jev with and on which dataset lived only in
summaries and notes, and the MCP server could find it only by free text.
`docs/benchmarks.md` and `docs/benchmarks.zh-CN.md` are generated from these
fields by `build_benchmarks.py`: decision patterns by stated direction, each
comparator and dataset with the rows that used it, and every measured row with
its star band, whether it is independent, whether raw data is published, its
caveat flags and its direction. `search_examples` gained `comparator`,
`dataset` and `direction` filters, and a measured row it returns carries its
`measurement`. `measurement.read_on` dates a person's reading of the report
against the fields; a measurement without it is listed in the
[review queue](review-queue.md#measurement-unread).

The fields were first filled in the same day, for the 25 benchmark rows with at
least five stars, by a model (the session that made this change) reading each
repository's README, results files, pull requests and linked reports with
read-only GitHub requests; no person has read them against the reports yet, so
none carries `read_on`. It recorded only what an author writes down: no `n`,
dataset or comparator it could not find stated, and a `direction` only where
the author concludes in words, which 17 of the 24 do. Seven state none (a
leaderboard, tables without a verdict, a show-and-tell), and legalforecastbench
was left without a measurement because its author withholds the Jev results. A
maintainer should spot-check all 24 against their reports:
hermes-agent-jev-evaluation, worldmonitor-shadow-mode,
no-mistakes-review-context, hippo-memory, ahastudio-til-jev-probing, jevbench,
jev-arena, windtunnel, jev-robot-control, typesafe-ai-benchmark,
jev-capability-atlas, smartmoney-cub, jev-benchmarks, jev-rag-benchmark,
pdf-race, jev-dspy-lab, jev-rerank-bench, jev-benchmark,
jev-korean-benchmark, jev-ood-calibration, jev-search-rerank-eval,
jev-code-review-benchmark, jev-little-airways and jev-phishing-bench. Three are
judgement calls. worldmonitor-shadow-mode is `unfavourable` because its author
kept Jev in shadow after it only tied the fixed labeller on 413 blind-judged
headlines (pull request 8326 in that repository); a later pre-registered
held-out NO-GO (pull request 8625) was still open and is not recorded.
jev-robot-control is `inconclusive` because its author calls its one seed-0
trial per controller "not success-rate estimates". ahastudio-til-jev-probing
summarises another author's API probing and states no direction. Benchmark
rows below five stars carry no measurement yet.

Since 2026-09-28 a negative result, a row whose own author measured Jev for
its use and concluded against it, is recorded in one place per row and found
the same way everywhere. A benchmark records it in `measurement.direction`
(`unfavourable`) and nowhere else; any other row carries the new
`negative-result` flag ("measured, not adopted"). `lint` fails the flag on a
benchmark, so a flag and a direction can never disagree, and without a `notes`
line naming a link, a pull request or issue number, or what was measured. One
predicate, `is_negative_result` in the MCP package's `query.py`, decides for
the READMEs, `docs/measured.md`, `docs/status.md` and the server; the site's
`isNegativeResult` is held to it on shared cases. The README's "Measured, not
claimed" and `docs/measured.md` now list negative results first, by star band
and title, never by the file's order, which is also how a plugin that dropped
a use reaches that section at all. `docs/status.md` lists them in a generated
block above its dated snapshot, which stays as written. The site gained a
`?neg=1` toggle and a badge; `search_examples(outcome="negative")` returns
them, rows flagged `shadow-mode-only` included, which a default search leaves
out; `list_patterns` counts them per pattern.

Of the seven rows the proposal named, reading each source the same day (a
model, as above) gave four negative results; a fifth row, outside the seven,
was found in the same reading.
hermes-agent-jev-evaluation, worldmonitor-shadow-mode and
no-mistakes-review-context are benchmarks whose authors conclude against Jev,
so their direction is `unfavourable`. hermes-jev-skills, a plugin, published a
handoff use it measured and dropped (its README: a handoff written from Jev's
digest recalled less than one written from the plain transcript) and got the
flag. So did the fifth, jev-skill-router, a plugin whose author ran it,
published that it is unlikely to help a strong model and keeps it in shadow
mode, with a `notes` line citing its README's measurements and the author's
write-up. ahastudio-til-jev-probing states no conclusion against Jev (it
summarises another author's probing), so it has no direction and is not a
negative result; nearhere-three-way-comparison's post answers only behind a
JavaScript challenge, so it was not read; jev-orderby-bench, below five stars
and mixed in its own words, was left for a person. A scan of every other
row's summary and notes for measurement words found no further row whose
author reports measuring and not adopting. No flag was set from a
reading of an author's numbers alone. The flag marks a whole row, not one use:
hermes-jev-skills keeps Jev for its other uses, and `list_patterns` counts it
as a negative result under every pattern the row files under.

Since 2026-09-28 a `kind: alternative` row may carry `wire`: what the project's
own files show about the interface it offers in place of Jev. Its route
(`endpoint`); the `type` its requests give the yes/no question
(`yesno_spelling`) and the keys a yes/no answer and a choice or score
confidence are read from (`answer_field`, `confidence_field`); whether state
and questions sit at the top of the request body (`envelope`); where its
answers come from in the default configuration (`weights`: `open`, a model you
can run yourself; `closed`, one only the project runs; `proxy`, another
provider's hosted model the server calls) and which model that is
(`base_model`); whether one of its files sends Jev the same requests to compare
(`calls_real_jev_as_baseline`, recorded only when true, since no string can
show a call is absent); where it publishes a comparison with Jev
(`comparison_url`); and the files all this was read in (`source`, up to four,
each a path and matched strings as `evidence` cites one). Until then the
catalogue said the same sentence about most alternatives, and a reader could
not tell the same route with the yes/no type spelt `boolean` from open weights
behind the same route, or a proxy in front of another provider's model, or a
project whose only link to Jev is an evaluation that calls it. `lint` allows
`wire` only on an alternative that carries the `not-jev` flag and a GitHub
repository, and requires every value copied out of a file (the endpoint's
path, the spellings and keys, the model) to sit inside one of the matched
strings, and a string naming Jev's own host or a gateway's id for Jev behind a
baseline call; the weekly `claims` run re-reads every cited file beside the
evidence files, so a value whose string disappears is reported. Nothing is
inferred: a field the files do not show is left out and printed as a dash.
`build_compat.py` generates `docs/compatibility.md` §7, "Compatible interfaces
that are not Jev", from these records alone: the *Weights* column on every
row, the `not-jev` caveat with the calibration sentence of its taxonomy blurb
on every row, the row's other caveats, whether a person has read the files,
and a count of the alternatives that record no interface. The site's
Compatibility view shows the same rows (`catalog-core.mjs` selects them, held
to `scripts/wire.py` on shared cases); `get_example` returns `wire` with the
row and `search_examples` leaves it out. `source` is a list where the
proposal named one object: a server's route, its request types and its default
model usually sit in different files (localjev's `src/server.ts`,
`src/types.ts` and `src/config.ts`), and one file would have left the
*Weights* column empty on most rows.

The records were first filled in the same day, for the 18 alternative rows with
at least 100 stars, by a model (the session that made this change) reading each
repository's server code with read-only GitHub requests; every matched string
was confirmed present at `HEAD` that day with `verify_claims.py --only`, and no
record carries `read_on`, so all 14 are in the review queue. Fourteen got a
record: laya-nandhakishorm, jaredpalmer-kev, nanojev, decider, jeff, localjev,
open-jev, open-jev-zefan-cai, openjev, openjev-siliconlabai, openjev-sglang,
rizzo-flow, simple-jev and von. Twelve serve `POST /v1/systemone` with the
yes/no type spelt `noul`; NanoJev serves `POST /api/evaluate` with `boolean`
and `p_true` inside a `{"states": [...]}` wrapper, and SiliconLabAI's OpenJev
serves `POST /api/evaluate` as a proxy to `gpt-4o-mini`. Six show a file that
sends Jev the same requests (laya, kev, NanoJev, simple-jev, openjev-sglang,
jeff). Four got none: openwork and deep-searcher offer no Jev-shaped
interface, and their only file about Jev calls Jev itself (a CI review script,
an evaluation of a stopping signal), so they look filed under `alternative`
for being an alternative to something else; semif is a command-line semantic
if with its own interface; jevlike is a trainable model with no server. A
maintainer should spot-check the fourteen and decide on the four. Judgement
calls: laya's `base_model` is its bundle repository, because its router picks
one of three checkpoints per request; kev, decider, Open-Jev and simple-jev
leave `base_model` out, their default being a local run path or a required
argument; jeff's and open-jev's is the checkpoint their default local directory
is named for (`models/gliformer-large-v1`, `models/gemma-3-4b-it`, which their
READMEs download from Hugging Face); razorback16/openjev's is its tokenizer
default, the repository its vLLM backend serves; simple-jev's baseline call
is its committed run record through OpenRouter; decider's notes say it calls the API as a baseline, but no
file read shows the call, so the field is left out. The alternatives below 100
stars carry no record yet; they are for a person, in the order discovery
brings them up.

## Discovery is crowdsourced, verification is not

There are dozens of Jev directories. Each is a different person's sweep of the
same ecosystem, so their union is a far better discovery surface than any single
one — including this one. `docs/sibling-lists.txt` names them, and
`scripts/discover_candidates.py` harvests them, ranks repositories by how many
cite each, and then reads the candidate's own code looking for a call site.

The two halves matter separately. Crowd agreement finds things: a repository
cited by twenty lists is worth looking at. Crowd agreement does not verify
anything: these lists copy from each other, so one miscataloguing propagates
everywhere. The most-starred "Jev visual inference tool" in this ecosystem
contains zero references to the API and is listed as a Jev project almost
universally.

So the script emits a shortlist with a verdict per candidate — `calls-jev` with
the file and strings that prove it, `mentions-only` when the README claims what
the code does not, or `no-signal`. A `calls-jev` verdict is not a catalog row.
Someone still reads it and writes the summary.

The first aggregation run harvested 32 lists, found 1,885 distinct repositories
cited, verified the 45 most-cited that were missing here, and added 34. Six were
`mentions-only` — including one cited by twenty lists — and four were dropped
because their only Jev reference was in a fixture named `fake_jev`, which proves
the request shape and nothing else.

Sibling lists that ship no licence can be used as pointers but not as prose: a
URL is a fact, a description is someone's writing. Rows discovered that way were
re-read at the call site and summarised independently.

Since 2026-09-27, who proposed a row is a caveat like any other. A row whose
`sources` include the fixed string `author submission` — the project's own
author or maintainer asked for it — carries the `self-submitted` flag, and
`lint.py` fails if either appears without the other. The flag is declared by
the submitter, never inferred: GitHub handles are rarely recorded and an owner
is often an organisation, and matching the wording of a note is guesswork. The
backfill therefore covered only rows already recorded as `author submission`.
Rows recorded as `maintainer submission` (this list's maintainer adding a row on
their own initiative) or `community submission` were not reclassified, so the
flag's absence is not evidence that a row was not self-submitted.

Since 2026-09-27, the script's verdicts are kept in git, in
`.discover/seen.json`, rather than only in the Actions cache. GitHub evicts a
cache nobody has read for seven days; discovery runs weekly, and its scheduled
start on 2026-09-24 came four and a half hours late, so one late or skipped run
would have lost every verdict, and the next issue would have proposed every
earlier candidate again as new. `discover` reads strangers' repositories and
holds no write permission, so it leaves the file as an artifact, and the weekly
`metadata` run commits it after checking every entry's shape (a lower-case
repository name, one of the script's verdicts, a date); the cache stays as the fast
path between commits, and the newer verdict for a repository wins. The file
says what it is: what a script found in the files it read, not a judgement
anyone made. `no-signal` does not mean a repository never calls Jev, and a
person's decision is still a row in `catalog.json` or a line in
`docs/declined.txt`. The same day the weekly issue became a task list: one box
per candidate, claimed with a comment, each with the command that re-reads
that one repository (`discover_candidates.py --only owner/name`), and the
candidates still waiting from earlier weeks are named instead of counted.

Since 2026-09-27, a candidate can start as a draft row:
`discover_candidates.py --drafts DIR` writes one per repository found calling
Jev, with what the script read filled in (the URL, GitHub's stars and licence,
the call site's path and the strings matched there) and the keyword rules'
kind and patterns labelled as guesses, and leaves the summaries,
`evidence.read_on` and, for a single `--only` read, `sources` to the person
who reads the code. A draft's first field, `_draft`, is what keeps it out of
the catalogue as it is: the schema knows no such field, and a rule of
`lint.py`'s own names it and says what is left to do. Nothing else is relied
on, since the schema accepts a one-character summary and does not require
`read_on`. The review card on the pull request that adds the row is the
second gate, and it matches text and compares facts; a maintainer still reads
the call site.

Since 2026-09-27, the discovery issue's description is the queue itself: every
repository the verdicts record as `calls-jev`, each shown as catalogued (a row
in `catalog.json` links to it), catalogued and since retired, declined (a line
in `docs/declined.txt`), or still to read. `scripts/queue_sync.py` derives
those states from the four files on every weekly run, and the same files
always give the same text, so the workflow rewrites the description only when
a state changed. No state is stored anywhere, and a person's decision still
comes only from the catalogue or the declined list, never from the verdict
file. Before this the issue was a thread of weekly comments whose boxes only
someone with write access could tick. One gap remains: a candidate catalogued
under a newer name than the one the sibling lists cite shows as still to read,
because the verdict file keeps the cited name.

Since 2026-09-27, which sibling directories cite a row is recorded on the row.
Until then 1,053 rows named one and the same source, the sibling-list
aggregate, while the harvest that knew which lists cited each repository kept
only the count, for the weekly issue, and dropped it. `scripts/sibling_lists.py`
now does the harvest for both scripts, and `scripts/attribute_sources.py`, run
weekly by `metadata` after the refresh, appends to every row with a GitHub
repository one `sources` item per list whose README links it:
`{"catalog": "owner/name", "url": "https://github.com/owner/name"}`, the list's
name and URL and nothing of its text, after the sources a person wrote and
sorted by URL. Those stay as they were and still say where the row was found;
`lint.py` holds the citations to that shape, that order and the lists
`docs/sibling-lists.txt` names. A list that does not answer keeps its
citations as last read, a list removed from the file loses them, a list never
cites its own row, and this repository's examples are cited by none. The
first read, on 2026-09-28, reached all 52 lines of the file and recorded 8,019
citations on 1,129 of the 1,136 rows whose repository is not this one; no list
links the other seven, and three of the lists link no catalogued repository.
The 52 lines are 50 directories: two had been renamed and were listed under
both names, and GitHub serves a renamed repository's README under its old name
too, so the first backfill counted them twice (250 citations, taken out the
same day). A README identical to an earlier line's now cites nothing, and
`docs/sibling-lists.txt` keeps each old name after the current one so that
discovery does not propose the directory itself. It is a
fact about the lists, and like a star count it measures attention: they copy
from each other, so the number says how widely a project is mentioned, not
that anyone checked it, and nothing here ranks, filters or flags a row by it.
`docs/status.md` counts rows by how many lists link them, `docs/sources.md`
gives the citations one line and each list a line of its own, the site shows
the count on each card and the lists in its details, and the weekly digest
counts the changes without naming a row, so they open no notice. A link is
matched on the repository name the list writes, so a list still linking a
renamed repository by its old name is not counted. The cost is size:
`catalog.json` grew from 1.78 MB to 2.77 MB and by 32,076 lines, about a sixth
once compressed.

### The bulk pass, and what it cost

A second aggregation run verified the 320 most-cited repositories missing here
and added 223. At that volume two standards had to bend, and both are recorded
in the data rather than hidden:

- **Summaries are the project's own description**, normalised, rather than a
  sentence written after reading the code. What _was_ read is the call site,
  and `evidence` on every row proves it.
- **Chinese is bulk-translated**, so those rows carry `zh_machine: true`. The
  counts script reports the split — 183 of 404 hand-written at the time of
  writing — because a catalogue that claimed all of them were would be lying
  about the one thing it sells.

Patterns were suggested by keyword rules over the description and then
reviewed. The review caught eight errors in 223, almost all of the same shape:
an SDK picking up a behavioural pattern from words describing its own API.
"Typed noul, choice and score" is an API surface, not content scoring;
"observable retries" is an HTTP client, not a retry decision. One was a plain
regex bug — `form\b` with no leading boundary matched "platform" and filed a
.NET SDK under document triage.

Since 2026-09-27, the rules' `tool-selection` test no longer counts "control",
"harness" or "screen" on their own, and counts "robot", "autonomous", "drive"
and "screen" only beside a word for deciding or acting ("decide", "decision",
"action", "step", "command", "move", "which", "next"). Every word in it now
starts at a word boundary: the old test had one on its first few words only,
the same kind of bug as `form\b`, so "control" matched "remote control" and a
content screener matched "screen". The rules moved to `scripts/classify.py`
and have their first tests. Replayed over the whole catalogue that day, with
each row's summary and title standing in for the GitHub description and
repository name the rules read at discovery (the catalogue keeps neither), the
old rules suggested `tool-selection` for 220 rows and the new ones for 133. The
suggestion changed for 87 rows, each by losing `tool-selection`. No kind
changed and no other suggested pattern was lost, though for 12 of them a
pattern the three-pattern cap had cut now shows in its place. 65 of those rows
carry `tool-selection` in `catalog.json`, and none was re-classified: whether a
project decides which action comes next is a reading, not a word count, and
some of them do — a Mario player that turns Jev's answers into controller
buttons says neither "decide" nor "action". They are listed, most-starred band
first, in the [review queue](review-queue.md#tool-selection-broad-words) for a
person to read. The rules suggested exactly a row's `patterns` for 818 rows
before the change and for 758 after it.

Since 2026-09-27, the catalogue shows which rows were never placed. `overview`
is for a row that surveys the model or the space, but it is also what the
keyword rules suggest when nothing matches, and the bulk passes took their
suggestion. That day 451 rows carried it, 351 of them exactly as the rules'
default before the change above (353 after it), and 252 were projects or
plugins with code — 251 of those with a cited call site, langchain's row ("The
agent engineering platform.") among them.
Nothing was inferred into `catalog.json`: whether anyone reviewed the patterns
of a row that matches the rules is not recorded, and a guess filed as a source
would be a claim nobody made. A new optional field, `patterns_reviewed`, records
the date a person read a row against the patterns; nobody has set it yet. Until
it is set, or the row gets a pattern, a project or plugin with code filed only
under `overview` is listed apart as *not yet indexed by pattern*: after the
other Overview rows in the READMEs, on the Overview page and on the site, and in
the [review queue](review-queue.md#unsorted-overview) with the rules'
suggestion, most-starred band first. The status page counts the rows whose
patterns equal the rules' suggestion for their summary as agreement with the
rules and nothing more, since any review of them was not recorded. Lint does
not warn per row: a warning repeated on hundreds of rows is a log nobody reads,
so the count is published instead.

`retry-control` went from zero to one genuine example, a semantic circuit
breaker that asks whether an HTTP 200 is a silent failure. The other apparent
matches were false positives and were removed. `recommendation` is still empty
across 32 lists and 1,887 repositories, which is now a reasonably strong claim
that nobody has published one.

Since 2026-09-27, every surface says whose words a summary is. The first
concession above was recorded here and nowhere in the data, and the generated
licence statement in `docs/sources.md` said the opposite: that every row being
`CC0-1.0` meant no descriptive text had been inherited. A row now carries
`summary_source: upstream-description` when its summary is identical to the
repository's own GitHub description — letter case, runs of whitespace and one
final full stop aside, nothing else forgiven — and `refresh_metadata.py` sets it
by comparing the two on every weekly run. The first comparison, run over the
whole catalogue that day with `--only-field summary_source` (which writes that
field and nothing else), labelled 890 summaries; every one is a row whose
Chinese was machine-translated. Of the other 121 such rows, 42 repositories
serve no description, two did not resolve, and 77 summaries differ from the
description GitHub serves now — edited here, cut short, or changed upstream
since; which, the data does not record. Eleven of those 77 are the opening
words of the current description, most cut at the length limit, so a person
can label them `upstream-description-stale`. That value is what the
refresh gives a labelled summary that stops matching, so the project's words
stay attributed after it rewrites its description. `curated` means a person
wrote the summary for this catalogue; the refresh never writes it and never
changes it. Nothing was reworded: rewriting 890 summaries in bulk would have put
text nobody reviewed in their place. `docs/sources.md` now counts the split and
says that the authors wrote those words and hold the copyright in them, and that
CC0 covers each row's structured metadata and the text written here. The
READMEs, the pattern pages and the site mark each such summary beside the
existing machine-translation mark; the MCP server returns the field with the
summary; lint warns about marketing words and emoji only in a summary marked
`curated`.

Since 2026-09-27, the machine translations are compared with their English, and
the ones most readers see are listed first for a person to replace. That day
1,011 of the 1,207 Chinese summaries were machine-translated (`zh_machine`).
Every Chinese surface marked them, the site's Chinese view since the change
above, but nothing looked at what they said. `scripts/zh_audit.py` applies three
rules to each: the Chinese has fewer than 30% as many characters as the English
(`short`; the median machine translation has 0.38); a number the English gives,
with digit groups joined, does not appear in the Chinese (`numbers`); more than
60% of the Chinese is ASCII (`ascii`). They flagged 284, 91 and 152 machine
translations, 457 in all. The same rules flagged 14, 1 and 16 of the 196
summaries a person wrote, 31 in all (tsai-sc's "1990s" is 90 年代), which is how
often they fire on a person's translation. Many hits on machine translations are
plain losses: jev-seo's Chinese drops "100% free ₹0", jev-phishing-bench's turns
"Claude Haiku 4.5" into "a lightweight LLM", jev-web-analyzer's leaves out that
it is "powered by ReplyNodes". Some are not: "Connect 4" is 四子棋 and "24/7" is
全天候. Names were tried as a fourth rule and dropped. A capitalised English word
missing from the Chinese flagged 839 machine translations and 121 of the
hand-written summaries, because every English sentence starts with one. A
name-like word missing from the Chinese, one with a capital after its first
letter or with letters and digits together (TypeSafe, MCP, OpenRouter, L1),
flagged about 490 machine translations and only 7 or 8 hand-written ones (the
counts move by a few with how the English is split into words), but about half
of those machine translations lacked nothing except "TypeSafe" or "AI" in a
sentence that still says Jev or 智能体: a translation style, not a loss. So no
row shows a signal. The READMEs,
the pattern pages and the site show only the (机翻) mark, which records who wrote
the words, and the generated [translation queue](zh-queue.md) lists every
machine translation on a row at ★100+ (82 that day, 17 of them at ★1k+), then
the other flagged ones, most-starred band first, capped at 200 with a count of
the rest. Only a person's own translation takes `zh_machine` off; one a model
wrote or drafted keeps it, however carefully edited, and says so in `notes`.
Nothing was re-translated: replacing 1,011 machine translations with another
model's would swap one unread text for another. Lint warns, and never fails,
when a change adds a row whose machine translation drops a number: a row whose
slug is not in `catalog.json` where the branch left the base the check runs with
(`lint.py --base`, which takes the merge base; `check.py` passes `HEAD^1` on a
pull request in CI and `origin/main` with `--fix`). Rows already filed are left
to the queue, since a warning repeated on hundreds of rows at every run is a log
nobody reads. The READMEs' "what is verified" section and `llms.txt` now give
the split, which only `docs/status.md` did before; the repository description
still says "EN/中文", unchanged.

### The long tail, 2026-09-22

A third run took the next 700 most-cited repositories and added 401, taking the
catalogue from 404 to 805. The median candidate was cited by two lists and had
two stars, so this pass is mostly the long tail rather than anything popular.
The same two concessions apply, and the same `zh_machine` flag records them.

Running at this size broke three things that had worked at 400 rows, all of
them in the machinery that keeps the catalogue honest rather than in the data:

- Two of the first three `path-gone` verdicts were transient fetch failures, not
  deleted files. The raw-file fetch now retries once before believing a miss.
- Scraping github.com HTML for link status hit its rate limit a few dozen rows
  in, so most GitHub rows never got stamped. Bare repository URLs now go through
  the authenticated API; paths inside a repository still go through HTTP,
  because the API answering for the repository says nothing about one file.
- The published repository description still said 148. It is the one claim
  that lives in GitHub's database rather than in git, so no build had ever
  checked it. It is checked now.

`recommendation` is still empty.

### The first weekly cycle, 2026-09-24

The scheduled jobs ran for the first time, and each surfaced something only
running could:

* The call-site re-read failed 18 of 721 claims a day after they were read.
  Fifteen call sites had moved in refactors; two repositories had been deleted
  and were retired with a reason; and one project had removed its Jev
  integration on purpose, with a published measurement of why. That row stayed
  as a negative result under a new `evidence_none` value, `removed-upstream`.
* Discovery proposed 80 candidates. Four were catalogued projects under an old
  or new name, which led to the weekly refresh following renames. Sixteen
  looked test-only; every one had a real call site the scanner missed —
  because it had no C or C++ at all, and read only files named after Jev.
  Both are fixed, and the language list is now checked against the schema.
* Of the 76 added, nine are reimplementations of the interface rather than
  Jev, including one with more stars than anything else found this week. The
  keyword classifier filed all nine as ordinary projects; each was corrected by
  hand.
* Four pull requests from outside contributors were merged after their claims
  were re-read against the code, and nineteen more sibling directories were
  added to the harvest.

### The second discovery batch, 2026-09-24

With 51 sibling directories instead of 32, the harvest cited 3,285 repositories,
2,368 of them uncatalogued. The 400 most-cited were read; 325 had a call site,
and 323 were added — taking the catalogue past 1,200.

* `recommendation`, empty since the first build, got its first example: a movie
  recommender that narrows 4,800 films by retrieval, then has Jev parse the
  request and choose from the shortlist. The absence recorded above was true
  for every list harvested at the time; it is not true any more.
* Twenty-two rows are reimplementations of the interface, among them wrappers
  that serve another vendor's model in Jev's API shape. The classifier again
  filed them as Jev projects.
* Independent measurements outside English arrived — Russian and Spanish
  calibration audits, and Brazil's national exam — which is the gap the status
  page lists as worth watching.
* The scanner learned two more places a call site hides: Google Apps Script
  (`.gs`), and extensionless CLI scripts named after Jev.
* Two candidates were declined with a reason in `docs/declined.txt`: an early
  copy of a catalogued project, and an account-pooling gateway.

## Why a status code is not a verdict

Every row's `link_status` says the URL answered. That is all it says. It does not
mean the code runs, the project is maintained, the benchmark is sound, or the
approach suits your system.

The distinction matters more here than in most catalogs, because this ecosystem
is days old. A repository can have four figures of stars, one commit, no licence
and a description written for a launch-week audience. Popularity and substance
have not had time to correlate. That is why `stars` is documented in the schema
as "a popularity signal, not a quality verdict", and why `single-commit`,
`no-license`, `archived` and `shadow-mode-only` exist as flags.

Since 2026-09-27, the READMEs and the pattern pages print `stars` as a band —
★10+, ★100+, ★1k+, ★10k+ or ★100k+, and nothing under 10 — and order rows by
band, then title, where they used to print and sort by the exact count. Counts
move every week, and every move rewrote generated lines for a precision no
reader of a list needs: the refresh of 2026-09-23 (b8bae37) changed 220 rows,
all of them stars only, and 1,134 lines each way in 32 generated files.
Replaying that refresh's two versions of `catalog.json` through today's
generators, exact counts change 1,152 lines each way in the same 32 files;
bands change 26 lines each way in 6 files: 24 for the 3 rows that crossed the
10-star floor, and the screenshot link in each README. `catalog.json`
keeps the exact count and still changes every week; the site and the MCP server
still show and sort by it, so inside a band their order can differ from the
README's. The README's link to the site screenshot still changes with any edit
to `catalog.json`, because the site it shows sorts by the exact count.
`scripts/tests/test_star_bands.py` moves every count inside its band on a copy
of the catalogue, runs every generator, and requires every generated file to
come out the same except that link.

Since 2026-09-27, the weekly refresh also records three facts GitHub states
about each row's repository, as it states them: `repo_created_at` and
`repo_pushed_at` (GitHub's `created_at` and `pushed_at`, UTC timestamps to the
second) and `repo_commits`, the default branch's commit count. Step 4 of the
pipeline above said creation dates and last pushes came from the API at the
first build; no field held them, so nothing a reader could see showed them, and
`single-commit` sat on two rows while nothing counted commits. The GraphQL
query now also asks for `createdAt`, `pushedAt` and the default
branch's `history.totalCount`; a row it leaves is read over REST, where the
count is the page number of the `rel="last"` link when asking for one commit
per page. Counting histories made a query of a hundred repositories take 9 to
10 seconds, at GitHub's 10-second limit for a GraphQL request, so a query now
asks about fifty (4.5 s on average, under 7 s at most that day). `--compare` read 101
rows and then 45 more (every ★10k+ row, every archived or single-commit row,
the eleven rows of one account whose repositories each hold one commit, and
one more such row) both ways: dates and counts agreed on every one. The first
run, with `--only-field repo_created_at --only-field repo_pushed_at
--only-field repo_commits` (those three fields and the `single-commit` flag,
which goes with the count, and nothing else), recorded them on 1,134 of the
1,136 rows with a GitHub repository (two did not resolve) in 23 GraphQL and 2
REST requests. 91 default branches had one commit: 90 rows gained `single-commit`,
and one lost it (jev-by-example, which has three now). None of the 91 has a
four-figure star count; the most-starred has 379. Every recorded last push
fell in September 2026; 1,036 of the repositories were created that month,
53 earlier in 2026 and 45 before it. From now on `single-commit` follows
`repo_commits` both ways, as `archived` follows GitHub's flag, and lint requires
the two to agree wherever a count is recorded; it needs no `notes` line, and its
description now states the count instead of guessing that maintenance is
unlikely. The digest counts a moved last push or commit count like a star count
and lists a flag that changed; a creation date that changes is listed too,
since GitHub keeps it through renames and transfers. None of the three is a
verdict: nothing derives "stale" or "maintained" from them, and
[vetting.md](vetting.md) still asks the reader to judge upkeep. The site's
entry details and the MCP server's rows show them; `docs/status.md` counts rows
per calendar month of the last push, absolute months rather than an age. The
READMEs and pattern pages do not print them: a last push moves every week, and
printing it would bring back the weekly rewrite the star bands above removed.

## Field precedence

When sources disagree:

1. The official raw Markdown docs win on anything about the model.
2. A platform's own docs win on how to reach the model through that platform.
3. The code at the call site wins over any prose describing it, including the
   project's own README.
4. The GitHub API wins over README badges.
5. Where a page's `<title>` and on-page heading differ, the heading a reader sees
   is used, and `notes` records the discrepancy.

## What was excluded

- **Content-farm and SEO rewrites of the launch announcement.** Dozens exist.
  Exclusion criterion: adds no observation of its own.
- **Press-release redistributions.** Many outlets carried the same wire copy.
- **Fabricated API documentation**, including the community site's own `/jev-api`
  page, whose request shape matches neither the official API nor that same
  site's other documentation.
- **Name collisions.** "JEV" is also Japanese encephalitis virus, a person's
  name, an Eve Online asset manager, a smart-camera vision framework, a Joomla
  component and several car models. Every candidate was checked for whether it
  genuinely concerns TypeSafe's model. All searching used qualifying terms;
  bare "JEV" returns mostly noise.
- **Claimed research papers.** There is no published paper for the training
  method. An unrelated 2023 paper abbreviates to the same four letters, and an
  arXiv link labelled as "the paper" is almost certainly that one.

## Known limits

- **Catalogue code and the live API were not executed as part of this review.**
  Treat all rows as untested by this repository, even when `code-untested` is
  absent. That flag is an additional caveat, not a complete testing-status
  field. Repository generation checks and package smoke tests validate this
  repository's tooling; they do not test the catalogued integrations against
  the live API.
- **Performance claims were not reproduced.** Rows repeating vendor benchmarks
  carry `vendor-reported`. Independent reports keep their authors' methods and
  limitations; inclusion does not turn those reports into our own reproduction.
- **Reddit produced nothing verifiable.** Four retrieval routes failed. There is
  no Reddit row, which is a gap rather than a judgement that none exists.
- **X/Twitter is barely represented**, for the same reason.
- **Video content was verified by metadata only.** Channel, title and existence
  were confirmed; the demonstrations inside were not reviewed, and the rows say
  so.
- **The ecosystem is far larger than this catalog.** Searching for the model
  alongside the vendor name returns repositories in the thousands. This is a
  curated subset chosen for being verifiable, not an enumeration. Nobody can
  enumerate it at this growth rate.
- **Star counts move hourly** and were true on 2026-09-22.

## Reproducing it

```bash
git clone https://github.com/kydlikebtc/awesome-jev
cd awesome-jev

python3 scripts/check.py         # every check lint runs, in lint's order; --list names them

# or one at a time:
python3 scripts/sort_catalog.py  # keep catalog.json and retired.json in slug order
python3 scripts/lint.py          # schema plus cross-entry invariants
python3 scripts/build_readme.py  # regenerate both READMEs, docs/by-pattern/ and docs/measured*.md
python3 scripts/counts.py        # coverage, with gaps marked, and every breakdown docs/shape.md publishes
python3 scripts/check_links.py   # sweep every URL, report only
python3 scripts/verify_claims.py # re-read every cited call site
python3 scripts/review_pr.py     # the review card for this branch's rows against origin/main
python3 scripts/build_assets.py  # regenerate the README figures
python3 scripts/build_compat.py  # regenerate the compatibility tables
python3 scripts/verify_compat.py # re-read each platform page for compat.json's strings
python3 scripts/lint_docs.py --simulate-model <version>  # rehearse a model release; writes nothing
python3 scripts/zh_audit.py      # the translation queue; --json: every machine translation measured
python3 scripts/build_benchmarks.py  # docs/benchmarks*.md, every benchmark's measurement side by side
python3 scripts/build_shape.py   # docs/shape*.md, the catalogue's shape as a dataset
python3 scripts/regenerate.py    # or: every generator above, in order
```

`refresh_metadata.py` and `check_links.py` need `GITHUB_TOKEN` set, and
`verify_claims.py` wants it — unauthenticated GitHub is 60 API requests an hour
and no GraphQL at all, which will not cover a full sweep. Locally,
`GITHUB_TOKEN=$(gh auth token)` does. `--discover` proposes
evidence for a row that has none; the proposal is a starting point for a
person, never written automatically.

`check_links.py --write` stamps `checked` and `link_status` on rows that
answered. It never retires a row: that needs a human-written reason.

Since 2026-09-27, `catalog.json` and `retired.json` are kept in slug order and
`lint.py` fails when either is not. The order carries no meaning: the figures
and docs only count rows, while the READMEs, pattern pages, site and MCP server
each sort for themselves, with slug now the last tie-break in every one of those
orders, so rows that tie on everything else (forks sharing a title and star
count) no longer fall back to their position in the file. The fixed order exists
only so that pull requests adding different rows insert at different places
instead of all appending at the end and conflicting.

Since 2026-09-28, the breakdowns `counts.py` prints (by pattern, kind,
language, platform, primitive, flag and declared licence) and the ones added
beside them — how rows reach Jev in five groups that partition the catalogue,
rows per star band for each kind, languages per decision pattern, the pattern
pairs most often filed together, and how the rows spread over their authors —
are computed by one function, `_stats.shape()`, and published on the generated
`docs/shape.md` and `docs/shape.zh-CN.md`. Until then `counts.py` tallied the
breakdowns itself, a second definition beside `_stats.py`, and they reached
nobody but a CI log, which `status.md` sent readers to. Stars are counted in
the README's bands, with the median as a band, because a quartile of exact
counts would move every week and a band is a popularity signal either way.
Authors are compared by display name without regard to case, and only
aggregate counts are published: 982 names on 1,089 rows that day, 15 of them
with three rows or more. The platform groups follow `compat.json`'s surfaces
rather than a bare "other than `typesafe-api`", which would have called
`claude-code`, `github` and `postgresql` gateways; and the page says what the
first group is: discovery does not tag `platforms`, so `typesafe-api` is what
a row records when nobody named another route.

Since 2026-09-28, the same page also sets the decision patterns against what
the catalogue records about their rows: TypeSafe AI's documentation pages,
the file a row cites by `evidence.kind` (a call site, a file speaking Jev's
request shape, only an example), independent reports (benchmarks not flagged
`vendor-reported`), negative results and rows citing no file. The counts are
the MCP server's own (`query.evidence_ladder()`, which `_stats.py` reads), so
`list_patterns` and the Pages API index (an `evidence` object per pattern),
`docs/shape.md` and a line at the top of every `docs/by-pattern/` page cannot
disagree. Every one says the counts are reports counted, not a verdict, and a
row counts in every column and under every pattern that applies. The column
first proposed for negative results would have counted a missing evidence file
(`evidence_none: removed-upstream`) and a row kept in shadow as measurements
that came out against Jev; it counts `query.is_negative_result()` instead, the
predicate every other surface uses, and "official documentation" means
`kind: official-docs`, not TypeSafe's SDKs. The table showed on its first day
that 23 independent reports were filed under `overview` alone, so no pattern
counts them for the decision they measured; the page says so, and re-filing
them is a person's reading.

Since 2026-09-28, the weekly `metadata` run also keeps a dated snapshot of the
catalogue's counts, `history/<UTC date>.json` (`scripts/snapshot_stats.py`),
written after every step that edits `catalog.json` and before the commit, so
each file is what that refresh committed: every number `_stats.compute()`
publishes, rows per kind, pattern, flag, language and declared licence, and
each row's slug, stars, licence and flags. Until then nothing kept what the
figures were a week earlier: each regeneration overwrote them, the week's
digest went with the runner, and `site/stats.json` is rebuilt at every deploy
and never committed. The files are generated data under a header that says
so, never read back into `catalog.json`; one is about 90 KB, a year of them
under 5 MB. There is no backfill: git's history of `catalog.json` before the
first snapshot is three days of bulk edits, and running today's definitions
over those commits would put numbers in `history/` that nobody published, so
the script also refuses a date before the newest snapshot. `docs/shape.md`
says since when it has been collecting and how many snapshots there are until
there are three, and shows a table of how the counts moved after that. The
proposal to count, in the same files, how many cited claims survive each week
was left for later: that result is `claims`' (a read-only workflow), and
carrying it here would need a second artifact hand-over like the discovery
verdicts'.

Since 2026-09-28, the questions that close the status page's dated snapshot
are a generated table rather than five bullets that never said where anything
stood. `watch.json` holds each question and how it is tracked; two are counted
from `catalog.json` (independent reports, with the directions their authors
state, and, as a proxy for the alternatives converging on one wire format,
the alternatives whose cited file matches `/v1/systemone`, which shows a shared
endpoint path and nothing about request shapes or calibration), one lists its
rows by hand (option-order sensitivity: no field records it, and a single
report is not a reproduction), and two are readings of the vendor's pages
(whether a paper is linked; whether the rate-limit warning is still there),
each with its date and whether a person or a model read it. The first
readings, on 2026-09-28, were a model's. A recent change is counted from the
snapshot before the newest in `history/`, or over the newest week of
`first_seen` dates until two snapshots hold the value, and names its dates: a
"last seven days" computed from the day the page was built would have been
wrong a week later without a byte changing, and changed the page every day
nothing else did. A `topics` field to tag rows by question was proposed and not
added: it would serve two rows.

Since 2026-09-27, `scripts/check.py` holds the one list of the checks `lint`
runs, in its order. The list used to be written out four times — in
`lint.yml`, in `CONTRIBUTING.md`, in the pull-request template and in the
weekly `metadata` refresh — and the copies had drifted: the contributor
instructions named a handful of the checks, so a pull request could pass them
and still fail `lint` on the unit tests, the site data or the curated
collections, and `metadata` pushed to `main` after only the generators and
four checks. Now `lint` runs `check.py --ci`; its `regenerate` job and
`metadata` run `check.py --ci --quick` — every check but the preview images,
which `pages` renders at deploy — on what they are about to commit; the
contributor instructions and the template name `check.py --fix`, which first
sorts the catalogue. A unit test fails if `lint.yml` runs a script the list
does not cover. Each check still runs even after an earlier one fails, so one
run shows every problem. Locally, a check whose tool is missing — Node.js for
the site's filter tests, Chrome for the preview images — is reported as
skipped, never as passed; in CI a missing tool fails the run. `metadata` now
commits on the runner first and runs the checks strictly against that commit
before pushing, so a regenerated file its `git add` left out would fail too.

Since 2026-09-27, every rule `lint.py` enforces is pinned by a unit test,
`scripts/tests/test_lint.py`: each test starts from a row that passes
everything, breaks one rule, and checks that lint reports exactly that one
finding in that rule's own words. Before, only the slug-order and
self-submission rules had tests, so any other rule written backwards would have
passed CI and let through every row it was meant to stop.
The same file holds the schema to what the validator actually does. `lint.py`
implements the part of JSON Schema the schema uses, and a keyword it does not
know (`oneOf`, `format: date`) is ignored rather than rejected, so a constraint
added to `schema/entry.schema.json` could look enforced while checking nothing.
The tests now fail when the schema uses a keyword, `format` or `type` outside
that part, until `validate()` implements it. What lint accepts and rejects did
not change.

Since 2026-09-27, the three weekly jobs that read GitHub (`links`, `claims`,
`metadata`) tell a rate limit from a refusal, keep what they read before one,
and say what they spent. Before, every 403 from the API ended the run — so one
repository GitHub blocks would have stopped the weekly refresh before it wrote
anything — while a 429 from the raw-file host counted as a deleted file, the
link sweep in `links` ran without a token, and `metadata` cut its sweep's
report to five lines, so how many links were stamped or refused was never
visible. GitHub documents the workflow token's budget as 1,000 REST requests an
hour per repository; yet the scheduled run on 2026-09-23 made over a thousand
authenticated requests in under two minutes, and the 734 repository reads at
the end of it met no limit. Rather than plan around either figure, every run
now records GitHub's `x-ratelimit-*` headers and writes what it spent and what
is left to its job summary.

- A rate limit (403 or 429 with `x-ratelimit-remaining: 0`, a `retry-after`, or
  "rate limit" in the message) is waited out once — at most 90 seconds, as
  GitHub asks — then that budget is closed for the run and the rows it would
  have read are counted as skipped, never as gone or failed. A budget with
  fewer than 50 requests left (a tenth, for a small one) is not spent further
  until it resets, leaving room for the job's own issue and dispatch calls.
  A 403 or 451 without those signals is a repository GitHub will not serve: one
  row, listed for a person, not the end of the run.
- `refresh_metadata.py` reads a hundred repositories per GraphQL query — about
  a dozen requests for the whole catalogue; fifty, about two dozen, once the
  query also counted each default branch's commits (see *Why a status code is
  not a verdict*) — and reads over REST any row the query did not answer.
  `--compare` reads rows both ways; on 203 rows (every `NOASSERTION` licence,
  every archived row, 40 unlicensed and 110 random) and two renamed
  repositories the two gave identical facts.
- `verify_claims.py` reads each cited file at `HEAD` on the raw-file host,
  which resolves to the default branch without an API request. That is
  observed behaviour, not documented, so only a pass is taken from it: a file
  missing or changed there is read again at the branch the API names, and that
  read is the one reported.
- `check_links.py` asks the API about bare repository URLs with a token in
  `links` too, and counts refusals (401, 403, 429) for GitHub and for other
  hosts apart. When more than a fifth of either group — of at least twenty
  URLs — refused, it exits 3 and says the sweep was rate limited or blocked
  rather than passing for a quiet week; dead links still exit 1. `metadata`
  keeps stamping through both, fails only if the sweep never reported, and
  keeps every row's verdict as a run artifact.
- `status.md` and `llms.txt` now give how many rows share the newest
  successful check date. The date alone read as if everything had been checked
  then, while seventy rows carried an older date or none.

## Kept current

Every figure this repository publishes changes for one of four reasons, and each
reason has its own mechanism. The rule underneath all of them: **a number may
appear only where something re-derives it.** Anything typed by hand froze at the
first build — the status page, the licence warning, the link-preview text, the
social card and the README screenshots all said 148 entries long after the
catalogue passed 800, and no build ever went red.

| What changes | When | Kept current by |
| --- | --- | --- |
| Counts and tables about the catalogue | Whenever a row is added or edited | Generated from `catalog.json` — the READMEs by `build_readme.py`, the figures by `build_assets.py`, the catalogue's shape (`docs/shape.md`) by `build_shape.py`, and every number inside the hand-written docs and `llms.txt` by `build_docs.py`. The site's link-preview tags are written into the Pages artifact at deploy by `assemble_site.py --deploy` and never committed. All numbers share one definition in `scripts/_stats.py`. `lint` regenerates all of them on every run (next row), and `lint_docs.py` rejects a catalogue count typed anywhere else. |
| Generated files after a merge | Whenever a pull request lands | A pull request need only change the sources. `lint` runs `regenerate.py` on every event, then `check_generated.py` decides: on a pull request each generated file must be untouched since the merge base or byte-identical to the regenerated output, with every verdict in the run's summary; on `main`, drift is handed to the `regenerate` job, which rebuilds from the tip, runs `lint`'s checks again and commits `chore: regenerate from catalog.json` as `github-actions[bot]` — rebasing if `main` moved, leaving a `regenerate/<sha>` branch if that no longer applies, never force-pushing. A dispatched or manual `lint` run is strict: any drift fails. |
| What each benchmark's author measured | When a person reads a benchmark's report | Recorded by hand in the row's `measurement` (`kind: benchmark` rows only). `lint` holds it to its rules and its model string to `compat.json`; `build_benchmarks.py` regenerates `docs/benchmarks.md` and its Chinese twin from it; a measurement without `read_on` stays in the review queue until a person reads the report against it. Every direction is the author's, shown as author-stated, not reproduced here. |
| The interface each `alternative` offers | When a person reads an alternative's files | Recorded by hand in the row's `wire` (`kind: alternative` rows with the `not-jev` flag only). `lint` holds every value copied out of a file to one of the matched strings in `wire.source` (`scripts/wire.py`); `build_compat.py` regenerates the table in `docs/compatibility.md` §7 and the site draws the same rows; `claims` re-reads every cited file weekly beside the evidence files, marked `wire.source`. A record no person has read (no `read_on` on some source) is listed in the [review queue](review-queue.md#wire-unread). |
| Which constants cited files compare Jev's answers with | When a person or a model reads a cited file for its thresholds | Recorded by hand in the row's `observed_thresholds` (since 2026-09-28), each item's `source` one of `evidence.matched`: `lint` holds each constant to that text and each quantity to what the primitive's answer carries (`scripts/thresholds.py`), and `claims` re-reads the text weekly with the rest of the evidence. `_stats` counts the rows and the lowest and highest constant per primitive and quantity, which `build_docs.py` writes into SKILL.md and examples/README.md; `lint_docs` rejects a range of thresholds typed anywhere else. Items without `read_on` keep their row in the [review queue](review-queue.md#thresholds-unread). Observations of what each project chose, never a recommendation. |
| Images that show data | Same | Rendered from the data on every Pages deploy by `render_images.py` and never committed: the site's `og:image`, and the README and compatibility screenshots. The deploy refuses to publish a page that did not finish loading its data, and (since 2026-10-24) renders nothing without a font that draws Chinese, which it installs first. |
| Files the site serves to agents | Same | Written into the Pages artifact at deploy by `assemble_site.py` and never committed: `retired.json`, the entry schema and `llms.txt` beside the page's own data, and under `api/v1/` an index plus one JSON file per decision pattern (`site_api.py`), each row shaped and ordered by the MCP server's own `query.py`. `check_site_data.py` refuses to publish a pattern file that differs from a rebuild or holds a different number of rows than `stats.json` counts for its pattern, and an index whose keys are not `patterns.json`'s. `llms.txt` is published with its values refilled from the same stats, so the site's copy never trails the data beside it. |
| The GitHub social preview | Never | It can only be uploaded by hand, so it is the durable card: its one figure is a floor ("800+") that growth can only make an understatement, never wrong. `description` reports whether one is uploaded. |
| The repository description | When the count crosses a hundred, or the wording changes | Only an admin can edit it, so it states the count floored to the hundred: `_stats.pitch_public()`, the same sentence as the site's `description` and `og:description`. The `description` workflow compares the whole sentence on every push to `main`; on drift it warns and keeps one open issue, labelled `description`, holding the exact `gh repo edit` command, instead of failing a build nobody but an admin can fix. `lint` prints the would-be sentence on every run, pull requests included. Every other surface — the READMEs, `status.md`, `llms.txt`, the figures — carries the exact count. |
| Labels for patterns, kinds and flags | When the taxonomy changes | One copy each, in `patterns.json` and `taxonomy.json`, read by the README generators and by the site at runtime. `lint` checks both against the schema; `lint_docs` checks `docs/patterns.md` and its Chinese rendering `docs/patterns.zh-CN.md` each have a section for each pattern, closing with the markers `build_docs.py` fills with its count and links (since 2026-09-28). |
| Which primitive fits a decision | When TypeSafe's documentation changes its guidance | One copy, `picker.json`, drawn by `build_assets.py` into the README figure under "What Jev returns" and read by the site's primitives view at runtime. Every step cites the docs.typesafe.ai page and heading it follows; `lint` (`scripts/picker.py`) holds it to that, to `patterns.json` and to the schema's primitives, and refuses a number or an answer field in its text. The counts beside a leaf come from `_stats.primitive_layers_by_pattern`. Nothing re-reads the vendor's pages on a schedule: a person who sees the guidance change edits the file. |
| Model strings and limits | When the vendor or a gateway ships | One source, `compat.json`. `lint_docs` checks every copy against it — in docs, examples, the generated README and figures, the MCP server's source, the plugin manifests, the issue forms, the prose the site and the server serve from `collections.json`, `patterns.json`, `taxonomy.json`, `picker.json` and the entry schema (since 2026-09-28), and `compat.json`'s own prose — and holds every hand-written link to a page whose address names a model version to the `docs_url` recorded there. Read from it rather than copied: the model names `verify_claims.py` and `discover_candidates.py` look for, the MCP server's `check_model_string` hint, and `docs/compatibility.md`'s tables and the date a person last read the pages (`as_of`). `claims` re-reads each platform's documentation weekly and opens an issue if a recorded string disappears, if a page names a newer model version than `compat.json` records, or if `as_of` is more than 45 days old; how old is said in the run's log and the issue, never in a committed file. `lint_docs.py --simulate-model` rehearses a release (below). |
| Which catalogued rows stand for each platform surface | Whenever a row's `platforms` or a surface in `compat.json` changes | Each surface in `compat.json` lists in `catalog_platforms` the values rows record for it; `taxonomy.json` lists in `platforms_without_surface` the values no surface claims. `lint` fails a row recording a value in neither, and a value two surfaces share unless both are marked `coarse`. The *Catalogued examples* column of `docs/compatibility.md` is generated by `build_compat.py` from `compat.json` and `catalog.json`, and the MCP server's `compatibility()` and `search_examples(platform=…)` apply the same rule (`query.py`); the site's platform filter applies its copy in `site/catalog-core.mjs`, which both test suites hold to `query.py` on one set of cases. |
| Link status, stars, licences, archive status, whether a summary is the repository's own description, creation date, last push and commit count (with `single-commit`), which sibling directories link each repository | Continuously, upstream | `metadata` weekly: stamps every link that answers, re-reads the GitHub API and every sibling directory's README, rebuilds everything generated, commits it, runs `lint`'s checks on that commit (`check.py --ci --quick`: all but the preview images, which `pages` renders), pushes to `main`, and redeploys the site. It opens an issue only for a change that is more than a star count, a last push, a commit count or a sibling-list citation, and falls back to a branch if `main` moved underneath it. `links` weekly is the separate alarm for a dead link, which only a person may retire, and for a sweep so refused by GitHub or by other hosts that it checked little; since 2026-10-24 it says so in one open issue, labelled `links`. Both jobs, and `claims`, write their counts and the GitHub budget they spent to the run's summary. The site shows the date of the sweep its figure comes from, and the status page how many rows share it. |
| Whether cited text is still present | Continuously, upstream | `claims` is scheduled weekly to fetch each `evidence` file and report missing strings or files. Counts show citations recorded, not CI passes, and the job does not update the human `read_on` date. A claim that lost only its pinned model version, from a file that names another, is `version-moved`: the issue counts those rows per version instead of listing each, and `verify_claims.py --propose-version-rewrite` prints each one's `evidence.matched` rewritten, for a person to apply without touching `read_on`. A `path-gone` file's line names, where one exists, a file in the same repository that still holds every matched string: a proposed path for a person to open. |
| Whether the scheduled jobs still run | Daily | `watchdog` (since 2026-10-24) asks the Actions API about every workflow with a schedule and keeps one issue, labelled `watchdog`, while any is disabled or has had no successful run in eight days; it rewrites the issue only when what it says changes and closes it when all are healthy. The jobs report through issues and commits, so one that stops says nothing; this is what hears that. |
| What the catalogue is missing | Continuously, upstream | `discover` weekly: harvests every sibling directory, reads the code of the most-cited uncatalogued repositories, searches for sibling directories not yet harvested, and keeps one issue: its description is the queue of every candidate, ticked or struck through from `catalog.json`, `retired.json` and `docs/declined.txt` (`queue_sync.py`), and each week's new candidates are a comment, a box per candidate to claim with the command that re-reads it. It never adds a row. Its verdicts are kept in `.discover/seen.json`, which `metadata` commits from `discover`'s artifact. |
| The open questions on the status page | Whenever a row is added or edited; a reading when a person re-reads its source | `build_watch.py` writes the table from `watch.json` and `catalog.json`, counting against the snapshot before the newest in `history/`. A reading carries its `as_of` and whether a person or a model made it, and changes only when someone edits `watch.json`. |
| What the published counts were on each weekly refresh | Weekly, from the first refresh after 2026-09-28 | `metadata` writes `history/<UTC date>.json` with `snapshot_stats.py` after the refresh and before its commit: generated data, never read back into `catalog.json`, never backfilled, never dated before the newest snapshot. `docs/shape.md` reads it for its trend table once there are three. |
| How many people reach the repository, and from where | Weekly, once a `TRAFFIC_TOKEN` secret exists | `metadata` writes `history/traffic/<UTC date>.json` with `snapshot_traffic.py` (since 2026-10-24): GitHub's own figures for the 14 days before the refresh, views and clones per day, the ten referrers and the ten paths it sees most. GitHub keeps no more than 14 days and the workflow token cannot read them, so without the secret nothing is kept. Successive files overlap; nothing reads them back, and no counter of this repository's own is added. |
| The MCP package on PyPI | When `pyproject.toml`'s version changes | A release is a tag a maintainer pushes, so PyPI can lag `main`. `check_release.py` compares the two on every push to `main`, in `lint`'s `release` job: a version not yet on PyPI is a warning carrying the tag command; a version older than PyPI's newest, or `pyproject.toml` and `.claude-plugin/plugin.json` disagreeing, fails. The file comparison also runs on every pull request, as a unit test. After an upload, `publish` installs the release back from PyPI. |
| Dated history | Never | This page's log sections are append-only and exempt from the number rules: what the first build found is true forever. |

- `lint` runs on every pull request, every push to `main`, and by hand; after
  a push to `main` it also commits the regenerated files and asks PyPI whether
  the MCP package's version is released, and on a pull request it writes the
  review card for the rows the pull request adds or changes. Its checks, and
  their order, are `scripts/check.py`'s list; `python3 scripts/check.py` runs
  them locally.
- `description` runs on every push to `main`, and by hand.
- `new-entry` runs when a new-entry issue is opened, and by hand on any issue:
  it reads the repository the issue names and comments a draft row
  (`draft_from_issue.py`), and only comments.
- `watchdog` runs daily, and by hand.
- `pages` rebuilds the site and its images whenever the data, the site or the
  rendering scripts change.
- `publish` builds and smoke-tests the MCP package on a pull request that
  changes the package (`src/`, `pyproject.toml` or the workflow itself), and
  uploads it only from a release tag, then installs that release back from
  PyPI. Since 2026-09-27 a pull request that changes only data no longer runs
  it: the wheel copies the data in verbatim, and `lint` already validates it.

Since 2026-09-27, the repository description and the site's meta description
state the catalogue size floored to the hundred rather than exactly, and the
description's drift opens an issue instead of failing `lint`. The exact count
made `main` red after every merged row, in the one check CI could never repair
— editing the description needs admin rights — until someone ran
`gh repo edit` by hand; a wording change alone did the same. A floor, like the
social preview's, stays true as the catalogue grows and goes stale once per
hundred rows. Until then the two surfaces show a smaller number than the
READMEs; that difference is deliberate, and the READMEs are the exact figure.

Since 2026-09-27, the site's link-preview tags (`description`, `og:*`,
`twitter:card`) are written into `site/index.html` only in the Pages artifact,
by `assemble_site.py --deploy`, from the same stats as the rest of the page.
Git keeps a placeholder between the `meta` markers. The tags quote the
catalogue size, so while `build_docs.py` kept them in git every pull request
that added a row also had to change the site's HTML. `check_site_data.py` holds
both ends: a committed file carrying anything but the placeholder fails `lint`,
and a deploy without current tags fails `pages` before anything is published.

Since 2026-09-27, `lint` checks on every push to `main` that the MCP
package's version is on PyPI (`check_release.py`). The package README, the
agent skill and `llms.txt` told everyone outside Claude Code to
`pip install awesome-jev-mcp`, and PyPI had never heard of it: `publish`
uploads only from a release tag, no tag had been pushed, and no check looked
at PyPI, so the documented route failed at its first step while every build
stayed green. A version not yet on PyPI is reported, not failed, because it is
the normal state between merging a version bump and pushing its tag, and only
a maintainer can push the tag; a version older than PyPI's newest fails,
because an uploaded version can never be uploaded again. An unreachable PyPI
is `skipped`. The same three documents now also give
`pip install git+https://github.com/kydlikebtc/awesome-jev`, which builds the
same package from the repository.

Since 2026-09-28, `lint` tests each decision the MCP server's tools make, on
every pull request. The filters, the order, the `limit` clamp, which flags keep
a row out by default, the caveats each result carries and the model-string
check moved out of `server.py`, the one file that needs the `mcp` package, into
`src/awesome_jev_mcp/query.py`, standard library only, where
`tests/test_mcp_query.py` tests them on a handful of made-up rows and a made-up
`compat.json`. `tests/test_mcp_data.py` walks `data.py`'s ladder (override,
checkout, GitHub with the cached ETags, cache, bundled snapshot) against a fake
GitHub: a 304 is served from the cache, one failed file discards the whole
fetch, and only the cache and the snapshot are labelled stale. Until then tests
reached the server only through `server.py` with `mcp` stubbed out, for
particular fields (caveats, evidence kind, summary source, the model-string
hint), and nothing tested the ladder. The move changed no answer:
every tool, called 3,224 ways on the catalogue of that day, returned the same
bytes before and after, and the real SDK registered the same tools with the
same schemas. `publish`'s smoke test now also asks that SDK, which nothing
else here installs, which tools it registered.

Since 2026-09-28, the Pages site also serves, from its own domain, what an
agent without the MCP server reads: `retired.json`, `schema/entry.schema.json`,
`llms.txt`, and under `api/v1/` an `index.json` and one file per decision
pattern (`api/v1/patterns/<key>.json`). Until then `catalog.json` was the only
way in — 2,773,876 bytes on that day, which no agent reads whole — and
`llms.txt`, the schema and `retired.json` answered only from
raw.githubusercontent.com, while `llms.txt` and the agent skill told agents to
read the catalogue directly. That day the index was 7 KB and the eighteen
pattern files ran from 1 KB (`recommendation`) to 231 KB (`overview`), median
23 KB. A row in them is exactly what the MCP server's `search_examples` returns
for it, in the same order: `assemble_site.py` loads the server's
`src/awesome_jev_mcp/query.py` by its path. Nothing is filtered: a pattern file
holds every row filed under its pattern, caveats attached, so its count is the
catalogue's, and it names the caveats (`not-jev`, `shadow-mode-only`) that mean
a row is not an example of deciding with Jev, which the server leaves out by
default. The only date in them is the catalogue's newest successful link check,
never the time of the build. `llms.txt` and the skill now give the Pages
addresses first and the raw ones as the fallback; the files under `api/` exist
only on Pages. A file missing there answers with the site's HTML 404 page, not
JSON: Pages has one 404 page per site.

Since 2026-09-28, the MCP server loads the same five files the site's page
does: `taxonomy.json` and `collections.json` joined `catalog.json`,
`compat.json` and `patterns.json` in `data.py`'s ladder, in the sdist and in
the wheel's bundled snapshot, and a test holds the server's list equal to
`assemble_site.py`'s. Until then a caveat reached an agent as a bare key such
as `code-untested`, whose meaning lived in `taxonomy.json`, which the server
never loaded, and the curated collections, each pick with an editorial
reason and caution, were invisible to it. Rows still carry the bare keys;
`search_examples` and `get_example` now end any answer holding flagged rows
with `caveat_glossary`, the English description of each flag among those rows
and of no other. Four resources serve the rest: `awesome-jev://flags`,
`awesome-jev://collections`, `awesome-jev://collections/{id}` and
`awesome-jev://patterns/{key}`, the last holding the same rows in the same
order as the site's `api/v1/patterns/<key>.json` (one function in
`query.py` builds both). The first fetch of a fresh install now asks GitHub
for five files rather than three, and a revalidation costs five 304s.

Since 2026-09-28, the server also offers one prompt, `wire_pattern(pattern,
language, surface)`, which puts into one message what a coding agent wiring a
decision would otherwise piece together from several calls, and a skeleton no
call returned: the pattern's description and a link to its section of
`docs/patterns.md`, where "when not to use" stays written by hand; the
surface's fields from `compat.json`; up to five rows under the pattern that are
examples of calling Jev and cite the file their code was read in, linked at
HEAD by the same rule as the site and the READMEs, with their caveats; and the
repository's own example for that pattern and language, under a comment saying
it was never executed, or a plain statement that there is none (every example
was Python that day). The examples reach an installed server through
`examples/index.json`, generated by `scripts/build_examples_index.py` from the
catalogue rows whose `evidence.path` is an example file and from the files
themselves; the server reads it by the same ladder as the catalogue, apart from
the five files and only when the prompt is first asked for, and names where it
came from. The link rule moved from `scripts/evidence_url.py` into
`src/awesome_jev_mcp/evidence_url.py`, which the script now loads by its path,
so there is still one copy.

Since 2026-09-28, `compat.json` and the catalogue name platforms in one
vocabulary. A row records in `platforms` how it reaches Jev, in the
catalogue's own words (`typesafe-api`, `vercel-ai-gateway`, `self-hosted`,
…); `compat.json` named its thirteen surfaces under ids of its own
(`typesafe-native`, `vercel-compat`, `cloudflare`, …), and only eight of those
ids were also a value some row recorded. So `docs/compatibility.md` could not
say whether any catalogued example used a surface, the site had no platform
filter, and the MCP server's `search_examples(platform=…)` matched a fragment
of a row's value: `vercel` matched both Vercel values, and `typesafe-native`,
the id `compatibility()` gives the direct API, matched nothing. Each surface
now lists in `catalog_platforms` the values that stand for it, and
`taxonomy.json` lists in `platforms_without_surface` the eighteen values no
surface claims: hosts, tools and frameworks an example runs in, and routes
`compat.json` does not describe, such as OpenCode Zen's hosted gateway and
jevai.org's separate API. `lint` fails a value in neither list, and a value
two surfaces share unless both are marked `granularity: "coarse"`. Four
surfaces are. Rows on Vercel's gateway record `vercel-ai-gateway`, not which of
its two routes (the evaluation API or the TypeSafe-compatible one) they take,
and the model string most of their cited files hold, `typesafe-ai/jev`, is the
same on both, so the file does not settle it either; rows using the AI SDK
record `vercel-ai-sdk` whether they go through the gateway or the
`@ai-sdk/typesafe-ai` provider; and `typesafe-api` is recorded both by rows
that call the native API and by rows that reach it through a pass-through
recorded beside it (Bifrost, OpenRouter, Vercel's compatible route). No row's
value was changed to a finer one: a finer value would be a guess its evidence
does not show. The last table of `docs/compatibility.md` gained a generated
*Catalogued examples* column that links each surface's rows on the site
(`?platform=<id>`); `compatibility()` gives the same count per surface; and
`search_examples(platform=…)` takes a surface id or a recorded value, matched
whole, says what it matched and whether coarsely, and answers anything else
with the valid ones. One function, in the MCP package's `query.py`, decides
what a platform matches for all three. The site's catalogue gained a platform
filter, `?platform=` in its address, taking a surface id or a recorded value by
the same rule in `site/catalog-core.mjs`, which both test suites hold to the
server's on one set of cases; its Compatibility view gained the same column.
`check_model_string` also gives, for a string `compat.json` records as wrong,
that entry's own reason.

Since 2026-09-27, a pull request no longer has to carry generated files, and
`lint` no longer fails a pull request because one is stale. Every pull request
that added a row used to change twenty-odd generated files, so any two open at
once conflicted, and each had to be brought up to date by hand before it could
merge. Now `lint` regenerates everything itself and judges each generated file
by event. On a pull request, a file the pull request did not touch may be
stale, since the bot rebuilds it after the merge; a file it did touch must be
exactly what the generators write, because anything else is a hand edit the bot
would silently overwrite. On `main`, the `regenerate` job commits the rebuilt
files, so `main` is behind its own sources for the minute between a merge and
that commit, and a dispatched `lint` run on `main` remains strict. This relaxes
the rule this section used to state as "`lint` fails on any drift": drift is
now repaired by a commit rather than refused at review. `.gitattributes` marks
the wholly generated files (both READMEs, `docs/by-pattern/`, `docs/assets/`)
`linguist-generated`, so GitHub collapses them in a pull request's diff; files
that are hand-written around generated blocks are not marked, because their
prose still needs reading.

Since 2026-09-28, each `docs/by-pattern/` page links its pattern's section of
`docs/patterns.md` and, before the full list, gives two short lists: what
TypeSafe AI publishes itself under the pattern (rows marked `official`) and
the examples this repository ships (rows citing a file under `examples/`, the
ones `examples/index.json` indexes), each row one line with its kind,
languages, primitives and caveat flags. Until then a page was a blurb and a
list, while how to model the decision lived on the patterns page, which linked
no pattern page: neither knew the other existed. The patterns page now closes
every `## key` section with a line `build_docs.py` writes between
`catalogued-<key>` markers: how many rows the catalogue files under the
pattern, the page listing them and the site's filter. `lint_docs` fails a
section without its markers, or with another pattern's. How to model each
decision stays hand-written on the patterns page and was not copied into
`patterns.json`: moving that prose into JSON strings would lose its links and
leave the page half generated.

Since 2026-09-28, the patterns page has a Chinese rendering,
`docs/patterns.zh-CN.md`, which the Chinese README and the Chinese pattern pages
link instead of the English page. A model wrote it from the English page, and
its first lines say so and that the English governs; no person had read it
when it landed. `lint_docs` holds it to the English page's rules: a `## key`
section for every pattern in `patterns.json`, each ending with its
`catalogued-<key>` markers, which `build_docs.py` fills in Chinese. Its model
strings and limits are checked against `compat.json` like any other page's,
and for that the limit rules gained the Chinese phrasings (`N 个选项`,
`N–M 级` or `N–M 个有序级别`, `Nk token` or `Nk 上下文`; written here without
the numbers, so this dated entry never has to change when a limit does),
which also read the limits where the Chinese README, the
Chinese overview page and the Chinese primitives figure already stated them;
each agreed with `compat.json`. The model-string rule no longer treats a
Chinese character as part of a word: Python's `\w` matches one, so a model
string written straight after Chinese text, with no space, was never read. No
page in the repository had one.

Since 2026-09-28 the README shows, under "What Jev returns", which primitive
fits a decision: TypeSafe's own guidance arranged as a decision list, kept in
`picker.json`. Each question is answered yes or no, and the first yes ends it:
an answer that is text to be written goes to a generative model, work code can
do exactly stays in code, a judgment resting on several independent things
becomes one question per thing, a checklist becomes one noul per item, a
spectrum whose points can be described is a score, a clean yes or no is a noul,
and one of a known set of options is a choice (with an other or none option
when the list may not cover every input); no to all means it is not yet one
snap judgment. Score and Noul are asked before Choice because a yes or no, and
a position on a spectrum, are also one of a known set of options, and the
vendor's Choice page opens by sending those to a Score and a Noul. Every
question and every answer cites the docs.typesafe.ai page and
heading it follows: the primitives page's "Choose a question type" and its
advice on splitting a complex judgment and on one snap judgment per question,
the Noul page's checklist advice and its advice on writing a question, the
Score page's on writing levels, the build guide's "Use code when you can", and
the limitations page's notes on generation and on a Choice being relative
where one Noul per option is absolute. Each page was read with a GET on
2026-09-28 and each heading found on the rendered page. The order of the
questions and their wording are this repository's arrangement, and the list
recommends no row; a model wrote it and its Chinese (`zh_machine`), and no
person had reviewed either when it landed. Beside a leaf that names a
primitive, the figure prints, for one pattern whose Shape on the patterns page
uses that primitive, how many rows a person read using it and how many only a
text signal shows (`_stats.primitive_layers_by_pattern`, the two layers the
primitives figure draws); the site's primitives view reads the same file and
the same counts from `stats.json`. `lint` refuses a step without a
docs.typesafe.ai source, an unknown pattern or primitive, a number or an answer
field in the text (limits live in `compat.json` and answer fields in the
primitives figure; a second copy would drift from them), and any shape the
figure cannot draw, and `build_assets.py` fails when a text no longer fits its
box. The versioned-link rule in `lint_docs` now reads a link to a heading of
the page `compat.json` records as that page, so the release rehearsal lists
`picker.json`'s links to the limitations page among the copies to edit.

Since 2026-09-28 a row may record, in `observed_thresholds`, the constants the
one file its `evidence` cites compares a Jev answer with: the primitive, which
quantity of its answer (a noul's probability, a choice's or a score's
confidence, one option's probability, a score's value), the constant, what the
code does on which side of it, and the text in the file that holds it
(`source`). Each `source` is also one of `evidence.matched`, so `claims`
re-reads it every week with the rest, and `lint` (`scripts/thresholds.py`)
requires the constant to be written in it, keeps the field off `not-jev` rows
and off this repository's own examples, and refuses a quantity the primitive's
answer does not carry. Until then the one number the docs gave, in SKILL.md and
in examples/README.md, was a range copied by hand from one row's notes, and
nothing would have noticed the row change. The first records were read by a
model, not a person, on 2026-09-28: a read-only GET of each of the 1,129 cited
files at HEAD (1,120 answered), a text search for a decimal on a line naming a
threshold, cutoff, gate, confidence or probability (334 files, 324 of them on
rows not flagged `not-jev`), then for a comparison with a decimal or a named
threshold constant (143 files), and a look at each hit in a few lines of
context, reading further in the files it recorded from. It recorded 55
constants on 33 rows, a first pass rather than every constant in those files:
only where the file itself, in its code or its own comment on the constant,
shows which answer's quantity the constant is compared with and what the code
then does, and not a check that a probability
lies between 0 and 1 or that probabilities sum to one, a test, a mock, a
benchmark's scoring or a report's filter, a score derived from several answers
or a posterior that blends an answer with a prior, or a file under an examples
or demos directory, and never more than the six
strings `evidence.matched` holds. Each of the 33 rows was then re-checked with
`verify_claims.py --only`, and every string was present at HEAD. None carries
`read_on`, so all 33 are listed in the review queue until a person reads them.
On review the next day (2026-09-29) the three recorded on jev-builder-loop were
removed with the matched strings added for them: its code compares those
constants with a posterior that blends a prior with Jev's probability, not with
Jev's answer. That leaves 52 constants on 32 rows.
A project that retunes a recorded constant turns its row's claim red in the
weekly `claims` issue, as any lost matched string does, and the weekly signal
step then drops the row's `primitives_seen` until a person updates the item and
its string. Inbox Zero's cited file is its API client, which holds no
threshold (its per-decision thresholds live in other files of that
repository), so it records none, and the docs no longer quote its notes'
range: SKILL.md and examples/README.md state the lowest and highest constant
recorded for a noul probability and for a choice confidence, as `build_docs.py`
inline values from `_stats`, never one range across both. SKILL.md now carries
those markers as HTML comments; how the Claude Code skill loader treats them
was not tested here, and the text reads the same with them left in, as
`llms.txt`'s does. `lint_docs` rejects a range of decimals typed into a
hand-written Markdown or text file. The evidence queue's single-model-name
signal ignores a threshold's `source`, which is text about a threshold, not
about the call. examples/04's two cutoffs stay constants, with a comment saying
they are unverified starting points. No page tabulates the thresholds yet:
`get_example` returns them with the row.

Since 2026-10-24, the scheduled jobs are watched, and the link sweep reports
like the others. `links` had only one way to say anything, a red run, and it
was red on each of its first four Mondays (2026-09-28 to 2026-10-19, 13 dead
links on the last) without anyone being told: nobody reads the Actions page of
a job that opens no issue. It now keeps one open issue, labelled `links`,
commented on with each week's dead links, redirects and, past the refusal
alarm, refused links (`check_links.py --markdown`), and its run is red only
when the sweep crashed before its counts. The new `watchdog` workflow asks
the Actions API once a day about every workflow with a `schedule:` trigger,
found by its file so a new one is watched from its first day, and keeps an
issue while any of them is disabled (GitHub turns a public repository's
schedules off after 60 days without activity) or has had no successful run in
eight days, a week and a day of slack for GitHub starting scheduled runs
late. Its body quotes dates rather than ages, so a quiet day changes nothing
and it can be rewritten only when the facts change; it closes the issue on
the first healthy day. Run on 2026-10-24, it reported only `links`, which had
never succeeded. It cannot report its own silence.

Since 2026-10-24, a `path-gone` claim in the weekly `claims` report comes with
a proposed path where one exists. 24 of the 66 failures of 2026-10-20 were
files missing from their default branch, most of them moved or renamed, and
each was a person's search through someone else's tree. For each one the
report now asks for the repository's file tree (one API call) and reads up to
twenty files on the raw host, the same file name first, then paths that
name the integration, then the same extension, until one holds every string
the claim matched; the line then names it. It is a proposal, not a fix: the
claim still fails, nothing is written, and a person opens the file before
changing `evidence.path`. Only the report searches. `--write-signals`,
`--propose-version-rewrite` and the pull-request review card read cited files
with the same function and spend nothing on it.

Since 2026-10-24, a new-entry issue is answered. The form had collected the
link, the summary and the primitives, and then waited for a person: issue #27
was opened on 2026-09-29, its row landed on 2026-10-24, and the issue never
heard back. The `new-entry` workflow now runs `draft_from_issue.py` when such
an issue is opened. It reads the repository with the discovery run's
`inspect()` and comments the call site it found and a draft row, built by
`discover_drafts.draft_row` from GitHub and that file, with the form's title,
summary, ticked primitives (only from someone who said they read the call
site) and the flags its boxes name exactly, the issue as its source, and a
`_draft` field listing what each came from and what a person still checks;
`lint.py` refuses the row until that field is deleted. A repository already
catalogued, retired or declined is told which row, or why; for one that was
catalogued, a form saying it is the author's own project and a row without
`self-submitted` is pointed out. The workflow holds `contents: read` and
`issues: write`: anyone can open an issue, so it commits nothing and opens no
pull request, and the issue's own text appears only inside the JSON block.
The pull request template now leads with the checklist a row needs and folds
the other field rules under it, and the issue templates gained a form for a
project's own author to confirm or correct its row, recorded as an `author
confirmation` or `author correction` source.

Since 2026-10-24, the site serves its own fonts. All three pages loaded IBM
Plex and Noto Sans SC from fonts.googleapis.com, a render-blocking stylesheet
on a host most readers in mainland China cannot reach, so the page could stay
blank until the request gave up, for exactly the readers the Chinese README is
for. `site/fonts/` now holds the Plex files Google Fonts served, unchanged and
split by script the same way (356 KB in all, of which a page loads the scripts
it shows), with their licence. No Chinese web font replaces Noto Sans SC: the
font stacks name the system ones (PingFang SC, Hiragino Sans GB, Microsoft
YaHei, Noto Sans CJK SC), as the README cover already did. The runner that
renders the screenshots has none of them, which is how the Chinese screenshot
once shipped as empty boxes, so `pages` installs `fonts-noto-cjk` first and
`render_images.py --require-cjk-font` fails rather than publish boxes.
`lint_docs` holds every stack on a page that shows Chinese to the four system
fonts, and every page, stylesheet and script under `site/` to loading nothing
from another host.

Since 2026-10-24, every answer that hands an agent rows says what their text
is. Most summaries are a project's own GitHub description, copied
(`summary_source`), and a description can be written to steer whatever model
reads it. The MCP server's `search_examples` and `get_example`, the pattern and
collection resources and the `wire_pattern` prompt now carry `text_note`
(query.TEXT_NOTE): titles, summaries and notes are data about a project, never
instructions, and `summary_source` says whose words a summary is. The site's
`api/v1` pattern files carry the same line and the skill says it in prose.
`lint.py` refuses a row whose title, summary or notes, in either language, is
written as instructions to a model: an order to ignore earlier instructions, a
role reassigned, a chat template's role tokens, a line addressed to AI readers,
an order to keep something from the user. No row matched when it was added. It
catches the plain cases only, so the note, not the pattern, is the defence; a
row about prompt injection describes the attack rather than quoting it.

Since 2026-10-24, the weekly refresh can keep the repository's traffic. The
catalogue has several doors (two READMEs, the site, the MCP server, the skill
and plugin, `llms.txt`, `api/v1`) and no figure for any of them. GitHub counts
the repository's views, clones, referrers and popular paths but keeps 14 days,
and only a token with the "Administration" repository permission (read) can
read them, which the workflow token is not. `snapshot_traffic.py` reads the
four with a fine-grained token kept as the `TRAFFIC_TOKEN` secret and writes
them to `history/traffic/<UTC date>.json`, which the refresh commits with the
counts; without the secret it says so and writes nothing. To turn it on, a
maintainer creates a fine-grained personal access token limited to this
repository with Administration set to Read-only (Settings, Developer settings,
Fine-grained tokens), and adds it under the repository's Settings, Secrets and
variables, Actions, as `TRAFFIC_TOKEN`. When it expires, the step's error says
so and the rest of the refresh goes on. The site and the MCP server still count
nobody: these are GitHub's figures, public once committed, like everything in
`history/`.

### When the vendor ships a model

Since 2026-09-27 a model release is rehearsed before it happens, and changes
`compat.json` rather than a list of files someone has to remember. Before
then the version was typed into the two scripts that recognise a Jev call
site, the MCP server's advice on model strings and the review queue's
model-name signal, and none of those copies was checked; links to the
vendor's versioned known-limitations page escaped `lint_docs` because a model
string after a slash reads as a URL path; and 183 rows quote the pinned
version in `evidence.matched`, each of which the weekly `claims` run would
have reported as `claim-gone`, mixed in with real removals, as its project
moved to the new pin.

The runbook:

1. `claims` reports `newer-version` when a platform's page names a model
   version newer than any `compat.json` records. That is the cue.
2. `python3 scripts/lint_docs.py --simulate-model <that version>` builds the
   `compat.json` a maintainer would write — the newest recorded version
   replaced in every model cell and `docs_url`, at the precision it was
   written in — runs `lint_docs`'s checks against it with
   `docs/compatibility.md` regenerated from it, and writes nothing. It lists
   each copy that would go red, what follows `compat.json` with nothing to
   edit, and what the catalogue will do. Run on 2026-09-27 for the next
   minor version, 1.14.0, it listed 14 findings in 12 files: the issue form's and two docs' links to
   the known-limitations page; `llms.txt` and the agent skill naming
   OpenRouter's versioned string; `docs/compatibility.md`'s hand-written
   table of common mistakes; the two explanations in `compat.json`'s
   `not_model_strings`; and both READMEs and three pattern pages, through
   three catalogue rows whose summaries quote the versioned id
   (`typesafe-models`, `jev-demo`, `typesafe-ai-jev-example`).
3. A person reads each platform's page and edits `compat.json`: the model
   cells, `docs_url`, the prose the rehearsal names, and `as_of` to the day
   of that reading. Whether the old version stays listed while the vendor
   still serves it is their call; keeping it keeps rows describing a
   measurement on it valid, which a person would otherwise reword. Then fix
   the files listed and run `python3 scripts/check.py`.
4. Over the following weeks, as projects move their pin, `claims` counts the
   rows whose cited file names another version ("N rows now pin X") and
   `python3 scripts/verify_claims.py --propose-version-rewrite` prints their
   rewritten strings. A person applies them in one pull request and leaves
   `read_on` alone: rewriting a string is not reading the call site.
   `version-moved` is a classification, not a verdict: a project may move its
   pin and drop the integration in the same commit, which only reading the
   file shows.

A pinned version `compat.json` does not list yet still counts as a Jev
signal when a script reads a stranger's code, so a mistake in `compat.json`
cannot hide a file that pins a real version.
