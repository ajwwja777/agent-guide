# Cobot Ops：历史与兼容入口

2026-09-27 用户取消独立 ops 维护项目，避免增加对话与交接成本。网页使用、终端流程、HTTP 排障、日志／PID 和恢复工具已归 [cobot-web](../cobot-web/README.md)。硬件、数据、算法直接在各自领域项目处理。

- 当前主文档：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/COMMAND_LINE.md`、`docs/WEB_RECOVERY.md`。
- Cobot 实现：`/home/agilex/jiaan/project/cobot-web/scripts/console.py` 和 `scripts/console_recovery.py`。
- 旧项目：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops`，仓库历史与迁移记录保留；旧脚本只转发。
- 现场旧目录 `/home/agilex/jiaan/project/cobot-ops/runtime` 与 `tools/uv` 仍被使用，不直接删除／搬动，不存在需单独启动的 ops 服务。
- 已验收的恢复证据仍在 `runtime/recovery/20260927-getea-offline`；旧 `/home/agilex/jiaan-recovery` 已清理。

不再新增独立运维流程或重复实现。具体迁移和验证写在 cobot-web，旧 ops 的 `docs/MIGRATION.md` 保留历史链路。来源：用户本次项目精简要求与实际目录／进程检查。
