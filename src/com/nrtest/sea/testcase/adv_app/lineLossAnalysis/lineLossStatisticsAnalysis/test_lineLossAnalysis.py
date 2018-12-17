# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_lineLossAnalysis.py
@time: 2018/10/30 16:26
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossStatisticsAnalysis_data import \
    LineLossStatisticsAnalysis_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossAnalysis_page import \
    LineLossAnalysisPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→线损统计分析→台区线损分析
@ddt
class TestTgLineLossAnalysis(unittest.TestCase, LineLossAnalysisPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(LineLossStatisticsAnalysis_data.LineLossAnalysis_para)

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
        # 线路编号
        self.inputStr_line_no(para['LINE_NO'])
        # 线路名称
        self.inputStr_line_name(para['LINE_NAME'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.LineLossAnalysis_para))
    def test_der(self, para):
        self.query(para)
