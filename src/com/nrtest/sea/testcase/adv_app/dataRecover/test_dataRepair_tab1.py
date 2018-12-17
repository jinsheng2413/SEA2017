# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_dataRepair_tab1.py
@time: 2018-10-31 15:38
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.dataRecover.dataRepair_data import DataRepair
from com.nrtest.sea.pages.adv_app.dataRecover.dataRepair_page import DataRepair_1Page, DataRepair_1Locators
from com.nrtest.sea.task.commonMath import *


# 高级应用--数据修复--修复数据查询（第一个tab页）
@ddt
class Test_DataRepair_1(unittest.TestCase, DataRepair_1Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(DataRepair.para_DataRepair)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        sleep(4)
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['ORG_NO'])
        # 用户类型
        self.inputSel_cons_sort(para['CONS_SORT'])
        # 数据类型
        self.inputSel_data_type(para['DATA_TYPE'])
        # 开始日期
        self.inputStr_start_date(para['START_DATE'])
        # 结束日期
        self.inputStr_end_date(para['END_DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*DataRepair_1Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataRepair.para_DataRepair, DataRepair.DataRepair_tab_count))
    def test_query(self, para):
        self.query(para)