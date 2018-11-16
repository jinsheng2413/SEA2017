# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_generalGroupSet.py
@time: 2018/11/12 15:18
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.groupMan.groupMan_data import GroupMan_data
from com.nrtest.sea.pages.run_man.groupMan.generalGroupSet_page import *
from com.nrtest.sea.task.commonMath import *


# 运行管理→群组管理→普通群组设置
@ddt
class TestGeneralGroupSet(unittest.TestCase, GeneralGroupSetPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            GroupMan_data.GeneralGroupSet_para, True)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭菜单页面
        cls.closePages(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        sleep(2)
        self.clickCheckBox('管理群组')
        # 名称
        self.inputStr_name(para['NAME'])
        # 查询日期，开始
        self.inputDt_start_date(para['START_DATE'])
        # 查询日期，结束
        self.inputDt_end_date(para['END_DATE'])
        # 查询按钮
        self.btn_search()
        # 校验
        result = self.assert_context(*GeneralGroupSetLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(GroupMan_data.GeneralGroupSet_para))
    def test_der(self, para):
        self.query(para)