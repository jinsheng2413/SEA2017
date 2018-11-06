# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_meterRealTimePowerCutQuery.py
@time: 2018/11/6 15:27
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutAnalysis_data import \
    PowerCutAnalysis_data
from com.nrtest.sea.pages.adv_app.variationMonitorAnalysis.powerCutAnalysis.meterRealTimePowerCutQuery_page import \
    MeterRealTimePowerCutQueryPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→配变监测分析→停电分析→表计实时停上电信息查询
@ddt
class TestMeterRealTimePowerCutQuery(unittest.TestCase, MeterRealTimePowerCutQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(PowerCutAnalysis_data.MeterRealTimePowerCutQuery_para, True)

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
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 台区编号
        self.inputStr_tg_no(para['TG_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 电表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 停电标志
        self.inputSel_power_cut_mark(para['POWER_CUT_MARK'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(PowerCutAnalysis_data.MeterRealTimePowerCutQuery_para))
    def test_der(self, para):
        self.query(para)
