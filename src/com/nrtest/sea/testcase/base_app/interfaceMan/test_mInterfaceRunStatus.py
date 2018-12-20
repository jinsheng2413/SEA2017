# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_mInterfaceRunStatus.py
@time: 2018-10-30 13:48
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.mInterfaceRunStatus_data import InterfaceMan_data
from com.nrtest.sea.pages.base_app.interfaceMan.mInterfaceRunStatus_page import MInterfaceRunStatusPage, \
    MInterfaceRunStatusLocators
from com.nrtest.sea.task.commonMath import *


# 基本应用--接口管理--其他业务接口--接口运行状态
@ddt
class Test_MInterfaceRunStatus(unittest.TestCase, MInterfaceRunStatusPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(InterfaceMan_data.para_mInterfaceRunStatus)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        # 业务系统
        self.inputSel_business_system(para['BUSINESS_SYSTEM'])
        # 服务对象名称
        self.inputSel_service_name(para['SERVICE_NAME'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*MInterfaceRunStatusLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(InterfaceMan_data.para_mInterfaceRunStatus))
    def test_query(self, para):
        self.query(para)
