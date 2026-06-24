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
    # body = json.loads(request.body) if request.body else {}
    # code = body.get("code", "")
    # if code == "857850":
    #     return (200, {}, json.dumps({
    #         "data": {
    #             "id": 195967, "nickname": "19912341110",
    #             "phone": "19912341110", "status": "1",
    #             "token": "a7640019e8ab6c7b7c93b4101114321991da8eb3e3d6c1cff6a",
    #             "username": "19912341110"
    #         },
    #         "msg": "登陆成功",
    #         "status": 200
    #     }))
    # else:
    #     return (200, {}, json.dumps({
    #         "msg": "验证码不正确",
    #         "status": 401
    #     }))
    print(type(request))
    print(request.method)
    print("=====================================================================================================")

    # 第一步：method 不是 POST → 不解析 body，直接返回 405
    if request.method.upper() != "POST":
        return (200, {}, json.dumps({
            "msg": "405 Method Not Allowed: The method is not allowed for the requested URL.",
            "status": 401
        }))

    # 第二步：body 是 form-encoded → 不解析 JSON，直接返回错误
    if request.body and str(request.body).startswith("phone="):
        return (200, {}, json.dumps({
            "msg": "服务器异常，请联系管理员",
            "status": 401
        }))

    # 只有 JSON 格式的 POST 请求才会执行到这里
    body = json.loads(request.body)
    if request.method  == "POST" and body.get("code", "") == "857850":
        return (200, {}, json.dumps({
            "data": {
                "id": 195967,
                "nickname": "19912341110",
                "phone": "19912341110",
                "status": "1",
                "token": "a7640019e8ab6c7b7c93b4101114321991da8eb3e3d6c1cff6a",
                "username": "19912341110"
            },
            "msg": "登陆成功",
            "status": 200
        }))
    
    elif body.get("code") == None:
        return (200, {}, json.dumps({
            'data': None,
            'msg': '参数不对',
            'status': 401
        }))
    
    elif request.method == "POST" and body.get("code", "") != "857850":
        return (200, {}, json.dumps({
            "msg": "验证码不正确",
            "status": 401
        }))
    elif request.headers.get('Content-Type')  == "text/plain":
        return (200, {}, json.dumps({
            'data': None,
            'msg': '服务器异常，请联系管理员',
            'status': 401
        }))
    
    elif request.method != "POST":
        return (200, {}, json.dumps({
            'data': None,
            'msg': '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.',
            'status': 401
        }))


@pytest.fixture
def mock_api():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add_callback(
            responses.POST,
            "http://www.liuyanzu.tech/task/server/api/phone/login",
            callback=_login_callback
        )
        rsps.add_callback(
            responses.GET,
            "http://www.liuyanzu.tech/task/server/api/phone/login",
            callback=_login_callback
        )
        rsps.add_callback(
            responses.PUT,
            "http://www.liuyanzu.tech/task/server/api/phone/login",
            callback=_login_callback
        )
        rsps.add_callback(
            responses.DELETE,
            "http://www.liuyanzu.tech/task/server/api/phone/login",
            callback=_login_callback
        )
        yield rsps


@pytest.fixture
def mock_db():
    with patch('Src.utils.mysql_client.MysqlClient.query') as mq:
        mq.return_value = [("19912341110",)]
        yield mq