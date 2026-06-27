# 6/27 周六 — 优化步骤清单

> Mock 笔记延后到项目收尾。今天做这 4 项。

---

| 序号 | 做什么 | 具体操作 | 预计 | [ ] |
|------|--------|---------|------|-----|
| 1 | 清注释 | 删掉 `test_login_param.py` 第17-88行被注释的旧代码；删掉 `conftest.py` 第20-37行注释的旧版 `_login_callback` | 15min | [ ] |
| 2 | 装 loguru | 终端执行 `pip install loguru` | 1min | [ ] |
| 3 | 写 logger.py | IDE 新建 `Src/utils/logger.py`，复制 TODAY_TASKS.md 里的代码块A；把 `validator.py` 和 `conftest.py` 里的 `print()` 换成 `logger.info()` | 20min | [ ] |
| 4 | 写 httprequest.py | IDE 新建 `Src/utils/httprequest.py`，复制 TODAY_TASKS.md 里的代码块B；把 `test_login_param.py` 里的 `requests.request(...)` 换成 `http_request.request(...)` | 15min | [ ] |
| 5 | 写 README.md | 按项目结构/技术栈/如何运行三块写，30行即可 | 30min | [ ] |
| 6 | 跑通 | `pytest Src/case/test_login_param.py -v` → 9 passed | 2min | [ ] |

---

## 代码块A：`Src/utils/logger.py`

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

## 代码块B：`Src/utils/httprequest.py`

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

## 改法示例

原来：`resp = requests.request(**new_data["request"])`
改为：`from Src.utils.httprequest import http_request` + `resp = http_request.request(**new_data["request"])`
