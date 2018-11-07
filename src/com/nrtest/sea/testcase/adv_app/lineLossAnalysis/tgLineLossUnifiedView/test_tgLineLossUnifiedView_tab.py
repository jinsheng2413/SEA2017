# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_tgLineLossUnifiedView_tab.py
@time: 2018/11/1 14:37
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.tgLineLossUnifiedView.tgLineLossUnifiedView_data import \
    TgLineLossUnifiedView_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.tgLineLossUnifiedView.tgLineLossUnifiedView_page import \
    TgLineLossUnifiedViewPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→线损分析→线损统计分析→台区线损监测→月线损
@ddt
class TestTgLineLossUnifiedView_Tab(unittest.TestCase, TgLineLossUnifiedViewPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(TgLineLossUnifiedView_data.TgLineLossUnifiedView_para, True)

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
        # 查询日期，开始
        self.inputDt_start_date_tab(para['START_DATE_TAB'])
        # 查询日期，结束
        self.inputDt_end_date_tab(para['END_DATE_TAB'])
        # 月线损，查询按钮
        self.btn_search_month()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TgLineLossUnifiedView_data.TgLineLossUnifiedView_para, tabName='月线损'))
    def test_der(self, para):
        clickTabPage('月线损')
        self.query(para)
