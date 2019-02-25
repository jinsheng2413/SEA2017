# -*- coding: utf-8 -*-


"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_workQuery_tab2.py
@time: 2018/10/31 15:45
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.workQuery.appQuery_data import AppQuery_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.stat_rey.workQuery.workQuery_page import WorkQueryPage


# 统计查询→工单查询→工单查询：工单查询
@ddt
class TestWorkQuery(TestCase, WorkQueryPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(AppQuery_data.AppQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(AppQuery_data.AppQuery_tab_query)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭菜单页面
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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'], is_closed=True)

        # 异常编号
        self.inputStr_abnormal_no(para['ABNORMAL_NO'])

        # 异常状态
        self.inputSel_abnormal_status(para['ABNORMAL_STATUS'])

        # 日期
        self.inputDt_query_date(para['QUERY_DATE'])

        self.btn_qry()

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
    @data(*DataAccess.getCaseData(AppQuery_data.AppQuery_para, AppQuery_data.AppQuery_tab_query))
    def test_query(self, para):
        """统计查询→工单查询→工单查询：工单查询
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(AppQuery_data.AppQuery_para, AppQuery_data.AppQuery_tab_query, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
