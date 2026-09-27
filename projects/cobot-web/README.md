# Cobot 操作网页

目标：保留现有操作台、统一采集、训练和部署页面，以及相机／输出面板、模型与任务状态交互。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\cobot-web\AGENTS.md`。
- 仓库：[ajwwja777/cobot-web](https://github.com/ajwwja777/cobot-web)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/cobot-web`，本轮未部署或切换。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `7d81a477adb6e89625bb9454d6c3d465cc237966`；补充发布记录后提交 `d08e656a6e8f16b3bd4ab64269c270dd9e52a5b8`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 下一步与协作

先制作当前页面与 API 的版本快照，迁移一个可隔离的静态资源／只读页面范围，以独立验证入口核对，不占用或替换现有 8015 服务。

页面和展示问题由本项目负责；业务状态错误交对应控制／采集／模型／RL 项目；进程、存储和日志异常交 cobot-ops。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。
