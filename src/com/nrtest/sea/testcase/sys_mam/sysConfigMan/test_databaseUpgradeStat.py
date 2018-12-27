# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_databaseUpgradeStat.py
@time: 2018/11/15 15:51
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysConfigMan.sysConfigMan_data import SysConfigManData
from com.nrtest.sea.pages.sys_mam.sysConfigMan.databaseUpgradeStat_page import DatabaseUpgradeStatPage, \
    DatabaseUpgradeStatLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→系统配置管理→数据库升级情况
@ddt
class TestDatabaseUpgradeStat(unittest.TestCase, DatabaseUpgradeStatPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SysConfigManData.DatabaseUpgradeStat_para)
        sleep(2)
        cls.exec_script(cls, DatabaseUpgradeStatLocators.DATE_JS)

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
        # 注册菜单
        self.menu_name = para['MENU_NAME']
        # 升级日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_query()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(self.check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SysConfigManData.DatabaseUpgradeStat_para))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SysConfigManData.DatabaseUpgradeStat_para))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
