# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_SpecialUserBalanceQuery.py
@time: 2018/8/19 0019 9:26
@desc:
"""
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.costControlManage_data import CostControlManage_data
from com.nrtest.sea.pages.adv_app.costControlManage.specialUserBalanceQuery_page import SpecialUserBalanceQueryPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用--》费控管理--》本地费控--》专变用户余额查询
@ddt
class TestSpecialUserBalanceQuery(TestCase, SpecialUserBalanceQueryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(CostControlManage_data.specialUserBalanceQuery_para)
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

        # self.sleep_time(2000)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # self.clear_values(SpecialUserBalanceQueryPage)

        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        self.openLeftTree(para['TREE_NODE'])

        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])

        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])

        # 终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 越线类型
        self.inputSel_over_type(para['OVER_TYPE'])

        # 召测日期
        self.inputDt_call_date(para['CALL_DATE'])

        # 查询
        self.btn_qry()
        sleep(2)

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
    @data(*DataAccess.getCaseData(CostControlManage_data.specialUserBalanceQuery_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CostControlManage_data.specialUserBalanceQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
