# Cobot 操作网页

## 当前交接状态（2026-09-29）

正式8015已切换五项目共用实现；统一模型登记/CLI、目录历史独立模型、可调输出任务列表与日志整理已发布。后端607通过/6跳过、DOM39通过；后续小修44项通过。无模型warmup目录111条记录与JPEG读取通过。交付回执记录模型offline、采集idle、机械臂节点stopped、相机PID524014保持；handover_publisher_unavailable因此尚待硬件启动后验证。浏览器未连接，未做截图验收。

已push并核验 main：82ecfc8f3f3769e049fe7a053997640065cd3f0d；Cobot副本 /home/agilex/jiaan/project/cobot-web 已逐文件SHA复核。A6000主项目 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web，先读README结构和docs/DEPLOYMENT.md，详细批次见docs/MIGRATION.md。

数据/模型实体保持 /media/agilex/Getea1/jiaan/{data,model}；本批未搬迁或新增其备份。完整跨项目交付：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/HANDOFF_20260929.md。来源为本次实际源码、Git核验及现场只读检查；guide Git不由本会话提交。

框架复核（2026-09-29）：已只读核对 A6000 项目 HEAD 与 origin/main 一致，并对照实际项目 docs/MIGRATION.md 和 [跨项目交付记录](../../../projects/cobot-web/docs/HANDOFF_20260929.md)。上述测试与现场状态来自项目验收记录，本次未连接 Cobot 或重跑测试；实时 PID、模型与采集状态需现场重新查询。

以下保留此前阶段记录；旧路径、PID与“尚未迁移”描述应按上述最新状态及所属项目迁移记录理解。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web`；先读AGENTS.md与README.md。
- Cobot：`/home/agilex/jiaan/project/cobot-web`。
- 仓库：[ajwwja777/cobot-web](https://github.com/ajwwja777/cobot-web)，独立仓库，main分支。
- 详细记录：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/MIGRATION.md`。

目标：维护操作台、统一采集、训练与部署页面，以及相机/输出面板、共享模型、任务状态和终端恢复。

## 历史阶段状态（2026-09-28）

- 正式8015运行新项目，调用同级cobot-control和rl-platform，新数据根/home/agilex/jiaan/data；最后冷启动实例PID222607仅作证据，预览8018已停止。
- 主实现为cobot_console、capture_core、segmented_capture。硬件89个Git重复文件和现场78个重复文件已移除；脚本轻量转发control，位姿仅保留control一份。
- 共享加载/释放固定5k和最新在线模型通过；加载后disarmed/暂停，未启动Session。数据历史、episode171视频与首尾图可读。目录可在加载前选择，四个浏览器已知偏好键按注册前缀迁移。
- RL收尾503曾由operator_nodes字段被请求schema拒绝导致，已修复并验证原生合同；不自动重复成功/失败操作。
- 当前代码6c2c5fb已push，207运行文件同步一致；全后端572通过/15跳过，指定RL根后4项原生合同通过。前端目录和采集profile回归通过。
- ops已归并并删除三机本地目录。旧cobot-platform在完整归档、隔离旧路径冷启动和相机启停验证后删除。旧task3的850日志转入runtime/console-jobs，859原件文件异机留档，旧日志目录删除。
- 两个π0.5入口仍使用登记的task3/task5共享部署资产，另批归vla-platform；不能删除整个cobot_magic。旧RLT已全量归档并完成无旧路径冷加载，原目录及其旧别名已删除。

## 终端与恢复

完整启动、普通/模型采集、Session、评测、归位和退出见docs/COMMAND_LINE.md。HTTP、PID、显存、磁盘I/O和UI重启见docs/WEB_RECOVERY.md。统一scripts/console.py复用网页API；recovery子命令不依赖8015。网页重启不修复磁盘或算法进程故障；不以HTTP报错判断结果已保存。

## 此前阶段的接续与协作

RLT历史归档、最后冷加载及清理记录已完成；37页面资源、历史视频/图片与6个模型路径可用。本会话无动作/真实Episode；后续网页启动的臂/相机保持运行，模型已释放。现场仍需短轮次HIL和结果提交验收。未做浏览器目视动画验收。网页问题归本项目；控制/ROS归cobot-control，算法/Replay归rl-platform，其他模型/RTC归vla-platform，采集库后续归cobot-dagger；不再增加独立ops维护层。

来源：cobot_rlt迁移会话，2026-09-28；对应项目迁移记录、现场测试与Git核验。历史阶段细节以实际项目MIGRATION为准；本会话只维护guide摘要，不提交或推送guide Git。

2026-09-28补充：用户确认数据/checkpoint按用途单机单份保存；原始采集与当前部署归Cobot，训练中间/历史模型归A6000。存放盘点及路径/占用见实际cobot-web/docs/STORAGE.md，各领域实际入口已注明相关资产。当前仍有重复副本待收尾，场景目录尚未改名；本次未删除数据或权重。


## 2026-09-28 存储方案更新

Cobot 数据与模型统一在 /media/agilex/Getea1/jiaan/data/ 和 /media/agilex/Getea1/jiaan/model/。数据按场景分、模型按项目/模型分；本轮不新增 A6000 权重备份。代码、安装环境、运行日志与 PID 留在 /home/agilex/jiaan/project/<项目>/。完整路径与批次状态见相邻 cobot-web/docs/STORAGE.md。
当前批次正在复制/验证及切换。以上旧 /home/agilex/jiaan/data、项目内 models 路径属于迁移前状态；最终完成结论以所属项目 docs/MIGRATION.md 最新批次为准。Guide 本轮只更新记录，由其负责 agent 提交。

## 2026-09-28 Getea1 迁移当前状态

主体数据/权重已迁移到 /media/agilex/Getea1/jiaan/{data,model}，新路径网页历史及 RLT 加载验收后清理了主体旧副本。20:00 Getea1 USB 掉线，FluxVLA 环境/暂存副本的验收和清理未完成；网页已正常停止，迁移进程已退出。恢复识别后先核对文件系统和资产校验，再续迁移，不要直接开始在线训练。详细证据见实际 cobot-web/docs/STORAGE.md 和所属项目 docs/MIGRATION.md。来源：cobot_rlt 迁移会话；未新增 A6000 数据/权重备份，guide Git 不由本会话提交。

## 2026-09-28 20:56：Getea1 存储迁移完成

本批已完成复制、哈希与运行验收、切换和对应旧文件清理。Getea1/jiaan 只保留 data、model；旧系统盘数据/模型目录移除。数据按场景/用途/方法归类，位姿与动作回放归 data/motion；模型按项目/模型/场景/版本归类。代码/环境/日志/PID 留在 /home/agilex/jiaan/project/<项目>。

USB 掉线重连后已完成已迁移资产的全量收据复核；尚不能据此认定硬件链路根因已消除。RLT 新路径暂停加载、在线状态恢复与历史媒体通过；FluxVLA 固定版本离线 baseline/prefix-RTC 通过；π0.5 两入口只做 dry-run。本批未启动真实 Episode 或机器人动作。

完整路径、占用、各项验证边界及回执见实际 cobot-web/docs/STORAGE.md。证据位于 rl-platform/outputs/migrations/20260928-getea-storage/cobot/（Cobot 去掉末尾 cobot/）。同批源码与项目记录已按各自仓库发布；guide Git 保持由其他会话管理。

## 2026-09-28：按钮与终端对照补充

来源：cobot_rlt 会话用户要求。实际项目 docs/COMMAND_LINE.md 补充“网页按钮 → CLI → 真正实现”、后台进程与前台终端的区别。网页命令区默认改成可直接复制的 cd + 相对脚本，并以注释说明实现；CAN 不再展示手工传递密码的内部协议，原始入口／进程／PID 仍可单独查看。web/control 职责下沉仍延期，本批不操作硬件。验证、发布和现场结果以实际项目 docs/MIGRATION.md 本批记录为准；guide Git 仍交框架维护对话。

本批源码 0519849 已发布并同步正式 8015；后端 45 项、前端 35 项通过，212 个运行文件 SHA 一致。模型 offline／采集 idle 时仅重启网页，实际输出 API 已显示 control 的直接终端命令；无硬件启动、归位或模型加载。完整现场回执见项目记录。

## 2026-09-28：本机启动路径与模型扩展

用户确认记住选择、手动启动／加载。web 增加本机启动路径／模型登记面板、服务器路径浏览、默认模型、磁盘权重发现及适配状态；相同契约的 RLT／π0.5 可登记另一权重，新架构仍交 vla-platform／rl-platform 适配。硬件路径可选 .sh／ROS 1 .launch，但话题／服务契约仍属当前 Cobot。已识别历史 RLT 20k actor 并补为冻结对比选项，未改当前默认模型或权重。

操作、实际配置路径及本批验证见所属项目 docs/COMMAND_LINE.md、docs/MIGRATION.md。web/control 大范围职责下沉仍延期；本批只做 web 可配置入口与文件清单，不操作现场硬件。guide Git 仍由维护对话提交。

本批源码 9a12d0a 已发布并同步正式 8015，216 个运行文件 SHA 一致；后端 111 passed／1 skipped，前端 36 passed。实际列出 25 项资产、7 个已登记加载入口，其余注明适配或本机权重缺失；仅重启空闲网页，未加载模型或启动硬件。配置／目录浏览和模型状态通过只读验收，默认选择未改。

## 2026-09-28：历史模型部署入口复用

用户要求迁入以前的 .sh 部署成果。vla-platform 现登记 12 个历史版本入口；FluxVLA π0.5、G05 两版本、XR1 原版接入原有暂停服务，其他直接运动脚本保留终端入口；DM0.5/XR1 DAgger 本机缺权重。web 列表补模型/场景/步骤/状态，区分终端可用、缺文件、基础依赖；RLT learner 与 actor 不混为同一步数。

代码、测试与实际部署以所属项目 docs/MIGRATION.md 为准。旧已安装 runtime 明确登记为依赖，尚未全量迁移；本轮无机器人运动或新模型成功率测试，不删除待现场验收的旧入口。Guide Git 仍由维护对话提交。

现场发布验收：web 82ced64、vla-platform fd7ee52 已 push 并同步，分别 217 / 280 个运行文件 SHA 一致。模型 offline、采集 idle 时只重启正式 8015，硬件节点未操作。实际目录为 26 项、11 个网页加载入口、6 个保留终端入口、2 个本机缺权重条目，以及历史 RLT/基础依赖；默认 plug_v3-online-latest 未改变。只读回执：cobot-web/outputs/deployments/20260928-legacy-model-entries.json；Cobot 为 cobot-web/runtime/migrations/20260928-legacy-model-entries.json。此数目表示入口与文件预检，新增 4 个网页入口尚未逐个加载 GPU 或验收现场动作。


## 2026-09-29：默认测试目录与最近选择

用户要求刷新默认使用测试目录。已建立 Getea1/jiaan/data/datasets/test（普通／模型辅助／RLT 采集）和 evaluations/test（部署评测），增加最近目录下拉选择；刷新时活动轮次保留实际目录，正常轮询不覆盖手动选择。正式场景数据、权重及 Replay 未改。test 是目录约定，不是禁止在线学习的开关。

cobot-web 源码 b785ed9 已 push 并同步正式 8015，217 个运行文件 SHA 一致；后端 50 passed/1 skipped、前端 39 passed，现场目录与历史保留接口通过，仅重启空闲网页，相机进程不变。没有真实采集、运动或在线更新。完整证据及用户下一次全流程现场验收安排见项目 docs/MIGRATION.md 最新段。来源：cobot_rlt 会话，2026-09-29；guide Git 不由本会话提交。

## 2026-09-29：硬件规则共用已切换

来源：cobot_rlt 跨项目整理。control 7329949、web 43569ff 已 push，Cobot 分别 132/218 文件 SHA 一致。硬件探测与进程管理归 control/src/cobot_control；CLI scripts/control.py 使用 control/runtime/devices，与网页相同。67 项兼容测试、3 项真实无硬件进程组测试通过。空闲时只重启网页；相机 PID524014 保持，网页与 CLI 一致。详情见实际项目 docs/MIGRATION.md；control 新增 docs/DEPLOYMENT.md。五项目环境重建、统一模型接入及网页后续修复仍进行中。Guide Git 未提交。
