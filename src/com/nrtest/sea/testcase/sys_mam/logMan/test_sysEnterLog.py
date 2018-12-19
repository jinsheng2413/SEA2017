# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_sysEnterLog.py
@time: 2018/11/29 14:01
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.logMan.logMan_data import LogEdit_data
from com.nrtest.sea.pages.sys_mam.logMan.sysEnterLog_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理→日志管理→系统登录日志
@ddt
class TestSysEnterLog(unittest.TestCase, SysEnterLogPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(LogEdit_data.sysEnterLog_para)

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
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 查询日期，开始
        self.inputDt_start_date(para['START_DATE'])
        # 查询日期，结束
        self.inputDt_end_date(para['END_DATE'])
        # 操作人员
        self.inputStr_operator(para['OPERATOR'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*SysEnterLogLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(LogEdit_data.sysEnterLog_para))
    def test_der(self, para):
        self.query(para)
