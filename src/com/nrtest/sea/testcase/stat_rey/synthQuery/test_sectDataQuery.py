# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_sectDataQuery.py
@time: 2018/9/29 16:13
@desc:
"""

import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.sectDataQuery_page import SectDataQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→抄表段数据查询
@ddt.ddt
class TestSectDataQuery(unittest.TestCase, SectDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.SectDataQuery_para)

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
        # 去除查询干扰数据(要传入对应的page页面类)
        self.clear_values(SectDataQueryPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 抄表段编号
        self.inputStr_sect_no(para['SECT_NO'])
        # 查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(SynthQuery_data.SectDataQuery_para))
    def test_der(self, para):
        self.query(para)

    # 数据展示
    def query_tab(self, para):
        # 抄表段编号
        self.inputStr_sect_no(para['SECT_NO'])
        # 查询按钮
        self.btn_search()
        self.sleep_time(2)
        # 点击数据展示,查询按钮
        self.btn_tab_search()

    @ddt.data(*DataAccess.getCaseData(SynthQuery_data.SectDataQuery_para))
    def test_der_tab(self, para):
        self.clickTabPage('数据展示')
        self.query_tab(para)
