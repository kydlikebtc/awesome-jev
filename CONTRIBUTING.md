# Contributing

This catalog is built around traceable sources and explicit limits. A submission
should say what you inspected and what remains unknown. A link, a code reading,
a text-matching check and a successful API run are different kinds of evidence;
do not present one as another.

So the bar is: **could a reader act on this row without opening the link?**

## Adding an entry

1. Add an object to `catalog.json`. Required fields: `slug`, `title`,
   `summary`, `summary_zh`, `url`, `kind`, `patterns`, `sources`, `license`.
   The file is kept in `slug` order, so add the row anywhere and let the
   next step move it into place (`sort_catalog.py`, which changes nothing
   else). A sorted file is what lets two pull requests adding different rows
   merge without conflicting.
2. Run the checks:

```bash
python3 scripts/check.py --fix
```

   That one command sorts `catalog.json`, then runs every check CI runs, in
   CI's order, and ends with one line per check. A check that needs Node.js or
   Chrome is reported as skipped where that is not installed; CI runs it.
3. Open a pull request. `catalog.json` alone is enough. The template's first
   checklist is what a row needs; the rest of the field rules are folded
   under it, for the fields your row uses beyond those.

Or open the [Add an entry](https://github.com/kydlikebtc/awesome-jev/issues/new?template=new-entry.yml)
form instead. When the issue opens, the `new-entry` workflow
(`scripts/draft_from_issue.py`) reads the repository it names, with the code
the weekly discovery run uses, and replies with what it found: the call site
and the strings it matched, and a draft row built from GitHub, that file and
the form's answers. The draft's first field, `_draft`, lists what a person
still has to check, and `lint.py` refuses the row until it is gone. A
repository already catalogued, retired or declined gets a reply saying which
row, or why. The workflow only comments: it commits nothing and opens no pull
request, since anyone can open an issue. Complete the draft yourself, or leave
it for a maintainer.

### Generated files are optional

The READMEs, the pages under `docs/by-pattern/`,
[`docs/measured.md`](docs/measured.md) and `docs/measured.zh-CN.md`,
[`docs/benchmarks.md`](docs/benchmarks.md) and `docs/benchmarks.zh-CN.md`,
[`docs/shape.md`](docs/shape.md) and `docs/shape.zh-CN.md`, the
figures in `docs/assets/`, [`docs/review-queue.md`](docs/review-queue.md),
[`docs/zh-queue.md`](docs/zh-queue.md), `examples/index.json` and the
generated numbers in `docs/status.md`, `docs/sources.md`, `docs/patterns.md`,
`docs/patterns.zh-CN.md`, `docs/compatibility.md` and `llms.txt` are all derived from the JSON files at
the root (the index from the example files too). You do not need to
regenerate them. CI regenerates everything on every run, and after your pull
request is merged, `github-actions[bot]`
commits the regenerated files to `main` as `chore: regenerate from
catalog.json`. Leaving them out also keeps two pull requests that add
different rows from conflicting over the generated files. `history/` is
different again: dated snapshots of the counts that only the weekly refresh
writes (`scripts/snapshot_stats.py`), never edited or added by hand, so leave
it out of a pull request.

If you do include a generated file, it must be exactly what the generators
write. CI checks each generated file your pull request changes, and lists the
verdict for every one in the run's summary. A hand edit fails, because the bot
would silently overwrite it on `main`. To change what a generated file says,
change `catalog.json` or the generator in `scripts/`.

`check.py --fix` regenerates them in your working tree, as CI does, and then
judges them as CI judges a pull request against `origin/main`: a generated
file your branch changed must be exactly what the generators write, and one it
left alone may be stale. Commit what it rewrote, or leave it out. If your
remote for this repository has another name, say so with
`--base upstream/main`.

The same list of checks, run other ways:

```bash
python3 scripts/check.py --list    # every check in order, and what each needs
python3 scripts/check.py --quick   # without the preview images (Chrome), the PyPI check and the review card
python3 scripts/check.py --only lint,lint-docs   # just these checks
python3 scripts/check.py           # strict: every generated file committed and current
```

No Python dependencies are needed, only Python 3.11 or newer (CI uses 3.12).
The schema validator in `scripts/lint.py` is self-contained: it implements the
part of JSON Schema that `schema/entry.schema.json` uses, and a unit test fails
if the schema starts using a keyword it does not enforce, so implement that in
`validate()` first.

To preview the site locally:

```bash
python3 scripts/assemble_site.py && python3 -m http.server --directory site
```

A local preview has no link-preview tags: `site/index.html` keeps a
placeholder in git, and only the Pages deploy (`assemble_site.py --deploy`)
writes them. The same command writes the files the site serves to agents —
`site/api/v1/`, one JSON file per decision pattern, and copies of
`retired.json`, the schema and `llms.txt` — which, like every other file it
writes, are never committed.

### The review card

When CI runs on your pull request, `lint`'s `review` job writes a review card
to the run's summary (open the `lint` run from the pull request's checks, then
**Summary**) and marks each finding on its row's line in `catalog.json` under
**Files changed**. For each row you added, and for each changed field one of
its checks reads, it:

- reads the cited file and checks every `evidence.matched` string is in it, as
  the weekly `claims` job will, and that a row with `question_types`, or with
  code in a GitHub repository, cites a file or says in `evidence_none` why it
  cannot;
- asks GitHub about the repository: `repo_license` and the `archived` flag must
  match exactly, `stars` only has to be close (within 5, or a tenth of GitHub's
  count) because it moves every day, and a repository with one commit should
  carry `single-commit`;
- requests the link and expects a 2xx answer;
- compares your GitHub login with the repository's owner and the row's
  `author.handle` and `author.url`: a match without `self-submitted` is marked.
  An organisation's repository escapes this comparison, so the template's
  checkbox still counts;
- checks that `ai-generated`, `unverified-claims` and `code-untested` come with
  a `notes` line;
- and, as a hint only, says which kind and patterns the keyword rules that
  `discover` uses (`scripts/classify.py`) would have guessed from your summary.

✗ is for you to fix before merging, ⚠ for a person to look at, ℹ is a hint,
and *not checked* is not a pass. The card is advisory while it is new: it never
fails the check. It is a second gate that matches text and compares facts with
GitHub; it is not a review, and it does not replace a maintainer, who still
reads the call site: strings present in a file do not show that the code calls
Jev the way the row says, and a clean card is not an approval.

The card runs the base branch's copy of `scripts/`, not your pull request's,
so a pull request that edits the checks is still judged by the ones on `main`.
On a first pull request it runs only after a maintainer clicks **Approve and
run** (see *How changes reach `main`*). To see the same card before you push:

```bash
GITHUB_TOKEN=$(gh auth token) python3 scripts/review_pr.py --author <your GitHub login>
```

It compares your branch with `origin/main` (`--base upstream/main` if your
remote has another name), and `--offline` leaves out everything that reads the
network. `python3 scripts/check.py` runs it too, without an author.

## How changes reach `main`

Every change lands through a pull request, the maintainer's own included.
Maintainers and agent sessions (Claude, Codex and the like) push a `claude/*`
or `codex/*` branch and open a pull request from it, and do not push to `main`
directly. The only commits made straight to `main` are the two bots':
`github-actions[bot]`'s weekly `metadata` refresh and `lint`'s `regenerate`
job. Neither ever force-pushes `main`; when it moves underneath one of them,
the bot rebases or leaves its commit on a branch.

GitHub may hold the checks on your first pull request here until a maintainer
clicks **Approve and run**. That is GitHub's safeguard for first-time
contributors to a repository, not a verdict on your change, and it stops once
you have had a pull request merged.

## Numbers in prose

Never type a catalogue count into a doc. Every one that was typed by hand froze
at the first build and quietly became wrong. Either reword the sentence without
the number, or let `build_docs.py` fill it:

```markdown
In all, <!--n:no_licence-->141<!--/n--> linked projects declare no licence.
```

The keys are in `inline_values()` in `scripts/build_docs.py`. Put a word before
the marker — a line that *starts* with `<!--` is a raw HTML block in Markdown
and splits the sentence in two. `lint_docs.py` rejects bare counts, hand-written
count tables and line-leading markers. Dated history in `docs/method.md` is
exempt: a log entry about the first build is true forever.

A range of thresholds typed into a doc ("from 0.x to 0.y", with digits) is
rejected the same way. State what catalogued files use with the `threshold_…` inline values,
which `_stats` computes from the rows' `observed_thresholds`.

Model strings and limits are held to `compat.json` the same way: write
`jev-latest` or `max 255` anywhere and `lint_docs.py` checks it against that
file — in the docs, the MCP server's source, the plugin manifests and the prose
in `collections.json`, `patterns.json`, `taxonomy.json`, `picker.json` and the
schema alike. A link to a vendor page whose address names a model version (the
known limitations page) must be the one `compat.json` records as that
platform's `docs_url`. If the vendor changes one, change `compat.json` and
every stale copy turns red. Before a release,
`python3 scripts/lint_docs.py --simulate-model <version>` lists what would
turn red, and writes nothing (the runbook is in
[`docs/method.md`](docs/method.md#when-the-vendor-ships-a-model)).

## Field rules

- **`title`** — as published at the source. If the page's `<title>` and its
  on-page heading disagree, use the heading a reader sees, and say so in `notes`.
- **`summary`** — what the example _actually demonstrates_, not what its README
  claims. "Routes support tickets with a choice and a score" beats "revolutionary
  AI-powered triage". On a row with code, say what the project asks Jev to
  decide: a project's own GitHub description rarely does, and a row with code
  whose summary names nothing about Jev and that has no `notes` is listed in
  the [review queue](docs/review-queue.md#generic-summary) (TypeSafe AI's own
  rows aside).
- **`summary_source`** — whose words `summary` is. Wrote it yourself? Set
  `curated`; lint then warns about marketing words and emoji in it. Pasted the
  repository's own GitHub description? Leave the field out: the weekly refresh
  compares the two and sets `upstream-description` when they are identical, and
  `upstream-description-stale` once a labelled one stops matching. Never write
  `upstream-description` for a text that differs. Rewriting a summary labelled
  with either upstream value? Set `curated`, or the refresh will call your
  words the project's old ones. The READMEs, pattern pages and site mark the
  project's own words, and [`docs/sources.md`](docs/sources.md#licences) says
  why: the copyright in them is the project author's, not this catalogue's.
- **`summary_zh`** — write it yourself if you can. If a model translated it,
  set `zh_machine: true`, and keep it after you edit the model's text: the flag
  records who wrote the words, not how good they are (see
  [Claim a translation](#claim-a-translation)). The READMEs report the split.
  This field describes translation provenance, not code quality or runtime
  testing. On a row you add with `zh_machine: true`, `check.py --fix` (and CI
  on your pull request) warns when the Chinese leaves out a number the English
  gives. The warning never fails the build; it is a text comparison, and a
  number that does not belong in the Chinese can stay out.
- **`kind`** — the form of the thing. Use `alternative` for anything that does
  not call Jev, however Jev-shaped it is.
- **`patterns`** — which decisions it demonstrates. Read
  [`docs/patterns.md`](docs/patterns.md) first. `overview` cannot be combined
  with a specific pattern; the linter enforces that. `overview` is for a row
  that surveys the model or the space, not for a project nobody has placed: a
  project or plugin with code filed only under `overview` is listed as *not
  yet indexed by pattern* until someone reads it.
- **`patterns_reviewed`** — the date you read the row against
  [`docs/patterns.md`](docs/patterns.md) and set or confirmed its `patterns`.
  Only a person writes it: never because the keyword rules agree, and never
  for a row you did not read. It takes the row off the *not yet indexed by
  pattern* list and off the pattern sections of
  [`docs/review-queue.md`](docs/review-queue.md).
- **`question_types`** — only the primitives the code _actually_ calls. Read the
  call site; do not infer from the README. Several projects describe "scoring"
  while using only `noul`. The primitive is `noul`, never `binary`.
- **`primitives_seen`** — leave it out; the weekly `metadata` run writes it
  (`python3 scripts/verify_claims.py --write-signals`). It lists the primitives
  whose request or answer shape — `"type": "choice"`, `Noul(`, `.noul` and the
  like — appears in the one file `evidence` cites: a text signal about that
  file, not a reading of the call. It never stands in for `question_types`: no
  filter, count or lint rule reads it as a primitive claim, and a shape in a
  file (a type definition, a test double) is not a call. Lint allows it only on
  a row with `evidence`.
- **`observed_thresholds`** — optional: the constants the one file `evidence`
  cites compares a Jev answer with. Each item names the primitive
  (`question_type`), the answer's quantity it is compared with (`compares`:
  a `noul`'s `probability`, a `choice`'s or `score`'s `confidence`, one
  option's `probability`, or a `score`'s value as `score`; a `noul` answer
  carries a probability alone), the constant (`value`), what the code does on
  which side of it in eighty characters (`decision`: `at or above: …`,
  `below: …`), and `source`, the text in the file that holds the constant,
  copied exactly — a named constant's definition or the comparison itself.
  Add that `source` to `evidence.matched` too (at most six strings): lint
  requires it there, and the weekly `claims` run then re-reads it, so a
  project that moves its threshold turns the claim red. Record only a constant
  that decides something about a Jev answer itself — not a range check, a
  test, a mock, a score derived from several answers or a posterior that
  blends an answer with a prior — and never on a `not-jev` row or on this
  repository's own examples. Set `read_on` on each item you read yourself;
  without it the row is listed in the
  [review queue](docs/review-queue.md#thresholds-unread). It records what that
  project chose, not a recommendation, and a `noul` probability is never a
  `choice` confidence.
- **`platforms`** — how the code reaches Jev, in the values the catalogue
  already uses: one that a surface in [`compat.json`](compat.json) lists in its
  `catalog_platforms` (`typesafe-api`, `vercel-ai-gateway`,
  `cloudflare-workers-ai`, …), or one that [`taxonomy.json`](taxonomy.json)
  lists in `platforms_without_surface` (a host, tool or framework the example
  runs in, such as `self-hosted`, `claude-code` or `mcp`, or a route
  `compat.json` does not describe). Record what the cited file shows and no
  more: a project on Vercel's gateway is `vercel-ai-gateway` whichever of the
  gateway's routes it takes, and that is why those surfaces are marked
  `granularity: "coarse"`. `lint.py` fails any other value; a new one goes, in
  the same pull request, into the `catalog_platforms` of the surface
  `compat.json` describes for that route, or into the list. The *Catalogued
  examples* column of [`docs/compatibility.md`](docs/compatibility.md), the
  site's platform filter and the MCP server's
  `search_examples(platform=…)` all read this join.
- **`evidence`** — the file you read the row's code in (for a row with
  `question_types`, the file you read that claim in), and strings from it that
  substantiate it. This is what makes the claim re-checkable rather than
  asserted, so a weekly job can notice when it stops being true. Let the
  discoverer propose one and then check it yourself:

  ```bash
  python3 scripts/verify_claims.py --discover --only <slug>
  python3 scripts/verify_claims.py --only <slug>
  ```

  Prefer the implementation over a test file: tests get deleted while features
  stay, and a mocked string is weaker proof than a real call site. When the
  source is a docs page, a video or a paywalled post, set `evidence_none`
  instead and say which; when the repository's code neither calls Jev nor
  speaks its request shape (a reimplementation with its own interface, tooling
  about Jev), `no-jev-call-site`. A link holding no code at all, such as a list
  of links or a community site, gets `has_code: false` rather than either. Set
  `read_on` to the date you actually read that file; do not advance it after an
  automated text check. When the weekly claims issue counts a row as
  `version-moved` (its file now names another model version),
  `python3 scripts/verify_claims.py --propose-version-rewrite --only <slug>`
  prints `matched` rewritten to the file as it reads; apply it and leave
  `read_on` as it is. An `evidence` record is a
  citation, not a stored CI pass or proof that the integration executes. The
  READMEs, the pattern pages and the site link the file at `HEAD` with the
  `read_on` date beside it (the pattern pages also print the path), so a wrong
  path is visible to every reader.
  `evidence.kind` says what the file shows: leave it out (or write
  `call-site`) when the project calls Jev there; write `wire-shape` when it only
  speaks Jev's request shape — lint requires this on every `alternative` — and
  `example-only` when the call is in an example the project ships rather than in
  its own code. Rows a script marks for a person to re-read (a file under
  `examples/`, a citation resting on one model name, a `tool-selection` that
  only words the keyword rules no longer count suggested) are listed in
  [`docs/review-queue.md`](docs/review-queue.md); each section there says what
  to record to take a row off.
  `lint.py` fails a row with `question_types`, and a row with `has_code: true`
  whose `url` or `repo` is a GitHub repository, when it has neither `evidence`
  nor `evidence_none`; `not-yet-backfilled` is an honest value while you look.
- **`official`** — true only for `typesafe.ai` hosts and the `typesafe-ai`
  GitHub org. A first-party integration published by another vendor is not
  official. The linter checks this.
- **`stars`**, **`repo_license`** — from the GitHub API on the date you add the
  row, not from a README badge. Several repos have a licence badge and no
  `LICENSE` file; that gets the `no-license` flag. The READMEs and pattern
  pages print only the band a count falls in (★10+, ★100+, …, nothing under
  10) and sort by it; the exact number stays in the row, and the weekly
  refresh keeps it current.
- **`repo_created_at`**, **`repo_pushed_at`**, **`repo_commits`** — leave them
  out; the weekly `metadata` run records them from the GitHub API
  (`scripts/refresh_metadata.py`): when the repository was created, when
  anything was last pushed to it (UTC timestamps as GitHub states them) and how
  many commits its default branch has. They are GitHub's facts, not a
  judgement of upkeep, and the READMEs do not print them (the site and the MCP
  server do). The same run adds `single-commit` when the count is 1 and removes
  it when it is more, and lint fails a row whose flag and recorded count
  disagree, or that carries these fields without a GitHub repository.
- **`measurement`** — on a `kind: benchmark` row only (`lint.py` fails it
  anywhere else): what the row's own author measured, indexed from their
  report. `task` is required, a short English phrase; everything else only as
  the report states it: `report` (the results file, pull request or write-up,
  when that is not the row's `url`), `datasets` and `comparators` as the author
  names them, `metrics` (the kinds in `taxonomy.json` `measurement_metrics`),
  `n` (only when the report gives one number for its main set), `model_string`
  (the one sent, or the version the author says answered; `lint.py` fails a
  string `compat.json` does not list, so leave it out then), `as_of` (the
  measurement's date; required when the row has no `published`), `raw_data`,
  `preregistered`, and `direction`: the author's own conclusion about Jev for
  that task (`favourable`, `mixed`, `unfavourable`, `inconclusive`), left out
  unless the author states it in words. Every surface shows a direction as
  author-stated, not reproduced here; `unfavourable` makes the row a negative
  result. Never infer a number, a dataset or a direction. Set `read_on` to the
  day you read the report against every field; a measurement without it was
  filled in by a script or a model, and
  [`docs/review-queue.md`](docs/review-queue.md#measurement-unread) lists it.
  [`docs/benchmarks.md`](docs/benchmarks.md) is generated from these fields.
- **`wire`** — on a `kind: alternative` row with the `not-jev` flag only
  (`lint.py` fails it anywhere else): what the project's own files show about
  the interface it offers in place of Jev. Read the files and record only what
  they show: `endpoint` (method and path, e.g. `POST /v1/systemone`),
  `yesno_spelling` (the `type` its yes/no question takes), `answer_field` and
  `confidence_field` (the keys a yes/no answer and a choice or score confidence
  are read from), `envelope` (`top-level` or `wrapped`), `weights` (`open`: a
  model you can run yourself; `closed`: one only the project runs; `proxy`:
  another provider's hosted model the server calls), `base_model` (as the file
  names it; leave it out when the default names no model, such as a local
  run directory or a required argument), `calls_real_jev_as_baseline` (only
  `true`, when a file sends Jev the same requests to compare), `comparison_url`
  (where the project publishes a comparison with Jev), and `source`: each
  file you read, as a `path` and the `matched` strings that back the fields
  read from it. `lint.py` fails a copied
  value (the endpoint's path, the spellings and keys, the model) that is in
  none of the matched strings, and a baseline call without a string naming
  `api.typesafe.ai` or a gateway's id for Jev; the weekly `claims` run re-reads
  every cited file. Never infer a field. Set `read_on` on a source to the day
  you read that file against the fields; a record without it was filled in by
  a script or a model, and
  [`docs/review-queue.md`](docs/review-queue.md#wire-unread) lists it.
  [`docs/compatibility.md`](docs/compatibility.md#7-compatible-interfaces-that-are-not-jev)
  §7 is generated from these fields.
- **`sources`** — at least one, so the row is attributable. Name where you found
  it, not where it lives. Two fixed strings name submissions made directly to
  this repository, and they mean different things:
  - `author submission` — the project's own author or maintainer proposed the
    row. Use it for your own project, with the pull request or issue as `url`.
    The row must then also carry the `self-submitted` flag; `lint.py` fails if
    either appears without the other.
  - `maintainer submission` — this list's maintainer added the row on their own
    initiative. It says nothing about who wrote the project and is not a
    self-submission, unless the maintainer is also that project's author, in
    which case it is an `author submission` like any other.

  Two more record what a project's author said about a row someone else
  proposed (see [If the project is yours](#if-the-project-is-yours)), with
  their issue or pull request as `url` and a `notes` sentence saying so:
  `author correction` when their words changed the row, `author confirmation`
  when they confirmed it as written. Neither makes the row a self-submission.

  After the sources you write, the weekly refresh
  (`scripts/attribute_sources.py`) appends one item per sibling directory in
  `docs/sibling-lists.txt` whose README links the row's repository:
  `{"catalog": "owner/name", "url": "https://github.com/owner/name"}`, the
  list's name and URL, sorted by URL. Leave those to it: do not add, edit or
  copy them into a new row. That shape is reserved: if you found the row in
  one of those directories, name it in words (`"heyjunpenn's awesome-jev"`,
  with its URL), or it is read as a citation. `lint.py` fails a row whose
  citations are out of order, come before a source you wrote, are all it has,
  or name a list the file does not;
  `python3 scripts/attribute_sources.py --offline --write` puts them right
  without reading anything.

## Flags are the point

Use them generously. A flagged row is more useful than an unflagged one.

| Flag                                     | Use when                                        |
| ---------------------------------------- | ----------------------------------------------- |
| `vendor-reported`                        | it repeats the vendor's own performance numbers |
| `unverified-claims`                      | it makes measurement claims you could not check |
| `not-jev`                                | it does not call Jev at all                     |
| `shadow-mode-only`                       | Jev is wired in but changes no behaviour        |
| `code-untested`                          | you read the code but did not run it            |
| `single-commit`                          | one commit; the weekly refresh keeps it current |
| `no-license`                             | no `LICENSE` file, whatever the README says     |
| `archived`                               | development visibly stopped                     |
| `paywalled`, `marketing`, `ai-generated` | as they say                                     |
| `early-access-required`                  | needs waitlist access to use                    |
| `third-party-api-key`                    | needs a key for a service other than TypeSafe   |
| `self-submitted`                         | its own author or maintainer proposed the row   |
| `negative-result`                        | its author measured Jev here and did not adopt it (not on a benchmark) |

`ai-generated`, `unverified-claims` and `code-untested` require a `notes` line
saying why — a flag a reader cannot interpret is worse than no flag.

Lint warns when the path `evidence` cites names a shadow or a dry run and the
row lacks `shadow-mode-only`: read the call, and add the flag if nothing it
returns reaches a decision.

`negative-result` ("measured, not adopted") marks a row whose own author
measured Jev for its use and concluded against it: did not adopt it, or removed
it. Set it only when the author's own write-up, pull request or results say so,
never from your own reading of their numbers. A `kind: benchmark` row records
the same thing in `measurement.direction` (`unfavourable`) instead, and
`lint.py` fails the flag on a benchmark, so the two can never disagree. It also
fails the flag without a `notes` line naming a link, a pull request or issue
number, or what was measured. Every surface derives "negative result" from
either and lists those rows first; they are the ones to read before the
positive examples.

`self-submitted` is a disclosure, not a defect: every surface shows it so a
reader knows the description came from the project's side. It is declared,
never guessed — it goes with an `author submission` source and nothing else.
Older rows recorded as `maintainer submission` or `community submission` have
not been classified, so a row without the flag is not a statement that nobody
self-submitted it.

All catalogue code is **untested by this repository by default**, including rows
without `code-untested`. That flag adds a caveat; its absence must never be used
as a passed-test signal. Upstream benchmark results belong to their authors and
have not been independently reproduced here. A future runtime-verification claim
needs a dated report with the source revision, environment, model version and
result; neither `checked` nor `evidence.read_on` is a substitute.

## If the project is yours

A row is written from a project's code and pages by someone who did not write
them. If you did, you know best whether it is right.

- **Confirm or correct it** with the
  [Confirm or correct your own project's entry](https://github.com/kydlikebtc/awesome-jev/issues/new?template=confirm-entry.yml)
  form. A maintainer checks what you say against the code, applies it, and
  records where it came from: a source `{"catalog": "author correction",
  "url": <the issue>}` when your words changed the row, or `author
  confirmation` when you confirmed it as written, and a `notes` sentence
  ("Confirmed by its maintainer in issue #…"). The row does not take the
  `self-submitted` flag, since you did not propose it, and `evidence.read_on`
  still dates a reading here, not yours.
- **Show that it is listed**, if you like, with the badge the site serves,
  linked to your row (its `slug` is the part after `#` in its address on the
  site):

  ```markdown
  [![Listed in awesome-jev](https://kydlikebtc.github.io/awesome-jev/badge.svg)](https://kydlikebtc.github.io/awesome-jev/#your-slug)
  ```

  It is a static image with no counter, and it says the project is
  catalogued, nothing about its quality.
- **Have it removed** with the
  [Report a problem with an entry](https://github.com/kydlikebtc/awesome-jev/issues/new?template=entry-problem.yml)
  form ("This is my project and I want it removed").

Nobody here asks authors to add the badge or to confirm their rows: both are
for an author who comes looking.

## What does not belong here

- **Anything you have not opened.** Including anything an AI tool suggested and
  you did not check. Fabricated entries are the failure mode this catalog is
  built to avoid.
- **A model string, package name or endpoint you have not seen in a primary
  source.** `typesafe/jev-1` is the canonical example: it appears in no
  documentation and keeps getting repeated.
- **Content-farm rewrites of the launch announcement.** There are hundreds. If it
  adds no observation of its own, it adds nothing here.
- **"Run Jev locally" content filed as a Jev tutorial.** There are no published
  weights. File it as `alternative` with `not-jev`.
- **Your own project, described the way you would describe it to an investor.**
  Self-submissions are welcome; marketing copy is not. Say what decision it makes
  and which primitive it uses, record the source as `author submission`, add the
  `self-submitted` flag, and tick the box in the pull request template.

## Finding things to add

The weekly `discover` workflow does this for you and keeps an open issue
labelled `discovery`. Its description is the queue: every repository the run
has found calling Jev, ticked once `catalog.json` has its row, struck through
once `docs/declined.txt` declines it, and otherwise waiting to be read.
`scripts/queue_sync.py` derives those states from `catalog.json`,
`retired.json`, `docs/declined.txt` and `.discover/seen.json`, and the weekly
run rewrites the description with them, so nobody ticks a box by hand: merging
the pull request that adds the row or the decline is what ticks it. Those
waiting to be read come strongest first, by GitHub's figures from the weekly
refresh (`.discover/facts.json`): most stars, then most commits, then the
latest push. A candidate weak on at least two counts (one commit or none, no
star, no README) is listed apart as parked. That is not a decline: read one if
you like, and it moves back once a refresh finds it stronger. Each
week's new candidates arrive as a comment, a task list with one box per
repository, its call site, and under it the command that reads that one
repository again:

```bash
python3 scripts/discover_candidates.py --only owner/name
```

To take one, comment `claim owner/name` on the issue, so two people do not
read the same code; the first comment wins, and nothing arbitrates beyond
that. Then read the call site and add the row as described above. Candidates
from earlier weeks that are still neither catalogued nor declined are listed by
name under the new ones.

To start the row from what the script already knows, add `--drafts drafts`:

```bash
python3 scripts/discover_candidates.py --only owner/name --drafts drafts
```

That also writes `drafts/<slug>.json`, a draft row: the URL, GitHub's stars
and licence, the call site's path and the strings matched there, and the
keyword rules' guess at `kind` and `patterns` are filled in; `summary`,
`summary_zh` and `evidence.read_on` are left for you, and so is `sources`,
since a single read cannot know where you found the repository. Its first
field, `_draft`, lists what is left to do. Read the call site, complete the
row, delete `_draft`, and move the row into `catalog.json`. `drafts/` is
ignored by git, and the command never writes over a draft that is already
there.

`lint.py` refuses any row that still has a `_draft` field, and that is the
only thing that keeps a draft out as it is. Do not count on anything else to
catch an unfinished one: an empty `summary` fails, but a one-word summary
passes, and `read_on` is optional. The review card on your pull request is a
second gate that compares facts and matches text; neither it nor lint reads
the code for you.

To run the whole harvest by hand:

```bash
python3 scripts/discover_candidates.py --top 40
```

This harvests every list in `docs/sibling-lists.txt`, ranks repositories by how
many cite each, and reads the candidate's code before reporting. A `calls-jev`
verdict means a call site was found — it is a shortlist, not a row. Read it,
write the summary yourself, and keep the evidence path the scan produced.
`verify_claims.py --discover` is for rows already in `catalog.json`; for a
candidate it finds nothing to read.

Read one and decided it does not belong? Add it to `docs/declined.txt` with a
reason, and the weekly run stops proposing it.

The script's own verdicts (which repositories it read, on what date, and what
it found in the files it read) are kept in `.discover/seen.json`, so the weekly
run does not read the same code again until a verdict is old (`RECHECK_DAYS` in
`scripts/discover_seen.py`) and does not propose a candidate twice. The weekly
`metadata` run commits that file; do not edit it by hand. It records a script's
verdicts, not anyone's decision: yours goes in `catalog.json` or
`docs/declined.txt`.

Know a directory we are not harvesting? Add it to `docs/sibling-lists.txt`.
That is a useful contribution on its own: the weekly refresh then also records
which catalogued rows it links. Removing a line? Run
`python3 scripts/attribute_sources.py --offline --write` in the same pull
request, or lint fails on the citations of the list you removed.

## Claim a translation

Most Chinese summaries were translated in bulk by a model and carry
`zh_machine: true`; the Chinese README and pattern pages and the site's
Chinese view mark each one *(机翻)*. [`docs/zh-queue.md`](docs/zh-queue.md)
lists them for a person to replace: first every one on a row at ★100+, the
rows most readers see, then the others a script flags, most-starred band
first. The flags
(`short`, `numbers`, `ascii`) are text comparisons between the Chinese and the
English made by `scripts/zh_audit.py`. They point at likely losses; they are
not verdicts, and a translation nothing flags can still be wrong.

To take some:

1. Pick about ten from the top of the queue and open a draft pull request
   naming their slugs, so two people do not translate the same rows. A
   reviewer who reads both languages can check ten summaries against their
   English; nobody can check a hundred.
2. For each row, read the English summary and, where it is unclear, the
   project, then write the Chinese yourself: every number, name and limit the
   English gives, and nothing it does not. Change `summary_zh`, `zh_machine`
   and, as below, `notes`/`notes_zh`; nothing else. If the English is wrong
   too, fix it in a separate pull request.
3. Only a translation you wrote yourself takes the flag off: delete
   `zh_machine`. A translation a model wrote or drafted is still a machine
   translation, however carefully you corrected it: keep `zh_machine: true`
   and add a sentence to `notes` (and to `notes_zh`, if the row has one)
   saying a model translated the Chinese, and who checked it against the
   English, and when. The *(机翻)* mark stays, because it says who wrote the
   words.
4. Run `python3 scripts/check.py --fix` and mark the pull request ready. After
   the merge the bot regenerates the queue, and a row whose `zh_machine` is
   gone leaves it.

Please do not re-translate rows in bulk with a model. That swaps one unread
machine translation for another, the rows keep their flag, and the queue's
signals stop pointing at anything.

## Reporting a dead link

Open an issue with the slug. Do not delete the row — retiring an entry means
moving it to `retired.json` with a `notes` line explaining why, so the dead
reference stays searchable. `retired.json` is kept in slug order too, so run
`python3 scripts/check.py --fix` after moving it; it sorts both files.
`scripts/check_links.py` finds them but deliberately never moves them; that
judgement is a person's.

## Updating what the status page watches

[`watch.json`](watch.json) holds the open questions at the end of
[`docs/status.md`](docs/status.md) and how each is tracked. A question with a
`signal` of `independent-reports` or `alternatives-matching` is counted from
`catalog.json`, so nothing needs editing when rows change. A `listed-rows` item
names its rows by slug, since no field records the topic: add a row there when
it belongs, and the generator fails if a listed slug leaves `catalog.json`. A
`manual` item is a reading of one source (`url`): when you re-read it, update
`status_en` and `status_zh`, set `as_of` to the day you read it, and set
`checked_by` to `person` (`model` marks a reading no person has confirmed).
Keep the English and Chinese in step, and mark model-written Chinese with
`zh_machine`. `scripts/build_watch.py` regenerates the table; like every
generated file, it may be left to the bot.

## Editing the primitive picker

[`picker.json`](picker.json) is TypeSafe's own guidance on which primitive fits
a decision, arranged as a decision list: the README draws it under "What Jev
returns" (`scripts/build_assets.py`) and the site's primitives view reads it.
It is the vendor's design guidance, not this catalogue's advice, so every node
and every leaf names in `source_url` the docs.typesafe.ai page, and heading,
it follows: change a step only when that page says so, and point it at the
page you read. Each node asks one yes/no question; yes ends at a leaf, no
moves to the next node, and the last node's no ends at a leaf. A leaf may name
a `primitive` and the `pattern_key` of a pattern whose **Shape** in
`docs/patterns.md` uses it; beside it the figure and the site print how many
of that pattern's rows a person read using the primitive and how many only a
text signal shows. Write no number, limit or answer field (`probabilities`,
`confidence`, `legend`) in any text: those live in `compat.json` and the
primitives figure. Keep the English and Chinese in step, and leave
`zh_machine` true while a model's Chinese is unreviewed. `lint.py` fails on a
step without a docs.typesafe.ai source, an unknown pattern or primitive, a
number in the text or a shape the figure cannot draw, and `build_assets.py`
fails when a text no longer fits its box. A link to the versioned limitations
page must be the page `compat.json` records, a heading on it aside.

## Adding a pattern

A pattern earns a heading once **two independent real examples** exist. Adding
one means editing four places:

1. the enum in `schema/entry.schema.json`
2. `patterns.json` — the English and Chinese label, the long blurb the README
   uses and the short one the site uses. The README, the figures, the site and
   the MCP server all read this one file.
3. `docs/patterns.md`, a `## key` section with an explicit *when NOT to use this*,
   ending with a pair of `<!-- catalogued-key:start -->` /
   `<!-- catalogued-key:end -->` markers (key being the pattern's key), which
   `build_docs.py` fills with the count, the pattern's page and the site's filter
4. `docs/patterns.zh-CN.md`, the same section in Chinese with the same markers.
   The page says at the top that a model wrote it from the English page and
   that the English governs; a model's draft of the new section is fine under
   that line, and a person's is better

`lint.py` fails if the schema and `patterns.json` disagree or a field is
missing, and `lint_docs.py` fails if either patterns page has no section for it
or the section has no markers —
a silent fallback to a raw slug is how a bilingual list starts rotting.

A new `kind` or flag is the same, minus the doc section: the schema enum, then
`taxonomy.json`, which holds both languages' labels for the README and the
site.

## Adding a runnable example

See [`examples/README.md`](examples/README.md) for the runnable examples maintained
inside this repository. Their coverage is separate from the public resources in
the catalogue; use [`docs/status.md`](docs/status.md) for current catalogue gaps.
Say plainly in the file whether you ran it against the live API, and include a
reproducible test record before claiming that you did.

An example reaches the MCP server's `wire_pattern` prompt through its catalogue
row: add a row whose `evidence.path` is the example's file (with its patterns
and languages, and `code-untested` until it has been run), and
`scripts/build_examples_index.py` indexes it in the generated
`examples/index.json`. A file no row cites is left out of the index.

## Ground rules

Be accurate, be brief, and say what you do not know. If you are not sure whether
something qualifies, open an issue and ask rather than guessing — an honest
question costs nothing and a wrong row costs a reader's trust.
