# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_ReadCompleteRate_count.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.gather_quality_analyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.ReadCompleteRate_page import \
    ReadCompleteRate_count_Page
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→数据采集管理→采集质量分析→采集完整率:采集完整率统计
@ddt
class TestReadCompleteRate(TestCase, ReadCompleteRate_count_Page):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(GatherQualityAnalyze_data.readCompleteRate_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(GatherQualityAnalyze_data.readCompleteRateCount_tab)
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

        # 回收左边树
        self.recoverLeftTree()

    def countQuery(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])

        # 通信方式
        self.inputSel_comm_mode(para['COMM_MODE'])

        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])

        # 蕊片厂家
        self.inputSel_chip_factory(para['CHIP_FACTORY'])

        # 日期时间
        self.inputDt_date_time_count(para['DATE_TIME'])

        # 查询
        self.btn_qry()

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
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.readCompleteRate_para,
                                  GatherQualityAnalyze_data.readCompleteRateCount_tab))
    def test_query(self, para):
        """基本应用→数据采集管理→采集质量分析→采集完整率:采集完整率统计

        :param para:
        """
        self.start_case(para, __file__)
        self.countQuery(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.readCompleteRate_para,
                                  GatherQualityAnalyze_data.readCompleteRateCount_tab))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.countQuery(para)
        self.assert_query_criteria(para)
        self.end_case()
