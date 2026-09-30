<!-- Written by scripts/build_shape.py from catalog.json, compat.json, patterns.json, the entry schema and history/. Edit those, not this file. -->

# 目录的形状

<sub>[awesome-jev](../README.zh-CN.md) · [English](shape.md)</sub>

> 本页中文说明由模型撰写（机翻），未经人工审校。

把本目录当作一个数据集来描述的计数，每当 `catalog.json` 变化就重新生成；其背后最新一次链接检查的日期是 **2026-09-30**。这些数字描述的是目录收录了什么——即经由兄弟目录、本仓库的发现流程和贡献者进入目录的内容——而不是整个生态。star 区间是热度信号，不是质量结论；这里的一切都没有被本仓库运行或复现。`python3 scripts/counts.py` 以文本形式打印同样的数字；主要数字见[状态页](status.md)。

## 按决策模式看证据

目录对归入每个模式的行记录了什么：只是计数，不是结论。一行在所有适用的列里都计数，归入几个模式就在几个模式下计数。**官方文档**是 TypeSafe AI 自己的文档页（`kind: official-docs`）。**调用点**、**接口形态**和**仅示例**按 `evidence.kind` 记录的文件内容，统计引用了文件的行：项目调用 Jev 的位置；只采用了 Jev 的请求结构、并非基于 Jev 构建的文件；项目附带的示例。**独立报告**是没有标 `vendor-reported` 的基准测试行：测量是其作者的，未经本仓库复现。**负面结果**是作者本人为该用途测过 Jev、并得出不利于它的结论的行（作者自述；[在状态页列出](status.md#negative-results)）。**未引用文件**统计没有 `evidence` 的行（`evidence_none` 可能说明了原因）。MCP server 的 `list_patterns` 和每个模式的页面给出同样的数字。

| 模式 | 行数 | 官方文档 | 调用点 | 接口形态 | 仅示例 | 独立报告 | 负面结果 | 未引用文件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [工具选择](by-pattern/tool-selection.zh-CN.md) | 230 | 3 | 222 | 4 | 0 | 12 | 1 | 4 |
| [意图路由](by-pattern/intent-routing.zh-CN.md) | 35 | 3 | 25 | 0 | 0 | 2 | 0 | 10 |
| [上下文压缩](by-pattern/context-compaction.zh-CN.md) | 34 | 0 | 34 | 0 | 0 | 2 | 2 | 0 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) | 139 | 2 | 133 | 2 | 0 | 10 | 0 | 4 |
| [输出校验](by-pattern/output-validation.zh-CN.md) | 134 | 2 | 129 | 1 | 0 | 11 | 0 | 4 |
| [重试控制](by-pattern/retry-control.zh-CN.md) | 7 | 0 | 6 | 1 | 0 | 0 | 0 | 0 |
| [人工升级](by-pattern/human-escalation.zh-CN.md) | 69 | 7 | 54 | 5 | 0 | 10 | 0 | 10 |
| [模型路由](by-pattern/model-routing.zh-CN.md) | 44 | 2 | 38 | 1 | 0 | 0 | 1 | 5 |
| [并行扇出](by-pattern/fan-out.zh-CN.md) | 32 | 3 | 25 | 1 | 0 | 1 | 0 | 6 |
| [检索与排序](by-pattern/search-ranking.zh-CN.md) | 64 | 3 | 60 | 0 | 0 | 6 | 1 | 4 |
| [结构化抽取](by-pattern/data-extraction.zh-CN.md) | 17 | 4 | 13 | 0 | 0 | 1 | 0 | 4 |
| [分类](by-pattern/classification.zh-CN.md) | 120 | 4 | 110 | 1 | 0 | 12 | 1 | 9 |
| [机器学习特征抽取](by-pattern/feature-extraction.zh-CN.md) | 8 | 1 | 7 | 0 | 0 | 0 | 0 | 1 |
| [文档分拣](by-pattern/document-triage.zh-CN.md) | 20 | 0 | 19 | 0 | 0 | 2 | 0 | 1 |
| [工单分拣](by-pattern/support-triage.zh-CN.md) | 8 | 1 | 4 | 0 | 0 | 0 | 0 | 4 |
| [内容评分](by-pattern/content-scoring.zh-CN.md) | 166 | 2 | 157 | 5 | 0 | 9 | 1 | 4 |
| [实时推荐](by-pattern/recommendation.zh-CN.md) | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| [总览](by-pattern/overview.zh-CN.md) | 451 | 6 | 370 | 45 | 0 | 23 | 1 | 36 |

有 23 份独立报告只归入了 `overview`、没有归入任何其他模式，所以在有人把它们归入所测的决策之前，这张表无法把它们计入那个决策。

## 语言

记录了每种语言的行数（`languages`；一行可以记录多种语言）。有 28 行没有记录语言。

| 语言 | 行数 |
| --- | --- |
| `python` | 458 |
| `typescript` | 403 |
| `javascript` | 152 |
| `rust` | 52 |
| `go` | 42 |
| `swift` | 16 |
| `java` | 15 |
| `ruby` | 12 |
| `shell` | 10 |
| `kotlin` | 8 |
| `csharp` | 7 |
| `elixir` | 7 |
| `php` | 7 |
| `c` | 5 |
| `cpp` | 4 |
| `haskell` | 1 |
| `lua` | 1 |

## 各行如何接入 Jev

`platforms` 记录一行如何接入 Jev。发现流程不会标注它：`scripts/discover_candidates.py` 及其生成的草稿都把这个字段留给添加该行的人，而没有人写明其他路径时，一行记录的就是 `typesafe-api`。所以下面第一组的数字至少同样反映了这个默认值，而不只是发现：经由透传接入 Jev 的行也可能只记录 `typesafe-api`（见[兼容性](compatibility.md)）。每行恰好计入一组。

| 分组 | 行数 |
| --- | --- |
| 只有 `typesafe-api` | 1091 |
| 至少有一个值对应[兼容性表](compatibility.md)中的其他接入面（网关、SDK 或框架），且不含 `self-hosted` | 35 |
| 除 `typesafe-api` 外只记录没有任何兼容性接入面对应的值（示例运行所在的主机、工具或框架，或该表未描述的路径），且不含 `self-hosted` | 29 |
| 含 `self-hosted`，无论还记录了什么 | 39 |
| 未记录任何值 | 17 |

各行记录的每个值，以及对应它的兼容性接入面：

| 值 | 兼容性接入面 | 行数 |
| --- | --- | --- |
| `typesafe-api` | `typesafe-native` | 1118 |
| `self-hosted` | — | 39 |
| `vercel-ai-gateway` | `vercel-eval`, `vercel-compat` | 15 |
| `claude-code` | — | 9 |
| `openrouter` | `openrouter` | 6 |
| `github` | — | 4 |
| `langchain` | `langchain` | 4 |
| `jevai-org` | — | 3 |
| `mcp` | — | 3 |
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

## 许可证

被链接仓库声明的许可证统计在[来源页](sources.md#licences)，旁边说明了本仓库自身许可覆盖的范围。

## 按类型看 star

每种类型在各 star 区间的行数，取自最近一次每周刷新时 GitHub 的计数；没有仓库的行没有计数。中位数是居中那一行所在的区间（两行居中时取较低者）。区间是热度信号，不是质量结论，也不说明是否有人维护。

| 类型 | 行数 | 有 star 计数 | 不足 10 | ★10+ | ★100+ | ★1k+ | ★10k+ | ★100k+ | 中位区间 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 官方文档 (`official-docs`) | 31 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | ★1k+ |
| 平台集成 (`integration`) | 34 | 24 | 8 | 6 | 1 | 3 | 5 | 1 | ★10+ |
| 开源项目 (`project`) | 655 | 652 | 367 | 172 | 82 | 15 | 14 | 2 | 不足 10 |
| 插件 (`plugin`) | 238 | 238 | 139 | 70 | 25 | 3 | 1 | 0 | 不足 10 |
| SDK (`sdk`) | 94 | 93 | 71 | 18 | 3 | 0 | 1 | 0 | 不足 10 |
| 代码片段 (`snippet`) | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| 教程 (`tutorial`) | 9 | 6 | 2 | 2 | 0 | 2 | 0 | 0 | ★10+ |
| 文章 (`article`) | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| 视频 (`video`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| 基准测试 (`benchmark`) | 71 | 69 | 52 | 10 | 4 | 1 | 1 | 1 | 不足 10 |
| 讨论 (`discussion`) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Jev 替代实现 (`alternative`) | 58 | 57 | 13 | 24 | 13 | 5 | 2 | 0 | ★10+ |

## 按决策模式看语言

每个模式下记录了最常见的 6 种语言各自的行数；其余语言合为一列。记录两种语言的行在两列都计数，归入两个模式的行在两个模式下都计数。

| 模式 | `python` | `typescript` | `javascript` | `rust` | `go` | `swift` | 其他语言 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [工具选择](by-pattern/tool-selection.zh-CN.md) | 89 | 83 | 45 | 4 | 4 | 5 | 1 |
| [意图路由](by-pattern/intent-routing.zh-CN.md) | 18 | 13 | 3 | 0 | 1 | 0 | 1 |
| [上下文压缩](by-pattern/context-compaction.zh-CN.md) | 10 | 20 | 3 | 1 | 0 | 0 | 0 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) | 46 | 61 | 20 | 5 | 4 | 0 | 4 |
| [输出校验](by-pattern/output-validation.zh-CN.md) | 45 | 52 | 19 | 8 | 3 | 1 | 4 |
| [重试控制](by-pattern/retry-control.zh-CN.md) | 2 | 2 | 1 | 0 | 0 | 1 | 1 |
| [人工升级](by-pattern/human-escalation.zh-CN.md) | 41 | 22 | 0 | 1 | 0 | 0 | 2 |
| [模型路由](by-pattern/model-routing.zh-CN.md) | 16 | 19 | 9 | 0 | 0 | 1 | 0 |
| [并行扇出](by-pattern/fan-out.zh-CN.md) | 15 | 12 | 3 | 1 | 1 | 1 | 4 |
| [检索与排序](by-pattern/search-ranking.zh-CN.md) | 28 | 19 | 5 | 7 | 2 | 0 | 4 |
| [结构化抽取](by-pattern/data-extraction.zh-CN.md) | 10 | 3 | 4 | 0 | 0 | 0 | 0 |
| [分类](by-pattern/classification.zh-CN.md) | 41 | 36 | 24 | 3 | 0 | 0 | 13 |
| [机器学习特征抽取](by-pattern/feature-extraction.zh-CN.md) | 4 | 2 | 1 | 1 | 0 | 0 | 0 |
| [文档分拣](by-pattern/document-triage.zh-CN.md) | 7 | 4 | 6 | 2 | 0 | 0 | 0 |
| [工单分拣](by-pattern/support-triage.zh-CN.md) | 5 | 2 | 0 | 0 | 1 | 0 | 3 |
| [内容评分](by-pattern/content-scoring.zh-CN.md) | 69 | 59 | 25 | 6 | 1 | 1 | 8 |
| [实时推荐](by-pattern/recommendation.zh-CN.md) | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| [总览](by-pattern/overview.zh-CN.md) | 165 | 118 | 45 | 24 | 29 | 8 | 50 |

## 一起归档的模式

有 286 行归入了不止一个模式。最常出现在同一行上的 10 对模式：

| 模式 | 行数 |
| --- | --- |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [输出校验](by-pattern/output-validation.zh-CN.md) | 30 |
| [工具选择](by-pattern/tool-selection.zh-CN.md) + [安全闸门](by-pattern/safety-gating.zh-CN.md) | 28 |
| [人工升级](by-pattern/human-escalation.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 27 |
| [分类](by-pattern/classification.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 24 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [分类](by-pattern/classification.zh-CN.md) | 23 |
| [输出校验](by-pattern/output-validation.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 23 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 22 |
| [工具选择](by-pattern/tool-selection.zh-CN.md) + [输出校验](by-pattern/output-validation.zh-CN.md) | 19 |
| [工具选择](by-pattern/tool-selection.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 17 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [人工升级](by-pattern/human-escalation.zh-CN.md) | 17 |

## 作者

有 1093 行写明了作者，共 986 位不同的作者（按显示名比较，不区分大小写）。其中 911 位在本目录只有一行，60 位有两行，15 位有三行或更多；单个作者最多有 11 行。本页不列出任何作者的名字：它显示的是目录的集中程度，而不是谁在贡献。

## 随时间的变化

自 2026-09-30 起开始收集：`history/` 中目前有 1 份快照，每次每周刷新一份。从第三份起，这里会出现一张计数变化表。

---

由 `scripts/build_shape.py` 根据 `catalog.json`、`compat.json`、`patterns.json`、条目 schema 与 `history/` 中的快照生成；请修改这些文件，不要改本页。
