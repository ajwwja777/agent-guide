# Cobot 硬件与独立前后双臂控制

## 2026-09-30：项目对话入口与并行协作交接

用户指定 cobot-control 对话负责本领域，允许多个专题及 fork 并行。笔记本 D:\Code\jiaan_workspace\cobot-control\AGENTS.md 指向本项目；职责、当前问题、worktree/任务范围登记与现场单一负责人约定见 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-control/AGENTS.md。对话不共享实时上下文，接管重查 Git 和现场，不沿用历史 PID/版本。
硬件规则已下沉，网页与终端共用；可诊断新增 CAN drop、持续 TX 堵塞/排空。TX 卡死根因尚未锁定，无人值守自动 CAN 重置未启用。
来源：cobot_rlt 本次用户指示及实际代码/记录核对；仅追加项目事实，guide Git 不提交/推送。


## 2026-09-29 示教显示防闪烁（最新）

用户复测确认进入示教不再闪黄，移动偶发黄色、退出瞬间仍闪黄。control ace3b1f / web fdd6cdc已push并同步Cobot146/197文件：共用只读显示改为普通偏差持续2秒≥0.25rad才告警、<0.15rad稳定0.5秒恢复，软信号确认1秒；原1秒接管保留。已确认示教退出最多1.5秒绿色“正在退出示教”，允许按钮/CAN残留/逐步失能先后到达，超时仍告警且不反复延长。前臂本体示教、明确硬件/CAN/ROS/控制通路故障及≥0.50rad偏差仍立即提示；不改真实控制、动作、HIL或安全参数。

100项设备/任务/健康回归通过，覆盖移动滞后、退出消息顺序/卡住/重入/双侧独立与故障优先。空闲时只重载8015，臂PID1318293、相机PID1317979保持；正式API健康、五路TX队列空。未发机器人动作；本版实际连续移动/退出颜色仍待用户观察。规则与发布事实见实际项目docs/MIGRATION.md、control/docs/DEPLOYMENT.md；完整回执位于control/outputs/diagnostics/teach-release-20260929/release.json（A6000），现场对应control/runtime/diagnostics/teach-release-20260929/release.json。guide Git不提交。

## 2026-09-29 中臂首次归位与示教排查（本轮最新）

来源：cobot_rlt 会话实际源码、被动CAN/ROS诊断及用户授权的小幅动作。control 5247de8 / web 412f31a 已push并同步146/197文件；硬件语义保留。修正mode=2/teach=1示教解析、latched协调器状态和配对故障显示；新增只读TX队列停滞诊断。中臂home增加无故障且已使能standby的原位ROS初始化，不嵌入Recover，冷上电动作仍待验证。

左右CAN曾在持续接收时TX停滞，队列各10帧并有gs_usb echo告警；用户确认现场条件后已受控恢复，队列清空。通过原home_front服务验证两前臂各0.01rad往返，返回误差<0.0005rad；未启动模型，正式位姿/控制参数未改。首次人工示教复测暴露latched状态误判，已修正并重载，第二次复测仍待用户操作；修正后3分钟只读观察均为空闲健康，网页与CLI五路TX状态一致，没有把这段空闲观察算作示教验收。完整过程与证据见所属项目docs/MIGRATION.md、control/outputs/diagnostics/teach-and-mid-20260929。guide Git不由本会话提交。

## 2026-09-29 五臂 CAN 无接收排查

用户报告接口已配置且 ERROR-ACTIVE、五臂无接收，重插 USB 无效，重插同时带电源/CAN的臂端线后恢复。12:02 后只读采样确认五路各约 6,090 帧/2秒、无新增 RX/TX 错误；11:55 有 gs_usb echo 告警，11:57 日志对应 USB 逐个重连。根因未锁定，臂端供电/初始化/连接为候选，不能把恢复归结为已证明的接触不良。本轮未运行配置/发送检测或控制指令，未改变服务。证据及源码判断见实际项目 docs/MIGRATION.md 最新节，outputs/diagnostics/can-reconnect-20260929/；事实记录已 push，guide Git 不提交。


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


## 2026-09-29：模型选择与选臂位姿本批交付

来源：cobot_rlt 对话本次用户要求及现场只读验收。位姿记录支持前臂向同侧后臂共用、显式四/五臂独立值及同名选臂覆盖；单夹爪开合补 --side，已有单夹爪恢复保留。控制语义/参数未变，CAN自动复位未启用。

control 15c1917 / web fd8d182 已push、核对远端并同步Cobot，146/197文件SHA一致；404项Python与44项Node回归通过，浏览器1800/1200/760宽度布局检查通过。仅重载空闲8015；机械臂、相机、在线RLT进程PID与Session UUID保留，正式位姿数据不变，无动作验证。发布前已有RLT Session fault / recorder_not_ready，重载后仍保留，不能称为全流程已正常。详见实际项目docs/MIGRATION.md本批记录及cobot-web/outputs/model-pose-layout-20260929/release.json。Guide Git未提交/推送。

## 2026-09-29：CAN事件与及时输出交付

来源：cobot_rlt实际现场只读采样。control f830dd21已push并同步。
CanTxMonitor增加新增drop计数、持续堵塞/排空事件；独立scripts/can_diagnose.py读tc/sysfs/ip，
网页和CLI共用规则。9项测试通过，含真实Python子进程未结束时输出已可读。
DeviceController/home.sh早期反馈且PYTHONUNBUFFERED=1，未绕过预检或改动作参数。

现场五路队列0、新增drops0，网页与终端一致。历史前臂drop不能当当前故障；
根因未重现确认，无人值守链路修复未开启，BUS-OFF restart-ms与TX卡死分开说明。
“排空”只是观察恢复，不冒称系统已自动修复；未CAN reset、未重启硬件或运动。
诊断：cd /home/agilex/jiaan/project/cobot-control 后 python3 scripts/can_diagnose.py --seconds 2。
完整边界和下一步真机验收见实际docs/DEPLOYMENT.md、MIGRATION.md。
Guide只追加事实，不提交/推送Git。

2026-09-30 交接发布核验：cobot-control 64899d14971befb1d220f67f592cd4c767de50b4 = origin/main，A6000工作树干净；本批选中文档/源码已逐文件SHA同步Cobot。详细回执 projects/cobot-web/outputs/pause-recovery-20260930/handoff-release.json；guide Git未提交。
