# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_authorityMan.py
@time: 2018/11/23 14:37
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.securityMan.securityMan_data import SecutityMan_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.sys_mam.securityMan.authorityMan_page import *


# 系统管理→权限密码管理→权限管理
@ddt
class TestAuthorityMan(TestCase, AuthorityManPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SecutityMan_data.AuthorityMan_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(SysConfigManData.SysAbnormalParaSet_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()


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
        # 工号
        self.inputStr_staff_no(para['STAFF_NO'])

        # 用户名
        self.inputStr_staff_name(para['STAFF_NAME'])

        # 当前状态
        self.inputSel_cur_status(para['CUR_STATUS'])

        # 查询按钮
        self.btn_query()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SecutityMan_data.AuthorityMan_para))
    def test_query(self, para):
        """系统管理→权限密码管理→权限管理

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SecutityMan_data.AuthorityMan_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
