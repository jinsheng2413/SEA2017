# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_unControlPlantGatherMon_tab1.py
@time: 2018-11-07 9:58
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_data import UnControlPlant
from com.nrtest.sea.pages.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_page import \
    UnControlPlantGatherMon1_locators, UnControlPlantGatherMon1_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--重点用户监测--非统调电厂管理--非统调电厂采集监测（第一个tab页）
@ddt
class Test_UnControlPlantGatherMon_1(unittest.TestCase, UnControlPlantGatherMon1_Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(UnControlPlant.para_unControlPlantGatherMon)
        sleep(2)
        cls.exec_script(cls, UnControlPlantGatherMon1_locators.START_DATE_JS)
        cls.exec_script(cls, UnControlPlantGatherMon1_locators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        sleep(4)
        # 开始日期
        self.inputStr_start_date(para['START_DATE'])
        # 结束日期
        self.inputStr_end_date(para['END_DATE'])
        # 发电方式
        self.inputSel_generate_electricity_way(para['GENERATE_ELECTRICITY_WAY'])
        # 采集方式
        self.inputSel_gather_way(para['GATHER_WAY'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*UnControlPlantGatherMon1_locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(UnControlPlant.para_unControlPlantGatherMon,
                                  UnControlPlant.para_unControlPlantGatherMon_tab_count))
    def test_query(self, para):
        self.query(para)
