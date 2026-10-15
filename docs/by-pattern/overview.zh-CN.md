# 总览

<sub>[awesome-jev](../../README.zh-CN.md) · [English](overview.md)</sub>

_介绍模型或整个领域，而非单一模式。_

这个决策的全部已收录例子 —— 共 453 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#总览)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=zh)还能按语言、原语和形态进一步筛选。

`overview` 在本目录里是什么意思、为什么只归在它下面的带代码项目算作尚未按模式索引，见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#overview)（由模型从[英文版](../patterns.md#overview)译写，以英文版为准）。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 6 · 调用点 370 · 接口形态 46 · 仅示例 0 · 独立报告 23 · 负面结果 1 · 未引用文件 37。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill) <sub>`官方文档` · `sh`</sub>
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) <sub>`插件` · `sh`</sub>
- [@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js) <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) <sub>`SDK` · `Py`</sub>
- [typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python) <sub>`SDK` · `Py` · `choice` · `score` · `noul`</sub>
- [API reference](https://docs.typesafe.ai/api) <sub>`官方文档` · `sh` · `Py` · `TS`</sub>
- [Models, pricing and limits](https://docs.typesafe.ai/models) <sub>`官方文档` · `sh` · `Py` · `TS`</sub>
- [Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives) <sub>`官方文档` · `Py` · `TS` · `choice` · `score` · `noul`</sub>
- [Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) <sub>`文章` · ⚠ `厂商自报数据`</sub>
- [Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) <sub>`官方文档`</sub>
- [Use case map](https://docs.typesafe.ai/concepts/use-case-map) <sub>`官方文档`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐ — 把 TypeSafe 官方技能装进 Claude Code，让智能体自己写出正确的 Jev 调用，不必每次手动贴 API 结构。
  <sub>`官方文档` · ★1k+ · `sh`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐ — 官方 TypeScript 客户端。同时提供 ESM、CJS 和类型声明，辅助函数是小写的 choice()/score()/noul()。
  <sub>`SDK` · ★100+ · `TS` · `JS` · `choice` · `score` · `noul` · 调用点 [`src/types.ts`](https://github.com/typesafe-ai/typesafe-sdk-js/blob/HEAD/src/types.ts)，2026-09-22 阅读</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐ — 一个可直接替换 TypeSafeClient 的适配器，底层走普通 LLM API —— 没有 Jev 权限也能跑 Jev 形状的代码。
  <sub>`SDK` · ★100+ · `Py` · 引用文件 [`src/system_one_adapter/_client.py`](https://github.com/typesafe-ai/system-one-adapter-python/blob/HEAD/src/system_one_adapter/_client.py)</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐ — 官方 Python 客户端。含同步与异步客户端、支持 retry-after 的重试策略，以及 Choice/Score/Noul 辅助类。
  <sub>`SDK` · ★100+ · `Py` · `choice` · `score` · `noul` · 调用点 [`src/typesafe_sdk/_core/client/aio/client.py`](https://github.com/typesafe-ai/typesafe-sdk-python/blob/HEAD/src/typesafe_sdk/_core/client/aio/client.py)，2026-09-22 阅读</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐ — POST /v1/systemone 的核心 Choice、Score、Noul 问题请求与应答结构，以及请求校验和 HTTP 错误处理。 <sub>(机翻)</sub>
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐ — 原生 Jev 1.14/1.13 的 ID、别名、价格与限制：输入 $0.042/Mtok，输出免费，默认每次请求 64k token、每个问题 32k。默认输入为文本；图像和 262k 长上下文需显式开启实验功能。 <sub>(机翻)</sub>
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐ — 核心 Choice、Score、Noul 问题类型的选择、组合与 criteria 写法；Choice 最多 255 个选项，Score 支持 2–10 级。 <sub>(机翻)</sub>
  <sub>`官方文档` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐ — 发布博文：什么是 System One 模型、为什么要把决策从生成里拆出来，以及厂商自报的延迟与成本数字。
  <sub>`文章` · Diogo Almeida · ⚠ `厂商自报数据`</sub>

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐ — 厂商列出的 Jev 1.13 局限：字面化理解、算术与计数、日期比较、间接指代、夹杂无关细节的长 state，以及对抗性内容。 <sub>(机翻)</sub>
  <sub>`官方文档`</sub>

- **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐ — 厂商自己的分类体系：五大类、十九个行业方向、十种决策形态（从分类一直到结构化数据抽取）。
  <sub>`官方文档`</sub>

- **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)** — 一个编程智能体，其托管网关转售 Jev，还提供一个免费档位的模型 id。
  <sub>`平台集成` · ★100k+ · `TS` · 调用点 [`packages/console/app/src/routes/zen/util/provider/systemone.ts`](https://github.com/anomalyco/opencode/blob/HEAD/packages/console/app/src/routes/zen/util/provider/systemone.ts)</sub>

- **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)** — 在 Jev 之上实现 Effect 的 DecisionModel 接口，并罕见地坦白说明取整行为尚未核实。
  <sub>`平台集成` · ★10k+ · `TS` · `choice` · `score` · `noul` · 调用点 [`packages/ai/typesafe/src/TypeSafeDecisionModel.ts`](https://github.com/Effect-TS/effect/blob/HEAD/packages/ai/typesafe/src/TypeSafeDecisionModel.ts)，2026-09-22 阅读</sub>

- **[ai](https://github.com/vercel/ai)** — TypeScript 的 AI 工具包，来自 Next.js 的作者们。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10k+ · vercel · `TS` · 调用点 [`examples/ai-functions/src/evaluate/typesafe-ai/basic.ts`](https://github.com/vercel/ai/blob/HEAD/examples/ai-functions/src/evaluate/typesafe-ai/basic.ts)，2026-09-22 阅读</sub>

- **[laya](https://github.com/NandhaKishorM/laya)** — 非自回归的 System 1 决策引擎：一次前向传播即可对任意文本给出 choice、score 与是非判断，支持 100 多种语言，并按请求路由到合适的检查点。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10k+ · nandhakishorm · `Py` · 引用文件 [`laya-ts/src/shortlist.ts`](https://github.com/NandhaKishorM/laya/blob/HEAD/laya-ts/src/shortlist.ts)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[litellm](https://github.com/BerriAI/litellm)** — 高性能 AI 网关：Rust 内核加 Python SDK，以 OpenAI 或原生格式调用上百种 LLM API。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · ★10k+ · berriai · `Py` · 调用点 [`litellm/proxy/guardrails/guardrail_hooks/typesafe/typesafe.py`](https://github.com/BerriAI/litellm/blob/HEAD/litellm/proxy/guardrails/guardrail_hooks/typesafe/typesafe.py)，2026-09-22 阅读</sub>

- **[openwork](https://github.com/different-ai/openwork)** — 某协作工具的开源替代品。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10k+ · different-ai · `TS` · 引用文件 [`.github/scripts/jev-test-coverage-review.mjs`](https://github.com/different-ai/openwork/blob/HEAD/.github/scripts/jev-test-coverage-review.mjs)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[decider](https://github.com/Mapika/decider)** — 一族 System One 风格的模型，从开源基座微调而来，做单次类型化决策。
  <sub>`Jev 替代实现` · ★1k+ · mapika · `Py` · 引用文件 [`decider/bench/loadtest.py`](https://github.com/Mapika/decider/blob/HEAD/decider/bench/loadtest.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[deep-searcher](https://github.com/zilliztech/deep-searcher)** — 开源的深度研究替代方案，在私有数据上推理与检索。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★1k+ · zilliztech · `Py` · 引用文件 [`evaluation/jev_stopping/run_full100.py`](https://github.com/zilliztech/deep-searcher/blob/HEAD/evaluation/jev_stopping/run_full100.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[jevlike](https://github.com/vinnylarouge/jevlike)** — 一个独立可训练的模型，输入输出形状与 Jev 相同：文本加 N 个选项进，每个选项一个概率出，单次前向完成。
  <sub>`Jev 替代实现` · ★1k+ · vinnylarouge · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[kev](https://github.com/jaredpalmer/kev)** — 一套可训练、可自托管的 Jev-like 决策模型，API 与 System One 兼容 —— 官方 SDK 可以直接指向你自己的服务。
  <sub>`Jev 替代实现` · ★1k+ · Jared Palmer · `Py` · `choice` · `score` · `noul` · 引用文件 [`playground/scripts/jev-evaluate.mjs`](https://github.com/jaredpalmer/kev/blob/HEAD/playground/scripts/jev-evaluate.mjs)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)** — 一个接进 adapter registry 的「JSON Schema 转问题」编译器，并诚实说明了它无法支持的场景。
  <sub>`平台集成` · ★1k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`libs/core/kiln_ai/adapters/jev/jev_client.py`](https://github.com/Kiln-AI/Kiln/blob/HEAD/libs/core/kiln_ai/adapters/jev/jev_client.py)，2026-09-22 阅读</sub>

- **[NanoJev](https://github.com/TianyuCodings/NanoJev)** — 自称 Jev 的「nano 复刻版」，用途是拿来读，不是拿来上生产。
  <sub>`Jev 替代实现` · ★1k+ · `Py` · 引用文件 [`scripts/jev_probe.mjs`](https://github.com/TianyuCodings/NanoJev/blob/HEAD/scripts/jev_probe.mjs) · ⚠ `并非 Jev 本身`</sub>

- **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)** — Rust 集成，选项数量在编译期检查 —— 超过 255 个选项的 Choice 会编译失败，而不是运行时才报错。
  <sub>`平台集成` · ★1k+ · `Rs` · `choice` · `score` · `noul` · 调用点 [`crates/rig-typesafeai/src/wire.rs`](https://github.com/0xPlaygrounds/rig/blob/HEAD/crates/rig-typesafeai/src/wire.rs)，2026-09-22 阅读</sub>

- **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)** — 带专门 System One 协议的 Ruby provider，是 Ruby 侧接入 Jev 的主要路径。
  <sub>`平台集成` · ★1k+ · `Rb` · `choice` · `score` · `noul` · 调用点 [`lib/ruby_llm/providers/typesafe.rb`](https://github.com/crmne/ruby_llm/blob/HEAD/lib/ruby_llm/providers/typesafe.rb)，2026-09-22 阅读</sub>

- **[SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev)** — 一个独立的「语义 if」实现，开门见山声明与 Jev 和 TypeSafe 无隶属关系。
  <sub>`Jev 替代实现` · ★1k+ · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[djev](https://github.com/mmastrac/djev)** — 在 DiffusionGemma 上做 Jev 式结构化决策的示例服务。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · mmastrac · `Py` · 引用文件 [`structured_server.py`](https://github.com/mmastrac/djev/blob/HEAD/structured_server.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[jeff](https://github.com/logan-markewich/jeff)** — 自托管的 Jev 直接替代品，底层由 GliFormer 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · logan-markewich · `Py` · 引用文件 [`bench/jevbench.py`](https://github.com/logan-markewich/jeff/blob/HEAD/bench/jevbench.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 —— 面向 Jev 这类类型化决策模型的基准。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★100+ · fstandhartinger · `Py` · 调用点 [`jevbench/adapters/typesafe.py`](https://github.com/fstandhartinger/jevbench/blob/HEAD/jevbench/adapters/typesafe.py)，2026-09-22 阅读</sub>

- **[jevcore](https://github.com/PerryLink/jevcore)** — 面向 DeepSeek Harness、MCP 与原生 Node 的 TypeSafe Jev 封装：返回带类型的判断而非文字，默认离线。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★100+ · perrylink · `TS` · 调用点 [`packages/cli/src/runtime.ts`](https://github.com/PerryLink/jevcore/blob/HEAD/packages/cli/src/runtime.ts)，2026-09-24 阅读</sub>

- **[jevk5](https://github.com/allebee/jevk5)** — JevK5：TypeSafe Jev 的开放权重替代品，一次前向传播即给出带概率的类型化决策，权重采用 Apache-2.0。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · allebee · `Py` · 引用文件 [`jevk5/prompt.py`](https://github.com/allebee/jevk5/blob/HEAD/jevk5/prompt.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[laya-server](https://github.com/1Panel-dev/laya-server)** — 为 Laya 结构化决策模型提供的自托管 API 与网页界面，兼容 TypeSafe Jev 的 API 格式。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · 1panel-dev · `TS` · 引用文件 [`backend/server/main.py`](https://github.com/1Panel-dev/laya-server/blob/HEAD/backend/server/main.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[localjev](https://github.com/githubnext/localjev)** — GitHub Next 用 TypeScript 写的本地 Jev 兼容 POST /v1/systemone 接口：在打过补丁的 vLLM 上，通过一步式结构化读取从 DiffusionGemma 模型得到概率。它重新实现的是协议，而不是模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · githubnext · `TS` · 引用文件 [`src/server.ts`](https://github.com/githubnext/localjev/blob/HEAD/src/server.ts)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[open-jev](https://github.com/daseinlabs/open-jev)** — 带自定义微调的开源 Jev 实现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · daseinlabs · `Py` · 引用文件 [`openjev/server.py`](https://github.com/daseinlabs/open-jev/blob/HEAD/openjev/server.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[Open-Jev](https://github.com/Zefan-Cai/Open-Jev)** — Open-Jev-27B：开放权重模型，针对给定的上下文、问题和候选项直接返回带类型的概率，而不生成答案——一个可以自己运行的 Jev 式决策模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · zefan-cai · `Py` · 引用文件 [`jev/eval_frontier.py`](https://github.com/Zefan-Cai/Open-Jev/blob/HEAD/jev/eval_frontier.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[openjev](https://github.com/razorback16/openjev)** — 基于开源扩散模型的 Jev 兼容决策服务。
  <sub>`Jev 替代实现` · ★100+ · razorback16 · `Py` · 引用文件 [`openjev/api.py`](https://github.com/razorback16/openjev/blob/HEAD/openjev/api.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[OpenJev](https://github.com/SiliconLabAI/OpenJev)** — 开源版 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · siliconlabai · `TS` · 引用文件 [`src/App.tsx`](https://github.com/SiliconLabAI/OpenJev/blob/HEAD/src/App.tsx)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[openjev-sglang](https://github.com/ekzhang/openjev-sglang)** — 用开源模型提供的 Jev 兼容端点，仅做 prefill。
  <sub>`Jev 替代实现` · ★100+ · ekzhang · `Py` · 引用文件 [`src/openjev/api.py`](https://github.com/ekzhang/openjev-sglang/blob/HEAD/src/openjev/api.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身` `无许可证` `已归档`</sub>

- **[rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow)** — Jev 的开源本地版：由 LLM 产出类型化决策，且不生成任何 token。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · rizzo-ai-academy · `Py` · 引用文件 [`src/rizzo_flow/compat.py`](https://github.com/Rizzo-AI-Academy/rizzo-flow/blob/HEAD/src/rizzo_flow/compat.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[simple-jev](https://github.com/featherless-ai/simple-jev)** — 通过读取 next-token logits，把任意开源权重模型变成 Jev 形状的端点 —— JSON 由服务端组装，而不是模型生成。
  <sub>`Jev 替代实现` · ★100+ · `Py` · 引用文件 [`hf-server/hf_server.py`](https://github.com/featherless-ai/simple-jev/blob/HEAD/hf-server/hf_server.py) · ⚠ `并非 Jev 本身`</sub>

- **[von](https://github.com/wfzyx/von)** — 开源的 System One 决策模型：非自回归、15 毫秒以内，可在本地替换 TypeSafe Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★100+ · wfzyx · `Py` · 引用文件 [`js/src/client.ts`](https://github.com/wfzyx/von/blob/HEAD/js/src/client.ts)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[advocaat](https://github.com/pithings/advocaat)** — 一个小巧的类型化客户端，用来对你自己的数据提问。
  <sub>`SDK` · ★10+ · pithings · `TS` · 调用点 [`src/api.ts`](https://github.com/pithings/advocaat/blob/HEAD/src/api.ts)，2026-09-22 阅读</sub>

- **[diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)** — 由 DiffusionGemma 与 SGLang 驱动的类 Jev 决策引擎——“长了眼睛的 Jev”。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · hangzhi · `Py` · 引用文件 [`scripts/compare_jevbench.py`](https://github.com/Hangzhi/diffusion-jev-sglang/blob/HEAD/scripts/compare_jevbench.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[dohnuts.cpp](https://github.com/DreamBlooms/dohnuts.cpp)** — 同样的决策，在 CPU 上完成。一个能在个人电脑上运行的 System One 模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · dreamblooms · `C++` · 引用文件 [`scripts/compare/ref_decider.py`](https://github.com/DreamBlooms/dohnuts.cpp/blob/HEAD/scripts/compare/ref_decider.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[fastjev](https://github.com/chengyongru/fastjev)** — 以 SDK 为先、独立维护的 SemIf 分支，用于快速的自托管语义决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · chengyongru · `Py` · 引用文件 [`demo/jev-ultrafast/record.py`](https://github.com/chengyongru/fastjev/blob/HEAD/demo/jev-ultrafast/record.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[go-jev](https://github.com/mattn/go-jev)** — TypeSafe Jev 的 Go SDK 与 CLI：从模型获得带类型的决策（是非、选择、评分）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · mattn · `Go` · 调用点 [`jev.go`](https://github.com/mattn/go-jev/blob/HEAD/jev.go)，2026-09-24 阅读</sub>

- **[hunch](https://github.com/carldaws/hunch)** — 面向 Ruby 与 Rails 的概率化控制流，由 TypeSafe Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · carldaws · `Rb` · 调用点 [`lib/hunch/configuration.rb`](https://github.com/carldaws/hunch/blob/HEAD/lib/hunch/configuration.rb)，2026-09-24 阅读</sub>

- **[jev (Elixir/OTP)](https://github.com/dannote/jev)** — 把 Jev 做成 OTP 进程：从 GenServer 回复，并对答案做模式匹配。
  <sub>`SDK` · ★10+ · dannote · `Ex` · 调用点 [`lib/jev/http.ex`](https://github.com/dannote/jev/blob/HEAD/lib/jev/http.ex)，2026-09-22 阅读</sub>

- **[jev-cli](https://github.com/tumf/jev-cli)** — 小巧的零依赖 Jev 命令行工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · tumf · `Py` · 调用点 [`src/jev_cli/__init__.py`](https://github.com/tumf/jev-cli/blob/HEAD/src/jev_cli/__init__.py)，2026-09-22 阅读</sub>

- **[jev-explained](https://github.com/davila7/jev-explained)** — Jev 讲解。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`教程` · ★10+ · davila7 · `TS` · 调用点 [`src/lib/providers.ts`](https://github.com/davila7/jev-explained/blob/HEAD/src/lib/providers.ts)，2026-09-24 阅读</sub>

- **[Jev-Quantum](https://github.com/karminski/Jev-Quantum)** — 兼容 Jev 协议的随机基线：讲 noul、choice、score，但不读提示词，答案来自高速伪随机数——可以当 mock，也可以作为路由评测的下界。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · karminski · `Rs` · 引用文件 [`crates/jev-quantum-bench/src/config.rs`](https://github.com/karminski/Jev-Quantum/blob/HEAD/crates/jev-quantum-bench/src/config.rs)，2026-09-24 阅读 · ⚠ `并非 Jev 本身` `仅一次提交`</sub>

- **[jev4k](https://github.com/pambrose/jev4k)** — Jev 的 Kotlin DSL 与客户端。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · pambrose · `Kt` · 调用点 [`src/main/kotlin/com/pambrose/jev4k/JevConfig.kt`](https://github.com/pambrose/jev4k/blob/HEAD/src/main/kotlin/com/pambrose/jev4k/JevConfig.kt)，2026-09-22 阅读</sub>

- **[jev_local](https://github.com/Argos1111/jev_local)** — 用本地 LLM 复刻 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · argos1111 · `Py` · 引用文件 [`tools/verify_api.py`](https://github.com/Argos1111/jev_local/blob/HEAD/tools/verify_api.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[JevAny](https://github.com/SimpleJev/JevAny)** — JevAny：面向强化学习、智能体与模型框架的校准决策层，一次预填充即可返回带类型的答案和选项概率——一个基于 Qwen 骨干的开放 27B 模型，并不是 Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · weitianxin · `Py` · 引用文件 [`jevany/api.py`](https://github.com/SimpleJev/JevAny/blob/HEAD/jevany/api.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[jevify](https://github.com/fidecastro/jevify)** — 把任意 LLM 以类 Jev 端点形式提供服务的极简方案。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · fidecastro · `Py` · 引用文件 [`jevify/api/app.py`](https://github.com/fidecastro/jevify/blob/HEAD/jevify/api/app.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[jevper](https://github.com/zhulinchng/jevper)** — 形似 Jev（TypeSafe System One）的分类封装，基于类 OpenAI 客户端：给出概率与置信度，而不是文本。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · zhulinchng · `Py` · 引用文件 [`src/jevper/types.py`](https://github.com/zhulinchng/jevper/blob/HEAD/src/jevper/types.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[learn-jev-end-to-end](https://github.com/harshithsunku/learn-jev-end-to-end)** — 端到端学习 Jev 的免费实践课程：用“快脑”（Jev）加“慢脑”（LLM）构建 13 个智能体用例，只需一个 OpenRouter key。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`教程` · ★10+ · harshithsunku · `Py` · 调用点 [`app.py`](https://github.com/harshithsunku/learn-jev-end-to-end/blob/HEAD/app.py)，2026-09-24 阅读</sub>

- **[litjev](https://github.com/zhengxuyu/litjev)** — 把任意现成 LLM 变成一个 Jev 式的决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · zhengxuyu · `Py` · 引用文件 [`src/litjev/api.py`](https://github.com/zhengxuyu/litjev/blob/HEAD/src/litjev/api.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[midscene-jev-runner](https://github.com/KiritoKing/midscene-jev-runner)** — 社区维护的 Midscene Test JEV 运行器集成。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · ★10+ · kiritoking · `TS` · 调用点 [`src/constants.ts`](https://github.com/KiritoKing/midscene-jev-runner/blob/HEAD/src/constants.ts)，2026-09-22 阅读</sub>

- **[notjev](https://github.com/9pings/notjev)** — 超快的类 Jev 服务器，与模型无关，可对接任何 OpenAI 兼容端点。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · 9pings · `JS` · 引用文件 [`bin/notjev.js`](https://github.com/9pings/notjev/blob/HEAD/bin/notjev.js)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)** — 一个开源语义决策引擎，本地跑零样本模型，其 FastAPI 服务已验证与官方 SDK 协议兼容。
  <sub>`Jev 替代实现` · ★10+ · deepanwadhwa · `Py` · `choice` · `score` · `noul` · 引用文件 [`examples/m3_typesafe_sdk_demo.py`](https://github.com/deepanwadhwa/OpenDecision/blob/HEAD/examples/m3_typesafe_sdk_demo.py)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[OpenJev](https://github.com/GPT-AGI/OpenJev)** — 兼容 Jev 的 System 开源 Jev。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · gpt-agi · `Py` · 引用文件 [`src/openjev/core/primitives.py`](https://github.com/GPT-AGI/OpenJev/blob/HEAD/src/openjev/core/primitives.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[OpenJev](https://github.com/zhangcy122/OpenJev)** — OpenJev：TypeSafe Jev 的开源替代品。由开源模型驱动的带类型概率决策 API（Choice、Noul、Score）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · zhangcy122 · `Py` · 引用文件 [`examples/benchmark_jev_vs_ollama.py`](https://github.com/zhangcy122/OpenJev/blob/HEAD/examples/benchmark_jev_vs_ollama.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[OpenSourceJev](https://github.com/sabeel111/OpenSourceJev)** — 把 LLM 变成类 Jev 系统。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · sabeel111 · `Py` · 引用文件 [`app/main.py`](https://github.com/sabeel111/OpenSourceJev/blob/HEAD/app/main.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[pijev](https://github.com/TypeLLM/pijev)** — 对 Jev 在不同选项顺序下的回答取平均——所有排列在一次请求中完成——并保证 Brier 分数与对数损失不劣于这些排列的平均水平。只需改一行 import。 <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · typellm · `Py` · 调用点 [`pijev/__init__.py`](https://github.com/TypeLLM/pijev/blob/HEAD/pijev/__init__.py)，2026-09-24 阅读</sub>

- **[refgarden](https://github.com/AlbionaHoti/refgarden)** — 面向创作者的空间参考浏览器：本地 Jev 查询选择、元数据高亮与带来源链接的合集。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · albionahoti · `TS` · 引用文件 [`src/jev-connection.ts`](https://github.com/AlbionaHoti/refgarden/blob/HEAD/src/jev-connection.ts)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[ruby_decision_model](https://github.com/obie/ruby_decision_model)** — 面向 Jev 这类决策模型的 Ruby 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · obie · `Rb` · 调用点 [`lib/ruby_decision_model/providers/typesafe.rb`](https://github.com/obie/ruby_decision_model/blob/HEAD/lib/ruby_decision_model/providers/typesafe.rb)，2026-09-22 阅读</sub>

- **[ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)** — 给某个 Ruby LLM 库做的结构化输出 provider。
  <sub>`平台集成` · ★10+ · kieranklaassen · `Rb` · 调用点 [`lib/ruby_llm/providers/typesafe.rb`](https://github.com/kieranklaassen/ruby_llm-typesafe/blob/HEAD/lib/ruby_llm/providers/typesafe.rb)，2026-09-22 阅读</sub>

- **[ruling](https://github.com/bradAGI/ruling)** — 由本地模型给出带类型、经校准的决策，不生成文本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · bradagi · `Py` · 引用文件 [`ruling/against.py`](https://github.com/bradAGI/ruling/blob/HEAD/ruling/against.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身` `宣称未核实`</sub>

- **[snap](https://github.com/emnlmn/snap)** — 从非结构化状态得到类型化决策：一次前向传播、零生成文本。本地、确定性、兼容 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · emnlmn · `Rs` · 引用文件 [`src/api.rs`](https://github.com/emnlmn/snap/blob/HEAD/src/api.rs)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[snapjudge](https://github.com/Micha0827/snapjudge)** — 在 Apple Silicon 上用本地 Qwen 模型给出带类型的决策（choice / score / 是非），概率直接来自模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · micha0827 · `Py` · 引用文件 [`eval/extern/typesafe_public.py`](https://github.com/Micha0827/snapjudge/blob/HEAD/eval/extern/typesafe_public.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[solar-mini4-jev](https://github.com/hunkim/solar-mini4-jev)** — 一个即插即用的封装：让 Upstage 的 Solar 模型以 Jev System One 的 API 形状对外提供服务——noul、choice、score 使用相同的 schema，并提供自带 key 的托管端点。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · hunkim · `Py` · 引用文件 [`jev_ref.py`](https://github.com/hunkim/solar-mini4-jev/blob/HEAD/jev_ref.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[swift-jev](https://github.com/d-date/swift-jev)** — TypeSafe AI Jev 的 Swift 客户端：返回带类型的判断，而不是文本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · d-date · `Swift` · 调用点 [`Sources/Jev/Transport.swift`](https://github.com/d-date/swift-jev/blob/HEAD/Sources/Jev/Transport.swift)，2026-09-24 阅读</sub>

- **[swift-typesafe](https://github.com/ainame/swift-typesafe)** — 非官方 Swift SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · ainame · `Swift` · 调用点 [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/ainame/swift-typesafe/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift)，2026-09-22 阅读</sub>

- **[sys1](https://github.com/alvarobartt/sys1)** — 用 Rust 编写、兼容 System One 的 API，面向 Laya 等开放决策模型。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · alvarobartt · `Rs` · 引用文件 [`src/api.rs`](https://github.com/alvarobartt/sys1/blob/HEAD/src/api.rs)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[system-one](https://github.com/iamaamir/system-one)** — 面向 TypeScript 与 Pi 的、与提供方无关的 System One 运行时。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · iamaamir · `TS` · 调用点 [`pi-system-one/src/tool.ts`](https://github.com/iamaamir/system-one/blob/HEAD/pi-system-one/src/tool.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[tinyjev](https://github.com/ankit-aglawe/tinyjev)** — 一个微型类 Jev 模型：一次前向传播回答 Choice、Score 与 Noul 问题并返回校准概率。支持 MLX 或 PyTorch，完全离线，兼容 System One 接口。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · ankit-aglawe · `Py` · 引用文件 [`tinyjev/cli.py`](https://github.com/ankit-aglawe/tinyjev/blob/HEAD/tinyjev/cli.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[typesafe](https://github.com/krzyzanowskim/TypeSafe)** — Swift 版 TypeSafe SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · krzyzanowskim · `Swift` · 调用点 [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/krzyzanowskim/TypeSafe/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift)，2026-09-22 阅读</sub>

- **[typesafe-ai](https://github.com/Twister915/typesafe-ai)** — Rust 的类型化客户端，含异步与阻塞后端，以及可观测的重试。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · twister915 · `Rs` · 调用点 [`examples/tsg/main.rs`](https://github.com/Twister915/typesafe-ai/blob/HEAD/examples/tsg/main.rs)，2026-09-22 阅读</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/inference-benchmarks)** — 一个模仿其结构化输出形状的网关，用于与之对比测试。
  <sub>`基准测试` · ★10+ · iammrduncan · `TS` · 调用点 [`packages/demos/lib/jev.ts`](https://github.com/iammrduncan/inference-benchmarks/blob/HEAD/packages/demos/lib/jev.ts)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[typesafe-sdk-go](https://github.com/atharvamhaske/typesafe-sdk-go)** — TypeSafe AI 的非官方 Go SDK，与 TypeSafe AI 无关、未获其背书，是为了填补空缺而做的业余项目。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · atharvamhaske · `Go` · 调用点 [`typesafe.go`](https://github.com/atharvamhaske/typesafe-sdk-go/blob/HEAD/typesafe.go)，2026-09-24 阅读</sub>

- **[typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java)** — 社区维护的 Java 客户端（非官方）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · premo-cloud · `Java` · 调用点 [`typesafe-sdk/src/main/java/io/github/premocloud/typesafe/TypeSafeClient.java`](https://github.com/Premo-Cloud/typesafe-sdk-java/blob/HEAD/typesafe-sdk/src/main/java/io/github/premocloud/typesafe/TypeSafeClient.java)，2026-09-22 阅读</sub>

- **[typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk)** — 社区维护的 .NET SDK，支持 noul、choice、score 三种类型化问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ★10+ · saibimajdi · `C#` · 调用点 [`examples/TypeSafe.BureauOfBadIdeas/Program.cs`](https://github.com/saibimajdi/typesafeai-dotnet-sdk/blob/HEAD/examples/TypeSafe.BureauOfBadIdeas/Program.cs)，2026-09-22 阅读</sub>

- **[WaterSheep](https://github.com/SamratDuttaOfficial/WaterSheep)** — 开源的 Jev 替代方案（Apache-2.0）：基于 ModernBERT 微调的模型，在本地通过 POST /v1/systemone 提供服务，回答 noul、choice、score 以及多标签问题，并为每个选项给出概率。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★10+ · SamratDuttaOfficial · `Py` · 引用文件 [`watersheep/cli.py`](https://github.com/SamratDuttaOfficial/WaterSheep/blob/HEAD/watersheep/cli.py)，2026-10-03 阅读 · ⚠ `并非 Jev 本身` `作者自荐`</sub>

- **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)** — 直连 TypeSafe 的 AI SDK provider 包，示例覆盖三种问题类型以及嵌套的 criteria 写法。
  <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[antigravity-mcp-semantic-search-with-typesafeai](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)** — 给 AI 编程助手的快速语义代码搜索与 diff 合理性审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · greenyamao · `Py` · 调用点 [`mcp_server.py`](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi/blob/HEAD/mcp_server.py)，2026-09-22 阅读</sub>

- **[audio-jevlike](https://github.com/alperiox/audio-jevlike)** — Prosodia：原生面向音频、形似 Jev 的决策模型——直接从语音给出校准的类型化决策，无需语音识别。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · alperiox · `Py` · 引用文件 [`space/prosodia/evaluation/baselines.py`](https://github.com/alperiox/audio-jevlike/blob/HEAD/space/prosodia/evaluation/baselines.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)** — 标题误导：它并没有在跑 Jev，而是用开源 LLM 加受约束的 next-token 打分，自己搭一个 Jev-like 决策引擎。
  <sub>`Jev 替代实现` · DataScience Nexus · `Py` · ⚠ `并非 Jev 本身` `代码未实测` `付费墙`</sub>

- **[can-jev-bayes](https://github.com/TomRichner/can-jev-bayes)** — Jev 会贝叶斯吗？把 TypeSafe AI 的 Jev 与贝叶斯最优策略对比，并测试它能否有效使用贝叶斯推理。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · tomrichner · `Py` · 调用点 [`src/jevbandits/client.py`](https://github.com/TomRichner/can-jev-bayes/blob/HEAD/src/jevbandits/client.py)，2026-09-24 阅读</sub>

- **[chat2jev](https://github.com/Chandler-Sun/chat2jev)** — 把传统的 chat completion API 请求转换为 TypeSafe Jev API 请求。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · chandler-sun · `TS` · 调用点 [`src/lib/typesafe.ts`](https://github.com/Chandler-Sun/chat2jev/blob/HEAD/src/lib/typesafe.ts)，2026-09-24 阅读</sub>

- **[cu-Jev](https://github.com/dtunai/cu-Jev)** — cuda-Jev：原生 CUDA 的 Jev System One 决策推理引擎，提供 Jev 兼容 API、示例和可复现的基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · dtunai · `C` · 引用文件 [`python/cujev/systemone.py`](https://github.com/dtunai/cu-Jev/blob/HEAD/python/cujev/systemone.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[decido](https://github.com/yairshy/decido)** — 给 Python 的概率式决策：可用 Jev 也可自带 provider，配合 Playwright 抓取。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · yairshy · `Py` · 调用点 [`src/decido/providers/typesafe.py`](https://github.com/yairshy/decido/blob/HEAD/src/decido/providers/typesafe.py)，2026-09-22 阅读</sub>

- **[decision-bench](https://github.com/Hanno-Labs/decision-bench)** — 面向基于文档的决策模型的开放基准运行框架。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · hanno-labs · `Py` · 调用点 [`src/decision_bench/models/jev_openrouter.py`](https://github.com/Hanno-Labs/decision-bench/blob/HEAD/src/decision_bench/models/jev_openrouter.py)，2026-09-24 阅读</sub>

- **[decision-circuits](https://github.com/Barneyjm/decision-circuits)** — 决策电路：向 System One 模型提出带类型的问题，拿回校准概率，关卡写在代码里。零依赖。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · barneyjm · `Py` · 调用点 [`examples/02_jev_backend.py`](https://github.com/Barneyjm/decision-circuits/blob/HEAD/examples/02_jev_backend.py)，2026-09-24 阅读</sub>

- **[go-system-one](https://github.com/rcarmo/go-system-one)** — 当地鼠遇上 Jev：一个 Go 语言的 System One 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · rcarmo · `Go` · 调用点 [`docs/benchmarks/data/jevbench-public-20260923/protocol/aggregate.py`](https://github.com/rcarmo/go-system-one/blob/HEAD/docs/benchmarks/data/jevbench-public-20260923/protocol/aggregate.py)，2026-09-24 阅读</sub>

- **[hunch-js](https://github.com/steven-shoemaker/hunch-js)** — 把 Jev 判断变成作用于数组的 TypeScript 函数：classify、score、check、where、extract、pick、rank、verify。LLM 提议，Jev 决定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · steven-shoemaker · `TS` · 调用点 [`src/gateway.ts`](https://github.com/steven-shoemaker/hunch-js/blob/HEAD/src/gateway.ts)，2026-09-24 阅读</sub>

- **[jear](https://github.com/iJ03l/jear)** — 由 Jev 路由的 NEAR AI Cloud 推理与智能体客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ij03l · `Rs` · 调用点 [`src/jev_wire.rs`](https://github.com/iJ03l/jear/blob/HEAD/src/jev_wire.rs)，2026-09-22 阅读</sub>

- **[jev](https://github.com/anilsenay/jev)** — TypeSafe System One API 及其模型 Jev 的非官方 Go 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · anilsenay · `Go` · 调用点 [`client.go`](https://github.com/anilsenay/jev/blob/HEAD/client.go)，2026-09-24 阅读</sub>

- **[jev](https://github.com/kataras/jev)** — TypeSafe AI System One API 及其模型 Jev 的 Go 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · kataras · `Go` · 调用点 [`client.go`](https://github.com/kataras/jev/blob/HEAD/client.go)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)** — 第三方解读文章，给了一张有用的架构草图，还罕见地诚实列出了「不该用决策模型」的场景。
  <sub>`文章` · `Py` · ⚠ `代码未实测`</sub>

- **[jev-acento](https://github.com/marcosmartinez/jev-acento)** — Jev 听得懂你的口音吗？一项预先注册的、针对 TypeSafe AI Jev 西班牙语表现的审计——准确率、校准与 token 成本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · marcosmartinez · `Py` · 调用点 [`src/jev_acento/providers.py`](https://github.com/marcosmartinez/jev-acento/blob/HEAD/src/jev_acento/providers.py)，2026-09-24 阅读</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — 在一个智能体失败归因基准上，把 Jev 与一个强 LLM 做对比测试。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · tokentrim · `Py` · 调用点 [`src/jevbench/backends/jev.py`](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/HEAD/src/jevbench/backends/jev.py)，2026-09-22 阅读</sub>

- **[jev-android](https://github.com/dougsong/jev-android)** — 由 Jev 驱动的 Kotlin Android UI 自动化 SDK，带无障碍运行时。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · dougsong · `Kt` · 调用点 [`sdk/src/main/kotlin/io/github/jevandroid/JevProvider.kt`](https://github.com/dougsong/jev-android/blob/HEAD/sdk/src/main/kotlin/io/github/jevandroid/JevProvider.kt)，2026-09-22 阅读</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Jev 的基准与 playground：国际象棋，以及语音转写中的说话对象判定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · wondertwins · `Py` · 调用点 [`jevcommon/client.py`](https://github.com/wondertwins/jev-benchmark/blob/HEAD/jevcommon/client.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-bun1](https://github.com/heiwa4126/jev-bun1)** — 用 TypeScript SDK 上手 Jev 的第一步（日语）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · heiwa4126 · `TS` · 调用点 [`src/ex0.ts`](https://github.com/heiwa4126/jev-bun1/blob/HEAD/src/ex0.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-cookbook](https://github.com/paramjeetn/jev-cookbook)** — TypeSafe AI Jev 的完整食谱：120 多个用例、10 个可运行示例、4 种组合模式。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`教程` · paramjeetn · `Py` · 调用点 [`examples/01-customer-support-triage/triage.py`](https://github.com/paramjeetn/jev-cookbook/blob/HEAD/examples/01-customer-support-triage/triage.py)，2026-09-24 阅读</sub>

- **[jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)** — TypeSafe 的 Jev 在俄语上能保持准确率与校准吗？一项独立的俄英对照审计（ECE、可靠性图）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ahtoooxa · `Py` · 调用点 [`src/jev_cyrillic_audit/run.py`](https://github.com/AHTOOOXA/jev-cyrillic-audit/blob/HEAD/src/jev_cyrillic_audit/run.py)，2026-09-24 阅读</sub>

- **[jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)** — 关于 Jev 概率校准、不确定性表达以及预测概率保真度的实验。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · kantahayashiai · `JS` · 调用点 [`src/run.mjs`](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/HEAD/src/run.mjs)，2026-09-24 阅读</sub>

- **[jev-go](https://github.com/guillemus/jev-go)** — 非官方的 Jev Go SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · guillemus · `Go` · 调用点 [`jev.go`](https://github.com/guillemus/jev-go/blob/HEAD/jev.go)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-go](https://github.com/Gaurav-Gosain/jev-go)** — TypeSafe System One API 及其模型 Jev 的 Go 客户端：返回带类型的判断与校准概率，而不是生成文本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · gaurav-gosain · `Go` · 调用点 [`client.go`](https://github.com/Gaurav-Gosain/jev-go/blob/HEAD/client.go)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-go-sdk](https://github.com/ajayk/jev-go-sdk)** — 无依赖的 Go 客户端，面向 TypeSafe AI 的 System One API 与 Jev 模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · ajayk · `Go` · 调用点 [`client.go`](https://github.com/ajayk/jev-go-sdk/blob/HEAD/client.go)，2026-09-24 阅读</sub>

- **[jev-java](https://github.com/Olti1947/jev-java)** — 地道的 Java SDK，对接 System One 决策引擎。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · olti1947 · `Java` · 调用点 [`src/main/java/io/github/Olti1947/jev/JevClient.java`](https://github.com/Olti1947/jev-java/blob/HEAD/src/main/java/io/github/Olti1947/jev/JevClient.java)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-java](https://github.com/gudcks0305/jev-java)** — TypeSafe Jev 与 Vercel AI Gateway 的非官方 Java SDK，支持 Spring Boot 与 WebClient。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · gudcks0305 · `Java` · 调用点 [`jev-cloudflare/src/main/java/io/github/gudcks0305/jev/cloudflare/CloudflareJevClient.java`](https://github.com/gudcks0305/jev-java/blob/HEAD/jev-cloudflare/src/main/java/io/github/gudcks0305/jev/cloudflare/CloudflareJevClient.java)，2026-09-24 阅读</sub>

- **[jev-jp-address](https://github.com/smasato/jev-jp-address)** — Jev 性能评测项目：以日本邮政地址库为基准，检验它在地址模糊匹配上的可用性。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · smasato · `TS` · 调用点 [`src/jev.ts`](https://github.com/smasato/jev-jp-address/blob/HEAD/src/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — 可复现的早期访问评测：Jev 在韩语理解与医学文本上的表现，附运行时与成本证据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · mahlernim · `Py` · 调用点 [`jevbench/medqa_run.py`](https://github.com/mahlernim/jev-korean-benchmark/blob/HEAD/jevbench/medqa_run.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现） · ⚠ `无许可证`</sub>

- **[jev-lab](https://github.com/danielhirt/jev-lab)** — 通过 OpenRouter 对 TypeSafe Jev（System One 决策模型）做的实验：可重复性、扰动敏感性与 LLM 基线对比。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · danielhirt · `TS` · 调用点 [`packages/codenames/src/judge.ts`](https://github.com/danielhirt/jev-lab/blob/HEAD/packages/codenames/src/judge.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-lab](https://github.com/llt22/jev-lab)** — TypeSafe Jev（System One 模型）的动手研究实验室：对 Noul/Choice/Score 原语的可复现基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · llt22 · `Py` · 调用点 [`experiments/json-render-jev/src/demo.tsx`](https://github.com/llt22/jev-lab/blob/HEAD/experiments/json-render-jev/src/demo.tsx)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-lab](https://github.com/Menny1337/jev-lab)** — 针对 TypeSafe Jev 模型的 TypeScript 实验、评测与延迟基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · menny1337 · `TS` · 调用点 [`src/client.ts`](https://github.com/Menny1337/jev-lab/blob/HEAD/src/client.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — Jev 的能力展示与研究：一次 show-and-tell 式的考察。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · lbotinelly · `TS` · 调用点 [`demo/js/jev-monitor.mjs`](https://github.com/lbotinelly/jev-little-airways/blob/HEAD/demo/js/jev-monitor.mjs)，2026-09-22 阅读</sub>

- **[jev-no-enem](https://github.com/patryckalves/jev-no-enem)** — 在巴西 2025 年 ENEM 标准化考试上评测 TypeSafe AI Jev（System One 范式）的可复现基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · patryckalves · `Py` · 调用点 [`src/evaluate_jev.py`](https://github.com/patryckalves/jev-no-enem/blob/HEAD/src/evaluate_jev.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-php-sdk](https://github.com/mzainzulifqar/jev-php-sdk)** — TypeSafe Jev 的 PHP SDK：发送文本和带类型的问题，得到带校准置信度的类型化答案。支持 PHP 8.1+。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · mzainzulifqar · `PHP` · 调用点 [`src/Jev.php`](https://github.com/mzainzulifqar/jev-php-sdk/blob/HEAD/src/Jev.php)，2026-09-24 阅读</sub>

- **[jev-research](https://github.com/sherajdev/jev-research)** — 把 TypeSafe Jev 与 Herdr 以及 Claude、Codex、Hermes 和浏览器智能体结合使用的实用指南。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`教程` · sherajdev · `TS` · 调用点 [`jev-router.ts`](https://github.com/sherajdev/jev-research/blob/HEAD/jev-router.ts)，2026-09-24 阅读</sub>

- **[jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment)** — 在 RouterArena 上把 Jev 当作低成本 LLM 路由器做基准测试。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · tokentrim · `Py` · 调用点 [`jev_router/jev.py`](https://github.com/TokenTrim/jev-routing-experiment/blob/HEAD/jev_router/jev.py)，2026-09-22 阅读</sub>

- **[jev-rs](https://github.com/abeldzan/jev-rs)** — 以异步为先的 TypeSafe AI API Rust SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · abeldzan · `Rs` · 调用点 [`src/response.rs`](https://github.com/abeldzan/jev-rs/blob/HEAD/src/response.rs)，2026-09-24 阅读</sub>

- **[jev-sdk-java](https://github.com/luigivis/jev-sdk-java)** — 类型安全的 Java 21 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · luigivis · `Java` · 调用点 [`src/main/java/com/luigivismara/jev/JevClient.java`](https://github.com/luigivis/jev-sdk-java/blob/HEAD/src/main/java/com/luigivismara/jev/JevClient.java)，2026-09-22 阅读</sub>

- **[jev-sim](https://github.com/dashbi1/jev-sim)** — 从 LLM logits 读出类型化决策的 Jev 兼容 /v1/systemone 服务，带基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · dashbi1 · `Py` · 调用点 [`jev_sim/cli.py`](https://github.com/dashbi1/jev-sim/blob/HEAD/jev_sim/cli.py)，2026-09-22 阅读</sub>

- **[jev-symfony-bundle](https://github.com/vbcherepanov/jev-symfony-bundle)** — TypeSafe AI Jev 的非官方 Symfony bundle：带类型的客户端、校验约束、Messenger、Workflow 守卫等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · vbcherepanov · `PHP` · 调用点 [`src/Client/JevClientInterface.php`](https://github.com/vbcherepanov/jev-symfony-bundle/blob/HEAD/src/Client/JevClientInterface.php)，2026-09-24 阅读</sub>

- **[jev4mellea](https://github.com/SoundBlaster/Jev4Mellea)** — 给 Mellea 的 Jev 适配器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · soundblaster · `Py` · 调用点 [`src/mellea_jev/providers/typesafe.py`](https://github.com/SoundBlaster/Jev4Mellea/blob/HEAD/src/mellea_jev/providers/typesafe.py)，2026-09-22 阅读</sub>

- **[jevclient](https://github.com/AboveColin/jevclient)** — Jev 的异步 Python 客户端：类型化问题进，概率与选择出，没有散文需要解析。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · abovecolin · `Py` · 调用点 [`jevclient/const.py`](https://github.com/AboveColin/jevclient/blob/HEAD/jevclient/const.py)，2026-09-22 阅读</sub>

- **[jevgo](https://github.com/fgn/jevgo)** — System One API 的 Go 客户端，可选接入 Langfuse 观测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · fgn · `Go` · 调用点 [`client.go`](https://github.com/fgn/jevgo/blob/HEAD/client.go)，2026-09-22 阅读</sub>

- **[jevgo](https://github.com/devbackend/jevgo)** — TypeSafe AI System One API（Jev）的非官方 Go 客户端：输入带类型的问题，输出校准后的答案。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · devbackend · `Go` · 调用点 [`client.go`](https://github.com/devbackend/jevgo/blob/HEAD/client.go)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jevlang](https://github.com/sumanmichael/jevlang)** — 用 Python 编写决策工作流最简单的方式：带“智能 if”的 Python。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · sumanmichael · `Py` · 调用点 [`jevlang/backend.py`](https://github.com/sumanmichael/jevlang/blob/HEAD/jevlang/backend.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jevsbistro](https://github.com/andrewsilber/JevsBistro)** — 用于低延迟决策模型基准测试的 3D 餐厅服务模拟器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · andrewsilber · `TS` · 调用点 [`src/jev/protocol.ts`](https://github.com/andrewsilber/JevsBistro/blob/HEAD/src/jev/protocol.ts)，2026-09-22 阅读</sub>

- **[kojev](https://github.com/ItisNoMatter/kojev)** — Jev 的 Kotlin 多平台客户端：返回你自己的枚举／密封类型，而不是字符串。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · itisnomatter · `Kt` · 调用点 [`src/commonTest/kotlin/io/github/itisnomatter/kojev/JevClientTest.kt`](https://github.com/ItisNoMatter/kojev/blob/HEAD/src/commonTest/kotlin/io/github/itisnomatter/kojev/JevClientTest.kt)，2026-09-22 阅读</sub>

- **[kunobi-jev](https://github.com/kunobi-ninja/kunobi-decision)** — System One API 的 Rust 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · kunobi-ninja · `Rs` · 调用点 [`src/client/mod.rs`](https://github.com/kunobi-ninja/kunobi-decision/blob/HEAD/src/client/mod.rs)，2026-09-22 阅读</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD 基准 alpha 版与官方评测流程。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · johnhughes3 · `Py` · 调用点 [`legalforecast/jev/execution.py`](https://github.com/johnhughes3/LegalForecastBench/blob/HEAD/legalforecast/jev/execution.py)，2026-09-22 阅读</sub>

- **[OpenJev](https://github.com/xingwudao/OpenJev)** — OpenJev：受 Jev 启发、基于 TypeSafe.ai 理念的独立 System One 决策 API，提供 choice、score、noul 原语、本地模拟服务器以及 Python 和 TypeScript SDK。真实推理尚在计划中，与 TypeSafe AI 无关。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · xingwudao · `Py` · 引用文件 [`sdk/python/openjev/__init__.py`](https://github.com/xingwudao/OpenJev/blob/HEAD/sdk/python/openjev/__init__.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[origin-civilization](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)** — AI 生命与文明模拟：每个决策都由 Jev 做出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · jacquesgariepy · `TS` · 调用点 [`legacy/source/providers.js`](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION/blob/HEAD/legacy/source/providers.js)，2026-09-22 阅读</sub>

- **[s1_ruby](https://github.com/innocentdiaz/s1_ruby)** — 把 S1 模型的“测量”（以及随之而来的坍缩）变成 Ruby 的一个基本操作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · innocentdiaz · `Rb` · 调用点 [`lib/s1/providers/typesafe.rb`](https://github.com/innocentdiaz/s1_ruby/blob/HEAD/lib/s1/providers/typesafe.rb)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[sysone-bench](https://github.com/instax-dutta/sysone-bench)** — 首个独立的 System One 决策模型横评（Laya 对比 Jev）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · instax-dutta · `Py` · 调用点 [`runners/jev_runner.py`](https://github.com/instax-dutta/sysone-bench/blob/HEAD/runners/jev_runner.py)，2026-09-22 阅读</sub>

- **[system-one-adapter-rust](https://github.com/codeitlikemiley/system-one-adapter-rust)** — 官方 system-one-adapter 的 Rust 移植（用 LLM 支撑 system_one 评估）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · codeitlikemiley · `Rs` · 调用点 [`src/client.rs`](https://github.com/codeitlikemiley/system-one-adapter-rust/blob/HEAD/src/client.rs)，2026-09-22 阅读</sub>

- **[SystemOneDotNet](https://github.com/JabbaKadabra/SystemOneDotNet)** — TypeSafe System One（Jev）的 .NET 客户端：输入带类型的问题，输出带概率与置信度的类型化答案。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · jabbakadabra · `C#` · 调用点 [`samples/SystemOneDotNet.Sample/Program.cs`](https://github.com/JabbaKadabra/SystemOneDotNet/blob/HEAD/samples/SystemOneDotNet.Sample/Program.cs)，2026-09-24 阅读</sub>

- **[tinyjevclient](https://github.com/tinyhumansai/tinydecisionmodels)** — Rust 版的 Jev 集成。 <sub>(机翻)</sub>
  <sub>`平台集成` · tinyhumansai · `Rs` · 调用点 [`crates/tinyjevclient/src/client/test.rs`](https://github.com/tinyhumansai/tinydecisionmodels/blob/HEAD/crates/tinyjevclient/src/client/test.rs)，2026-09-22 阅读 · ⚠ `已归档`</sub>

- **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)** — 目前唯一有 Jev 专用可观测性的平台：一个 OpenInference instrumentor，通过 OpenTelemetry 追踪每次决策调用。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul`</sub>

- **[typesafe](https://github.com/mattneel/typesafe)** — 地道的 Elixir 版 TypeSafe AI API 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · mattneel · `Ex` · 调用点 [`lib/typesafe/req.ex`](https://github.com/mattneel/typesafe/blob/HEAD/lib/typesafe/req.ex)，2026-09-24 阅读</sub>

- **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)** — Vercel 在 AI Gateway 上线 Jev 的公告，附 experimental_evaluate 示例，模型串为 typesafe-ai/jev。
  <sub>`平台集成` · `TS` · `noul`</sub>

- **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)** — Pydantic AI 的一方支持：用 typesafe:jev-latest 这个模型串、配 output_type=bool 建 Agent。
  <sub>`平台集成` · `Py`</sub>

- **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)** — 通过 LiteLLM 代理 Jev，统一密钥与成本追踪，/typesafe/ 下的任意路径都直接透传。
  <sub>`平台集成` · `sh`</sub>

- **[typesafe-ai-go](https://github.com/kisshan13/typesafe-ai-go)** — 社区维护的 TypeSafe AI System One 评估 API 的 Go SDK，支持带类型的问题、流式构建器与重试。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · kisshan13 · `Go` · 调用点 [`types.go`](https://github.com/kisshan13/typesafe-ai-go/blob/HEAD/types.go)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[typesafe-ai-java](https://github.com/jamilxt/typesafe-ai-java)** — 社区维护的 TypeSafe AI System One（Jev）API 的 Java SDK，并非 TypeSafe 官方产品。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · jamilxt · `Java` · 调用点 [`typesafe-ai-java-core/src/main/java/ai/typesafe/TypeSafeClient.java`](https://github.com/jamilxt/typesafe-ai-java/blob/HEAD/typesafe-ai-java-core/src/main/java/ai/typesafe/TypeSafeClient.java)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-ai-rails](https://github.com/GenieRobot/typesafe-ai-rails)** — TypeSafe AI System One API 的社区版 Rails 集成，基于社区 typesafe-sdk gem：提供 Rails 配置、持久化的用量与成本记录，以及针对 Choice 和 Score 答案的可选置信度策略。 <sub>(机翻)</sub>
  <sub>`SDK` · genierobot · `Rb` · 调用点 [`lib/typesafe/rails/client.rb`](https://github.com/GenieRobot/typesafe-ai-rails/blob/HEAD/lib/typesafe/rails/client.rb)，2026-09-24 阅读</sub>

- **[typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs)** — 独立的 Rust SDK，同时提供异步与阻塞两种形式。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · gilljon · `Rs` · 调用点 [`src/lib.rs`](https://github.com/gilljon/typesafe-ai-rs/blob/HEAD/src/lib.rs)，2026-09-22 阅读</sub>

- **[typesafe-ai-ruby](https://github.com/hnegishi/typesafe-ai-ruby)** — System One API 的 Ruby 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · hnegishi · `Rb` · 调用点 [`lib/typesafe/constants.rb`](https://github.com/hnegishi/typesafe-ai-ruby/blob/HEAD/lib/typesafe/constants.rb)，2026-09-22 阅读</sub>

- **[typesafe-client](https://github.com/JedimEmO/typesafe-client)** — 非官方的类型化异步 Rust 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · jedimemo · `Rs` · 调用点 [`crates/typesafe-client/src/client/mod.rs`](https://github.com/JedimEmO/typesafe-client/blob/HEAD/crates/typesafe-client/src/client/mod.rs)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)** — 只改一个 baseURL 就能把官方 TypeSafe SDK 指向 Vercel，也可以直接用 cURL 调网关的 systemone 端点。
  <sub>`平台集成` · `TS` · `sh` · `noul`</sub>

- **[typesafe-go](https://github.com/zhirschtritt/typesafe-go)** — 地道的 Go SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · zhirschtritt · `Go` · 调用点 [`client.go`](https://github.com/zhirschtritt/typesafe-go/blob/HEAD/client.go)，2026-09-22 阅读</sub>

- **[typesafe-go](https://github.com/cole-gillespie/typesafe-go)** — TypeSafe AI 的非官方 Go SDK，支持带类型的答案、重试和 context。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · cole-gillespie · `Go` · 调用点 [`client.go`](https://github.com/cole-gillespie/typesafe-go/blob/HEAD/client.go)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[typesafe-go](https://github.com/Nibir1/typesafe-go)** — 零依赖的社区 Go SDK，还带一个静态分析器，能在编译期指出设计不良的问题。
  <sub>`SDK` · Nibir1 · `Go` · `choice` · `score` · `noul` · 调用点 [`cmd/typesafe/main.go`](https://github.com/Nibir1/typesafe-go/blob/HEAD/cmd/typesafe/main.go)，2026-09-22 阅读 · ⚠ `代码未实测`</sub>

- **[typesafe-go](https://github.com/Shubham510/typesafe-go)** — TypeSafe AI System One API（Jev）的非官方 Go SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · shubham510 · `Go` · 调用点 [`client.go`](https://github.com/Shubham510/typesafe-go/blob/HEAD/client.go)，2026-09-24 阅读</sub>

- **[typesafe-rs](https://github.com/AbdelStark/typesafe-rs)** — 以延迟为先的 System One Rust SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · abdelstark · `Rs` · 调用点 [`crates/typesafe-rs-mock/src/lib.rs`](https://github.com/AbdelStark/typesafe-rs/blob/HEAD/crates/typesafe-rs-mock/src/lib.rs)，2026-09-22 阅读</sub>

- **[typesafe-sdk](https://github.com/joshmn/typesafe-sdk)** — typesafe.ai 的 Ruby 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · joshmn · `Rb` · 调用点 [`lib/typesafe/sdk.rb`](https://github.com/joshmn/typesafe-sdk/blob/HEAD/lib/typesafe/sdk.rb)，2026-09-22 阅读</sub>

- **[typesafe-sdk](https://github.com/binnash/typesafe-sdk)** — 面向 TypeSafe AI JEV 模型系列的 PHP 与 Laravel SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · binnash · `PHP` · 调用点 [`config/typesafe.php`](https://github.com/binnash/typesafe-sdk/blob/HEAD/config/typesafe.php)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-sdk](https://github.com/typesafe-sdk-csharp/typesafe-sdk)** — TypeSafe AI 的非官方 .NET SDK，发布在 NuGet 上，提供确定性的问题构建与高吞吐的验证。 <sub>(机翻)</sub>
  <sub>`SDK` · typesafe-sdk-csharp · `C#` · 调用点 [`src/TypeSafe.AI/TypeSafeClientOptions.cs`](https://github.com/typesafe-sdk-csharp/typesafe-sdk/blob/HEAD/src/TypeSafe.AI/TypeSafeClientOptions.cs)，2026-09-24 阅读</sub>

- **[typesafe-sdk-dotnet](https://github.com/hardkoded/typesafe-sdk-dotnet)** — TypeSafe AI 客户端 SDK 的非官方 .NET 移植（带类型的问题与答案）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · hardkoded · `C#` · 调用点 [`src/TypeSafe.AI.Sdk/TypeSafeClient.cs`](https://github.com/hardkoded/typesafe-sdk-dotnet/blob/HEAD/src/TypeSafe.AI.Sdk/TypeSafeClient.cs)，2026-09-24 阅读</sub>

- **[typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go)** — Go SDK —— 类型化问题进，概率分布出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · tangerg · `Go` · 调用点 [`client.go`](https://github.com/Tangerg/typesafe-sdk-go/blob/HEAD/client.go)，2026-09-22 阅读</sub>

- **[typesafe-sdk-go](https://github.com/dwisiswant0/typesafe-sdk-go)** — TypeSafe AI 的 Go SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · dwisiswant0 · `Go` · 调用点 [`client.go`](https://github.com/dwisiswant0/typesafe-sdk-go/blob/HEAD/client.go)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[typesafe-sdk-go](https://github.com/SergeAx/typesafe-sdk-go)** — TypeSafe.AI 的 Go SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · sergeax · `Go` · 调用点 [`config.go`](https://github.com/SergeAx/typesafe-sdk-go/blob/HEAD/config.go)，2026-09-24 阅读</sub>

- **[typesafe-sdk-go](https://github.com/valksor/typesafe-sdk-go)** — TypeSafe AI System One API 的非官方 Go SDK，与官方 JS 和 Python SDK 一一对应，与 TypeSafe AI 无关。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · valksor · `Go` · 调用点 [`client.go`](https://github.com/valksor/typesafe-sdk-go/blob/HEAD/client.go)，2026-09-24 阅读</sub>

- **[typesafe-sdk-kotlin](https://github.com/ufec/typesafe-sdk-kotlin)** — TypeSafe AI 的 Kotlin SDK，移植自官方 JavaScript SDK，并记录了与原版的差异；针对一段文本提出带类型的问题，得到带类型的答案。 <sub>(机翻)</sub>
  <sub>`SDK` · ufec · `Kt` · 调用点 [`src/commonMain/kotlin/me/ethanxu/typesafe/sdk/TypeSafeClient.kt`](https://github.com/ufec/typesafe-sdk-kotlin/blob/HEAD/src/commonMain/kotlin/me/ethanxu/typesafe/sdk/TypeSafeClient.kt)，2026-09-24 阅读</sub>

- **[typesafe-sdk-php](https://github.com/Fox-Islam/typesafe-sdk-php)** — TypeSafe API 的非官方 PHP 库。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · fox-islam · `PHP` · 调用点 [`src/TypeSafe.php`](https://github.com/Fox-Islam/typesafe-sdk-php/blob/HEAD/src/TypeSafe.php)，2026-09-24 阅读</sub>

- **[typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php)** — TypeSafe AI System One API 的非官方 PHP SDK，与官方 JS 和 Python SDK 一一对应，与 TypeSafe AI 无关。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · valksor · `PHP` · 调用点 [`src/Client.php`](https://github.com/valksor/typesafe-sdk-php/blob/HEAD/src/Client.php)，2026-09-24 阅读</sub>

- **[typesafe-sdk-ruby](https://github.com/afurm/typesafe-sdk-ruby)** — TypeSafe AI API（Jev 模型）的非官方 Ruby SDK：带类型的问题、重试与类型化错误。社区移植版。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · afurm · `Rb` · 调用点 [`lib/typesafe/sdk/client.rb`](https://github.com/afurm/typesafe-sdk-ruby/blob/HEAD/lib/typesafe/sdk/client.rb)，2026-09-24 阅读</sub>

- **[typesafe-sdk-rust](https://github.com/codeitlikemiley/typesafe-sdk-rust)** — TypeSafe AI API 的 Rust SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · codeitlikemiley · `Rs` · 调用点 [`src/client.rs`](https://github.com/codeitlikemiley/typesafe-sdk-rust/blob/HEAD/src/client.rs)，2026-09-22 阅读</sub>

- **[typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift)** — 非官方的 Swift 客户端库。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · alterhq · `Swift` · 调用点 [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/alterhq/typesafe-sdk-swift/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[typesafe-sdk-swift](https://github.com/InsaneArts/typesafe-sdk-swift)** — TypeSafe AI 的 Swift SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · insanearts · `Swift` · 调用点 [`Sources/TypeSafe/Client.swift`](https://github.com/InsaneArts/typesafe-sdk-swift/blob/HEAD/Sources/TypeSafe/Client.swift)，2026-09-24 阅读</sub>

- **[typesafe-sdk-swift](https://github.com/marandaneto/typesafe-sdk-swift)** — typesafe-sdk-js 与 typesafe-sdk-python 的 Swift 移植版。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · marandaneto · `Swift` · 调用点 [`Sources/TypeSafe/TypeSafeClient.swift`](https://github.com/marandaneto/typesafe-sdk-swift/blob/HEAD/Sources/TypeSafe/TypeSafeClient.swift)，2026-09-24 阅读</sub>

- **[typesafe_ai](https://github.com/hfiguera/typesafe_ai)** — TypeSafe AI 的 Elixir 客户端，提供带类型的响应和有界并发。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · hfiguera · `Ex` · 调用点 [`bench/recorded/tail-investigation/versions/async-timers/lib/typesafe/client.ex`](https://github.com/hfiguera/typesafe_ai/blob/HEAD/bench/recorded/tail-investigation/versions/async-timers/lib/typesafe/client.ex)，2026-09-24 阅读</sub>

- **[typesafe_ai](https://github.com/typesend/typesafe_ai)** — 面向 TypeSafe AI 及其 Jev System One 模型的带类型 Elixir 客户端，提供离线测试桩、并发扇出与原子化结果。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · typesend · `Ex` · 调用点 [`lib/typesafe_api/client.ex`](https://github.com/typesend/typesafe_ai/blob/HEAD/lib/typesafe_api/client.ex)，2026-09-24 阅读</sub>

- **[typesafe_sdk (Elixir)](https://github.com/nshkrdotcom/typesafe_sdk)** — 官方 SDK 的 Elixir 移植。
  <sub>`SDK` · nshkrdotcom · `Ex` · 调用点 [`codegen/typesafe_sdk/codegen/source/openapi.ex`](https://github.com/nshkrdotcom/typesafe_sdk/blob/HEAD/codegen/typesafe_sdk/codegen/source/openapi.ex)，2026-09-22 阅读</sub>

- **[typesafe_sdk_ex](https://github.com/vinnie357/typesafe_sdk_ex)** — 基于 Req 的 Elixir 版 TypeSafe AI SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · vinnie357 · `Ex` · 调用点 [`lib/type_safe.ex`](https://github.com/vinnie357/typesafe_sdk_ex/blob/HEAD/lib/type_safe.ex)，2026-09-22 阅读</sub>

- **[typesafeai-go](https://github.com/chez-shanpu/typesafeai-go)** — TypeSafe AI API 的 Go SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · chez-shanpu · `Go` · 调用点 [`systemone.go`](https://github.com/chez-shanpu/typesafeai-go/blob/HEAD/systemone.go)，2026-09-22 阅读</sub>

- **[typesafeai.net](https://github.com/Hawxy/TypeSafeAI.Net)** — 面向 TypeSafe AI 平台的 .NET SDK。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · hawxy · `C#` · 调用点 [`src/TypeSafeAI.Extensions.AI/Evaluation/TypeSafeEvaluator.cs`](https://github.com/Hawxy/TypeSafeAI.Net/blob/HEAD/src/TypeSafeAI.Extensions.AI/Evaluation/TypeSafeEvaluator.cs)，2026-09-22 阅读</sub>

- **[werr](https://github.com/pCwOrM/werr)** — 零记忆的 System-1 决策引擎，与 TypeSafe Jev 协议兼容的运行时，由“曼德博波动力学”驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · pcworm · `Py` · 引用文件 [`werr/server.py`](https://github.com/pCwOrM/werr/blob/HEAD/werr/server.py)，2026-09-24 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[what-is-jev](https://github.com/g0runmezadam/what-is-jev)** — 关于 TypeSafe AI Jev（System One）的独立、有来源的研究，包含对 947 个公开仓库的评分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · g0runmezadam · `Py`</sub>

- **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)** — 目前这个领域里 star 数最高的同类目录。
  <sub>`开源项目` · ★1k+ · ⚠ `无许可证`</sub>

- **[awesome-jev (heyjunpenn)](https://github.com/heyjunpenn/awesome-jev)** — 覆盖最广的同类目录：数百个项目、六种语言，且它的 README 本身就是被解析的数据源。
  <sub>`开源项目` · ★100+ · heyjunpenn</sub>

- **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)** — 一个同类目录，主打生态广度：来源锚定到具体 commit、四语 README、以及一个生成式站点。
  <sub>`开源项目` · ★100+ · logicrw</sub>

- **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)** — 唯一一篇引用了开发者一手说法（而非厂商数字）的发布报道，其中还提醒：解释阈值的责任现在落在你自己头上。
  <sub>`文章` · Tim Fernholz</sub>

- **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)** — 重点落在可解释性的缺失 —— 模型不给出语言层面的理由 —— 以及所有已公布基准都出自厂商自己。
  <sub>`文章` · Tomislav Bezmalinović</sub>

- **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)** — 发布讨论帖，也是质疑最集中的地方：RLCD 缺乏支撑材料、延迟对比不对等、以及官方刻意不公开基准。
  <sub>`讨论`</sub>

- **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))** — 最大价值在于当索引用：它的参考文献列表是找到值得读的报道的最快路径。
  <sub>`文章`</sub>

- **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)** — 从智能体开发者角度，讲决策模型在智能体技术栈里的位置。
  <sub>`文章` · ⚠ `营销内容`</sub>

- **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)** — 主流媒体对这次发布、以及各家网关上线速度的报道。
  <sub>`文章` · Josipa Majic Predin · ⚠ `厂商自报数据` `付费墙`</sub>

- **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)** — 一篇把限制直接写进标题、而不是藏在正文里的评测。
  <sub>`视频` · Gary Explains</sub>

- **[Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216)** — 首个基于数据的 Jev 应用生态综述与分析，研究 2,170 个公开 GitHub 项目，记录早期快速增长、应用领域和决策用途分布。 <sub>(机翻)</sub>
  <sub>`文章` · Guoming Ling, Muen Xue, and Zijian Ye</sub>

- **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)** — 唯一的长篇创始人访谈：为什么 RLHF 是错的优化目标、为什么不公开基准、以及全合成数据的路线。
  <sub>`讨论` · Latent Space</sub>

- **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)** — 对架构、宣称的基准和定价的中立综述，并明确指出当时还没有出现大规模的独立复现。
  <sub>`文章` · Matt Crabtree</sub>

- **[jevai.org community app gallery](https://www.jevai.org/apps)** — 从社交帖子里策展的 36 个社区作品：浏览器智能体、表格工具、按意图搜邮箱、会判断的广告拦截、游戏与机器人。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

- **[jevai.org community site](https://www.jevai.org/)** — 一个与官方无关的社区站：有 playground、预设决策 API、MCP 服务、可下载技能，以及一个社区应用展示廊。
  <sub>`开源项目` · ⚠ `需第三方密钥` `宣称未核实`</sub>

- **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)** — 一份独立整理，其最有价值的结论是否定性的：RLCD 没有论文、没有奖励函数、没有数据集说明、也没有可复现的评测。
  <sub>`文章`</sub>

- **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)** — 最具怀疑视角的主流报道：它质疑「不会幻觉」的说法 —— 格式正确的答案不等于正确的答案。
  <sub>`文章` · Thomas Claburn</sub>

- **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)** — OpenRouter 上的 Jev 条目，有自己的模型 id，以及「输入收费、输出免费」这种少见的定价结构。
  <sub>`平台集成`</sub>

<a name="unindexed"></a>

## 尚未按模式索引

带代码的项目或插件，共 252 行：唯一的模式是 `overview`，且没有记录 `patterns_reviewed`。`overview` 也是关键词规则无法归类时给出的默认值，所以这些行可能从未被归类。有人为某行指定模式，或对照[决策模式](../patterns.zh-CN.md#overview)读过它并把日期记入 `patterns_reviewed` 后，该行就会离开此列表。[复核队列](../review-queue.md#unsorted-overview)列出了它们以及规则给出的建议。 <sub>(机翻)</sub>

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐ — Claude Code 插件背后的官方技能仓库，里面的 SKILL.md 教会智能体如何使用 System One API。
  <sub>`插件` · ★1k+ · `sh`</sub>

- **[langchain](https://github.com/langchain-ai/langchain)** — 智能体工程平台。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100k+ · langchain-ai · `Py` · 调用点 [`libs/partners/typesafe/langchain_typesafe/classifier.py`](https://github.com/langchain-ai/langchain/blob/HEAD/libs/partners/typesafe/langchain_typesafe/classifier.py)，2026-09-22 阅读</sub>

- **[eliza](https://github.com/elizaOS/eliza)** — 开源的智能体操作系统。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10k+ · elizaos · `TS` · 调用点 [`packages/agent/src/services/typesafe/client.ts`](https://github.com/elizaOS/eliza/blob/HEAD/packages/agent/src/services/typesafe/client.ts)，2026-09-22 阅读</sub>

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)** — 深度整合 IDE 的编程智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10k+ · can1357 · `TS` · 调用点 [`packages/ai/src/judgment/typesafe.ts`](https://github.com/can1357/oh-my-pi/blob/HEAD/packages/ai/src/judgment/typesafe.ts)，2026-09-22 阅读</sub>

- **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)** — 包装同步与异步客户端，把每次 system_one 调用记录成一个可追踪的 span。
  <sub>`开源项目` · ★10k+ · `Py` · 调用点 [`sdks/python/src/opik/integrations/typesafe/opik_tracker.py`](https://github.com/comet-ml/opik/blob/HEAD/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)</sub>

- **[pydantic-ai](https://github.com/pydantic/pydantic-ai)** — Python 做 AI 的方式：智能体、实时语音、图像生成、嵌入。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10k+ · pydantic · `Py` · 调用点 [`pydantic_ai_slim/pydantic_ai/models/typesafe.py`](https://github.com/pydantic/pydantic-ai/blob/HEAD/pydantic_ai_slim/pydantic_ai/models/typesafe.py)，2026-09-22 阅读</sub>

- **[ax](https://github.com/ax-llm/ax)** — TypeScript 版的 DSPy 框架。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · ax-llm · `TS` · 调用点 [`src/ax/ai/typesafe/client.ts`](https://github.com/ax-llm/ax/blob/HEAD/src/ax/ai/typesafe/client.ts)，2026-09-22 阅读</sub>

- **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)** — 一个 Go 网关 provider，对原生 API 做一比一透传 —— 官方 SDK 只需改 base URL 即可使用。
  <sub>`开源项目` · ★1k+ · `Go` · 调用点 [`core/providers/typesafe/typesafe.go`](https://github.com/maximhq/bifrost/blob/HEAD/core/providers/typesafe/typesafe.go)</sub>

- **[celesto](https://github.com/CelestoAI/celesto)** — 给 AI 智能体的安全持久化计算环境。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · celestoai · `Py` · 调用点 [`examples/pr-review-jev/models.py`](https://github.com/CelestoAI/celesto/blob/HEAD/examples/pr-review-jev/models.py)，2026-09-22 阅读</sub>

- **[laya-mlx](https://github.com/mizorewww/laya-mlx)** — 给 Laya 类型化决策模型的原生 MLX 运行时：短决策 7–14 毫秒，不生成文本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · mizorewww · `Py` · 调用点 [`laya_mlx/agent.py`](https://github.com/mizorewww/laya-mlx/blob/HEAD/laya_mlx/agent.py)，2026-09-22 阅读</sub>

- **[memsearch](https://github.com/zilliztech/memsearch)** — 面向多个 AI 编程智能体的持久化统一记忆层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★1k+ · zilliztech · `Py` · 调用点 [`src/memsearch/jev_reranker.py`](https://github.com/zilliztech/memsearch/blob/HEAD/src/memsearch/jev_reranker.py)，2026-09-22 阅读</sub>

- **[vellum-assistant](https://github.com/vellum-ai/vellum-assistant)** — 易于配置的 AI 助手：全天候工作、了解你的偏好。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · vellum-ai · `TS` · 调用点 [`assistant/src/providers/jev/client.ts`](https://github.com/vellum-ai/vellum-assistant/blob/HEAD/assistant/src/providers/jev/client.ts)，2026-09-22 阅读</sub>

- **[agent-router](https://github.com/nidhi-singh02/agent-router)** — CLI：为一个任务挑选编程智能体与模型／推理强度，然后启动它。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · nidhi-singh02 · `TS` · 调用点 [`packages/router/src/semantic/typesafe-client.ts`](https://github.com/nidhi-singh02/agent-router/blob/HEAD/packages/router/src/semantic/typesafe-client.ts)，2026-09-22 阅读</sub>

- **[aiavatarkit](https://github.com/uezo/aiavatarkit)** — 快速构建基于 AI 的对话式虚拟形象。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · uezo · `Py` · 调用点 [`aiavatar/sts/vad/turn_end_gates/jev.py`](https://github.com/uezo/aiavatarkit/blob/HEAD/aiavatar/sts/vad/turn_end_gates/jev.py)，2026-09-22 阅读</sub>

- **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)** — 一个同类目录，提交由 Jev 自己审核，其多语言社区客户端清单相当完整。
  <sub>`开源项目` · ★100+ · fatwang2 · `JS` · 调用点 [`.github/workflows/jev-review.yml`](https://github.com/fatwang2/awesome-jev/blob/HEAD/.github/workflows/jev-review.yml)</sub>

- **[crush-monitor](https://github.com/FerryCorleone/crush-monitor)** — 用 Jev 分析微信聊天的情绪、意图与回复表现，本机部署、自带密钥。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · ferrycorleone · `TS` · 调用点 [`server/provider-config.ts`](https://github.com/FerryCorleone/crush-monitor/blob/HEAD/server/provider-config.ts)，2026-09-24 阅读</sub>

- **[dasheng](https://github.com/wquguru/dasheng)** — 英文朗读评分：流式 ASR 听，Jev 逐词判定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · wquguru · `JS` · 调用点 [`lib/jev.js`](https://github.com/wquguru/dasheng/blob/HEAD/lib/jev.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[distill](https://github.com/samuelfaj/distill)** — 用远更少的 token 完成远更多的事。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · samuelfaj · `Rs` · 调用点 [`crates/codegen/distill-workspace/src/jev/client.rs`](https://github.com/samuelfaj/distill/blob/HEAD/crates/codegen/distill-workspace/src/jev/client.rs)，2026-09-22 阅读</sub>

- **[djev-spark](https://github.com/mmastrac/djev-spark)** — 在 DGX Spark 上跑 DiffusionGemma NVFP4 结构化决策的容器配方。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · mmastrac · `TS` · 调用点 [`scripts/long-context-probe.py`](https://github.com/mmastrac/djev-spark/blob/HEAD/scripts/long-context-probe.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[Jev](https://github.com/cobusgreyling/Jev)** — 非官方的 TypeSafe Jev 展示：System One 决策，而不是聊天。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · cobusgreyling · `Py` · 调用点 [`jev_lab/client.py`](https://github.com/cobusgreyling/Jev/blob/HEAD/jev_lab/client.py)，2026-09-24 阅读</sub>

- **[jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac)** — 微信消息意图识别悬浮窗（macOS）：看屏加本地小模型判断意图与风险，再生成回复候选。纯只读。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · jev-chat · `Py` · 调用点 [`src/judge_jev.py`](https://github.com/jev-chat/jev-chat-jarvis-mac/blob/HEAD/src/judge_jev.py)，2026-09-22 阅读</sub>

- **[jev-chat-windows](https://github.com/jev-chat/jev-chat-windows)** — 微信（Windows）旁挂回复辅助：截图加本地 OCR 读消息，Jev 判断意图，生成候选，发送永远手动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · jev-chat · `Py` · 调用点 [`core/jev_client.py`](https://github.com/jev-chat/jev-chat-windows/blob/HEAD/core/jev_client.py)，2026-09-22 阅读</sub>

- **[jev-docs-zh](https://github.com/datawhalechina/jev-cookbook)** — Jev 官方使用文档的非官方中文翻译。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · bald0wang · `Py` · 调用点 [`dist/assets/search-index.js`](https://github.com/datawhalechina/jev-cookbook/blob/HEAD/dist/assets/search-index.js)，2026-09-22 阅读</sub>

- **[jev-experiments](https://github.com/dabit3/jev-experiments)** — Nader Dabit 的一组 Jev 小实验，每个目录一个：提交审查、shell 防护、发送防护、日志哨兵、即时搜索、重排、语音轮次检测等。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · dabit3 · `TS` · 调用点 [`commit-sentry/src/jev.ts`](https://github.com/dabit3/jev-experiments/blob/HEAD/commit-sentry/src/jev.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-foundation-models](https://github.com/peterfriese/system-one-foundation-models)** — 轻量的原生 Swift 6 桥接，把 Jev 接入 Apple 的 Foundation Models。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · peterfriese · `Swift` · 调用点 [`Sources/JevFoundationModels/JevLanguageModel.swift`](https://github.com/peterfriese/system-one-foundation-models/blob/HEAD/Sources/JevFoundationModels/JevLanguageModel.swift)，2026-09-22 阅读</sub>

- **[jev-skill](https://github.com/wuyoscar/jev-skill)** — 一个 agent 技能加 CLI：校验三种原语、在产生计费调用前要求明确同意、并禁止在模拟时编造输出。
  <sub>`插件` · ★100+ · `Py` · `choice` · `score` · `noul` · 调用点 [`skills/jev/scripts/jev.py`](https://github.com/wuyoscar/jev-skill/blob/HEAD/skills/jev/scripts/jev.py)，2026-09-22 阅读</sub>

- **[jev-voice](https://github.com/kevinbadi/jev-voice)** — 对你的 Mac 说话：本地 whisper.cpp + 每条命令一次 Jev 调用 + macOS 自动化。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · kevinbadi · `Py` · 调用点 [`jev_voice/config.py`](https://github.com/kevinbadi/jev-voice/blob/HEAD/jev_voice/config.py)，2026-09-22 阅读</sub>

- **[jevmem](https://github.com/Avinash-jetwani/jevmem)** — 为 Claude Code 提供自动的项目记忆，同样适用于 Cursor 和 Codex。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · avinash-jetwani · `TS` · 调用点 [`src/jev.ts`](https://github.com/Avinash-jetwani/jevmem/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[Jevmind](https://github.com/dealerdefi/Jevmind)** — 把智能体的决策从它的文字中抽离出来集中管理：带置信度的类型化答案，经过用代码写的关卡，封存进账本，被评分并用于学习。默认在本地规则大脑上离线运行，一个开关即可换成 Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · dealerdefi · `Py` · 调用点 [`src/jevmind/brain.py`](https://github.com/dealerdefi/Jevmind/blob/HEAD/src/jevmind/brain.py)，2026-09-24 阅读</sub>

- **[kody](https://github.com/kentcdodds/kody)** — 你的助手之家：AI 智能体所需的记忆、密钥、代码与自动化。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · kentcdodds · `TS` · 调用点 [`packages/worker/src/mcp/tools/search-jev-rerank.ts`](https://github.com/kentcdodds/kody/blob/HEAD/packages/worker/src/mcp/tools/search-jev-rerank.ts)，2026-09-22 阅读</sub>

- **[laya](https://github.com/receptron/laya)** — 通过 ONNX Runtime 从 Node.js／TypeScript 运行开源的 Jev 兼容 System-1 决策模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · receptron · `TS` · 调用点 [`src/laya.ts`](https://github.com/receptron/laya/blob/HEAD/src/laya.ts)，2026-09-22 阅读</sub>

- **[laya-ultrafast](https://github.com/ipenywis/laya-ultrafast)** — 与 jev-ultrafast 相同，但换成 Laya。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · ipenywis · `Py` · 调用点 [`laya_ultrafast/model.py`](https://github.com/ipenywis/laya-ultrafast/blob/HEAD/laya_ultrafast/model.py)，2026-09-22 阅读</sub>

- **[laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev)** — Laya 对比 Jev：本地 MLX 与托管 API 并排玩恐龙跑酷，带实时指标。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · virajbhartiya · `Py` · 调用点 [`laya_mlx/agent.py`](https://github.com/virajbhartiya/laya-vs-jev/blob/HEAD/laya_mlx/agent.py)，2026-09-22 阅读</sub>

- **[openwhisper](https://github.com/Knuckles92/OpenWhisper)** — 基于 Whisper 的本地语音转写、听写与会议记录。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · knuckles92 · `Py` · 调用点 [`benchmarks/typesafe_experiments.py`](https://github.com/Knuckles92/OpenWhisper/blob/HEAD/benchmarks/typesafe_experiments.py)，2026-09-22 阅读</sub>

- **[orchestkit](https://github.com/yonatangross/orchestkit)** — 面向 Claude Code 的完整 AI 开发工具包：106 个技能、36 个智能体、171 个钩子。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · yonatangross · `TS` · 调用点 [`docs/audits/jev-session-category-heldout-2026-09-17/run_jev_b.mjs`](https://github.com/yonatangross/orchestkit/blob/HEAD/docs/audits/jev-session-category-heldout-2026-09-17/run_jev_b.mjs)，2026-09-22 阅读</sub>

- **[pi-fabric](https://github.com/fabric-runtime/pi-fabric)** — 给 Pi 的可编程工具与智能体运行时。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · monotykamary · `TS` · 调用点 [`src/jev/routes.ts`](https://github.com/fabric-runtime/pi-fabric/blob/HEAD/src/jev/routes.ts)，2026-09-22 阅读</sub>

- **[req_llm](https://github.com/agentjido/req_llm)** — 基于 Req 和 Finch 的可组合 Elixir LLM 交互库。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · agentjido · `Ex` · 调用点 [`lib/req_llm/providers/typesafe.ex`](https://github.com/agentjido/req_llm/blob/HEAD/lib/req_llm/providers/typesafe.ex)，2026-09-22 阅读</sub>

- **[runline](https://github.com/Michaelliv/runline)** — 给智能体的代码模式。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · michaelliv · `TS` · 调用点 [`packages/runline-plugins/typesafe/src/shared.ts`](https://github.com/Michaelliv/runline/blob/HEAD/packages/runline-plugins/typesafe/src/shared.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[smithers](https://github.com/smithersai/smithers)** — Smithers：用简单 TypeScript 配置定义工作流的智能体工作流框架。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · smithersai · `TS` · 调用点 [`apps/server/src/jev.ts`](https://github.com/smithersai/smithers/blob/HEAD/apps/server/src/jev.ts)，2026-09-22 阅读</sub>

- **[stanley-code](https://github.com/devagrawal09/stanley-code)** — 给编程智能体的有界 Jev 工作流。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · devagrawal09 · `TS` · 调用点 [`src/adapters/jev.ts`](https://github.com/devagrawal09/stanley-code/blob/HEAD/src/adapters/jev.ts)，2026-09-22 阅读</sub>

- **[third-hand](https://github.com/shhivv/third-hand)** — 由决策模型驱动的 computer-use 助手。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · shhivv · `Swift` · 调用点 [`Sources/ThirdHand/JevClient.swift`](https://github.com/shhivv/third-hand/blob/HEAD/Sources/ThirdHand/JevClient.swift)，2026-09-22 阅读</sub>

- **[typesafe-mcp](https://github.com/itsmostafa/system-one-connector)** — 最适合刚拿到 API 的人。把 Jev 接进 Claude Code、Claude Desktop、Codex 和 Pi，随时做 Choice / Score / Noul。
  <sub>`插件` · ★100+ · `Go` · `choice` · `score` · `noul` · 调用点 [`cmd/evaluate/main.go`](https://github.com/itsmostafa/system-one-connector/blob/HEAD/cmd/evaluate/main.go)，2026-09-22 阅读</sub>

- **[webctl](https://github.com/dorkitude/webctl)** — 给智能体用的智能网页搜索 CLI，由 Jev 支撑，大幅省 token。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · dorkitude · `Go` · 调用点 [`internal/jev/client.go`](https://github.com/dorkitude/webctl/blob/HEAD/internal/jev/client.go)，2026-09-22 阅读</sub>

- **[ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill)** — 给 Hermes 及其他智能体用的技能，用来向 Jev 提问。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · shantanugoel · `Py` · 调用点 [`scripts/askjev.py`](https://github.com/shantanugoel/ask-jev-skill/blob/HEAD/scripts/askjev.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[awesome-jev](https://github.com/daftAI2026/awesome-jev)** — System One / Jev 社区目录：围绕类型化决策的 GitHub 项目与文章。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · daftai2026 · `TS` · 调用点 [`scripts/jev-client.ts`](https://github.com/daftAI2026/awesome-jev/blob/HEAD/scripts/jev-client.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[call-coach-ai](https://github.com/ZeroGold/call-coach-ai)** — 由 Jev 驱动的通话教练。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · zerogold · `TS` · 调用点 [`server.mjs`](https://github.com/ZeroGold/call-coach-ai/blob/HEAD/server.mjs)，2026-09-22 阅读</sub>

- **[captaincore](https://github.com/CaptainCore/captaincore)** — 自动化 WordPress 运维的命令行应用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · captaincore · `Go` · 调用点 [`typesafe/client.go`](https://github.com/CaptainCore/captaincore/blob/HEAD/typesafe/client.go)，2026-09-22 阅读</sub>

- **[clash-jev](https://github.com/bytelabs-oss/clash-jev)** — 没有训练策略的皇室战争机器人：每个决策都由 Jev 现场做出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · bytelabs-oss · `Py` · 调用点 [`clash_jev/policy.py`](https://github.com/bytelabs-oss/clash-jev/blob/HEAD/clash_jev/policy.py)，2026-09-22 阅读</sub>

- **[cultivar](https://github.com/pinecone-io/cultivar)** — 在沙盒里跨环境测试你的 Agent 技能与文档。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · pinecone-io · `Py` · 调用点 [`evals/framework/typesafe_grader.py`](https://github.com/pinecone-io/cultivar/blob/HEAD/evals/framework/typesafe_grader.py)，2026-09-22 阅读</sub>

- **[dspy-typesafeify](https://github.com/typesafeainate/dspy-typesafeify)** — 给 dspy Signature 加一个装饰器，在合适处自动改用 TypeSafe。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · typesafeainate · `Py` · 调用点 [`examples/typesafe_dspy_ticket_triage/run_demo.py`](https://github.com/typesafeainate/dspy-typesafeify/blob/HEAD/examples/typesafe_dspy_ticket_triage/run_demo.py)，2026-09-22 阅读</sub>

- **[duckdb-jev](https://github.com/colliber/duckdb-jev)** — DuckDB 扩展：把 Jev 的类型化答案作为真正的 SQL 类型返回。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · colliber · `C++` · 调用点 [`src/include/jev_secret.hpp`](https://github.com/colliber/duckdb-jev/blob/HEAD/src/include/jev_secret.hpp)，2026-09-24 阅读</sub>

- **[edgejev](https://github.com/yzfly/edgejev)** — 离线可用的本地类型化决策：4 核 CPU 单题 15.6 毫秒，ONNX 加 INT8。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · yzfly · `Py` · 调用点 [`edgejev/serve.py`](https://github.com/yzfly/edgejev/blob/HEAD/edgejev/serve.py)，2026-09-22 阅读</sub>

- **[is-jeven](https://github.com/wobsoriano/is-jeven)** — 它是偶数吗？问 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · wobsoriano · `JS` · 调用点 [`index.js`](https://github.com/wobsoriano/is-jeven/blob/HEAD/index.js)，2026-09-24 阅读</sub>

- **[james_library](https://github.com/topherchris420/james_library)** — R.A.I.N. Lab：一个实验性的科学智能体架构，把快速的本地判断、独立的概率判断与推理分离开来。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · topherchris420 · `Rs` · 调用点 [`james_library/judgment/typesafe.py`](https://github.com/topherchris420/james_library/blob/HEAD/james_library/judgment/typesafe.py)，2026-09-24 阅读 · ⚠ `已归档`</sub>

- **[jeq](https://github.com/cristianoliveira/jeq)** — 当 jev 遇上 jq 会怎样？可以用管道串联的“智能”，适合快速实验和脚本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · cristianoliveira · `Go` · 调用点 [`internal/infra/typesafeapi/client.go`](https://github.com/cristianoliveira/jeq/blob/HEAD/internal/infra/typesafeapi/client.go)，2026-09-24 阅读</sub>

- **[jev](https://github.com/BorisLeMeec/jev)** — 一个 Jev 的 Claude Code 插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · borislemeec · `Go` · 调用点 [`internal/typesafe/client.go`](https://github.com/BorisLeMeec/jev/blob/HEAD/internal/typesafe/client.go)，2026-09-22 阅读</sub>

- **[Jev](https://github.com/mayank953/Jev)** — 六个实时并排的演示：Jev 负责决策，LLM 负责写字，代码掌控流程；LLM 一侧可在 Claude 与 Kimi 模型之间切换。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · mayank953 · `JS` · 调用点 [`src/jev.ts`](https://github.com/mayank953/Jev/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[jev](https://github.com/okooo5km/jev)** — 在命令行里做类型化决策：一个非官方的、只用标准库的 Python CLI 与智能体技能，面向 TypeSafe 的 Jev 模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · okooo5km · `Py` · 调用点 [`jev/scripts/jev`](https://github.com/okooo5km/jev/blob/HEAD/jev/scripts/jev)，2026-09-24 阅读</sub>

- **[jev-blindspot](https://github.com/jsk4581/jev-blindspot)** — 一个侧边栏助手，帮你找出提示词中的盲点。适用于 Claude Code 与 Codex CLI。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · jsk4581 · `TS` · 调用点 [`scripts/gate-tune.mjs`](https://github.com/jsk4581/jev-blindspot/blob/HEAD/scripts/gate-tune.mjs)，2026-09-24 阅读</sub>

- **[jev-canvas](https://github.com/gaborishka/jev-canvas)** — 用语音加手指指向在 tldraw 画布上作画：由 Jev 决定动作与目标。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · gaborishka · `JS` · 调用点 [`server/decide.js`](https://github.com/gaborishka/jev-canvas/blob/HEAD/server/decide.js)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-chat-for-twitch](https://github.com/ethanplusai/jev-chat-for-twitch)** — 用 Jev 过滤任意 Twitch 直播聊天的自带密钥 Chrome 扩展。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · ethanplusai · `JS` · 调用点 [`extension/jev.mjs`](https://github.com/ethanplusai/jev-chat-for-twitch/blob/HEAD/extension/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-chat-windows-deepseek-jev](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev)** — Windows 微信回复助手：大模型生成话术、Jev 判断排序，支持可取消的三秒自动发送。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · aimark-dai · `Py` · 调用点 [`core/typesafe_client.py`](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev/blob/HEAD/core/typesafe_client.py)，2026-09-22 阅读</sub>

- **[jev-cli](https://github.com/shaharia-lab/jev-cli)** — TypeSafe AI Jev 模型的命令行工具：对任意文本提出是非题、多选题和评分题，并得到校准后的答案。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · shaharia-lab · `Rs` · 调用点 [`crates/jev-cli/src/cli.rs`](https://github.com/shaharia-lab/jev-cli/blob/HEAD/crates/jev-cli/src/cli.rs)，2026-09-24 阅读</sub>

- **[jev-judge-mcp](https://github.com/PyModel/jev-judge-mcp)** — 面向 MCP 智能体的带类型判断工具：把 TypeSafe Jev 模型包装成 verify、screen、find、classify、rerank、decide、compare 等工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · pymodel · `Py` · 调用点 [`src/jev_judge_mcp/domain/questions.py`](https://github.com/PyModel/jev-judge-mcp/blob/HEAD/src/jev_judge_mcp/domain/questions.py)，2026-09-24 阅读</sub>

- **[jev-leftpad](https://github.com/f/jev-leftpad)** — 用 Jev 给字符串做左填充。就是想试试。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · f · `JS` · 调用点 [`src/index.js`](https://github.com/f/jev-leftpad/blob/HEAD/src/index.js)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-mcp](https://github.com/burnigtm/jev-mcp)** — 把 TypeSafe Jev 接入 Cursor、Codex 等任意 MCP 客户端编码流程的 MCP 服务器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · burnigtm · `TS` · 调用点 [`src/typesafe.ts`](https://github.com/burnigtm/jev-mcp/blob/HEAD/src/typesafe.ts)，2026-09-24 阅读</sub>

- **[jev-paint](https://github.com/achimala/jev-paint)** — 用 Jev 做艺术创作。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · achimala · `JS` · 调用点 [`web/jev.mjs`](https://github.com/achimala/jev-paint/blob/HEAD/web/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-playground](https://github.com/mizchi/jev-playground)** — 一个从 MoonBit 调用 Jev 的演练场：每种问题类型（score、choice、noul）各有一个命令行入口，并附有哪种组合模式更好的实测报告。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · mizchi · `TS` · 调用点 [`experiments/agent-questions/src/spec.ts`](https://github.com/mizchi/jev-playground/blob/HEAD/experiments/agent-questions/src/spec.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-recipes](https://github.com/agencyenterprise/jev-recipes)** — 80 多个由 Jev 驱动的可组合 TypeScript 配方，覆盖 AI 智能体、检索、答案校验与对话流程。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · agencyenterprise · `TS` · 调用点 [`examples/checkers/ai.mjs`](https://github.com/agencyenterprise/jev-recipes/blob/HEAD/examples/checkers/ai.mjs)，2026-09-24 阅读</sub>

- **[jev-register-tool](https://github.com/2951461586/Jev-Register-Tool)** — Jev 从申请到建密钥的全链路工具，纯 HTTP 无浏览器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · 2951461586 · `Py` · 调用点 [`src/typesafe.py`](https://github.com/2951461586/Jev-Register-Tool/blob/HEAD/src/typesafe.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-rules](https://github.com/EliaAlberti/jev-rules)** — 由 Jev 挑出哪些规则适用于当前提示，让模型只看到相关的那些。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · eliaalberti · `JS` · 调用点 [`plugins/jev-rules/hooks/lib/jev.mjs`](https://github.com/EliaAlberti/jev-rules/blob/HEAD/plugins/jev-rules/hooks/lib/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-seo](https://github.com/AkashPriyadarshii/jev-seo)** — 用 Rust 写的 agent 优先 SEO/GEO CLI 套件与 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · akashpriyadarshii · `Rs` · 调用点 [`src/engine.rs`](https://github.com/AkashPriyadarshii/jev-seo/blob/HEAD/src/engine.rs)，2026-09-24 阅读</sub>

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)** — Claude Code 插件：询问 Jev 哪个已安装技能适配当前提示，并记录答案（先影子运行）。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · shimo4228 · `Py` · 调用点 [`scripts/jev_client.py`](https://github.com/shimo4228/jev-skill-router/blob/HEAD/scripts/jev_client.py)，2026-09-22 阅读 · ⚠ `实测后未采用`</sub>

- **[jev-skill-suggester](https://github.com/win4r/jev-skill-suggester)** — 用 Jev 做有界的已安装技能推荐，含 Python CLI。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · win4r · `Py` · 调用点 [`scripts/jev_client.py`](https://github.com/win4r/jev-skill-suggester/blob/HEAD/scripts/jev_client.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-spring-boot-starter](https://github.com/danvega/jev-spring-boot-starter)** — 给 Spring Boot 4 的简单 Jev starter，基于 Spring MVC 与 RestClient。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · danvega · `Java` · 调用点 [`src/main/java/dev/danvega/jev/autoconfigure/JevProperties.java`](https://github.com/danvega/jev-spring-boot-starter/blob/HEAD/src/main/java/dev/danvega/jev/autoconfigure/JevProperties.java)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-studio](https://github.com/utk2103/jev-studio)** — 如果你在试用 Jev，从这里开始会更省事。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · utk2103 · `Py` · 调用点 [`jev_studio/cli/provider.py`](https://github.com/utk2103/jev-studio/blob/HEAD/jev_studio/cli/provider.py)，2026-09-22 阅读</sub>

- **[jev-tetris](https://github.com/trungdq88/jev-tetris)** — 让 Jev 实时与其他 AI 模型对战俄罗斯方块。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · trungdq88 · `JS` · 调用点 [`lib/typesafe.mjs`](https://github.com/trungdq88/jev-tetris/blob/HEAD/lib/typesafe.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-to-answer](https://github.com/csskrtao/jev-to-answer)** — 答案之书jev
  <sub>`开源项目` · ★10+ · csskrtao · `JS` · 调用点 [`src/jev.js`](https://github.com/csskrtao/jev-to-answer/blob/HEAD/src/jev.js)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-trades](https://github.com/zadescoxp/Jev-Trades)** — 用 Jev 驱动的交易机器人。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · zadescoxp · `Py` · 调用点 [`pipeline/paper_trader.py`](https://github.com/zadescoxp/Jev-Trades/blob/HEAD/pipeline/paper_trader.py)，2026-09-22 阅读</sub>

- **[jev-tree](https://github.com/Chuf-H/jev-tree)** — 原生面向 Jev 的概率树与图运行时，用于可验证的多步决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · chuf-h · `Py` · 调用点 [`src/jevtree/providers.py`](https://github.com/Chuf-H/jev-tree/blob/HEAD/src/jevtree/providers.py)，2026-09-24 阅读</sub>

- **[jev-trip](https://github.com/liaoyuhua/jev-trip)** — 两个大脑，一次旅行。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · liaoyuhua · `TS` · 调用点 [`lib/providers/jev.ts`](https://github.com/liaoyuhua/jev-trip/blob/HEAD/lib/providers/jev.ts)，2026-09-24 阅读</sub>

- **[jev-vs-ml](https://github.com/QuicqDev/Jev-vs-ML)** — Jev 与传统机器学习的对比。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · quicqdev · `Py` · 调用点 [`jevbench_v4/providers.py`](https://github.com/QuicqDev/Jev-vs-ML/blob/HEAD/jevbench_v4/providers.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[Jev_Ontology](https://github.com/dagfinndybvig/Jev_Ontology)** — 尝试把 Jev 与本体论结合起来。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · dagfinndybvig · `Py` · 调用点 [`mvp_jev_ontology.py`](https://github.com/dagfinndybvig/Jev_Ontology/blob/HEAD/mvp_jev_ontology.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev_stock](https://github.com/sosopop/jev_stock)** — 实验性框架：从结构化市场数据预测短期股价方向。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sosopop · `Py` · 调用点 [`jev_hk_predict.py`](https://github.com/sosopop/jev_stock/blob/HEAD/jev_hk_predict.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevchat](https://github.com/kyle-pena-nlp/jevchat)** — 把 Jev 变成聊天机器人。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kyle-pena-nlp · `Py` · 调用点 [`jevchat/client.py`](https://github.com/kyle-pena-nlp/jevchat/blob/HEAD/jevchat/client.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jevernetes](https://github.com/sunil-sadasivan/jevernetes)** — 由 Jev 驱动的 Kubernetes 实时日志分析、上下文调查与智能体交接。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sunil-sadasivan · `Py` · 调用点 [`jevernetes/jev.py`](https://github.com/sunil-sadasivan/jevernetes/blob/HEAD/jevernetes/jev.py)，2026-09-22 阅读</sub>

- **[jevgraph](https://github.com/chenmingtang830/jevgraph)** — 用类型化 Jev 关系决策构建有证据支撑的知识图谱。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · chenmingtang830 · `Py` · 调用点 [`src/jevgraph/benchmark.py`](https://github.com/chenmingtang830/jevgraph/blob/HEAD/src/jevgraph/benchmark.py)，2026-09-22 阅读</sub>

- **[jeview](https://github.com/andududu/jeview)** — 非官方的本地可视化工具：实时查看你的代码发出的每一次 Jev 调用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · andududu · `JS` · 调用点 [`jeview.ts`](https://github.com/andududu/jeview/blob/HEAD/jeview.ts)，2026-09-22 阅读</sub>

- **[jevify](https://github.com/altryne/jevify)** — 一个 agent 技能：发现适合用 Jev 的场景、设计类型化问题，并从近期社区实验中学习。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · altryne · `Py` · 调用点 [`scripts/jev_client.py`](https://github.com/altryne/jevify/blob/HEAD/scripts/jev_client.py)，2026-09-22 阅读</sub>

- **[jevloop](https://github.com/zjunlp/JevLoop)** — 决策不再消耗大模型调用的智能体循环：零依赖、可离线运行。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · zjunlp · `TS` · 调用点 [`bench/compare.ts`](https://github.com/zjunlp/JevLoop/blob/HEAD/bench/compare.ts)，2026-09-22 阅读</sub>

- **[jevocks](https://github.com/unicodeveloper/jevocks)** — 用 Jev 看每日股票状态。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · unicodeveloper · `TS` · 调用点 [`src/lib/classify.ts`](https://github.com/unicodeveloper/jevocks/blob/HEAD/src/lib/classify.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevplayspokemon](https://github.com/anxkhn/JevPlaysPokemon)** — 让 Jev 通过 Showdown 和真实 ROM 玩第三世代宝可梦。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · anxkhn · `TS` · 调用点 [`jev.js`](https://github.com/anxkhn/JevPlaysPokemon/blob/HEAD/jev.js)，2026-09-22 阅读</sub>

- **[jevthoven](https://github.com/cocktailpeanut/jevthoven)** — 由 Jev 驱动的 AI 音乐（MIDI）生成器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · cocktailpeanut · `TS` · 调用点 [`app/scripts/live-smoke.mjs`](https://github.com/cocktailpeanut/jevthoven/blob/HEAD/app/scripts/live-smoke.mjs)，2026-09-22 阅读</sub>

- **[jevtown](https://github.com/gaborishka/jevtown)** — 一个社交网络：真人写帖，一万个 AI 人格来回应。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · gaborishka · `JS` · 调用点 [`public/shared/jev.js`](https://github.com/gaborishka/jevtown/blob/HEAD/public/shared/jev.js)，2026-09-22 阅读</sub>

- **[jevvy](https://github.com/PanAchy/jevvy)** — 给编程智能体的 Jev 插件集。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · panachy · `TS` · 调用点 [`packages/core/src/typesafe.ts`](https://github.com/PanAchy/jevvy/blob/HEAD/packages/core/src/typesafe.ts)，2026-09-22 阅读</sub>

- **[jot](https://github.com/runta-dev/jot)** — 第一个面向 Jev 的通用 System One 智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · runta-dev · `TS` · 调用点 [`packages/jev-core/src/typesafe.ts`](https://github.com/runta-dev/jot/blob/HEAD/packages/jev-core/src/typesafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jpp](https://github.com/Towow-ai/jpp)** — J++：一门实验性语言，拥有独立源码和 Rust 运行时，可以组合问题与方法。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · towow-ai · `Rs` · 调用点 [`src/foundation/clients/eye_client.py`](https://github.com/Towow-ai/jpp/blob/HEAD/src/foundation/clients/eye_client.py)，2026-09-24 阅读</sub>

- **[laya-jev-lab](https://github.com/yibie/laya-jev-lab)** — 类型化决策模型的独立实测：Jev 对比开源权重的 Laya。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · yibie · `Py` · 调用点 [`cascade/run2-jev.mjs`](https://github.com/yibie/laya-jev-lab/blob/HEAD/cascade/run2-jev.mjs)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[laya-vs-jev-arena](https://github.com/PromptEngineer48/laya-vs-jev-arena)** — Laya（开源本地）对比 Jev（API）：两个模型比赛贪吃蛇。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · promptengineer48 · `JS` · 调用点 [`server.py`](https://github.com/PromptEngineer48/laya-vs-jev-arena/blob/HEAD/server.py)，2026-09-22 阅读</sub>

- **[llm-typesafe](https://github.com/simonw/llm-typesafe)** — 为 LLM 命令行工具访问 Jev 及其他 TypeSafe AI 模型的插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · simonw · `Py` · 调用点 [`llm_typesafe.py`](https://github.com/simonw/llm-typesafe/blob/HEAD/llm_typesafe.py)，2026-09-24 阅读</sub>

- **[loki](https://github.com/wundercorp/loki)** — 与你一同演进的智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · wundercorp · `Py` · 调用点 [`agent/typesafe_client.py`](https://github.com/wundercorp/loki/blob/HEAD/agent/typesafe_client.py)，2026-09-22 阅读</sub>

- **[open-spark-jev](https://github.com/abhishek085/open-spark-jev)** — 受 Jev 与 System One 启发、基于 Qwen3 的开源本地决策模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · abhishek085 · `Py` · 调用点 [`open_spark_jev/eval/speed_vs_generation.py`](https://github.com/abhishek085/open-spark-jev/blob/HEAD/open_spark_jev/eval/speed_vs_generation.py)，2026-09-22 阅读</sub>

- **[openthai-systemone](https://github.com/iapp-technology/openthai-systemone)** — OpenThai-SystemOne：开源的泰语加英语 System One 决策模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · iapp-technology · `Py` · 调用点 [`openthai_systemone/server.py`](https://github.com/iapp-technology/openthai-systemone/blob/HEAD/openthai_systemone/server.py)，2026-09-22 阅读</sub>

- **[pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)** — 把 Jev 作为 pi 编程智能体的安静决策层。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · hyunjunjeon · `TS` · 调用点 [`bench/src/jev_bench/providers/jev.py`](https://github.com/HyunjunJeon/pi-quiet-ask/blob/HEAD/bench/src/jev_bench/providers/jev.py)，2026-09-22 阅读</sub>

- **[st-jeved](https://github.com/mossyfield/ST-jeved)** — SillyTavern 扩展：度量每条回复，并在规则命中时指导叙述者。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · mossyfield · `JS` · 调用点 [`src/classifier.js`](https://github.com/mossyfield/ST-jeved/blob/HEAD/src/classifier.js)，2026-09-22 阅读</sub>

- **[switchboard](https://github.com/ruban-24/switchboard)** — 开源、模型无关的决策路由器，面向 Claude Code 和 Codex。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · ruban-24 · `TS` · 调用点 [`src/jev.ts`](https://github.com/ruban-24/switchboard/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[trade-jev](https://github.com/justinhe16/trade-jev)** — 在 NQ 十档盘口数据上回测 Jev 作为买／卖／持有交易者的表现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · justinhe16 · `Py` · 调用点 [`src/trade_jev/policies.py`](https://github.com/justinhe16/trade-jev/blob/HEAD/src/trade_jev/policies.py)，2026-09-22 阅读</sub>

- **[typesafe-chess](https://github.com/TholeG/typesafe-chess)** — 双方都是 Jev 的国际象棋：每一步都是一次类型化 Choice。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tholeg · `JS` · 调用点 [`jev-player.js`](https://github.com/TholeG/typesafe-chess/blob/HEAD/jev-player.js)，2026-09-22 阅读</sub>

- **[typesafe-playground](https://github.com/kavehmz/typesafe-playground)** — 围绕 Jev 的交互式实验，从工单路由到带真实 AI 决策的 3D 驾驶仿真。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · kavehmz · `JS` · 调用点 [`demo01/server.mjs`](https://github.com/kavehmz/typesafe-playground/blob/HEAD/demo01/server.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground)** — 社区版 TypeSafe AI 演练场：110 个用例、游戏、两难问题和模型挑战，可编辑提示、做 A/B 对比，并适配移动端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · typesafeai · `TS` · 调用点 [`lib/callJev.ts`](https://github.com/TypeSafeAI/typesafe-playground/blob/HEAD/lib/callJev.ts)，2026-09-24 阅读</sub>

- **[typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router)** — 给 Hermes Agent 的技能路由：在模型调用之前，指出唯一值得加载的那个技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · decrux9812 · `Py` · 调用点 [`typesafe_router/client.py`](https://github.com/DECRUX9812/typesafe-skill-router/blob/HEAD/typesafe_router/client.py)，2026-09-22 阅读</sub>

- **[xtags](https://github.com/manifoldor/xtags)** — 在 X 的时间线上，给每条帖子标出它想让你干什么 —— 判断来自只返回概率、不生成文本的 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · manifoldor · `JS` · 调用点 [`extension/service.js`](https://github.com/manifoldor/xtags/blob/HEAD/extension/service.js)，2026-09-22 阅读</sub>

- **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)** — 一个个人 Rust AI 网关，内置 TypeSafe provider，用真实响应体测试了用量提取与别名解析。
  <sub>`开源项目` · dvjn · `Rs` · 调用点 [`src/providers.rs`](https://github.com/dvjn/aegis/blob/HEAD/src/providers.rs) · ⚠ `代码未实测` `无许可证`</sub>

- **[agent-jev-tetris](https://github.com/Yasserbhb/Agent-JEV-Tetris)** — 用 JEV 玩俄罗斯方块。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · yasserbhb · `TS` · 调用点 [`server.mjs`](https://github.com/Yasserbhb/Agent-JEV-Tetris/blob/HEAD/server.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[ai-elo-ranker](https://github.com/opaielsheikh/ai-elo-ranker)** — 由 Jev 驱动的高速递归 AI Elo 锦标赛引擎，采用瑞士轮匹配。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · opaielsheikh · `Py` · 调用点 [`elo_ranker/judge.py`](https://github.com/opaielsheikh/ai-elo-ranker/blob/HEAD/elo_ranker/judge.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[ailerix](https://github.com/tylerjharden/ailerix)** — 类型安全的模型路由器：Jev 把每个请求归入一条类型化的目录路线。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tylerjharden · `TS` · 调用点 [`src/app/docs/page.tsx`](https://github.com/tylerjharden/ailerix/blob/HEAD/src/app/docs/page.tsx)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[alphaoptimizer](https://github.com/alpha-tales/alphaoptimizer)** — 由 Jev 驱动的 Codex 输出优化，让庞大的工具结果保持简洁可用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · alpha-tales · `TS` · 调用点 [`dist/src/providers/jev.js`](https://github.com/alpha-tales/alphaoptimizer/blob/HEAD/dist/src/providers/jev.js)，2026-09-22 阅读</sub>

- **[askjev](https://github.com/pZacca/askjev)** — 非官方的 Jev MCP server。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · pzacca · `TS` · 调用点 [`src/jev.ts`](https://github.com/pZacca/askjev/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[AskJev-MCP](https://github.com/cbruyndoncx/AskJev-MCP)** — TypeSafe System One API（Jev）的 MCP 服务器：带校准概率的类型化 choice/noul/score 判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · cbruyndoncx · `JS` · 调用点 [`src/index.ts`](https://github.com/cbruyndoncx/AskJev-MCP/blob/HEAD/src/index.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[auto-mode-for-paseo](https://github.com/obetomuniz/auto-mode-for-paseo)** — 一个 Paseo provider，用 Jev 路由 Codex 的每一轮。 <sub>(机翻)</sub>
  <sub>`插件` · obetomuniz · `TS` · 调用点 [`server/jev.ts`](https://github.com/obetomuniz/auto-mode-for-paseo/blob/HEAD/server/jev.ts)，2026-09-22 阅读</sub>

- **[awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases)** — 浏览基于 TypeSafe AI Jev 构建的真实用例与项目：内容审核、AI 智能体、模型路由等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · seeapi · `Py` · 调用点 [`recipes/model-routing/run.py`](https://github.com/SeeAPI/awesome-jev-use-cases/blob/HEAD/recipes/model-routing/run.py)，2026-09-24 阅读</sub>

- **[barrunto](https://github.com/elpumberto/barrunto)** — Chrome 扩展：在你浏览 X 时用 Jev 分析帖子。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · elpumberto · `TS` · 调用点 [`src/jev/real.ts`](https://github.com/elpumberto/barrunto/blob/HEAD/src/jev/real.ts)，2026-09-22 阅读</sub>

- **[beatjev](https://github.com/lambertsj/beatjev)** — 来试试能不能赢过 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lambertsj · `JS` · 调用点 [`src/worker.js`](https://github.com/lambertsj/beatjev/blob/HEAD/src/worker.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[bes-kelime-jev](https://github.com/mahmut-gundogdu/bes-kelime-jev)** — 无论你写什么，都只用五个词之一回答的聊天机器人（土耳其语）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · mahmut-gundogdu · `TS` · 调用点 [`src/jev.ts`](https://github.com/mahmut-gundogdu/bes-kelime-jev/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[btc-jev-signal](https://github.com/WebGrga/btc-jev-signal)** — 实验性的多周期 BTC 信号生成器，使用 Jev 概率与交易所数据。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · webgrga · `TS` · 调用点 [`src/experiment-jev.ts`](https://github.com/WebGrga/btc-jev-signal/blob/HEAD/src/experiment-jev.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[cairn-jev-lab](https://github.com/Cairn-ink/cairn-jev-lab)** — 测试你的 AI 应该记住什么：实验性的、感知来源的记忆准入评估器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cairn-ink · `JS` · 调用点 [`src/jev.mjs`](https://github.com/Cairn-ink/cairn-jev-lab/blob/HEAD/src/jev.mjs)，2026-09-22 阅读</sub>

- **[cartshield](https://github.com/ndolinschi/cartshield)** — CartShield：中小商户结账反欺诈判定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/cartshield/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[codex-jev-preflight](https://github.com/wellkilo/codex-jev-preflight)** — 失败时放行的 Codex 钩子，在提交提示时注入 Jev 的任务前路由元数据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · wellkilo · `Py` · 调用点 [`configure_jev.py`](https://github.com/wellkilo/codex-jev-preflight/blob/HEAD/configure_jev.py)，2026-09-22 阅读</sub>

- **[commentcop](https://github.com/ntedvs/commentcop)** — 审判你的代码注释，由 Jev 主持。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ntedvs · `TS` · 调用点 [`src/judge.ts`](https://github.com/ntedvs/commentcop/blob/HEAD/src/judge.ts)，2026-09-22 阅读</sub>

- **[cyber-breach-jev](https://github.com/rchovatiya88/cyber-breach-jev)** — 由 Jev 驱动的赛博朋克竞技场战斗游戏。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rchovatiya88 · `JS` · 调用点 [`backend/jev_client.py`](https://github.com/rchovatiya88/cyber-breach-jev/blob/HEAD/backend/jev_client.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[dbt_jev](https://github.com/smithclay/dbt_jev)** — 在 dbt 中使用 jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · smithclay · `Py` · 调用点 [`src/dbt_jev/runtime.py`](https://github.com/smithclay/dbt_jev/blob/HEAD/src/dbt_jev/runtime.py)，2026-09-24 阅读</sub>

- **[decisions-judge-mcp](https://github.com/clouatre-labs/decisions-judge-mcp)** — 把 AI 智能体的类型化决策做成一个 MCP 工具：是非概率（noul）、choice 和 score，一次快速请求完成。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · clouatre-labs · `JS` · 调用点 [`providers/typesafe-api.mjs`](https://github.com/clouatre-labs/decisions-judge-mcp/blob/HEAD/providers/typesafe-api.mjs)，2026-09-24 阅读</sub>

- **[dgp](https://github.com/numerous-com/dgp)** — Numerous ApS 的决策图协议（DGP）：面向决策型 AI 智能体的开源契约，由 TypeSafe Jev 编排。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · numerous-com · `Py` · 调用点 [`dgp_demo/providers.py`](https://github.com/numerous-com/dgp/blob/HEAD/dgp_demo/providers.py)，2026-09-24 阅读</sub>

- **[emoji-jev](https://github.com/colinmcdermott/emoji-jev)** — 跟得上打字速度的 emoji 自动补全。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · colinmcdermott · `TS` · 调用点 [`src/jev.ts`](https://github.com/colinmcdermott/emoji-jev/blob/HEAD/src/jev.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[everything-about-jev](https://github.com/qingshungLI/everything-about-jev)** — 关于 Jev 这个类型化决策模型的全面介绍。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · qingshungli · `Py` · 调用点 [`demos/python/jev_demo.py`](https://github.com/qingshungLI/everything-about-jev/blob/HEAD/demos/python/jev_demo.py)，2026-09-22 阅读</sub>

- **[extremely-specific-council](https://github.com/cbetz/extremely-specific-council)** — 十二个成员、零资质：一个带动画投票的趣味 AI 议会。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cbetz · `TS` · 调用点 [`lib/engine.ts`](https://github.com/cbetz/extremely-specific-council/blob/HEAD/lib/engine.ts)，2026-09-22 阅读</sub>

- **[financialpredictionjev](https://github.com/thodoh1/FinancialPredictionJev)** — 用 Jev 测试它预测金融市场的能力。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · thodoh1 · `Py` · 调用点 [`untitled15.py`](https://github.com/thodoh1/FinancialPredictionJev/blob/HEAD/untitled15.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[frost](https://github.com/marcus/frost)** — 灵活可配置的 CLI 模型路由器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · marcus · `Go` · 调用点 [`internal/analyzer/typesafe/typesafe.go`](https://github.com/marcus/frost/blob/HEAD/internal/analyzer/typesafe/typesafe.go)，2026-09-22 阅读</sub>

- **[functions](https://github.com/TrainLCD/Functions)** — 某移动应用的 Cloudflare Workers 后端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · trainlcd · `TS` · 调用点 [`src/cli/typesafe-triage-spike.ts`](https://github.com/TrainLCD/Functions/blob/HEAD/src/cli/typesafe-triage-spike.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[git-jev-stage](https://github.com/ibrahemid/git-jev-stage)** — 用一句大白话描述来挑选要暂存的 Git 变更。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ibrahemid · `TS` · 调用点 [`src/core/jevClient.ts`](https://github.com/ibrahemid/git-jev-stage/blob/HEAD/src/core/jevClient.ts)，2026-09-22 阅读</sub>

- **[got-jev](https://github.com/phureewat29/jev-got)** — 以《权力的游戏》为素材的 Jev 概念验证。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · phureewat29 · `TS` · 调用点 [`src/core/providers/TypeSafe.ts`](https://github.com/phureewat29/jev-got/blob/HEAD/src/core/providers/TypeSafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[ha-conversation-jev](https://github.com/luxus/ha-conversation-jev)** — Home Assistant 自定义组件：Jev 快路径加大模型兜底的对话智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · luxus · `Py` · 调用点 [`custom_components/jev_assist/jev_client.py`](https://github.com/luxus/ha-conversation-jev/blob/HEAD/custom_components/jev_assist/jev_client.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[harden-jev-decides](https://github.com/tylerjharden/harden-jev-decides)** — 由 JEV 挑选哪个直播创意成为最小可行产品的决策看板。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tylerjharden · `TS` · 调用点 [`src/lib/jev/run.ts`](https://github.com/tylerjharden/harden-jev-decides/blob/HEAD/src/lib/jev/run.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[hermes-jev-curator](https://github.com/anpicasso/hermes-jev-curator)** — 为 Hermes Curator 提供带类型的 Jev 关系治理与安全的归档计划。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · anpicasso · `Py` · 调用点 [`plugin/transport.py`](https://github.com/anpicasso/hermes-jev-curator/blob/HEAD/plugin/transport.py)，2026-09-24 阅读</sub>

- **[hiresignal](https://github.com/ndolinschi/hiresignal)** — HireSignal：简历初筛与面试匹配。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/hiresignal/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jcm-router](https://github.com/adarshmishra07/jcm-router)** — 本地代理：逐条消息用 Jev 选择 Claude 模型与推理强度，并路由子智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · adarshmishra07 · `TS` · 调用点 [`src/jev.ts`](https://github.com/adarshmishra07/jcm-router/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jeff-cli](https://github.com/saembit/jeff-cli)** — jeff：用 Go 写的 Jev 命令行工具。在 shell 脚本里给它 state 和一个固定选项的问题，就能拿回校准概率；支持排序命令和有意义的退出码。 <sub>(机翻)</sub>
  <sub>`开源项目` · saembit · `Go` · 调用点 [`pkg/jev/client.go`](https://github.com/saembit/jeff-cli/blob/HEAD/pkg/jev/client.go)，2026-09-24 阅读</sub>

- **[jev-2048](https://github.com/ARCJ137442/jev-2048)** — 带插桩的 2048 网页实验：每一步都是一次 Jev Choice。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arcj137442 · `TS` · 调用点 [`src/client/api.ts`](https://github.com/ARCJ137442/jev-2048/blob/HEAD/src/client/api.ts)，2026-09-22 阅读</sub>

- **[jev-acp](https://github.com/formulahendry/jev-acp)** — 在任意 ACP（Agent Client Protocol）客户端或 IDE 里使用 Jev 类型化决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · formulahendry · `TS` · 调用点 [`src/engine.ts`](https://github.com/formulahendry/jev-acp/blob/HEAD/src/engine.ts)，2026-09-22 阅读</sub>

- **[jev-anotacao-sentencas](https://github.com/lab-dados/jev-anotacao-sentencas)** — Jev 与两个大模型在结构化句子标注上的对比（葡萄牙语）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · lab-dados · `Py` · 调用点 [`src/jevtest/clientes.py`](https://github.com/lab-dados/jev-anotacao-sentencas/blob/HEAD/src/jevtest/clientes.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-arena-nanojev](https://github.com/liao96312/jev-arena-nanojev)** — 完全本地的 NanoJev 网格决策游戏实验场，支持中文界面与多关卡。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · liao96312 · `Py` · 调用点 [`nanojev_adapter/typesafe_client.py`](https://github.com/liao96312/jev-arena-nanojev/blob/HEAD/nanojev_adapter/typesafe_client.py)，2026-09-22 阅读</sub>

- **[jev-bot](https://github.com/nssmd/jev-bot)** — 自托管的 Jev 决策工作台与飞书机器人：自动选择、概率与证据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · nssmd · `JS` · 调用点 [`gateway.mjs`](https://github.com/nssmd/jev-bot/blob/HEAD/gateway.mjs)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-broadcast-lab](https://github.com/4anti/jev-broadcast-lab)** — Jev 的测试实验室。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 4anti · `JS` · 调用点 [`web/shared/jev-client.js`](https://github.com/4anti/jev-broadcast-lab/blob/HEAD/web/shared/jev-client.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-calculator](https://github.com/pc418/jev-calculator)** — 由 Jev 驱动的概率化 AI 计算器。 <sub>(机翻)</sub>
  <sub>`开源项目` · pc418 · `TS` · 调用点 [`shared/protocol.ts`](https://github.com/pc418/jev-calculator/blob/HEAD/shared/protocol.ts)，2026-09-24 阅读</sub>

- **[jev-chat](https://github.com/adhyaay-karnwal/jev-chat)** — 由类型化 Jev 决策构成的聊天机器人：在 System One 概率上做分层推测解码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · adhyaay-karnwal · `Py` · 调用点 [`src/jevchat/client.py`](https://github.com/adhyaay-karnwal/jev-chat/blob/HEAD/src/jevchat/client.py)，2026-09-22 阅读</sub>

- **[jev-ci-selector](https://github.com/guilhem/jev-ci-selector)** — 为 GitHub Actions 做 CI 任务选择：Jev 加一个纯策略引擎；当前默认实际应用选择，可显式开启影子模式观察。 <sub>(机翻)</sub>
  <sub>`开源项目` · guilhem · `TS` · 调用点 [`src/jev.ts`](https://github.com/guilhem/jev-ci-selector/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[jev-cli](https://github.com/jtsang4/jev-cli)** — TypeSafe AI Jev 评估模型的命令行工具：输入带类型的问题，输出结构化的 JSON 答案。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jtsang4 · `TS` · 调用点 [`src/providers/jev.ts`](https://github.com/jtsang4/jev-cli/blob/HEAD/src/providers/jev.ts)，2026-09-24 阅读</sub>

- **[jev-cloud-quiz](https://github.com/minorun365/jev-cloud-quiz)** — 一个演示：由 TypeSafe AI 的 System One 模型 Jev 带概率地判断某个功能名属于三大云中的哪一家。 <sub>(机翻)</sub>
  <sub>`开源项目` · minorun365 · `TS` · 调用点 [`server/server.mjs`](https://github.com/minorun365/jev-cloud-quiz/blob/HEAD/server/server.mjs)，2026-09-24 阅读</sub>

- **[jev-codex-router-skill](https://github.com/455-dIAO/jev-codex-router-skill)** — 可移植的 Codex 技能：Jev 模型与推理强度路由，含安全安装。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · 455-diao · `Py` · 调用点 [`jev-codex-router/scripts/route.py`](https://github.com/455-dIAO/jev-codex-router-skill/blob/HEAD/jev-codex-router/scripts/route.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-connector](https://github.com/juanlentino/jev-connector)** — TypeSafe Jev 的 WordPress 连接器：带类型、带置信度分数的答案，你的代码可以据此分支。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · juanlentino · `PHP` · 调用点 [`includes/class-client.php`](https://github.com/juanlentino/jev-connector/blob/HEAD/includes/class-client.php)，2026-09-24 阅读</sub>

- **[jev-cvss](https://github.com/Red5d/jev-cvss)** — 从漏洞描述快速给出 CVSS 评分。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · red5d · `Py` · 调用点 [`cvss31_jev.py`](https://github.com/Red5d/jev-cvss/blob/HEAD/cvss31_jev.py)，2026-09-22 阅读</sub>

- **[jev-demo](https://github.com/sawzhang/jev-demo)** — Jev 学习与实测：概念文档、5 个可运行 demo 与可复现压测 —— 实测扇出几乎免费。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · sawzhang · `TS` · 调用点 [`demo/jev_lite.py`](https://github.com/sawzhang/jev-demo/blob/HEAD/demo/jev_lite.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-demo](https://github.com/PenglongHuang/jev-demo)** — TypeSafe Jev（System One 决策模型）零依赖网页体验台：浏览器操作 / 意图识别 / Agent 上下文裁剪三大预设场景，发送状态与类型化问题，拿到带校准概率的结构化答案
  <sub>`开源项目` · penglonghuang · `JS` · 调用点 [`public/js/app.js`](https://github.com/PenglongHuang/jev-demo/blob/HEAD/public/js/app.js)，2026-09-24 阅读</sub>

- **[jev-evaluation](https://github.com/willkelly/jev-evaluation)** — 对 Jev 的对抗性评测：九个实验与 28 条预测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · willkelly · `Py` · 调用点 [`jeveval/config.py`](https://github.com/willkelly/jev-evaluation/blob/HEAD/jeveval/config.py)，2026-09-22 阅读</sub>

- **[jev-eyes](https://github.com/LeddoEngano/jev-eyes)** — 给 Jev 装上眼睛 —— 为纯文本的 System One 模型提供诚实的本地图像感知。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · leddoengano · `Py` · 调用点 [`benchmarks/jev_accuracy.py`](https://github.com/LeddoEngano/jev-eyes/blob/HEAD/benchmarks/jev_accuracy.py)，2026-09-22 阅读</sub>

- **[jev-freeform](https://github.com/kesku/jev-freeform)** — 完全由 Jev Choice 驱动的可观测逐字符聊天实验。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kesku · `JS` · 调用点 [`main.mjs`](https://github.com/kesku/jev-freeform/blob/HEAD/main.mjs)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-games](https://github.com/shantanugoel/jev-games)** — 面向多种游戏与模拟器平台的可视化 Jev 实验室。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shantanugoel · `Py` · 调用点 [`src/jev_games/games/mario/policy.py`](https://github.com/shantanugoel/jev-games/blob/HEAD/src/jev_games/games/mario/policy.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-gomoku](https://github.com/XieChengYuan/jev-gomoku)** — 弈瞬：双 Jev 五子棋实验台，逐手查看模型决策，支持对局回放与实时对战。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · xiechengyuan · `JS` · 调用点 [`server.mjs`](https://github.com/XieChengYuan/jev-gomoku/blob/HEAD/server.mjs)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-grand-prix](https://github.com/enoyola/jev-grand-prix)** — 一个 F1 赛车游戏：Jev 选择赛车线与踏板，并逐条赛道学习。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · enoyola · `JS` · 调用点 [`server.py`](https://github.com/enoyola/jev-grand-prix/blob/HEAD/server.py)，2026-09-22 阅读</sub>

- **[jev-grug](https://github.com/mkotlikov/jev-grug)** — 帮 Jev 开口说话。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · mkotlikov · `TS` · 调用点 [`lib/jev.ts`](https://github.com/mkotlikov/jev-grug/blob/HEAD/lib/jev.ts)，2026-09-22 阅读</sub>

- **[jev-mcp](https://github.com/arunav25/jev-mcp)** — 把 JEV 接入 MCP 客户端，并用共享数据集和可衡量的指标，将它的判断与通用 LLM 进行对比。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · arunav25 · `JS` · 调用点 [`eval/adapters/jev.js`](https://github.com/arunav25/jev-mcp/blob/HEAD/eval/adapters/jev.js)，2026-09-24 阅读</sub>

- **[jev-mcp](https://github.com/BYK/jev-mcp)** — 以评测为先的 TypeSafe Jev MCP 服务器；Jev 是 System One 模型，返回带概率的类型化判断（noul、choice、score），而不是生成文本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · byk · `TS` · 调用点 [`src/typesafe.ts`](https://github.com/BYK/jev-mcp/blob/HEAD/src/typesafe.ts)，2026-09-24 阅读</sub>

- **[jev-mcp](https://github.com/freepik-company/jev-mcp)** — 通过 OpenRouter 或 TypeSafe 调用 Jev / System One 做带类型决策的 MCP 服务器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · freepik-company · `Go` · 调用点 [`internal/config/config.go`](https://github.com/freepik-company/jev-mcp/blob/HEAD/internal/config/config.go)，2026-09-24 阅读</sub>

- **[jev-mcp](https://github.com/rajasekharponakala/jev-mcp)** — 封装 TypeSafe Jev System One 模型的 MCP 服务器——为 AI 智能体提供类型化的 noul/choice/score 判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · rajasekharponakala · `Py` · 调用点 [`server.py`](https://github.com/rajasekharponakala/jev-mcp/blob/HEAD/server.py)，2026-09-24 阅读</sub>

- **[jev-mcp](https://github.com/rashedInt32/jev-mcp)** — 把 TypeSafe Jev 暴露为带类型、经校准的判断工具的 MCP 服务器：classify、score、check 与批量提问，并以 Claude Code 插件形式发布。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · rashedint32 · `TS` · 调用点 [`src/index.ts`](https://github.com/rashedInt32/jev-mcp/blob/HEAD/src/index.ts)，2026-09-24 阅读</sub>

- **[jev-mcp-spring](https://github.com/Ashfaqbs/jev-mcp-spring)** — 面向 TypeSafe Jev 的 Java/Spring Boot MCP 服务器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ashfaqbs · `Java` · 调用点 [`src/main/java/dev/ashfaqbs/jevmcp/tools/JevTools.java`](https://github.com/Ashfaqbs/jev-mcp-spring/blob/HEAD/src/main/java/dev/ashfaqbs/jevmcp/tools/JevTools.java)，2026-09-24 阅读</sub>

- **[jev-measured](https://github.com/WallerChen/jev-measured)** — 在多个场景上实测 Jev 线上 API 的成本、延迟与原始输出。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · wallerchen · `Py` · 调用点 [`bench/accuracy.py`](https://github.com/WallerChen/jev-measured/blob/HEAD/bench/accuracy.py)，2026-09-22 阅读</sub>

- **[jev-minesweeper](https://github.com/comoc/jev-minesweeper)** — 让 Jev 解浏览器扫雷的演示（日语）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · comoc · `JS` · 调用点 [`lib/typesafe.mjs`](https://github.com/comoc/jev-minesweeper/blob/HEAD/lib/typesafe.mjs)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-pick-and-place-study](https://github.com/tryaksh/jev-pick-and-place-study)** — 小而可复现的 MuJoCo 试点：对比 Jev、某轻量 LLM 与反应式规则的抓取表现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tryaksh · `Py` · 调用点 [`compare.py`](https://github.com/tryaksh/jev-pick-and-place-study/blob/HEAD/compare.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-pii-checker](https://github.com/coo-quack/jev-pii-checker)** — 用 Jev 在文本中定位 PII 的 CLI：存在性、敏感度与具体位置。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · coo-quack · `TS` · 调用点 [`src/judge.ts`](https://github.com/coo-quack/jev-pii-checker/blob/HEAD/src/judge.ts)，2026-09-22 阅读</sub>

- **[jev-playground](https://github.com/wustep/jev-playground)** — System One 模型能否指挥音乐？Jev 只选方案（纯枚举），由代码渲染乐谱与音频。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · wustep · `TS` · 调用点 [`src/planner/jev/systemOne.ts`](https://github.com/wustep/jev-playground/blob/HEAD/src/planner/jev/systemOne.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-playground](https://github.com/Little-Planet-Labs/jev-playground)** — 一个用来试验 TypeSafe AI Jev 模型（System One）的小型 Next.js 应用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · little-planet-labs · `TS` · 调用点 [`src/app/api/evaluate/route.ts`](https://github.com/Little-Planet-Labs/jev-playground/blob/HEAD/src/app/api/evaluate/route.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon)** — 用 Jev 玩《宝可梦红》。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · milanboers · `Py` · 调用点 [`jev_plays_pokemon/agent.py`](https://github.com/milanboers/jev-plays-pokemon/blob/HEAD/jev_plays_pokemon/agent.py)，2026-09-22 阅读</sub>

- **[jev-practice-speed](https://github.com/tubone24/jev-practice-speed)** — WebGL 演示：与一个大脑是 Jev 的 CPU 玩快速纸牌。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tubone24 · `JS` · 调用点 [`src/core/jev-core.js`](https://github.com/tubone24/jev-practice-speed/blob/HEAD/src/core/jev-core.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-realtime-trading](https://github.com/rthomas24/jev-realtime-trading)** — 在实时行情上跑的模拟交易智能体，每秒由 Jev 决策。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rthomas24 · `TS` · 调用点 [`src/core/realtime/jev.ts`](https://github.com/rthomas24/jev-realtime-trading/blob/HEAD/src/core/realtime/jev.ts)，2026-09-22 阅读</sub>

- **[jev-resume-disqualifier](https://github.com/AiPersonacademy/jev-resume-disqualifier)** — 亚 25 毫秒的简历自动淘汰引擎。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · aipersonacademy · `Py` · 调用点 [`engine/decision_gateway.py`](https://github.com/AiPersonacademy/jev-resume-disqualifier/blob/HEAD/engine/decision_gateway.py)，2026-09-22 阅读</sub>

- **[jev-search](https://github.com/larguesa/jev-search)** — 通过 OpenRouter 用 Jev 做实验性语义行检索的 Python CLI。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · larguesa · `Py` · 调用点 [`jev_search.py`](https://github.com/larguesa/jev-search/blob/HEAD/jev_search.py)，2026-09-22 阅读</sub>

- **[jev-skills](https://github.com/laguagu/jev-skills)** — 用 Jev 构建应用的实用智能体技能与示例：API 配置、路由、排序与证据检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · laguagu · `JS` · 调用点 [`examples/decisions/run.mjs`](https://github.com/laguagu/jev-skills/blob/HEAD/examples/decisions/run.mjs)，2026-09-24 阅读</sub>

- **[jev-skills](https://github.com/WanLanglin/jev-skills)** — 由 TypeSafe System One 模型 Jev 驱动的 Claude Code 与 Codex 技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · wanlanglin · `Py` · 调用点 [`scripts/jev.py`](https://github.com/WanLanglin/jev-skills/blob/HEAD/scripts/jev.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-snake](https://github.com/iammusham/jev-snake)** — 实验性贪吃蛇环境：游戏引擎掌管确定性规则，Jev 负责决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · iammusham · `Py` · 调用点 [`snake_game/jev_agent.py`](https://github.com/iammusham/jev-snake/blob/HEAD/snake_game/jev_agent.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jev-system-one](https://github.com/haseeb-heaven/jev-system-one)** — 打磨过的终端界面，输出答案的同时给出透明的决策报告。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · haseeb-heaven · `Py` · 调用点 [`src/jev_system_one/jev.py`](https://github.com/haseeb-heaven/jev-system-one/blob/HEAD/src/jev_system_one/jev.py)，2026-09-22 阅读</sub>

- **[jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner)** — 由 Jev 模型来玩 Chrome 恐龙小游戏。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · joshlarsen · `JS` · 调用点 [`server/decision-service.mjs`](https://github.com/joshlarsen/jev-t-rex-runner/blob/HEAD/server/decision-service.mjs)，2026-09-22 阅读</sub>

- **[jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales)** — 由 Jev 裁判的擂台式动物锦标赛，本地游戏。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hectorlcastro09 · `TS` · 调用点 [`motor.py`](https://github.com/hectorlcastro09/jev-torneo-animales/blob/HEAD/motor.py)，2026-09-22 阅读</sub>

- **[jev-wingman](https://github.com/1104480426-hash/jev-wingman)** — 基于 Jev 的聊天决策辅助，不挑 App（QQ／微信／飞书皆可），端上返回类型化判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · 1104480426-hash · `Java` · 调用点 [`app/src/ai/jev/assist/Prefs.java`](https://github.com/1104480426-hash/jev-wingman/blob/HEAD/app/src/ai/jev/assist/Prefs.java)，2026-09-22 阅读</sub>

- **[jev-x-kit](https://github.com/Kadihx/jev-x-kit)** — 面向编码智能体的离线决策层：Choice/Score/Noul 原语、置信度守门与超规划，另可接入 TypeSafe 原生提供方。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kadihx · `TS` · 调用点 [`src/core/providers/typesafe-native.ts`](https://github.com/Kadihx/jev-x-kit/blob/HEAD/src/core/providers/typesafe-native.ts)，2026-09-24 阅读</sub>

- **[jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver)** — Chrome 扩展：用 Jev 遮住让人分心的 YouTube 视频，想看随时可展开。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · jaibhasin · `JS` · 调用点 [`background/background.js`](https://github.com/jaibhasin/jev-yt-time-saver/blob/HEAD/background/background.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev2048](https://github.com/KyleKreuter/jev2048)** — 让 Jev 解 2048。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kylekreuter · `TS` · 调用点 [`backend/jev.py`](https://github.com/KyleKreuter/jev2048/blob/HEAD/backend/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev_jsonschema](https://github.com/Kiln-AI/jev_jsonschema)** — 把一份 JSON Schema 丢给 Jev API，拿回 JSON。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kiln-ai · `Py` · 调用点 [`src/jev_jsonschema/client.py`](https://github.com/Kiln-AI/jev_jsonschema/blob/HEAD/src/jev_jsonschema/client.py)，2026-09-22 阅读</sub>

- **[jev_project_context](https://github.com/poiuyjie/jev_project_context)** — 面向 AI 编程智能体的证据优先长期实验记忆技能，可选接入 Jev 决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · poiuyjie · `Py` · 调用点 [`scripts/jev_client.py`](https://github.com/poiuyjie/jev_project_context/blob/HEAD/scripts/jev_client.py)，2026-09-22 阅读</sub>

- **[jevals](https://github.com/dayhaysoos/jevals)** — TypeSafe Jev 的本地评估工作台。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dayhaysoos · `TS` · 调用点 [`src/server.ts`](https://github.com/dayhaysoos/jevals/blob/HEAD/src/server.ts)，2026-09-24 阅读</sub>

- **[jevcode](https://github.com/miounet11/jevcode)** — JevCode — Jev (TypeSafe System One) 技术解决方案与最佳实践 · https://www.jevcode.ai
  <sub>`开源项目` · miounet11 · `TS` · 调用点 [`scripts/build-jev-cards.mjs`](https://github.com/miounet11/jevcode/blob/HEAD/scripts/build-jev-cards.mjs)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[Jevometry](https://github.com/Kunyanli230/Jevometry)** — 面向任意 System One（Jev 及类 Jev）智能体系统的信息几何分析工具包。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kunyanli230 · `Py` · 调用点 [`src/jevometry/adapters/typesafe.py`](https://github.com/Kunyanli230/Jevometry/blob/HEAD/src/jevometry/adapters/typesafe.py)，2026-09-24 阅读</sub>

- **[jevopt](https://github.com/Ramneet-Singh/jevopt)** — 用 Jev 做智能的编译器优化决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ramneet-singh · `Py` · 调用点 [`src/jevopt/cli.py`](https://github.com/Ramneet-Singh/jevopt/blob/HEAD/src/jevopt/cli.py)，2026-09-22 阅读</sub>

- **[jevscope](https://github.com/jeiel85/jevscope)** — 本地优先的可视化决策调试器与回归测试台，面向 TypeSafe AI Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jeiel85 · `TS` · 调用点 [`packages/provider-typesafe/src/index.ts`](https://github.com/jeiel85/jevscope/blob/HEAD/packages/provider-typesafe/src/index.ts)，2026-09-24 阅读</sub>

- **[jevseek](https://github.com/blingdivinity/jevseek)** — DeepSeek 提出下一个 token，由 TypeSafe 的 Jev 来选择：把决策模型用作采样器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · blingdivinity · `Py` · 调用点 [`src/jevseek/jev.py`](https://github.com/blingdivinity/jevseek/blob/HEAD/src/jevseek/jev.py)，2026-09-24 阅读</sub>

- **[jevslop](https://github.com/TKY-27/JevSlop)** — 用 Jev 判定 note 文章是否为 AI 水文的站点。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tky-27 · `TS` · 调用点 [`lib/jev.ts`](https://github.com/TKY-27/JevSlop/blob/HEAD/lib/jev.ts)，2026-09-22 阅读</sub>

- **[JevTape](https://github.com/Hugo-DDT/JevTape)** — Jev 决策的 Record / Replay 工具：CLI + 本地代理 + JSON 磁带，回放彻底离线。
  <sub>`开源项目` · hugo-ddt · `Java` · 调用点 [`src/main/java/io/jevtape/cassette/RecordedRequest.java`](https://github.com/Hugo-DDT/JevTape/blob/HEAD/src/main/java/io/jevtape/cassette/RecordedRequest.java)，2026-09-24 阅读</sub>

- **[jevtest](https://github.com/joshhu/jevtest)** — 情绪测谎器：嘴上说「好」，心里真的好吗？用 Jev 实时判断并与普通 LLM 对照。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · joshhu · `TS` · 调用点 [`main.py`](https://github.com/joshhu/jevtest/blob/HEAD/main.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevtok](https://github.com/LabGuy94/jevtok)** — Jev 的精确 token 计数与请求成本预测（tiktoken 风格）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · labguy94 · `Py` · 调用点 [`src/jevtok/cli.py`](https://github.com/LabGuy94/jevtok/blob/HEAD/src/jevtok/cli.py)，2026-09-22 阅读</sub>

- **[labs](https://github.com/kiarina/labs)** — 用于实验、研究与调查的小型独立项目集。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kiarina · `Py` · 调用点 [`2026/09/17/typesafe-jev-evaluation/client.py`](https://github.com/kiarina/labs/blob/HEAD/2026/09/17/typesafe-jev-evaluation/client.py)，2026-09-22 阅读</sub>

- **[magic-jev-ball](https://github.com/mikecann/magic-jev-ball)** — 一个魔术 8 号球：不随机挑答案，而是去问 Jev。基于 Convex、AI Gateway 与 three.js。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · mikecann · `TS` · 调用点 [`convex/jev.ts`](https://github.com/mikecann/magic-jev-ball/blob/HEAD/convex/jev.ts)，2026-09-24 阅读</sub>

- **[mcpmatch](https://github.com/ndolinschi/mcpmatch)** — 用两段式流程把用户目标匹配到 MCP 目录。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/mcpmatch/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[mcts-agent](https://github.com/lhemerly/mcts-agent)** — 用 System One 原语做判别式蒙特卡洛树搜索。 <sub>(机翻)</sub>
  <sub>`开源项目` · lhemerly · `Py` · 调用点 [`agent/system_one.py`](https://github.com/lhemerly/mcts-agent/blob/HEAD/agent/system_one.py)，2026-09-22 阅读</sub>

- **[mimicry](https://github.com/jxucoder/mimicry)** — 用有界反馈循环把 AI 草稿改写成你自己的语气。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jxucoder · `Py` · 调用点 [`src/mimicry/engine.py`](https://github.com/jxucoder/mimicry/blob/HEAD/src/mimicry/engine.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[n8n-nodes-jev](https://github.com/vibe-with-me-tools/n8n-nodes-jev)** — TypeSafe Jev 的 n8n 社区节点：用你定义的问题对文本做分类、路由与打分，并得到概率。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · vibe-with-me-tools · `TS` · 调用点 [`nodes/Jev/shared/descriptions.ts`](https://github.com/vibe-with-me-tools/n8n-nodes-jev/blob/HEAD/nodes/Jev/shared/descriptions.ts)，2026-09-24 阅读</sub>

- **[n8n-nodes-typesafe](https://github.com/Biztactix/n8n-nodes-typesafe)** — 用于 n8n 的 TypeSafe AI 节点。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · biztactix · `TS` · 调用点 [`nodes/TypeSafe/TypeSafe.node.ts`](https://github.com/Biztactix/n8n-nodes-typesafe/blob/HEAD/nodes/TypeSafe/TypeSafe.node.ts)，2026-09-24 阅读</sub>

- **[n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev)** — 面向 Jev 结构化 AI 决策的 n8n 社区节点。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · n3ndor · `TS` · 调用点 [`nodes/TypeSafeJev/transport.ts`](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/HEAD/nodes/TypeSafeJev/transport.ts)，2026-09-22 阅读</sub>

- **[new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe)** — 给 new-api 的 Jev 任务插件：原生 /v1/systemone、同步评估。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ffattiger · `JS` · 调用点 [`plugins/tasks/typesafe/1.1.0/plugin.js`](https://github.com/FFatTiger/new-api-plugin-typesafe/blob/HEAD/plugins/tasks/typesafe/1.1.0/plugin.js)，2026-09-22 阅读</sub>

- **[open-jev-bridge](https://github.com/louis-szeto/open-jev-bridge)** — 把类 Jev 的 System One API（本地托管或 TypeSafe Jev）接入 Codex 和 Claude Code 的 MCP 插件，用于决策任务。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · louis-szeto · `JS` · 调用点 [`bin/open-jev-bridge.mjs`](https://github.com/louis-szeto/open-jev-bridge/blob/HEAD/bin/open-jev-bridge.mjs)，2026-09-24 阅读</sub>

- **[openpoke-meets-jev](https://github.com/0xShin0221/openpoke-meets-jev)** — 某助手产品的开源实现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 0xshin0221 · `Py` · 调用点 [`server/jev/client.py`](https://github.com/0xShin0221/openpoke-meets-jev/blob/HEAD/server/jev/client.py)，2026-09-22 阅读</sub>

- **[pi-agent-foreman](https://github.com/alexshpunt/pi-agent-foreman)** — 当 Pi 智能体在活没干完时停下，把它赶回去继续。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · alexshpunt · `TS` · 调用点 [`src/typesafe.ts`](https://github.com/alexshpunt/pi-agent-foreman/blob/HEAD/src/typesafe.ts)，2026-09-22 阅读</sub>

- **[pi-typesafe](https://github.com/twilwa/pi-typesafe)** — 基于 TypeSafe AI System One API（Jev）构建的 Pi 编码智能体扩展。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · twilwa · `TS` · 调用点 [`scripts/jev-bench.ts`](https://github.com/twilwa/pi-typesafe/blob/HEAD/scripts/jev-bench.ts)，2026-09-24 阅读</sub>

- **[pong-jev](https://github.com/safzanpirani/pong-jev)** — 让 Jev 玩雅达利乒乓：每帧一个类型化 Choice 问题，不发送坐标。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · safzanpirani · `TS` · 调用点 [`src/jev.ts`](https://github.com/safzanpirani/pong-jev/blob/HEAD/src/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[pydantic-jev-examples](https://github.com/adtyavrdhn/pydantic-jev-examples)** — 用 Jev 增强 Pydantic AI 能力的小型可运行演示，每个一个文件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · adtyavrdhn · `Py` · 调用点 [`flappy_bird/jev_player.py`](https://github.com/adtyavrdhn/pydantic-jev-examples/blob/HEAD/flappy_bird/jev_player.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[r2r-jev](https://github.com/Thneoly/r2r-jev)** — 面向 AI 智能体的持久化治理——用 R2R 把 Jev 的判断变成可回放的关系状态。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · thneoly · `Rs` · 调用点 [`src/jev.rs`](https://github.com/Thneoly/r2r-jev/blob/HEAD/src/jev.rs)，2026-09-24 阅读</sub>

- **[research_desk](https://github.com/0xnairb/research_desk)** — 用 Jev 做快速分析的演示。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 0xnairb · `Py` · 调用点 [`app/desk/pipeline.py`](https://github.com/0xnairb/research_desk/blob/HEAD/app/desk/pipeline.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[risc-jev](https://github.com/i2cjak/RISC-jeV)** — 我把 Jev 折腾成了一个 RISC-V CPU。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · i2cjak · `Py` · 调用点 [`jev.py`](https://github.com/i2cjak/RISC-jeV/blob/HEAD/jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[river-run-typesafe](https://github.com/ashaazami/river-run-typesafe)** — Python 写的河流射击游戏，由 AI 飞行员驾驶。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ashaazami · `Py` · 调用点 [`typesafe_pilot/pilot.py`](https://github.com/ashaazami/river-run-typesafe/blob/HEAD/typesafe_pilot/pilot.py)，2026-09-22 阅读</sub>

- **[rubikjev](https://github.com/0xtrou/rubikjev)** — 用魔方谜题挑战 Jev 的智力。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 0xtrou · `TS` · 调用点 [`src/server/jev-engine.ts`](https://github.com/0xtrou/rubikjev/blob/HEAD/src/server/jev-engine.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[rust-sysone](https://github.com/zcoder-run/rust-sysone)** — 非官方的 System One Rust 客户端。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · zcoder-run · `Rs` · 调用点 [`src/client.rs`](https://github.com/zcoder-run/rust-sysone/blob/HEAD/src/client.rs)，2026-09-22 阅读</sub>

- **[scam-shield](https://github.com/ShupingR/scam-shield)** — 由 Jev 驱动的诈骗短信过滤器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shupingr · `TS` · 调用点 [`src/server/check.ts`](https://github.com/ShupingR/scam-shield/blob/HEAD/src/server/check.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[search-function-test](https://github.com/Shifros/Search-Function-Test)** — 基于 Jev 的试验项目，目标是给博客做搜索功能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shifros · `JS` · 调用点 [`htr-hero/src/lib/typesafeSearch.js`](https://github.com/Shifros/Search-Function-Test/blob/HEAD/htr-hero/src/lib/typesafeSearch.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[second-thought](https://github.com/KNambiarDJsc/second-thought)** — 从 System One 模型（Laya，以及你自带的类型化决策服务）学习带类型概率决策的基础设施。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · knambiardjsc · `Py` · 调用点 [`src/second_thought/adapters/jev.py`](https://github.com/KNambiarDJsc/second-thought/blob/HEAD/src/second_thought/adapters/jev.py)，2026-09-24 阅读</sub>

- **[secondlayer](https://github.com/ryanwaits/secondlayer)** — 把解码后的链上数据放进你自己的数据库，可自托管。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ryanwaits · `TS` · 调用点 [`scripts/ops/jev-fault-triage.ts`](https://github.com/ryanwaits/secondlayer/blob/HEAD/scripts/ops/jev-fault-triage.ts)，2026-09-22 阅读</sub>

- **[should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all)** — 每十分钟问一次 Jev：AI 是否应该毁灭人类。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hellogumbo · `JS` · 调用点 [`functions/api/verdict.js`](https://github.com/hellogumbo/should-ai-kill-us-all/blob/HEAD/functions/api/verdict.js)，2026-09-22 阅读</sub>

- **[skill-router](https://github.com/lomeshdutta/skill-router)** — 用 Jev 告诉 Claude Code 当前会话需要哪个已安装技能。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · lomeshdutta · `Py` · 调用点 [`src/skill_router/router.py`](https://github.com/lomeshdutta/skill-router/blob/HEAD/src/skill_router/router.py)，2026-09-22 阅读</sub>

- **[soupbase](https://github.com/spoonnotfound/soupbase)** — Jev 版海龟汤。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · spoonnotfound · `TS` · 调用点 [`src/server/providers.ts`](https://github.com/spoonnotfound/soupbase/blob/HEAD/src/server/providers.ts)，2026-09-24 阅读</sub>

- **[sqlite3-jev](https://github.com/mattn/sqlite3-jev)** — 在 SQL 中调用 TypeSafe Jev（或 tensai serve）的 SQLite 扩展。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · mattn · `C` · 调用点 [`jev.c`](https://github.com/mattn/sqlite3-jev/blob/HEAD/jev.c)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[system-one-chess](https://github.com/dperezcabrera/ai-chess-lab)** — 通过 OpenRouter 与 Jev 下国际象棋。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dperezcabrera · `Py` · 调用点 [`system_one_chess/jev.py`](https://github.com/dperezcabrera/ai-chess-lab/blob/HEAD/system_one_chess/jev.py)，2026-09-22 阅读</sub>

- **[systemone-lite](https://github.com/fritzprix/systemone-lite)** — 玩具级的本地 System One 风格决策 API，与官方无关。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · fritzprix · `Py` · 调用点 [`scripts/jevbench_eval.py`](https://github.com/fritzprix/systemone-lite/blob/HEAD/scripts/jevbench_eval.py)，2026-09-22 阅读</sub>

- **[tempo-jev-demo](https://github.com/mychaelangelo/tempo-jev-demo)** — 自然语言任务工作区，横向对比多个 AI 模型的表现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · mychaelangelo · `TS` · 调用点 [`src/server/providers/typesafe.ts`](https://github.com/mychaelangelo/tempo-jev-demo/blob/HEAD/src/server/providers/typesafe.ts)，2026-09-22 阅读</sub>

- **[typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground)** — 围绕 Jev 做实验的 playground。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · markjaquith · `Rs` · 调用点 [`src/typesafe.rs`](https://github.com/markjaquith/typesafe-ai-playground/blob/HEAD/src/typesafe.rs)，2026-09-22 阅读</sub>

- **[typesafe-assist](https://github.com/JanOstrowka/typesafe-assist)** — 由 Jev 驱动的 Home Assistant 对话智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · janostrowka · `Py` · 调用点 [`custom_components/typesafe_conversation/api.py`](https://github.com/JanOstrowka/typesafe-assist/blob/HEAD/custom_components/typesafe_conversation/api.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-comment](https://github.com/Hexdigest123/typesafe-comment)** — 用若干启发式规则评估代码注释的小型 Python 包。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hexdigest123 · `Py` · 调用点 [`typesafe_comment/client.py`](https://github.com/Hexdigest123/typesafe-comment/blob/HEAD/typesafe_comment/client.py)，2026-09-22 阅读 · ⚠ `已归档`</sub>

- **[typesafe-jev-examples](https://github.com/rajivkuriakose/typesafe-jev-examples)** — Jev 的实战示例，今天就能通过 OpenRouter 跑起来。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rajivkuriakose · `Py` · 调用点 [`src/jevx/client.py`](https://github.com/rajivkuriakose/typesafe-jev-examples/blob/HEAD/src/jevx/client.py)，2026-09-22 阅读</sub>

- **[typesafe-jev-mcp](https://github.com/anasbekheit/typesafe-jev-mcp)** — 把 Jev 暴露成类型化 evaluate 工具的 MCP server。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · anasbekheit · `Rs` · 调用点 [`src/jev.rs`](https://github.com/anasbekheit/typesafe-jev-mcp/blob/HEAD/src/jev.rs)，2026-09-22 阅读</sub>

- **[typesafe-jev-tools](https://github.com/wotai-dev/typesafe-jev-tools)** — 一个 Claude Code 钩子：判断你正在写的这个决策到底需不需要模型。附带一份实测的 149 行对比。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · wotai-dev · `TS` · 调用点 [`hooks/typesafe-check.sh`](https://github.com/wotai-dev/typesafe-jev-tools/blob/HEAD/hooks/typesafe-check.sh)，2026-09-24 阅读</sub>

- **[typesafe-ui](https://github.com/TypeSafeAI/typesafe-ui)** — shadcn 风格的可复用组件与区块，用于接入 TypeSafe AI。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · bunsdev · `TS` · 调用点 [`apps/web/components/demos.tsx`](https://github.com/TypeSafeAI/typesafe-ui/blob/HEAD/apps/web/components/demos.tsx)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe_chess_eval](https://github.com/AliceRoselia/Typesafe_chess_eval)** — 对 Jev 下棋能力的评测 —— 结论是它下得并不好。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · aliceroselia · `Py` · 调用点 [`Chess.py`](https://github.com/AliceRoselia/Typesafe_chess_eval/blob/HEAD/Chess.py)，2026-09-22 阅读</sub>

- **[typesafeai-cli](https://github.com/maddygoround/typesafeai-cli)** — 给你的 AI 智能体配一个能访问 TypeSafe AI Jev 的命令行伙伴。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · maddygoround · `Py` · 调用点 [`src/typesafe_cli/client.py`](https://github.com/maddygoround/typesafeai-cli/blob/HEAD/src/typesafe_cli/client.py)，2026-09-24 阅读</sub>

- **[wellposed](https://github.com/suraj-phanindra/wellposed)** — 在 jev 请求自信地给出错误答案之前，先对请求本身做检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · suraj-phanindra · `JS` · 调用点 [`skills/wellposed/scripts/semantic.mjs`](https://github.com/suraj-phanindra/wellposed/blob/HEAD/skills/wellposed/scripts/semantic.mjs)，2026-09-24 阅读</sub>

- **[your-signal](https://github.com/MithrilMan/your-signal)** — 开源的自带密钥 Chrome 扩展：个人化、可撤销的 X 时间线过滤。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · mithrilman · `JS` · 调用点 [`eval/run.py`](https://github.com/MithrilMan/your-signal/blob/HEAD/eval/run.py)，2026-09-22 阅读</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
