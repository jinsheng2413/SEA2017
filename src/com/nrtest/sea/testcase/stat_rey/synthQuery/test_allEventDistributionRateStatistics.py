# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_allEventDistributionRateStatistics.py
@time: 2018/10/18 9:49
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.allEventDistributionRateStatistics_page import \
    AllEventDistributionRateStatisticsPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→全事件配置率统计
@ddt
class TestAllEventDistributionRateStatistics(unittest.TestCase, AllEventDistributionRateStatisticsPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.AllEventDistributionRateStatistics_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.refreshPage(cls)

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
        # # 回收左边树
        # self.recoverLeftTree()

    # 全事件配置率统计
    def query(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 时间
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.AllEventDistributionRateStatistics_para))
    def test_der(self, para):
        self.query(para)

    # 全事件未配置明细
    def query_tab(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 时间
        self.inputDt_date_tab(para['DATE_TAB'])
        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        # 查询按钮
        self.btn_search_tab()

    @data(*DataAccess.getCaseData(SynthQuery_data.AllEventDistributionRateStatistics_para))
    def test_der_tab(self, para):
        self.clickTabPage('全事件未配置明细')
        self.query_tab(para)
