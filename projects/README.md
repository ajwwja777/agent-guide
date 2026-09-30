# 项目索引

## 主要项目

2026-09-27 最初完成六个项目入口；用户随后取消独立 ops 维护层，当前主要项目为下面五个。网页源码、环境、正式 8015、runtime／uv 和恢复证据已归入 cobot-web；三机 ops 本地目录验收后删除。2026-09-28 已完成当前 RLT、硬件入口与约158GB数据切换，并在完整归档及独立运行核验后删除对应旧RLT、cobot-platform和旧数据根；共享驱动、π0.5及其他旧VLA资产仍保留登记依赖。跨项目迁移由当前 cobot_rlt 对话统筹，每次只处理一个可验收范围。

| 项目 | 职责 | 状态 |
|---|---|---|
| [cobot-control](cobot-control/README.md) | 硬件、独立前后双臂、CAN／ROS／相机、示教与归位。 | 共用 CAN／设备规则、示教显示与独立 CLI 已发布；TX 卡死根因、驱动重建及剩余动作验收待现场 |
| [cobot-dagger](cobot-dagger/README.md) | 数采、HIL、mask 与 DAgger 迭代。 | 录制保留模型恢复、暂存与历史结果修复已发布；采集领域 78 项回归通过，真实 HIL 全流程待现场 |
| [vla-platform](vla-platform/README.md) | 基于 FluxVLA；模型、Franka／Cobot、RTC 与真机／仿真评测。 | 共用 Hz／RTC／滤波配置与暂停适配器已接入；CPU／合成与 dry-run 通过，各模型连续真机待验收 |
| [rl-platform](rl-platform/README.md) | RLT、EXPO-FT 的统一实验入口，保留算法独立实现。 | MC30 诊断、可选异步 RTC 与 NVMe Stage1 引用已发布；自主收益、在线分支及连续 50 Hz 待现场，EXPO-FT 待适配 |
| [cobot-web](cobot-web/README.md) | 网页、API 编排、命令行使用、任务／状态、网页故障与恢复。 | 方法／步数、历史结果、所选执行参数与两行权重路径已发布；734 后端／69 前端回归通过，视觉和真机全流程待现场 |

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

## 2026-09-30 校园 VPN 排障

- [campus-vpn](campus-vpn/README.md)：网关 Fake-IP 冲突、用户名格式及浏览器 HTTP 转发问题已定位并绕行；手机关闭校园 Wi-Fi 后，Cobot 网页与 SSH 经校园 VPN 验收通过。后续已统一校园域名与 10/8 分流，保留热点局域网直连，并加入“校园访问”选择组切换 DIRECT／校园代理；普通 A6000/Cobot SSH、Cobot 网页及 HPC SSH banner 验收通过，未登录 HPC。详见项目记录；本次未初始化 Git 或部署容器。来源：campus-vpn 项目对话。

## 2026-10-01 框架复核

依据各项目最新记录及已有发布回执更新上方摘要；本轮只读核对 A6000 Git 与 GitHub 分支，不复跑现场服务、训练或动作。下表为本次核对的版本，历史表保留当时状态。

| 项目 | 本地与 GitHub main 一致的提交 |
|---|---|
| cobot-control | `64899d14` |
| cobot-dagger | `127b3f34` |
| cobot-web | `bdf2e087` |
| vla-platform | `a9f87e0f` |
| rl-platform | `bf111eb7` |
| codex-notify | `52fe0b3b` |
| storage-cleanup | `d786d0bc` |
| expo-ft | `803381fc` |

EXPO-FT 的两处依赖修改仍未提交，适配／训练待开展；PREPARATION.md 合并仍交对应项目对话。校园 VPN 记录纳入 guide；Monitor 与 Ctrl+Shift+V 图片粘贴的最新验证见 [工具说明](../tools/README.md)。三个项目摘要中的问号段落已按实际原文与 JSON 发布回执重写；实际项目文档的同类损坏仍由对应项目对话处理。
