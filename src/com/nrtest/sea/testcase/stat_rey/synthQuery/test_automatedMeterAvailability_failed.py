# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_automatedMeterAvailability_failed.py
@time: 2018/10/19 14:04
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.automatedMeterAvailability_page import AutomatedMeterAvailabilityPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→自动化抄表可用率→全项失败明细
@ddt
class TestAutomatedMeterAvailability_Failed(unittest.TestCase, AutomatedMeterAvailabilityPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.AutomatedMeterAvailability_para)

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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 表计类型
        self.inputSel_failed_meter_type(para['FAILED_METER_TYPE'])
        # 终端地址
        self.inputStr_failed_tmnl_addr(para['FAILED_TMNL_ADDR'])
        # 日期
        self.inputDt_failed_date(para['FAILED_DATE'])
        # 查询按钮
        self.failed_btn_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.AutomatedMeterAvailability_para))
    def test_der(self, para):
        clickTabPage('全项失败明细')
        self.query(para)
