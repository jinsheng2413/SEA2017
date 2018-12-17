# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_suspectPowerCutObjectQuery.py
@time: 2018/11/6 14:40
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutAnalysis_data import \
    PowerCutAnalysis_data
from com.nrtest.sea.pages.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutMonitor.suspecteAreaPowerCutMonitor_page import \
    SuspectePowerCutObjectQueryPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测→疑似停电对象查询
@ddt
class TestSuspectePowerCutObjectQuery(unittest.TestCase, SuspectePowerCutObjectQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(PowerCutAnalysis_data.SuspectedAreaPowerCutMonitor_para)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        clickTabPage('疑似停电对象查询')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 是否线路停电
        self.inputSel_whether_line_power_cut(para['WHETHER_LINE_POWER_CUT'])
        # 对象类型
        self.inputSel_object_type(para['OBJECT_TYPE'])
        # 停电日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.SuspectedAreaPowerCutMonitor_para, tabName='疑似停电对象查询'))
    def test_der(self, para):
        self.query(para)
