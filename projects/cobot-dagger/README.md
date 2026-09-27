# Cobot 采集、HIL 与 DAgger

目标：统一人工与模型辅助采集、HIL 事件、数据格式、训练 mask、质量校验和 DAgger 迭代流程，训练通过 vla-platform 接入。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-dagger`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-dagger/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\cobot-dagger\AGENTS.md`。
- 仓库：[ajwwja777/cobot-dagger](https://github.com/ajwwja777/cobot-dagger)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/cobot-dagger`，本轮未部署或切换。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `16a9f37c9381596244bc4f4a5db1677d31f851a8`；补充发布记录后提交 `f3b0b41e245e3a366351ae22515785dfafbca48e`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 下一步与协作

先迁移一份数据格式说明、样例校验与转换入口，以现有一条成功保存的 episode 做离线对照，不改变现场录制服务。

缺帧、节点、标签和 mask 由本项目负责；物理示教状态交 cobot-control；模型训练执行和归一化交 vla-platform。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。
