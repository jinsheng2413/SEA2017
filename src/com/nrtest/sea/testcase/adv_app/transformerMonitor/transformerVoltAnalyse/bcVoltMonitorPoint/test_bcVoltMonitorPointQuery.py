# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 14:42
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.transformerMonitor.transformerMonitor_data import TradnsformerMonitorData
# from com.nrtest.sea.pages.adv_app.transformerMonitor.transformerVoltAnalyse.bcVoltMonitorPoint.bcVoltMonitorPointQuery_page import \
#     BcVoltMonitorPointQueryPage
from com.nrtest.sea.pages.adv_app.transformerMonitor.transformerVoltAnalyse.bcVoltMonitorPoint_page import BcVoltMonitorPointQueryPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用--》配变监测分析--》电压质量分析--》B/C类电压监测点
# B/C类电压监测点查询
@ddt
class TestBcVoltMonitorPointQuery(TestCase, BcVoltMonitorPointQueryPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(TradnsformerMonitorData.para_BcVoltMonitorPoint)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(TradnsformerMonitorData.para_BcVoltMonitorPointQuery)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        """
        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 监测点类型
        self.inputSel_monitor_point_type(para['MONITOR_POINT_TYPE'])
        # 监测点名称
        self.inputStr_monitor_point_name(para['MONITOR_POINT_NAME'])

        self.btn_qry()
        self.sleep_time(2)

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(TradnsformerMonitorData.para_BcVoltMonitorPoint,
                                  TradnsformerMonitorData.para_BcVoltMonitorPointQuery))
    def test_query(self, para):
        """
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TradnsformerMonitorData.para_BcVoltMonitorPoint,
                                  TradnsformerMonitorData.para_BcVoltMonitorPointQuery, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

    # def test_test(self):
    #     # 供电单位
    #     openLeftTree('13401')
    #     # 监测点类型
    #     self.inputRSel_monitor_point_type('全部')
    #     # 监测点名称
    #     self.inputStr_monitor_point_name('')
    #
    #     self.btn_query()
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(BcVoltMonitorPointQueryLocators.TABLE_DATA)
    #     self.assertTrue(result)