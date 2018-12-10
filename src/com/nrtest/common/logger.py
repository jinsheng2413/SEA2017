# -*- coding: utf-8 -*-

"""
@author: 郭春彪，李建方
@license: (C) Copyright 2018, Nari.
@file: logger.py
@time: 2018-06-04 18:58
@desc:
"""
import logging
import os.path
from logging.handlers import RotatingFileHandler

from com.nrtest.common.parse_nrtest import ParseNrTest
from com.nrtest.common.setting import Setting


class Logger(object):
    def __init__(self, logger):
        """
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        log_name = Setting.LOG_PATH + Setting.PROJECT_NAME + '.log'
        vals = ParseNrTest().getSectionVals('LOG')
        fh = RotatingFileHandler(filename=log_name, mode=vals[0], maxBytes=int(vals[1]), backupCount=int(vals[2]),
                                 encoding=vals[3])
        fh.setLevel(logging.INFO)

        # 创建一个handler，用于控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(name)s - %(funcName)s [line：%(lineno)d]-> %(message)s',
                                      '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    @staticmethod
    def get_module(file):
        dirname = os.path.dirname(os.path.abspath(file))
        return dirname[dirname.find('src') + 4:] + Setting.PATTERN[0]

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    logger = Logger(Logger.get_module(__file__)).getlog()
    logger.error('日志测试!!')
    # def __init__(self):
    #     self.logger = Logger(Logger.get_module(__file__)).getlog()
    logger.debug('\031This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')
    print("\033[1;36;m", "*** 蓝字")
    print("\033[0m", "*** 默认")
    print("\033[1;31;m", "*** 红字!")
