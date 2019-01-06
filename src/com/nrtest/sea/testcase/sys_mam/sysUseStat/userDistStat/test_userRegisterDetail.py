# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_userRegisterDetail.py
@time: 2018/11/15 9:34
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysUseStat.sysUseStat_data import SysUseStat_date
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.sys_mam.sysUseStat.userDistributionStat_page import UserRegisterDetailPage


# 系统管理→系统使用情况统计→用户分布情况统计
# 注册用户明细
@ddt
class TestUserRegisterDetail(TestCase, UserRegisterDetailPage):
    @classmethod
    def setUpClass(cls):

        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SysUseStat_date.UserDistributionStat_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SysUseStat_date.UserRegisterDetail_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 类型
        self.inputSel_type(para['TYPE'])

        # 查询按钮
        self.btn_qry()
        self.sleep_time(2)

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
    @data(
        *DataAccess.getCaseData(SysUseStat_date.UserDistributionStat_para, SysUseStat_date.UserRegisterDetail_tabName))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SysUseStat_date.UserDistributionStat_para, SysUseStat_date.UserRegisterDetail_tabName, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
