# 项目索引

## 主要项目

2026-09-27 最初完成六个项目入口；用户随后取消独立 ops 维护层，当前主要项目为下面五个。网页源码、环境、正式 8015、runtime／uv 和恢复证据已归入 cobot-web；三机 ops 本地目录验收后删除。2026-09-28 已完成当前 RLT、硬件入口与约158GB数据切换，并在完整归档及独立运行核验后删除对应旧RLT、cobot-platform和旧数据根；共享驱动、π0.5及其他旧VLA资产仍保留登记依赖。跨项目迁移由当前 cobot_rlt 对话统筹，每次只处理一个可验收范围。

| 项目 | 职责 | 状态 |
|---|---|---|
| [cobot-control](cobot-control/README.md) | 硬件、独立前后双臂、CAN／ROS／相机、示教与归位。 | 共用硬件规则与独立CLI已发布；源码材料/配置/安装入口齐备；进程验收通过，驱动重建和动作待验收 |
| [cobot-dagger](cobot-dagger/README.md) | 数采、HIL、mask 与 DAgger 迭代。 | 35个采集领域模块已迁入并现场切换；独立环境75项测试通过，真实HIL时序待现场 |
| [vla-platform](vla-platform/README.md) | 基于 FluxVLA；模型、Franka／Cobot、RTC 与真机／仿真评测。 | 统一登记与历史薄适配已发布；Flux冻结环境独立恢复通过；新GPU/真机验收待完成 |
| [rl-platform](rl-platform/README.md) | RLT、EXPO-FT 的统一实验入口，保留算法独立实现。 | 运行边界独立、冻结环境恢复、78项在线及35项Stage1契约通过；EXPO-FT待适配，真实在线更新待验收 |
| [cobot-web](cobot-web/README.md) | 网页、API 编排、命令行使用、任务／状态、网页故障与恢复。 | 正式8015已同步；607项后端/39项DOM通过，无模型历史可读；视觉与真机全流程待现场 |

Franka、各模型、RTC、ZR-0／LiLaWAM 及仿真评测归入 vla-platform；RLT、EXPO-FT 归入 rl-platform。归属登记不表示旧代码或资产已完成迁移。每次只迁移一个可验收范围，验证后切换，再清理对应旧文件。

## 已有算法与工具

- [Codex 手机通知](codex-notify/README.md)：`v0.1.0` 已按 MIT 公开发布；CLI／插件通知实收、托盘开关及旧会话重启恢复均有验收记录，后续维护升级兼容性。

- [框架工具](../tools/README.md)：归 agent-guide 维护的长期工具与辅助脚本。
- [EXPO-FT × Cobot](expo-ft/README.md)：环境与原始数据读取准备完成；两处依赖修改未提交，SFT/replay 适配、真实 batch 和训练待完成。
- [各机器空间清理](storage-cleanup/README.md)：最新 9 月 28 日 R1–R3 清理 1209 文件／0.688 GiB；当时 C 盘可用 4.410 GiB，下一步系统清理候选待单独确认。

ops 不再有独立项目入口；本地目录已清理，历史 Git、备份和删除回执见 [cobot-web](cobot-web/README.md)。

2026-09-28 索引状态依据各项目对话写入的摘要同步；具体版本、迁移回执与未完成项以对应项目记录为准。

2026-09-29：上述五项目状态依据本批实际代码、独立环境测试、Git main和Cobot逐文件SHA核验更新。详见各摘要最新节与 cobot-web/docs/HANDOFF_20260929.md；未执行机器人运动，guide Git仍由负责对话提交。

## 2026-09-29 框架复核版本

下表是本次只读核对的 A6000 HEAD 与 Git 远端分支；测试和现场状态来自所属项目验收记录，未在本次复跑。

| 项目 | 分支 | 本地与远端一致的提交 |
|---|---|---|
| cobot-control | main | `f238b64` |
| cobot-dagger | main | `910ddc0` |
| cobot-web | main | `82ecfc8` |
| vla-platform | main | `052a3c5` |
| rl-platform | main | `c6b640e` |
| codex-notify | main | `52fe0b3` |
| storage-cleanup | main | `d786d0b` |
| expo-ft | main | `803381f` |
| expo-ft 内嵌 OpenPI | expo_ft | `46407a4` |

EXPO-FT 的 `pyproject.toml`、`uv.lock` 仍有未提交修改；本次只发布 guide。其 `PREPARATION.md` 尚待对应项目对话按单 README 约定合并。
