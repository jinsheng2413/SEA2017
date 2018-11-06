# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_lowPressureMonitor.py
@time: 2018-11-01 11:30
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lowCollect.lowPressureMonitor_data import LowColletc
from com.nrtest.sea.pages.adv_app.lowCollect.lowPressureMonitor_page import LowPressureMonitor_Locators, \
    LowPressureMonitor_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--低压采集监控--配置采集任务
@ddt
class Test_LowPressureMonitor(unittest.TestCase, LowPressureMonitor_Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(LowColletc.para_LowPressureMonitor, True)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        sleep(3)
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['ORG_NO'])
        # 用户定义类别
        self.inputSel_cons_define_type(para['CONS_DEFINE_TYPE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*LowPressureMonitor_Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LowColletc.para_LowPressureMonitor))
    def test_query(self, para):
        self.query(para)
