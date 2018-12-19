# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_importantClientRealTimePowerCutMonitor.py
@time: 2018/11/6 10:50
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutAnalysis_data import \
    PowerCutAnalysis_data
from com.nrtest.sea.pages.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutMonitor.importantClientRealTimePowerCutMonitor_page import *
from com.nrtest.sea.task.commonMath import *


# 高级应用→配变监测分析→停电分析→停电监测→重要客户实时停电监测→重要客户历史停电查询
@ddt
class TestImportantClientRealTimePowerCutMonitor(unittest.TestCase, ImportantClientRealTimePowerCutMonitorPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(PowerCutAnalysis_data.ImportantClientRealTimePowerCutMonitor_para)

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
        clickTabPage('重要客户历史停电查询')
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 电压等级
        self.inputSel_volt_level(para['VOLT_LEVEL'])
        # 停电开始日期
        self.inputDt_start_date(para['START_DATE'])
        # 停电结束日期
        self.inputDt_end_date(para['END_DATE'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.ImportantClientRealTimePowerCutMonitor_para,
                                  tabName='重要客户历史停电查询'))
    def test_der(self, para):
        self.query(para)
