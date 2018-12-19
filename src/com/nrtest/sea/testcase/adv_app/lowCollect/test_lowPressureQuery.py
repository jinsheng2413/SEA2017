# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_lowPressureQuery.py
@time: 2018-11-01 16:22
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lowCollect.lowPressureQuery_data import LowColletc
from com.nrtest.sea.pages.adv_app.lowCollect.lowPressureQuery_page import LowPressureQuery_Locators, \
    LowPressureQuery_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--低压采集监控--配置采集任务
@ddt
class Test_LowPressureQuery(unittest.TestCase, LowPressureQuery_Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(LowColletc.para_LowpressureQuery)
        sleep(2)
        cls.exec_script(cls, LowPressureQuery_Locators.START_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        sleep(3)
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 日期
        self.inputStr_date(para['DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*LowPressureQuery_Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LowColletc.para_LowpressureQuery))
    def test_query(self, para):
        self.query(para)
