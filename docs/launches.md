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
| Daily board | A board per day instead of per week | After 4 closed weeks in a row with at least 20 launches each; the board page counts the run |

Until the first week opens, the board lists the products that entered the
catalogue in the newest week, ordered by who read the call site and then by
stars. That is an order, not a ranking.

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
  the repository's owner, and a public member of the organisation that owns
  it, and then adds them to `makers`. Anyone else who says they made it is
  held until a maintainer confirms it.
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
   held for a person and why, or not launched and what to change. It holds a
   launch whose maker it cannot confirm, whose repository is a fork or has
   had no push for 60 days, or whose submitter's account is younger than 30
   days; a person decides those, as discovery candidates are decided
   ([docs/held.txt](held.txt)). A product whose call site nobody has read
   yet is read before its week opens, so every launch opens with at least a
   model's reading.
2. Early on Friday (00:20 UTC) the week's launches are written to
   `launches/<YYYY>-W<ww>.json` ([schema](../schema/launch.schema.json)) and
   pushed to `main`, with no merge to wait for. The board lists them under
   next week. A launch the check held is filed as held, and a maintainer
   decides it before Monday.
3. On Monday at 00:05 UTC the week opens: each launch gets a post in the
   repository's `Launches` Discussions, and a vote is a thumbs-up on it. The
   launch's issue gets the link to its post and is closed.
4. While the week runs, the board shows its launches in a shuffled order and
   without counts, so nobody votes for whatever is on top. (A Discussion shows
   its own reactions; the board does not repeat them.)
5. The next Monday the week closes: its votes are counted and the results
   written to the week's file. A launch whose votes come mostly from new
   accounts is held for a person instead of ranked. The top three with a vote
   counted get a badge, an image on the site for their README
   (`badges/<slug>.svg`), and the week gets its own page. Each launch's
   issue is told its result, and a top three the line that shows its badge.

Each month's report ([docs/monthly/](monthly/), written in the first week of
the next) lists the weeks that ended in the month with their top three.

Agents read the board without the pages. The MCP server's `launch_board()`
returns the running week (shuffled, no counts), the last closed week (ranked)
and the next one, and `top_launches(pattern=…)` the products that placed best,
each once at its best week. The site serves every week as filed, and as the
board shows it, at `api/v1/launches.json`. Both carry each launch's evidence
and caveats beside its votes, as the pages do.

## How votes count (rules v1)

- One vote per GitHub account, cast inside the week.
- Votes from the product's makers and from whoever submitted the launch count
  for nothing.
- An account younger than 30 days when it voted, or whose age cannot be read,
  counts for half.
- A launch ranks by its counted votes. A tie goes to the stronger evidence
  (a person read the call site, then a model, then a script's match, then
  none), then to the earlier submission.

A rule is never changed in place: a new one gets the next name (`v2`), and
each closed week records the rule it was counted under.

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

## The year's decision award

Jev entered early access on 2026-09-15, so the board's year runs from 15
September to the 14th of the next September. On each anniversary, from
2027-09-15, every decision pattern gets an award. `python3 scripts/award.py
--year 2027` draws up one shortlist per pattern from the year's closed weeks:
products whose call site a person or a model read, each at its best week,
ordered by rank and then counted votes, three at most. A person picks the award
from a shortlist and writes the pick and the reasons in `docs/award/<year>.md`.
Votes order a shortlist; the evidence decides who may be on it. The script
never picks.

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
  ([MAINTAINING.md](../MAINTAINING.md#what-only-the-owner-can-do)).
- **A separate template repository: no.** [launch-engine.md](launch-engine.md)
  lists what to copy and what to change; a second repository would be one more
  copy to keep in step.
- **Reaching makers: only inside this repository.** The board writes to nobody
  elsewhere and runs no social account. Makers meet it where they already are:
  the README links it, the new-entry bot's comment says a catalogued product
  can launch, and every product has a page.
- **More reviewers: not yet.** One maintainer reads launches while a week has
  a handful; the question comes back when a week passes 20.

## What is never done

- No ranking is sold, and no launch is placed above another for money.
- A launch found to be gamed (a ring of new accounts, votes bought) is removed,
  and the reason stays in its week's file.
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
| `scripts/site_products.py` | the product, maker, week and board pages, the badges and the weekly results feed | |
| `src/awesome_jev_mcp/query.py` | what the MCP server's launch tools and `api/v1/launches.json` answer | |
| `scripts/award.py` | the year's award shortlists, one per pattern | |
| [launch-engine.md](launch-engine.md) | how to run this board for another catalogue | |
| `.github/workflows/launch-intake.yml` | answers each launch issue with its check | |
| `.github/workflows/launch-collect.yml` | Fridays: files next week's launches on `main` | |
| `.github/workflows/launch-week.yml` | Mondays: closes last week, opens this one, tells the issues | |
| `.github/workflows/launch-votes.yml` | by hand: reads one Discussion's votes | |
| `.github/workflows/launch-probe.yml` | by hand: whether the workflow may post in `Launches` | |

`python3 scripts/check_launches.py` runs with the other checks
(`python3 scripts/check.py`).
