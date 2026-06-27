# 6/27 周六 — 代码优化步骤（逐项对比 + 原因）

> 每项都是：原来什么样 → 改成什么样 → 为什么这样改。
> 代码块直接复制，不需要自己写。

---

## 第 1 步：清注释

| | 原来 | 改成 | 为什么 |
|------|------|------|--------|
| 文件 | `test_login_param.py` 第17-88行 | 删掉这些行 | 全是注释掉的旧版本，占半个文件，面试官打开看到一堆死代码 |
| 文件 | `conftest.py` 第20-37行 | 删掉这些行 | 注释掉的旧版 `_login_callback`，新版本已在下面，死的没必要留 |

**保留目的**：你之前说最后一并 copy 新文件、旧版留作错题集。现在做这件事——copy 一份干净的。

---

## 第 2 步：装 loguru

| 操作 | 命令 |
|------|------|
| 终端执行 | `pip install loguru` |

---

## 第 3 步：把 `print()` 换成日志

### 3.1 新建 `Src/utils/logger.py`

> 复制下面全部，新建文件粘贴进去，保存。

```python
from loguru import logger as logutil
from datetime import datetime


class Logger:
    def __init__(self, log_file=''):
        self.logger = logutil
        if log_file:
            self.logger.add(log_file, encoding="utf-8")

    def info(self, msg):
        self.logger.info(msg)

    def success(self, msg):
        self.logger.success(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warning(self, msg):
        self.logger.warning(msg)


log_file = f'log/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}-log.log'
logger = Logger(log_file=log_file)
```

### 3.2 替换项目中所有的 `print()`

| 文件 | 原来 | 改成 | 为什么 |
|------|------|------|--------|
| `test_login_param.py` 第95行 | `print(f"用例名称===", new_data["name"])` | `logger.info(f"用例名称=== {new_data['name']}")` | 写入日志文件，带时间戳，不再一闪而过 |
| `validator.py` 第82行 | `print("===响应数据校验通过===")` | `logger.info("===响应数据校验通过===")` | 同上 |
| `validator.py` 第89行 | `print("===数据库校验通过===")` | `logger.success("===数据库校验通过===")` | 同上 |
| `validator.py` 第80行 | `print(jp(resp.json(), v[0])[0])` | **删掉** | 纯调试用的脏 print，正式代码不留 |
| `conftest.py` 第38-40行 | `print(type(request))` + `print(request.method)` + `print("======")` | **删掉** | Mock 已经跑通了，调试代码不需要了 |

### 对比

| 维度 | `print()` | `logger.info()` |
|------|-----------|-----------------|
| 能看到吗 | 只在控制台，关了没了 | 控制台 + 写入文件 |
| 能翻历史吗 | ❌ | ✅ `log/` 目录下有文件 |
| 面试能讲吗 | "我用 print 调试" | "我集成了 loguru 日志系统" |

---

## 第 4 步：把 `requests.request` 换成 `HttpRequest`

### 4.1 新建 `Src/utils/httprequest.py`

> 复制下面全部，新建文件粘贴进去，保存。

```python
import requests


class HttpRequest:

    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.session.request("get", url=url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.request("post", url=url, **kwargs)

    def put(self, url, **kwargs):
        return self.session.request("put", url=url, **kwargs)

    def request(self, method, url, **kwargs):
        return self.session.request(method, url=url, **kwargs)

    def __del__(self):
        self.session.close()


http_request = HttpRequest()
```

### 4.2 改造 `test_login_param.py`

| | 原来 | 改成 | 为什么 |
|------|------|------|--------|
| 导入 | `import requests`（已有） | 下面加一行：`from Src.utils.httprequest import http_request` | 引入封装好的请求对象 |
| 发请求 | `resp = requests.request(**new_data["request"])` | `resp = http_request.request(**new_data["request"])` | 用 Session 保持 Cookie，自动复用连接 |

### 对比

| 维度 | `requests.request(...)` | `http_request.request(...)` |
|------|--------------------------|----------------------------|
| Cookie | 每次重新握手 | Session 自动保持 |
| 连接 | 每次新建/销毁 | 复用 TCP 连接（更快） |
| 可扩展 | 无 | 后面穿装饰器，自动打日志 |
| 面试能讲吗 | "我直接用 requests" | "我封装了 HttpRequest 类，集中管理请求" |

---

## 第 5 步：写 README.md

三块内容：项目结构 / 技术栈 / 如何运行。

```markdown
# Python API Auto Test Demo

## 技术栈
Python 3.12 | pytest 9.x | requests | jsonpath | YAML 数据驱动
responses (HTTP Mock) | unittest.mock (DB Mock) | Allure 报告

## 项目结构
├── Src/case/        测试用例
├── Src/utils/       工具类 (validator / mysql_client / yamloader / logger / httprequest)
├── data/            YAML 测试数据
├── conf/            配置
├── log/             日志输出

## 运行
pip install -r requirements.txt
pytest Src/case/ -v

## 亮点
- YAML 数据驱动 + 动态占位符替换
- HTTP Mock + DB Mock，不依赖外部环境
- 接口断言 + 数据库断言双重验证
- 10 条用例覆盖正常/异常/边界/安全场景
```

---

## 第 6 步：跑通

```bash
pytest Src/case/test_login_param.py -v
```

**目标：9 passed。**
