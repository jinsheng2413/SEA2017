# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tgLineLossAnalysisJibei.py
@time: 2018/10/31 16:25
@desc:
"""

import unittest
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossStatisticsAnalysis_data import \
    LineLossStatisticsAnalysis_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.tgLineLossAnalysisJibei_page import \
    TgLineLossAnalysisJibeiPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→线损统计分析→台区线损分析（冀北）
@ddt
class TestTgLineLossAnalysisJibei(unittest.TestCase, TgLineLossAnalysisJibeiPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossStatisticsAnalysis_data.TgLineLossAnalysisJibei_para)
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
        openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])
        # 台区名称
        self.inputStr_tg_name(para['TG_NAME'])
        # 安装率
        self.inputSel_installation_rate(para['INSTALLATION_RATE'])
        # self.inputStr_installation_rate(para['INSTALLATION_RATE_INPUT'])
        # 抄读成功率
        self.inputSel_read_success_rate(para['READ_SUCCESS_RATE'])
        # self.inputStr_read_success_rate(para['READ_SUCCESS_RATE_INPUT'])
        # 线损率
        self.inputSel_line_loss_rate(para['LINE_LOSS_RATE'])
        # self.inputStr_line_loss_rate(para['LINE_LOSS_RATE_INPUT'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 可算
        self.inputChk_may(para['LINE_LOSS_TYPE_MAY'])
        # 达标
        self.inputChk_reach(para['LINE_LOSS_TYPE_REACH'])
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

    # @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.TgLineLossAnalysisJibei_para)[0:1])
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossStatisticsAnalysis_data.TgLineLossAnalysisJibei_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
