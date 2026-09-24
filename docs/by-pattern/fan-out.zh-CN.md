# 并行扇出

<sub>[awesome-jev](../../README.zh-CN.md) · [English](fan-out.md)</sub>

_把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。_

这个决策的全部已收录例子 —— 共 32 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#并行扇出)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐ — 对一篇长文提 13 个合规问题，证明全部打包进一次调用便宜得多、也快得多，而答案不变。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐ — 把大量问题（包括可能用不上的）打包进一次请求，之后再由代码决定哪些答案真的用得上。
  <sub>`官方文档` · `Py`</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★187,515 · `Py` · `choice` · `score` · `noul`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。
  <sub>`开源项目` · ★42,557 · `Go` · `noul`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。
  <sub>`开源项目` · ★19,261 · Browser Use · `Py` · `choice` · ⚠ `厂商自报数据`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★4,578 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★94 · `TS` · `choice` · `noul`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★46 · kbhuw · `JS` · ⚠ `无许可证`</sub>

- **[pi-typesafe](https://github.com/DevMortimer/pi-typesafe)** — 给 Pi 用的 Jev 决策：批量评估工具、终端 playground，以及给扩展作者的类型化 API。 <sub>(机翻)</sub>
  <sub>`插件` · ★45 · devmortimer · `TS`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 面向 Jev 式决策模型的开源训练与推理栈。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★34 · zwlijay · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[system-one](https://github.com/sgoedecke/system-one)** — 面向开源语言模型的批量单 token 选择推理，兼容 TypeSafe 协议。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★33 · sgoedecke · `Py` · ⚠ `无许可证`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。
  <sub>`开源项目` · ★30 · `TS` · `choice` · ⚠ `代码未实测` `无许可证`</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — 基于规则的文本评分器：每条规则并行跑过每一行，不跳读、不漏行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★22 · lukstei · `TS`</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — 对一大堆文本（工单、评论、日志）批量回答同一个问题：把多个条目打包进每次请求，并称吞吐量是逐条请求的 32 倍、成本低 41%。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · collapseindex · `Py` · ⚠ `宣称未核实`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · reachjalil · `TS`</sub>

- **[jevswiftsdk](https://github.com/NSStudent/JevSwiftSDK)** — 独立的类型安全 Swift SDK，支持 async/await、批处理与重试。 <sub>(机翻)</sub>
  <sub>`SDK` · ★8 · nsstudent · `Swift`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · prasanthj · `C++`</sub>

- **[sqlite-jev](https://github.com/mgaitan/sqlite-jev)** — 为 SQLite 提供批量的自然语言判断，由 TypeSafe Jev 驱动。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · mgaitan · `C` · ⚠ `无许可证`</sub>

- **[jev-pr-judge](https://github.com/juanegido/jev-pr-judge)** — 用 TypeSafe System One（Jev）为拉取请求给出类型化结论：一次并行调用，策略写在代码里，可作为 GitHub Action 使用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · juanegido · `TS`</sub>

- **[jackalope](https://github.com/Jackalope-Dev/jackalope)** — 面向编程智能体、并行 Git worktree 与代码审查的桌面工作区。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jackalope-dev · `Rs`</sub>

- **[jev-switchboard](https://github.com/ZIJIAN004/jev-switchboard)** — 给并行编程智能体的 JEV 门控语义通信层。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · zijian004 · `JS`</sub>

- **[psearch](https://github.com/komikat/psearch)** — 给终端与智能体的并行网页搜索，带本地 Chromium 与 Jev 引导的探索。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · komikat · `Py`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — 由并行 Jev 判断控制的贪吃蛇，每个游戏 tick 一次 API 调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · siroccomask · `Py`</sub>

- **[typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase)** — 展示 Jev 的 Next.js 界面：并行 Noul 判断与实时结果。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ashadeepa · `TS` · ⚠ `无许可证`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。
  <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。
  <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · ⚠ `代码未实测`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。
  <sub>`平台集成` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench)** — 实测：在一次调用里向 TypeSafe Jev 提 N 个问题，state 只计费一次。基于 2,976 次真实请求，附原始数据和精确的计费核对。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · blowxian · `Py`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — 用通用分类器做扩散风格像素画：256 个并行像素问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · wizhill05 · `TS` · ⚠ `无许可证`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。
  <sub>`教程` · `TS` · `noul` · `choice` · `score`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
