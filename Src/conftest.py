import json
import pytest
import requests
import responses
from unittest.mock import patch
from jsonpath import jsonpath as jp


@pytest.fixture(scope='session', params=[{"phone": "19912341110", "code": "857850"}], ids=["getToken_success"])
def get_token(request):
    url = "http://www.liuyanzu.tech/task/server/api/phone/login"
    data = request.param
    resp = requests.request(method="post", url=url, json=data)
    token = jp(resp.json(), '$..token')[0]
    return token


def _login_callback(request):
    """根据请求体中的code返回成功或失败响应"""
    body = json.loads(request.body) if request.body else {}
    code = body.get("code", "")
    if code == "857850":
        return (200, {}, json.dumps({
            "data": {
                "id": 195967, "nickname": "19912341110",
                "phone": "19912341110", "status": "1",
                "token": "a7640019e8ab6c7b7c93b4101114321991da8eb3e3d6c1cff6a",
                "username": "19912341110"
            },
            "msg": "登陆成功",
            "status": 200
        }))
    else:
        return (200, {}, json.dumps({
            "msg": "验证码不正确",
            "status": 401
        }))


@pytest.fixture
def mock_api():
    with responses.RequestsMock() as rsps:
        rsps.add_callback(
            responses.POST,
            "http://www.liuyanzu.tech/task/server/api/phone/login",
            callback=_login_callback
        )
        yield rsps


@pytest.fixture
def mock_db():
    with patch('Src.utils.mysql_client.MysqlClient.query') as mq:
        mq.return_value = [("19912341110",)]
        yield mq