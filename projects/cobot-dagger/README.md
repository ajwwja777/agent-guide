# Cobot 采集、HIL 与 DAgger

## 2026-09-30：项目对话入口与并行协作交接

用户指定 cobot-dagger 对话负责本领域，允许多个专题及 fork 并行。笔记本 D:\Code\jiaan_workspace\cobot-dagger\AGENTS.md 指向本项目；职责、当前问题、worktree/任务范围登记与现场单一负责人约定见 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-dagger/AGENTS.md。对话不共享实时上下文，接管重查 Git 和现场，不沿用历史 PID/版本。
采集领域已从 web 迁入；web 只留 HTTP 与兼容入口。完整未标注历史不阻塞新轮次；incomplete/损坏文件仍需处理。模型退出后 writer 应仍能诊断/收尾。
来源：cobot_rlt 本次用户指示及实际代码/记录核对；仅追加项目事实，guide Git 不提交/推送。


## 当前交接状态（2026-09-29）

35个采集、HIL、mask与数据领域模块已从web归入 src/capture_core、src/segmented_capture；web保留API与兼容导入。独立uv环境75项测试通过，现场调用新库；清理SHA匹配旧文件后111条RLT历史和JPEG仍可读。数据格式和控制语义未改，真实HIL时序待现场。

已push并核验 main：910ddc0a3fcea8a774744d539cd3ead0db16ca92；Cobot副本 /home/agilex/jiaan/project/cobot-dagger 已逐文件SHA复核。A6000主项目 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-dagger，先读README结构和docs/DEPLOYMENT.md，详细批次见docs/MIGRATION.md。

数据/模型实体保持 /media/agilex/Getea1/jiaan/{data,model}；本批未搬迁或新增其备份。完整跨项目交付：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/HANDOFF_20260929.md。来源为本次实际源码、Git核验及现场只读检查；guide Git不由本会话提交。

框架复核（2026-09-29）：已只读核对 A6000 项目 HEAD 与 origin/main 一致，并对照实际项目 docs/MIGRATION.md 和 [跨项目交付记录](../../../projects/cobot-web/docs/HANDOFF_20260929.md)。上述测试与现场状态来自项目验收记录，本次未连接 Cobot 或重跑测试；实时 PID、模型与采集状态需现场重新查询。

以下保留此前阶段记录；旧路径、PID与“尚未迁移”描述应按上述最新状态及所属项目迁移记录理解。

目标：统一人工与模型辅助采集、HIL 事件、数据格式、训练 mask、质量校验和 DAgger 迭代流程，训练通过 vla-platform 接入。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-dagger`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-dagger/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\cobot-dagger\AGENTS.md`。
- 仓库：[ajwwja777/cobot-dagger](https://github.com/ajwwja777/cobot-dagger)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/cobot-dagger`，2026-09-29 已同步采集领域库并切换调用；真实 HIL 时序待现场验收。

## 初始化记录（2026-09-27）

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `16a9f37c9381596244bc4f4a5db1677d31f851a8`；补充发布记录后提交 `f3b0b41e245e3a366351ae22515785dfafbca48e`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 初始化时的计划与协作

先迁移一份数据格式说明、样例校验与转换入口，以现有一条成功保存的 episode 做离线对照，不改变现场录制服务。

缺帧、节点、标签和 mask 由本项目负责；物理示教状态交 cobot-control；模型训练执行和归一化交 vla-platform。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。

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


## 2026-09-29：RLT录制保留模型恢复

来源：cobot_rlt用户要求，不释放已加载模型。先用原Session stop清除无未决Episode的启动故障，保留PID1436537；web新增录制预检/恢复页面与同API CLI、具体503原因，fault可结束Session。dagger修复实时预检clock先取值后等待cache锁的竞态；未修改RL算法/HIL/mask或数据格式。旧503无细节，不能将全部历史错误归因该竞态。

dagger dffc3f1 / web 8dd6983已push并同步，45/198文件SHA一致；254项Python通过、1项既有跳过，45项前端通过。模型保持暂停时连续3次12帧真实录制/放弃清理通过，无新增训练数据；最终模型ready、recorder idle、Session stopped，手动开始下一Session。Learner5090/Actor2545及模型、硬件PID保留。本轮未真实推理或运动，完整HIL仍需现场使用验收。

具体代码/终端步骤/现场回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/WEB_RECOVERY.md、docs/MIGRATION.md、outputs/rlt-recorder-recovery-20260929/；采集领域细节见cobot-dagger/docs/MIGRATION.md。Guide只更新事实，不提交Git。

## 2026-09-29：历史未标注示范目录的 RLT 开始失败

现场明确错误 Task5 latest episode labels are incomplete：demonstrations/legacy_test 有4条已完成未标注的人工示范，最后index16；旧规则阻塞且RLT的同身份orphan处理不能处理其他模型。dagger b4762c8 / web 96c74a9 已push并同步45/198文件SHA；统一flat目录允许未标注历史继续保留，legacy门禁不改，incomplete/损坏仍拒绝。恢复/检查按钮现核对同一目录完整性、显示路径及处理建议。93项Python与45项Node通过；Cobot新进程只读对照旧label_blocked=true、新false、nextindex17，未修改数据/标签。

用户已切换online目录继续真实采集；本轮未由agent请求推理、暂停或停止。网页后端重载必须等待用户当前轮次结束，不能将源码已同步当成正式API已生效。模型supervisor2139119/Stage12139241保留；最终切换结果另记。详细记录与故障操作在所属项目docs/MIGRATION.md和web/docs/WEB_RECOVERY.md。Guide Git不提交。


## 2026-09-29：正式后端切换已完成

用户反馈仍无published后，现场确认waiting_scene/policy_paused、无活动writer/操作，持模型操作锁仅重载8015。模型supervisor2139119、Stage12139241、机械臂1318293、相机1317979身份与Session UUID/generation119保持。正式API确认Learner6915/internal3457、published6500/3250、last inference3250；录制标签修复一并生效。未开始推理或释放模型。回执：Cobot /home/agilex/jiaan/project/cobot-web/runtime/verification/rlt-publication-20260929/release.json。guide Git未提交。

2026-09-30 交接发布核验：cobot-dagger b4819d832bdaf4f376139daa78e0985fe0ebaf1f = origin/main，A6000工作树干净；本批选中文档/源码已逐文件SHA同步Cobot。详细回执 projects/cobot-web/outputs/pause-recovery-20260930/handoff-release.json；guide Git未提交。

2026-09-30：运行选项、录制暂存与历史补标签已交付。模型详情区分发布频率与逻辑／Replay 步频，支持 Hz／RTC／滤波选择；暂存结束当前 writer，保留文件与模型任务，完整未标注记录可补标签，不隐式提交 Replay。离线网页后端 725 passed／6 skipped、前端 62、采集 78、RL 79 通过；连续真机 50 Hz 和成功率仍未验收。

最终发布回执：web e75d3cbb、dagger bb85a8a6、RL d878bded；网页 PID 866075、模型 offline、录制 idle、ROS readiness ok，采样进程身份保持，未启动模型／动作或改生产数据。此前两段已被写成问号，现依据实际项目 docs/MIGRATION.md 与 cobot-web/outputs/recording-defer-rate-20260930/final-release.json 核对后重写；详细过程仍归所属项目。

## 2026-10-01：方法／步数、历史结果与 NVMe 路径现场事实

来源：cobot-web 当前任务。原版／MC30 方法与纯数字步数独立，固定 5000 保留，新增在线分支读取真实已发布步数；所选 50 Hz 的详情与实际生效设置分开。历史标签接口与目录迁移一致，普通采集节点历史保留记录结果，成功／失败／未知可修改并同步同目录显示。Stage1 清单和实际 CPU preflight 恢复 NVMe /home/agilex/jiaan/data/rlt/plug_insertion/reference_4999；在线资产按原登记引用，未搬数据／权重。

cobot-dagger 发布 127b3f349cbedc61ef61792800e62049f9e9e236；三项目源码／记录 SHA 已核验，正式 8015 只重载网页 PID 970937。模型 offline、recorder idle、无活动 writer；9 个采样硬件／模型身份及固定 5000／历史标签 SHA 不变。离线前端 69、完整 web 734（6 skipped）、末次相关 60（1 skipped）、采集 78、RL 24 通过。8 条实际历史标签 GET 与目录 DOM 通过；未启动 GPU／训练／动作，真实在线分支与 50 Hz 连续运动、浏览器视觉仍待现场。详见实际项目 docs/MIGRATION.md 与 web outputs/catalog-results-20261001/final-release.json；guide Git 未提交或推送。
