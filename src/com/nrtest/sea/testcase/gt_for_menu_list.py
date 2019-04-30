# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: gt_for_menu_list.py
@time: 2019-01-31 23:34
@desc:
"""
import sys

sys.path.append(__file__.split('/com')[0])

from unittest import TestSuite, TestLoader

from com.nrtest.common import global_drv
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.setting import Setting
from com.nrtest.common.utils import Utils

def add_case():
    # 测试用例清单，带package的类文件路径（以“.”分割）
    # 格式[推荐]：com/nrtest/sea/testcase/gt_for_menu_list.py
    # 格式：com.nrtest.sea.testcase.gt_for_menu_list

    menu_path_list = DataAccess.load_tests_ByMenuList()
    loader = TestLoader()
    test_suite = TestSuite()
    for menu_path in menu_path_list:
        # 要加载的testCase类列表，即每个菜单的Class名
        # suite.addTests(loader.loadTestsFromTestCase(test_class))
        # file_path格式：com/nrtest/sea/testcase/gt_for_menu_list.py
        try:
            module = Utils.map_module_by_file_path(menu_path[0])
            test_suite.addTests(loader.loadTestsFromModule(module))
        except Exception as ex:
            print('加载test模块失败：\r')
            print(menu_path[0] + '\r')
            print(ex.__str__())
    return test_suite


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
    test_suite = add_case()
    run(test_suite)
    # for case in test_suite:
    #     run(case)
    global_drv.quit()
