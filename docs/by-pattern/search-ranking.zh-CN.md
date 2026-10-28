# 检索与排序

<sub>[awesome-jev](../../README.zh-CN.md) · [English](search-ranking.md)</sub>

_对来自廉价检索步骤的候选做打分或重排。_

这个决策的全部已收录例子 —— 共 71 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#检索与排序)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#search-ranking)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#search-ranking)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 3 · 调用点 67 · 接口形态 0 · 仅示例 0 · 独立报告 6 · 负面结果 1 · 未引用文件 4。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) <sub>`官方文档` · `Py`</sub>
- [Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find) <sub>`官方文档` · `Py` · `choice` · `noul`</sub>
- [Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) <sub>`官方文档` · `Py`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐ — 对一份服务条款做语义检索：一次请求用 Choice 给 218 个行号打分，同时用 Noul 判断文档里到底有没有答案。
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐ — 对 40 个法律检索问题各取 30 条 BM25 候选，按「问题-候选」逐对提问重排，top-1 与 top-10 准确率均大幅提升。
  <sub>`官方文档` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。
  <sub>`开源项目` · ★10k+ · `Py` · `choice` · `noul` · 调用点 [`fastmcp_slim/fastmcp/experimental/transforms/jev_search.py`](https://github.com/PrefectHQ/fastmcp/blob/HEAD/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)，2026-09-22 阅读</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。
  <sub>`开源项目` · ★10k+ · `Rs` · `noul` · 调用点 [`crates/jcode-base/src/jev.rs`](https://github.com/1jehuang/jcode/blob/HEAD/crates/jcode-base/src/jev.rs)，2026-09-22 阅读</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)** — 向量数据库的重排器：对每条结果问一个 Noul，把「是」的概率当作绝对相关性分数 —— 可以跨查询比较。
  <sub>`开源项目` · ★10k+ · `Py` · `noul` · 调用点 [`python/python/lancedb/rerankers/typesafe.py`](https://github.com/lancedb/lancedb/blob/HEAD/python/python/lancedb/rerankers/typesafe.py)，2026-09-22 阅读</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)** — 单次批量请求里对每个候选文档问一个 Noul，直接把「是」的概率当相关性分数。
  <sub>`开源项目` · ★10k+ · `Py` · `noul` · 调用点 [`openviking/models/rerank/jev_rerank.py`](https://github.com/volcengine/OpenViking/blob/HEAD/openviking/models/rerank/jev_rerank.py)，2026-09-22 阅读</sub>

- **[XERJ](https://github.com/xerj-org/xerj)** — 一个本地优先的搜索引擎兼 MCP 服务器，打包为单个 Rust 二进制文件。可选的 `rerank` 阶段对每条靠前结果向 Jev 提一个 `noul`（`document` 是否回答了 state 中的查询？），再按概率重新排序。作者报告 FiQA 上的 nDCG@10 从 0.24 升至 0.36，总共 648 次搜索花费约 0.64 美元。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10k+ · xerj-org · `Rs` · `noul` · 调用点 [`engine/crates/xerj-rerank/src/lib.rs`](https://github.com/xerj-org/xerj/blob/HEAD/engine/crates/xerj-rerank/src/lib.rs)，2026-10-26 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★1k+ · `Java` · `choice` · `score` · `noul` · 调用点 [`app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-09-22 阅读</sub>

- **[jevgrep (dzhng)](https://github.com/dzhng/jevgrep)** — 一个命令行工具和 Agent 技能，用“这段代码做什么”来找代码：`jg "遥测事件是如何记录的？" ./repo` 让 Jev 在目录、文件和声明层面判断相关性，返回相关文件、阅读线索和原文摘录。作者报告在 10 个 SWE-bench 任务上同样解决 8 个，成本约低 30%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · dzhng · `TS` · `noul` · 调用点 [`packages/core/test-node/provider-protocol.mjs`](https://github.com/dzhng/jevgrep/blob/HEAD/packages/core/test-node/provider-protocol.mjs)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)** — 为代码审查预选上下文：每个候选文件问一个 Score —— 测了两次后被移除：计费输入明显增加、耗时几乎没有收益；离线回放还表明，候选列表根本够不到审查发现实际所在的位置。
  <sub>`基准测试` · ★1k+ · `Go` · `score` · 作者结论：不利（作者自述，未经本仓库复现）</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · 调用点 [`sql/jev--0.2.0.sql`](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql)，2026-09-22 阅读</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — 受生物启发的智能体记忆：衰减、检索强化与巩固。零运行时依赖，基于 SQLite。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★100+ · kitfunso · `TS` · 调用点 [`src/rerankers/jev.ts`](https://github.com/kitfunso/hippo-memory/blob/HEAD/src/rerankers/jev.ts)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jegrep](https://github.com/can1357/jegrep)** — 不建索引、不用向量嵌入的代码语义 grep：用 Jev 的 noul 先判断每个路径、再判断读到的段落是否符合你的描述，每个都给出“是”的概率，所以阈值在各批之间可比；结果以行范围返回。作者估计，在几千个文件中做一次典型搜索约花 0.005 美元。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · can1357 · `Rs` · 调用点 [`src/jev.rs`](https://github.com/can1357/jegrep/blob/HEAD/src/jev.rs)，2026-09-22 阅读</sub>

- **[jev-doc-search](https://github.com/VectifyAI/jev-doc-search)** — 教程：用 Jev 的 `Choice` 在长 PDF 中找到回答问题的那一页。短文档每页一个选项；长文档则沿 PageIndex 树逐层向下，每层对章节标题和摘要做一次小规模 `Choice`，从而避开 255 个选项和 32k token 的上限。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`教程` · ★100+ · VectifyAI · `Py` · `choice` · 调用点 [`page_search.py`](https://github.com/VectifyAI/jev-doc-search/blob/HEAD/page_search.py)，2026-10-26 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts)，2026-09-22 阅读</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · 调用点 [`src/lib/typesafe.ts`](https://github.com/superagents-lab/jev-search/blob/HEAD/src/lib/typesafe.ts)，2026-09-22 阅读</sub>

- **[jev-semgrep](https://github.com/uehaj/sys1grep)** — 按含义 grep 的工具，现名 sys1grep：对每一行，Jev 回答一个 noul，判断这一行是否符合给定含义（例如“网络故障”），再由阈值决定是否匹配。多个含义可用 AND、OR、NOT 组合，可先用正则预筛行，含义和文本可以是不同语言。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · uehaj · `JS` · 调用点 [`semgrep.mjs`](https://github.com/uehaj/sys1grep/blob/HEAD/semgrep.mjs)，2026-09-22 阅读</sub>

- **[jev-shell-history](https://github.com/mrnugget/jev-shell-history)** — Fish 风格的 zsh 历史自动建议，由 Jev 排序而不是按时间。
  <sub>`开源项目` · ★100+ · mrnugget · `TS` · 调用点 [`src/cli.ts`](https://github.com/mrnugget/jev-shell-history/blob/HEAD/src/cli.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev4pg](https://github.com/Sheltercosmo/jev4pg)** — 为 PostgreSQL 提供自然语言 SQL 和 41 个语义算子。过滤、抽取、排序、匹配和核验以有上限的批次交给 Jev，答案须先通过校验；choice 选项需达 0.55、noul 需达 0.8 才算成立。作者报告其准确率为 98%，pg-jev 的请求路径为 92%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · Sheltercosmo · `Py` · `choice` · `noul` · 调用点 [`sdd/generic/jev.py`](https://github.com/Sheltercosmo/jev4pg/blob/HEAD/sdd/generic/jev.py)，2026-10-26 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jevgrep](https://github.com/nassim-arifette/jevgrep)** — 为不知道符号名的智能体做的代码搜索：把已授权的仓库切成片段，对每个片段用一个 Jev noul 判断它是否回答了你的问题，再返回原样的代码摘录及其路径和行号；可通过命令行或本地 MCP 使用。远程调用默认关闭，需按项目开启。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · nassim-arifette · `TS` · 调用点 [`experiments/jev-contract/probe.mjs`](https://github.com/nassim-arifette/jevgrep/blob/HEAD/experiments/jev-contract/probe.mjs)，2026-09-24 阅读</sub>

- **[jgrep](https://github.com/keltokhy/jgrep)** — 以描述为模式的 grep：每一行变成一个 Jev noul，默认概率达到 0.5 即算匹配；并发判断、按输入顺序输出，所以也能用在 tail -f 上。作者在 994 条 Hacker News 标题上测得，一条描述用时 4.6 秒、花费 0.012 美元。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · keltokhy · `Py` · 调用点 [`bench/code_review.py`](https://github.com/keltokhy/jgrep/blob/HEAD/bench/code_review.py)，2026-09-22 阅读</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。
  <sub>`开源项目` · ★100+ · `Py` · `choice` · 调用点 [`src/neo4jev/navigator.py`](https://github.com/jexp/neo4jev/blob/HEAD/src/neo4jev/navigator.py)，2026-09-22 阅读</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接多家 AI 供应商，覆盖生成、流式与决策三种推理形态；决策由 TypeSafe Jev 或开源权重的 Laya 返回类型化、经过校准的判断，而非文本。 <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · juspay · `TS` · 调用点 [`src/lib/providers/typesafe.ts`](https://github.com/juspay/neurolink/blob/HEAD/src/lib/providers/typesafe.ts)，2026-09-22 阅读</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — 用当前会话上下文给智能体的技能排序以决定下一步，带 Claude Code hook。
  <sub>`插件` · ★100+ · dicklesworthstone · `Rs` · 调用点 [`src/jev/endpoint.rs`](https://github.com/Dicklesworthstone/skillranker/blob/HEAD/src/jev/endpoint.rs)，2026-09-22 阅读</sub>

- **[vector-graph-rag](https://github.com/zilliztech/vector-graph-rag)** — 把实体和关系作为向量存进 Milvus 的 Graph RAG，无需图数据库。两阶段 Jev 重排先针对查询给每条候选关系提一个 noul，再给排名靠前的关系所指向的段落打分；按作者的测试，在 MuSiQue 和 2Wiki（各 1,000 题）上平均 Recall@5 为 86.61%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · zilliztech · `Py` · 调用点 [`src/vector_graph_rag/llm/jev.py`](https://github.com/zilliztech/vector-graph-rag/blob/HEAD/src/vector_graph_rag/llm/jev.py)，2026-09-22 阅读</sub>

- **[warrenduffer](https://github.com/arimanyus/warrenduffer)** — 面向印度股票的日内交易机器人，下的是真实订单，没有模拟盘：Jev 分两轮给 Nifty 50 成分股排序，并决定止盈和离场；代码负责每笔仓位、设置止损，并在触及每日亏损上限时停止交易，经 Zerodha Kite 或 Kotak Neo 下单。回放功能可在过去某一天的数据上跑同一套循环。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · arimanyus · `TS` · 调用点 [`src/model/jev.ts`](https://github.com/arimanyus/warrenduffer/blob/HEAD/src/model/jev.ts)，2026-09-24 阅读</sub>

- **[狗头军师 Jev Chat](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat)** — 聊天回复助手（桌面悬浮窗、Android 悬浮助手、iOS 键盘），基于 Jev Android。它根据可见对话或截图向 Jev 询问字面问题、对方意图、危险程度、是否现在回复以及最佳行动，再让 Jev 在起草的回复中挑选。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · shengjidaguai-china · `Kt` · `choice` · `score` · `noul` · 调用点 [`integrations/jev_android/app/src/main/java/com/jev/probe/jev/JevQuestions.kt`](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat/blob/HEAD/integrations/jev_android/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-10-26 模型阅读 · ⚠ `需第三方密钥`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★10+ · `TS` · `choice` · 调用点 [`src/search.ts`](https://github.com/ellipsis-dev/blink/blob/HEAD/src/search.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[Cheshi](https://github.com/CheshiAI/Cheshi)** — 由 Jev 驱动的对话记忆：找回过去的会话，并结合原始来源重新审视当时的决策。一个 macOS 工作区。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · cheshiai · `C` · 调用点 [`desktop/lib/typesafe-connection.mts`](https://github.com/CheshiAI/Cheshi/blob/HEAD/desktop/lib/typesafe-connection.mts)，2026-09-24 阅读</sub>

- **[grev](https://github.com/aurorainfra/grev)** — 用提问代替模式匹配的 Unix 过滤工具：`grev 'is a vegan meal' menu.txt` 只保留 Jev 回答“是”的行；配套工具还会用到 choice 的置信度或路径分数。默认固定 jev-1.13.0，因为阈值是按模型版本调的。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · aurorainfra · `Go` · 调用点 [`internal/jev/price.go`](https://github.com/aurorainfra/grev/blob/HEAD/internal/jev/price.go)，2026-10-24 模型阅读</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · keeltrace · `Py` · 调用点 [`hermes_nerve/client.py`](https://github.com/keeltrace/hermes-nerve/blob/HEAD/hermes_nerve/client.py)，2026-09-22 阅读</sub>

- **[Jev RAG](https://github.com/aifabrice/jev-rag)** — 用 SQLite FTS5/BM25 索引本地文档，再对每个候选文段询问一个 Jev Noul，按返回的相关性概率重排，并可选生成带引用的回答。
  <sub>`开源项目` · ★10+ · aifabrice · `Py` · `noul` · 调用点 [`local_kb.py`](https://github.com/aifabrice/jev-rag/blob/HEAD/local_kb.py)，2026-09-26 阅读 · ⚠ `需第三方密钥` `疑似 AI 生成` `作者自荐`</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — 可复现的基准：衡量 Jev 在 RAG 里的重排质量、延迟与成本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · erendikmenn · `Py` · 调用点 [`src/jev_rag_benchmark/rerankers.py`](https://github.com/erendikmenn/jev-rag-benchmark/blob/HEAD/src/jev_rag_benchmark/rerankers.py)，2026-09-22 阅读 · 作者结论：有利（作者自述，未经本仓库复现）</sub>

- **[jev-recall](https://github.com/samdotmak/jev-recall)** — 按相关性而非相似度召回：用 Jev 过滤 AI 助手的记忆。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · samdotmak · `TS` · 调用点 [`src/jev_recall/core.py`](https://github.com/samdotmak/jev-recall/blob/HEAD/src/jev_recall/core.py)，2026-09-22 阅读</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — 与专用重排模型在 14 个数据集上的独立横评。
  <sub>`基准测试` · ★10+ · anessbelbati · `Py` · 调用点 [`rerankers/jev.py`](https://github.com/anessbelbati/jev-rerank-bench/blob/HEAD/rerankers/jev.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-reranker](https://github.com/hotchpotch/jev-reranker)** — 用 Jev 为 Python 的 RAG 做相关性过滤与重排。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · hotchpotch · `Py` · 调用点 [`src/jev_reranker/reranker.py`](https://github.com/hotchpotch/jev-reranker/blob/HEAD/src/jev_reranker/reranker.py)，2026-09-24 阅读</sub>

- **[jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval)** — TypeSafe Jev 重排能否胜过向量检索？在 Agent Skills Hub 目录上做分级相关性评测（9,831 对、164 条中英文查询），并测量了“裁判循环”偏差。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · zhuyansen · `Py` · 调用点 [`src/jse/openrouter.py`](https://github.com/zhuyansen/jev-search-rerank-eval/blob/HEAD/src/jse/openrouter.py)，2026-09-24 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[JevGPT: Thinking Fast and Slow in Autonomous Research](https://github.com/sunyasheng/JevGPT)** — 论文 arXiv 2610.18272 的研究 Agent。GPT-5.5 规划检索并写出答案；在 BrowseComp-Plus 问答中，对每个被检查的文档区域和每个查询，Jev 回答一个 Choice（在编号的原文行中选出答案所在行）和一个 Noul（该区域是否涉及该查询），在多个文档上并行运行。GPT 拿到的是原文行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sunyasheng · `TS` · `Py` · `choice` · `noul` · 调用点 [`runtime/pi-serini/src/extensions/jev_find_v1.ts`](https://github.com/sunyasheng/JevGPT/blob/HEAD/runtime/pi-serini/src/extensions/jev_find_v1.ts) · ⚠ `需第三方密钥` `宣称未核实` `作者自荐`</sub>

- **[jevql](https://github.com/kylemclaren/jevql)** — 给 Postgres 用的语义 SQL，由 Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kylemclaren · `Go` · 调用点 [`sdk/go/jevql.go`](https://github.com/kylemclaren/jevql/blob/HEAD/sdk/go/jevql.go)，2026-09-22 阅读</sub>

- **[jevsearch](https://github.com/kylemclaren/jevsearch)** — shadcn/ui 的 ⌘K 站内搜索组件：先用本地关键词匹配立即出结果，再把前 20 条一次性发给 Jev（每个候选一个 Noul、一个选出最佳页面的 Choice、一个判断是否有页面能回答的 Noul），据此重排或剔除结果；TypeSafe 变慢或不可用时保留关键词排序。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kylemclaren · `TS` · `noul` · `choice` · 调用点 [`src/lib/jev-search-server.ts`](https://github.com/kylemclaren/jevsearch/blob/HEAD/src/lib/jev-search-server.ts)，2026-09-23 阅读 · ⚠ `宣称未核实` `作者自荐`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · 调用点 [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts)，2026-09-23 阅读 · ⚠ `宣称未核实` `作者自荐`</sub>

- **[laya-jev-GraphRAG](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG)** — 一个智能体式 GraphRAG 引擎，可切换 System One 决策模型（本地 Laya 或云端 Jev）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · bodepudimuneendra-netizen · `Py` · 调用点 [`graphrag_neo4j_laya/graphrag/models/jev.py`](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG/blob/HEAD/graphrag_neo4j_laya/graphrag/models/jev.py)，2026-09-24 阅读</sub>

- **[milvus-model](https://github.com/milvus-io/milvus-model)** — 把 OpenAI、SentenceTransformers 等嵌入与重排模型集成进来的库，用于 Milvus 等向量数据库中的语义检索；Jev 是其中一个可用的重排器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · milvus-io · `Py` · 调用点 [`src/pymilvus/model/reranker/jev.py`](https://github.com/milvus-io/milvus-model/blob/HEAD/src/pymilvus/model/reranker/jev.py)，2026-09-24 阅读</sub>

- **[oko](https://github.com/bartlomein/oko)** — 通过 MCP 为 Codex、Claude Code 与 OpenCode 做代码检索：直接给出相关源码片段，让智能体少读无关代码。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · bartlomein · `Rs` · 调用点 [`scripts/benchmark-public/replay/replay.py`](https://github.com/bartlomein/oko/blob/HEAD/scripts/benchmark-public/replay/replay.py)，2026-09-24 阅读 · ⚠ `宣称未核实`</sub>

- **[pi-jev](https://github.com/madeye/pi-jev)** — 用 Jev 辅助文件检索与请求缓存，让 Pi 工作流更快。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · madeye · `TS` · 调用点 [`src/jev.ts`](https://github.com/madeye/pi-jev/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)** — 用 Jev 给当前任务的 Pi Agent 技能排序。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · safzanpirani · `TS` · 调用点 [`extensions/jev.ts`](https://github.com/safzanpirani/pi-jev-skill-picker/blob/HEAD/extensions/jev.ts)，2026-09-22 阅读</sub>

- **[transcript-lens](https://github.com/sensahin/transcript-lens)** — 按含义浏览 YouTube 字幕：土耳其语界面、由 Jev 分析、可导出字幕，并附 Vercel 部署说明。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sensahin · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/sensahin/transcript-lens/blob/HEAD/src/lib/jev.ts)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[agent-seek](https://github.com/Gitmaxd/agent-seek)** — Agent Seek——为智能体提供精准的网页召回：You.com 负责发现，TypeSafe Jev 负责排序。提供 MCP 与 REST。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · gitmaxd · `Py` · 调用点 [`packages/core/rank/jev.py`](https://github.com/Gitmaxd/agent-seek/blob/HEAD/packages/core/rank/jev.py)，2026-09-24 阅读</sub>

- **[askgrep](https://github.com/fajarhide/askgrep)** — 为那些写不成正则的问题而生的 grep：逐个读取每个函数而不是抽样，由 TypeSafe Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · fajarhide · `Rs` · 调用点 [`src/jev.rs`](https://github.com/fajarhide/askgrep/blob/HEAD/src/jev.rs)，2026-09-24 阅读</sub>

- **[clay-jev-people-ranker](https://github.com/promptgtm-shared/clay-jev-people-ranker)** — 面向 Clay 的智能体技能与 Python 工作流：用 TypeSafe Jev 做线索评分、B2B 潜在客户筛选与人物搜索排序。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · promptgtm-shared · `Py` · 调用点 [`scripts/rank_clay_people.py`](https://github.com/promptgtm-shared/clay-jev-people-ranker/blob/HEAD/scripts/rank_clay_people.py)，2026-09-24 阅读</sub>

- **[every](https://github.com/sufianetaouil/every)** — 对代码库里每一个函数问一个是非问题，几秒内得到排序结果 —— 模式本身是一个问题的 grep。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · sufianetaouil · `Py` · 调用点 [`reference/probe_jev.py`](https://github.com/sufianetaouil/every/blob/HEAD/reference/probe_jev.py)，2026-09-22 阅读</sub>

- **[jev-assist](https://github.com/glud123/jev-assist)** — 别让昂贵的主模型干「grep 加猜」的粗活 —— 让 Jev 先把整个仓库排一遍序。 <sub>(机翻)</sub>
  <sub>`开源项目` · glud123 · `JS` · 调用点 [`scripts/jev.mjs`](https://github.com/glud123/jev-assist/blob/HEAD/scripts/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-bfs](https://github.com/komikat/jev-bfs)** — 用 Jev 直接排序来跑维基百科链接竞速，带实时终端显示。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · komikat · `Py` · 调用点 [`jev_bfs/core.py`](https://github.com/komikat/jev-bfs/blob/HEAD/jev_bfs/core.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-nlgrep](https://github.com/YehuiTang0316/jev-nlgrep)** — 用自然语言 grep 按含义搜索代码与文本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · yehuitang0316 · `TS` · 调用点 [`src/jev.ts`](https://github.com/YehuiTang0316/jev-nlgrep/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · yodablocks · `Py` · 调用点 [`harness/client.py`](https://github.com/yodablocks/jev-orderby-bench/blob/HEAD/harness/client.py)，2026-09-22 阅读</sub>

- **[jev-reranker](https://github.com/shinpr/jev-reranker)** — 用 Jev 对 JSON 搜索结果做重排、过滤与压缩。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shinpr · `Rs` · 调用点 [`src/http.rs`](https://github.com/shinpr/jev-reranker/blob/HEAD/src/http.rs)，2026-09-22 阅读</sub>

- **[jev-retrieval](https://github.com/romeromarcelo/jev-retrieval)** — 语义化的代码与文档检索 CLI：BM25 负责召回，TypeSafe Jev 负责校准后的精确筛选。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · romeromarcelo · `Rs` · 调用点 [`src/jev/client.rs`](https://github.com/romeromarcelo/jev-retrieval/blob/HEAD/src/jev/client.rs)，2026-09-24 阅读</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · shivampansuriya · `JS` · 调用点 [`src/providers/typesafe.mjs`](https://github.com/ShivamPansuriya/jev-skill-gate/blob/HEAD/src/providers/typesafe.mjs)，2026-09-24 阅读</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · hamakyo · `TS` · 调用点 [`src/providers/jev-provider.ts`](https://github.com/hamakyo/jev-starter/blob/HEAD/src/providers/jev-provider.ts)，2026-09-22 阅读</sub>

- **[jev.nvim](https://github.com/valentynkit/jev.nvim)** — Neovim 插件：向当前缓冲区提问，得到 quickfix 列表。Treesitter 切分函数，Jev 给每个函数打分，概率以虚拟文本显示。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · valentynkit · `Lua` · 调用点 [`lua/jev/client.lua`](https://github.com/valentynkit/jev.nvim/blob/HEAD/lua/jev/client.lua)，2026-09-24 阅读</sub>

- **[Jevflix](https://github.com/ArielBubis/Jevflix)** — 电影推荐器：FAISS 与 BM25 检索把 4,800 部电影缩成短名单，Jev 读出请求里的约束（片长、不要血腥画面）供代码过滤，再由一次覆盖最多 250 个候选的 Jev choice 选出一部影片。没有把握时，由 LLM 权衡前五名或追问一个问题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arielbubis · `Py` · 调用点 [`movie_rec/jev_client.py`](https://github.com/ArielBubis/Jevflix/blob/HEAD/movie_rec/jev_client.py)，2026-09-24 阅读</sub>

- **[jevgrep](https://github.com/allebee/jevgrep)** — 按含义 grep：管道传入任意文本，用大白话问一个是非问题，只留下匹配的行。 <sub>(机翻)</sub>
  <sub>`开源项目` · allebee · `Py` · 调用点 [`src/jevgrep/judge.py`](https://github.com/allebee/jevgrep/blob/HEAD/src/jevgrep/judge.py)，2026-09-22 阅读</sub>

- **[JevPDF](https://github.com/kylemclaren/jevpdf)** — 按语义搜索 PDF：pdf.js 在浏览器里逐页提取文本行，Jev 对每一行回答一个 Noul（“这一行是否回答了查询？”），每批最多 16 行、共享整页文本作为 state；概率不低于 0.55 的行被高亮并按概率排序。只发送文本，API key 由服务端代理持有。 <sub>(机翻)</sub>
  <sub>`开源项目` · kylemclaren · `TS` · `noul` · 调用点 [`src/lib/jev-config.ts`](https://github.com/kylemclaren/jevpdf/blob/HEAD/src/lib/jev-config.ts)，2026-09-23 阅读 · ⚠ `作者自荐`</sub>

- **[jfind](https://github.com/religa/jfind)** — 用自然语言描述来找文件：带语义 --like 条件的 find(1)，由 TypeSafe.ai 的 jev 回答。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · religa · `Py` · 调用点 [`src/jfind/matcher.py`](https://github.com/religa/jfind/blob/HEAD/src/jfind/matcher.py)，2026-09-24 阅读</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — 由 Jev 驱动的 LlamaIndex 重排器与路由器 —— 类型化的分数与选择，比 LLM-as-judge 便宜。 <sub>(机翻)</sub>
  <sub>`开源项目` · wiktorb2004 · `Py` · 调用点 [`packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py`](https://github.com/WiktorB2004/llama-index-jev/blob/HEAD/packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py)，2026-09-22 阅读</sub>

- **[pijev](https://github.com/tonyzdev/pijev)** — PiJev：Jev 参与循环的终端编码智能体——在第一次调用前由 Jev 给仓库文件排序，并挑选技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tonyzdev · `TS` · 调用点 [`src/jev.ts`](https://github.com/tonyzdev/pijev/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[sift](https://github.com/tylergibbs1/sift)** — 用 TypeSafe Jev 重排 Google 搜索结果的 Chrome 扩展，并收起销售页面和 SEO 填充内容。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · tylergibbs1 · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/tylergibbs1/sift/blob/HEAD/src/jev/client.ts)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — 给 Codex 与 Claude Code 的非官方社区 MCP 插件，用 Jev 做有界路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · e-fl · `JS` · 调用点 [`server/judge.mjs`](https://github.com/E-FL/typesafe-as-a-judge/blob/HEAD/server/judge.mjs)，2026-09-22 阅读</sub>

- **[typesafe-mod](https://github.com/BeLazy167/typesafe-mod)** — Claude Code 模组：把决策路由给 Jev，逐会话给已安装技能排序。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · belazy167 · `TS` · 调用点 [`hooks/suggest.ts`](https://github.com/BeLazy167/typesafe-mod/blob/HEAD/hooks/suggest.ts)，2026-09-22 阅读</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
