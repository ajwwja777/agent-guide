# 项目索引

## 主要项目

2026-09-27 已完成六个项目的入口、Git 发布与记录，Cobot 六个项目目录及数据目录也已建立。恢复证据已迁入 cobot-ops 并验收清理原目录，cobot-web 源码、环境与正式 8015 已迁入新目录，旧依赖仍保留。跨项目迁移由用户指定的当前 cobot_rlt 对话统筹，每次只处理一个可验收范围。

| 项目 | 职责 | 状态 |
|---|---|---|
| [cobot-control](cobot-control/README.md) | 硬件、独立前后双臂、CAN／ROS／相机、示教与归位。 | 已初始化并 push；待逐批迁移 |
| [cobot-dagger](cobot-dagger/README.md) | 数采、HIL、mask 与 DAgger 迭代。 | 已初始化并 push；待逐批迁移 |
| [vla-platform](vla-platform/README.md) | 基于 FluxVLA；模型、Franka／Cobot、RTC 与真机／仿真评测。 | 已初始化并 push；待逐批迁移 |
| [rl-platform](rl-platform/README.md) | RLT、EXPO-FT 的统一实验入口，保留算法独立实现。 | 已初始化并 push；待逐批迁移 |
| [cobot-web](cobot-web/README.md) | 网页、API 编排、任务与状态展示。 | 正式 8015 已切换并验证；继续完善共享模型加载与采集交互 |
| [cobot-ops](cobot-ops/README.md) | 使用、部署、健康检查、日志／PID、备份与故障分流。 | 目录与恢复证据迁移已验收；业务待迁移 |

Franka、各模型、RTC、ZR-0／LiLaWAM 及仿真评测归入 vla-platform；RLT、EXPO-FT 归入 rl-platform。归属登记不表示旧代码或资产已完成迁移。每次只迁移一个可验收范围，验证后切换，再清理对应旧文件。

## 已有算法与工具

- [Agent 工具](agent-tools/README.md)：长期工具与辅助脚本。
- [EXPO-FT × Cobot](expo-ft/README.md)：已有独立算法仓库，作为 rl-platform 的方法依赖保留；准备进度见原项目记录。
- [各机器空间清理](storage-cleanup/README.md)：基础已发布至 ajwwja777/storage-cleanup；Windows 盘点与占用核验可用，首次确认清理已留记录。
