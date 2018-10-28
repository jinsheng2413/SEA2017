# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_patrolDataQuery_anomalousEvent.py
@time: 2018/10/18 16:35
@desc:
'''

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.patrolDataQuery_page import PatrolDataQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→巡检仪数据查询→异常事件查询
@ddt
class TestPatrolDataQuery_AnomalousEvent(unittest.TestCase, PatrolDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.PatrolDataQuery_para)

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
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 终端地址
        self.inputStr_anomalous_event_tmnl_addr(para['ANOMALOUS_EVENT_TMNL_ADDR'])
        # 用户编号
        self.inputStr_anomalous_event_cons_no(para['ANOMALOUS_EVENT_CONS_NO'])
        # 异常事件
        self.inputSel_anomalous_event(para['ANOMALOUS_EVENT'])
        # 查询按钮
        self.btn_anomalous_event_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.PatrolDataQuery_para))
    def test_der(self, para):
        self.clickTabPage('异常事件查询')
        self.query(para)
