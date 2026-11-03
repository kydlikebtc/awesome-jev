# Running the launch board for another catalogue

[中文](launch-engine.zh-CN.md)

The launch board ([launches.md](launches.md)) is a handful of scripts over a
catalogue file and four things every public GitHub repository already has:
Issues for submissions, Discussions for votes, Actions for the weekly close,
Pages for the board. No server, no database, nothing paid. This page is for
someone who wants the same board over another catalogue. It is the template:
there is no separate template repository, by a decision of 2026-11-03
([launches.md](launches.md#decisions-2026-11-03)).

## What the board needs from each row

A product is a row of `catalog.json`. The board reads these fields:

| Field | What the board does with it |
| --- | --- |
| `slug`, `title`, `url` | names the product and links it |
| `kind`, `has_code`, `flags` | whether it can launch at all (`launches.is_product`: a project, plugin, SDK or integration with code, not flagged as no example) |
| `evidence` (`path`, `matched`, `read_on` or `model_read_on`) | the evidence tier shown beside the votes: a person read the call site, a model did, a script matched it, or none |
| `patterns` | `top_launches(pattern=…)` and the award's shortlists |
| `makers`, else `author.url` | who counts as a maker |
| `repo_pushed_at`, `first_seen` | the quiet check and the "new this week" list |
| `tagline`, `tagline_zh`, `demo_url` | optional, the maker's own words |

Another catalogue needs the same fields, or a small function that maps its
own fields onto them before the scripts read the rows.

## The files

The rules, standard library only, with no other import from this repository:

| File | What it does |
| --- | --- |
| `src/awesome_jev_mcp/query.py` (its launch section) | the evidence tier, the shuffled order, and what a week looks like to an agent |
| `scripts/launches.py` | every rule of the board: products, weeks, vote weights, the ring check, ranking, badges, hunters, the daily-board streak |
| `scripts/launch_votes.py` | reads one Discussion's thumbs-up reactions and voters' account ages over GraphQL |
| `scripts/launch_week.py` | closes last week and opens this one; `--probe` checks the token may post |
| `scripts/award.py` | the year's award shortlists |
| `scripts/_github.py` | the GitHub client the three above use (token, GraphQL query and mutation, job summary) |
| `schema/launch.schema.json`, `schema/maker.schema.json` | the week file and the maker profile |

The intake and the file check lean on this catalogue's own tooling, and a
fork replaces those parts with its own:

| File | Depends on |
| --- | --- |
| `scripts/launch_intake.py` | `draft_from_issue.py` (reading the issue form), `lint.py` (the schema validator) |
| `scripts/check_launches.py` | `lint.py` (`lint.validate`, a minimal JSON Schema draft-07 validator) |
| `scripts/site_products.py` | this site's page shell (`site_pages.py`); another site renders `launches.weeks()` its own way |

The workflows: `.github/workflows/launch-intake.yml`, `launch-week.yml`,
`launch-votes.yml`, `launch-probe.yml`, and the issue form
`.github/ISSUE_TEMPLATE/launch.yml`. `tests/test_launches.py`,
`tests/test_launch_flow.py`, `tests/test_mcp_launches.py` and
`tests/test_launch_award.py` test all of it without the network.

## What to change

- The board's addresses: `SITE` and `REPOSITORY_URL` in `query.py`, and
  `SELF` in `_github.py`. Every launch address derives from these three.
- The year: `ANNIVERSARY` and `FIRST_YEAR` in `award.py`.
- The rules: `RULES` in `launches.py`. Add a new version rather than editing
  one a closed week was counted under.
- The words: the issue form, the vote post (`launch_week.post`) and the board
  page's text.

## What the owner turns on

1. Discussions (Settings, then Features), and a category named `Launches` in
   Announcement format, so only maintainers start discussions there.
2. Run `launch-probe` once from the Actions page. If the workflow's token may
   not post in an Announcement category, switch the category to Open-ended:
   the weekly run only takes a post for a vote post when `github-actions` or
   the owner started it.
3. Run `launch-votes` on any discussion with a thumbs-up, to check the token
   can read reactions and account ages.
4. Pages, if the board pages are wanted.
