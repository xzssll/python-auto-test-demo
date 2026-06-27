import requests

from Src.utils.logger import log


class HttpRequest:

    def __init__(self):
        """
            初始化函数：初始化session对象
        """
        self.session = requests.session()
    @log
    def get(self, url, **kwargs):
        """
            get方法
        """
        return self.session.request("get", url=url, **kwargs)

    @log
    def post(self, url, **kwargs):
        """
            post方法
        """
        return self.session.request("post", url=url, **kwargs)

    @log
    def put(self, url, **kwargs):
        """
            put方法
        """
        return self.session.request("put", url=url, **kwargs)

    @log
    def request(self, method, url, **kwargs):
        """
            request方法
        """
        return self.session.request(method, url=url, **kwargs)

    def __del__(self):
        """
            析构函数：释放对象
        """
        self.session.close()


http_request = HttpRequest()
