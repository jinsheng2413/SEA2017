# -*- coding: utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: test_workQuery2017_tab2.py
@time: 2018/11/1 15:27
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.workQuery.workQuery_data import WorkQuery_data
from com.nrtest.sea.pages.stat_rey.workQuery.workQuery2017_page import WorkQuery2017Page
from com.nrtest.sea.task.commonMath import *


# 统计查询--工单查询--工单查询2017（第二个tab页）
@ddt
class TestWorkQuery2017_tab2(TestCase, WorkQuery2017Page):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(WorkQuery_data.WorkQuery2017_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(WorkQuery_data.WorkQuery2017_tab_query)
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
        self.openLeftTree(para['TREE_NODE'])

        # 工单编号
        self.inputStr_workNo(para['WORK_NO'])

        # 工单处理人
        self.inputStr_workMan(para['WORK_MAN'])

        # 工单类型
        self.inputSel_workTitle(para['WORK_TITLE'])

        # 工单状态
        self.inputSel_workStatus(para['WORK_STATUS'])

        # 工单发生时间
        self.inputStr_startDate(para['START_DATE'])

        # 工单完成时间
        self.inputStr_endDate(para['END_DATE'])

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
    @data(*DataAccess.getCaseData(WorkQuery_data.WorkQuery2017_para, WorkQuery_data.WorkQuery2017_tab_query))
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
    @data(*DataAccess.getCaseData(WorkQuery_data.WorkQuery2017_para, WorkQuery_data.WorkQuery2017_tab_query,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
