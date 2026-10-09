# 项目索引

## 主要项目

2026-09-27 最初完成六个项目入口；用户随后取消独立 ops 维护层，当前主要项目为下面五个。网页源码、环境、正式 8015、runtime／uv 和恢复证据已归入 cobot-web；三机 ops 本地目录验收后删除。2026-09-28 已完成当前 RLT、硬件入口与约158GB数据切换，并在完整归档及独立运行核验后删除对应旧RLT、cobot-platform和旧数据根；共享驱动、π0.5及其他旧VLA资产仍保留登记依赖。历史跨项目迁移由 cobot_rlt 对话统筹；2026-10-09 用户停用并清理该笔记本入口，当前任务由对应领域项目负责，每次只处理一个可验收范围。

| 项目 | 职责 | 状态 |
|---|---|---|
| [cobot-control](cobot-control/README.md) | 硬件、独立前后双臂、CAN／ROS／相机、示教与归位。 | 共用 CAN／设备规则、示教显示与独立 CLI 已发布；TX 卡死根因、驱动重建及剩余动作验收待现场 |
| [cobot-dagger](cobot-dagger/README.md) | 数采、HIL、mask 与 DAgger 迭代。 | 录制迟到补采已修复，新增积压/时延诊断；领域 80 项及合成 480 帧验证通过，真实 HIL 与持续录制待验收 |
| [vla-platform](vla-platform/README.md) | 基于 FluxVLA；模型、Franka／Cobot、RTC 与真机／仿真评测。 | π0.5 两套原始权重恢复到获准 NVMe 路径；真实预热暂停加载及无指令影子验证通过，连续真机与 Getea 底层故障仍待处理 |
| [rl-platform](rl-platform/README.md) | RLT、EXPO-FT 的统一实验入口，保留算法独立实现。 | 离线候选/完整恢复核验、控制发布与反馈采样修复已交付；首轮完整受控 Online、自主持续收益及 EXPO-FT 适配待验证 |
| [cobot-web](cobot-web/README.md) | 网页、API 编排、命令行使用、任务／状态、网页故障与恢复。 | 独立相机预览、π0.5 原始权重恢复与退出释放修复已交付；暂停加载/影子验证通过，连续真机全流程待操作者验收 |

Franka、各模型、RTC、ZR-0／LiLaWAM 及仿真评测归入 vla-platform；RLT、EXPO-FT 归入 rl-platform。归属登记不表示旧代码或资产已完成迁移。每次只迁移一个可验收范围，验证后切换，再清理对应旧文件。

## 已有算法与工具

- [Codex 手机通知](codex-notify/README.md)：`v0.1.0` 已按 MIT 公开发布；CLI／插件通知实收、托盘开关及旧会话重启恢复均有验收记录，后续维护升级兼容性。

- [框架工具](../tools/README.md)：归 agent-guide 维护的长期工具与辅助脚本。
- [EXPO-FT × Cobot](expo-ft/README.md)：环境与原始数据读取准备完成；两处依赖修改未提交，SFT/replay 适配、真实 batch 和训练待完成。
- [各机器空间清理](storage-cleanup/README.md)：最新 10 月 9 日 D1/D2 清理 51 文件／1.646 GiB；当时 C 盘可用 1.763 GiB，私有报告已归档 A6000，本地目录归位待项目对话处理。

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

## 2026-10-07 实习材料项目

- [智能门锁测试材料](smart-lock-testing/README.md)：77 个原始文件及 demo 已公开发布至 `ajwwja777/smart-lock-testing`，源码 Word 凭据已脱敏，A6000 与 GitHub main 同为 `53a7377`。简历数量统计待逐项核验。来源：本次材料导入与发布回执。

## 2026-10-09 摘要复核与材料项目

上方当前摘要依据实际项目 10 月 5–9 日的记录及已有验收回执更新；下方和前文历史版本表仅代表各自核对日期。本轮未复跑现场服务、训练或动作，也未操作其他项目 Git。

- [校园 VPN](campus-vpn/README.md)：最新记录改为精确网关域名使用动态 114 DNS、校园网关选择 DIRECT；物理 WLAN HTTPS 和配置验证通过，新 VPN 会话及切换网络后的业务仍待项目复验。此前默认香港9为历史方案。
- 申请材料项目 `school-application`：笔记本入口 `D:\Code\jiaan_workspace\school-application\AGENTS.md`。目前已有上传材料、版本稿和本地生成工具；尚无 A6000 实际工作区，待项目对话迁移并只保留本地必需内容。个人材料不写入公开 guide；未建立 Git。
- 审稿能力与评价 agent 项目 `paper-review-agent`：笔记本入口 `D:\Code\jiaan_workspace\paper-review-agent\AGENTS.md`。已有上传材料及检查预览；尚无 A6000 实际工作区，待项目对话迁移整理，未建立 Git。此登记不表示审稿完成或 agent 已实现；稿件、评审细节不纳入公开 guide。

智能门锁项目 10 月 7 日已有 README 总览更新（A6000 HEAD `b030184`）；前文 `53a7377` 是材料首次发布版本。材料、生成成果与缓存按用途处理，八个待整理项目和工作区散落文件目前只完成盘点，未由框架对话清理。

来源：2026-10-09 本地文件、A6000 实际目录与项目记录核对。后续整理结果由对应项目对话更新摘要。

## 2026-10-09 后续：EXPO-FT 与废弃 cobot_rlt 的本地副本清理完成

EXPO-FT 仅保留笔记本 AGENTS.md；完整旧 Git/未提交成果归 A6000 scratch/expo-ft/laptop-migration-20261009/repository，两个原始 Git 索引差异另存 cleanup-original-git-metadata。旧 cobot_rlt 目录已移除，34 份 RL 历史分析/图表归 RL，9 份网页文件归 web，2 份交接入口归 guide；当前维护按五领域入口进行。

两处本地旧副本已移入可恢复回收站并核验原路径消失，未清空回收站；代码运行与项目 Git 不留在 EXPO-FT 笔记本入口。归档/清理收据见 scratch/agent-guide/retired-cobot-rlt-20261009/receipt.json 与 scratch/expo-ft/laptop-migration-20261009/cleanup-result-20261009.json。来源：用户本次授权及实际操作回执，未操作其他项目 Git 或现场服务。
