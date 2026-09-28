# 统一 RL 实验平台

目标：参考 FluxVLA 的模块化方式组织配置、数据／Replay、采样、学习、模型发布与评测；先接入 RLT，再按现有进度接入 EXPO-FT。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\rl-platform\AGENTS.md`。
- 仓库：[ajwwja777/rl-platform](https://github.com/ajwwja777/rl-platform)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/rl-platform`，代码已同步，现场服务切换待验收。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `3063ae62a7043184e7331d877d1e89bb067b18cc`；补充发布记录后提交 `a08a1df03c7d8a416ad5412c9f3210049d7acf1d`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 下一步与协作

先登记并验证当前 RLT warmup 5k 模型及现有评测的完整来源，做固定输入的离线加载对照；不启动新的在线学习。

Replay、奖励、learner 与在线更新由本项目负责；推理预处理交 vla-platform；硬件控制交 cobot-control；网页编排交 cobot-web，算法服务和存储由本项目排查。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。

## 2026-09-27 RLT 业务迁移进展

主代码已迁入并发布 1f57443c19ac3ae948ca8dcf922b2c29ba0d6cbf；自有 upstream 独立仓库 ajwwja777/rlt-openpi 8cef77e 作为固定子模块。Cobot 同步 501 文件；当前模型、环境复制完成，新路径 preflight 5000/2500/2567 通过。A6000 无机器人恢复测试通过：新增 1 条模拟 transition 后恰好 5 次更新，重启不重复更新。1,731 个历史 warmup 文件已复制、校验到新项目；详见项目 README、RUNBOOK、MIGRATION。

用户允许断电状态重启节点。Cobot SSH/ping 在实际权重验证期间失联，尚未取得 Stage 1 验证结果；数据全量校验／旧资产异机归档未完成，网页路径切换和节点重启未执行，旧项目均保留。优先恢复连接、读取任务结果再继续，不宣称在线真机交付完成。本摘要由 cobot_rlt 迁移会话写入，guide Git 不由该会话提交。

## 2026-09-28 接续进度

新Stage1实际加载、固定输入推理通过；正式8015已切换，固定5k/最新在线模型均ready且暂停。Cobot独立副本测试5000/2500→5005/2502，正式资产SHA不变；11,123数据文件约158GB完整校验，媒体可读。历史跨机归档仍在执行，原件保留。

来源：对应项目docs/MIGRATION.md的实测记录。无真实Episode／运动测试；旧目录清理见后续回执。guide Git由原负责agent管理。
