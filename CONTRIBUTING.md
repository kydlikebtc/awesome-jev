# Contributing

This catalog is built around traceable sources and explicit limits. A submission
should say what you inspected and what remains unknown. A link, a code reading,
a text-matching check and a successful API run are different kinds of evidence;
do not present one as another.

So the bar is: **could a reader act on this row without opening the link?**

## Adding an entry

1. Add an object to `catalog.json`. Required fields: `slug`, `title`, `summary`,
   `summary_zh`, `url`, `kind`, `patterns`, `sources`, `license`.
2. Run the checks:

```bash
python3 scripts/lint.py \
  && python3 scripts/build_readme.py \
  && python3 scripts/build_assets.py \
  && python3 scripts/build_docs.py \
  && python3 scripts/lint_docs.py
```

`build_assets.py` regenerates the README's SVG figures, and `build_docs.py`
refills every generated number in `docs/status.md`, `docs/sources.md`,
`llms.txt` and the site's meta tags. CI fails if any of them are stale, because
a figure that disagrees with the catalog is worse than no figure.

3. Commit `catalog.json`, both generated READMEs, and whatever else those
   scripts rewrote. CI fails if any of it drifts.

No Python dependencies are needed. The schema validator is self-contained.

To preview the site locally:

```bash
python3 scripts/assemble_site.py && python3 -m http.server --directory site
```

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

Model strings and limits are held to `compat.json` the same way: write
`jev-latest` or `max 255` anywhere and `lint_docs.py` checks it against that
file. If the vendor changes one, change `compat.json` and every stale copy
turns red.

## Field rules

- **`title`** — as published at the source. If the page's `<title>` and its
  on-page heading disagree, use the heading a reader sees, and say so in `notes`.
- **`summary`** — what the example _actually demonstrates_, not what its README
  claims. "Routes support tickets with a choice and a score" beats "revolutionary
  AI-powered triage".
- **`summary_zh`** — write it yourself if you can. If you machine-translated it,
  set `zh_machine: true`. The READMEs report the split. This field describes
  translation provenance, not code quality or runtime testing.
- **`kind`** — the form of the thing. Use `alternative` for anything that does
  not call Jev, however Jev-shaped it is.
- **`patterns`** — which decisions it demonstrates. Read
  [`docs/patterns.md`](docs/patterns.md) first. `overview` cannot be combined
  with a specific pattern; the linter enforces that.
- **`question_types`** — only the primitives the code _actually_ calls. Read the
  call site; do not infer from the README. Several projects describe "scoring"
  while using only `noul`. The primitive is `noul`, never `binary`.
- **`evidence`** — the file you read that claim in, and strings from it that
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
  instead and say which. Set `read_on` to the date you actually read that file;
  do not advance it after an automated text check. An `evidence` record is a
  citation, not a stored CI pass or proof that the integration executes.
- **`official`** — true only for `typesafe.ai` hosts and the `typesafe-ai`
  GitHub org. A first-party integration published by another vendor is not
  official. The linter checks this.
- **`stars`**, **`repo_license`** — from the GitHub API on the date you add the
  row, not from a README badge. Several repos have a licence badge and no
  `LICENSE` file; that gets the `no-license` flag.
- **`sources`** — at least one, so the row is attributable. Name where you found
  it, not where it lives.

## Flags are the point

Use them generously. A flagged row is more useful than an unflagged one.

| Flag                                     | Use when                                        |
| ---------------------------------------- | ----------------------------------------------- |
| `vendor-reported`                        | it repeats the vendor's own performance numbers |
| `unverified-claims`                      | it makes measurement claims you could not check |
| `not-jev`                                | it does not call Jev at all                     |
| `shadow-mode-only`                       | Jev is wired in but changes no behaviour        |
| `code-untested`                          | you read the code but did not run it            |
| `single-commit`                          | one commit, so maintenance is unlikely          |
| `no-license`                             | no `LICENSE` file, whatever the README says     |
| `archived`                               | development visibly stopped                     |
| `paywalled`, `marketing`, `ai-generated` | as they say                                     |
| `early-access-required`                  | needs waitlist access to use                    |
| `third-party-api-key`                    | needs a key for a service other than TypeSafe   |

`ai-generated`, `unverified-claims` and `code-untested` require a `notes` line
saying why — a flag a reader cannot interpret is worse than no flag.

All catalogue code is **untested by this repository by default**, including rows
without `code-untested`. That flag adds a caveat; its absence must never be used
as a passed-test signal. Upstream benchmark results belong to their authors and
have not been independently reproduced here. A future runtime-verification claim
needs a dated report with the source revision, environment, model version and
result; neither `checked` nor `evidence.read_on` is a substitute.

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
  and which primitive it uses.

## Finding things to add

The weekly `discover` workflow does this for you and keeps an open issue
labelled `discovery` with what it found. To run it by hand:

```bash
python3 scripts/discover_candidates.py --top 40
```

This harvests every list in `docs/sibling-lists.txt`, ranks repositories by how
many cite each, and reads the candidate's code before reporting. A `calls-jev`
verdict means a call site was found — it is a shortlist, not a row. Read it,
write the summary yourself, and keep the evidence path the scan produced.

Read one and decided it does not belong? Add it to `docs/declined.txt` with a
reason, and the weekly run stops proposing it.

Know a directory we are not harvesting? Add it to `docs/sibling-lists.txt`.
That is a useful contribution on its own.

## Reporting a dead link

Open an issue with the slug. Do not delete the row — retiring an entry means
moving it to `retired.json` with a `notes` line explaining why, so the dead
reference stays searchable. `scripts/check_links.py` finds them but deliberately
never moves them; that judgement is a person's.

## Adding a pattern

A pattern earns a heading once **two independent real examples** exist. Adding
one means editing three places:

1. the enum in `schema/entry.schema.json`
2. `patterns.json` — the English and Chinese label, the long blurb the README
   uses and the short one the site uses. The README, the figures, the site and
   the MCP server all read this one file.
3. `docs/patterns.md`, a `## key` section with an explicit *when NOT to use this*

`lint.py` fails if the schema and `patterns.json` disagree or a field is
missing, and `lint_docs.py` fails if `docs/patterns.md` has no section for it —
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

## Ground rules

Be accurate, be brief, and say what you do not know. If you are not sure whether
something qualifies, open an issue and ask rather than guessing — an honest
question costs nothing and a wrong row costs a reader's trust.
