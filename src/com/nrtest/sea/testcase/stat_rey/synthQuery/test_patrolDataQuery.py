# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_patrolDataQuery.py
@time: 2018/10/18 16:20
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.patrolDataQuery_page import PatrolDataQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→巡检仪数据查询→基本档案
@ddt
class TestPatrolDataQuery(unittest.TestCase, PatrolDataQueryPage):
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
        # # 回收左边树
        # self.recoverLeftTree()

    def query(self, para):
        # 终端资产号
        self.inputStr_tmnl_asset_no(para['TMNL_ASSET_NO'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.PatrolDataQuery_para))
    def test_der(self, para):
        self.query(para)
