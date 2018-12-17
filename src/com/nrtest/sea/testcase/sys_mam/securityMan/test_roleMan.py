# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_roleMan.py
@time: 2018/11/23 11:38
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.securityMan.securityMan_data import SecutityMan_date
from com.nrtest.sea.pages.sys_mam.securityMan.roleMan_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理→权限密码管理→角色管理
@ddt
class TestRoleMAn(unittest.TestCase, RoleMAnPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SecutityMan_date.RoleMan_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新菜单页面
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
        # self.recoverLeftTree()

    def query(self, para):
        # 角色名称
        self.inputStr_role_name(para['ROLE_NAME'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*RoleMAnLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(SecutityMan_date.RoleMan_para))
    def test_der(self, para):
        self.query(para)
