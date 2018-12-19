# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_meterSuccessRateQuery.py
@time: 2018/10/10 15:07
@desc:
"""

import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.meterSuccessRateQuery_page import MeterSuccessRateQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→抄表成功率查询（河北）
@ddt.ddt
class TestAllEventMeterEventQuery(unittest.TestCase, MeterSuccessRateQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.MeterSuccessRateQuery_para)

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
        # 日期
        self.inputDt_factory_date(para['FACTORY_DATE'])
        # 用户类型
        self.inputCSel_factory_cons_type(para['FACTORY_CONS_TYPE'])
        # 终端类型
        self.inputCSel_factory_tmnl_type(para['FACTORY_TMNL_TYPE'])
        # 查询按钮
        self.factory_btn_search()

    @ddt.data(*DataAccess.getCaseData(SynthQuery_data.MeterSuccessRateQuery_para))
    def test_der(self, para):
        self.query(para)
