# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_costContolManage.py
@time: 2018/8/2 0002 21:25
@desc:
"""
import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.adv_app.costControlManage.costControlManage_para import CostControlManage_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.locators.adv_app.costControlManage.costControlManage_page_locators import \
    CostControlManagePageLocators
from com.nrtest.sea.task.feiMange import *


# 高级应用--》费控管理--》本地费控--》专变用户费控管理
class TestCostControlManage(unittest.TestCase, CostControlManagePage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = specil_user_fei_mange()
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
        self.clear_values(CostControlManagePage)

    # 营销单号查询
    @BeautifulReport.add_test_img()
    def test_mark_single(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                CostControlManage_para.para_test_mark_single)
        # 输入营销单号
        self.inputStr_mark_sigle(lip[0][0])
        # 输入开始时间
        self.input_start_date(lip[0][1])
        # 输入结束时间
        self.input_end_date(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CostControlManagePageLocators.TAB_ONE)
        self.assertTrue(result)

    # 用户编号查询
    @BeautifulReport.add_test_img()
    def test_user_no(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                CostControlManage_para.para_test_user_no)
        # 输入
        self.inputStr_user_num(lip[0][0])
        # 输入开始时间
        self.input_start_date(lip[0][1])
        # 输入结束时间
        self.input_end_date(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CostControlManagePageLocators.TAB_ONE)
        self.assertTrue(result)

    # 用户名称查询
    @BeautifulReport.add_test_img()
    def test_user_name(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                CostControlManage_para.para_test_user_name)
        # 输入
        self.inputStr_user_name(lip[0][0])
        # 输入开始时间
        self.input_start_date(lip[0][1])
        # 输入结束时间
        self.input_end_date(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CostControlManagePageLocators.TAB_ONE)
        self.assertTrue(result)

    # 时间查询
    @BeautifulReport.add_test_img()
    def test_date(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                CostControlManage_para.para_test_date)
        # 输入开始时间
        self.input_start_date(lip[0][0])
        # 输入结束时间
        self.input_end_date(lip[0][1])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CostControlManagePageLocators.TAB_ONE)
        self.assertTrue(result)

    # 业务类型查询
    @BeautifulReport.add_test_img()
    def test_buiness_cata(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                CostControlManage_para.para_test_buiness_cata)
        self.inputSel_buniess_cata(lip[0][0])
        # 输入开始时间
        self.input_start_date(lip[0][1])
        # 输入结束时间
        self.input_end_date(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CostControlManagePageLocators.TAB_ONE)
        self.assertTrue(result)

    # 参数下发状态查询
    @BeautifulReport.add_test_img()
    def test_para_lower_hair(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, CostControlManage_para.para_test_para_lower_hair)
        self.inputSel_para_deve(lip[0][0])
        # 输入开始时间
        self.input_start_date(lip[0][1])
        # 输入结束时间
        self.input_end_date(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CostControlManagePageLocators.TAB_ONE)
        self.assertTrue(result)
