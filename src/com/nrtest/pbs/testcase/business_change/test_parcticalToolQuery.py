# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_practicalToolQuery.py
@time: 2019-07-08 14:32
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.pbs.data.business_change.businessChange_data import BusinessChange_data
from com.nrtest.pbs.page.business_change.practicalTool_page import PracticalToolQueryPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 业务变更→实用工具:计算公式手动查询
@ddt
class TestPracticalToolQuery(TestCase, PracticalToolQueryPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(BusinessChange_data.PracticalTool_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        cls.goto_frame(cls)
        # menuPage.clickTabPage()
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        cls.goto_home_page(cls)


    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        # self.closeLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 点击菜单
        self.btn_practical_tool_query()
        # 公式
        self.inputSel_query_formula(para['QUERY_FORMULA'])
        # 时间
        self.inputDt_query_date(para['QUERY_DATE'])
        # 查询按钮
        self.btn_qry()



    def assert_query_result(self, para):
        """
        查询结果校验
        :param para:
        """
        # self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(BusinessChange_data.PracticalTool_para,BusinessChange_data.PracticalTool_tabName_query))
    def test_query(self, para):
        """业务变更→实用工具:计算公式手动查询
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(BusinessChange_data.PracticalTool_para,BusinessChange_data.PracticalTool_tabName_query, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
