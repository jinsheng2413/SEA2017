# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_differentialloopSettingDetail.py
@time: 2018-11-07 14:00
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.differentialloopSettingDetail_data import VipConsMan
from com.nrtest.sea.pages.adv_app.vipConsMan.differentialloopSettingDetail_page import \
    DifferentialloopSettingDetail_locators, DifferentialloopSettingDetail_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--重点用户监测--差动回路明细查询
@ddt
class Test_DifferentialloopSettingDetail(unittest.TestCase, DifferentialloopSettingDetail_Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(VipConsMan.para_differentialloopSettingDetail)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(SysDictManPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        sleep(2)
        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*DifferentialloopSettingDetail_locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(VipConsMan.para_differentialloopSettingDetail))
    def test_query(self, para):
        self.query(para)
