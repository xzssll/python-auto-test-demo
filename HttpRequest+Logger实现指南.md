# HttpRequest 封装 + Logger 日志 —— 实现指南

> 参考项目：`D:\Python_test\testApi\Src\util\httprequest.py` 和 `logger.py`
> 目标项目：`d:\23_24test_26\2026_Python_auto1\`

---

## 一、HttpRequest 封装

### 它在解决什么问题

现在你的项目里每调一次接口都是：
```python
resp = requests.request(method="post", url=url, json=data, headers=header)
```
URL 变了要改、method 变了要改、每次都要写 `requests.request`。散的。

HttpRequest 把它包一层，变成一个可复用的对象。

### 它是怎么实现的（拆解）

**第 1 步：创建类，初始化时建立一个 Session**
```python
import requests

class HttpRequest:
    def __init__(self):
        self.session = requests.session()   # Session 自动保持 Cookie
```

**第 2 步：提供 get / post / put / request 四个方法**
```python
    def get(self, url, **kwargs):
        return self.session.request("get", url=url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.request("post", url=url, **kwargs)

    def put(self, url, **kwargs):
        return self.session.request("put", url=url, **kwargs)

    def request(self, method, url, **kwargs):
        return self.session.request(method, url=url, **kwargs)
```

`**kwargs` 把 json / headers / data 等参数原样传进去。你原来怎么传，现在还是怎么传。

**第 3 步：最后清理**
```python
    def __del__(self):
        self.session.close()
```

**第 4 步：暴露一个单例**
```python
http_request = HttpRequest()   # 全局唯一实例
```

### 用起来什么样

你原来的代码：
```python
resp = requests.request(**new_data["request"])
```

改为：
```python
from Src.util.httprequest import http_request
resp = http_request.request(**new_data["request"])
```

YAML 里的 `method` / `url` / `json` / `headers` 通过 `**` 解包自动匹配。

---

## 二、Logger 日志

### 它在解决什么问题

现在你用的是 `print()`——不看控制台就丢了。Logger 能写文件 + 带时间戳 + 分级别（info/success/error/warning）。

### 它是怎么实现的（拆解）

**第 1 步：装 loguru**
```bash
pip install loguru
```

**第 2 步：封装一个 Logger 类**
```python
from loguru import logger as logutil

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
```

**第 3 步：最关键——装饰器**
```python
def log(func):
    """装饰器：自动记录每次接口调用的请求参数和响应"""
    def wrapper(*args, **kwargs):
        logger.info("开始测试接口，接口信息如下：")
        for k, v in kwargs.items():
            logger.info(f"{k} : {v}")

        resp = func(*args, **kwargs)    # 执行真正的请求

        logger.info(f"status_code: {resp.status_code}")
        logger.info(f"返回值:\n {resp.text}")
        return resp

    return wrapper
```

装饰器就是：把函数包一层。原函数执行前后自动插日志。

你看 HttpRequest 里每个方法上都有 `@log`：
```python
@log
def post(self, url, **kwargs):
    ...
```
每次调 `post()`，装饰器自动记录请求参数 → 执行请求 → 记录响应。不用你手动写 print。

**第 4 步：用日期时间生成日志文件名**
```python
from datetime import datetime
log_file = f'log/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}-log.log'
logger = Logger(log_file=log_file)
```

---

## 三、你在项目中要做的

| 步骤 | 做什么 | 在哪里 |
|------|--------|--------|
| 1 | `pip install loguru` | 终端 |
| 2 | 在 `Src/utils/` 下新建 `logger.py` | 参考上面「二、Logger」 |
| 3 | 在 `Src/utils/` 下新建 `httprequest.py` | 参考上面「一、HttpRequest」 |
| 4 | 在 `test_login_param.py` 里导入并替换 | `from Src.util.httprequest import http_request` |
| 5 | 把所有 `print()` 换成 `logger.info()` | 整个项目搜索 `print` |

### 关键点

- HttpRequest 的 `request()` 方法参数和 `requests.request()` 完全一样（`method, url, **kwargs`）。YAML 里的 `**data["request"]` 解包后自动对应。
- Logger 装饰器 `@log` 挂在 HttpRequest 的每个方法上。你调用时自动打日志，不用写一行 print。
- 日志文件自动生成在 `log/` 目录下。

---

开始写。写完了跑 `pytest Src/case/test_login_param.py -v`，9 passed 就继续。
