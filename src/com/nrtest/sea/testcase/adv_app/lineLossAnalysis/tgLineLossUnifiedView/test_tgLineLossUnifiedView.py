# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tgLineLossUnifiedView.py
@time: 2018/11/1 14:17
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.tgLineLossUnifiedView.tgLineLossUnifiedView_data import \
    TgLineLossUnifiedView_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.tgLineLossUnifiedView.tgLineLossUnifiedView_page import \
    TgLineLossUnifiedViewPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→线损分析→线损统计分析→台区线损统一视图
# 首页
@ddt
class TestTgLineLossUnifiedView(TestCase, TgLineLossUnifiedViewPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(TgLineLossUnifiedView_data.TgLineLossUnifiedView_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(TgLineLossUnifiedView_data.TgLineLossUnifiedView_home_page)
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
        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])

        # 查询按钮
        self.btn_search()

        # TAB页名称
        self.inputChk_tab_name(para['TAB_NAME'])

        if self.get_para_value(para['TAB_NAME']) == '日线损':
            # 查询日期，开始
            self.inputDt_start_date(para['START_DATE'])

            # 查询日期，结束
            self.inputDt_end_date(para['END_DATE'])

            # 日线损，查询按钮
            self.btn_search_day()

        if self.get_para_value(para['TAB_NAME']) == '月线损':
            # 查询日期，开始
            self.inputDt_start_date(para['START_DATE'])

            # 查询日期，结束
            self.inputDt_end_date(para['END_DATE'])

            # 月线损，查询按钮
            self.btn_search_month()

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
    @data(*DataAccess.getCaseData(TgLineLossUnifiedView_data.TgLineLossUnifiedView_para, TgLineLossUnifiedView_data.TgLineLossUnifiedView_home_page))
    def test_query(self, para):
        """高级应用→线损分析→线损统计分析→台区线损统一视图:首页
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TgLineLossUnifiedView_data.TgLineLossUnifiedView_para, TgLineLossUnifiedView_data.TgLineLossUnifiedView_home_page,
                                  valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
