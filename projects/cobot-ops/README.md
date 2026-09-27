# Cobot 使用、部署与运维

目标：统一使用手册、部署维护、健康检查、服务启停、日志与 PID、备份恢复及故障分流，让命令行和网页使用同一套运行入口。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\cobot-ops\AGENTS.md`。
- 仓库：[ajwwja777/cobot-ops](https://github.com/ajwwja777/cobot-ops)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/cobot-ops`，本轮未部署或切换。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `22651c7ee958ae22ae81b0c1f18a226c5620ac5b`；补充发布记录后提交 `79498c2a7f11fceac90718e38629eec03bb3590e`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 下一步与协作

先整理现用命令、路径、健康检查和故障分流，迁移一项只读状态查询；核验日志来源和 PID 对应关系，不重启现有服务。

每次交接至少带症状、机器／版本、命令与关键日志、复现条件、已检查项；专家修复后由运维验证部署并更新手册。跨对话通过项目记录交接，不能假设聊天自动共享记忆。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。
