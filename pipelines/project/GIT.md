# Git 与 GitHub 仓库

先按[项目启动流程](README.md)确定项目和工作位置，再选择新建、clone 或 fork。以下是用户已确定的默认设置，后续对话直接使用。

## 默认设置

| 项目 | 默认值 |
|---|---|
| GitHub 所有者 | `ajwwja777` |
| Git 提交署名（user.name） | `ajwwja777` |
| Git 提交邮箱（user.email） | `139873756+ajwwja777@users.noreply.github.com`（GitHub 隐私邮箱） |
| 新建仓库可见性 | 公开（public） |
| 新建仓库名称 | 根据项目用途自动选取简短明确的英文名，小写、连字符分词；通常与项目目录名一致 |
| 新建本地默认分支 | `main` |
| 默认完成范围 | 创建项目目录和基础文档、初始化独立 Git、创建 GitHub 仓库、关联 origin、验证并记录结果 |

用户要求新建项目时，agent 自动执行上述范围，不重复询问固定账号、公开设置或常规命名。用户在当前对话另有要求时以其为准。需要浏览器登录、设备授权或权限确认时，给出链接或操作让用户完成，然后继续。

自动建仓关联不等于自动发布目录里的全部文件；首次提交与 push 按用户当前要求完成，按文件审阅和暂存。

## 执行前检查

- 优先使用 `gh`。A6000 固定入口为 `/data/LFT-W02_data/jiaan/jiaan/projects/agent-tools/bin/gh`；长期工具存放在 agent-tools，scratch 只作下载与缓存。
- 用 `gh api user --jq .login` 核对账号。已有正确认证直接复用；缺少认证时用 GitHub CLI 的设备/浏览器登录流程，不让用户在聊天或仓库提供 token。
- 提交身份默认使用上表的署名与邮箱，在目标仓库用 `git config --local user.name ajwwja777` 和 `git config --local user.email 139873756+ajwwja777@users.noreply.github.com` 设置；提交前核对生效身份。GitHub 登录账号仍为 `ajwwja777`。
- 查看目标目录、仓库根和 origin。已有正确仓库与关联时直接复用，不重复初始化。
- 查询拟用仓库名是否存在；只有认证正常且明确返回 404 才按不存在处理。已有仓库需确认属于本项目；不覆盖无关 origin，不将已有私有仓库自动改为公开。

## A. 新建自己的项目

1. 在选定机器工作区创建项目目录和基础文档，保留已有内容。
2. 在项目目录执行 `git init`，新仓库设为 main，并用 `git rev-parse --show-toplevel` 确认根目录。配置适合项目的忽略项；嵌套在其他仓库内时从外层本地排除，避免重复纳入。
3. 在目标目录执行以下建仓和关联命令。`<仓库名>` 是占位符，由 agent 根据项目自动选取：

   `gh repo create ajwwja777/<仓库名> --public --source=. --remote=origin`

4. 用 `git remote -v` 和 GitHub API 核对仓库所有者、公开状态和写入权限。若建仓成功但关联失败，下次只补齐关联，不重复创建。
5. 写回实际路径、仓库链接、分支和完成状态；向用户报告。

新远端保持空仓库，不同时添加另一份 README。已有且确定属于当前项目的空远端，可以通过 `git remote add origin <仓库URL>` 关联；若远端已有提交，先检查历史，不强制推送。

## B. 直接 clone 已有项目

确认来源与目标路径，clone 到新目录或空目录；无需再 init。保留 origin 指向原仓库，记录复现的 commit/tag。直接 clone 不意味着有向原仓库 push 的权限，也不自动为其创建另一个空仓库。

## C. fork 后维护适配

需要自己维护上游副本时，优先在 `ajwwja777` 下创建或复用对应 fork，再 clone。通常 origin 指向自己的 fork，upstream 指向原仓库；记录固定上游版本和适配分支。权限、许可或私有上游限制不通过公开复制绕过。

## 提交与同步

需要发布时，审阅具体文件，按文件暂存、提交，再用 `git push -u origin <分支名>` 发布；不使用 `git add .` 或强制推送。验证远端分支后记录已发布状态。

新建、clone、fork 各自扩展实际需要的流程；每次更新向用户说明改了哪些文件，以及创建、关联、提交和推送分别完成到哪一步。
