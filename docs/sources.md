# Sources and licences

Every row in `catalog.json` carries a `sources` array naming where it was found,
so the catalog is auditable rather than asserted. This page aggregates that
array and states the licence position.

## Where the rows come from

Regenerated from every row's `sources[]` on each build, so the order is what is
true now rather than what was true at launch. A row can cite more than one
source.

<!-- sources:start -->
| Source | URL | Rows |
| --- | --- | --- |
| sibling-list aggregate (docs/sibling-lists.txt) | <https://github.com/kydlikebtc/awesome-jev/blob/main/docs/sibling-lists.txt> | 1053 |
| GitHub code search | <https://github.com/search> | 51 |
| TypeSafe AI docs index | <https://docs.typesafe.ai/llms.txt> | 36 |
| maintainer submission | <https://github.com/kydlikebtc/awesome-jev> | 20 |
| web search | various | 12 |
| Hacker News | various | 5 |
| jevai.org community site | <https://www.jevai.org/> | 5 |
| author submission | various | 4 |
| this repository | <https://github.com/kydlikebtc/awesome-jev> | 4 |
| YouTube search | <https://www.youtube.com/results?search_query=typesafe+jev> | 3 |
| AI SDK providers | <https://ai-sdk.dev/providers> | 1 |
| AI/ML API docs | <https://docs.aimlapi.com/> | 1 |
| arXiv | <https://arxiv.org/abs/2609.30216> | 1 |
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

## Licences

This repository separates code from data, following the convention the reference
repository established.

| What                                      | Licence                   |
| ----------------------------------------- | ------------------------- |
| `scripts/`, `site/`, `examples/`          | [MIT](../LICENSE-MIT)     |
| `catalog.json`, `retired.json`, `schema/` | [CC0-1.0](../LICENSE-CC0) |
| `docs/`, `README*.md`                     | CC0-1.0                   |

<!-- row-licences:start -->
Every row in the current build is `CC0-1.0`, meaning no descriptive text was inherited from a source that requires attribution.
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
| MIT | 735 |
| None declared | 203 |
| Apache-2.0 | 129 |
| NOASSERTION (non-standard terms) | 49 |
| AGPL-3.0 | 6 |
| GPL-3.0 | 6 |
| BSD-3-Clause | 2 |
| CC0-1.0 | 2 |
| GPL-2.0 | 2 |
| CC-BY-4.0 | 1 |
| LGPL-3.0 | 1 |
<!-- licences:end -->

In all, <!--n:no_licence-->203<!--/n--> linked projects declare no licence. If you
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
