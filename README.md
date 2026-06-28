# Python API Auto Test Demo

## 技术栈
Python 3.12 | pytest 9.x | requests | jsonpath | loguru | YAML 数据驱动
responses (HTTP Mock) | unittest.mock (DB Mock) | Allure 报告

## 项目结构
```
├── Src/case/           测试用例
├── Src/utils/          工具类
│   ├── validator.py    断言器（接口断言 + 数据库断言）
│   ├── httprequest.py  请求层封装（Session 复用）
│   ├── logger.py       日志封装（loguru）
│   ├── yamloader.py    YAML 加载器
│   ├── handle_data.py  动态占位符替换（${phone} → 实际值）
│   └── mysql_client.py 数据库操作
├── data/               YAML 测试数据
├── conf/               配置
├── log/                日志输出
└── conftest.py         fixture + Mock
```

## 运行
```bash
pip install -r requirements.txt
pytest Src/case/ -v
```

## 亮点
- YAML 数据驱动 + 动态占位符替换（${phone} / ${token}）
- HTTP Mock（responses.add_callback 按请求体动态返回）+ DB Mock
- 接口断言 + 数据库断言双重验证
- loguru 日志系统，所有请求链路可追踪
- 10 条用例覆盖正常 / 异常 / 边界 / 安全场景
- Mock 全场景覆盖，不依赖外部环境，CI 随时跑
