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
product (`products/<slug>.html`) and one per maker (`makers/<login>.html`).
The rules below are code: [`scripts/launches.py`](../scripts/launches.py).

## Where it stands

| Stage | What it adds | State |
| --- | --- | --- |
| Product and maker pages | A page per product and per maker; the board lists what is new each week | Built (2026-11-03) |
| Reading votes | [`launch-votes.yml`](../.github/workflows/launch-votes.yml) reads a Discussion's thumbs-up, run by hand | Built; waits for Discussions to be turned on |
| Open launches | The launch form, a vote post per launch, an hourly count, the weekly close | Next |
| Daily board | A board per day instead of per week | Once a week holds enough launches |

Until launches open, the board lists the products that entered the catalogue
in the newest week, ordered by who read the call site and then by stars. That
is an order, not a ranking.

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
  none, the login in its `author.url`. A maker is the repository's owner or a
  collaborator, checked when their issue is read.
- A **hunter** is anyone else who puts a product forward. The launch credits
  them; the product's makers can still claim it.
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

1. A launch is submitted by Thursday 23:59 UTC for the next week. Its checks
   run when it is submitted; what a check cannot settle is held for a person,
   as discovery candidates are ([docs/held.txt](held.txt)).
2. The week's launches and any new rows they need reach `main` with the
   owner's Friday merge.
3. On Monday the week opens. Each launch has a GitHub Discussion; a vote is a
   thumbs-up on its post.
4. While the week runs, the board shows its launches in a shuffled order and
   without counts, so nobody votes for whatever is on top.
5. When the week closes, its votes are counted and the results are written to
   `launches/<YYYY>-W<ww>.json` ([schema](../schema/launch.schema.json)). The
   top three with a vote counted get a badge.

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
| `launches/<YYYY>-W<ww>.json` | one week: its launches, their status and, once closed, their results | the launch workflows |
| `makers/<login>.json` | a maker's own profile, optional | that maker |
| `scripts/launches.py` | every rule above | |
| `scripts/check_launches.py` | holds `launches/` and `makers/` to those rules | |
| `scripts/launch_votes.py` | reads one Discussion's votes | |
| `scripts/site_products.py` | the product, maker and board pages | |

`python3 scripts/check_launches.py` runs with the other checks
(`python3 scripts/check.py`).
