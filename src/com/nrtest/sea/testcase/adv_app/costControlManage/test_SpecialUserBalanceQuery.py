# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_SpecialUserBalanceQuery.py
@time: 2018/8/19 0019 9:26
@desc:
'''

import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.adv_app.costControlManage.specialUserBalanceQuery_para import SpecialUserBalanceQuery_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.locators.adv_app.costControlManage.specialUserBalanceQuery_locators import \
    SpecialUserBalanceQuery_locators
from com.nrtest.sea.pages.adv_app.costControlManage.specialUserBalanceQuery_page import SpecialUserBalanceQueryPage
from com.nrtest.sea.task.feiMange import *


# 高级应用--》费控管理--》本地费控--》专变用户余额查询
class TestSpecialUserBalanceQuery(unittest.TestCase, SpecialUserBalanceQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = specialUserBalanceQuery()
        cls.orl = Oracle()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.driver.quit()

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

        # self.sleep_time(2000)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.clear_values(SpecialUserBalanceQueryPage)

    def commonTime(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, SpecialUserBalanceQuery_para.para_test_subq_user_num)
        self.inputStr_call_test_date(lip[0][1])

    # 用户编号
    @BeautifulReport.add_test_img()
    def test_subq_user_num(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, SpecialUserBalanceQuery_para.para_test_subq_user_num)
        self.inputStr_call_test_date(lip[0][1])
        self.inputStr_user_num(lip[0][0])
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*SpecialUserBalanceQuery_locators.TAB_ONE)
        self.assertTrue(result)

    # 用户名称
    @BeautifulReport.add_test_img()
    def test_subq_user_name(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, SpecialUserBalanceQuery_para.para_test_subq_user_name)
        self.commonTime()
        self.inputStr_User_name(lip[0][0])
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*SpecialUserBalanceQuery_locators.TAB_ONE)
        self.assertTrue(result)

    # 终端地址
    @BeautifulReport.add_test_img()
    def test_subq_termianl_addr(self):
        self.commonTime()
        lip = self.orl.queryAll(DataCommon.sql_commom, SpecialUserBalanceQuery_para.para_test_subq_termianl_addr)
        self.inputStr_terminal_addr(lip[0][0])
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*SpecialUserBalanceQuery_locators.TAB_ONE)
        self.assertTrue(result)

    # 时间查询
    @BeautifulReport.add_test_img()
    def test_subq_time_qry(self):
        self.commonTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*SpecialUserBalanceQuery_locators.TAB_ONE)
        self.assertTrue(result)
