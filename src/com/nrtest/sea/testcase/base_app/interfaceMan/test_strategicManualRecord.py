# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_strategicManualRecord.py
@time: 2018-11-08 10:06
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.strategicManualRecord_data import InterfaceManager_data
from com.nrtest.sea.pages.base_app.interfaceMan.strategicManualRecord_page import StrategicManualRecord_Locators, \
    StrategicManualRecordPage
from com.nrtest.sea.task.commonMath import *


# 基本应用--接口管理--关口人工补录
@ddt
class Test_StrategicManualRecord(unittest.TestCase, StrategicManualRecordPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(InterfaceManager_data.para_StrategicManualRecord)
        sleep(2)
        cls.exec_script(cls, StrategicManualRecord_Locators.DATE_JS)

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
        # 点击电网结构
        self.click(StrategicManualRecord_Locators.QRY_DWJG)
        # 点击供电单位
        self.click(StrategicManualRecord_Locators.QRY_ORG)
        # 采集点名
        self.inputStr_gatherpoint_name(para['GATHERPOINT_NAME'])
        # 电表名称
        self.inputStr_meter_name(para['METER_NAME'])
        # 电表地址
        self.inputStr_meter_addr(para['METER_ADDR'])
        # 日期
        self.inputStr_date(para['DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(StrategicManualRecord_Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(InterfaceManager_data.para_StrategicManualRecord))
    def test_query(self, para):
        self.query(para)
