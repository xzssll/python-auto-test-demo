import requests
from jsonpath import jsonpath as jp
import sys
import os


project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_path)
from conf.mysql import query


class TestLogin:
    def test_01_login_success(self):
        """
            用户登录成功
        """
        url = "http://www.liuyanzu.tech/task/server/api/phone/login"
        data = {"phone":"19912341110","code":"857850"}
        rep = requests.request(method="post",url=url,json=data)
        print(rep.json())
        # res = query(sql = "select phone,status from tb_user where phone = '19912341110' ")
        # print(rep)
        assert jp(rep.json(), '$.status')[0] == 200
        assert jp(rep.json(), '$.data.status')[0] == '1'
        assert jp(rep.json(), '$..msg')[0] == '登陆成功'
        # assert res[0][0] == '19912341110'
        # assert res[0][1] == '1'
    
    def test_02_login_success(self):
        """
            验证码错误，登录失败
        """
        url = "http://www.liuyanzu.tech/task/server/api/phone/login"
        data = {"phone":"19912341110","code":"85785a"}
        rep = requests.request(method="post",url=url,json=data)
        print(rep.json())
         # res = query(sql = "select phone,status from tb_user where phone = '19912341110' ")
#       print(res)
        assert jp(rep.json(), '$.status')[0] == 401
        assert jp(rep.json(), '$..msg')[0] == '验证码不正确'
        # assert res[0][0] == '19912341110'
        # assert res[0][1] == '1'