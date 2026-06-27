# 每日日志

> 记录每一天做了什么、学到了什么、踩了什么坑。
> 面试前回顾这个文件，每一天都是你的素材。

---

## 6/17 周二 — 启动日

**做了什么**：
- 评估个人画像（优势/劣势）
- 讨论成都/深圳市场
- 制定 2.5 个月跳槽冲刺计划框架
- 确定用自有 Python 项目（web后台+APP）作为测试靶场
- 生成 Excel 计划文档 `跳槽冲刺计划_2.5个月.xlsx`（5个Sheet）
- 创建 PLAN.md

**学到/收获**：
- 市场要的不是"精通Python"，是"能搭建框架 + AI辅助落地"
- Mock + DB断言 + YAML数据驱动 + CI 是面试核心亮点
- 周末不能调公司API → 用 Mock 解决

---

## 6/18 周三 — 环境确认

**做了什么**：
- 确认 Python 3.7 + pytest 7.3.1 + requests 环境 OK
- 跑通 `test_login.py`，**2 passed**
- 修复 jsonpath 版本不兼容（安装 jsonpath==0.82）
- 发现项目有两个版本：venv（Python 3.12）和 Anaconda（Python 3.7）
- 读了自己的 `test_login_param.py`，发现已经写过参数化 + YAML数据驱动

**学到/收获**：
- `jsonpath` 老版本用 `search`，新版本没有这个函数
- 自己两年前写的代码比自己以为的好

---

## 6/19-20 — 缺勤（加班）

---

## 6/21 周六 — Mock 层搭建

**做了什么**：
- 因 IP 被服务器拉黑，被迫提前学 Mock
- 在 `Src/conftest.py` 创建 `mock_api`（responses.add_callback）+ `mock_db`（unittest.mock.patch）
- GitHub 仓库 `python-auto-test-demo` 首次 push
- 被拉黑后发现"不是学了备用，是不得不做"——坏事变好事

**学到/收获**：
- `responses.RequestsMock` 拦截 HTTP 请求
- `unittest.mock.patch` 替换数据库查询
- 被拉黑 = Mock 面试素材（"我的项目不依赖任何外部环境"）

---

## 6/22 周日 — 缺勤（有事）

---

## 6/23 周一 — 加班

**做了什么**：
- 加班，抽空写了 `_login_callback` 但没跑通
- 犯了 3 个致命错误：`json.loads(request)` / `body["request"]["method"]` / `body.get("code","")==None`
- 心态崩了，提前收工

**踩的坑**：
- 把 `request` 对象当成了 YAML 字典
- HTTP 方法在 `request.method` 不在 `body["request"]["method"]`
- 空字符串 `""` 永远不等于 `None`

---

## 6/24 周二 — Mock 调试 + 全场景跑通

**做了什么**：
- 用 `print(type(request))` 定位了参数类型
- 修正 3 处错误，Mock 从 2 passed → **9 passed**
- 理解 `json.loads` 必须在过滤之后执行
- DB 断言通过（mock_db 生效）
- 记录了 5 个技术踩坑

**学到/收获**（面试可讲）：
- **坑1**：`request` 是 `PreparedRequest` 对象，不是 YAML 字典
- **坑2**：`json.loads()` 放最后，不是最前
- **坑3**：`.get("code","")` 混了"缺失"和"错误"
- **坑4**：Windows 下 `request.body` 可能是 str 不是 bytes
- **坑5**：`dict.get(key)` vs `dict.get(key, default)` 的区别

**关键认知**：
- 不确定参数类型 → `print(type(x))` + `print(dir(x))`
- 慢就慢，print 调试比猜着写快
- 自己写的 Mock 逻辑覆盖了所有场景，只是顺序问题，不是全错

---

## 6/25 周三 — 代码审计 + 旧项目复盘

**做了什么**：
- 通读两年前的项目 `taskApiRunner`（17个py文件）
- 对比两个版本的差距：2026版有Mock但结构不全，2024版结构完整但是跟着视频抄的
- 确认两年前框架的精华：HttpRequest类、Logger封装、pytest_terminal_summary钩子、钉钉通知
- 制定搬运策略：搬 HttpRequest + Logger，周末搞定
- 调整本周剩余计划：周四周五轻活（笔记+清理），周末攻坚（写代码）
- 更新 PLAN.md

**学到/收获**：
- 两年前写过一个完整的测试框架，只是忘了
- 现在的代码结构不如两年前，但理解深度超过了当时
- "能改能讲"比"能从零写"更适合当前定位
- 面试12-15K要的是"能改能讲"，18-25K才要"独立设计"

**两版本对比**：

| 维度 | 2026版 | 2024版 |
|------|--------|--------|
| 结构 | 8个py文件 | 17个py文件 |
| Mock | ✅ 有 | ❌ 无 |
| 日志 | print | ✅ loguru |
| HTTP封装 | 散装 | ✅ HttpRequest类 |
| 独立思考 | ✅ | ❌（跟着抄的） |

---

## 6/26 周四 — 任务完成

**原计划**：写 Mock 理解笔记
**状态**：用户确认完成（待补充具体内容）

---

## 6/27 周六 — 追齐进度（4h）

**任务**：
- [ ] 清理 test_login_param.py / conftest.py 注释旧代码
- [ ] pip install loguru，替换所有 print → logger
- [ ] 写 README.md
- [ ] HttpRequest 封装（耗时不够则推到明天）
- [ ] Mock 笔记：标记为「项目收尾时统一整理」，不在今天做

今日的一些理解

