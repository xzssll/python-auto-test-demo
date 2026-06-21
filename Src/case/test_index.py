import requests
from jsonpath import jsonpath as jp

class TestIndex:
    def test_get_tacklists(self,get_token):
        """
            获取任务列表
        """
        url = "http://www.liuyanzu.tech/task/server/api/get/tasklist/1/10"  
        header = {"token":get_token}
        data = {"sorttype":"money"}
        print(get_token)
        resp = requests.request(method="post",url=url,json=data,headers=header)
        # print(resp)
        assert jp(resp.json(), '$.status')[0] == 200
        assert jp(resp.json(), '$.msg')[0] == "操作成功！"

    def test_get_tacklists_error01(self,get_token):
        """
            获取任务列表
        """
        url = "http://www.liuyanzu.tech/task/server/api/get/tasklist/10000/10"  
        header = {"token":get_token}
        data = {"sorttype":"money"}
        # print(get_token)
        resp = requests.request(method="post",url=url,json=data,headers=header)
        # print(resp.json())
        assert jp(resp.json(), '$.status')[0] == 401
        assert jp(resp.json(), '$.msg')[0] == "当前查询没有数据"