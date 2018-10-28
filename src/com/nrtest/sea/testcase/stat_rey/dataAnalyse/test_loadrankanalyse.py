# -*- coding:utf-8 -*-

'''
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: test_loadrankanalyse.py
@time: 2018/8/9 14:05
@desc:
'''
import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.locators.stat_rey.dataAnalyse.dataanalyse_rank_locators import DataAnalyseRankLocators
from com.nrtest.sea.pages.stat_rey.dataAnalyse.dataanalyse_rank_page import DataAnalyseRankPage
from com.nrtest.sea.task.loadRankAnalyse import *


# @ddt.ddt
class TestLoadRankAnalyse(unittest.TestCase, DataAnalyseRankPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = loadrankanalyse()
        cls.orl = Oracle()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.driver.quit()

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        pass

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.clear_values(DataAnalyseRankPage)

    # 查询专变用户，排名为20的结果
    @BeautifulReport.add_test_img()
    # @ddt.data(*pg.lis)
    def test_rank_num_two(self, data):
        self.btn_org_no()
        self.sleep_time(2)
        self.inputStr_start_date(data[1])
        self.inputStr_end_date(data[2])
        print(data[0])
        self.inputStr_rank_num(data[0])
        self.btn_search()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*DataAnalyseRankLocators.TAB_ONE)

        s = self.body_value()
        if ('排名数量不能小于1!' in s) or ('排名数量不能大于100!' in s):
            self.assertTrue(True)
            self.btn_confirm()
        elif result is True:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
#

#
