# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_authorityMan.py
@time: 2018/11/23 14:37
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.securityMan.securityMan_data import SecutityMan_date
from com.nrtest.sea.pages.sys_mam.securityMan.authorityMan_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理→权限密码管理→权限管理
@ddt
class TestAuthorityMan(unittest.TestCase, AuthorityManPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SecutityMan_date.AuthorityMan_para)

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
        # 注册菜单
        self.menu_name = para['MENU_NAME']
        # 注册菜单
        self.menu_name = para['MENU_NAME']
        # 工号
        self.inputStr_staff_no(para['STAFF_NO'])
        # 用户名
        self.inputStr_user_name(para['USER_NAME'])
        # 当前状态
        self.inputSel_cur_status(para['CUR_STATUS'])
        # 查询按钮
        self.btn_query()

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
    @data(*DataAccess.getCaseData(SecutityMan_date.AuthorityMan_para))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SecutityMan_date.AuthorityMan_para))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
