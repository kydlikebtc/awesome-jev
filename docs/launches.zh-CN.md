# 发布榜

[English](launches.md)

目录收录能找到的所有 Jev 公开示例。发布榜是叠在目录之上的一层，只面向产品：每周由产品的 Maker 发布，大家投票，周末收榜排名。它回答的是"这周大家用 Jev 做了什么，大家怎么看"。

每个 Launch 旁边并排放着两样东西，二者从不相加：

- **票数**：有多少人关心，按下面的规则计票。
- **证据**：产品是否真的调用 Jev，谁读过那段代码。和目录里每一行记录的是同一份证据。

名次只是票数的排序，不是本目录的推荐。这里的一切都与 TypeSafe AI 无关。

榜单页面在站点上：[发布榜](https://kydlikebtc.github.io/awesome-jev/launches.zh.html)（[English](https://kydlikebtc.github.io/awesome-jev/launches.html)），每个产品一页（`products/<slug>.html`），每位 Maker 一页（`makers/<login>.html`）。下面的规则都写在代码里：[`scripts/launches.py`](../scripts/launches.py)。

## 进度

| 阶段 | 加了什么 | 状态 |
| --- | --- | --- |
| 产品页和 Maker 页 | 每个产品、每位 Maker 一页；榜单列出每周新收录的产品 | 已完成（2026-11-03） |
| 读取投票 | [`launch-votes.yml`](../.github/workflows/launch-votes.yml) 手动运行，读取一个 Discussion 上的点赞 | 已完成；等开启 Discussions |
| 开放发布 | 发布表单、每个 Launch 一个投票帖、每小时统计、每周收榜 | 下一步 |
| 日榜 | 从周榜改为日榜 | 等每周的 Launch 足够多 |

开放发布之前，榜单列出最新一周进入目录的产品，先按谁读过调用点、再按星标排序。这是排序，不是排名。

## 什么可以发布

**产品**是目录里满足以下条件的一行：类型为 `project`、`plugin`、`sdk` 或 `integration`，带代码，并且是用 Jev 做决策的示例（没有 `not-jev` 或 `shadow-mode-only` 标记）。文章、视频、教程、基准测试和替代品留在目录里，不参与发布。

还没被收录的产品，先按常规方式加入目录（[CONTRIBUTING.md](../CONTRIBUTING.md#adding-an-entry)）；发布需要先有这一行。

同一个产品 60 天内最多发布一次。

## 谁来发布

- **Maker**：这一行 `makers` 里的 GitHub 登录名；没有 `makers` 时，取 `author.url` 里的登录名。Maker 是仓库的所有者或协作者，在读他们的 issue 时核对。
- **Hunter**：替别人发布产品的人。Launch 会记下他们，产品的 Maker 之后仍可认领。
- 发现管线自动收录的行，在有人发布之前没有 Launch。

Maker 可以提一个 pull request，添加 `makers/<login>.json`（[schema](../schema/maker.schema.json)），在自己的页面上写名字、链接和中英文各一句介绍。页面上列出的产品始终来自目录。

Maker 还可以通过 [confirm-entry 表单](https://github.com/kydlikebtc/awesome-jev/issues/new?template=confirm-entry.yml) 或 pull request，给产品加上 `tagline`（及 `tagline_zh`）和 `demo_url`。tagline 是 Maker 自己的话，模型从不代写。

## 一周的流程

周按 ISO 周计算：周一 00:00 UTC 到周日 23:59 UTC。

1. 下一周的 Launch 在周四 23:59 UTC 前提交。提交时自动检查；检查拿不准的交给人决定，和发现候选的做法一样（[docs/held.txt](held.txt)）。
2. 本周的 Launch 和它们需要的新行，随 owner 周五的合并进入 `main`。
3. 周一开榜。每个 Launch 有一个 GitHub Discussion，在帖子上点赞就是投票。
4. 开榜期间，榜单按随机顺序展示，不显示票数，免得大家只给排在前面的投票。
5. 收榜时统计票数，结果写入 `launches/<YYYY>-W<ww>.json`（[schema](../schema/launch.schema.json)）。至少计到一票的前三名获得徽章。

## 怎么计票（规则 v1）

- 每个 GitHub 账号一票，必须在本周内投出。
- 产品 Maker 和 Launch 提交者自己的票不计。
- 投票时注册不满 30 天、或读不到注册时间的账号，按半票计。
- 按计入的票数排名。同票时证据强的在前（有人读过调用点，其次模型读过，其次脚本匹配，最后没有证据），再同则先提交的在前。

规则从不原地修改：新规则用下一个名字（`v2`），每个已收榜的周都记录当时用的规则。

仓库只保存数字：多少票、计入多少、打了折扣的有多少。从不保存谁投了票。

## 绝不做的事

- 不出售排名，不因为钱把一个 Launch 排到另一个前面。
- 发现刷票（成批新账号、买票）的 Launch 会被下榜，原因留在当周的文件里。
- 榜单不请任何人投票，也不在本仓库之外发帖。

## 文件

| 路径 | 内容 | 由谁写 |
| --- | --- | --- |
| `catalog.json` | 产品，含 `makers`、`tagline`、`tagline_zh`、`demo_url` | 贡献者和 Maker |
| `launches/<YYYY>-W<ww>.json` | 一周：它的 Launch、状态，收榜后的结果 | 发布工作流 |
| `makers/<login>.json` | Maker 自己的介绍，可选 | Maker 本人 |
| `scripts/launches.py` | 上面所有规则 | |
| `scripts/check_launches.py` | 按这些规则校验 `launches/` 和 `makers/` | |
| `scripts/launch_votes.py` | 读取一个 Discussion 的投票 | |
| `scripts/site_products.py` | 产品页、Maker 页和榜单页 | |

`python3 scripts/check_launches.py` 和其他检查一起运行（`python3 scripts/check.py`）。
