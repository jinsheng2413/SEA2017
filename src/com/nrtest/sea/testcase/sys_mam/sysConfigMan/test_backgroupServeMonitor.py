# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_backgroupServeMonitor.py
@time: 2018/11/20 9:45
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysConfigMan.sysConfigMan_data import SysConfigManData
from com.nrtest.sea.pages.sys_mam.sysConfigMan.backgroupServeMonitor_page import BackgroupServeMonitorPage
from com.nrtest.sea.task.commonMath import *


# 系统管理→系统配置管理→后台服务监测
@ddt
class TestBackgroupServeMonitor(unittest.TestCase, BackgroupServeMonitorPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # # 打开菜单（需要传入对应的菜单编号）
        # cls.driver = openMenu(SysConfigManData.BackgroundServeMonitor_para)
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SysConfigManData.BackgroundServeMonitor_para)
        super(unittest.TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SysConfigManData.BackgroupServeMonitorDetail_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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
        # self.recoverLeftTree()

    def query(self, para):
        sleep(2)
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 运行状态
        self.inputSel_operation_stat(para['OPERATION_STAT'])
        # 查询按钮
        self.btn_search()

    # @BeautifulReport.add_test_img()
    # @data(
    #     *DataAccess.getCaseData(SysConfigManData.BackgroundServeMonitor_para,
    #                             SysConfigManData.BackgroupServeMonitor_tabName))
    # def test_der(self, para):
    #     self.query(para)
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
    @data(*DataAccess.getCaseData(SysConfigManData.BackgroundServeMonitor_para, SysConfigManData.BackgroupServeMonitorDetail_tabName))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SysConfigManData.BackgroundServeMonitor_para, SysConfigManData.BackgroupServeMonitorDetail_tabName, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
