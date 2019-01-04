# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_suspectPowerCutObjectQuery.py
@time: 2018/11/6 14:40
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutAnalysis_data import \
    PowerCutAnalysis_data
from com.nrtest.sea.pages.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutMonitor.suspecteAreaPowerCutMonitor_page import \
    SuspectePowerCutObjectQueryPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测→疑似停电对象查询
@ddt
class TestSuspectePowerCutObjectQuery(TestCase, SuspectePowerCutObjectQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(PowerCutAnalysis_data.SuspectedAreaPowerCutMonitor_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(PowerCutAnalysis_data.SuspectedObjectPowerCutMonitor_tabName)
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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 是否线路停电
        self.inputSel_whether_line_power_cut(para['WHETHER_LINE_POWER_CUT'])
        # 对象类型
        self.inputSel_object_type(para['OBJECT_TYPE'])
        # 停电日期
        self.inputDt_date(para['DATE'])
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
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.SuspectedAreaPowerCutMonitor_para,
                                  PowerCutAnalysis_data.SuspectedObjectPowerCutMonitor_tabName))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.SuspectedAreaPowerCutMonitor_para,
                                  PowerCutAnalysis_data.SuspectedObjectPowerCutMonitor_tabName,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
