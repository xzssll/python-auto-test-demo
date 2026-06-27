import sys

from loguru import logger as logutil
from datetime import datetime


class Logger:
    def __init__(self, log_file=''):
        self.logger = logutil
        if log_file:
            self.logger.add(log_file, encoding="utf-8", serialize=True)

    def info(self, message, *args, **kwargs):
        """
            info
        """
        self.logger.info(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        """
            debug
        """
        self.logger.debug(message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        """
            success
        """
        self.logger.success(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        """
            error
        """
        self.logger.error(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        """
            critical
        """
        self.logger.critical(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        """
            warning
        """
        self.logger.warning(message, *args, **kwargs)


log_file = f'log/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}-log.log'
# log_file = f"log/{datetime.now()}-log.log"
logger = Logger(log_file=log_file)


def log(func):
    """
    打印日志装饰器
    :param func:
    :return:
    """

    def log_request(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        logger.info("开始测试接口，接口信息如下：")
        for k, v in kwargs.items():
            logger.info(f"{k} : {v}")

        resp = func(*args, **kwargs)

        logger.info(f"status_code: {resp.status_code}")
        logger.info("响应头: ")
        for k, v in resp.headers.items():
            logger.info(f"{k} : {v}")
        logger.info(f"返回值:\n {resp.json()}")

        return resp

    return log_request
