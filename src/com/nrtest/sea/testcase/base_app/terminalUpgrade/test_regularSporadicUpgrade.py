# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgrade_locators.py
@time: 2018/9/26 16:12
@desc:
"""

import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalUpgrade.regularSporadicUpgrade_data import RegularSporadicUpgrade_data
from com.nrtest.sea.locators.base_app.terminalUpgrade.regularSporadicUpgrade_locators import \
    RegularSporadicUpgradeLocators
from com.nrtest.sea.pages.base_app.terminalUpgrade.regularSporadicUpgrade_page import RegularSporadicUpgradePage
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端升级→常规零星升级
@ddt.ddt
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
        cls.refreshPage(cls)

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
        self.clear_values(RegularSporadicUpgradePage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['TREE_ORG_NO'])
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
        self.btn_search()
        # 校验
        result = self.assert_context(*RegularSporadicUpgradeLocators.CHECK)
        self.assertTrue(result)

    @ddt.data(*DataAccess.getCaseData(RegularSporadicUpgrade_data.para_RegularSporadicUpgrade))
    def test_der(self, para):
        self.query(para)
