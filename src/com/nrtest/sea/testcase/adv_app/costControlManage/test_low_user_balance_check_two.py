# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_low_user_balance_check_one.py
@time: 2018/8/10 0010 11:03
@desc:
"""
from unittest import TestCase

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.adv_app.costControlManage.lowUserBalancecheck_para import LowUserBalanceCheck_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.locators.adv_app.costControlManage.lowUserMoneyCheck_locators import BalanceCheckLocator
from com.nrtest.sea.task.feiMange import *


# 高级应用--》费控管理--》本地费控--》抵押用户余额查看
class TestBalanceCheck(TestCase, BalanceCheck_page):
    @classmethod
    def setUpClass(cls):
        cls.driver = low_user_money_check_two()
        cls.orl = Oracle()

    @classmethod
    def tearDownClass(cls):
        # 关闭菜单
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
        # self.clear_values(BalanceCheck_page)

    # 指定时间区域
    def firstOne(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                LowUserBalanceCheck_para.para_test_work_order)
        self.inputStr_receive_date(lip[0][1])
        self.inputStr_end_date(lip[0][2])

    # 数据工单编号
    @BeautifulReport.add_test_img()
    def test_work_order(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                LowUserBalanceCheck_para.para_test_work_order)
        self.inputStr_work_order(lip[0][0])
        self.inputStr_receive_date(lip[0][1])
        self.inputStr_end_date(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 用户编号
    @BeautifulReport.add_test_img()
    def test_user_order(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                LowUserBalanceCheck_para.para_test_user_order)
        self.inputStr_user_order(lip[0][0])
        self.firstOne()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 终端地址
    @BeautifulReport.add_test_img()
    def test_terminal_addr(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_terminal_addr)
        self.inputStr_terminal_addr(lip[0][0])
        self.firstOne()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 电表地址
    @BeautifulReport.add_test_img()
    def test_ele_meter_addr(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_ele_meter_addr)
        self.inputStr_meter_addr(lip[0][0])
        self.firstOne()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 抄表段号
    @BeautifulReport.add_test_img()
    def test_meter_reading_number(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_meter_reading_number)
        self.inputStr_meter_reading_number(lip[0][0])
        self.firstOne()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 用户名称
    @BeautifulReport.add_test_img()
    def test_BalanceCheck_user_name(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_BalanceCheck_user_name)
        self.inputStr_user_name(lip[0][0])
        self.firstOne()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 电表局编号
    @BeautifulReport.add_test_img()
    def test_ele_meter_bureea_order(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_ele_meter_bureea_order)
        self.inputStr_ele_meter_bureea_order(lip[0][0])
        self.firstOne()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 时间查询
    @BeautifulReport.add_test_img()
    def test_date(self):
        self.firstOne()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)

    # 执行状态
    @BeautifulReport.add_test_img()
    def test_execute_state(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_execute_state)
        self.firstOne()
        self.inputRSel_execute_state(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BalanceCheckLocator.TAB_ONE)
        self.assertTrue(result)
