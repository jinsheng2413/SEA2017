# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gt.py
@time: 2018/6/5 0005 10:34
@desc:
"""
import os
from unittest import defaultTestLoader

from com.nrtest.common import global_drv
# from BeautifulReport import BeautifulReport
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.setting import Setting


def add_case(case_path=r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\base_app\terminalMan\softwareUpgrading', rule='test_*.py'):
    if len(case_path) == 0:
        case_path = os.path.dirname(os.path.realpath(__file__))
    # 加载所有的测试用例
    discover = defaultTestLoader.discover(case_path,
                                          pattern=rule,
                                          top_level_dir=None)
    return discover


# @threads(2)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试deafult报告')


if __name__ == '__main__':
    global_drv.__init()

    # 如果group_user为admin则全量刷新用例
    if Setting.GROUP_USER == 'admin':
        DataAccess.refresh_case()

    # 用例集合
    cases = add_case()
    run(cases)
    global_drv.quit()

    # # 用例集合
    # test_suite = add_case()
    # for case in test_suite:
    #     run(case)
