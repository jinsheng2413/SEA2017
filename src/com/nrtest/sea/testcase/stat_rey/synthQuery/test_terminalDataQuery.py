# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_terminalDataQueryPage.py
@time: 2018/8/14 0002 10:30
"""

import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.locators.stat_rey.synthQuery.terminalDataQuery_locators import TerminalDataQueryLocators
from com.nrtest.sea.pages.stat_rey.synthQuery.terminalDataQuery_page import TerminalDataQueryPage
from com.nrtest.sea.task.synthQuery import TerminalDataQueryLog


# 统计查询→综合查询→用户数据查询
class TestUserDataQuery(unittest.TestCase, TerminalDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = TerminalDataQueryLog()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.driver.quit()

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        self.orl = Oracle()
        self.clear_values(TerminalDataQueryPage)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

    # 基本档案，终端资产号查询
    @BeautifulReport.add_test_img()
    def test_terminalnum(self):
        td = TerminalDataQueryPage(self.driver)
        # 点击左边树-国网冀北电力有限公司
        td.inputNode_jibei()
        # 点击展开-唐山供电公司
        td.inputNode_tangshan()
        # 点击展开-直属用户
        td.inputNode_directlyuser()
        # 点击选择-电网-国各庄
        td.inputNode_guogezhuang()
        # 点击查询按钮
        td.btn_search()
        # 校验
        result = self.assert_context(*TerminalDataQueryLocators.TREE_GUOGEZHUANG)
        self.assertTrue(result)

    # 基本档案，终端资产号查询
    @BeautifulReport.add_test_img()
    def test_terminalnum_two(self):
        td = TerminalDataQueryPage(self.driver)
        # 在终端资产号栏输入“100000045465144”
        td.inputStr_terminalnum('100000045465144')
        # 点击查询按钮
        td.btn_search()

    # 基本档案，终端地址
    @BeautifulReport.add_test_img()
    def test_terminaladdress(self):
        td = TerminalDataQueryPage(self.driver)
        # 在终端地址栏输入“130224866”
        td.inputStr_terminaladdress('130224866')
        # 点击查询按钮
        td.btn_search()

    # 数据展示，电量
    @BeautifulReport.add_test_img()
    def test_electricquantity(self):
        td = TerminalDataQueryPage(self.driver)
        # 在终端地址栏输入“130224866”
        td.inputStr_terminaladdress('130224866')
        # 点击查询按钮
        td.btn_search()
        # 点击数据展示
        td.sleep_time(2)
        td.btn_datashow()
        # #点击电量→查询
        # td.btn_electricquantity_search()
        # 点击基本档案
        td.btn_basicfile()

    # 数据展示，功率
    @BeautifulReport.add_test_img()
    def test_power(self):
        td = TerminalDataQueryPage(self.driver)
        # 在终端地址栏输入“130224866”
        td.inputStr_terminaladdress('130224866')
        # 点击查询按钮
        td.btn_search()
        td.sleep_time(2)
        # 点击数据展示
        td.btn_datashow()
        # # 点击功率→查询
        # td.btn_power_search()
        # 点击基本档案
        td.btn_basicfile()
