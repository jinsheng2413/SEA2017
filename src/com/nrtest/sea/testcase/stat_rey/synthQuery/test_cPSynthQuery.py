# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_cPSynthQuery.py
@time: 2018/10/20 14:09
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.cPSynthQuery_page import CPSynthQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→采集点综合查询
@ddt
class TestCPSynthQuery(unittest.TestCase, CPSynthQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.CPSynthQuery_para)

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
        # 终端类型
        self.inputSel_tmnl_status(para['TMNL_STATUS'])
        # 用户范围
        self.inputSel_cons_range(para['CONS_RANGE'])
        # 查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.CPSynthQuery_para))
    def test_der(self, para):
        self.query(para)
