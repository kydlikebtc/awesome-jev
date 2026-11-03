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
form.

## Where it stands

| Stage | What it adds | State |
| --- | --- | --- |
| Product and maker pages | A page per product and per maker; the board lists what is new each week | Built (2026-11-03) |
| Reading votes | [`launch-votes.yml`](../.github/workflows/launch-votes.yml) reads a Discussion's thumbs-up, run by hand | Built (2026-11-03); read the votes on a test post the same day |
| Open launches | The launch form and its check, a vote post per launch, the Monday close, week pages and badges | Built (2026-11-03); Discussions and the `Launches` category turned on the same day |
| Daily board | A board per day instead of per week | Once a week holds enough launches |

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
or a pull request. A tagline is the maker's own words; a model never writes one.

## The week

Weeks are ISO weeks: Monday 00:00 UTC to Sunday 23:59 UTC.

1. A launch is submitted with the form by Thursday 23:59 UTC for the next
   week (later, the week after). A check answers the issue at once: ready,
   held for a person and why, or not launched and what to change. It holds a
   launch whose maker it cannot confirm, whose repository is a fork or has
   had no push for 60 days, or whose submitter's account is younger than 30
   days; a person decides those, as discovery candidates are decided
   ([docs/held.txt](held.txt)).
2. On Friday the week's launches are written to
   `launches/<YYYY>-W<ww>.json` ([schema](../schema/launch.schema.json)) and
   reach `main` with the owner's merge. The board lists them under next week.
3. On Monday at 00:05 UTC the week opens: each launch gets a post in the
   repository's `Launches` Discussions, and a vote is a thumbs-up on it.
4. While the week runs, the board shows its launches in a shuffled order and
   without counts, so nobody votes for whatever is on top. (A Discussion shows
   its own reactions; the board does not repeat them.)
5. The next Monday the week closes: its votes are counted and the results
   written to the week's file. A launch whose votes come mostly from new
   accounts is held for a person instead of ranked. The top three with a vote
   counted get a badge, an image on the site for their README
   (`badges/<slug>.svg`), and the week gets its own page.

Each month's report ([docs/monthly/](monthly/), written in the first week of
the next) lists the weeks that ended in the month with their top three.

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
| `scripts/launch_intake.py` | checks a launch issue, and collects a week's launches | |
| `scripts/launch_week.py` | opens a week and closes the one before | |
| `scripts/launch_votes.py` | reads one Discussion's votes | |
| `scripts/site_products.py` | the product, maker, week and board pages, and the badges | |

`python3 scripts/check_launches.py` runs with the other checks
(`python3 scripts/check.py`).
