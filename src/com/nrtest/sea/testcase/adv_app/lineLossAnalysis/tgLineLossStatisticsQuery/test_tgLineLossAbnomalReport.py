# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tgLineLossAbnomalReport.py
@time: 2018/11/2 11:09
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossStatisticsQuery_data import \
    TgLineLossStatisticsQuery_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossAbnormalReport_page import \
    TgLineLossAbnormalReportPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→线损统计分析→台区线损异常报表
@ddt
class TestTgLineLossAbnormalReport(unittest.TestCase, TgLineLossAbnormalReportPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(TgLineLossStatisticsQuery_data.TgLineLossAbnormalReport_para)

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
        # 线损维度
        self.inputSel_line_loss_dimension(para['LINE_LOSS_DIMENSION'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TgLineLossStatisticsQuery_data.TgLineLossAbnormalReport_para))
    def test_der(self, para):
        self.query(para)
