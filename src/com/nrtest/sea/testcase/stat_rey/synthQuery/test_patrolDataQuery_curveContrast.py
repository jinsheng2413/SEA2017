# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_patrolDataQuery_curveContrast.py
@time: 2018/10/18 16:32
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.patrolDataQuery_page import PatrolDataQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→巡检仪数据查询→曲线对比
@ddt
class TestPatrolDataQuery_CurveContrast(TestCase, PatrolDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SynthQuery_data.PatrolDataQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SynthQuery_data.PatrolDataQuery_tabName_contrast)
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
        # 终端资产号
        self.inputStr_curve_contrast_tmnl_asset_no(
            para['CURVR_CONTRAST_TMNL_ASSET_NO'])
        # 终端地址
        self.inputStr_curve_contrast_tmnl_addr(
            para['CURVR_CONTRAST_TMNL_ADDR'])
        # 曲线类型
        self.inputSel_curve_contrast_curve_type(
            para['CURVR_CONTRAST_CURVE_TYPE'])
        # 查询按钮
        self.btn_curve_contrast_search()

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
    @data(
        *DataAccess.getCaseData(SynthQuery_data.PatrolDataQuery_para, SynthQuery_data.PatrolDataQuery_tabName_contrast))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(SynthQuery_data.PatrolDataQuery_para, SynthQuery_data.PatrolDataQuery_tabName_contrast,
                                valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
