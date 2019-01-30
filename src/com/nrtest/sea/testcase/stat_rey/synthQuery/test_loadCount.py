# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_loadCount.py
@time: 2019/1/30 0030 9:12
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assertResult import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.onlyChangeSysthesisQuery import LoadCountPage


# 统计查询--综合查询--专公变综合查询：负荷统计
@ddt
class TestMeterDataQuery(TestCase, LoadCountPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.onlyChangeSysthesisQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.onlyChangeSysthesisQuery_loadCount_tab)
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
        self.openLeftTree(para['TREE_CONS_NO'])
        # 数据类型
        self.inputCHR_dataType(para['DATA_TYPE'])
        if self.dateType == '日数据':
            # 有功
            self.inputCHR_power_type(para['POWER_TYPE'])
            # 日期
            self.inputDT_displayDate(para['DISPLAY_DATE'])
            # 瞬时量
            self.inputCHR_quantityType(para['QUANTITY_TYPE'])
            # 曲线间隔
            self.inputStr_curveBetween(para['CURVE_BETWEEN'])
        elif self.dateType == '月数据':
            self.inputDT_monthDay(para['MONTH_DAY'])
            # 有功
            self.inputCHR_power_type(para['POWER_TYPE'])
            self.inputCHR_max_min(para['MAX_MIN_TYPE'])
        elif self.dateType == '年数据':
            # 有功
            self.inputCHR_power_type(para['POWER_TYPE'])
            self.inputDT_yearDay(para['YEAR_DAY'])

        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult().check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.onlyChangeSysthesisQuery_para,
                                  SynthQuery_data.onlyChangeSysthesisQuery_loadCount_tab)[0:1])
    def test_query(self, para):
        """# 统计查询--综合查询--专公变综合查询：负荷统计

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.onlyChangeSysthesisQuery_para,
                                  SynthQuery_data.onlyChangeSysthesisQuery_loadCount_tab, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()