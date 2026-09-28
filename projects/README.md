# 项目索引

## 主要项目

2026-09-27 最初完成六个项目入口；用户随后取消独立 ops 维护层，当前主要项目为下面五个。网页源码、环境、正式 8015、runtime／uv 和恢复证据已归入 cobot-web；三机 ops 本地目录验收后删除。旧硬件、模型、RLT 和历史数据仍保留登记依赖。跨项目迁移由当前 cobot_rlt 对话统筹，每次只处理一个可验收范围。

| 项目 | 职责 | 状态 |
|---|---|---|
| [cobot-control](cobot-control/README.md) | 硬件、独立前后双臂、CAN／ROS／相机、示教与归位。 | 代码已迁入；被动节点／相机检查通过，上电示教待现场验收 |
| [cobot-dagger](cobot-dagger/README.md) | 数采、HIL、mask 与 DAgger 迭代。 | 已初始化并 push；待逐批迁移 |
| [vla-platform](vla-platform/README.md) | 基于 FluxVLA；模型、Franka／Cobot、RTC 与真机／仿真评测。 | 历史资产已接管；FluxVLA 运行适配未完成 |
| [rl-platform](rl-platform/README.md) | RLT、EXPO-FT 的统一实验入口，保留算法独立实现。 | 新 Stage 1 加载／固定输入推理通过，正式网页已切换；历史归档进行中 |
| [cobot-web](cobot-web/README.md) | 网页、API 编排、命令行使用、任务／状态、网页故障与恢复。 | 正式 8015 已切换新项目路径；模型与媒体检查通过，现场操作待验收 |

Franka、各模型、RTC、ZR-0／LiLaWAM 及仿真评测归入 vla-platform；RLT、EXPO-FT 归入 rl-platform。归属登记不表示旧代码或资产已完成迁移。每次只迁移一个可验收范围，验证后切换，再清理对应旧文件。

## 已有算法与工具

- [框架工具](../tools/README.md)：归 agent-guide 维护的长期工具与辅助脚本。
- [EXPO-FT × Cobot](expo-ft/README.md)：已有独立算法仓库，作为 rl-platform 的方法依赖保留；准备进度见原项目记录。
- [各机器空间清理](storage-cleanup/README.md)：基础已发布至 ajwwja777/storage-cleanup；Windows 盘点与占用核验可用，首次确认清理已留记录。

ops 不再有独立项目入口；本地目录已清理，历史 Git、备份和删除回执见 [cobot-web](cobot-web/README.md)。

2026-09-28 索引状态依据各项目对话写入的摘要同步；具体版本、迁移回执与未完成项以对应项目记录为准。
