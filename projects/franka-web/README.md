# Franka Web

用 Rust 为 Franka 开发类似 cobot-web 的操作网页；具体首版功能、架构与验收方式由新项目对话和用户确认。

仓库：[ajwwja777/franka-web](https://github.com/ajwwja777/franka-web)，公开，main，初始化提交 `ddcb8b1`。

2026-10-25 已完成笔记本对话入口、A6000 主项目和 Franka 现场 clone；三机访问已核验，A6000、GitHub 与 Franka 提交一致，现场四个引导/配置文件 SHA256 一致。当前是文档基础，尚未实现应用或启动服务。

项目对话从笔记本 franka-web 的 AGENTS.md 开始，沿项目 README、AGENTS.md 和不入库的 LOCAL_HANDOFF.md 读取三机连接、认证来源、实际目录及参考接口。公开仓库不包含内部访问说明。接管后先阅读 cobot-web 和 Franka 现有接口，确认首版方案再实现。

来源：2026-10-25 用户初始化要求、用户明确授权使用既有 Franka 登录材料、三机连接/目录及 Git 核验。
