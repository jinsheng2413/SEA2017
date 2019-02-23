# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_susLowVoltAnalyDetail.py
@time: 2019-02-13 15:13:21
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lowVoltFixTimeMonitor.lowVoltFixTimeMonitor_data import LowVoltFixTimeMonitorData
from com.nrtest.sea.pages.adv_app.lowVoltFixTimeMonitor.lowVoltMonitor.susLowVoltAnaly_page import SusLowVoltAnalyDetailPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→低压固定时间点电压电流监测→低电压监测→疑似低电压分析:疑似低电压用户明细
@ddt
class TestSusLowVoltAnalyDetail(TestCase, SusLowVoltAnalyDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(LowVoltFixTimeMonitorData.SusLowVoltAnaly_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(LowVoltFixTimeMonitorData.para_SusLowVoltAnaly_detail)
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
        每个测试用例测试结束后的操作，在这里做相关清理工作
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
        # 供电单位
        self.openLeftTree(para['TREE_NODE'])

        # 接线方式
        self.inputSel_wiring_type(para['WIRING_TYPE'])

        # 月份
        self.inputDt_query_date(para['QUERY_DATE'])

        # 低压天数
        self.inputStr_low_volt_days(para['LOW_VOLT_DAYS'])

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
    @data(*DataAccess.getCaseData(LowVoltFixTimeMonitorData.SusLowVoltAnaly_para, LowVoltFixTimeMonitorData.para_SusLowVoltAnaly_detail))
    def test_query(self, para):
        """高级应用→低压固定时间点电压电流监测→低电压监测→疑似低电压分析:疑似低电压用户明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(LowVoltFixTimeMonitorData.SusLowVoltAnaly_para, LowVoltFixTimeMonitorData.para_SusLowVoltAnaly_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
