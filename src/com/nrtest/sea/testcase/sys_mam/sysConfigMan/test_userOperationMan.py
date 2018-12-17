# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_userOperationMan.py
@time: 2018/11/20 15:18
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysConfigMan.sysConfigMan_data import SysConfigManData
from com.nrtest.sea.pages.sys_mam.sysConfigMan.userOperationMan_page import UserOperationMonitorPage, \
    UserOperationMonitorLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→系统配置管理→用户操作监测
@ddt
class TestUserOperationMonitor(unittest.TestCase, UserOperationMonitorPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SysConfigManData.UserOperationMonitor_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭菜单页面
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
        self.displayTreeMenu()
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 日期
        self.inputDt_date(para['DATE'])
        # 操作模块
        self.inputSel_operation_module(para['OPERATION_MODULE'])
        # 操作人员
        self.inputStr_operator(para['OPERATOR'])
        # 查询按钮
        self.btn_search()
        # 校验
        sleep(2)
        result = self.assert_context(*UserOperationMonitorLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(SysConfigManData.UserOperationMonitor_para))
    def test_der(self, para):
        self.query(para)
