# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_allEventMeterEventQuery.py
@time: 2018/9/30 14:43
@desc:
'''

import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.pages.stat_rey.synthQuery.allEventMeterEventQuery_page import AllEventMeterEventQueryPage
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.task.commonMath import *
import ddt

# 统计查询→综合查询→全事件电表事件查询
@ddt.ddt
class TestAllEventMeterEventQuery(unittest.TestCase,AllEventMeterEventQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.AllEventMeterEventQuery_para)

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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        #打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        #电表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 事件等级
        self.inputSel_event_level(para['EVENT_LEVEL'])
        # 事件类型
        self.inputSel_event_type(para['EVENT_TYPE'])
        # 采集开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 采集结束时间
        self.inputDt_end_date(para['END_DATE'])
        #查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(SynthQuery_data.AllEventMeterEventQuery_para))
    def test_der(self, para):
        self.query(para)
