# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_lineTopologyDiagram.py
@time: 2018/10/8 14:39
@desc:
"""

import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.lineTopologyDiagram_page import LineTopoLogyDiagramPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→线路拓扑图
@ddt.ddt
class TestLineTopologyDiagram(unittest.TestCase, LineTopoLogyDiagramPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.LineTopologyDiagram_para)

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
        # 线路名称
        self.inputSel_line_name(para['LINE_NAME'])
        # 查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(SynthQuery_data.LineTopologyDiagram_para))
    def test_der(self, para):
        self.query(para)
