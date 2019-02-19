# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tgLineLossAbnomalReport.py
@time: 2018/11/2 11:09
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossStatisticsQuery_data import \
    TgLineLossStatisticsQuery_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossAbnormalReport_page import \
    TgLineLossAbnormalReportPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→线损分析→台区线损统计查询→台区线损异常报表
@ddt
class TestTgLineLossAbnormalReport(TestCase, TgLineLossAbnormalReportPage):
    @classmethod
    def setUpClass(cls):

        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(TgLineLossStatisticsQuery_data.TgLineLossAbnormalReport_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 线损维度
        self.inputSel_line_loss_dimension(para['LINE_LOSS_DIMENSION'])

        # 查询日期
        self.inputDt_query_date(para['QUERY_DATE'])

        # 查询按钮
        self.btn_search()

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
    @data(*DataAccess.getCaseData(TgLineLossStatisticsQuery_data.TgLineLossAbnormalReport_para))
    def test_query(self, para):
        """高级应用→线损分析→台区线损统计查询→台区线损异常报表
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TgLineLossStatisticsQuery_data.TgLineLossAbnormalReport_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
