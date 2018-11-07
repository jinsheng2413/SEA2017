# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_CustControlCommissioning_ele_manage.py
@time: 2018/8/23 0023 11:20
@desc:
"""
import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.adv_app.costControlManage.custControlCommissioning_para import CcustControlCommissioning_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.pages.adv_app.costControlManage.custControlCommissioning_page import CustControlCommissioning_page
from com.nrtest.sea.task.feiMange import *


class TestCustControlCommissioning_cust_manage(unittest.TestCase, CustControlCommissioning_page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = custControlCommissioning_ele_cust()
        cls.orl = Oracle()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        self.clear_values(CustControlCommissioning_page)

    def commonTime(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, CcustControlCommissioning_para.para_test_cccm_mark_single)
        # 输入开始时间
        self.inputStr_start_date(lip[0][1])
        # 输入结束时间
        self.inputStr_end_date(lip[0][2])

    # 营销单号查询
    @BeautifulReport.add_test_img()
    def test_cccm_mark_single(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, CcustControlCommissioning_para.para_test_cccm_mark_single)
        # 输入营销单号
        self.inputStr_mark_sigle(lip[0][0])
        # 输入开始时间
        self.inputStr_start_date(lip[0][1])
        # 输入结束时间
        self.inputStr_end_date(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CustControlCommissioning_locators.TAB_ONE)
        self.assertTrue(result)

    # 时间查询
    @BeautifulReport.add_test_img()
    def test_cccm_time(self):
        self.commonTime()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CustControlCommissioning_locators.TAB_ONE)
        self.assertTrue(result)

    # 终端地址查询
    @BeautifulReport.add_test_img()
    def test_cccm_terminal_addr(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, CcustControlCommissioning_para.para_test_cccm_terminal_addr)
        # 输入终端地址
        self.inputStr_terminal_addr(lip[0][0])
        self.commonTime()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CustControlCommissioning_locators.TAB_ONE)
        self.assertTrue(result)

    # 用户编号查询
    @BeautifulReport.add_test_img()
    def test_cccm_user_no(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, CcustControlCommissioning_para.para_test_cccm_user_no)
        # 输入用户编号
        self.inputStr_user_num(lip[0][0])
        self.commonTime()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CustControlCommissioning_locators.TAB_ONE)
        self.assertTrue(result)

    # 用户名称查询
    @BeautifulReport.add_test_img()
    def test_cccm_user_name(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, CcustControlCommissioning_para.para_test_cccm_user_name)
        # 输入用户名称
        self.inputStr_user_name(lip[0][0])
        self.commonTime()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CustControlCommissioning_locators.TAB_ONE)
        self.assertTrue(result)

    # 按调试日期
    def test_cccm_commissioning_date(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, CcustControlCommissioning_para.para_test_cccm_commissioning_date)
        # 输入按调试日期
        self.inputRSel_buy_ele_date(lip[0][0])
        self.commonTime()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CustControlCommissioning_locators.TAB_ONE)
        self.assertTrue(result)

    # 下发状态
    def test_cccm_provide_state(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, CcustControlCommissioning_para.para_test_cccm_provide_state)
        # 输入按调试日期
        self.inputSel_provide_state(lip[0][0])
        self.commonTime()
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CustControlCommissioning_locators.TAB_ONE)
        self.assertTrue(result)
