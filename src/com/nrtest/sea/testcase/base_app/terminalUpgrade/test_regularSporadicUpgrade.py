# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgrade_locators.py
@time: 2018/9/26 16:12
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalUpgrade.regularSporadicUpgrade_data import RegularSporadicUpgrade_data
from com.nrtest.sea.pages.base_app.terminalUpgrade.regularSporadicUpgrade_page import RegularSporadicUpgradePage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→终端升级→常规零星升级
@ddt
class TestUpgradeEditionMan(TestCase, RegularSporadicUpgradePage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(RegularSporadicUpgrade_data.para_RegularSporadicUpgrade)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(RegularSporadicUpgrade_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(RegularSporadicUpgradePage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 忽略历史版本
        self.inputChk_history_version(para['HISTORY_VERSION'])

        # 打开左边树选择供电单位
        self.openLeftTree(para['TREE_NODE'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        # 终端用途
        self.inputSel_tmnl_purpose(para['TMNL_PURPOSE'])
        # 升级版本号
        self.inputSel_upgrade_version_no(para['UPGRADE_VERSION_NO'])
        # 起始终端地址
        self.inputStr_tmnl_addr_start(para['TMNL_ADDR_START'])
        # 结束终端地址
        self.inputStr_tmnl_addr_end(para['TMNL_ADDR_END'])
        # 终端资产号
        self.inputStr_tmnl_asset_no(para['TMNL_ASSET_NO'])
        # 点击查询按钮
        self.btn_qry()

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
    @data(*DataAccess.getCaseData(RegularSporadicUpgrade_data.para_RegularSporadicUpgrade))
    def test_query(self, para):
        """基本应用→终端升级→常规零星升级

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RegularSporadicUpgrade_data.para_RegularSporadicUpgrade, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
