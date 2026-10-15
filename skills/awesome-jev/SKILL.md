---
name: awesome-jev
description: Use when building on Jev, TypeSafe AI's System One decision model, and you need what the vendor's docs do not give — a public worked example of a specific decision such as tool selection, safety gating or context compaction, the caveat flags on a project you are about to copy from, whether a model string really exists, how the model string, field names and request shape differ on Vercel, Cloudflare, OpenRouter or LiteLLM, or which published measurements are independent or negative. For the API contract and for designing the questions themselves, follow TypeSafe's own typesafe-ai skill and the live docs at docs.typesafe.ai instead. This skill complements them with what the public ecosystem shows and does not restate them.
---

# Building with Jev

A source-attributed catalogue of public Jev examples, indexed by the decision each one
makes. Use it to find how someone already solved the decision you are wiring up,
and to avoid the mistakes that recur in this ecosystem.

## Division of labour

TypeSafe publishes its own agent skill,
[`typesafe-ai`](https://github.com/typesafe-ai/skills) (catalogued here as
[`typesafe-skills-repo`](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-skills-repo)).
It, and the live docs it sends you to, starting from
[docs.typesafe.ai/llms.txt](https://docs.typesafe.ai/llms.txt), are the
reference for the API contract, the SDKs and how to design the questions: the
state, the instructions and criteria, which primitive fits. Where anything
below disagrees with them on those, they are right.

This skill covers what the vendor's pages cannot: what people have published —
worked examples of each decision pattern with the file each claim was read in
and the caveat flags that travel with it — how the surfaces differ, which model
strings exist, and which measurements are independent or negative. It indexes
other people's work: treat the code it lists as untested by this repository.

## Get the facts right first

These are the errors that show up most often in generated Jev code.

**The yes/no primitive is `noul`.** Not "binary", not "boolean". One SDK — the
Vercel AI SDK evaluation API — spells it `boolean` and reads `.probability`;
everywhere else it is `noul` and `.noul`. Much of the press coverage got this
wrong, so training data is contaminated.

**`noul` answers carry no `confidence` field.** The probability _is_ the answer.
`choice` and `score` do carry one. A helper that reads `.confidence` uniformly
across all three returns nothing for a third of the questions.

**There is no portable model string.** `jev-latest` on the native API,
`typesafe-ai/jev` on Vercel, `typesafe/jev` on Cloudflare, `typesafe/jev-1.13`
on OpenRouter. **`typesafe/jev-1` exists nowhere** and is the most repeated
fabrication about this model — check before writing one.

**Text is the default input.** Native Jev 1.13 and 1.14 also accept experimental
[PNG/JPEG images](https://docs.typesafe.ai/images) with
`TypeSafe-Danger-Zone-Images: true`. Audio and video remain unsupported.
Jev 1.14 adds experimental [Box](https://docs.typesafe.ai/primitives/box): one
normalized bounding box and confidence per question, with no "not found" answer.
It requires an image and the same opt-in header; combine with Noul for presence
when needed. The catalogue's primitive filters and picker still cover the three
core primitives, Choice, Score and Noul.

**Native versions, checked 2026-10-15:** `jev-1.14.0` and `jev-1.13.0` are
accepted; `jev-preview` points to 1.14 and `jev-latest` still points to 1.13.
The [October 14 announcement](https://typesafe.ai/blog/jev-1-14) said latest
would move about a week later, without an exact switch date. Recheck
[models](https://docs.typesafe.ai/models) before relying on an alias. This says
nothing about a gateway's support for the new version or experimental features.

**It cannot be run locally.** No weights are published. Anything claiming to run
Jev locally is a different model with a compatible wire format, and a compatible
API implies nothing about compatible calibration — thresholds do not transfer.

## Default limits

|                  |                                                                 |
| ---------------- | --------------------------------------------------------------- |
| `choice` options | max 255                                                         |
| `score` levels   | 2 to 10, 0-indexed, ordered low to high                         |
| Context          | 64k tokens per request; 32k for state plus the longest question |
| Output tokens    | free — the model generates no text                              |
| Streaming        | not supported on any surface                                    |

On native Jev 1.13 and 1.14, the experimental header
`TypeSafe-Danger-Zone-Long-Context: true` raises both context limits to 262k,
with lower speed and accuracy. The table above retains the defaults; see
[models](https://docs.typesafe.ai/models).

A `score` is probability-weighted and lands _between_ levels — the official
example returns `1.05` on a three-level scale. Do not assume an integer.

## Querying the catalogue

If the MCP server is available, prefer it over guessing:

- `search_examples(pattern=…, language=…, question_type=…)` — worked examples of
  a specific decision. `comparator=…`, `dataset=…` and `direction=…` find the
  benchmarks whose own authors compared Jev with something or used a dataset;
  a row's `measurement` is what its author reported, and its `direction` is
  author-stated, not reproduced here. `outcome="negative"` returns the rows
  whose own author measured Jev for that use and concluded against it (read
  them before the positive examples); `list_patterns()` counts them per pattern
- `get_example(slug)` — one row in full: its sources, the file its claim was
  read in (`evidence`) and every caveat flag
- `check_model_string(model)` — before writing any model string
- `compatibility(surface=…)` — before porting between gateways; each surface
  also says how many catalogued rows record it, and
  `search_examples(platform=<its id>)` lists them. A surface marked `coarse`
  shares its catalogue value with another route, so a row listed there may use
  that other route
- `list_patterns()` — the taxonomy, including which decisions nobody has
  published an example of, and per pattern what the catalogue records about
  its rows (`evidence`: documentation pages, cited files by kind, independent
  reports, negative results, rows citing no file) — reports counted, not a
  verdict

It also serves resources, for a client that reads them:

- `awesome-jev://flags` — what each caveat flag means. Rows carry bare flag
  keys; every answer holding flagged rows ends with a `caveat_glossary` for
  those flags
- `awesome-jev://collections`, then `awesome-jev://collections/{id}` — short
  editorial paths through the catalogue (a first call, projects to adapt,
  measurements), each pick with a reason and a caution
- `awesome-jev://patterns/{key}` — every row filed under one decision pattern,
  caveated rows included, with a link to that pattern's section of
  `docs/patterns.md` (its "when not to", where one is written)

And one prompt, `wire_pattern(pattern, language, surface)`: the pattern and a
link to its section of `docs/patterns.md`, that surface's model strings and
request shape, up to five cited rows with their caveats, and the repository's
own skeleton for the pattern in that language when there is one, under a
comment saying it was never executed. The catalogue runs nothing it lists.

Every result carries a `data` line saying where the catalogue came from and how
current it is. If it begins `STALE`, the server could not reach GitHub and is
answering from a cache or from the snapshot it was installed with — say so when
you rely on it, the same way you would pass on a row's caveat flags.

The Claude Code plugin for this repository starts the server for you. Elsewhere,
`pip install awesome-jev-mcp` and run `awesome-jev-mcp`. If pip finds no such
package, install it from the repository instead:
`pip install git+https://github.com/kydlikebtc/awesome-jev`.

Without it, start from
[`api/v1/index.json`](https://kydlikebtc.github.io/awesome-jev/api/v1/index.json)
on the catalogue's site. It lists every decision pattern with its row count and
the address and size of a file holding that pattern's rows, shaped as
`search_examples` returns them, caveat flags included: read the one pattern you
need rather than the whole catalogue, and skip rows flagged `not-jev` or
`shadow-mode-only`, as the server does. Read
[`compat.json`](https://kydlikebtc.github.io/awesome-jev/compat.json) before
writing a model string. If the site is unreachable, the same data files are on
GitHub:
[`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json)
and
[`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json).
A person can search [the site](https://kydlikebtc.github.io/awesome-jev/) itself.

## Design rules worth following

How to shape the questions — independent ones asked together in one request,
known rules, arithmetic, counting and dates kept in code, a no-match outcome
for a closed choice — is the official skill's ground: follow it. Four rules
the catalogue adds:

**A `none` option and a separate `noul` answer different questions.** A
`choice` must return one of its options, and `none` wins only by beating every
other one, so it is relative: whether the agent declines depends on what else
is on the list. A `noul` such as "does this request need a tool at all?" is
absolute: it weighs no option against another. Use the `noul` when acting at
all must not depend on the list.

**Thresholds are policy, not modelling.** They depend on what being wrong costs.
One catalogued production system, Inbox Zero, chooses a separate threshold for
each of its email decisions. The <!--n:threshold_rows-->32<!--/n--> rows that
so far record a constant their cited file compares a Jev answer with (a first
reading, not every row whose file has one) cut a `noul` probability anywhere
from <!--n:threshold_noul_low-->0.2<!--/n--> to <!--n:threshold_noul_high-->0.9<!--/n-->
and a `choice` confidence from <!--n:threshold_choice_low-->0.3<!--/n--> to <!--n:threshold_choice_high-->0.9<!--/n-->.
Those are what each project chose, not recommendations: `get_example` returns a
row's `observed_thresholds` with the text in its file each one stands on, and no
person has yet checked them on <!--n:thresholds_unread-->32<!--/n--> of those rows,
which a model read. A threshold tuned on a `noul` probability is not a `choice`
confidence.

**Pin a model version once you have tuned anything.** A threshold tuned against
one model version does not survive an alias moving to the next. Where a
surface documents a versioned string, send it rather than the alias;
`compat.json` lists each surface's strings, and not every surface has one.

**A probabilistic gate is not a security boundary.** It is useful defence in
depth in front of a shell command, a write or a spend. It is not a permission
system: an attacker chooses the input, and the vendor's own documentation names
adversarial content as a known weak spot. Anything destructive or irreversible
needs a deterministic rule or a human.

## Before believing a benchmark

Nearly every performance figure circulating about this model is the vendor's
own, produced with reference answers derived from other models' judgements
rather than human ground truth. The catalogue flags those `vendor-reported`.
Several independent measurements are _negative_ results — one large agent
framework ported the compaction approach, measured it, and published the
conclusion not to adopt it. Read those first: `search_examples(outcome="negative")`
returns them, and https://github.com/kydlikebtc/awesome-jev/blob/main/docs/benchmarks.md
sets every benchmark's measurement side by side, each direction as its author
states it, not reproduced here.

## Claiming a candidate from the discovery queue

When someone wants to add a project to the catalogue, start from the open issue
labelled `discovery` in kydlikebtc/awesome-jev. Its description is the queue:
repositories a script found calling Jev that nobody has read yet (unticked),
with the ones already catalogued or declined ticked or struck through.

1. Pick an unticked box and comment `claim owner/name` on the issue; the first
   claim wins.
2. In a clone of the repository, run
   `python3 scripts/discover_candidates.py --only owner/name --drafts drafts`.
   It re-reads the repository and writes `drafts/<slug>.json`, a draft row with
   what the script found filled in and a `_draft` field listing what is left.
3. Open the call site the draft names and read it. Write `summary` and
   `summary_zh` from what the code does, not from its README, and set
   `summary_source: curated`, since you wrote it; add
   `question_types` only for the primitives it actually calls; set
   `evidence.read_on` to the day you read the file; check the guessed `kind`,
   `patterns` and `languages`; if the kind is `alternative`, set
   `evidence.kind` to `wire-shape`, since the project is not built on Jev; set
   `zh_machine: true` if a model wrote the Chinese; name the source in
   `sources`. Leave `patterns_reviewed` out: it records a person reading the
   row against `docs/patterns.md`, which the person you work for adds. Leave
   `primitives_seen` out too: the weekly refresh writes it from the cited
   file's text, and it is no substitute for `question_types`.
4. Delete `_draft`, add the row to `catalog.json`, run
   `python3 scripts/check.py --fix`, and open a pull request naming the
   candidate you claimed. If it does not belong, add `owner/name  # reason` to
   `docs/declined.txt` instead.

`lint.py` refuses a row while `_draft` is in it. Deleting that field without
reading the code is the fabrication this catalogue exists to prevent: if you
could not open the file, say so and stop.
