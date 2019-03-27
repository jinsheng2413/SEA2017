# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_ReadCompleteRate.py
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
from com.nrtest.sea.pages.base_app.dataGatherMan.backgroundTaskQuery_page import BackgroundTaskQueryPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→数据采集管理→采集质量检查(new)→后台任务查询
@ddt
class TestReadCompleteRate(TestCase, BackgroundTaskQueryPage):

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
        # 任务来源
        self.inputSel_task_from(para['TASK_FROM'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 任务当前状态
        self.inputSel_task_status(para['TASK_STATUS'])
        # 任务时间从
        self.inputDt_start_time(para['START_TIME'])
        # 到
        self.inputDt_end_time(para['END_TIME'])
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
                                  DataGatherMan_data.dataGatherQualityAnalyze_new_backgroundTaskQuery))
    def test_query(self, para):
        """基本应用→数据采集管理→采集质量检查(new)→后台任务查询
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.dataGatherQualityAnalyze_new_para,
                                  DataGatherMan_data.dataGatherQualityAnalyze_new_backgroundTaskQuery))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
