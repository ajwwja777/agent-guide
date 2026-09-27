# Cobot 使用、部署与运维

目标：统一使用手册、部署维护、健康检查、服务启停、日志与 PID、备份恢复及故障分流，让命令行和网页使用同一套运行入口。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\cobot-ops\AGENTS.md`。
- 仓库：[ajwwja777/cobot-ops](https://github.com/ajwwja777/cobot-ops)，独立仓库，分支 `main`。
- Cobot：`/home/agilex/jiaan/project/cobot-ops` 已建立，恢复证据在 `runtime/recovery/20260927-getea-offline/`；网页已在 cobot-web 新目录运行，并使用本项目 runtime；终端恢复脚本和使用手册已部署。模型／数据／历史硬件依赖仍待逐批迁移。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `22651c7ee958ae22ae81b0c1f18a226c5620ac5b`；补充发布记录后提交 `79498c2a7f11fceac90718e38629eec03bb3590e`，均已核验远端 main 与当时本地一致。笔记本入口已创建。这是初始化当时状态；后续切换与恢复工具验证见下文和实际项目记录。

## 下一步与协作

按现场故障继续维护手册和任务身份核验，逐批迁移硬件／算法依赖；未观察到可靠归属的残留进程交给对应专家，不泛匹配终止。

每次交接至少带症状、机器／版本、命令与关键日志、复现条件、已检查项；专家修复后由运维验证部署并更新手册。跨对话通过项目记录交接，不能假设聊天自动共享记忆。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。

## 恢复证据批次已验收

2026-09-27 已建立六个 Cobot 项目目录及数据目录；旧 `/home/agilex/jiaan-recovery` 的 17 个文件已迁入本项目 runtime/recovery，SHA-256、权限与时间校验通过，A6000 备份也已逐项校验，原目录已清理。7 个 JSON、PNG 文件头与保存脚本语法检查通过；未执行脚本或重启服务。完整清单、备份与回执见实际项目 `docs/MIGRATION.md`。

用户指定跨项目迁移由当前已有 cobot_rlt 对话继续统筹，按范围验收后切换和清理；专家项目按需交接分析与维护。


## 网页自助恢复入口已部署

2026-09-27，用户要求演示现场不依赖助手排查 HTTP／PID／任务残留。实际项目新增：

- 手册：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops/docs/WEB_RECOVERY.md`。
- Cobot 现场文档：`/home/agilex/jiaan/project/cobot-ops/docs/WEB_RECOVERY.md`；同目录项目的 `scripts/console_recovery.py` 提供 status、snapshot、logs、pause、interrupt。
- 刷新和 UI 重启不会完整停止模型；超时／503 后先检查是否部分完成。停止默认只预览，实际执行核验 PID、启动时间和 ROS 子进程树；web 仅发单 PID 信号。
- 代码 `da1f9a9cbbb61fae72569e51b8df0a45778ca2ea`，验证记录提交 `5f6a404fa5e7a9fd5cb3797b63e15ed89d61e337`，已 push 并核对远端。13 个隔离测试通过；现场状态和 web／arms／cameras 预览通过，识别 arms 7、cameras 4、roscore 3 个进程。
- 本批没有停止现场服务或执行运动；模型实机停止恢复尚未演练。SHA-256、证据路径及限制见实际项目迁移记录。
- 网页现于新 cobot-web 目录运行；算法、模型、数据和部分硬件仍有旧路径依赖，不把本批完成等同于全量迁移。

来源：实际目录、进程与只读接口检查、cobot-ops 测试及同步回执；跨项目统筹仍由已有 cobot_rlt 对话继续。
