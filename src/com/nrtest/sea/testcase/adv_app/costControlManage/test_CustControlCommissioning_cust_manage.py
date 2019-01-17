# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_CustControlCommissioning_ele_manage.py
@time: 2018/8/23 0023 11:20
@desc:
"""
from unittest import TestCase

from ddt import data
from ddt import ddt

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.costControlManage_data import CostControlManage_data
from com.nrtest.sea.pages.adv_app.costControlManage.custControlCommissioning_page import CustControlCommissioning_page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→费控管理→本地费控→费控投入调试

@ddt
class TestCustControlCommissioning_cust_manage(TestCase, CustControlCommissioning_page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(CostControlManage_data.custControlCommissioning_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(CostControlManage_data.custControlCommissioning_tab_cust)
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
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 控制类型
        self.inputChk_ctrl_type(para['CTRL_TYPE'])

        # 营销单号查询
        self.inputStr_app_no(para['APP_NO'])

        # 按调试日期
        self.inputSel_debug_dt(para['DEBUG_DATE'])

        # 开始时间
        self.inputDt_start_date(para['START_DATE'])

        # 结束时间
        self.inputDt_end_date(para['END_DATE'])

        # 终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])

        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])

        # 下发状态
        self.inputSel_send_status(para['SEND_STATUS'])

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
    @data(*DataAccess.getCaseData(CostControlManage_data.custControlCommissioning_para))
    def test_query(self, para):
        """高级应用→费控管理→本地费控→费控投入调试

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CostControlManage_data.custControlCommissioning_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
