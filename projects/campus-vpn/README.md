# campus-vpn

目标：校外访问校园资源，当前重点为 Cobot 网页与 SSH。

正式记录：[项目 README](../../../projects/campus-vpn/README.md)。笔记本入口：`D:\Code\jiaan_workspace\campus-vpn\AGENTS.md`。

2026-09-30，来源：campus-vpn 项目对话和本机/A6000 实测。

- Windows 11 x64，HKUST(GZ) Connect 2.0.3。Fake-IP 导致网关解析为 `198.18.0.33`，引擎显示配置无效；Clash 添加网关 Fake-IP 排除和 DIRECT 规则后解决。
- 认证响应不兼容与用户名格式错误相关：官方客户端先报用户名或密码错误，去掉邮箱后缀后成功，具体原始错误码未采集。
- 最初热点仍共享校园 Wi-Fi，不能算校外验收；用户关闭手机 Wi-Fi 后重新测试。
- 内置浏览器 HTTP 代理转发返回空响应，但 SOCKS5/CONNECT 正常；关闭严格本地代理认证后浏览器成功。
- 普通应用原来按 Clash `10/8` DIRECT。已在当前订阅持久扩展脚本增加 `HKUSTGZ-Campus` SOCKS5 出站和 Cobot `10.7.165.64/32` 优先规则，运行配置重载成功；最终网页 HTTP 200、普通 SSH 命令执行成功。
- 脚本编辑曾误匹配注释模板，已修正并实际执行核验。A6000 通过客户端 helper 的 SSH ProxyCommand 成功访问。

本次只建立记录，不初始化项目 Git/远端仓库，不部署容器。后续按需扩展其他校内地址分流；长期稳定性、UDP 和上游 HTTP 转发修复未验收。详细配置位置、证据及限制见项目 README。Guide Git 由框架维护对话处理。

## 2026-09-30 当前：统一校园范围已生效

用户要求扩展 A6000、HPC 等资源。当前规则已从 Cobot /32 扩展为 `hkust-gz.edu.cn`、`hkust.edu.hk` 两个域名后缀与 `10.0.0.0/8`，统一走本机校园 SOCKS5 代理。网关 DIRECT/Fake-IP 排除保留；当前热点 `10.176.141.0/24` 优先直连。更换到其他 10.x 本地局域网时须更新例外；10/8 是分流范围，不代表全部地址均属校园或均可达。

普通 SSH 已通过 A6000、Cobot；Cobot HTTP 200；HPC 域名 SSH banner 正常，未登录 HPC。无需逐台配置 ProxyCommand。持久订阅脚本已执行核验并加载生效，仍需校园客户端连接、Clash TUN 开启、本地 SOCKS 1080 与严格认证关闭。该状态取代首次记录的“仅覆盖 Cobot / A6000 需 ProxyCommand”。来源：本项目对话及实测，详见正式 README 末节。

## 2026-09-30 后续：校园/校外手动切换

用户询问如何把校园分流切为 DIRECT，以及校外是否切回规则模式。已将固定校园出站改为可选组“校园访问”（select），成员为 `DIRECT` 和 `HKUSTGZ-Campus`。校园域名、10/8 规则现在指向该组；网关和热点局域网直连例外保持。

- 人在校园：Clash 保持规则模式，在“代理”页的“校园访问”组选 DIRECT；可以断开 HKUST(GZ) Connect。
- 人在校外：先连接 HKUST(GZ) Connect，在同一组选 HKUSTGZ-Campus；Clash 仍保持规则模式，终端经 TUN 分流。
- 两种场景均不需要改为全局模式或整个 Clash 直连模式。只切校园组，其他订阅分流仍按原规则。

当前电脑已回校园 WLAN `10.12.124.1/22`，组当前选择 DIRECT，API GET 核对一致。Cobot 网页 HTTP 200，A6000 普通 SSH 返回 `a6000-direct-ok`。校外代理成员与范围在之前移动数据测试中通过，本次未再次切换手机网络验收。

持久订阅脚本位置不变，新增 proxy-groups select，并将旧固定校园规则替换；实际执行和重复执行核验通过，运行配置加载返回 HTTP 204。后续在 UI 切换即可；若 UI 暂未显示，可刷新/重新进入代理页。参考：https://wiki.metacubex.one/config/proxy-groups/select/ 。

补充协议边界：本地校园 SOCKS5 路径不转发 ICMP，ping 超时不能据此判定校内资源不可达；此前重新测试 Cobot HTTP 200 和 SSH 命令正常。可用 `Test-NetConnection 10.7.165.64 -Port 22` 或端口 8015 的 TcpTestSucceeded 判断 TCP 可用性。来源：RFC 1928、本项目实测。

来源：2026-09-30 本项目后续对话。此节取代前文校园范围固定走 HKUSTGZ-Campus 的使用方式，历史排障证据保留。
