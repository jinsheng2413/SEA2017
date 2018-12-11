# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_menuUseStat.py
@time: 2018/11/30 11:28
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysUseStat.sysUseStat_data import SysUseStat_date
from com.nrtest.sea.pages.sys_mam.sysUseStat.menuUseStat_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理→系统使用情况统计→菜单使用情况统计
@ddt
class TestMenuUseStat(unittest.TestCase, MenuUseStatPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            SysUseStat_date.menuUseStat_para, True)

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
        self.displayTreeMenu()
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 菜单
        self.inputSel_menu(para['MENU'])
        # 操作员
        self.inputStr_operator(para['OPERATOR'])
        # 查询日期，开始
        self.inputDt_start_date(para['START_DATE'])
        # 查询日期，结束
        self.inputDt_end_date(para['END_DATE'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*MenuUseStatLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(SysUseStat_date.menuUseStat_para, SysUseStat_date.menuUseStat_tabName))
    def test_der(self, para):
        self.query(para)
