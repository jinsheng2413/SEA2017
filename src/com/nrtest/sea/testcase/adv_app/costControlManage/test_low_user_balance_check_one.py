# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_low_user_balance_check_one.py
@time: 2018/8/10 0010 11:03
@desc:
'''
import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.adv_app.costControlManage.lowUserBalancecheck_para import LowUserBalanceCheck_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.locators.adv_app.costControlManage.lowUserMoneyCheck_locators import BalanceCountLocator
from com.nrtest.sea.pages.adv_app.costControlManage.lowUserMoneyCheck_Page import BalanceCount_page
from com.nrtest.sea.task.feiMange import *


# 高级应用--》费控管理--》本地费控--》专变用户费控管理
class TestBalanceCount(unittest.TestCase, BalanceCount_page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = low_user_money_check()
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

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.clear_values(BalanceCount_page)

    # 查询出第一个数据
    def firstone(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_data_date)
        self.inputStr_data_date(lip[0][0])
        self.btn_qry()

    # 数据日期查询
    @BeautifulReport.add_test_img()
    def test_data_date(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, LowUserBalanceCheck_para.para_test_data_date)
        self.inputStr_data_date(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*BalanceCountLocator.TAB_ONE)
        self.assertTrue(result)

    # 供电单位明细
    @BeautifulReport.add_test_img()
    def test_ele_company_detail(self):
        self.firstone()
        self.btn_ele_company()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*BalanceCountLocator.BAL_CHECK)
        self.assertTrue(result)
        self.btn_balance_count()

    # 10元内用户总数
    @BeautifulReport.add_test_img()
    def test_ten_user_all_detail(self):
        self.firstone()
        self.btn_tab_one_ten_user_all()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*BalanceCountLocator.BAL_CHECK)
        self.assertTrue(result)
        self.btn_balance_count()

    # 50元内用户总数
    @BeautifulReport.add_test_img()
    def test_fifty_user_all_detail(self):
        self.firstone()
        self.btn_tab_one_fifty_user_all()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*BalanceCountLocator.BAL_CHECK)
        self.assertTrue(result)
        self.btn_balance_count()

    # 超50元内用户总数
    @BeautifulReport.add_test_img()
    def test_more_fifty_user_all_detail(self):
        self.firstone()
        self.btn_tab_one_more_fifty_user_all()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*BalanceCountLocator.BAL_CHECK)
        self.assertTrue(result)
        self.btn_balance_count()
