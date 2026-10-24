<!-- Written by scripts/build_shape.py from catalog.json, compat.json, patterns.json, the entry schema and history/. Edit those, not this file. -->

# The catalogue's shape

<sub>[awesome-jev](../README.md) · [中文](shape.zh-CN.md)</sub>

Counts that describe this catalogue as a dataset, regenerated from `catalog.json` whenever it changes; the newest link check behind them is dated **2026-10-21**. They describe what the catalogue holds, which is what reached it through the sibling directories, this repository's discovery and its contributors, not the ecosystem at large. A star band is a popularity signal, not a quality verdict, and nothing here was run or reproduced by this repository. `python3 scripts/counts.py` prints the same numbers as text; the headline figures are on [the status page](status.md).

## Evidence by decision pattern

What the catalogue records about the rows filed under each pattern: reports counted, not a verdict. A row counts in every column that applies and under every pattern it is filed under. **Official documentation** is TypeSafe AI's own documentation pages (`kind: official-docs`). **Call site**, **wire shape** and **example only** count rows citing a file, by what `evidence.kind` records it shows: where the project calls Jev; a file speaking Jev's request shape rather than building on Jev; only an example the project ships. **Independent reports** are benchmark rows not flagged `vendor-reported`: their authors' measurements, not reproduced by this repository. **Negative results** are rows whose own author measured Jev for the use and concluded against it (author-stated; [listed on the status page](status.md#negative-results)). **No file cited** counts rows with no `evidence` (`evidence_none` may say why). The MCP server's `list_patterns` and each pattern's page give the same numbers.

| Pattern | Rows | Official documentation | Call site | Wire shape | Example only | Independent reports | Negative results | No file cited |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 236 | 3 | 228 | 4 | 0 | 11 | 1 | 4 |
| [Intent routing](by-pattern/intent-routing.md) | 38 | 3 | 27 | 0 | 0 | 2 | 0 | 11 |
| [Context compaction](by-pattern/context-compaction.md) | 37 | 0 | 37 | 0 | 0 | 2 | 2 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 142 | 2 | 136 | 2 | 0 | 10 | 0 | 4 |
| [Output validation](by-pattern/output-validation.md) | 135 | 2 | 130 | 1 | 0 | 11 | 0 | 4 |
| [Retry control](by-pattern/retry-control.md) | 8 | 0 | 7 | 1 | 0 | 0 | 0 | 0 |
| [Human escalation](by-pattern/human-escalation.md) | 73 | 7 | 58 | 5 | 0 | 10 | 0 | 10 |
| [Model routing](by-pattern/model-routing.md) | 49 | 2 | 42 | 1 | 0 | 0 | 1 | 6 |
| [Speculative fan-out](by-pattern/fan-out.md) | 34 | 3 | 26 | 1 | 0 | 1 | 0 | 7 |
| [Search & ranking](by-pattern/search-ranking.md) | 67 | 3 | 63 | 0 | 0 | 6 | 1 | 4 |
| [Structured extraction](by-pattern/data-extraction.md) | 17 | 4 | 13 | 0 | 0 | 1 | 0 | 4 |
| [Classification](by-pattern/classification.md) | 126 | 4 | 116 | 1 | 0 | 11 | 1 | 9 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 8 | 1 | 7 | 0 | 0 | 0 | 0 | 1 |
| [Document triage](by-pattern/document-triage.md) | 22 | 0 | 21 | 0 | 0 | 2 | 0 | 1 |
| [Support triage](by-pattern/support-triage.md) | 9 | 1 | 4 | 0 | 0 | 1 | 0 | 5 |
| [Content scoring](by-pattern/content-scoring.md) | 164 | 2 | 155 | 5 | 0 | 9 | 1 | 4 |
| [Recommendation](by-pattern/recommendation.md) | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 469 | 6 | 373 | 57 | 0 | 23 | 1 | 39 |

23 independent reports are filed under `overview` and no other pattern, so this table cannot count them for the decision they measured until a person files them under it.

## Languages

Rows recording each language (`languages`; a row may record several). 32 rows record none.

| Language | Rows |
| --- | --- |
| `python` | 482 |
| `typescript` | 415 |
| `javascript` | 153 |
| `rust` | 50 |
| `go` | 46 |
| `swift` | 17 |
| `java` | 15 |
| `ruby` | 12 |
| `shell` | 10 |
| `kotlin` | 8 |
| `php` | 8 |
| `csharp` | 7 |
| `elixir` | 7 |
| `cpp` | 6 |
| `c` | 5 |
| `haskell` | 1 |
| `lua` | 1 |

## How rows reach Jev

`platforms` records how a row reaches Jev. Discovery does not tag it: `scripts/discover_candidates.py` and the drafts it writes leave the field to the person adding a row, and `typesafe-api` is what a row records when nobody named another route. So the first group below counts that default at least as much as a finding: a row that reaches Jev through a pass-through may record `typesafe-api` alone ([compatibility](compatibility.md)). Each row counts in exactly one group.

| Group | Rows |
| --- | --- |
| `typesafe-api` and nothing else | 1093 |
| At least one value another surface in [the compatibility table](compatibility.md) stands for (a gateway, SDK or framework), and not `self-hosted` | 47 |
| Besides `typesafe-api`, only values no compatibility surface stands for (a host, tool or framework the example runs in, or a route that table does not describe), and not `self-hosted` | 35 |
| `self-hosted`, whatever else is recorded | 58 |
| No value recorded | 21 |

Every value rows record, with the compatibility surfaces that stand for it:

| Value | Compatibility surface | Rows |
| --- | --- | --- |
| `typesafe-api` | `typesafe-native` | 1142 |
| `self-hosted` | — | 58 |
| `vercel-ai-gateway` | `vercel-eval`, `vercel-compat` | 21 |
| `claude-code` | — | 18 |
| `openrouter` | `openrouter` | 17 |
| `mcp` | — | 6 |
| `github` | — | 4 |
| `langchain` | `langchain` | 4 |
| `jevai-org` | — | 3 |
| `opencode-zen` | — | 2 |
| `pydantic-ai` | `pydantic-ai` | 2 |
| `vercel-ai-sdk` | `vercel-eval`, `ai-sdk-direct` | 2 |
| `aimlapi` | `aimlapi` | 1 |
| `airflow` | — | 1 |
| `autogpt` | — | 1 |
| `bifrost` | `bifrost` | 1 |
| `cloudflare-workers-ai` | `cloudflare` | 1 |
| `composio` | — | 1 |
| `discord` | — | 1 |
| `effect` | — | 1 |
| `kiln` | — | 1 |
| `lancedb` | — | 1 |
| `langfuse` | — | 1 |
| `litellm` | `litellm` | 1 |
| `netlify` | `netlify` | 1 |
| `opik` | — | 1 |
| `postgresql` | — | 1 |
| `rig` | `rig` | 1 |
| `ruby-llm` | — | 1 |
| `spring-ai` | — | 1 |

## Licences

The licences the linked repositories declare are counted on [the sources page](sources.md#licences), beside what this repository's own licence covers.

## Stars by kind

Rows of each kind per star band, from GitHub's count at the last weekly refresh; a row without a repository has no count. The median is the band of the middle row (the lower of two). A band is a popularity signal, not a quality verdict, and says nothing about upkeep.

| Kind | Rows | With a star count | under 10 | ★10+ | ★100+ | ★1k+ | ★10k+ | ★100k+ | Median band |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Official docs (`official-docs`) | 31 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | ★1k+ |
| Integration (`integration`) | 35 | 24 | 8 | 6 | 1 | 3 | 5 | 1 | ★10+ |
| Project (`project`) | 670 | 649 | 354 | 175 | 85 | 19 | 14 | 2 | under 10 |
| Plugin (`plugin`) | 241 | 234 | 125 | 77 | 27 | 4 | 1 | 0 | under 10 |
| SDK (`sdk`) | 99 | 94 | 73 | 16 | 4 | 0 | 1 | 0 | under 10 |
| Snippet (`snippet`) | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Tutorial (`tutorial`) | 11 | 6 | 1 | 3 | 0 | 2 | 0 | 0 | ★10+ |
| Article (`article`) | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Video (`video`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Benchmark (`benchmark`) | 72 | 69 | 50 | 12 | 4 | 1 | 1 | 1 | under 10 |
| Discussion (`discussion`) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Jev-like alternative (`alternative`) | 72 | 59 | 12 | 22 | 17 | 6 | 2 | 0 | ★10+ |

## Languages by decision pattern

Rows per pattern recording each of the 6 most recorded languages; the rest share one column. A row recording two languages counts in both, and a row filed under two patterns counts in both.

| Pattern | `python` | `typescript` | `javascript` | `rust` | `go` | `swift` | Other languages |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 91 | 88 | 45 | 3 | 4 | 6 | 1 |
| [Intent routing](by-pattern/intent-routing.md) | 18 | 14 | 3 | 0 | 1 | 0 | 2 |
| [Context compaction](by-pattern/context-compaction.md) | 10 | 22 | 4 | 1 | 0 | 0 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 50 | 60 | 20 | 4 | 5 | 0 | 4 |
| [Output validation](by-pattern/output-validation.md) | 45 | 54 | 19 | 7 | 3 | 1 | 4 |
| [Retry control](by-pattern/retry-control.md) | 3 | 2 | 1 | 0 | 0 | 1 | 1 |
| [Human escalation](by-pattern/human-escalation.md) | 44 | 22 | 1 | 1 | 0 | 0 | 2 |
| [Model routing](by-pattern/model-routing.md) | 18 | 21 | 9 | 1 | 0 | 1 | 0 |
| [Speculative fan-out](by-pattern/fan-out.md) | 17 | 13 | 3 | 1 | 1 | 1 | 4 |
| [Search & ranking](by-pattern/search-ranking.md) | 29 | 21 | 5 | 7 | 3 | 0 | 4 |
| [Structured extraction](by-pattern/data-extraction.md) | 10 | 3 | 4 | 0 | 0 | 0 | 0 |
| [Classification](by-pattern/classification.md) | 45 | 35 | 25 | 3 | 1 | 0 | 14 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 5 | 2 | 1 | 0 | 0 | 0 | 0 |
| [Document triage](by-pattern/document-triage.md) | 7 | 5 | 7 | 2 | 0 | 0 | 0 |
| [Support triage](by-pattern/support-triage.md) | 5 | 2 | 0 | 0 | 1 | 0 | 3 |
| [Content scoring](by-pattern/content-scoring.md) | 70 | 59 | 24 | 4 | 1 | 1 | 8 |
| [Recommendation](by-pattern/recommendation.md) | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 177 | 119 | 45 | 24 | 31 | 8 | 52 |

## Patterns filed together

298 rows are filed under more than one pattern. The 10 pairs most often filed on the same row:

| Patterns | Rows |
| --- | --- |
| [Safety gating](by-pattern/safety-gating.md) + [Output validation](by-pattern/output-validation.md) | 31 |
| [Tool selection](by-pattern/tool-selection.md) + [Safety gating](by-pattern/safety-gating.md) | 27 |
| [Human escalation](by-pattern/human-escalation.md) + [Content scoring](by-pattern/content-scoring.md) | 27 |
| [Classification](by-pattern/classification.md) + [Content scoring](by-pattern/content-scoring.md) | 25 |
| [Safety gating](by-pattern/safety-gating.md) + [Content scoring](by-pattern/content-scoring.md) | 22 |
| [Output validation](by-pattern/output-validation.md) + [Content scoring](by-pattern/content-scoring.md) | 22 |
| [Safety gating](by-pattern/safety-gating.md) + [Classification](by-pattern/classification.md) | 21 |
| [Tool selection](by-pattern/tool-selection.md) + [Output validation](by-pattern/output-validation.md) | 19 |
| [Safety gating](by-pattern/safety-gating.md) + [Human escalation](by-pattern/human-escalation.md) | 19 |
| [Tool selection](by-pattern/tool-selection.md) + [Content scoring](by-pattern/content-scoring.md) | 18 |

## Authors

1137 rows name an author; they name 1033 different ones, compared by display name without regard to case. 960 of them have one row here, 58 two, and 15 three or more; the most any one author has is 11. No author is named on this page: it shows how concentrated the catalogue is, not who contributes to it.

## Over time

The catalogue's counts at each weekly refresh, from the snapshots in `history/` (generated data, never a source): 4 since 2026-09-30, the newest 4 shown. A count is what was catalogued on that day, not how the ecosystem grew; a dash is a count that snapshot did not record.

| Snapshot | Entries | With code | Rows citing a call site | Independent reports | Negative results | Alternatives | No licence declared |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-30 | 1210 | 1182 | 1076 | 71 | 5 | 58 | 198 |
| 2026-10-08 | 1214 | 1185 | 1078 | 71 | 5 | 59 | 197 |
| 2026-10-14 | 1217 | 1186 | 1079 | 72 | 5 | 59 | 196 |
| 2026-10-21 | 1218 | 1187 | 1079 | 72 | 5 | 60 | 194 |

---

Generated by `scripts/build_shape.py` from `catalog.json`, `compat.json`, `patterns.json`, the entry schema and the snapshots in `history/`; edit those, not this page.
