# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gt.py
@time: 2018/6/5 0005 10:34
@desc:
"""
import os
import unittest
from BeautifulReport import BeautifulReport

# from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common import global_drv
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.setting import Setting


def add_case(case_path='', rule='test*.py'):
    if len(case_path) == 0:
        case_path = os.path.dirname(os.path.realpath(__file__))
    # 加载所有的测试用例
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


# @threads(2)
def run(test_suit):
    result = BeautifulReport(test_suit)
    # , log_path=Setting.REPORT_PATH)
    result.report(filename='report.html', description='测试deafult报告')


if __name__ == '__main__':
    global_drv.__init()

    # 如果group_user为admin则全量刷新用例
    if Setting.GROUP_USER == 'admin':
        DataAccess.refresh_case()

    # 用例集合
    # curpath = 'D:\pythonworkspace\SEA2017\src\com/nrtest\sea/testcase/adv_app\dataRecover'
    cases = add_case()

    # print(cases)
    # for case in cases:
    #     print(case)
    #     run(case)
    run(cases)
    global_drv.quit()

    #
