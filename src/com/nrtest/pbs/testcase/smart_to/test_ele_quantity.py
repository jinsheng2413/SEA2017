# -*- coding: utf-8 -*-

"""
@author:郭春彪
@license: (C) Copyright 2019, Nari.
@file: test_ele_quantity.py
@time: 2019-03-15 10:52
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.pbs.data.smart_to.smartTo_data import SmartTo_data
from com.nrtest.pbs.page.smart_to.eleQuantity_page import EleQuantity_page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 智能研判-->电量短信
@ddt
class Test_ele_quantity(TestCase, EleQuantity_page):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SmartTo_data.EleQuantity_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        cls.goto_frame(cls)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage()
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.goto_home_page(cls)

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
        # self.closeLeftTree()

    def query(self, para):
        """
        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        # 用户列表
        self.inputSel_user_list(para["USER_LIST"])

        # 时      间
        self.inputDt_query_date(para["QUERY_DATE"])

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """

    # self.assertTrue(AssertResult(self).check_query_result(para))
    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """

    # self.assertTrue(self.check_query_criteria(para))

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SmartTo_data.EleQuantity_para))
    def test_query(self, para):
        """#智能研判-->电量短信
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SmartTo_data.EleQuantity_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()