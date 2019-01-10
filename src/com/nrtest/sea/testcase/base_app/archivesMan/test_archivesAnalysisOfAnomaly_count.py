# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesAnalysisOfAnomaly_count.py
@time: 2018/8/30 0030 9:11
@desc:
"""
import unittest
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_data import ArchivesMan_data
from com.nrtest.sea.pages.base_app.archivesMan.archivesAnalysisOfAnomaly_pages import *
from com.nrtest.sea.task.archivesManage import *


# 基本应用--》档案管理--》档案异常分析：档案异常统计

@ddt
class test_archivesAnalysisOfAnomaly_count(unittest.TestCase, ArchivesAnalysisOfAnomaly_count_pages):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(ArchivesMan_data.archivesAnalysisOfAnomaly)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(ArchivesMan_data.archivesAnalysisOfAnomaly_count_tab)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        # 关闭菜单
        cls.closePages(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

        # self.sleep_time(2000)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # self.clear_values(ArchivesAnalysisOfAnomaly_count_pages)
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 用户类型
        self.inputSel_cons_sort(para['CONS_SORT'])

        # 日期
        self.inputDt_date_time(para['DATE_TIME'])

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
    @data(*DataAccess.getCaseData(ArchivesMan_data.archivesAnalysisOfAnomaly,
                                  ArchivesMan_data.archivesAnalysisOfAnomaly_count_tab))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesMan_data.archivesAnalysisOfAnomaly,
                                  ArchivesMan_data.archivesAnalysisOfAnomaly_count_tab, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
