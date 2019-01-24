# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_meterSuccessRateQuery.py
@time: 2018/10/10 15:07
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.meterSuccessRateQuery_page import MeterSuccessRateQueryPage


# 统计查询→综合查询→抄表成功率查询（河北）:按地区、厂家统计
@ddt
class TestMeterSuccessRateQuery(TestCase, MeterSuccessRateQueryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.MeterSuccessRateQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.MeterSuccessRateQuery_tabName)
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
        if para['TAB_NAME'] == '1':
            self.clickTabPage(SynthQuery_data.MeterSuccessRateQuery_tabName1)
        if para['TAB_NAME'] == '2':
            self.clickTabPage(SynthQuery_data.MeterSuccessRateQuery_tabName2)
        if para['TAB_NAME'] == '3':
            self.clickTabPage(SynthQuery_data.MeterSuccessRateQuery_tabName3)
        if para['TAB_NAME'] == '4':
            self.clickTabPage(SynthQuery_data.MeterSuccessRateQuery_tabName4)
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 日期
        self.inputDt_query_date(para['QUERY_DATE'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        # 通信方式
        self.inputSel_comm_mode(para['COMM_MODE'])
        # 规约类型
        self.inputSel_protocol_type(para['PROTOCOL_TYPE'])
        # 用户范围
        self.inputSel_cons_range(para['CONS_RANGE'])
        # 统计类型
        self.inputSel_stat_type(para['STAT_TYPE'])
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
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterSuccessRateQuery_para,
                                  SynthQuery_data.MeterSuccessRateQuery_tabName))
    def test_query(self, para):
        """统计查询→综合查询→抄表成功率查询（河北）:按地区、厂家统计

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.MeterSuccessRateQuery_para,
                                  SynthQuery_data.MeterSuccessRateQuery_tabName, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
