import pytest
import requests
import traceback
from jsonpath import jsonpath as jp
from Src.utils.mysql_client import MysqlClient

class Validator:
    """
        封装结果校验函数
    """

    # def validate(self,data,resp):
    #     try:
    #         for check_items in data["validate"]:
    #             for  k,v in check_items.items():
    #                 if "eq" == k:
    #                     if "$." in v[0]:
    #                         assert jp(resp.json(),v[0])[0] == v[1]  
    #                     elif v[0].startswith("select"):
    #                         # 数据库校验
    #                         pass
    #                 if "nq" == k:
    #                     if "$." in v[0]:
    #                         assert jp(resp.json(),v[0])[0] != v[1]
    #                     elif v[0].startswith("select"):
    #                         # 数据库校验
    #                         pass
    #                 if "in" == k:
    #                     if "$." in v[0]:
    #                         assert jp(resp.json(),v[0])[0] in v[1]
    #                     elif v[0].startswith("select"):
    #                         # 数据库校验
    #                         pass
    #                 if "nn" == k:
    #                     if "$." in v[0]:
    #                         assert jp(resp.json(),v[0])[0] is not v[1]
    #                     elif v[0].startswith("select"):
    #                         # 数据库校验
    #                         pass

    #     except Exception as e:
    #         traceback.print_exc()
    #         raise e 
    #     return True

    @classmethod
    def eq(cls,r1,r2):
        return r1 == r2
    
    @classmethod
    def nq(cls,r1,r2):
        return r1 != r2
    
    @classmethod
    def iin(cls,r1,r2):
        return r1 in r2
    @classmethod
    def nni(cls,r1,r2):
        return r1 not in r2

    # 字典映射
    rule_map = {
        "eq":"self.eq",
        "nq":"self.nq",
        "iin":"self,iin",
        "nni":"self.nni"

    }

    def validate(self,data,resp):
        try:
            for check_items in data["validate"]:
                for  k,v in check_items.items():
                    # if "$." in v[0]:
                    #     assert getattr(Validator,k)(jp(resp.json(), v[0])[0],v[1])
                    # elif v[0].startswith("select"):
                    #      # 数据库校验
                    #     pass
                    if "$." in v[0]:
                        # 判断数据有没有正常获取
                        assert getattr(Validator,k)(jp(resp.json(), v[0])[0],v[1])
                        print("===响应数据校验通过===")
                    elif v[0].startswith("select"):
                        #  数据库校验
                        db_res = MysqlClient.query(v[0])
                        assert getattr(Validator,k)(len(db_res),v[1]),f"数据库未查到手机号为 {jp(data, '$..phone')[0]} 的数据，或查出多条！"
                        assert getattr(Validator,k)(db_res[0][0],v[2]),f"数据库中不存在phone = {jp(data, '$..phone')[0]}的账号！"
                        print("===数据库校验通过===")
        except Exception as e:
            traceback.print_exc()
            raise e 
        return True