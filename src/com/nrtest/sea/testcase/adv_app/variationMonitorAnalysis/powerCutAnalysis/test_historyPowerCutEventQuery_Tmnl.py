# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_historyPowerCutEventQuery_Tmnl.py
@time: 2018/11/7 14:38
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutAnalysis_data import \
    PowerCutAnalysis_data
from com.nrtest.sea.pages.adv_app.variationMonitorAnalysis.powerCutAnalysis.historyPowerCutEventQuery_page import \
    TmnlPowerCutEventQueryPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→配变监测分析→停电分析→历史停电事件查询→终端停电事件查询
@ddt
class TestHistoryPowerCutEventQuery_Tmnl(TestCase, TmnlPowerCutEventQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(PowerCutAnalysis_data.HistoryPowerCutEventQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(PowerCutAnalysis_data.HistoryPowerCutEventQuery_tabName_Tmnl)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 关闭菜单页面
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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 日期类型
        self.inputChk_date_type(para['DATE_TYPE'])
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 停复电标识
        self.inputSel_power_cut_identifying(para['POWER_CUT_IDENTIFYING'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 是否有效
        self.inputSel_whether_valid(para['WHETHER_VALID'])
        # 查询按钮
        self.btn_search()

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
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.HistoryPowerCutEventQuery_para,
                                  PowerCutAnalysis_data.HistoryPowerCutEventQuery_tabName_Tmnl))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.HistoryPowerCutEventQuery_para,
                                  PowerCutAnalysis_data.HistoryPowerCutEventQuery_tabName_Tmnl, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
