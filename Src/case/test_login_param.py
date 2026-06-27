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
from Src.utils.logger import logger
from Src.utils.httprequest import http_request

class TestLogin:
    file_path = os.path.join(os.path.dirname(__file__), "../../data/new_test_login.yaml")
    datas = Yamloader().yamloader(file_path)["login"]

    @pytest.mark.parametrize("data",datas)
    def test_login(self,data,mock_api,mock_db):
        replace_phone = jp(data,'$..phone')[0]
        new_data = replace_dynamic_params(data,{"phone":replace_phone})
        resp = http_request.request(**new_data["request"])
        logger.info(f"****开始断言****")
        Validator().validate(new_data,resp)
        logger.info(f"用例名称==={new_data['name']}执行成功\n<end>")