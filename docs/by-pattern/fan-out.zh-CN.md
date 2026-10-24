# 并行扇出

<sub>[awesome-jev](../../README.zh-CN.md) · [English](fan-out.md)</sub>

_把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。_

这个决策的全部已收录例子 —— 共 34 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#并行扇出)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#fan-out)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#fan-out)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 3 · 调用点 26 · 接口形态 1 · 仅示例 0 · 独立报告 1 · 负面结果 0 · 未引用文件 7。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) <sub>`官方文档` · `Py`</sub>
- [Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) <sub>`官方文档` · `Py`</sub>
- [Quickstart](https://docs.typesafe.ai/introduction/quickstart) <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

## 本仓库的示例

本仓库 [`examples/`](../../examples/) 里归在这个模式下的代码。每一条在下文也都列出，附有摘要；[示例的 README](../../examples/README.md) 说明了它们核验到了哪一步。 <sub>(机翻)</sub>

- [Example: speculative fan-out](../../examples/03-fan-out/main.py) <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>
- [Example: three primitives in one request](../../examples/01-three-primitives/main.py) <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · ⚠ `代码未实测`</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

- **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐ — 对一篇长文提 13 个合规问题，证明全部打包进一次调用便宜得多、也快得多，而答案不变。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐ — 把大量问题（包括可能用不上的）打包进一次请求，之后再由代码决定哪些答案真的用得上。
  <sub>`官方文档` · `Py`</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。
  <sub>`开源项目` · ★10k+ · Browser Use · `Py` · `choice` · 调用点 [`jev_ultrafast/model.py`](https://github.com/browser-use/jev-ultrafast/blob/HEAD/jev_ultrafast/model.py)，2026-09-22 阅读 · ⚠ `厂商自报数据`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。
  <sub>`开源项目` · ★10k+ · `Go` · `noul` · 调用点 [`backend/internal/pkg/typesafe/client.go`](https://github.com/Wei-Shaw/sub2api/blob/HEAD/backend/internal/pkg/typesafe/client.go)，2026-09-22 阅读</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · 调用点 [`apps/server/src/jev/client.ts`](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts)，2026-09-22 阅读</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 并非 Jev：一套合成决策数据、训练并校准小型候选打分模型（JevForge-0.8B）、再通过兼容 Jev 的 API 提供服务的工具链，首个场景是在网页上挑选下一次点击或表单控件。其基准脚本把同一批留出的 choice、noul 和 score 问题发给真正的 Jev 作对比。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · zwlijay · `Py` · 引用文件 [`jevforge/bench_jev.py`](https://github.com/zwliJay/jev-forge/blob/HEAD/jevforge/bench_jev.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[VideoJev](https://github.com/MCG-NJU/VideoJev)** — 开源 System One 视频模型，在共享视频前缀上对多个问题的时间候选和多选答案直接打分，返回区间、答案和候选概率，无需生成文本。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · Yuhan Zhu and collaborators · `Py` · ⚠ `并非 Jev 本身` `代码未实测` `作者自荐`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · prasanthj · `C++` · 调用点 [`benchmarks/live.py`](https://github.com/prasanthj/duckdb-jev/blob/HEAD/benchmarks/live.py)，2026-09-22 阅读</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · kbhuw · `JS` · 调用点 [`dist/server.mjs`](https://github.com/kbhuw/jev-sift/blob/HEAD/dist/server.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · reachjalil · `TS` · 调用点 [`benchmarks/run.mjs`](https://github.com/reachjalil/jev-tree/blob/HEAD/benchmarks/run.mjs)，2026-09-22 阅读</sub>

- **[jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed)** — 对一大堆文本（工单、评论、日志）批量回答同一个问题：把多个条目打包进每次请求，并称吞吐量是逐条请求的 32 倍、成本低 41%。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · collapseindex · `Py` · 调用点 [`src/jev_ultralightspeed/_settings.py`](https://github.com/collapseindex/jev-ultralightspeed/blob/HEAD/src/jev_ultralightspeed/_settings.py)，2026-09-24 阅读 · ⚠ `宣称未核实`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。
  <sub>`开源项目` · ★10+ · `TS` · `choice` · 调用点 [`server/src/jev.ts`](https://github.com/emrickgarrett/OneVOneJev/blob/HEAD/server/src/jev.ts)，2026-09-22 阅读 · ⚠ `代码未实测` `无许可证`</sub>

- **[pi-typesafe](https://github.com/DevMortimer/pi-typesafe)** — 给 Pi 用的 Jev 决策：批量评估工具、终端 playground，以及给扩展作者的类型化 API。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · devmortimer · `TS` · 调用点 [`src/client.ts`](https://github.com/DevMortimer/pi-typesafe/blob/HEAD/src/client.ts)，2026-09-24 阅读</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — 基于规则的文本评分器：每条规则并行跑过每一行，不跳读、不漏行。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · lukstei · `TS` · 调用点 [`src/providers/jev.ts`](https://github.com/lukstei/slop-grader/blob/HEAD/src/providers/jev.ts)，2026-09-22 阅读</sub>

- **[system-one](https://github.com/sgoedecke/system-one)** — 面向开源语言模型的批量单 token 选择推理，兼容 TypeSafe 协议。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sgoedecke · `Py` · 调用点 [`system_one/inference.py`](https://github.com/sgoedecke/system-one/blob/HEAD/system_one/inference.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。
  <sub>`代码片段` · `Py` · `choice` · `noul` · 调用点 [`examples/03-fan-out/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/03-fan-out/main.py)，2026-09-22 阅读 · ⚠ `代码未实测`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。
  <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · 调用点 [`examples/01-three-primitives/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/01-three-primitives/main.py)，2026-09-22 阅读 · ⚠ `代码未实测`</sub>

- **[jackalope](https://github.com/Jackalope-Dev/jackalope)** — 面向编程智能体、并行 Git worktree 与代码审查的桌面工作区。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jackalope-dev · `Rs` · 调用点 [`apps/desktop/src-tauri/src/commands/jev.rs`](https://github.com/Jackalope-Dev/jackalope/blob/HEAD/apps/desktop/src-tauri/src/commands/jev.rs)，2026-09-22 阅读</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。
  <sub>`平台集成` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench)** — 实测：在一次调用里向 TypeSafe Jev 提 N 个问题，state 只计费一次。基于 2,976 次真实请求，附原始数据和精确的计费核对。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · blowxian · `Py` · 调用点 [`bench.py`](https://github.com/blowxian/jev-fanout-bench/blob/HEAD/bench.py)，2026-09-24 阅读</sub>

- **[jev-pr-judge](https://github.com/juanegido/jev-pr-judge)** — 用 TypeSafe System One（Jev）为拉取请求给出类型化结论：一次并行调用，策略写在代码里，可作为 GitHub Action 使用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · juanegido · `TS` · 调用点 [`dist/action/index.js`](https://github.com/juanegido/jev-pr-judge/blob/HEAD/dist/action/index.js)，2026-09-24 阅读</sub>

- **[jev-switchboard](https://github.com/ZIJIAN004/jev-switchboard)** — 给并行编程智能体的 JEV 门控语义通信层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · zijian004 · `JS` · 调用点 [`src/jev.mjs`](https://github.com/ZIJIAN004/jev-switchboard/blob/HEAD/src/jev.mjs)，2026-09-22 阅读</sub>

- **[JevGPT: Thinking Fast and Slow in Autonomous Research](https://github.com/sunyasheng/JevGPT)** — 论文 arXiv 2610.18272 的研究 Agent。GPT-5.5 规划检索并写出答案；在 BrowseComp-Plus 问答中，对每个被检查的文档区域和每个查询，Jev 回答一个 Choice（在编号的原文行中选出答案所在行）和一个 Noul（该区域是否涉及该查询），在多个文档上并行运行。GPT 拿到的是原文行。 <sub>(机翻)</sub>
  <sub>`开源项目` · sunyasheng · `TS` · `Py` · `choice` · `noul` · 调用点 [`runtime/pi-serini/src/extensions/jev_find_v1.ts`](https://github.com/sunyasheng/JevGPT/blob/HEAD/runtime/pi-serini/src/extensions/jev_find_v1.ts) · ⚠ `需第三方密钥` `宣称未核实` `作者自荐`</sub>

- **[jevswiftsdk](https://github.com/NSStudent/JevSwiftSDK)** — 独立、非官方、零依赖的 System One API Swift SDK：choice、noul 和 score 问题都映射为 Swift 类型（比如对枚举的 choice），具名批量问题一次调用作答并逐个校验答案，支持按策略重试和取消。支持 iOS 15+、macOS 12+ 和 Linux。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · nsstudent · `Swift` · 调用点 [`Sources/JevSwiftSDK/Configuration.swift`](https://github.com/NSStudent/JevSwiftSDK/blob/HEAD/Sources/JevSwiftSDK/Configuration.swift)，2026-09-22 阅读</sub>

- **[psearch](https://github.com/komikat/psearch)** — 给终端与智能体的并行网页搜索，带本地 Chromium 与 Jev 引导的探索。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · komikat · `Py` · 调用点 [`psearch.py`](https://github.com/komikat/psearch/blob/HEAD/psearch.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — 由并行 Jev 判断控制的贪吃蛇，每个游戏 tick 一次 API 调用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · siroccomask · `Py` · 调用点 [`jev_controller.py`](https://github.com/siroccomask/snake-jev/blob/HEAD/jev_controller.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[sqlite-jev](https://github.com/mgaitan/sqlite-jev)** — 为 SQLite 提供批量的自然语言判断，由 TypeSafe Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · mgaitan · `C` · 调用点 [`src/jev.c`](https://github.com/mgaitan/sqlite-jev/blob/HEAD/src/jev.c)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — 用通用分类器做扩散风格像素画：256 个并行像素问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · wizhill05 · `TS` · 调用点 [`fix_synthesizer.py`](https://github.com/Wizhill05/typesafe-image-diffusion/blob/HEAD/fix_synthesizer.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase)** — 展示 Jev 的 Next.js 界面：并行 Noul 判断与实时结果。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ashadeepa · `TS` · 调用点 [`lib/typesafe-client.ts`](https://github.com/Ashadeepa/typesafe-showcase/blob/HEAD/lib/typesafe-client.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。
  <sub>`教程` · `TS` · `noul` · `choice` · `score`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
