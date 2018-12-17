# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_countServeDeploy.py
@time: 2018/11/16 16:14
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysConfigMan.sysConfigMan_data import SysConfigManData
from com.nrtest.sea.pages.sys_mam.sysConfigMan.countServeDeploy_page import CountServeDeployPage, \
    CountServeDeployLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→系统配置管理→计算服务配置
@ddt
class TestCountServeDeploy(unittest.TestCase, CountServeDeployPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SysConfigManData.CountServeDeploy_para)

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
        # JOB名称
        self.inputSel_job_name(para['JOB_NAME'])
        # 服务名称
        self.inputSel_serve_name(para['SERVE_NAME'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*CountServeDeployLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(SysConfigManData.CountServeDeploy_para))
    def test_der(self, para):
        self.query(para)
