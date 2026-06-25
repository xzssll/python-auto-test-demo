import pytest
import requests
import os
import sys
from jsonpath import jsonpath as jp

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_path)

# from conf.mysql import query
from Src.utils.validator import Validator
from Src.utils.yamloader import Yamloader
from Src.utils.handle_data import replace_dynamic_params
from Src.utils.mysql_client import MysqlClient

class TestLogin:
    # datas = [
    #     {
    #         "name":"登录成功",
    #         "request":{
    #             "url" : "http://www.liuyanzu.tech/task/server/api/phone/login",
    #             "json" : {"phone":"19912341110","code":"857850"},
    #             "headers" : {},
    #             "method" : "post",
                
    #         },
    #         "validate":[
    #             {"eq":["$.status",200]},
    #             {"eq":["$.data.status",'1']},
    #             {"eq":["$..msg","登陆成功"]},
    #             {"eq":["select phone,status from tb_user where phone = '19912341110' ","19912341110"]}
    #         ]

    #     },

    #     {
    #         "name":"验证码错误，登录失败",
    #         "request":{
    #             "url" : "http://www.liuyanzu.tech/task/server/api/phone/login",
    #             "json" : {"phone":"19912341110","code":"85785 "},
    #             "headers" : {},
    #             "method" : "post",
                
    #         },
    #         "validate":[
    #             {"eq":["$.status",401]},
    #             {"eq":["$..msg","验证码不正确"]},
    #             {"eq":["select phone,status from tb_user where phone = '19912341110' ","19912341110"]}
    #         ]

    #     }
        
    # ]

    # @pytest.mark.parametrize("data",datas)
    # def test_login(self,data):
    #     resp = requests.request(**data["request"])
    #     for check_items in data["validate"]:
    #         for  k,v in check_items.items():
    #             print(k,v)
    #             if "eq" == k:
    #                 if "$." in v[0]:
    #                     assert jp(resp.json(),v[0])[0] == v[1]
    #                 elif v[0].startswith("select"):
    #                     # 数据库校验
    #                     pass
    
    file_path = os.path.join(os.path.dirname(__file__), "../../data/new_test_login.yaml")
    datas = Yamloader().yamloader(file_path)["login"]
    # @pytest.mark.parametrize("data",datas)
    # def test_login(self,data):
    #     replace_phone = jp(data,'$..phone')[0]
    #     new_data = replace_dynamic_params(data,{"phone":replace_phone})
    #     resp = requests.request(**new_data["request"])
    #     Validator().validate(new_data,resp)
    #     print("======数据库校验======")
    #     if "sql" in new_data:
    #         target_sql = jp(new_data,'$..sql')[0]
    #         assert len(MysqlClient.query(target_sql)) ==1,f"数据库未查到手机号为 {replace_phone} 的数据，或查出多条！"
    #         assert (MysqlClient.query(target_sql))[0][0] == replace_phone, f"数据库中不存在phone = {replace_phone}的账号！"
    #     print (f"用例名称===",data["name"])
    # @pytest.mark.parametrize("data",datas)
    # def test_login(self,data):
    #     replace_phone = jp(data,'$..phone')[0]
    #     new_data = replace_dynamic_params(data,{"phone":replace_phone})
    #     resp = requests.request(**new_data["request"])
    #     Validator().validate(new_data,resp)
    #     print (f"用例名称===",new_data["name"])
    @pytest.mark.parametrize("data",datas)
    def test_login(self,data,mock_api,mock_db):
        replace_phone = jp(data,'$..phone')[0]
        new_data = replace_dynamic_params(data,{"phone":replace_phone})
        resp = requests.request(**new_data["request"])
        print(resp.json())
        print(type(resp.json()))
        Validator().validate(new_data,resp)
        print (f"用例名称===",new_data["name"])
