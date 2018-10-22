# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_fourTableMeterReadSuccessRate.py
@time: 2018/10/20 11:14
@desc:
'''

import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.pages.stat_rey.synthQuery.fourTableMeterReadSuccessRate_page import FourTableMeterReadSuccessRatePage
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.task.commonMath import *
from ddt import ddt,data

# 统计查询→综合查询→四表合一抄表成功率
@ddt
class TestAutomatedMeterAvailability(unittest.TestCase,FourTableMeterReadSuccessRatePage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.FourTableMeterReadSuccessRate_para)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        #回收左边树
        self.recoverLeftTree()

    def query(self, para):
        #打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        #表计类型
        self.inputSel_meter_type(para['METER_TYPE'])
        #日期
        self.inputDt_date(para['DATE'])
        #查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.FourTableMeterReadSuccessRate_para))
    def test_der(self, para):
        self.query(para)
