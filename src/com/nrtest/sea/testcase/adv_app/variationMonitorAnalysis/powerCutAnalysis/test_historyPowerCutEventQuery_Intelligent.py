# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_historyPowerCutEventQuery_Intelligent.py
@time: 2018/11/7 14:47
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutAnalysis_data import \
    PowerCutAnalysis_data
from com.nrtest.sea.pages.adv_app.variationMonitorAnalysis.powerCutAnalysis.historyPowerCutEventQuery_page import \
    IntelligentMeterPowerCutEventQueryDetailPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→配变监测分析→停电分析→历史停电事件查询→智能表停电事件查询
@ddt
class TestHistoryPowerCutEventQuery_Intelligent(unittest.TestCase, IntelligentMeterPowerCutEventQueryDetailPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(PowerCutAnalysis_data.HistoryPowerCutEventQuery_para)

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
        clickTabPage('智能表停电事件查询')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 查询日期
        self.inputDt_date(para['DATE'])
        # 事件正确性
        self.inputSel_event_correctness(para['EVENT_CORRECTNESS'])
        # 停电时长
        self.inputStr_power_cut_start(para['POWER_CUT_START'])
        self.inputStr_power_cut_end(para['POWER_CUT_END'])
        # 电表厂家
        self.inputSel_meter_factory(para['METER_FACTORY'])
        # 是否有效
        self.inputSel_whether_valid(para['WHETHER_VALID'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.HistoryPowerCutEventQuery_para, tabName='智能表停电事件查询'))
    def test_der(self, para):
        self.query(para)
