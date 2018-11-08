# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_aeeseementResultStatistics.py
@time: 2018/11/1 10:22
@desc:
"""

import unittest

from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossIndexEvaluation.aeeseementResultStatistics_locators import \
    AeeseementResultStatisticsLocators
from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossIndexEvaluation.lineLossIndexEvaluation_data import \
    LineLossIndexEvaluation_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossIndexEvaluation.aeeseementResultStatistics_page import \
    AeeseementResultStatisticsPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→线损统计分析→区域线损分析
@ddt
class TestAeeseementResultStatistics(unittest.TestCase, AeeseementResultStatisticsPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            LineLossIndexEvaluation_data.AssessmentResultStatistics_para, True)

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
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 责任人
        self.inputSel_charge_person(para['CHARGE_PERSON'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()
        # 校验
        result = self.assert_context(
            *AeeseementResultStatisticsLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossIndexEvaluation_data.AssessmentResultStatistics_para))
    def test_der(self, para):
        self.query(para)
