# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_patrolDataQuery_currentStatus.py
@time: 2018/10/18 16:34
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.patrolDataQuery_page import PatrolDataQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→巡检仪数据查询→电流回路状态
@ddt
class TestPatrolDataQuery_CurrentStatus(unittest.TestCase, PatrolDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.PatrolDataQuery_para)

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
        openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 终端地址
        self.inputStr_current_status_tmnl_addr(
            para['CURRENT_STATUS_TMNL_ADDR'])
        # 终端资产号
        self.inputStr_current_status_tmnl_asset_no(
            para['CURRENT_STATUS_TMNL_ASSET_NO'])
        # 查询按钮
        self.btn_current_status_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.PatrolDataQuery_para))
    def test_der(self, para):
        clickTabPage('电流回路状态')
        self.query(para)
