# 统一 RL 实验平台

## 当前交接状态（2026-09-29）

固定RLT算法与参数保留；共享采集/评测边界和目录状态归 integrations/cobot_runtime，不再反向import web Python。录制HTTP仍由web同一个recorder提供，领域库归dagger。现场preflight为Learner5000/Actor2500/warmup锚点2567；在线契约78项、恢复Stage1契约35项通过。两冻结环境在A6000独立恢复导入通过。EXPO-FT保留独立仓库/同步训练，登记为待适配。没有启动真实Episode或更新生产Replay。

已push并核验 main：c6b640ead7d1c869dacce65f224f7d49cd18c553；Cobot副本 /home/agilex/jiaan/project/rl-platform 已逐文件SHA复核。A6000主项目 /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform，先读README结构和docs/DEPLOYMENT.md，详细批次见docs/MIGRATION.md。

数据/模型实体保持 /media/agilex/Getea1/jiaan/{data,model}；本批未搬迁或新增其备份。完整跨项目交付：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/HANDOFF_20260929.md。来源为本次实际源码、Git核验及现场只读检查；guide Git不由本会话提交。

框架复核（2026-09-29）：已只读核对 A6000 项目 HEAD 与 origin/main 一致，并对照实际项目 docs/MIGRATION.md 和 [跨项目交付记录](../../../projects/cobot-web/docs/HANDOFF_20260929.md)。上述测试与现场状态来自项目验收记录，本次未连接 Cobot 或重跑测试；实时 PID、模型与采集状态需现场重新查询。

以下保留此前阶段记录；旧路径、PID与“尚未迁移”描述应按上述最新状态及所属项目迁移记录理解。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform`；先读AGENTS.md与README.md。
- Cobot：`/home/agilex/jiaan/project/rl-platform`。
- 仓库：[ajwwja777/rl-platform](https://github.com/ajwwja777/rl-platform)，独立仓库，main分支。
- 详细记录：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/MIGRATION.md`。

目标：按方法组织采样、Replay、学习、模型发布与评测；当前接入RLT，EXPO-FT沿已有独立实现推进。迁移保持原算法、5k warmup、数据比例和动作语义。

## 历史阶段状态（2026-09-28）

- 当前运行代码、模型、Replay、环境和数据均用新根；正式8015共享入口已加载固定5k及最新在线模型到ready/disarmed，再正常释放。
- 基线learner5000/actor2500/Replay2567；无新数据不更新。A6000与Cobot独立副本测试均通过，一条模拟transition驱动5次更新，重启不重复更新；正式权重和Replay不变。
- Stage1现场加载约44秒，首次固定输入编译16.8秒，后续约76ms。31文件/15.43GB跨机SHA一致；不是新真机成功率。
- 11,123数据文件/158.04GB和2内部链接验收后，旧data下rlt/evaluations/cobot-platform/record/test已删除。新数据在/home/agilex/jiaan/data。
- A6000旧proj-20260904-cobot-realworld-rl已完整归档并删除；479条目一致。历史warmup对比1,731文件已归入outputs/rlt/plug_v3_yyshadow/history。
- Cobot旧RLT历史39,001条目/122.21GB在A6000全量SHA通过，模型归models/history、数据归data/history；旧路径隔离冷加载/释放通过后，旧RLT及其别名已删除。7.49GB现场环境备份已在A6000完成SHA校验并保留，现场暂存tar已清理。
- 当前源码918a2bf已push并同步506文件；自有独立upstream ajwwja777/rlt-openpi固定8cef77e，不fork、不向上游提PR。

## 此前阶段的接续

本批迁移/归档/清理已完成。最终模型offline、无活动Session、无GPU计算进程，系统盘约77.6GiB可用；后续网页新启动的臂/相机任务保留，5臂反馈与3相机可用。本会话没有归位或真实Episode。现场需短轮次验证HIL、暂停、终止结果和复位，再连续在线采集。完整回执在outputs/migrations/20260928-retirement/cobot/，汇总在outputs/migrations/20260928-cutover/final-summary.json。

在线入口：采集页选择/home/agilex/jiaan/data/rlt/plug_v3_yyshadow/online和plug_v3-online-latest；加载完成后才开始Session。固定warmup/Reference是对照，评测不写Replay。完整终端与恢复命令见docs/RUNBOOK.md以及cobot-web/docs/COMMAND_LINE.md、WEB_RECOVERY.md。

## 协作

本项目负责Replay、奖励、learner与在线状态；硬件由cobot-control负责，网页/任务/API由cobot-web负责。录制库暂在web，后续单独交接cobot-dagger。历史58次/22次成功是既有37.9%基线，不能与新路径加载测试或单独Reference目录的成绩混用。

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
