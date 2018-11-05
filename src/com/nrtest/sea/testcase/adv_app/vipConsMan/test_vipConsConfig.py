# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_vipConsConfig.py
@time: 2018-11-05 11:22
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.vipConsConfig_data import VipConsMan
from com.nrtest.sea.pages.adv_app.vipConsMan.vipConsConfig_page import VipConsConfig_locators, VipConsConfig_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--重点用户监测--重点用户管理
@ddt
class Test_VipConsConfig(unittest.TestCase, VipConsConfig_Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(VipConsMan.para_VipConsConfig, True)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        sleep(4)
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['ORG_NO'])
        # 运行容量等级
        self.inputSel_run_level(para['RUN_LEVEL'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*VipConsConfig_locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(VipConsMan.para_VipConsConfig))
    def test_query(self, para):
        self.query(para)
