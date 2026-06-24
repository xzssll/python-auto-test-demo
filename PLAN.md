# PLAN.md — 2.5个月跳槽冲刺计划 进展总览

> 更新时间: 2026-06-24
> 目标: 2026年9月1日前完成跳槽（成都为主，深圳为辅）

---

## 一、个人画像

| 维度 | 现状 |
|------|------|
| 测试经验 | 2.5年手工测试（断续） |
| Python | 能读能改，手写吃力——用AI辅助生成后人工review |
| Pytest | 已掌握：@parametrize + YAML数据驱动 + Validator断言器 + fixture/conftest（学习中） |
| 数据库 | MySQL 增删查改 / JOIN / 子查询 / 聚合函数 |
| 工具链 | 云效 / Xmind / Fiddler / Charles / Apifox |
| 性能测试 | 做过1次单接口压测但没搞懂 |
| 可用时间 | 工作日 1-1.5h + 周末 4h（半天） |
| 自有项目 | Python web后台+APP项目，可在本地跑，有MySQL |

---

## 二、已完成事项

| 日期 | 完成项 | 详情 |
|------|--------|------|
| 6/17 | 初始评估 + 计划制定 | Excel: `跳槽冲刺计划_2.5个月.xlsx`（5个Sheet） |
| 6/18 | jsonpath环境修复 | pip install jsonpath==0.82，test_login.py 2 passed |
| 6/21 | Mock层搭建 | conftest.py: mock_api（responses.add_callback）+ mock_db（unittest.mock.patch） |
| 6/22 | GitHub仓库上线 | https://github.com/xzssll/python-auto-test-demo，首次push完成 |
| 6/23 | 异常场景数据扩展 | **AI辅助生成** new_test_login.yaml，从2条扩到10条：正常/错误码/缺字段/SQL注入/form-encoded/GET/PUT/DELETE |

---

## 三、当前实际进度 vs 原始计划

| 原始计划（第2周周一） | 实际状态 | 偏差说明 |
|----------------------|---------|---------|
| 补5条异常用例 | ✅ **超额完成** — 10条YAML数据已就绪 | AI辅助生成 + 人工review |
| — | 🔴 **Mock未跟上** — 只支持POST+2种返回，10条用例5 failed | 回调逻辑需扩展 |

**结论：数据层超前，Mock层滞后。整体方向没错，是正常的"数据先行→Mock追数据"迭代节奏。**

---

## 四、修正后的路线图（从今天 6/24 出发）

### 第 2 周剩余（6/24-29）：补 Mock + 数据驱动 + CI

| 天 | 晚（1.5h） | 产出 |
|----|-----------|------|
| **6/24 周二** | **扩 Mock**：`_login_callback` 加6个分支，让10条全绿 | 10 passed |
| **6/25 周三** | **数据库断言恢复**：打开 validator.py 里被注释的 DB 验证部分，确认 mock_db 生效 | DB断言跑通 |
| **6/26 周四** | **README.md**：写清楚项目结构/技术栈/运行方式 | README就绪 |
| **6/27 周五** | **AI辅助用例文档**：写1页文档记录"AI生成数据→人工review→接入框架"全流程 | AI实践文档 |
| **6/28 周六(4h)** | **CI流水线**：GitHub Actions push自动跑pytest + Allure报告 + Mock保证CI不依赖外部 | CI绿灯 |
| **6/29 周日(3h)** | **简历 v1.0 定稿** + 发周报 | 简历就绪 |

### 第 3 周（6/30-7/6）：深度覆盖 + 投递练手

| 天 | 晚（1.5h） | 产出 |
|----|-----------|------|
| 6/30 周一 | 边界值：字段长度/数值上下界/空字符串 用例 | 边界值5条 |
| 7/1 周二 | 鉴权场景：token过期/无token/错误token | 鉴权3条 |
| 7/2 周三 | 业务流程：连调3接口场景 + 中间查库 | 场景用例1条 |
| 7/3 周四 | 并发：pytest-xdist 并行观察数据竞争 | 并发记录 |
| 7/4 周五 | AI第2轮：让AI评审用例覆盖盲区→补3条 | 覆盖盲区补齐 |
| **7/5 周六(4h)** | Mock体系完善 + README终版 + 项目亮点清单 | 项目收尾 |
| **7/6 周日(3h)** | **投第一批简历 5-8家** + 自我介绍录音 | 简历已投 |

### 第 4 周（7/7-13）：面试准备 + Locust

| 天 | 任务 | 
|----|------|
| 周一至五 | 每天准备1个面试高频问题话术（共5个） |
| 周六 | Locust单接口压测脚本 + 报告 |
| 周日 | 面试复盘 + 继续投递 |

### 第 5 周（7/14-20）：项目收尾 + 密集投递

| 天 | 任务 |
|----|------|
| 周一至五 | 面试反馈修补 + 用例数补到30+ |
| 周六 | 项目最终收尾（代码风格/演示视频/简历v1.5） |
| **周日** | **密集投递模式启动** |

### 第 6-11 周（7/21-8/31）：面试冲刺

| 周次 | 重点 |
|------|------|
| 第6-8周 | 密集面试 + 逐场复盘 |
| 第9-10周 | offer谈判 + 市场数据整理 |
| 第11周 | 离职交接 + 入职准备 |

---

## 五、里程碑（修正版）

| 日期 | 必须产出 | 验收标准 |
|------|---------|---------|
| **6/29** | CI绿灯 + 数据驱动 + DB断言 + AI文档 + 简历v1.0 + **10条用例全绿** | push自动跑 |
| **7/6** | 30+用例 + Mock完善 + 开始投简历 | 已投5-8家 |
| **7/13** | 面试5问题话术 + Locust报告 | 5问流畅对答 |
| **7/20** | 项目收尾 + 简历v1.5 + 密集投递 | 每天5-8家 |
| **8/15前** | 第一个offer | 至少1个offer在手 |
| **8/31前** | 跳槽完成 | 入职材料就绪 |

---

## 六、当前卡点（6/24 周二状态）

**Mock 回调未跑通**：`_login_callback` 中的 3 个错误已定位，明日修改目标：

1. `json.loads(request)` → `json.loads(request.body)`
2. `body["request"]["method"]` → `request.method`
3. `body.get("code", "") == None` → `not body.get("code")`

**明日第一件事**：在 `_login_callback` 第一行加 `print(type(request))`，确认参数类型后再改。

---

## 七、项目面试亮点清单（动态更新）

- [x] pytest + requests + jsonpath 接口自动化
- [x] YAML 数据驱动 + 动态占位符替换（`${phone}` → 实际值）
- [x] Validator 断言器模式（eq/nq/iin/nni），接口断言 + DB断言分离
- [x] HTTP Mock（responses.add_callback 按请求体动态返回）
- [x] DB Mock（unittest.mock.patch 替换 pymysql 查询）
- [x] AI 辅助生成测试数据（10条YAML用例：正常/异常/边界/安全，AI生成→人工review）
- [x] **9 passed, 0 skipped, 0 error** — Mock 全场景覆盖
- [ ] CI 流水线（GitHub Actions，push自动跑）
- [ ] Allure 测试报告
- [ ] AI 辅助测试实践文档（正式版）
- [ ] Locust 单接口压测脚本 + 报告

---

## 九、技术踩坑记录（面试可讲）

### 坑1：`_login_callback(request)` 的 `request` 到底是什么？

**错误**：当成 YAML 字典写 `body["request"]["method"]`
**真相**：`request` 是 HTTP `PreparedRequest` 对象，结构完全不同：

```
request.method    → "POST" / "GET" / "PUT" ...（大写！）
request.body      → b'{"phone":"...","code":"..."}'（bytes，可能为空）
request.headers   → {'Content-Type': 'application/json'}
request.url       → 'http://...'
request.path_url  → '/task/server/api/phone/login'
```

不是 `request.body["request"]["method"]`，是 `request.method`。
不是 `json.loads(request)`，是 `json.loads(request.body)`。

**教训**：
- 不确定参数类型 → `print(type(x))` + `print(dir(x))` 看清楚
- `request.method` 返回大写（`"POST"`），用小写判断会不匹配
- `request.body` 可能是 `None`（GET请求）或 form-encoded字符串（非JSON），`json.loads` 前必须判空+判格式
- 慢就慢，print 调试比猜着写快

### 坑2：`json.loads()` 放到最后，不是最前

**错误**：所有请求先 `json.loads`，再判断 method/Content-Type
**真相**：非 POST 请求的 body 为空或非 JSON → 直接崩在解析那行，后面的判断永远走不到

**正确做法**：
```
1. 先判断 method
2. 再判断 body 格式
3. 最后才 json.loads（只处理真正的 JSON POST 请求）
```

### 坑3：`body.get("code", "")` 把"不存在"和"空字符串"混成一件事

**错误**：`.get("code", "")` 缺失时返回 `""`，和 code 为空串无法区分
**真相**：缺 code 应返回"参数不对"，code 错误应返回"验证码不正确"——两类场景
**修复**：把缺 code 的判断提到 code 错误判断之前

### 坑4：Windows下 `request.body` 可能是 str 不是 bytes

**错误**：`request.body.startswith(b"phone=")`
**真相**：Windows 的 requests 库有时 body 是 str 类型，`str.startswith(bytes)` 报 TypeError
**修复**：`str(request.body).startswith("phone=")`，兼容两种类型

---

## 八、周报模板

---

## 九、技术踩坑记录（面试可讲）

（内容见上）

---

## 十、6/24 当日总结：用户自我复盘

### 心路历程
- 不知道 `request` 是 `PreparedRequest` 类对象，不是 YAML 字典
- 不知道 `request` 包含 headers/body/method/url 等属性，以及用 `.` 取值的方法
- 取出来的数据格式不确定（method 是大写、body 可能是 None/str/bytes），判断时容易出错
- 学会了用 `print(type(x))` + `print(dir(x))` 逐步调试，虽然慢但有效
- 自主写代码太少，逻辑漏洞多，调试耗时长

### 核心收获
1. `request` 是 HTTP 请求对象，属性用 `.` 访问，跟 YAML 字典完全不是一回事
2. `json.loads()` 必须放到分支过滤之后执行，不是第一行
3. `print(type(x))` 是最可靠的调试起点
4. 代码跑通了 ≠ 全理解了，明日需要花时间捋清楚每一行

### 明天（6/25）计划
**先捋，再写。** 把 conftest.py 的 `_login_callback` 逐行理解透彻，再做 README。

```
【第N周 周报 — 日期：______】
1. 本周完成条目（打✓）
2. GitHub本周提交次数：____次 | 当前用例总数：____条
3. 工作中提升事项（技术分析/漏测复盘/Apifox/风险汇报）
4. 卡点/问题
5. 面试情况（投递/面试/复盘）
6. 下周计划微调
7. 本周产出物链接
```
