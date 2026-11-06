# Launches

[中文](launches.zh-CN.md)

The catalogue indexes every public Jev example it can find. The launch board is
a layer on top of it, for products: once a week, a product's maker puts it
forward, people vote, and the week closes with a ranking. It is the
catalogue's answer to "what did people build with Jev this week, and what do
they think of it?"

Two things sit side by side on every launch and are never added together:

- **Votes**: how many people cared, counted under the rules below.
- **Evidence**: whether the product calls Jev, and who read the code that
  does: the same record every row in the catalogue carries.

A rank is a count of votes. It is not this catalogue's recommendation, and
nothing here is affiliated with TypeSafe AI.

The board's pages are on the site: [Launches](https://kydlikebtc.github.io/awesome-jev/launches.html)
([中文](https://kydlikebtc.github.io/awesome-jev/launches.zh.html)), one page per
product (`products/<slug>.html`), one per maker (`makers/<login>.html`) and one
per closed week (`weeks/<week>.html`). The rules below are code:
[`scripts/launches.py`](../scripts/launches.py).

To launch a product, open the
[Launch a product](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml)
form, or follow "Launch it" on the product's page, which fills the product in.

## Where it stands

| Stage | What it adds | State |
| --- | --- | --- |
| Product and maker pages | A page per product and per maker; the board lists what is new each week | Built (2026-11-03) |
| Reading votes | [`launch-votes.yml`](../.github/workflows/launch-votes.yml) reads a Discussion's thumbs-up, run by hand | Built (2026-11-03); read the votes on a test post the same day |
| Open launches | The launch form and its check, a vote post per launch, the Monday close, week pages and badges | Built (2026-11-03); Discussions and the `Launches` category turned on the same day |
| For agents | The MCP server's `launch_board` and `top_launches` tools, and [`api/v1/launches.json`](https://kydlikebtc.github.io/awesome-jev/api/v1/launches.json) on the site | Built (2026-11-03) |
| Weekly results feed | Each closed week as an Atom entry: [`launches.xml`](https://kydlikebtc.github.io/awesome-jev/launches.xml) ([中文](https://kydlikebtc.github.io/awesome-jev/launches.zh.xml)) | Built (2026-11-03) |
| Filing without a merge | [`launch-collect.yml`](../.github/workflows/launch-collect.yml) files next week's launches early on Friday and pushes them to `main` | Built (2026-11-04) |
| Telling each launch | On Monday each launch's issue gets the link to its vote post and is closed; when the week closes, its result, and a top three its badge line | Built (2026-11-04) |
| One click from a product | "Launch it" and "Made this?" on every product page open the launch and confirm-entry forms with the product filled in; the board's new products have "Launch it" too | Built (2026-11-04) |
| Measures | Each closed week keeps how many accounts voted and how many came back, and each launch who had read its call site when it opened ([below](#how-the-board-is-measured)) | Built (2026-11-04) |
| Rising | The products whose GitHub stars grew fastest between the two latest weekly refreshes, on the board, and over the month in each monthly report ([below](#rising)) | Built (2026-11-04) |
| A badge for every product | One line for a product's README whose picture says it is listed, then that it is launching, then its top-three place; every product page shows the line ([below](#the-readme-badge)) | Built (2026-11-04) |
| Link previews | Every product, maker, week and board page names the site's preview card, so a link shared anywhere shows one | Built (2026-11-04) |
| Nothing waits for a person | Every case the launch check and the close used to hold for a maintainer has a rule ([below](#decisions-2026-11-05)); a failed run tries again by itself; the award is written by its rule | Built (2026-11-05) |
| The README leads with it | Both READMEs open with the board as a feed (the week running, the week filed next, last week's top three, the rising list) and how to launch; the cover draws the same cards. Friday's and Monday's commits regenerate them | Built (2026-11-05) |
| Daily board | A board per day instead of per week | After 4 closed weeks in a row with at least 20 launches each; the board page counts the run |

Until the first week opens, the board lists the products that entered the
catalogue in the newest week, ordered by who read the call site and then by
stars. That is an order, not a ranking. It also lists the products rising
fastest, whatever any week holds ([Rising](#rising)).

## What can launch

A **product** is a catalogued row that is a `project`, `plugin`, `sdk` or
`integration`, has code, and is an example of deciding with Jev (not flagged
`not-jev` or `shadow-mode-only`). Articles, videos, tutorials, benchmarks and
alternatives stay in the catalogue and are not launched.

A product not yet catalogued is added the usual way first
([CONTRIBUTING.md](../CONTRIBUTING.md#adding-an-entry)); a launch needs its
row.

A product launches at most once in 60 days.

## Who launches it

- A **maker** is a GitHub login in the row's `makers`, or, when the row names
  none, the login in its `author.url`. The check on a launch issue also takes
  the repository's owner, a public member of the organisation that owns it,
  and one of the repository's three top contributors with at least 5 commits,
  and then adds them to `makers`. Anyone else who says they made it launches
  as a hunter, and the check's comment says why; nobody is asked to confirm
  it.
- A **hunter** is anyone else who puts a product forward. The launch credits
  them; the product's makers can still claim it. The board thanks hunters by
  how many of their launches ran a week, and how many of those placed.
- Rows the discovery pipeline adds on its own have no launch until someone
  launches them.

A maker can say who they are on their page with a pull request adding
`makers/<login>.json` ([schema](../schema/maker.schema.json)): a name, a link
and a line in each language. The products on the page always come from the
catalogue.

A maker can also give their product a `tagline` (and `tagline_zh`) and a
`demo_url`, with the
[confirm-entry form](https://github.com/kydlikebtc/awesome-jev/issues/new?template=confirm-entry.yml)
or a pull request; "Made this?" on the product's page opens that form with
the row filled in. A tagline is the maker's own words; a model never writes one.

After a launch, the product's page says when it can launch again: until a
launch submitted that day would fall 60 days or more after its last week, the
Monday of the first week it can; from then on, "Launch it again".

## The week

Weeks are ISO weeks: Monday 00:00 UTC to Sunday 23:59 UTC.

1. A launch is submitted with the form by Thursday 23:59 UTC for the next
   week (later, the week after). A check answers the issue at once: ready,
   with what the rules settled; not read yet, when GitHub did not answer,
   and Friday's filing reads it again; or not launched and what to change.
   Since 2026-11-05 it holds nothing for a person:
   - a maker it cannot confirm launches as a hunter;
   - a submitter's account younger than 30 days launches in the first week
     after the account turns 30;
   - a fork launches once it has at least 10 commits of its own, and a
     repository with no push for 60 days once it has a new one; until then
     it is not launched, and editing the issue checks it again.

   A product whose call site nobody has read yet is read before its week
   opens, so every launch opens with at least a model's reading.
2. On Friday (the run is set for 00:20 UTC, and GitHub can start it hours
   late) the week's launches are written to
   `launches/<YYYY>-W<ww>.json` ([schema](../schema/launch.schema.json)) and
   pushed to `main`, with no merge to wait for. The board lists them under
   next week. A launch whose week has passed (its facts were read too late
   for it) goes on this one.
3. On Monday the week opens (the run is set for 00:05 UTC and can start
   hours late too): each launch gets a post in the repository's `Launches`
   Discussions, and a vote is a thumbs-up on it. A vote counts when it is
   cast by Sunday 23:59 UTC. The launch's issue gets the link to its post
   and is closed.
4. While the week runs, the board shows its launches in a shuffled order and
   without counts, so nobody votes for whatever is on top. (A Discussion shows
   its own reactions; the board does not repeat them.)
5. The next Monday the week closes: its votes are counted and the results
   written to the week's file. When most of a launch's votes come from new
   accounts, those votes count for nothing and it ranks by the rest; its
   result and the week's page say so. The top three with a vote
   counted put their place on their README badge
   ([below](#the-readme-badge)), and the week gets its own page. Each
   launch's issue is told its result, and a top three the line that shows
   its badge.

Each month's report ([docs/monthly/](monthly/), written in the first week of
the next) lists the weeks that ended in the month with their top three.

Agents read the board without the pages. The MCP server's `launch_board()`
returns the running week (shuffled, no counts), the last closed week (ranked)
and the next one, and `top_launches(pattern=…)` the products that placed best,
each once at its best week. The site serves every week as filed, and as the
board shows it, at `api/v1/launches.json`. Both carry each launch's evidence
and caveats beside its votes, as the pages do.

## How votes count (rules v2)

- One vote per GitHub account, cast inside the week.
- Votes from the product's makers and from whoever submitted the launch count
  for nothing.
- An account younger than 30 days when it voted, or whose age cannot be read,
  counts for half.
- When a launch has at least 10 votes and at least half of them come from such
  accounts, it looks like a ring of new accounts: their votes count for
  nothing, and its result says so (`ring`).
- A launch ranks by its counted votes. A tie goes to the stronger evidence
  (a person read the call site, then a model, then a script's match, then
  none), then to the earlier submission.

A rule is never changed in place: a new one gets the next name, and each
closed week records the rule it was counted under. Rules v1 (2026-11-03) were
the same except for a ring, which v1 held for a person instead of ranking; v2
(2026-11-05) settles it without one. No week closed under v1.

The repository keeps the counts only: how many votes, how many counted, how
many were discounted. It never keeps who voted.

## How the board is measured

Each closed week keeps a few counts beside its results. The board shows them
for the last week, the week's page for its week, and the monthly report for
each week of the month:

- **Accounts:** how many accounts' votes counted for something that week
  (`voters`), and how many of them had voted the week before too
  (`returning_voters`). As with votes, only the counts are kept.
- **Launches with at least 5 counted votes:** the board's main measure.
- **Read before opening:** how many launches had their call site read by a
  person or a model when their week opened (each launch's `tier_at_open`).
  The aim is all of them: `python3 scripts/launch_intake.py --unread` lists
  the launches about to open that nobody has read, and the daily task reads
  them first.
- **Discounted votes:** how many votes counted for less than one.

The board is doing its job when, four weeks in a row, at least 10 launches
run and at least 50 accounts' votes count; the monthly report says how many
weeks in a row so far. The rules for both are in
[`scripts/launches.py`](../scripts/launches.py) (`week_measures`,
`gate_streak`).

## Rising

The board lists the products whose GitHub stars grew fastest between the two
latest weekly refreshes (the snapshots in [history/](../history/), one each
Wednesday): those that gained at least 10 stars, in order of the gain as a
share of the stars they had before, then of the gain, ten at most. A quiet
product (no push in 60 days) is left out, as from the new products. Each
monthly report lists the same over its month, from its first snapshot to its
last.

It is there so the board says something every week, launches or not, and so
a hunter has somewhere to start: a rising product that can launch has
"Launch it", and one on the board this week its vote post. Stars are GitHub's
count, a popularity signal, not a verdict, and they are never added to votes
or evidence. Nothing is awarded for rising. The rule is `rising` in
[`scripts/launches.py`](../scripts/launches.py).

## The README badge

Every product has a badge at `badges/<slug>.svg`, and its page shows the one
line that puts it in a README, linked to the page:

```markdown
[![awesome-jev](https://kydlikebtc.github.io/awesome-jev/badges/your-slug.svg)](https://kydlikebtc.github.io/awesome-jev/products/your-slug.html)
```

The address stays the same and the picture keeps up: it says **listed**;
once the product is filed for a week, **launching 2026-W46**; while that week
runs, **vote this week**; after a week in which it placed in the top three
with a vote counted, that place (**#1 launch of 2026-W46**), until a later
week places it again. It is rebuilt with the site and says nothing the board
does not. Each launch's issue gets the line when its week opens, and a top
three again when it closes. The rule is `badge_state` in
[`scripts/launches.py`](../scripts/launches.py).

## The year's decision award

Jev entered early access on 2026-09-15, so the board's year runs from 15
September to the 14th of the next September. On each anniversary, from
2027-09-15, every decision pattern gets an award. `python3 scripts/award.py
--year 2027` draws up one shortlist per pattern from the year's closed weeks:
products whose call site a person or a model read, each at its best week,
ordered by rank and then counted votes, three at most. The award is the first
of each shortlist. Votes order a shortlist; the evidence decides who may be on
it. Nobody picks: on the 15th of each month
[`award.yml`](../.github/workflows/award.yml) runs `award.py --due`, which
writes `docs/award/<year>.md` once the year has ended and leaves a year
already written alone.

## Decisions (2026-11-03)

The owner asked for the board's open questions to be settled without waiting
on them. Each is settled here and can be reopened in an issue.

- **Name.** The board is "awesome-jev Launches" ("awesome-jev 发布榜"). It
  keeps the catalogue's name, so there is nothing new to register, and it
  borrows no other product's name.
- **An email newsletter: no; a feed instead.** Each closed week is an entry in
  [`launches.xml`](https://kydlikebtc.github.io/awesome-jev/launches.xml) ([中文](https://kydlikebtc.github.io/awesome-jev/launches.zh.xml)),
  linked from the board. A feed reader follows it, and anyone who wants email
  can turn the feed into one with a service of their own. A newsletter would
  need a mailing service, a list of addresses to keep and a sender who speaks
  for the project; the board keeps none of those.
- **Comments on the site (giscus): no.** The site loads no script from another
  host, and each launch's vote post in Discussions is already the place to talk
  about it. The product page links that post.
- **The MCP registry: after the package is on PyPI.** A registry entry points
  at a published package, and publishing `awesome-jev-mcp` is the owner's step
  ([MAINTAINING.md](../MAINTAINING.md#set-up-once)).
- **A separate template repository: no.** [launch-engine.md](launch-engine.md)
  lists what to copy and what to change; a second repository would be one more
  copy to keep in step.
- **Reaching makers: only inside this repository.** The board writes to nobody
  elsewhere and runs no social account. Makers meet it where they already are:
  the README links it, the new-entry bot's comment says a catalogued product
  can launch, and every product has a page.
- **More reviewers: not yet.** One maintainer reads launches while a week has
  a handful; the question comes back when a week passes 20. (Since
  2026-11-05 the daily task reads every launch's call site before its week
  opens, and no launch waits for a reviewer.)

## Decisions (2026-11-05)

The owner asked that the whole flow run with nothing left for them to do by
hand. Each case that used to wait for a maintainer now has a rule, in
[`scripts/launch_intake.py`](../scripts/launch_intake.py) and
[`scripts/launches.py`](../scripts/launches.py):

- **A maker the check cannot confirm** launches as a hunter. The check also
  takes one of the repository's three top contributors with at least 5
  commits as a maker.
- **A fork** launches once it has at least 10 commits of its own (GitHub's
  comparison with the repository it was forked from); until then its comment
  says how many it has.
- **A repository with no push for 60 days** launches after its next push;
  editing the issue checks it again.
- **A submitter's account younger than 30 days** launches in the first week
  that starts after the account turns 30, and the comment names that week.
- **Facts GitHub did not answer** are read again by Friday's filing, which also
  reads GitHub for any fact the check's comment did not record.
- **A launch whose week has passed** goes on the next one.
- **Votes that look like a ring** count for nothing under rules v2, and the
  launch ranks by the rest.
- **The award** is the first of each shortlist, written by `award.yml`.
- **A failed run** on `main` runs once more by itself
  ([`retry.yml`](../.github/workflows/retry.yml)), the Friday and Monday runs
  twice more the same day, and when `main` moves under the Friday or Monday
  push, the run files or counts again from the new `main` instead of leaving
  a branch for someone to merge.

## What is never done

- No ranking is sold, and no launch is placed above another for money.
- Votes that look like a ring of new accounts count for nothing (rules v2). A
  launch found gamed otherwise (votes bought) is removed, and the reason stays
  in its week's file.
- The board does not ask anyone to vote, and posts nowhere outside this
  repository.

## Files

| Path | What it holds | Written by |
| --- | --- | --- |
| `catalog.json` | the products, with `makers`, `tagline`, `tagline_zh`, `demo_url` | contributors and makers |
| `launches/<YYYY>-W<ww>.json` | one week: its launches, their status and, once closed, their results | the launch scripts |
| `makers/<login>.json` | a maker's own profile, optional | that maker |
| `scripts/launches.py` | every rule above | |
| `scripts/check_launches.py` | holds `launches/` and `makers/` to those rules | |
| `scripts/launch_intake.py` | checks a launch issue, collects a week's launches, and lists those nobody has read | |
| `scripts/launch_week.py` | opens a week, closes the one before, and tells each launch's issue | |
| `scripts/launch_votes.py` | reads one Discussion's votes | |
| `scripts/site_products.py` | the product, maker, week and board pages, the rising list, the badges and the weekly results feed | |
| `history/<date>.json` | each weekly refresh's counts and stars; the rising list reads the two newest | `metadata.yml` |
| `src/awesome_jev_mcp/query.py` | what the MCP server's launch tools and `api/v1/launches.json` answer | |
| `scripts/award.py` | the year's award: one shortlist per pattern, and its first as the award | |
| `docs/award/<year>.md` | the year's award, once the year has ended | `award.yml` |
| [launch-engine.md](launch-engine.md) | how to run this board for another catalogue | |
| `.github/workflows/launch-intake.yml` | answers each launch issue with its check | |
| `.github/workflows/launch-collect.yml` | Fridays: files next week's launches on `main` | |
| `.github/workflows/launch-week.yml` | Mondays: closes last week, opens this one, tells the issues | |
| `.github/workflows/launch-votes.yml` | by hand: reads one Discussion's votes | |
| `.github/workflows/launch-probe.yml` | by hand: whether the workflow may post in `Launches` | |
| `.github/workflows/award.yml` | the 15th of each month: writes the year's award once it is due | |
| `.github/workflows/retry.yml` | runs a failed run on `main` once more | |

`python3 scripts/check_launches.py` runs with the other checks
(`python3 scripts/check.py`).
