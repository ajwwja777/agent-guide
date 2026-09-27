# 统一 RL 实验平台

目标：参考 FluxVLA 的模块化方式组织配置、数据／Replay、采样、学习、模型发布与评测；先接入 RLT，再按现有进度接入 EXPO-FT。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\rl-platform\AGENTS.md`。
- 仓库：[ajwwja777/rl-platform](https://github.com/ajwwja777/rl-platform)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/rl-platform`，本轮未部署或切换。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `3063ae62a7043184e7331d877d1e89bb067b18cc`；补充发布记录后提交 `a08a1df03c7d8a416ad5412c9f3210049d7acf1d`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 下一步与协作

先登记并验证当前 RLT warmup 5k 模型及现有评测的完整来源，做固定输入的离线加载对照；不启动新的在线学习。

Replay、奖励、learner 与在线更新由本项目负责；推理预处理交 vla-platform；硬件控制交 cobot-control；网页编排交 cobot-web，算法服务和存储由本项目排查。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。
