# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_cPSynthQuery.py
@time: 2018/10/20 14:09
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.cPSynthQuery_page import CPSynthQueryPage


# 统计查询→综合查询→采集点综合查询
@ddt
class TestCPSynthQuery(TestCase, CPSynthQueryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.CPSynthQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage()
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 终端类型
        self.inputChk_tmnl_type(para['TMNL_TYPE'])
        if self.get_para_value(para['TMNL_TYPE']) == '专变':
            # 终端状态
            self.inputSel_tmnl_status(para['TMNL_STATUS'])
            # 用户范围
            self.inputSel_cons_range(para['CONS_RANGE'])
            # 停电标志
            self.inputSel_power_cut_flag(para['POWER_CUT_FLAG'])
            # 终端投运日期
            self.inputChk_tmnl_comm_date(para['TMNL_COMM_DATE'])
            # 开始日期
            self.inputDt_start_date(para['START_DATE'])
            # 结束日期
            self.inputDt_end_date(para['END_DATE'])
            # 接线方式
            self.inputSel_wiring_mode(para['WIRING_MODE'])

        if self.get_para_value(para['TMNL_TYPE']) == '公变':
            # 终端状态
            self.inputSel_tmnl_status(para['TMNL_STATUS'])
            # 终端投运日期
            self.inputChk_tmnl_comm_date(para['TMNL_COMM_DATE'])
            # 开始日期
            self.inputDt_start_date(para['START_DATE'])
            # 结束日期
            self.inputDt_end_date(para['END_DATE'])
            # 接线方式
            self.inputSel_wiring_mode(para['WIRING_MODE'])

        if self.get_para_value(para['TMNL_TYPE']) == '关口':
            # 终端状态
            self.inputSel_tmnl_status(para['TMNL_STATUS'])
            # 终端投运日期
            self.inputChk_tmnl_comm_date(para['TMNL_COMM_DATE'])
            # 开始日期
            self.inputDt_start_date(para['START_DATE'])
            # 结束日期
            self.inputDt_end_date(para['END_DATE'])
            # 接线方式
            self.inputSel_wiring_mode(para['WIRING_MODE'])

        # 查询按钮
        self.btn_search()

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
    @data(*DataAccess.getCaseData(SynthQuery_data.CPSynthQuery_para))
    def test_query(self, para):
        """统计查询→综合查询→采集点综合查询

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.CPSynthQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
