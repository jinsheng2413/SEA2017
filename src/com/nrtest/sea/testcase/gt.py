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
from tomorrow import threads
from BeautifulReport import BeautifulReport
from com.nrtest.common.setting import Setting
from com.nrtest.common import global_drv
#curpath = os.path.dirname(os.path.realpath(__file__))
curpath = 'D:\pythonworkspace\SEA2017\src\com/nrtest\sea/testcase/adv_app\dataRecover'


def add_case(case_path=curpath, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,

                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

@threads(2)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试deafult报告', log_path=Setting.REPORT_PATH)

if __name__ == "__main__":
    global_drv.__init()
    # 用例集合
    cases = add_case()

    print(cases)
    for i in cases:
        print(i)
        run(i)
    global_drv.quit()
    #