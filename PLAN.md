# PLAN.md — 2.5个月跳槽冲刺计划 进展总览

> 更新时间: 2026-06-25
> 目标: 2026年9月1日前完成跳槽（成都为主，深圳为辅）
> 当前阶段: 第2周（6/23-29）Mock 已跑通 → 追 日志 + README + AI文档 + CI

---

## 一、个人画像

| 维度 | 现状 |
|------|------|
| 测试经验 | 2.5年手工测试（断续） |
| Python | 能读能改，手写吃力——用AI辅助生成后人工review |
| Pytest | 已掌握：@parametrize + YAML数据驱动 + Validator断言器 + fixture（学习中） |
| 数据库 | MySQL 增删查改 / JOIN / 子查询 / 聚合函数 |
| 工具链 | 云效 / Xmind / Fiddler / Charles / Apifox |
| 性能测试 | 做过1次单接口压测但没搞懂 |
| 可用时间 | 工作日 1-1.5h + 周末 4h（半天） |
| 自有项目 | Python web后台+APP项目，可在本地跑，有MySQL |

---

## 二、代码水平重新评估（两个版本对比）

### 当前项目（2026版）
- ✅ pytest + requests + jsonpath 接口自动化
- ✅ YAML 数据驱动 + 动态占位符替换（json序列化方案）
- ✅ Validator 断言器（eq/nq/iin/nni），接口断言 + DB断言
- ✅ Mock 双件套（responses.add_callback + unittest.mock.patch）
- ✅ **9 passed** — Mock 全场景覆盖（POST/GET/PUT + JSON/form-encoded + code缺失/错误/正确）
- ✅ **每个坑都踩了，能讲清楚为什么**

### 两年前项目（2024版，taskApiRunner，跟着视频抄的）
- ⭐ HttpRequest 类 — requests.Session 封装，装饰器自动打日志
- ⭐ Yamloader — 自定义 `!get_token` 标签 + `${phone}` 替换（正则+eval方案）
- ⭐ Logger — loguru 全封装
- ⭐ conftest — pytest_terminal_summary 钩子自动汇总 + 钉钉/邮件通知
- ⭐ create_task fixture — DB插入+查ID+返回
- ⚠️ 跟着B站视频抄的，独立写不出来，两年后已忘记

### 两个版本对比结论
| 维度 | 2026版（当前） | 2024版（两年前） |
|------|-------------|---------------|
| 结构完整性 | 中等（8个py文件） | 高（17个py文件） |
| Mock能力 | ✅ **有**（超越两年前） | ❌ 无 |
| HTTP封装 | 散装 requests.request | ✅ HttpRequest类 |
| 日志 | print | ✅ loguru全封装 |
| 独立思考 | ✅ **每个坑都踩了** | ❌ 跟着视频抄的 |
| 能讲清楚吗 | ✅ 能 | ❌ 忘了 |

**策略：从两年前的代码里搬 HttpRequest + Logger 到当前项目，周末搞定。**

---

## 三、已完成事项

| 日期 | 完成项 | 详情 |
|------|--------|------|
| 6/17 | 初始评估 + 计划制定 | Excel: `跳槽冲刺计划_2.5个月.xlsx`（5个Sheet） |
| 6/18 | jsonpath环境修复 | pip install jsonpath==0.82，test_login.py 2 passed |
| 6/21 | Mock层搭建 | conftest.py: mock_api + mock_db |
| 6/22 | GitHub仓库上线 | https://github.com/xzssll/python-auto-test-demo |
| 6/23 | 异常场景数据扩展 | AI辅助生成 new_test_login.yaml，10条 |
| 6/24 | Mock 全场景跑通 | **9 passed**，踩坑5个，全部记录在案 |
| 6/25 | 项目代码审计 + 旧项目复盘 | 对比两年前版本，定位搬运目标（HttpRequest+日志） |

---

## 四、修正后的路线图（从 6/26 出发）

### 第 2 周剩余（6/25-29）：日志 + README + AI文档 + CI

| 天 | 晚（1.5h） | 产出 |
|----|-----------|------|
| **6/25 周三** | 代码审计 + 旧项目复盘 + 计划更新 | 两版本对比完成 |
| **6/26 周四** | 用自己的话写 Mock 理解笔记 | Mock 笔记 |
| **6/27 周五** | 清理项目文件（删注释掉的旧代码） | 代码干净 |
| **6/28 周六(4h)** | **重点**：①loguru日志替换print ②README.md ③HttpRequest封装 | 日志+README+请求层 |
| **6/29 周日(3h)** | **AI辅助测试实践文档** + **简历 v1.0 定稿** + 发周报 | AI文档+简历 |

> 周四周五做轻活（笔记+整理），周末集中攻坚写代码。

### 第 3 周（6/30-7/6）：深度覆盖 + 投递练手

| 天 | 晚（1.5h） | 产出 |
|----|-----------|------|
| 6/30 周一 | 边界值用例 | 5条 |
| 7/1 周二 | 鉴权场景 | 3条 |
| 7/2 周三 | 业务流程场景 | 1条 |
| 7/3 周四 | 并发测试 | 记录 |
| 7/4 周五 | AI第2轮评审 | 盲区补齐 |
| **7/5 周六(4h)** | 项目收尾 | — |
| **7/6 周日(3h)** | **投第一批简历 5-8家** | 简历已投 |

### 第 4 周（7/7-13）：面试准备 + Locust

| 天 | 任务 |
|----|------|
| 周一至五 | 每天准备1个面试高频问题话术 |
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
| **6/29** | CI绿灯 + 日志 + README + AI文档 + 简历v1.0 | push自动跑 |
| **7/6** | 30+用例 + 开始投简历 | 已投5-8家 |
| **7/13** | 面试5问题话术 + Locust报告 | 5问流畅对答 |
| **7/20** | 项目收尾 + 简历v1.5 + 密集投递 | 每天5-8家 |
| **8/15前** | 第一个offer | 至少1个offer在手 |
| **8/31前** | 跳槽完成 | 入职材料就绪 |

---

## 六、当前状态（6/25 周三）

已完成 Mock 跑通 + 代码审计 + 旧项目复盘。今晚剩余任务：**用你自己的话写一份 Mock 理解笔记。**

**明日（6/26）任务**：
1. 装 loguru，把项目中所有 `print()` 换成 logger
2. 写 README.md

---

## 七、项目面试亮点清单（动态更新）

- [x] pytest + requests + jsonpath 接口自动化
- [x] YAML 数据驱动 + 动态占位符替换
- [x] Validator 断言器（接口断言 + DB断言分离）
- [x] HTTP Mock（responses.add_callback 按请求体动态返回）
- [x] DB Mock（unittest.mock.patch 替换 pymysql 查询）
- [x] AI 辅助生成测试数据（10条YAML用例）
- [x] **9 passed** — Mock 全场景覆盖
- [ ] loguru 日志系统
- [ ] HttpRequest 请求层封装
- [ ] CI 流水线（GitHub Actions）
- [ ] Allure 测试报告
- [ ] AI 辅助测试实践文档
- [ ] Locust 单接口压测脚本

---

## 八、技术踩坑记录（面试可讲）

### 坑1：`_login_callback(request)` 的 `request` 到底是什么？

**错误**：当成 YAML 字典写 `body["request"]["method"]`
**真相**：`request` 是 HTTP `PreparedRequest` 对象：
```
request.method    → "POST" / "GET" / "PUT" ...（大写！）
request.body      → b'{"phone":"..."}'（bytes，可能为空）
request.headers   → {'Content-Type': 'application/json'}
request.url       → 'http://...'
```
**教训**：
- 不确定参数类型 → `print(type(x))` + `print(dir(x))`
- `request.method` 返回**大写**，小写判断会不匹配
- `request.body` 可能为 None（GET）或 form-encoded（非JSON），`json.loads` 前必须判空+判格式

### 坑2：`json.loads()` 放到最后，不是最前

**错误**：所有请求先 `json.loads`，再判断 method/Content-Type → 非JSON请求直接崩在解析行
**正确**：先过滤（method → body格式）→ 再 json.loads

### 坑3：`body.get("code", "")` 把"不存在"和"空字符串"混成一件事

**错误**：`.get("code", "")` 缺失时返回 `""`，无法区分缺字段和值错误
**真相**：`.get("code")` → None（可判断缺失）；`.get("code","xx")` → "xx"（缺失被掩盖）

### 坑4：Windows下 `request.body` 可能是 str 不是 bytes

**错误**：`request.body.startswith(b"phone=")` → TypeError
**修复**：`str(request.body).startswith("phone=")`，兼容两种类型

### 坑5：`dict.get(key)` vs `dict.get(key, default)`

```
dict.get("key")        → key不存在返回 None
dict.get("key", "xx")  → key不存在返回默认值 "xx"
```
查方法：`print(dir({}))` + `help({}.get)` 比文档快

---

## 九、6/24-25 关键认知

1. 用户两年前写的框架（taskApiRunner）是跟着视频抄的，独立写不出来
2. 现在写的版本代码结构不如两年前，但**理解深度超过了当时**——每个坑都是独立思考
3. 策略：从两年前代码里搬运 HttpRequest + Logger，周末搞定
4. 定位：面试要的是"能改能讲"，不是"能从零写框架"
5. 下一个里程碑：用自己的话写 Mock 笔记 → 整理清楚了就是面试话术

---

## 十、周报模板

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

---

## 十一、每日速查

**6/26 周四（今晚 1.5h）**：
- [ ] 写 Mock 理解笔记（自己的话，markdown，发到对话）

**目标**：9/1 前成都跳槽，12-15K 自动化测试岗
**最近里程碑**：6/29（周日）AI文档 + 简历 v1.0
