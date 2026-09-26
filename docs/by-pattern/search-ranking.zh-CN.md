# 检索与排序

<sub>[awesome-jev](../../README.zh-CN.md) · [English](search-ranking.md)</sub>

_对来自廉价检索步骤的候选做打分或重排。_

这个决策的全部已收录例子 —— 共 65 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#检索与排序)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐ — 对一份服务条款做语义检索：一次请求用 Choice 给 218 个行号打分，同时用 Noul 判断文档里到底有没有答案。
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐ — 对 40 个法律检索问题各取 30 条 BM25 候选，按「问题-候选」逐对提问重排，top-1 与 top-10 准确率均大幅提升。
  <sub>`官方文档` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)** — 单次批量请求里对每个候选文档问一个 Noul，直接把「是」的概率当相关性分数。
  <sub>`开源项目` · ★38,571 · `Py` · `noul`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。
  <sub>`开源项目` · ★27,886 · `Py` · `choice` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。
  <sub>`开源项目` · ★20,069 · `Rs` · `noul`</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)** — 向量数据库的重排器：对每条结果问一个 Noul，把「是」的概率当作绝对相关性分数 —— 可以跨查询比较。
  <sub>`开源项目` · ★11,513 · `Py` · `noul`</sub>

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)** — 为代码审查预选上下文：每个候选文件问一个 Score —— 测了两次后被移除：计费输入明显增加、耗时几乎没有收益；离线回放还表明，候选列表根本够不到审查发现实际所在的位置。
  <sub>`基准测试` · ★8,617 · `Go` · `score`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★5,414 · `Java` · `choice` · `score` · `noul`</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — 受生物启发的智能体记忆：衰减、检索强化与巩固。零运行时依赖，基于 SQLite。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★756 · kitfunso · `TS`</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。
  <sub>`开源项目` · ★443 · `TS` · `choice` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★324 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[vector-graph-rag](https://github.com/zilliztech/vector-graph-rag)** — 纯向量检索的 Graph RAG，在多跳推理场景上达到当前最好水平。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★248 · zilliztech · `Py`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接 40 家 AI 供应商，覆盖生成、流式与决策三种推理形态。 <sub>(机翻)</sub>
  <sub>`插件` · ★139 · juspay · `TS`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — 按含义 grep，跨语言：Jev 给每一行按含义打分，可用 AND/OR/NOT 组合多个含义。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★134 · uehaj · `JS`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。
  <sub>`开源项目` · ★126 · `Py` · `choice`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — 用当前会话上下文给智能体的技能排序以决定下一步，带 Claude Code hook。
  <sub>`插件` · ★116 · dicklesworthstone · `Rs`</sub>

- **[jev-shell-history](https://github.com/mrnugget/jev-shell-history)** — Fish 风格的 zsh 历史自动建议，由 Jev 排序而不是按时间。
  <sub>`开源项目` · ★108 · mrnugget · `TS` · ⚠ `无许可证`</sub>

- **[jegrep](https://github.com/can1357/jegrep)** — 语义 grep：用描述来找代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★87 · can1357 · `Rs`</sub>

- **[warrenduffer](https://github.com/arimanyus/warrenduffer)** — 面向印度股票的 AI 日内交易机器人：Jev 每 15 秒给 Nifty 50 排序，代码决定每笔交易的仓位并下单。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★86 · arimanyus · `TS`</sub>

- **[jgrep](https://github.com/keltokhy/jgrep)** — grep，但模式是一段描述：用 Jev 按含义过滤行，约 200 毫秒处理上千行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★74 · keltokhy · `Py`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★69 · `TS` · `choice` · ⚠ `无许可证`</sub>

- **[jevgrep](https://github.com/nassim-arifette/jevgrep)** — 为编码智能体提供由 Jev 驱动的语义代码搜索：通过 CLI 或 MCP 跨仓库查找某种行为，并给出精确的源码位置。 <sub>(机翻)</sub>
  <sub>`插件` · ★62 · nassim-arifette · `TS`</sub>

- **[milvus-model](https://github.com/milvus-io/milvus-model)** — 把 OpenAI、SentenceTransformers 等嵌入与重排模型集成进来的库，用于 Milvus 等向量数据库中的语义检索；Jev 是其中一个可用的重排器。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★60 · milvus-io · `Py`</sub>

- **[jev-recall](https://github.com/samdotmak/jev-recall)** — 按相关性而非相似度召回：用 Jev 过滤 AI 助手的记忆。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★33 · samdotmak · `TS`</sub>

- **[pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)** — 用 Jev 给当前任务的 Pi Agent 技能排序。 <sub>(机翻)</sub>
  <sub>`插件` · ★30 · safzanpirani · `TS`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★24 · kyu1204 · `TS` · `noul` · `choice` · `score` · ⚠ `宣称未核实`</sub>

- **[laya-jev-GraphRAG](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG)** — 一个智能体式 GraphRAG 引擎，可切换 System One 决策模型（本地 Laya 或云端 Jev）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★22 · bodepudimuneendra-netizen · `Py`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20 · keeltrace · `Py`</sub>

- **[jev-reranker](https://github.com/hotchpotch/jev-reranker)** — 用 Jev 为 Python 的 RAG 做相关性过滤与重排。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20 · hotchpotch · `Py`</sub>

- **[Cheshi](https://github.com/CheshiAI/Cheshi)** — 由 Jev 驱动的对话记忆：找回过去的会话，并结合原始来源重新审视当时的决策。一个 macOS 工作区。 <sub>(机翻)</sub>
  <sub>`插件` · ★18 · cheshiai · `C`</sub>

- **[transcript-lens](https://github.com/sensahin/transcript-lens)** — 按含义浏览 YouTube 字幕：土耳其语界面、由 Jev 分析、可导出字幕，并附 Vercel 部署说明。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · sensahin · `TS`</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — 可复现的基准：衡量 Jev 在 RAG 里的重排质量、延迟与成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★14 · erendikmenn · `Py`</sub>

- **[jevql](https://github.com/kylemclaren/jevql)** — 给 Postgres 用的语义 SQL，由 Jev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · kylemclaren · `Go`</sub>

- **[pi-jev](https://github.com/madeye/pi-jev)** — 用 Jev 辅助文件检索与请求缓存，让 Pi 工作流更快。 <sub>(机翻)</sub>
  <sub>`插件` · ★11 · madeye · `TS`</sub>

- **[every](https://github.com/sufianetaouil/every)** — 对代码库里每一个函数问一个是非问题，几秒内得到排序结果 —— 模式本身是一个问题的 grep。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · sufianetaouil · `Py`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — 与专用重排模型在 14 个数据集上的独立横评。
  <sub>`基准测试` · ★7 · anessbelbati · `Py`</sub>

- **[jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval)** — TypeSafe Jev 重排能否胜过向量检索？在 Agent Skills Hub 目录上做分级相关性评测（9,831 对、164 条中英文查询），并测量了“裁判循环”偏差。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · zhuyansen · `Py`</sub>

- **[oko](https://github.com/bartlomein/oko)** — 通过 MCP 为 Codex、Claude Code 与 OpenCode 做代码检索：直接给出相关源码片段，让智能体少读无关代码。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · bartlomein · `Rs` · ⚠ `宣称未核实`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · shivampansuriya · `JS`</sub>

- **[jev.nvim](https://github.com/valentynkit/jev.nvim)** — Neovim 插件：向当前缓冲区提问，得到 quickfix 列表。Treesitter 切分函数，Jev 给每个函数打分，概率以虚拟文本显示。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · valentynkit · `Lua`</sub>

- **[jevsearch](https://github.com/kylemclaren/jevsearch)** — shadcn/ui 的 ⌘K 站内搜索组件：先用本地关键词匹配立即出结果，再把前 20 条一次性发给 Jev（每个候选一个 Noul、一个选出最佳页面的 Choice、一个判断是否有页面能回答的 Noul），据此重排或剔除结果；TypeSafe 变慢或不可用时保留关键词排序。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · kylemclaren · `TS` · `noul` · `choice` · ⚠ `宣称未核实`</sub>

- **[askgrep](https://github.com/fajarhide/askgrep)** — 为那些写不成正则的问题而生的 grep：逐个读取每个函数而不是抽样，由 TypeSafe Jev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · fajarhide · `Rs`</sub>

- **[jev-nlgrep](https://github.com/YehuiTang0316/jev-nlgrep)** — 用自然语言 grep 按含义搜索代码与文本。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · yehuitang0316 · `TS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — 由 Jev 驱动的 LlamaIndex 重排器与路由器 —— 类型化的分数与选择，比 LLM-as-judge 便宜。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · wiktorb2004 · `Py`</sub>

- **[pijev](https://github.com/tonyzdev/pijev)** — PiJev：Jev 参与循环的终端编码智能体——在第一次调用前由 Jev 给仓库文件排序，并挑选技能。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · tonyzdev · `TS`</sub>

- **[jev-assist](https://github.com/glud123/jev-assist)** — 别让昂贵的主模型干「grep 加猜」的粗活 —— 让 Jev 先把整个仓库排一遍序。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · glud123 · `JS`</sub>

- **[jev-reranker](https://github.com/shinpr/jev-reranker)** — 用 Jev 对 JSON 搜索结果做重排、过滤与压缩。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · shinpr · `Rs`</sub>

- **[typesafe-mod](https://github.com/BeLazy167/typesafe-mod)** — Claude Code 模组：把决策路由给 Jev，逐会话给已安装技能排序。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · belazy167 · `TS`</sub>

- **[agent-seek](https://github.com/Gitmaxd/agent-seek)** — Agent Seek——为智能体提供精准的网页召回：You.com 负责发现，TypeSafe Jev 负责排序。提供 MCP 与 REST。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · gitmaxd · `Py`</sub>

- **[Jev RAG](https://github.com/aifabrice/jev-rag)** — 用 SQLite FTS5/BM25 索引本地文档，再对每个候选文段询问一个 Jev Noul，按返回的相关性概率重排，并可选生成带引用的回答。
  <sub>`开源项目` · ★2 · aifabrice · `Py` · `noul` · ⚠ `需第三方密钥` `疑似 AI 生成`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · hamakyo · `TS`</sub>

- **[JevPDF](https://github.com/kylemclaren/jevpdf)** — 按语义搜索 PDF：pdf.js 在浏览器里逐页提取文本行，Jev 对每一行回答一个 Noul（“这一行是否回答了查询？”），每批最多 16 行、共享整页文本作为 state；概率不低于 0.55 的行被高亮并按概率排序。只发送文本，API key 由服务端代理持有。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · kylemclaren · `TS` · `noul`</sub>

- **[jfind](https://github.com/religa/jfind)** — 用自然语言描述来找文件：带语义 --like 条件的 find(1)，由 TypeSafe.ai 的 jev 回答。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · religa · `Py`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — 给 Codex 与 Claude Code 的非官方社区 MCP 插件，用 Jev 做有界路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · e-fl · `JS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — 面向 AI 智能体的决策层：约 400 毫秒、两百分之一美分的类型化校准决策，用于拦截工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · eugeniughelbur · `Py`</sub>

- **[jevgrep](https://github.com/allebee/jevgrep)** — 按含义 grep：管道传入任意文本，用大白话问一个是非问题，只留下匹配的行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · allebee · `Py`</sub>

- **[clay-jev-people-ranker](https://github.com/promptgtm-shared/clay-jev-people-ranker)** — 面向 Clay 的智能体技能与 Python 工作流：用 TypeSafe Jev 做线索评分、B2B 潜在客户筛选与人物搜索排序。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · promptgtm-shared · `Py`</sub>

- **[jev-bfs](https://github.com/komikat/jev-bfs)** — 用 Jev 直接排序来跑维基百科链接竞速，带实时终端显示。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · komikat · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · yodablocks · `Py`</sub>

- **[jev-retrieval](https://github.com/romeromarcelo/jev-retrieval)** — 语义化的代码与文档检索 CLI：BM25 负责召回，TypeSafe Jev 负责校准后的精确筛选。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · romeromarcelo · `Rs`</sub>

- **[Jevflix](https://github.com/ArielBubis/Jevflix)** — Jev 来挑，你来看。一个混合电影推荐器：快速的语义加关键词检索把 4,800 部电影缩小成短名单，再由 TypeSafe Jev 读懂你的请求并挑选。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · arielbubis · `Py`</sub>

- **[sift](https://github.com/tylergibbs1/sift)** — 用 TypeSafe Jev 重排 Google 搜索结果的 Chrome 扩展，并收起销售页面和 SEO 填充内容。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · tylergibbs1 · `TS`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
