# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_lineDataQueryPage.py
@time: 2018/8/17 0002 14:50
'''

import unittest
from com.nrtest.sea.pages.stat_rey.synthQuery.lineDataQuery_page import LineDataQueryPage
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.sea.task.synthQuery import LineDataQueryLog
from com.nrtest.sea.locators.stat_rey.synthQuery.lineDataQuery_locators import LineDataQueryLocators

#统计查询→综合查询→线路数据查询
class TestLineDataQuery(unittest.TestCase,LineDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = LineDataQueryLog()

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
        self.clear_values(LineDataQueryPage)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
    #基本档案，查询
    @BeautifulReport.add_test_img()
    def test_a_linenum(self):
        #点击电网结构
        self.inputNode_electricpower()
        #点击营销电网结构
        self.inputNode_marketing()
        self.sleep_time(2)
        #点击国网冀北电力有限公司
        self.inputNode_jibei()
        #点击电网_安各庄变电站
        self.inputNode_angezhuang()
        #点击电网_10kV523安变无税庄
        self.inputNode_anbianwu()
        #点击查询按钮
        self.btn_search()

    # 基本档案，查询
    @BeautifulReport.add_test_img()
    def test_b_linenum(self):
        #线路编号栏输入“1100771326”
        self.inputStr_linenum('1100771326')
        #点击查询按钮
        self.btn_search()

    #数据展示，查询
    @BeautifulReport.add_test_img()
    def test_c_data_search(self):
        # 线路编号栏输入“1100771326”
        self.inputStr_linenum('1100771326')
        # 点击查询按钮
        self.btn_search()
        #数据展示，点击查询
        self.btn_data_search()