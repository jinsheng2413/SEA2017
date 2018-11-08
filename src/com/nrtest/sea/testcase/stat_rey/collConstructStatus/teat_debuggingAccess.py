# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_debuggingAccess.py
@time: 2018/10/24 16:33
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.collConstructStatus.collConstructStatus_data import CollConstructStatus_data
from com.nrtest.sea.pages.stat_rey.collConstructStatus.debuggingAccess_page import DebuggingAccessPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→采集建设情况→调试接入情况
@ddt
class TestDebuggingAccess(unittest.TestCase, DebuggingAccessPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(CollConstructStatus_data.DebuggingAccess_para)

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
        # # 回收左边树
        # self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 管理方式
        self.inputSel_manage_style(para['MANAGE_STYLE'])
        # 装接方式
        self.inputCSel_assembling_way(para['ASSEMBLING_WAY'])
        # 日期
        self.inputDt_date(para['DATE'])
        # 查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(CollConstructStatus_data.DebuggingAccess_para))
    def test_der(self, para):
        self.query(para)
