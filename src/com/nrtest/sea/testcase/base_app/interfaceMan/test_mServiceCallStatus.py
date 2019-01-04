# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_mServiceCallStatus.py
@time: 2018-10-15 15:00
@desc:
"""

import unittest
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.mServiceCallStatus_data import InterfaceMan_data
from com.nrtest.sea.locators.base_app.interfaceMan.mServiceCallStatus_locators import MServiceCallStatusLocators
from com.nrtest.sea.pages.base_app.interfaceMan.mServiceCallStatus_page import MServiceCallStatusPage
from com.nrtest.sea.task.commonMath import *


# 基本应用--接口管理--其他业务接口--服务调用情况
@ddt
class TestMServiceCallStatus(unittest.TestCase, MServiceCallStatusPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(InterfaceMan_data.para_MServiceCallStatus)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(DataGatherMan_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(InterfaceMan_data.para_MServiceCallStatus)
        sleep(2)
        cls.exec_script(cls, MServiceCallStatusLocators.START_DATE_JS)
        cls.exec_script(cls, MServiceCallStatusLocators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 业务系统
        self.inputSel_business_system(para['BUSINESS_SYSTEM'])
        # #服务名称
        self.inputSel_business_name(para['BUSINESS_NAME'])
        # 开始时间
        self.inputStr_start_date(para['START_DATE'])
        # 结束时间
        self.inputStr_end_date(para['END_DATE'])
        # 查询
        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
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
    @data(*DataAccess.getCaseData(InterfaceMan_data.para_MServiceCallStatus))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(InterfaceMan_data.para_MServiceCallStatus, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
