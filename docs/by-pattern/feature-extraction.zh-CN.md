# 机器学习特征抽取

<sub>[awesome-jev](../../README.zh-CN.md) · [English](feature-extraction.md)</sub>

_把自由文本转成数值特征，喂给下游的传统模型。_

这个决策的全部已收录例子 —— 共 8 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#机器学习特征抽取)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=feature-extraction&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐ — 一个自动研究循环：自己提出问题、把自由文本转成数值特征、再用误差反过来改进下游的梯度提升回归模型。
  <sub>`官方文档` · `Py`</sub>

- **[nimble](https://github.com/bespokelabsai/nimble)** — 本地类型化决策、对比式数据筛选与模型评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1,699 · bespokelabsai · `Py` · ⚠ `无许可证`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — 从人类反馈出发，构建经过校准的决策函数。
  <sub>`开源项目` · ★284 · sutro-sh · `Py`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★97 · `TS` · `choice` · `score`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。
  <sub>`开源项目` · ★45 · `Rs` · `score` · `noul`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — 把每次 LLM 调用下沉到能胜任的最便宜模型，路由由 Jev 在约 180 毫秒内决定，无需训练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · iamvatsalpatel · `TS`</sub>

- **[jev-board-lab](https://github.com/WebGrga/jev-board-lab)** — 面向 Jev Board 数据集的交互式浏览与问题工作区。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · webgrga · `JS` · ⚠ `无许可证`</sub>

- **[jev-calibrated-narrative-coding](https://github.com/pozapas/jev-calibrated-narrative-coding)** — 用 System One 模型把警方的交通事故叙述，校准地转换为带概率的事故变量。包含完整流程。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · pozapas · `Py`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
