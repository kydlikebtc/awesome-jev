# 机器学习特征抽取

<sub>[awesome-jev](../../README.zh-CN.md) · [English](feature-extraction.md)</sub>

_把自由文本转成数值特征，喂给下游的传统模型。_

这个决策的全部已收录例子 —— 共 8 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#机器学习特征抽取)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=feature-extraction&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#feature-extraction)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#feature-extraction)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 1 · 调用点 7 · 接口形态 0 · 仅示例 0 · 独立报告 0 · 负面结果 0 · 未引用文件 1。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) <sub>`官方文档` · `Py`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

- **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐ — 一个自动研究循环：自己提出问题、把自由文本转成数值特征、再用误差反过来改进下游的梯度提升回归模型。
  <sub>`官方文档` · `Py`</sub>

- **[nimble](https://github.com/bespokelabsai/nimble)** — 本地类型化决策、对比式数据筛选与模型评测。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · bespokelabsai · `Py` · 调用点 [`nimble/evaluation/evaluate_public_jev.py`](https://github.com/bespokelabsai/nimble/blob/HEAD/nimble/evaluation/evaluate_public_jev.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — 从人类反馈出发，构建经过校准的决策函数。
  <sub>`开源项目` · ★100+ · sutro-sh · `Py` · 调用点 [`src/jev_align/jev.py`](https://github.com/sutro-sh/jev-align/blob/HEAD/src/jev_align/jev.py)，2026-09-22 阅读</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `score` · 调用点 [`engine/jev-service.ts`](https://github.com/irfndi/prism-liquidity-agent/blob/HEAD/engine/jev-service.ts)，2026-09-22 阅读</sub>

- **[JEV Sees](https://github.com/CharlesFeng0314/JEV_sees)** — 让 Jev“看见”：本地的 Florence-2 和 CLIP 模型在图像、视频或 RGB-D 画面中找出物体，并在帧之间保持物体 ID 一致，然后由 Jev 针对每个相关物体回答 choice、noul 或 score 问题（如公交车颜色、行人风险、动物运动状态）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · charlesfeng0314 · `Py` · `choice` · `noul` · `score` · 调用点 [`jev_sees/session.py`](https://github.com/CharlesFeng0314/JEV_sees/blob/HEAD/jev_sees/session.py)，2026-10-24 模型阅读</sub>

- **[jev-board-lab](https://github.com/WebGrga/jev-board-lab)** — 面向 Jev Board 数据集的交互式浏览与问题工作区。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · webgrga · `JS` · 调用点 [`worker/src/index.js`](https://github.com/WebGrga/jev-board-lab/blob/HEAD/worker/src/index.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-calibrated-narrative-coding](https://github.com/pozapas/jev-calibrated-narrative-coding)** — 用 System One 模型把警方的交通事故叙述，校准地转换为带概率的事故变量。包含完整流程。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · pozapas · `Py` · 调用点 [`src/jev_runner.py`](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/HEAD/src/jev_runner.py)，2026-09-24 阅读</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — 把每次 LLM 调用下沉到能胜任的最便宜模型，路由由 Jev 在约 180 毫秒内决定，无需训练。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · iamvatsalpatel · `TS` · 调用点 [`bench/experiments/gate-experiment.ts`](https://github.com/iamvatsalpatel/tiershift/blob/HEAD/bench/experiments/gate-experiment.ts)，2026-09-22 阅读</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
