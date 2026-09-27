# Cobot 硬件与独立前后双臂控制

目标：统一前后双臂独立控制、CAN、ROS、相机、示教按钮、控制权切换、归位与恢复。保留已验证的控制语义和现场操作方式。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-control`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-control/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\cobot-control\AGENTS.md`。
- 仓库：[ajwwja777/cobot-control](https://github.com/ajwwja777/cobot-control)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/cobot-control`，本轮未部署或切换。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `ff565f2abe977473c7e2f087cfa48b13d4a841bd`；补充发布记录后提交 `be7cc99ef093efd87c65c803a86f642a3571bd7e`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 下一步与协作

选择一个可隔离的设备状态查询入口，核清依赖后复制到新位置，比较新旧状态语义和错误处理；第一批不改变运动逻辑。

CAN、反馈、相机和归位问题由本项目负责；网页任务／PID 问题交 cobot-web，硬件服务和存储问题在实际负责项目排查；模型输出异常交 vla-platform。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。
