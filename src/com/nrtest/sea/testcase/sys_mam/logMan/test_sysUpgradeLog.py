# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_sysUpgradeLog.py
@time: 2018/11/30 10:58
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.logMan.logMan_data import LogEdit_data
from com.nrtest.sea.pages.sys_mam.logMan.sysUpgradeLog_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理→日志管理→系统升级日志
@ddt
class TestSysUpgradeLog(unittest.TestCase, SysUpgradeLogPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            LogEdit_data.sysUpgradeLog_para, True)

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
        # 版本类型
        self.inputSel_version_type(para['VERSION_TYPE'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*SysUpgradeLogLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(LogEdit_data.sysUpgradeLog_para))
    def test_der(self, para):
        self.query(para)
