# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_localFeiManageExeCount_dis_count.py
@time: 2018/8/22 0022 15:59
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.costControlManage_data import CostControlManage_data
from com.nrtest.sea.pages.adv_app.costControlManage.localFeiManageExeCount_page import \
    LocalFeiManageExeCount_dis_count_Page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用--》费控管理--》本地费控--》本地费控执行统计:费控情况统计
@ddt
class TestlocalFeiManageExeCount_dis_count(TestCase, LocalFeiManageExeCount_dis_count_Page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(CostControlManage_data.localFeiManageExeCount_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(CostControlManage_data.localFeiManageExeCount_tab_stats)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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

    def query(self, para):
        # 工单类型
        self.inputSel_app_type(para['APP_TYPE'])
        # 费控用户类型
        self.inputSel_fee_ctrl_type(para['FEE_CTRL_TYPE'])

        self.inputDt_receive_time(para['RECEIVE_TIME'])
        self.inputDt_end_time(para['END_TIME'])
        self.btn_qry()

    # # 工单总数明细
    # def test_lfdc_workAll_detail(self):
    #     self.commonTime()
    #     # 点击查询
    #     self.btn_qry()
    #     self.sleep_time(1)
    #     self.btn_work_all()
    #
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(
    #         *LocalFeiManageExeCount_dis_count_Locators.BTN_LOCAL_FEI_MANGE_EXE_COUNT)
    #     self.assertTrue(result)
    #     self.btn_localFeiMangeexeCount()
    #
    # # 执行成功工单总数明细
    # def test_lfdc_workSuccessAll_detail(self):
    #     self.commonTime()
    #     # 点击查询
    #     self.btn_qry()
    #     self.sleep_time(1)
    #     self.btn_work_success_all()
    #
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(
    #         *LocalFeiManageExeCount_dis_count_Locators.BTN_LOCAL_FEI_MANGE_EXE_COUNT)
    #     self.assertTrue(result)
    #     self.btn_localFeiMangeexeCount()
    #
    #     # 执行失败工单总数明细
    #
    # def test_lfdc_workfailAll_detail(self):
    #     self.commonTime()
    #     # 点击查询
    #     self.btn_qry()
    #     self.sleep_time(1)
    #     self.btn_work_fail_all()
    #
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(
    #         *LocalFeiManageExeCount_dis_count_Locators.BTN_LOCAL_FEI_MANGE_EXE_COUNT)
    #     self.assertTrue(result)
    #     self.btn_localFeiMangeexeCount()

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
    @data(*DataAccess.getCaseData(CostControlManage_data.localFeiManageExeCount_para, CostControlManage_data.localFeiManageExeCount_tab_stats))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CostControlManage_data.localFeiManageExeCount_para, CostControlManage_data.localFeiManageExeCount_tab_stats,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
