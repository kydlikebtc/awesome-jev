# history/

One JSON file per weekly refresh, named by the UTC date it ran
(`YYYY-MM-DD.json`), written by
[`scripts/snapshot_stats.py`](../scripts/snapshot_stats.py) in
[`metadata.yml`](../.github/workflows/metadata.yml) just before that refresh's
commit. Each holds every number `_stats.compute()` published that day; rows
per kind, pattern, flag, language and declared licence; the value of each
question [`watch.json`](../watch.json) counts; since 2026-10-30, the
discovery queue's candidates in each state (to read, held, parked, ...); and
each row's slug, stars, licence and flags.

These are generated data, not a source of truth: `catalog.json` is, and
nothing reads a snapshot back into it. Do not edit or add files here by hand.
Nothing was backfilled from git's history of `catalog.json`, because nobody
published those numbers at the time. [`docs/shape.md`](../docs/shape.md)
reads the files for its "Over time" table once there are three. A star count
is GitHub's at the refresh: a popularity signal, not a quality verdict.

`traffic/` holds a second kind of snapshot, once a `TRAFFIC_TOKEN` secret
exists (since 2026-10-24): GitHub's own traffic figures for this repository
(views and clones per day, the top ten referrers and paths) for the 14 days
before each weekly refresh, written by
[`scripts/snapshot_traffic.py`](../scripts/snapshot_traffic.py). Successive
files overlap, so count a day once. They are GitHub's numbers, not a counter of
this repository's own, and public once committed.

## 中文 <sub>(机翻)</sub>

每次每周刷新写一个 JSON 文件，按运行当天的 UTC 日期命名（`YYYY-MM-DD.json`），由
[`metadata.yml`](../.github/workflows/metadata.yml) 在该次刷新提交之前运行
[`scripts/snapshot_stats.py`](../scripts/snapshot_stats.py) 写入。每个文件记录当天
`_stats.compute()` 公布的全部数字；按类型、模式、标记、语言和声明的许可证统计的行数；
[`watch.json`](../watch.json) 所计数的每个问题的值；自 2026-10-30 起，发现队列各状态（待读、等人看、暂缓等）的候选数；以及每一行的
slug、star、许可证和标记。

这些是生成的数据，不是事实来源：事实来源是 `catalog.json`，任何快照都不会被读回其中。请不要手动编辑或添加这里的文件。
没有根据 `catalog.json` 的 git 历史回填，因为当时没有人公布过那些数字。
[`docs/shape.zh-CN.md`](../docs/shape.zh-CN.md) 在有三份快照后会读取它们，生成「随时间的变化」表。
star 数是刷新时 GitHub 的计数：热度信号，不是质量结论。

在配置了 `TRAFFIC_TOKEN` secret 之后（自 2026-10-24 起），`traffic/` 存放另一种快照：
每次每周刷新之前 14 天里 GitHub 为本仓库统计的访问数据（每天的浏览和克隆次数、前十个来源站点和前十个页面），
由 [`scripts/snapshot_traffic.py`](../scripts/snapshot_traffic.py) 写入。相邻文件的时间段会重叠，同一天只算一次。
这些是 GitHub 自己的数字，本仓库没有另设计数器；提交之后即公开。
