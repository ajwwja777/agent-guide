# Cobot 操作网页

## 当前摘要（2026-10-09 复核）

独立相机预览、π0.5 导入/代际取消及 kill 后释放修复已交付。DAgger 与原版两套 π0.5 原始迁移 SHA 均恢复到用户批准的 Cobot NVMe 路径，实际 20 Hz 和 50 Hz＋RTC＋滤波预热均 ready/PAUSED，无机器人指令发布器的影子运行通过。Getea 底层读取问题未定位或修复，连续运动与长期 50 Hz 尚未验收。以下保留各阶段故障及恢复记录，最终结论以最新节为准。来源：所属项目 docs/MIGRATION.md 与本摘要 10 月 6–8 日记录；本轮未重新查询实时 PID/状态。

## 2026-09-30：项目对话入口与并行协作交接

用户指定 cobot-web 对话负责本领域，允许多个专题及 fork 并行。笔记本 D:\Code\jiaan_workspace\cobot-web\AGENTS.md 指向本项目；职责、当前问题、worktree/任务范围登记与现场单一负责人约定见 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/AGENTS.md。对话不共享实时上下文，接管重查 Git 和现场，不沿用历史 PID/版本。
正式 8015 已在新项目。2026-09-30 增加根因、Stage1 保留状态、针对性收尾恢复与常驻 RLT 通用重启；实际活动录制收尾并保留模型重建通过。
来源：cobot_rlt 本次用户指示及实际代码/记录核对；仅追加项目事实，guide Git 不提交/推送。


2026-09-30 实际稳定性修复验收：rl3902fa8/web6b84116 已push、13文件SHA同步。
暂停/HIL旧时钟误报已修复，录制HTTP移出RTC推理预算；web新增收尾未标注录制和通用保留模型重启。
现场活动writer的48帧测试文件提交、writer占用释放、runtime重建ready/disarmed，Stage1 PID233064/start_ticks20025113保留，7个采样硬件身份不变。
Replay3917/Learner7000/Actor3500未变，未执行推理/运动；50Hz连续真机与插入成功率仍待验收。
回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/pause-recovery-20260930/；
Cobot对应 /home/agilex/jiaan/project/cobot-web/runtime/verification/pause-recovery-20260930/。
具体恢复按钮、CLI和限制见web docs/WEB_RECOVERY.md与RL docs/RUNBOOK.md；guide Git不提交。

## 2026-09-29 示教显示防闪烁（最新）

用户复测确认进入示教不再闪黄，移动偶发黄色、退出瞬间仍闪黄。control ace3b1f / web fdd6cdc已push并同步Cobot146/197文件：共用只读显示改为普通偏差持续2秒≥0.25rad才告警、<0.15rad稳定0.5秒恢复，软信号确认1秒；原1秒接管保留。已确认示教退出最多1.5秒绿色“正在退出示教”，允许按钮/CAN残留/逐步失能先后到达，超时仍告警且不反复延长。前臂本体示教、明确硬件/CAN/ROS/控制通路故障及≥0.50rad偏差仍立即提示；不改真实控制、动作、HIL或安全参数。

100项设备/任务/健康回归通过，覆盖移动滞后、退出消息顺序/卡住/重入/双侧独立与故障优先。空闲时只重载8015，臂PID1318293、相机PID1317979保持；正式API健康、五路TX队列空。未发机器人动作；本版实际连续移动/退出颜色仍待用户观察。规则与发布事实见实际项目docs/MIGRATION.md、control/docs/DEPLOYMENT.md；完整回执位于control/outputs/diagnostics/teach-release-20260929/release.json（A6000），现场对应control/runtime/diagnostics/teach-release-20260929/release.json。guide Git不提交。

## 2026-09-29 中臂首次归位与示教排查（本轮最新）

来源：cobot_rlt 会话实际源码、被动CAN/ROS诊断及用户授权的小幅动作。control 5247de8 / web 412f31a 已push并同步146/197文件；硬件语义保留。修正mode=2/teach=1示教解析、latched协调器状态和配对故障显示；新增只读TX队列停滞诊断。中臂home增加无故障且已使能standby的原位ROS初始化，不嵌入Recover，冷上电动作仍待验证。

左右CAN曾在持续接收时TX停滞，队列各10帧并有gs_usb echo告警；用户确认现场条件后已受控恢复，队列清空。通过原home_front服务验证两前臂各0.01rad往返，返回误差<0.0005rad；未启动模型，正式位姿/控制参数未改。首次人工示教复测暴露latched状态误判，已修正并重载，第二次复测仍待用户操作；修正后3分钟只读观察均为空闲健康，网页与CLI五路TX状态一致，没有把这段空闲观察算作示教验收。完整过程与证据见所属项目docs/MIGRATION.md、control/outputs/diagnostics/teach-and-mid-20260929。guide Git不由本会话提交。

## 页面布局更新（2026-09-29）

训练、部署与操作台/采集的内容区顶部和左侧统一；切换类别回到中央内容区左上角。采集与部署现共用四框，默认左上保存位置、右上模型、左下数据/评估、右下控制；设置 → 编辑布局可拖动四框，两页各自保存排列，刷新恢复。模型详情在卡片内滚动，窄内容区按单列显示。

A6000 主项目 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web；a370e59d450f3964ad4500002fff9c4a9930b7ce 已提交 push 并核验 origin/main，Cobot /home/agilex/jiaan/project/cobot-web 同步 197 个运行文件 SHA 一致，6 个实际 HTTP 静态资源核验一致。前端回归 42 项通过；Chromium 验证四页顶部左侧、两页四框几何位置、真实拖放与刷新恢复，截图已查看。仅静态更新，未重启网页/硬件或加载模型；现场部署状态只读检查为 offline。详见项目 docs/MIGRATION.md 最新两节和 docs/COMMAND_LINE.md“采集与部署面板排列”。guide Git 不提交/推送。


## 场景/模型选择更新（2026-09-29）

采集与部署已共用左右场景/模型选择框，双向配对、空闲时同步选择，完整权重路径在下方；不可用选项统一置灰禁用。按实际登记task生成场景，新增同类模型不改网页。前端42项、相关后端28项通过，实际26条目录/11个可加载条目两API一致。59080f823b32f568147ddbc7cbb9904a4764fa30 已push，Cobot 196个运行文件SHA及5个HTTP资源核验一致；只同步静态资源，不重启网页或硬件，不加载模型。详情 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/MIGRATION.md 最新节，命令/使用说明 docs/COMMAND_LINE.md。guide Git不提交。

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


## 2026-09-29：模型选择与选臂位姿本批交付

来源：cobot_rlt 对话本次用户要求及现场只读验收。采集/部署统一三段 Scene/Model/Steps 和四卡模板；英文模型选项、路径去底色、详情展开无内部滚动。位姿可选已有名/编辑新名并勾选记录臂，底部整行Recover、单夹爪操作。

control 15c1917 / web fd8d182 已push、核对远端并同步Cobot，146/197文件SHA一致；404项Python与44项Node回归通过，浏览器1800/1200/760宽度布局检查通过。仅重载空闲8015；机械臂、相机、在线RLT进程PID与Session UUID保留，正式位姿数据不变，无动作验证。发布前已有RLT Session fault / recorder_not_ready，重载后仍保留，不能称为全流程已正常。详见实际项目docs/MIGRATION.md本批记录及cobot-web/outputs/model-pose-layout-20260929/release.json。Guide Git未提交/推送。


## 2026-09-29：RLT录制保留模型恢复

来源：cobot_rlt用户要求，不释放已加载模型。先用原Session stop清除无未决Episode的启动故障，保留PID1436537；web新增录制预检/恢复页面与同API CLI、具体503原因，fault可结束Session。dagger修复实时预检clock先取值后等待cache锁的竞态；未修改RL算法/HIL/mask或数据格式。旧503无细节，不能将全部历史错误归因该竞态。

dagger dffc3f1 / web 8dd6983已push并同步，45/198文件SHA一致；254项Python通过、1项既有跳过，45项前端通过。模型保持暂停时连续3次12帧真实录制/放弃清理通过，无新增训练数据；最终模型ready、recorder idle、Session stopped，手动开始下一Session。Learner5090/Actor2545及模型、硬件PID保留。本轮未真实推理或运动，完整HIL仍需现场使用验收。

具体代码/终端步骤/现场回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/WEB_RECOVERY.md、docs/MIGRATION.md、outputs/rlt-recorder-recovery-20260929/；采集领域细节见cobot-dagger/docs/MIGRATION.md。Guide只更新事实，不提交Git。

## 2026-09-29：π0.5 Recover 暂停锁修复

用户先正常部署in_the_pot DAgger、Recover双后臂后点击开始反复暂停。实测后臂正常失能、协调器policy且无fault；原因是web旧π0.5 wrapper将Recover保护暂停误当HIL。新分类只将实际协调器识别为HIL，Recover须由操作者开始/继续；旧版桥接检查实际paused回复，增加保持权重的暂停锁协调，并接入显式开始/继续，真实示教/故障仍拒绝恢复。

web 3d05c63及后续 4be8602已push并同步Cobot198文件；63项回归通过/1跳过。现场repair-pause成功后保持手动暂停，GPU服务2019058/客户端2025877/硬件PID不变。用户随后自行开始eval-20260929T154302-897142dd，15:43只读确认running、paused=false；未由agent请求运动，未将本次状态通过当作整轮动作成功率验收。新wrapper下次正常加载生效，当前旧进程通过新bridge兼容，无需重新加载权重。

完整恢复方式、边界与回执见 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/WEB_RECOVERY.md 和 docs/MIGRATION.md；Cobot对应 /home/agilex/jiaan/project/cobot-web/docs/。guide只更新事实，不提交/推送Git。

本批最终web 9c5d3f9 已push并同步198文件，65项回归通过/1跳过；补齐Recover前HIL旧锁退休和所有π0.5开始/继续的policy/空fault检查。后续开始仅由用户显式操作触发；自动兼容路径已离线覆盖，未为测试请求真机动作。

## 2026-09-29：历史未标注示范目录的 RLT 开始失败

现场明确错误 Task5 latest episode labels are incomplete：demonstrations/legacy_test 有4条已完成未标注的人工示范，最后index16；旧规则阻塞且RLT的同身份orphan处理不能处理其他模型。dagger b4762c8 / web 96c74a9 已push并同步45/198文件SHA；统一flat目录允许未标注历史继续保留，legacy门禁不改，incomplete/损坏仍拒绝。恢复/检查按钮现核对同一目录完整性、显示路径及处理建议。93项Python与45项Node通过；Cobot新进程只读对照旧label_blocked=true、新false、nextindex17，未修改数据/标签。

用户已切换online目录继续真实采集；本轮未由agent请求推理、暂停或停止。网页后端重载必须等待用户当前轮次结束，不能将源码已同步当成正式API已生效。模型supervisor2139119/Stage12139241保留；最终切换结果另记。详细记录与故障操作在所属项目docs/MIGRATION.md和web/docs/WEB_RECOVERY.md。Guide Git不提交。

## 2026-09-29：RLT训练与发布显示纠正

web 81114d1已push并同步199文件SHA一致。原选项6915/3457来自Learner内部，而真正发布快照为6500/3250，Session最近episode14实际使用3250。现在分别展示训练、发布、实际推理版本，选项以真实发布快照为准；只读解析512字节标量头，不执行pickle或加载模型。24项Python通过/1既有跳过、46项Node通过；不改500步发布/训练逻辑。正式后端与上个录制修复一起等待用户结束连续采集后的重载窗口，不把同步当生效。详情见实际项目docs/MIGRATION.md、docs/COMMAND_LINE.md；guide Git不提交。


## 2026-09-29：正式后端切换已完成

用户反馈仍无published后，现场确认waiting_scene/policy_paused、无活动writer/操作，持模型操作锁仅重载8015。模型supervisor2139119、Stage12139241、机械臂1318293、相机1317979身份与Session UUID/generation119保持。正式API确认Learner6915/internal3457、published6500/3250、last inference3250；录制标签修复一并生效。未开始推理或释放模型。回执：Cobot /home/agilex/jiaan/project/cobot-web/runtime/verification/rlt-publication-20260929/release.json。guide Git未提交。

## 2026-09-29：RLT训练与诊断分析页面

来源：cobot_rlt用户要求新增分析板块、训练页整理对齐。web e775308已push并同步202文件，正式8015新增只读/api/analysis/rlt；训练保留进度/发布/参数/主要loss，核心分析归独立页面，历史Warmup图折叠保留。rl-platform 88b3e1c新增轻量聚合和离线Replay PCA/k-means，保留算法；该项目本批只同步3个新增分析文件，未覆盖另一对话的NVMe/probe现场改动。

4项RL测试、24项web Python、47项Node通过；1800/1200/760宽度同左/上边界、无横向溢出、0 JS异常。真实快照3917条transition，前两轴解释31.50%，属于姿态/动作覆盖，不是视觉阶段或失败因果。正式API Learner11750、published11500/Actor5750；日志旧心跳标历史快照，未冒充训练仍运行。只在模型offline/录制idle/无writer时持锁重载网页，9个硬件进程身份保持，未运动或加载模型。

说明：/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/ANALYSIS.md；网页使用与记录：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/COMMAND_LINE.md、docs/MIGRATION.md。Cobot快照在 /home/agilex/jiaan/project/rl-platform/outputs/rlt/plug_v3_yyshadow/analysis/replay_projection.json，手动运行 envs/online/bin/python scripts/analyze_replay.py 重新生成。HTTP回执归web/runtime/verification/rlt-analysis-20260929/。Guide仅追加事实，不提交/推送Git。

## 2026-09-29：诊断可视化、模型目录与操作响应交付

来源：cobot_rlt代码、测试和8015现场只读检查；web120a3175 已push并同步。
Analysis新增Replay/实际batch构成、14版本回看、12组采样实验、
梯度/输入消融与6帧三相机遮挡；明确不是Attention或独立验证成功率。
Training保留核心曲线。53项Python、50项Node回归通过；
1800/1200/760无横向溢出、对齐；正式浏览器0JS异常，英文检查通过。

明确选模型时按configs/model_directories.json或模型data_directories选择采集/评测目录，
Warmup/Online分开；之后可手动改，活动轮次不切换，轮询不覆盖。
设备操作立即显示核对/待接收，输出跟随任务，CAN堵塞/排空提供提示。
在model offline、capture/recorder idle、无writer时持模型操作锁，仅重载web；
7个匹配到的硬件进程身份保留，未运动、未重置CAN或启动模型。
API一次采样analysis约0.229秒、devices约0.0064秒，不代表所有操作耗时承诺。

复现/接入边界：实际项目docs/COMMAND_LINE.md、ARCHITECTURE.md、MIGRATION.md。
证据：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/rlt-analysis-20260929/。
训练通用选择器仍为后续扩展，未声称任意模型一键训练。Guide Git不提交/推送。

## 2026-09-30: RL action diagnostics and candidate selection

Source: cobot_rlt dialogue. Analysis now shows 21 credit/sampling comparisons and per-joint Reference/Actor/executed curves; details collapse for readability. Project registration exposes a distinct MC30 candidate, with its own live telemetry/publication paths, through the existing paused-load workflow. Original online remains selectable. Web owns no MC/RTC algorithm. Tests: 51 Node checks and 22 selected Python checks pass (one skip); read-only responsive preview has no JS errors. Full paths/use/limits in actual cobot-web/docs/COMMAND_LINE.md and rl-platform/docs/EXPERIMENTS_20260930.md. Robot success and integrated RTC remain pending. Project code pushed; guide Git not submitted.

Final release verification (2026-09-30): main/origin f145a800a52ce57ad364912e606075fedaf31e68; A6000 tree clean; selected Cobot files SHA256 match. Formal 8015 read-only verification passed; no robot motion. Guide Git not committed by this dialogue.

## 2026-09-30: RTC field timeout and retained-Stage1 recovery

Actual19:50:31 MC30 async_rtc50 EnvDriver failed because queue delay exceeded its
200 ms budget; final supervisor traceback was a consequence. Old inference
latency omitted recorder checks, so full contention cause is not established.
RL now records actual/allowed delay and inference/recorder timing; bounds and
algorithm settings unchanged. Web collection/deployment display root cause,
Stage1 retention and explicit status/output/runtime recovery controls.

Recovery verifies fully exited owned runtime and no pending writer/evaluation,
uses original launcher and refuses implicit Stage1 reload. No automatic inference,
home, label, data deletion or Replay commit. Completed orphan writer can permit
UI shutdown only after local process-group verification. Source/docs release:
rl-platform d4c798f, cobot-web4f5db63;18 Cobot hashes checked. Full backend709/6skip,
DOM56, selected RL40, additional shutdown/CLI32 passed. Formal8015 updated with
Stage1 PID233064 retained and14 hardware identities unchanged; recovery/start
were not invoked. Live restart/RTC contention acceptance still pending.

Usage: /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/WEB_RECOVERY.md
and /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/RUNBOOK.md.
Evidence: /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/rtc-runtime-recovery-20260930/;
Cobot /home/agilex/jiaan/project/cobot-web/runtime/verification/rtc-runtime-recovery-20260930/.
Source: actual code/tests/live API and cobot_rlt dialogue. Guide Git untouched.

Final record-only release 6c8aea5b412bf24d78fed6b4300eed2e076ece11 = origin/main; A6000 clean and all18 selected Cobot source/docs hashes verified. Guide Git not committed.

Operator follow-up: retained recovery launched20:33:53, Stage1 still233064; at20:34:15 async_rtc50 then failed execution_clock_late. Recovery works, but50Hz field timing is not accepted. No recovery/start requested by agent. Evidence in web outputs/runtime rtc-runtime-recovery-20260930/operator-followup.json.

2026-09-30 交接发布核验：cobot-web 3875e3811248e7de38cddfcdf6c1b97d48d7f96c = origin/main，A6000工作树干净；本批选中文档/源码已逐文件SHA同步Cobot。详细回执 projects/cobot-web/outputs/pause-recovery-20260930/handoff-release.json；guide Git未提交。

2026-09-30：运行选项、录制暂存与历史补标签已交付。模型详情区分发布频率与逻辑／Replay 步频，支持 Hz／RTC／滤波选择；暂存结束当前 writer，保留文件与模型任务，完整未标注记录可补标签，不隐式提交 Replay。离线网页后端 725 passed／6 skipped、前端 62、采集 78、RL 79 通过；连续真机 50 Hz 和成功率仍未验收。

最终发布回执：web e75d3cbb、dagger bb85a8a6、RL d878bded；网页 PID 866075、模型 offline、录制 idle、ROS readiness ok，采样进程身份保持，未启动模型／动作或改生产数据。此前两段已被写成问号，现依据实际项目 docs/MIGRATION.md 与 cobot-web/outputs/recording-defer-rate-20260930/final-release.json 核对后重写；详细过程仍归所属项目。

## 2026-10-01：精简执行选项发布事实

来源：cobot-web 本次任务。模型步数项去除 Hz，运行 Hz/RTC/滤波独立成一行；历史结果成功/失败/未知自动保存，保留原备注与训练许可，CAS 与丢响应查询确认。VLA 共用执行配置、物理时间发布/滤波及可选 chunk 执行已接入当前暂停适配器，RLT 复用配置合同。

A6000 web af56ffc / VLA a9f87e0 / RL aee49de 已提交 push。Cobot web 209 个运行文件全 SHA 校验，VLA 16/RL 2 个本次文件校验；只重载 8015，新网页 PID 927182，模型 offline、录制 idle、无 writer/active lease。9 个采样硬件/模型进程身份保持。共用模块现场导入与 4 个 VLA 文件启动计划、两项 π0.5 dry-run 通过；未新加载 GPU、未真实 Episode/Replay 改写/动作，连续真机 Hz/效果待验收。

离线前端 67，web 后端 87（另 1 skipped），RLT 21，共用 VLA 27，G05 15，XR1 26 项通过。回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/execution-compact-20261001/final-release.json；Cobot 对应 runtime/verification/execution-compact-20261001/final-release.json。guide Git 不由本对话提交或推送。

## 2026-10-01：方法／步数、历史结果与 NVMe 路径现场事实

来源：cobot-web 当前任务。原版／MC30 方法与纯数字步数独立，固定 5000 保留，新增在线分支读取真实已发布步数；所选 50 Hz 的详情与实际生效设置分开。历史标签接口与目录迁移一致，普通采集节点历史保留记录结果，成功／失败／未知可修改并同步同目录显示。Stage1 清单和实际 CPU preflight 恢复 NVMe /home/agilex/jiaan/data/rlt/plug_insertion/reference_4999；在线资产按原登记引用，未搬数据／权重。

cobot-web 发布 562f8f83317617213ecac6c5e1a5ea367c876d81；三项目源码／记录 SHA 已核验，正式 8015 只重载网页 PID 970937。模型 offline、recorder idle、无活动 writer；9 个采样硬件／模型身份及固定 5000／历史标签 SHA 不变。离线前端 69、完整 web 734（6 skipped）、末次相关 60（1 skipped）、采集 78、RL 24 通过。8 条实际历史标签 GET 与目录 DOM 通过；未启动 GPU／训练／动作，真实在线分支与 50 Hz 连续运动、浏览器视觉仍待现场。详见实际项目 docs/MIGRATION.md 与 web outputs/catalog-results-20261001/final-release.json；guide Git 未提交或推送。

## 2026-10-01：两行权重路径现场事实

来源：cobot-web 用户本次要求。采集／部署共用模型选择器在选中时立即显示权重路径与 Base model 两行；Base model 从折叠详情移至路径处。69 项前端回归、实际目录 15 项 DOM 与正式 8015 静态响应 SHA 通过；发布 bdf2e0876364d944f7ae6ce3f24651c8f882631e，网页 PID 970937 保持，无网页／模型／硬件重启或动作。真实浏览器视觉未验收。详见项目 docs/MIGRATION.md 和 outputs/selected-paths-20261001/final-release.json；guide Git 未提交／推送。

## 2026-10-01：选中即显示两行权重路径

采集与部署共用选择器立即显示所选权重与 Base model 两行路径，清空选择同步清空旧值；无 base 时仅显示实际权重。web bdf2e087 已 push，静态运行文件与正式 HTTP 资源 SHA 核对一致。69 项前端回归及现场目录 15 个可选模型的 DOM 核验通过；网页 PID 970937 与采样硬件／模型身份保持，未重启网页、加载模型或发动作，真实浏览器视觉仍待验收。来源：实际 cobot-web/docs/MIGRATION.md 最新节与 outputs/selected-paths-20261001/。

## 2026-10-01：迁移记录问号段落已修复

来源：guide 转交、cobot-web 本对话核验。实际项目 docs/MIGRATION.md 的 2026-09-30 现场验收段落在最初 Git 提交中已为字面问号；已依据当次 outputs/recording-defer-rate-20260930/ 的版本、前后状态、网页重载、缓存和最终发布回执重写，区分首次 web 98488778 与最终 e75d3cbb，并保留 50 Hz／视觉未验收边界及历史快照日期。UTF-8、无连续问号／替代字符、段落外内容不变和 Cobot 文档 SHA 校验通过；文档修复版本 95392105b09c64b8f6a4b43089f0890a67a47584 已 push 并仅同步文档，未重启网页／模型／硬件。原损坏段落及修复回执：cobot-web/outputs/migration-encoding-20261001/。guide Git 不由本对话提交／推送。


## 2026-10-06：单路掉线时独立相机预览

cobot-web `22b058c` 已提交/push：网页每路独立缓存/帧率/更新版本，一路断线、冻结或编码失败时其余继续预览，异常画面隐藏提示，恢复自动重连。评测首尾图的同步三路合同、录制/模型输入/控制不变。743 Python 通过/6既有跳过、69前端通过；隔离实际HTTP/MJPEG合成断线验证正常两路各8张不同JPEG、恢复ready；Chromium显示回归通过。

现场初次发布检查遇到活动录制，未中断；用户结束并确认后，209运行文件SHA同步，只重载网页7444→63917。相机/ROS/机械臂/保留Stage1共7进程身份不变；三路实际预览各约16FPS且版本持续推进/JPEG有效，录制idle、模型offline。原文件备份在Cobot `runtime/incidents/independent-camera-preview-20261006/before`。源码/完整事实见所属项目 `docs/MIGRATION.md`，验证/发布回执见 `scratch/cobot-web/independent-camera-preview/validation/delivery.json`。Guide Git不提交/push。

## 2026-10-08：π0.5 导入修复；DAgger 权重阻碍

来源：cobot-web 用户报告及本对话现场核验。VLA 明确包名导入修复已发布 83a49c9c059da661df34f152c617b7d54d3424a5，144 项 CPU 回归及真实环境 8 个导入组合通过。实际 DAgger 3000 的暂停加载在首次普通 baseline 预热失败；只读扫描发现 4 个参数张量共 96 个非有限值，19 个文件中 4 个 SHA 与 9 月 28 日迁移记录不同。旧路径是当前坏权重链接，历史训练机两个登记入口均超时，等待可信同版本权重；部署尚未恢复，不声称 20／50 Hz 真机通过。最终无模型运行、网页及 12 个采样硬件／模型身份保持，未运动／写 Episode／改 Replay／权重，现场拥有权释放。完整证据 cobot-web/outputs/pi05-import-20261008/，详见所属项目 docs/MIGRATION.md，本次文档版本 b6e76171d7902219a8af076e99661cd4ac82fbee；guide Git 不提交／推送。

### 2026-10-08 追加：更正 π0.5 权重初步归因

用户补充迁移后曾成功且旧训练机已不用；现场 9 月 29 日两次 DAgger ready＋PAUSED 日志支持，同样加载当前 Getea DAgger 路径。用户指定旧部署目录 step_3000 是当前权重链接。直接读取及针对 checkpoint 的缓存 advice 曾使一个文件恢复原 SHA，但其他仍异常，后续恢复又令读取 SHA 改变；CPU 非有限参数由 96 变 127，隔离串行读取 embedding 仍有 26。独立读取样本 395 字节／3 扇区有差异，多数候选未匹配原 SHA，不部署。尚不能确认持久文件损坏；不以旧训练机副本为唯一恢复路径。等待管理员底层只读诊断信息以区分文件系统／缓存／内存／读取路径。15:39 释放现场后，网页已另行加载 RLT，本对话不停止或切换它。源码修复完成，实际 DAgger 恢复仍未完成。详见所属 MIGRATION 追加核验与 cobot-web/outputs/pi05-import-20261008/，文档 8ef45d39fe41649eb206cfddc87e5a08980f4f0d；guide Git 不提交／推送。

### 2026-10-08：π0.5 原始 DAgger 权重恢复到 NVMe

底层只读读取获得全部 19 文件原始迁移 SHA，CPU 恢复 33.53 亿参数非有限值为 0，恢复后全部 SHA 稳定。两次块设备 O_DIRECT 样本仍出现差异，底层链路故障未定位或修复。用户明确批准永久 NVMe 路径 /home/agilex/jiaan/model/vla-platform/pi05/in_the_pot/dagger_2000plus3000，原 Getea 权重保留；web 主机配置登记仅此模型例外。用户批准接管做暂停加载，接管时模型 offline、无录制/GPU 任务。实际 20／50 Hz＋RTC＋滤波加载结果待追加；不以 CPU 验收代替运行验收。来源：所属 docs/MIGRATION.md、web outputs/pi05-import-20261008/；文档发布 c516622147b712c1f7d3cc1cd327d0e532a83e15，guide Git 不提交／推送。

### 2026-10-08：π0.5 DAgger 暂停部署恢复通过

来源：所属项目 MIGRATION 最终验收与 web outputs/pi05-import-20261008/。完整原始 19 文件恢复到用户批准的 NVMe 路径，CPU 参数非有限值为 0，GPU 加载后 SHA 仍全匹配。20 Hz 无 RTC／滤波及 50 Hz＋RTC＋滤波两次真实 observation＋baseline／guided RTC 预热 ready and PAUSED；最终保留 50 Hz 手动暂停，3 秒只读监测无 policy 动作消息，无运动、录制或 Replay 编辑。只重载网页生效路径；重载当时硬件 12 身份保持，加载后另有 cameras_up 使三路相机 PID 改变，本任务没有发硬件启停，最终其余 9 身份保持。Getea 底层读取链路故障尚未定位／修复；不要误称整机存储健康或运动／50 Hz 连续发布已验收。文档 f67d3f859ba799ff942ed7127428212eca242c36；guide Git 不提交／推送。

### 2026-10-08：π0.5 运动后退出修复，保持暂停待操作者复测

用户运动后退出；无发布器影子诊断确认首次 guided RTC 延迟超过 baseline 初始化预测，异步停止又与 50 Hz 发布 reset 竞争产生 NoneType。已修复代际取消竞争，Task2 异常保护性手动暂停并保留模型／原始原因；网页显示 fault。guided 预热后两次往返校准＋2 逻辑步余量，严格超时／过期动作检查保留，逻辑 20 Hz／发布 50 Hz 不变。VLA f4f1f6b／29cbbb6，web 803d797，48＋50 项测试通过／1 既有跳过，SHA 与两套 RTC manifest 同步核验。中断 eval 保留为 unknown，三个 start JPEG 字节保持。真实相机／关节／NVMe DAgger 的无机器人指令发布器影子运行 300 步／750 次／15.76 秒无错误；最终模型 3727953 保持 ready／手动暂停、无活动轮次／writer。只重载网页，12 采样硬件身份保持；没有实际运动验收，拥有权交还用户。详细事实与证据在所属 docs/MIGRATION.md 和 cobot-web/outputs/pi05-publication-race-20261008/；Getea 底层读取问题未修复。guide Git 不提交／推送。

### 2026-10-08：π0.5 终端 kill 后释放超时修复

来源：cobot-web 用户报错与现场核验。policy server 已退出但 launcher／客户端残留，旧释放被不存在的 /task2/policy/set_paused 超时阻断。web 05bc673 已 push／SHA 同步：明确 unload 的有界暂停失败保存 warning，继续仅停止身份核验的所属组，确认全部退出才 offline；PID 复用／等待期间退出／未退出拒绝等合计 85 passed／1 既有 skipped。正式 HTTP 对当前残留组真实释放，原服务仍超时但 5.38 秒后 offline／无组成员、error／active／writer 清空，warning 保留。只重载网页，未加载模型、恢复推理、归位、重启硬件或改数据／权重；现场拥有权交还用户。详细事实见所属 docs/MIGRATION.md 与 outputs/pi05-release-after-kill-20261008/。guide Git 不提交／推送。

### 2026-10-08：原版 π0.5 step2000 恢复到工控机 NVMe

来源：cobot-web 用户错误截图及原版现场核验。首次 baseline 预热返回非有限动作，尚未进入 RTC／滤波发布；Getea 原版副本 4/28 SHA 异常、两个 MLP 张量共 30 非有限值。文件／块设备只读恢复获得全部原始 SHA；末个文件两次块设备读有 136 字节／1 扇区变化，底层故障仍未定位／修复。完整原版 28 文件、33.53 亿参数 CPU 非有限值为 0，复制到 /home/agilex/jiaan/model/vla-platform/pi05/in_the_pot/baseline_2000 并登记单键 pi05_checkpoint（web cac047a），Getea 原文件保留。20 Hz 无 RTC／滤波与 50 Hz＋RTC＋滤波真实预热均暂停就绪，GPU restore 约 5 秒，GPU 加载后全部 SHA 仍匹配。无指令发布器影子运行 300 步／750 次／15.60 秒无错误；最终原版模型 3902257 手动暂停，12 采样硬件身份保持，未实际运动或写数据／Replay。现场拥有权交还用户，实际运动复测仍待操作者完成。详见所属 docs/MIGRATION.md 与 cobot-web/outputs/pi05-baseline-finite-20261008/；guide Git 不提交／推送。
