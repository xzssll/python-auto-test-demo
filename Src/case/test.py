import pytest
import requests
from jsonpath import search as jp

@pytest.fixture(scope='function',params=[{"phone":"19912341110","code":"857850"},],ids=["getToken_success"])
def get_token(request):
    url = "http://www.liuyanzu.tech/task/server/api/phone/login"
    data = request.param
    resp = requests.request(method="post",url=url,json=data)
    token = jp('$..token',resp.json())[0]
    print(token)
    return token

# 函数直接调用夹具函数
def test_use_token02(get_token):
    # print("也在等待一个token")
    print(f"拿到 Token 了: {get_token}") 