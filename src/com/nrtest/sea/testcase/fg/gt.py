# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gt.py
@time: 2018/6/5 0005 10:34
@desc:
'''
import os
import unittest

from BeautifulReport import BeautifulReport

curpath = os.path.dirname(os.path.realpath(__file__))


def add_case(case_path='D:/pythonworkspace/SEA2017/src/com/nrtest/sea/exp/', rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,

                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report_old_model.html', description='测试deafult报告',
                  log_path='D:/pythonworkspace/SEA2017/reports/')


if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    run(cases)
