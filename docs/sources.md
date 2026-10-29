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
| Sibling directories linking the row's repository (one `owner/name` item per list, read weekly) | [each list, below](#sibling-directories-linking-catalogued-repositories) | 1181 |
| sibling-list aggregate (docs/sibling-lists.txt) | <https://github.com/kydlikebtc/awesome-jev/blob/main/docs/sibling-lists.txt> | 1104 |
| GitHub code search | <https://github.com/search> | 51 |
| TypeSafe AI docs index | <https://docs.typesafe.ai/llms.txt> | 36 |
| author submission | various | 24 |
| maintainer submission | <https://github.com/kydlikebtc/awesome-jev> | 20 |
| web search | various | 12 |
| Hacker News | various | 5 |
| jevai.org community site | <https://www.jevai.org/> | 5 |
| this repository | <https://github.com/kydlikebtc/awesome-jev> | 4 |
| YouTube search | <https://www.youtube.com/results?search_query=typesafe+jev> | 3 |
| AI SDK providers | <https://ai-sdk.dev/providers> | 1 |
| AI/ML API docs | <https://docs.aimlapi.com/> | 1 |
| arXiv | <https://arxiv.org/abs/2609.30216> | 1 |
| arXiv paper | <https://arxiv.org/abs/2610.18615> | 1 |
| author correction | <https://github.com/kydlikebtc/awesome-jev/pull/8> | 1 |
| Cloudflare Workers AI models | <https://developers.cloudflare.com/ai/models/> | 1 |
| community submission (issue #2) | <https://github.com/kydlikebtc/awesome-jev/issues/2> | 1 |
| community submission (issue #4) | <https://github.com/kydlikebtc/awesome-jev/issues/4> | 1 |
| Hugging Face model card | <https://huggingface.co/nace-ai/drex-v2.0> | 1 |
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
| [Omrigotlieb/awesome-jev](https://github.com/Omrigotlieb/awesome-jev) | 853 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | 776 |
| [daftAI2026/awesome-jev](https://github.com/daftAI2026/awesome-jev) | 714 |
| [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) | 679 |
| [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) | 500 |
| [RadRebelSam/awesome-jev](https://github.com/RadRebelSam/awesome-jev) | 480 |
| [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev) | 403 |
| [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) | 368 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | 302 |
| [valentynkit/awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) | 263 |
| [jqueryscript/awesome-jev](https://github.com/jqueryscript/awesome-jev) | 240 |
| [wh000wh000/awesome-jev-live](https://github.com/wh000wh000/awesome-jev-live) | 227 |
| [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) | 197 |
| [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) | 193 |
| [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) | 190 |
| [JohnDotOwl/awesome-jev](https://github.com/JohnDotOwl/awesome-jev) | 184 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | 179 |
| [BeatAPI/awesome-jev](https://github.com/BeatAPI/awesome-jev) | 164 |
| [tanxarx/awesome-jev](https://github.com/tanxarx/awesome-jev) | 161 |
| [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) | 154 |
| [walidboulanouar/awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases) | 145 |
| [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) | 133 |
| [Gerry9000/awesome-jev](https://github.com/Gerry9000/awesome-jev) | 127 |
| [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) | 127 |
| [Eurekaleo/awesome-jev-survey](https://github.com/Eurekaleo/awesome-jev-survey) | 92 |
| [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) | 91 |
| [jtnkminimal/awesome-jev](https://github.com/jtnkminimal/awesome-jev) | 87 |
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | 87 |
| [sontakey/awesome-jev](https://github.com/sontakey/awesome-jev) | 84 |
| [onlyoasis/awesome-jev-cases](https://github.com/onlyoasis/awesome-jev-cases) | 82 |
| [charetterat/awesome-jev-essentials](https://github.com/charetterat/awesome-jev-essentials) | 72 |
| [anandi1989/awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) | 68 |
| [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev) | 67 |
| [seeapi/awesome-jev-use-cases](https://github.com/seeapi/awesome-jev-use-cases) | 63 |
| [Li-Evan/awesome-jev](https://github.com/Li-Evan/awesome-jev) | 53 |
| [Ai-trainee/awesome-jev](https://github.com/Ai-trainee/awesome-jev) | 49 |
| [Amal-David/awesome-jev](https://github.com/Amal-David/awesome-jev) | 45 |
| [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) | 41 |
| [JingHao-Leon/awesome-jev-apps](https://github.com/JingHao-Leon/awesome-jev-apps) | 39 |
| [Yifan-Lan/awesome-jev-robustness](https://github.com/Yifan-Lan/awesome-jev-robustness) | 34 |
| [Promethe-us/awesome-jev](https://github.com/Promethe-us/awesome-jev) | 26 |
| [majiayu000/awesome-jev](https://github.com/majiayu000/awesome-jev) | 25 |
| [aliaihub/awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) | 16 |
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
752 of the 1276 summaries in `catalog.json` are the linked project's own GitHub description, word for word apart from letter case, spacing and a final full stop (`summary_source: upstream-description`), and 27 more were taken from such a description and no longer match it (`upstream-description-stale`). The projects' authors wrote those words and the copyright in them is theirs: this repository does not dedicate them under `CC0-1.0`. 779 of their Chinese counterparts are machine translations of them (`zh_machine`); the Chinese of such a row translates the project's words, and this repository does not dedicate it under `CC0-1.0` either. The READMEs, the pattern pages and the site mark each such summary *(upstream description)* or *(earlier upstream description)*.

11 summaries are marked `curated`: written for this catalogue by a person. 168 are marked `model-written`: written for it by a model, and marked *(written by a model)* wherever they are shown. The other 318 carry no `summary_source`, so where their words come from is not recorded row by row.

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
| MIT | 775 |
| None declared | 193 |
| Apache-2.0 | 159 |
| NOASSERTION (non-standard terms) | 50 |
| AGPL-3.0 | 8 |
| GPL-3.0 | 6 |
| CC0-1.0 | 3 |
| GPL-2.0 | 3 |
| BSD-3-Clause | 2 |
| CC-BY-4.0 | 1 |
| LGPL-3.0 | 1 |
<!-- licences:end -->

In all, <!--n:no_licence-->193<!--/n--> linked projects declare no licence. If you
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
