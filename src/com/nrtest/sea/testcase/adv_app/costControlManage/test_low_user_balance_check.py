# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_low_user_balance_check.py
@time: 2018/8/10 0010 11:03
@desc:
"""
from unittest import TestCase

from com.nrtest.sea.pages.adv_app.costControlManage.lowUserMoneyCheck_page import BalanceCheck_page
from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.localCostControl.localCostControl_para import LocalCostContral_data
from com.nrtest.sea.pages.other.menu_page import MenuPage


@ddt
# 高级应用→费控管理→本地费控→低压用户余额查看:余额查看
class TestBalanceCheck(TestCase, BalanceCheck_page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(LocalCostContral_data.lowUserBalanceCheck_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(LocalCostContral_data.lowUserBalanceCheck_check_tab)
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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(EleParaManPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 工单编号
        self.inputStr_app_no(para['APP_NO'])

        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])

        # 接收时间
        self.inputDt_receive_date(para['RECEIVE_DATE'])

        # 执行状态
        self.inputSel_execute_status(para['EXECUTE_STATUS'])

        # 终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 电表地址
        self.inputStr_meter_addr(para['METER_ADDR'])

        # 抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])

        # 结束时间
        self.inputDt_end_date(para['END_DATE'])

        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])

        # 电表局编号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])

        # 查询
        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LocalCostContral_data.lowUserBalanceCheck_para,
                                  LocalCostContral_data.lowUserBalanceCheck_check_tab))
    def test_query(self, para):
        """高级应用→费控管理→本地费控→低压用户余额查看:余额查看
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LocalCostContral_data.lowUserBalanceCheck_para,
                                  LocalCostContral_data.lowUserBalanceCheck_check_tab,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
