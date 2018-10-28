# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: test_dataspeciality_analyse.py
@time: 2018/8/15 14:38
@desc:
"""
import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.sea.locators.stat_rey.dataAnalyse.dataspeciality_analyse_locators import DataSpecialityAnalyseLocators
from com.nrtest.sea.pages.stat_rey.dataAnalyse.dataspeciality_analyse_page import DataSpecialityAnalysePage
from com.nrtest.sea.task.dataspecialityAnalyse import *


class DataSpecialityAnalyse(unittest.TestCase, DataSpecialityAnalysePage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = dataspecialityanalyse()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.driver.quit()

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

        self.clear_values(DataSpecialityAnalysePage)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

    @BeautifulReport.add_test_img('txz.png')
    def test_dataspeciality_analyse(self):
        self.spread_org_no()
        self.tangshan_org_no()
        self.sleep_time(2)
        self.select_cons_type()
        self.select_public()
        self.time()
        self.time_year1()
        self.time_year2()
        self.sleep_time(2)
        self.time_mouth()
        self.sleep_time(2)
        self.time_confirm()
        self.time_day()
        self.sleep_time(2)
        self.bin_search()
        self.sleep_time(2)
        result = self.assert_context(*DataSpecialityAnalyseLocators.TeAB_ONE)
        self.assertTrue(result)
