# Cobot 硬件与独立前后双臂控制

## 当前交接状态（2026-09-29）

硬件健康、CAN/ROS检查与设备任务规则已归 src/cobot_control，网页只转发；独立 scripts/control.py 与网页共用 runtime/devices。换机配置、Piper/Astra/SDK源码快照、系统helper/udev/sudoers来源及安装入口已登记。3项真实无害进程测试覆盖重复启动、PID复用与组停止；关闭web仍能读取同一相机PID524014。公共工作区没有删除，aloha未升级。干净catkin构建受Docker代理阻挡，硬件动作仍待现场。

已push并核验 main：f238b6495a21f5fe839cdd4d857b78fbaf44ae7b；Cobot副本 /home/agilex/jiaan/project/cobot-control 已逐文件SHA复核。A6000主项目 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-control，先读README结构和docs/DEPLOYMENT.md，详细批次见docs/MIGRATION.md。

数据/模型实体保持 /media/agilex/Getea1/jiaan/{data,model}；本批未搬迁或新增其备份。完整跨项目交付：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/HANDOFF_20260929.md。来源为本次实际源码、Git核验及现场只读检查；guide Git不由本会话提交。

框架复核（2026-09-29）：已只读核对 A6000 项目 HEAD 与 origin/main 一致，并对照实际项目 docs/MIGRATION.md 和 [跨项目交付记录](../../../projects/cobot-web/docs/HANDOFF_20260929.md)。上述测试与现场状态来自项目验收记录，本次未连接 Cobot 或重跑测试；实时 PID、模型与采集状态需现场重新查询。

以下保留此前阶段记录；旧路径、PID与“尚未迁移”描述应按上述最新状态及所属项目迁移记录理解。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-control`；先读AGENTS.md与README.md。
- Cobot：`/home/agilex/jiaan/project/cobot-control`。
- 仓库：[ajwwja777/cobot-control](https://github.com/ajwwja777/cobot-control)，独立仓库，main分支。
- 详细记录：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-control/docs/MIGRATION.md`。

目标：维护独立前后双臂、CAN、ROS、相机、示教按钮、控制权、归位与恢复，保留已验证的硬件语义。

## 历史阶段状态（2026-09-28）

- 主代码、硬件脚本、ROS launch与现场位姿均在本项目；A6000为Git主工作区。当前ffced01已push，同步Cobot114文件SHA一致。
- 342项硬件回归通过。六个臂/交接节点在front/mid/rear auto_enable=false下被动启动注册正常；三相机640×480 RGB8约29.9FPS。
- 网页重复硬件实现已移除，web保留转发。旧cobot-platform隔离后，从新web/control实际启动/停止相机、读取三路帧并核验home --help，随后旧平台原目录删除。
- scripts/system/cobot-can-recover-one保存现场root helper原源码；未改sudo策略、未重新安装。
- 本会话被动验收launch已停止；后来网页启动的arms148006/cameras158179保留，最终5臂/5CAN/3相机可用。本会话未归位或进行示教动作。已有相机calibration缺失提示并非迁移丢失文件。
- 已安装ROS/Piper/Astra工作区和aloha SDK仍作为共享依赖保留；Piper/Astra/SDK源码快照1,374条目/70.96MB已异机SHA保全，系统/包版本见configs/environments/cobot-hardware.json。不是已验收的从零环境重建，不能整棵删除/home/agilex/cobot_magic。

## 此前阶段的接续与协作

早期被动验收按用户断电授权执行；后续现场状态已变为硬件节点运行。先查最新状态，避免重复launch；现场按手册做后臂示教接管、同步/夹爪及退出示教短测。本项目负责硬件状态与行为；网页任务/PID/显示交cobot-web，模型或动作输出交rl-platform/vla-platform。证据见docs/HARDWARE_SOURCE.md及docs/MIGRATION.md。

来源：cobot_rlt迁移会话，2026-09-28；对应项目迁移记录、现场测试与Git核验。历史阶段细节以实际项目MIGRATION为准；本会话只维护guide摘要，不提交或推送guide Git。


## 2026-09-28 存储方案更新

Cobot 数据与模型统一在 /media/agilex/Getea1/jiaan/data/ 和 /media/agilex/Getea1/jiaan/model/。数据按场景分、模型按项目/模型分；本轮不新增 A6000 权重备份。代码、安装环境、运行日志与 PID 留在 /home/agilex/jiaan/project/<项目>/。完整路径与批次状态见相邻 cobot-web/docs/STORAGE.md。
当前批次正在复制/验证及切换。以上旧 /home/agilex/jiaan/data、项目内 models 路径属于迁移前状态；最终完成结论以所属项目 docs/MIGRATION.md 最新批次为准。Guide 本轮只更新记录，由其负责 agent 提交。

## 2026-09-28 Getea1 迁移当前状态

主体数据/权重已迁移到 /media/agilex/Getea1/jiaan/{data,model}，新路径网页历史及 RLT 加载验收后清理了主体旧副本。20:00 Getea1 USB 掉线，FluxVLA 环境/暂存副本的验收和清理未完成；网页已正常停止，迁移进程已退出。恢复识别后先核对文件系统和资产校验，再续迁移，不要直接开始在线训练。详细证据见实际 cobot-web/docs/STORAGE.md 和所属项目 docs/MIGRATION.md。来源：cobot_rlt 迁移会话；未新增 A6000 数据/权重备份，guide Git 不由本会话提交。

## 2026-09-28 20:56：Getea1 存储迁移完成

本批已完成复制、哈希与运行验收、切换和对应旧文件清理。Getea1/jiaan 只保留 data、model；旧系统盘数据/模型目录移除。数据按场景/用途/方法归类，位姿与动作回放归 data/motion；模型按项目/模型/场景/版本归类。代码/环境/日志/PID 留在 /home/agilex/jiaan/project/<项目>。

USB 掉线重连后已完成已迁移资产的全量收据复核；尚不能据此认定硬件链路根因已消除。RLT 新路径暂停加载、在线状态恢复与历史媒体通过；FluxVLA 固定版本离线 baseline/prefix-RTC 通过；π0.5 两入口只做 dry-run。本批未启动真实 Episode 或机器人动作。

完整路径、占用、各项验证边界及回执见实际 cobot-web/docs/STORAGE.md。证据位于 rl-platform/outputs/migrations/20260928-getea-storage/cobot/（Cobot 去掉末尾 cobot/）。同批源码与项目记录已按各自仓库发布；guide Git 保持由其他会话管理。


## 2026-09-29：硬件规则共用已切换

来源：cobot_rlt 跨项目整理。control 7329949、web 43569ff 已 push，Cobot 分别 132/218 文件 SHA 一致。硬件探测与进程管理归 control/src/cobot_control；CLI scripts/control.py 使用 control/runtime/devices，与网页相同。67 项兼容测试、3 项真实无硬件进程组测试通过。空闲时只重启网页；相机 PID524014 保持，网页与 CLI 一致。详情见实际项目 docs/MIGRATION.md；control 新增 docs/DEPLOYMENT.md。五项目环境重建、统一模型接入及网页后续修复仍进行中。Guide Git 未提交。
