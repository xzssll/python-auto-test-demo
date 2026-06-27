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

## 6/26 周四 — 缺勤

---

## 6/27 周六 — 日志封装 + 注释清理（4h）

### 1. 🎯 今日任务执行清单

| 任务 | 简述 | 状态 |
|------|------|------|
| 任务1 | 从参考项目搬运 logger.py 和 httprequest.py，整合到当前项目 | ✅ 完成 |
| 任务2 | 替换项目中所有 `print()` 为 `logger.info()`，删除 conftest.py 调试 print | ✅ 完成 |
| 任务3 | 删除 @log 装饰器，解决控制台冗余输出问题 | ✅ 完成 |
| 任务4 | 清理 test_login_param.py 中所有被注释的旧代码（110行→29行） | ✅ 完成 |
| 任务5 | 撰写每日极客日志（五模块格式） | ✅ 完成 |

### 2. 🛠️ 技术沉淀与踩坑复盘

**完成情况**：日志封装 100% / HttpRequest 封装 100% / 注释清理 100% / Mock 笔记 0%（延后）

**技术亮点**：
- **loguru 日志封装**：参考 D:\Python_test\testApi 中的 Logger 类，整合到 `Src/utils/logger.py`
- **HttpRequest 单例封装**：`http_request = HttpRequest()` 全局唯一实例，Session 复用 TCP 连接
- **装饰器（@log）的权衡**：理解装饰器工作原理，选择删除 @log 装饰器以保持输出清洁

**踩坑与破局**：

| 坑 | 根本原因 | 避坑指南 |
|----|---------|---------|
| `logger().info()` 写成调用函数 | Logger 是类，`logger = Logger(...)` 创建的是实例，直接 `.info()`。写成 `logger()` 是在试图调用实例 | 区分「类」和「实例」 |
| @log 装饰器打印过多 | 装饰器自动打印每次请求的完整信息，9 条用例累积大量输出 | 调试阶段用装饰器，正式项目按需移除 |
| `<class 'requests.models.PreparedRequest'> POST` | @log 装饰器自动打印 | 定位到 httprequest.py 的 @log 行后删除 |

### 3. 👨‍💻 简历与面试语料转化

**简历优化句**：
> 独立封装 HttpRequest 请求层与 Logger 日志层，采用单例模式管理 Session 生命周期，引入 loguru 替换裸 print，实现接口调用链路全日志追踪。

**面试模拟答（STAR 法则）**：
- **S**：项目早期用 `print()` 输出，9 条数据驱动用例上线后满屏输出，失败定位困难
- **T**：需要可控日志系统 + 清理堆积的旧版注释代码
- **A**：调研 logging 和 loguru，选择后者封装 Logger 类；删除 @log 装饰器冗余输出；test_login_param.py 从 110 行清理到 29 行
- **R**：控制台清洁，日志文件在 `log/` 目录；面试官看到的代码干净、结构清晰

### 4. 💡 导师点评与精进建议

**评价**：用户独立完成日志和请求层封装，在 `logger().info` 错误上实现自我纠正。今日最大进展：从"能改代码"向"能讲清楚为什么这样改"的跨越。

**精进建议**：
- `validator.py` 中 `traceback.print_exc()` 应改为 `logger.error()` 统一出口
- HttpRequest 的 `__del__` 可提及"生产环境建议用 `with` 上下文管理器确保资源释放"

### 5. 📅 进度管控与明日规划

**大盘健康度**：第 2 周（6/23-29），日志/HTTP/注释三项提前完成，延后 2 天的 Mock 笔记标记为「项目收尾时统一整理」。README + 简历未动。

**明日作战计划（6/28 周日）**：
1. README.md — 30min
2. 简历 v1.0 — 2h
