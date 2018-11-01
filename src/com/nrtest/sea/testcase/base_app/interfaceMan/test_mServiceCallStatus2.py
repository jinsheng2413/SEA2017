# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_mServiceCallStatus2.py
@time: 2018-10-31 9:14
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.mServiceCallStatus2_data import InterfaceMan_data
from com.nrtest.sea.pages.base_app.interfaceMan.mServiceCallStatus2_page import MServiceCallStatus2Locators, \
    MServiceCallStatus2Page
from com.nrtest.sea.task.commonMath import *


@ddt
class TestMServiceCallStatus2(unittest.TestCase, MServiceCallStatus2Page):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(InterfaceMan_data.para_MServiceCallStatus2, True)
        sleep(2)
        cls.exec_script(cls, MServiceCallStatus2Locators.START_DATE_JS)
        cls.exec_script(cls, MServiceCallStatus2Locators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

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
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*MServiceCallStatus2Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(InterfaceMan_data.para_MServiceCallStatus2))
    def test_query(self, para):
        self.query(para)
