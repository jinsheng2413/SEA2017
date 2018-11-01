# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_dataRepair_tab2.py
@time: 2018-10-31 16:33
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.dataRecover.dataRepair_data import DataRepair
from com.nrtest.sea.pages.adv_app.dataRecover.dataRepair_page import DataRepair_2Page, DataRepair_2Locators
from com.nrtest.sea.task.commonMath import *


# 高级应用--数据修复--修复数据查询（第二个tab页）
@ddt
class Test_DataRepair_2(unittest.TestCase, DataRepair_2Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(DataRepair.para_DataRepair, True)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        # 选择第二个tab页
        clickTabPage('数据修复明细')
        sleep(4)
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['ORG_NO'])
        # 用户类型
        self.inputSel_cons_sort(para['CONS_SORT'])
        # 数据类型
        self.inputSel_data_type(para['DATA_TYPE'])
        # 查询日期
        self.inputStr_date(para['DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*DataRepair_2Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataRepair.para_DataRepair))
    def test_query(self, para):
        self.query(para)
