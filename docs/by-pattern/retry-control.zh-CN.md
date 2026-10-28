# 重试控制

<sub>[awesome-jev](../../README.zh-CN.md) · [English](retry-control.md)</sub>

_判断失败的步骤是否值得重试。_

这个决策的全部已收录例子 —— 共 8 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#重试控制)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=retry-control&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#retry-control)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#retry-control)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 0 · 调用点 7 · 接口形态 1 · 仅示例 0 · 独立报告 0 · 负面结果 0 · 未引用文件 0。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

目录里没有归在这个模式下的 TypeSafe AI 官方材料。 <sub>(机翻)</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

- **[DuoMind](https://github.com/j1s4nn/duomind)** — 一个 OpenAI 兼容的本地服务器，把 llama.cpp 上的小模型与 Jev 搭配：在生成之前、之中和之后共 18 个决策点（是否需要推理、是否安全、输出格式、是否该停、是否重试）引导本地模型。提示词会发送给 TypeSafe，生成过程留在本地。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · j1s4nn · `Py` · `noul` · `choice` · 调用点 [`src/duomind/jev_client.py`](https://github.com/j1s4nn/duomind/blob/HEAD/src/duomind/jev_client.py)，2026-10-24 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)** — 面向 AI 编码智能体的决策关卡，提供 CLI、MCP 服务器、CI 钩子以及 Python、TypeScript 和 Rust SDK：先用离线启发式规则，再可选地交给 Jev 判断：失败的测试日志是否需要动用 LLM、是否中止反复修改的循环、该用哪个模型档位和推理力度、某一步是否已完成。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · ismaelsoilet · `Py` · 调用点 [`src/jev_harness/client.py`](https://github.com/ismaelsoilet/jev-harness/blob/HEAD/src/jev_harness/client.py)，2026-09-24 阅读</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — 面向智能体开发者的网页应用：粘贴某一步的执行轨迹，由 Jev 判定为通过、重试、升级或停止。没有 TYPESAFE_API_KEY 时，本地启发式规则返回同样结构的答案，并标为演示模式。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ndolinschi · `TS` · 调用点 [`src/lib/jev.ts`](https://github.com/ndolinschi/harnessjudge/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · Really Artificial · `JS` · `choice` · `score` · `noul` · 调用点 [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs)，2026-09-22 阅读 · ⚠ `疑似 AI 生成`</sub>

- **[jev-reasoning-navigator](https://github.com/AndreuVM/praxeon)** — JEV 推理导航器：面向自主 LLM 智能体的认知监督、防止循环与反幻觉引擎。 <sub>(机翻)</sub>
  <sub>`开源项目` · andreuvm · `Py` · 调用点 [`jev_navigator/core/typesafe_client.py`](https://github.com/AndreuVM/praxeon/blob/HEAD/jev_navigator/core/typesafe_client.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 面向 WebFlux 的 Spring Boot Starter：标注了 @SemanticCircuitBreaker 的方法会把每个响应体发给 Jev，用一个 noul 判断这个 HTTP 200 是否掩盖了错误、堆栈信息或维护通知；超过阈值（示例中为 0.85）就抛出熔断器可以计数的异常。失败即放行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · vicente-md · `Java` · 调用点 [`src/main/java/ai/jev/resilience/client/dto/JevRequest.java`](https://github.com/Vicente-MD/jev-resilience/blob/HEAD/src/main/java/ai/jev/resilience/client/dto/JevRequest.java)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jevswiftsdk](https://github.com/NSStudent/JevSwiftSDK)** — 独立、非官方、零依赖的 System One API Swift SDK：choice、noul 和 score 问题都映射为 Swift 类型（比如对枚举的 choice），具名批量问题一次调用作答并逐个校验答案，支持按策略重试和取消。支持 iOS 15+、macOS 12+ 和 Linux。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · nsstudent · `Swift` · 调用点 [`Sources/JevSwiftSDK/Configuration.swift`](https://github.com/NSStudent/JevSwiftSDK/blob/HEAD/Sources/JevSwiftSDK/Configuration.swift)，2026-09-22 阅读</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)** — Jev 形状的本地决策层：是非、选择和量表问题都从本地模型单个 token 的 logprob 读出答案；附带一个在留出命令集上测量过的 Claude Code 权限闸门。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · Xinyu Liu · `TS` · `noul` · `choice` · `score` · 引用文件 [`src/gate.ts`](https://github.com/liu-x27/XavierJev/blob/HEAD/src/gate.ts)，2026-09-25 阅读 · ⚠ `并非 Jev 本身` `疑似 AI 生成`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
