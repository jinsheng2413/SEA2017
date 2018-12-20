# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_runTmnlStatistics_detail.py
@time: 2018/10/25 13:33
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.collConstructStatus.collConstructStatus_data import CollConstructStatus_data
from com.nrtest.sea.pages.stat_rey.collConstructStatus.runTmnlStatistics_page import RunTmnlStatisticsPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→采集建设情况→运行终端统计→终端运行状态明细
@ddt
class TestRunTmnlStatistics_Detail(unittest.TestCase, RunTmnlStatisticsPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(CollConstructStatus_data.RunTmnlStatistics_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        sleep(2)
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'DETAIL_TREE_ORG_NO'])
        # 用户类型
        self.inputCSel_detail_cons_type(para['DETAIL_CONS_TYPE'])
        # 终端类型
        self.inputCSel_detail_tmnl_type(para['DETAIL_TMNL_TYPE'])
        # 通讯规约
        self.inputCSel_detail_tmnl_protocol(para['DETAIL_TMNL_PROTOCOL'])
        # 通讯方式
        self.inputCSel_detail_tmnl_way(para['DETAIL_TMNL_WAY'])
        # 终端厂家
        self.inputCSel_detail_tmnl_factory(para['DETAIL_TMNL_FACTORY'])
        # 终端状态
        self.inputCSel_detail_tmnl_ststus(para['DETAIL_TMNL_STATUS'])
        # 查询按钮
        self.btn_detail_search()

    @data(*DataAccess.getCaseData(CollConstructStatus_data.RunTmnlStatistics_para))
    def test_der(self, para):
        clickTabPage('终端运行状态明细')
        self.query(para)
