import os
import sys
import pytest
import requests
from jsonpath import jsonpath as jp


project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_path)


from conf.mysql import query
from Src.utils.validator import Validator
from Src.utils.yamloader import Yamloader             
from Src.utils.handle_data import replace_dynamic_params   # pyright: ignore[reportMissingImports]

# 设置文件路径
file_path = os.path.join(os.path.dirname(__file__), "../../data/test_index.yaml")
datas = Yamloader().yamloader(file_path)["index"]

class TestIndex:
    
    @pytest.mark.parametrize("data",datas)
    def test_get_tacklists_success(self,get_token,data):
        """
            获取任务列表
        """
        new_data = replace_dynamic_params(data,{"token": get_token})
        print(new_data)
        resp = requests.request(**new_data["request"])
        # print(resp)
        
        Validator().validate(new_data,resp)
        print (f"用例名称===",new_data["name"])
