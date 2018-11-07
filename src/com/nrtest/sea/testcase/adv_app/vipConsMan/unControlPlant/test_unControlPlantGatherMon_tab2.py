# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_unControlPlantGatherMon_tab2.py
@time: 2018-11-07 10:17
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_data import UnControlPlant
from com.nrtest.sea.pages.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_page import \
    UnControlPlantGatherMon2_locators, UnControlPlantGatherMon2_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--重点用户监测--非统调电厂管理--非统调电厂采集监测（第二个tab页）
@ddt
class Test_UnControlPlantGatherMon_2(unittest.TestCase, UnControlPlantGatherMon2_Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(UnControlPlant.para_unControlPlantGatherMon, True)
        sleep(2)
        # 选择第二个tab页
        clickTabPage('非统调电厂采集监测明细')
        cls.exec_script(cls, UnControlPlantGatherMon2_locators.DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        sleep(4)
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['ORG_NO'])
        # 发电方式
        self.inputSel_generate_electricity_way(para['GENERATE_ELECTRICITY_WAY'])
        # 采集方式
        self.inputSel_gather_way(para['GATHER_WAY'])
        # 查询日期
        self.inputStr_date(para['DATE'])
        # 户号
        self.inputStr_cons_no(para['CONS_NO'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*UnControlPlantGatherMon2_locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(UnControlPlant.para_unControlPlantGatherMon,
                                  UnControlPlant.para_unControlPlantGatherMon_tab_detail))
    def test_query(self, para):
        self.query(para)
