# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_localFeiManageExeCount_dis_count.py
@time: 2018/8/22 0022 15:59
@desc:
"""
import unittest

from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.adv_app.costControlManage.localFeiManageExeCount_para import LocalFeiManageExeCount_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.locators.adv_app.costControlManage.localFeiManageExeCount_Locators import \
    LocalFeiManageExeCount_dis_count_Locators
from com.nrtest.sea.pages.adv_app.costControlManage.localFeiManageExeCount_page import \
    LocalFeiManageExeCount_dis_count_Page
from com.nrtest.sea.task.feiMange import *


# 高级应用--》费控管理--》本地费控--》本地费控执行统计
class TestlocalFeiManageExeCount_dis_count(unittest.TestCase, LocalFeiManageExeCount_dis_count_Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = localFeiManageCount_dis_count()
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

        # self.sleep_time(2000)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # self.clear_values(LocalFeiManageExeCount_dis_count_Page)

    def commonTime(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LocalFeiManageExeCount_para.para_test_lfdc_feiUserCata)
        self.inputStr_receive_time(lip[0][1])
        self.inputStr_end_time(lip[0][2])

    # 费控用户类型
    def test_lfdc_feiUserCata(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LocalFeiManageExeCount_para.para_test_lfdc_feiUserCata)
        self.inputSel_feiUserCata(lip[0][0])
        self.inputStr_receive_time(lip[0][1])
        self.inputStr_end_time(lip[0][2])
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(
            *LocalFeiManageExeCount_dis_count_Locators.TAB_ONE)
        self.assertTrue(result)

    # 工单类型
    def test_lfdc_workCata(self):
        lip = self.orl.queryAll(
            DataCommon.sql_commom, LocalFeiManageExeCount_para.para_test_lfdc_workCata)
        self.commonTime()
        self.inputSel_work_cata(lip[0][0])
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(
            *LocalFeiManageExeCount_dis_count_Locators.TAB_ONE)
        self.assertTrue(result)

    # 时间查询
    def test_lfdc_time(self):
        self.commonTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(
            *LocalFeiManageExeCount_dis_count_Locators.TAB_ONE)
        self.assertTrue(result)

    # 工单总数明细
    def test_lfdc_workAll_detail(self):
        self.commonTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(1)
        self.btn_work_all()

        self.sleep_time(2)
        # 校验
        result = self.assert_context(
            *LocalFeiManageExeCount_dis_count_Locators.BTN_LOCAL_FEI_MANGE_EXE_COUNT)
        self.assertTrue(result)
        self.btn_localFeiMangeexeCount()

    # 执行成功工单总数明细
    def test_lfdc_workSuccessAll_detail(self):
        self.commonTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(1)
        self.btn_work_success_all()

        self.sleep_time(2)
        # 校验
        result = self.assert_context(
            *LocalFeiManageExeCount_dis_count_Locators.BTN_LOCAL_FEI_MANGE_EXE_COUNT)
        self.assertTrue(result)
        self.btn_localFeiMangeexeCount()

        # 执行失败工单总数明细

    def test_lfdc_workfailAll_detail(self):
        self.commonTime()
        # 点击查询
        self.btn_qry()
        self.sleep_time(1)
        self.btn_work_fail_all()

        self.sleep_time(2)
        # 校验
        result = self.assert_context(
            *LocalFeiManageExeCount_dis_count_Locators.BTN_LOCAL_FEI_MANGE_EXE_COUNT)
        self.assertTrue(result)
        self.btn_localFeiMangeexeCount()
