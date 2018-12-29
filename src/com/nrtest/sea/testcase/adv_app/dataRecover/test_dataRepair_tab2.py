# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_dataRepair_tab2.py
@time: 2018-10-31 16:33
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.dataRecover.dataRepair_data import DataRepair
from com.nrtest.sea.pages.adv_app.dataRecover.dataRepair_page import DataRepair_2Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--数据修复--修复数据查询（第二个tab页）
@ddt
class Test_DataRepair_2(TestCase, DataRepair_2Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(DataRepair.para_DataRepair)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(DataRepair.DataRepair_tab_detail)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 数据类型
        self.inputSel_data_type(para['DATA_TYPE'])

        # 用户类型
        self.inputSel_cons_sort(para['CONS_SORT'])

        # 查询日期
        self.inputStr_date(para['DATE'])

        # 查询
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
    @data(*DataAccess.getCaseData(DataRepair.para_DataRepair,DataRepair.DataRepair_tab_detail))
    def test_query(self, para):
        """
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataRepair.para_DataRepair,DataRepair.DataRepair_tab_detail,valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
