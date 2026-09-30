# Sources and licences

Every row in `catalog.json` carries a `sources` array naming where it was found,
so the catalog is auditable rather than asserted. This page aggregates that
array and states the licence position.

## Where the rows come from

Regenerated from every row's `sources[]` on each build, so the order is what is
true now rather than what was true at launch. A row can cite more than one
source. The sources a person wrote say where a row was found; after them, a
row with a GitHub repository lists the sibling directories whose README links
it, one item per list, and those are counted together on one line here and
list by list below.

<!-- sources:start -->
| Source | URL | Rows |
| --- | --- | --- |
| Sibling directories linking the row's repository (one `owner/name` item per list, read weekly) | [each list, below](#sibling-directories-linking-catalogued-repositories) | 1130 |
| sibling-list aggregate (docs/sibling-lists.txt) | <https://github.com/kydlikebtc/awesome-jev/blob/main/docs/sibling-lists.txt> | 1053 |
| GitHub code search | <https://github.com/search> | 51 |
| TypeSafe AI docs index | <https://docs.typesafe.ai/llms.txt> | 36 |
| maintainer submission | <https://github.com/kydlikebtc/awesome-jev> | 21 |
| web search | various | 12 |
| author submission | various | 8 |
| Hacker News | various | 5 |
| jevai.org community site | <https://www.jevai.org/> | 5 |
| this repository | <https://github.com/kydlikebtc/awesome-jev> | 4 |
| YouTube search | <https://www.youtube.com/results?search_query=typesafe+jev> | 3 |
| AI SDK providers | <https://ai-sdk.dev/providers> | 1 |
| AI/ML API docs | <https://docs.aimlapi.com/> | 1 |
| author correction | <https://github.com/kydlikebtc/awesome-jev/pull/8> | 1 |
| Cloudflare Workers AI models | <https://developers.cloudflare.com/ai/models/> | 1 |
| community submission (issue #2) | <https://github.com/kydlikebtc/awesome-jev/issues/2> | 1 |
| community submission (issue #4) | <https://github.com/kydlikebtc/awesome-jev/issues/4> | 1 |
| LangChain blog | <https://www.langchain.com/blog> | 1 |
| LangChain integrations | <https://docs.langchain.com/oss/python/integrations/providers/> | 1 |
| Langfuse integrations | <https://langfuse.com/integrations> | 1 |
| LiteLLM docs | <https://docs.litellm.ai/docs/pass_through> | 1 |
| Netlify changelog | <https://www.netlify.com/changelog/> | 1 |
| OpenRouter providers | <https://openrouter.ai/providers> | 1 |
| Pydantic AI docs | <https://pydantic.dev/docs/ai/models/> | 1 |
| Spring blog | <https://spring.io/blog> | 1 |
| Upstream README: default-mode recheck (2026-09-24) | <https://github.com/guilhem/jev-ci-selector#readme> | 1 |
| Vercel changelog | <https://vercel.com/changelog> | 1 |
| Vercel docs | <https://vercel.com/docs/ai-gateway> | 1 |
| Vercel knowledge base | <https://vercel.com/kb> | 1 |
<!-- sources:end -->

Most of the long tail arrives through the sibling-list aggregate: a repository
that several other Jev directories cite gets its code read, and only enters here
if that reading finds a call site. By usefulness per row, though, the official
cookbooks and pattern pages remain the best material in the catalogue — they are
primary sources, written by the people who built the model.

### Sibling directories linking catalogued repositories

Which of the directories in [`docs/sibling-lists.txt`](sibling-lists.txt)
link how many catalogued rows' repositories in their README. The weekly refresh
reads each README (`scripts/attribute_sources.py`) and records every link it
finds on the row as a `sources` item: the list's `owner/name` and its URL.
Nothing else is taken from a list — many ship no licence, and a URL is a fact
where a description is someone's writing. A list that could not be read keeps
the citations it had when last read. A directory renamed since it was listed
is there under both names, and its old name shows no rows: GitHub serves the
same README under each, and it is counted once, under the name listed first.

<!-- citations:start -->
| Sibling directory | Catalogued rows whose repository its README links |
| --- | --- |
| [Omrigotlieb/awesome-jev](https://github.com/Omrigotlieb/awesome-jev) | 769 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | 719 |
| [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) | 654 |
| [daftAI2026/awesome-jev](https://github.com/daftAI2026/awesome-jev) | 637 |
| [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) | 482 |
| [RadRebelSam/awesome-jev](https://github.com/RadRebelSam/awesome-jev) | 477 |
| [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev) | 328 |
| [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) | 288 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | 276 |
| [valentynkit/awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) | 257 |
| [wh000wh000/awesome-jev-live](https://github.com/wh000wh000/awesome-jev-live) | 231 |
| [jqueryscript/awesome-jev](https://github.com/jqueryscript/awesome-jev) | 207 |
| [JohnDotOwl/awesome-jev](https://github.com/JohnDotOwl/awesome-jev) | 187 |
| [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) | 176 |
| [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) | 176 |
| [BeatAPI/awesome-jev](https://github.com/BeatAPI/awesome-jev) | 168 |
| [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) | 153 |
| [walidboulanouar/awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases) | 150 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | 141 |
| [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) | 136 |
| [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) | 127 |
| [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) | 125 |
| [Gerry9000/awesome-jev](https://github.com/Gerry9000/awesome-jev) | 121 |
| [tanxarx/awesome-jev](https://github.com/tanxarx/awesome-jev) | 114 |
| [jtnkminimal/awesome-jev](https://github.com/jtnkminimal/awesome-jev) | 88 |
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | 78 |
| [sontakey/awesome-jev](https://github.com/sontakey/awesome-jev) | 78 |
| [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) | 77 |
| [charetterat/awesome-jev-essentials](https://github.com/charetterat/awesome-jev-essentials) | 72 |
| [onlyoasis/awesome-jev-cases](https://github.com/onlyoasis/awesome-jev-cases) | 66 |
| [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev) | 63 |
| [seeapi/awesome-jev-use-cases](https://github.com/seeapi/awesome-jev-use-cases) | 63 |
| [anandi1989/awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) | 57 |
| [Li-Evan/awesome-jev](https://github.com/Li-Evan/awesome-jev) | 53 |
| [Ai-trainee/awesome-jev](https://github.com/Ai-trainee/awesome-jev) | 47 |
| [Amal-David/awesome-jev](https://github.com/Amal-David/awesome-jev) | 39 |
| [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) | 39 |
| [Yifan-Lan/awesome-jev-robustness](https://github.com/Yifan-Lan/awesome-jev-robustness) | 38 |
| [JingHao-Leon/awesome-jev-apps](https://github.com/JingHao-Leon/awesome-jev-apps) | 33 |
| [majiayu000/awesome-jev](https://github.com/majiayu000/awesome-jev) | 25 |
| [Eurekaleo/awesome-jev-survey](https://github.com/Eurekaleo/awesome-jev-survey) | 24 |
| [Promethe-us/awesome-jev](https://github.com/Promethe-us/awesome-jev) | 24 |
| [aliaihub/awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) | 14 |
| [yangzhou-chaofan/awesome-jev-prompt](https://github.com/yangzhou-chaofan/awesome-jev-prompt) | 11 |
| [everyinfra/jev-radar](https://github.com/everyinfra/jev-radar) | 3 |
| [visitworld123/Awesome-Robot-Use-Agent](https://github.com/visitworld123/Awesome-Robot-Use-Agent) | 3 |
| [nexibeo/jev-cookbook](https://github.com/nexibeo/jev-cookbook) | 2 |
| [AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) | 0 |
| [Hiwoniu/Jev-Case](https://github.com/Hiwoniu/Jev-Case) | 0 |
| [mizzlelover/jev-hub](https://github.com/mizzlelover/jev-hub) | 0 |
| [OmniJev/awesome-jev](https://github.com/OmniJev/awesome-jev) | 0 |
| [theSekyi/jevusecases](https://github.com/theSekyi/jevusecases) | 0 |
<!-- citations:end -->

## Licences

This repository separates code from data, following the convention the reference
repository established.

| What                                      | Licence                                                   |
| ----------------------------------------- | --------------------------------------------------------- |
| `scripts/`, `site/`, `examples/`          | [MIT](../LICENSE-MIT)                                     |
| `catalog.json`, `retired.json`, `schema/` | [CC0-1.0](../LICENSE-CC0), quoted summaries aside (below) |
| `docs/`, `README*.md`                     | CC0-1.0, quoted summaries aside (below)                   |

<!-- row-licences:start -->
882 of the 1211 summaries in `catalog.json` are the linked project's own GitHub description, word for word apart from letter case, spacing and a final full stop (`summary_source: upstream-description`), and 9 more were taken from such a description and no longer match it (`upstream-description-stale`). The projects' authors wrote those words and the copyright in them is theirs: this repository does not dedicate them under `CC0-1.0`. 891 of their Chinese counterparts are machine translations of them (`zh_machine`); the Chinese of such a row translates the project's words, and this repository does not dedicate it under `CC0-1.0` either. The READMEs, the pattern pages and the site mark each such summary *(upstream description)* or *(earlier upstream description)*.

3 summaries are marked `curated`: written for this catalogue. The other 317 carry no `summary_source`, so where their words come from is not recorded row by row.

Every row's `license` field is `CC0-1.0`. It covers the row's structured metadata (slug, kind, patterns, flags, dates, counts, evidence records and the rest) and any text written for this catalogue, not a summary labelled as the project's own description or the Chinese translation of one.
<!-- row-licences:end -->

If a row does inherit text from a CC BY 4.0 catalog, it gets
`license: "CC-BY-4.0"` and the attribution is that row's `sources` array.

**Linked works keep their own licences.** The `repo_license` field on a row
records what the linked project declares, which is not always what its README
badge claims — `no-license` flags the cases where a repository ships no `LICENSE`
file at all.

Declared licences across the catalog's linked repositories:

<!-- licences:start -->
| Licence | Repositories |
| --- | --- |
| MIT | 743 |
| None declared | 199 |
| Apache-2.0 | 129 |
| NOASSERTION (non-standard terms) | 48 |
| AGPL-3.0 | 7 |
| GPL-3.0 | 6 |
| BSD-3-Clause | 2 |
| CC0-1.0 | 2 |
| GPL-2.0 | 2 |
| CC-BY-4.0 | 1 |
| LGPL-3.0 | 1 |
<!-- licences:end -->

In all, <!--n:no_licence-->199<!--/n--> linked projects declare no licence. If you
plan to reuse code from one, that is a blocker, not a detail — check before you
copy.

## Relationship to TypeSafe AI

None. This is an unaffiliated community index. "Jev", "TypeSafe" and "System
One" are used descriptively to refer to the vendor's product. No endorsement is
claimed or implied, and no row here should be read as a recommendation.

## Relationship to other Jev directories

There are dozens. Several are catalogued in this repository as rows of their own,
including the largest ones, because pretending otherwise would be silly. They
compete on coverage; this one competes on verification. If you are looking for a
project and cannot find it here, they are worth checking — and if you find a real
one that is missing here, [please add it](../CONTRIBUTING.md).

## Corrections

If a row misattributes your work, mischaracterises your project, or you want it
removed, open an issue. Correction requests take priority over additions.
