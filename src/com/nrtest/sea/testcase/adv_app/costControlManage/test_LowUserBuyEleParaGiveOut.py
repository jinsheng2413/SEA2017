# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_elePricePara.py
@time: 2018/8/16 0016 8:55
@desc:
"""
import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.adv_app.costControlManage.lowUserBuyEleParaGiveOut_para import lowUserBuyEleParaGiveOut_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.locators.adv_app.costControlManage.lowUserBuyEleParaGiveOut_locators import \
    LowUserBuyEleParaGiveOutLocators
from com.nrtest.sea.pages.adv_app.costControlManage.lowUserBuyEleParaGiveOut_page import LowUserBuyEleParaGiveOut_page
from com.nrtest.sea.task.feiMange import *


# 高级应用--》费控管理--》本地费控--》低压用户购电参数下发
class TestLowUserBuyEleParaGiveOut(unittest.TestCase, LowUserBuyEleParaGiveOut_page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = lowUserBuyParaGiveOut()
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
        self.clear_values(LowUserBuyEleParaGiveOut_page)

    def commomTime(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, lowUserBuyEleParaGiveOut_para.para_test_epg_workNumber)
        # 输入接收时间
        self.inputStr_receive_time(lip[0][1])
        # 输入结束时间
        self.inputStr_end_time(lip[0][2])

        # 工单编号查询

    @BeautifulReport.add_test_img()
    def test_epg_workNumber(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, lowUserBuyEleParaGiveOut_para.para_test_epg_workNumber)
        # 输入工单编号
        self.inputStr_work_num(lip[0][0])
        # 输入接收时间
        self.inputStr_receive_time(lip[0][1])
        # 输入结束时间
        self.inputStr_end_time(lip[0][2])
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LowUserBuyEleParaGiveOutLocators.TAB_ONE)
        self.assertTrue(result)

    # 用户编号查询
    @BeautifulReport.add_test_img()
    def test_epg_user_number(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, lowUserBuyEleParaGiveOut_para.para_test_epg_user_number)
        # 输入用户编号
        self.inputStr_user_num(lip[0][0])
        self.commomTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LowUserBuyEleParaGiveOutLocators.TAB_ONE)
        self.assertTrue(result)

    # 终端地址查询
    @BeautifulReport.add_test_img()
    def test_epg_terminal_addr(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, lowUserBuyEleParaGiveOut_para.para_test_epg_terminal_addr)
        # 输入终端地址
        self.inputStr_terminal_addr(lip[0][0])
        self.commomTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LowUserBuyEleParaGiveOutLocators.TAB_ONE)
        self.assertTrue(result)

    # 电表地址查询
    @BeautifulReport.add_test_img()
    def test_epg_meter_addr(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, lowUserBuyEleParaGiveOut_para.para_test_epg_meter_addr)
        # 输入电表地址
        self.inputStr_meter_addr(lip[0][0])
        self.commomTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LowUserBuyEleParaGiveOutLocators.TAB_ONE)
        self.assertTrue(result)

    # 抄表段号
    @BeautifulReport.add_test_img()
    def test_epg_meter_reading_number(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, lowUserBuyEleParaGiveOut_para.para_test_epg_meter_reading_number)
        # 输入抄表段号
        self.inputStr_meter_reading_num(lip[0][0])
        self.commomTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LowUserBuyEleParaGiveOutLocators.TAB_ONE)
        self.assertTrue(result)

    # 时间查询
    @BeautifulReport.add_test_img()
    def test_epg_time(self):
        self.commomTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LowUserBuyEleParaGiveOutLocators.TAB_ONE)
        self.assertTrue(result)

    # 执行状态查询
    @BeautifulReport.add_test_img()
    def test_epg_execute_state(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, lowUserBuyEleParaGiveOut_para.para_test_epg_execute_state)
        self.commomTime()
        self.inputSel_execute_state(lip[0][0])
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LowUserBuyEleParaGiveOutLocators.TAB_ONE)
        self.assertTrue(result)
