# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgrade_locators.py
@time: 2018/9/26 16:12
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalUpgrade.regularSporadicUpgrade_data import RegularSporadicUpgrade_data
from com.nrtest.sea.pages.base_app.terminalUpgrade.regularSporadicUpgrade_page import RegularSporadicUpgradePage
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端升级→常规零星升级
@ddt
class TestUpgradeEditionMan(unittest.TestCase, RegularSporadicUpgradePage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            RegularSporadicUpgrade_data.para_RegularSporadicUpgrade)

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
        # 注册菜单
        self.menu_name = para['MENU_NAME']
        # 忽略历史版本
        self.inputChk_history_version(para['HISTORY_VERSION'])
        # 打开左边树选择供电单位
        openLeftTree(para['TREE_NODE'])
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
    @data(*DataAccess.getCaseData(RegularSporadicUpgrade_data.para_RegularSporadicUpgrade))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RegularSporadicUpgrade_data.para_RegularSporadicUpgrade, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
