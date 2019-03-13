# -*- coding:utf-8 -*-

"""
@author: jinsheng
@file:test_consDataQueryDisplay.py
@time:2019/2/19 9:38
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.synthQuery.consDataQuery_page import *


# 统计查询--综合查询--用户数据查询：数据展示
@ddt
class TestConsDataQueryDisplay(TestCase, ConsDataQueryDisplayPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SynthQuery_data.ConsDataQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(SynthQuery_data.consDataQry_display_tab)  # 2019-03-12
        menuPage.clickTabPage(SynthQuery_data.ConsDataQuery_tab_display)
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
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        if self.is_tree_node_first():
            self.openLeftTree(para['TREE_NODE'])
        else:
            # 用户编号
            self.inputStr_cons_no(para['CONS_NO'])

        # 点击查询按钮
        self.btn_search()

        # tab页选择
        self.inputChk_tab_name(para['TAB_NAME'])
        tab_name = self.get_para_value(para['TAB_NAME'])
        if tab_name == '电能示值':
            self.inputChk_query_type(para['QUERY_TYPE'])
            self.inputDt_start_time(para['START_TIME'])
            self.inputDt_end_time(para['END_TIME'])
            self.btn_search_tab()
        elif tab_name in ['电压曲线', '电流曲线', '功率曲线']:
            self.inputChk_query_type(para['QUERY_TYPE'])
            self.inputDt_start_time(para['START_TIME'])
            self.btn_search_tab()
        elif tab_name == '功率因数曲线':
            self.inputDt_start_time(para['START_TIME'])
            self.btn_search_tab()
        elif tab_name in ['电量', '负荷', '用电异常']:
            self.inputDt_start_time(para['START_TIME'])
            self.inputDt_end_time(para['END_TIME'])
            self.btn_search_tab()


    # 校验
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
    @data(*DataAccess.getCaseData(SynthQuery_data.ConsDataQuery_para, SynthQuery_data.consDataQry_display_tab))
    def test_query(self, para):
        """统计查询--综合查询--用户数据查询：电能示值
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.ConsDataQuery_para, SynthQuery_data.consDataQry_display_tab,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
