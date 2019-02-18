# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_news.py
@time: 2018-11-02 10:36
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.newsanswer.news_data import NewsAnswer
from com.nrtest.sea.pages.adv_app.newsanswer.news_page import News_Page
from com.nrtest.sea.pages.other.menu_page import MenuPage


@ddt
class Test_News(TestCase, News_Page):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(NewsAnswer.para_News)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(DataGatherMan_data.tmnlInstallDetail_tabOne)
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

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'],is_closed=True)

        # 问题标题
        self.inputStr_question_title(para['QUESTION_TITLE'])

        # 问题类型
        self.inputSel_question_type(para['QUESTION_TYPE'])

        # 问题版块
        self.inputSel_question_plate(para['QUESTION_PLATE'])

        # 紧急程度
        self.inputSel_emergency_degree(para['EMERGENCY_DEGREE'])

        # 查询方式
        self.inputSel_query_type(para['QUERY_TYPE'])

        # 问题状态
        self.inputSel_question_status(para['QUESTION_STATUS'])

        # 开始日期
        self.inputDt_start_date(para['START_DATE'])

        # 结束日期
        self.inputDt_end_date(para['END_DATE'])

        # 查询
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
    @data(*DataAccess.getCaseData(NewsAnswer.para_News))
    def test_query(self, para):
        """高级应用→问题交流平台→问题在线交流
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(NewsAnswer.para_News,valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
