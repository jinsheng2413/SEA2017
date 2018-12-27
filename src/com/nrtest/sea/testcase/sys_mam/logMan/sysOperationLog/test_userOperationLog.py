# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_userOperationLog.py
@time: 2018/11/29 16:28
@desc:
"""

import unittest
from unittest import TestCase
from time import sleep

from com.nrtest.common.BeautifulReport import BeautifulReport
from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.logMan.logMan_data import LogEdit_data
from com.nrtest.sea.pages.sys_mam.logMan.sysOperationLog_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理→日志管理→系统操作日志→用户操作日志
@ddt
class TestUserOperationLog(unittest.TestCase, UserOperationLogPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LogEdit_data.sysOperationLog_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(LogEdit_data.sysOperationLog_tabName_user)
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
        self.recoverLeftTree()

    def query(self, para):
        clickTabPage('用户操作日志')
        # 操作模块
        self.inputSel_operation_tem(para['OPERATION_TEM'])
        # 查询日期，开始
        self.inputDt_start_date(para['START_DATE'])
        # 查询日期，结束
        self.inputDt_end_date(para['END_DATE'])
        # 操作人员
        self.inputStr_operator(para['OPERATOR'])
        # 查询按钮
        self.btn_qry()

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
    @data(*DataAccess.getCaseData(LogEdit_data.sysOperationLog_para, LogEdit_data.sysOperationLog_tabName_user))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LogEdit_data.sysOperationLog_para, LogEdit_data.sysOperationLog_tabName_user, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)