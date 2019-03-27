# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_taskSuccess.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.tree.tree_page import TreeQualityPage
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.taskSuccess_page import TaskSuccessPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→数据采集管理→采集质量检查(new)→采集任务成功率
@ddt
class TestReadCompleteRate(TestCase, TaskSuccessPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(DataGatherMan_data.dataGatherQualityAnalyze_new_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(GatherQualityAnalyze_data.readCompleteRate_tab)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()
        cls.user_page = TreeQualityPage(cls)

    @classmethod
    def tearDownClass(cls):
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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        self.user_page.openLeftTree(para['NODE'])
        sleep(2)
        self.openLeftTree(para['TREE_NODE'])
        # 日期
        self.inputDt_query_date(para['QUERY_DATE'])
        # 任务名称
        self.inputSel_task_name(para['TASK_NAME'])
        # 查询
        self.btn_query()

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
    @data(*DataAccess.getCaseData(DataGatherMan_data.dataGatherQualityAnalyze_new_para,
                                  DataGatherMan_data.dataGatherQualityAnalyze_new_taskSuccess))
    def test_query(self, para):
        """基本应用→数据采集管理→采集质量检查(new)→采集任务成功率
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.dataGatherQualityAnalyze_new_para,
                                  DataGatherMan_data.dataGatherQualityAnalyze_new_taskSuccess))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
