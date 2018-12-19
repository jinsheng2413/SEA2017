# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_vipConsStealAnal.py
@time: 2018-11-05 14:30
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.vipConsStealAnal_data import VipConsMan
from com.nrtest.sea.pages.adv_app.vipConsMan.vipConsStealAnal_page import VipConsStealAnal_locators, \
    VipConsStealAnal_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--重点用户监测--重点用户管理
@ddt
class Test_VipConsStealAnal(unittest.TestCase, VipConsStealAnal_Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(VipConsMan.para_VipConsStealAnal)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        # 注册菜单
        self.menu_name = para['MENU_NAME']
        sleep(4)
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['ORG_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 用户名称
        self.inputStr_cons_name(para['CONS_NAME'])
        # 正常
        self.click(*VipConsStealAnal_locators.QRY_TYPE_NORMAL)
        # 查询
        self.btn_qry()
        self.sleep_time(2)

    def assert_query_result(self, para):
        """
        查询结果校验
        :param para:
        """
        self.assertTrue(self.check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(VipConsMan.para_VipConsStealAnal))
    def test_query(self, para):
        """
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(VipConsMan.para_VipConsStealAnal, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(VipConsMan.para_VipConsStealAnal))
    def test_query(self, para):
        self.query(para)
