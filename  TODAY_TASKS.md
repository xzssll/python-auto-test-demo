# 6/27 周六 — 今日任务清单

> 时间：4h | 目标：日志 + 封装 + README

---

## 最终任务表

| 序号 | 任务 | 具体操作 | 参考 | 预计 | 状态 |
|------|------|---------|------|------|------|
| 1 | 装 loguru | 终端执行 `pip install loguru` | — | 1min | [ ] |
| 2 | 写 logger.py | IDE 新建 `Src/utils/logger.py`，复制下方「代码块A」 | 见下 | 10min | [ ] |
| 3 | 写 httprequest.py | IDE 新建 `Src/utils/httprequest.py`，复制下方「代码块B」 | 见下 | 10min | [ ] |
| 4 | 改造 test_login_param.py | ①导入 `from Src.utils.httprequest import http_request` ②把 `resp = requests.request(...)` 换成 `resp = http_request.request(...)` ③把 `print()` 换成 `logger.info()` | — | 10min | [ ] |
| 5 | 改造 validator.py | 删掉第80行 `print(jp(...))`，把其他 `print` 换成 `logger.info()` | — | 5min | [ ] |
| 6 | 改造 conftest.py | 把那 3 行 `print(type/print/print)` 换掉或直接删掉 | — | 5min | [ ] |
| 7 | 跑测试 | `pytest Src/case/test_login_param.py -v` → **9 passed** | — | 2min | [ ] |
| 8 | README.md | 参考 PLAN.md 的面试亮点清单写 | — | 30min | [ ] |
| 9 | Git commit | `git add . && git commit -m "feat: 日志+HttpRequest封装，替换print"` | — | 5min | [ ] |

---

## 代码块A：`Src/utils/logger.py`（直接复制）

```python
import sys
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

## 代码块B：`Src/utils/httprequest.py`（直接复制）

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

---

## 测试用例里怎么用（改法示例）

你原来的代码：
```python
resp = requests.request(**new_data["request"])
```

改为：
```python
from Src.utils.httprequest import http_request
resp = http_request.request(**new_data["request"])
```

YAML 里的 `method` / `url` / `json` / `headers` 通过 `**` 自动解包匹配，不改 YAML。
