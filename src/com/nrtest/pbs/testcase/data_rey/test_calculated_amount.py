# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_calculated_amount.py
@time: 2019/3/11 0011 16:15
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.pbs.data.data_rey.data_query_data import Data_query
from com.nrtest.pbs.page.data_rey.calculated_amount_page import Calcluteamount_page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 数据查询--计算量
@ddt
class test_CalculatedAmount(TestCase, Calcluteamount_page):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(Data_query.calculated_amount_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        cls.goto_frame(cls)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(CollOperMain_data.collSuccRate_tab)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.iframe_back(cls, num=1)

        # 关闭菜单页面
        cls.main_page(cls)

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
        self.closeLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        self.openLeftTree(para['TREE_NODE'])
        # 时间方案
        self.inputBtn_time_blue_print(para['TIME_BLUE_PRINT'])

        # 时间
        self.inputDt_query_time(para['QUERY_TIME'])
        # 电量单位计算方式
        self.inputChk_ele_unit(para['ELE_UNIT'])

        # 查询
        self.btn_qry(para['BTN_QUERY'])

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
        self.assertTrue(self.check_query_criteria(para))

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(Data_query.calculated_amount_para))
    def test_query(self, para):
        """采集运维→采集监视
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(Data_query.calculated_amount_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
