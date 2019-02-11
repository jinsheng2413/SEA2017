# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_LowUserBuyEleParaGiveOut.py
@time: 2018/8/16 0016 8:55
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.costControlManage_data import CostControlManage_data
from com.nrtest.sea.pages.adv_app.costControlManage.lowUserBuyEleParaGiveOut_page import LowUserBuyEleParaGiveOut_page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→费控管理→本地费控→低压用户购电参数下发
@ddt
class TestLowUserBuyEleParaGiveOut(TestCase, LowUserBuyEleParaGiveOut_page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(CostControlManage_data.lowUserBuyEleParaGiveOut_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(CostControlManage_data.tmnlInstallDetail_tabOne)
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

    def tearDown(self):
        """
        :return:
        """
        self.recoverLeftTree()

    def query(self, para):
        self.openLeftTree(para['TREE_NODE'])

        # 工单编号
        self.inputStr_app_no(para['APP_NO'])

        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])

        # 终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 电表地址
        self.inputStr_meter_addr(para['METER_ADDR'])

        # 抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])

        # 执行状态查询
        self.inputSel_execute_status(para['EXECUTE_STATUS'])

        # 开始时间
        self.inputDt_start_time(para['START_TIME'])

        # 结束时间
        self.inputDt_end_time(para['END_TIME'])

        # 查询
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
    @data(*DataAccess.getCaseData(CostControlManage_data.lowUserBuyEleParaGiveOut_para))
    def test_query(self, para):
        """高级应用→费控管理→本地费控→低压用户购电参数下发

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CostControlManage_data.lowUserBuyEleParaGiveOut_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
