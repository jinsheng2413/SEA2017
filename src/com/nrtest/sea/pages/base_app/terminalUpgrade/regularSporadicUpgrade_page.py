# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgrade_page.py
@time: 2018/9/26 16:12
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalUpgrade.regularSporadicUpgrade_locators import \
    RegularSporadicUpgradeLocators


# 基本应用→终端升级→常规零星升级
class RegularSporadicUpgradePage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.click(*RegularSporadicUpgradeLocators.TMNL_FACTORY)
        locator = self.get_select_locator(RegularSporadicUpgradeLocators.TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.click(*RegularSporadicUpgradeLocators.TMNL_TYPE)
        locator = self.get_select_locator(RegularSporadicUpgradeLocators.TMNL_TYPE_VALUE, index)
        self.click(*locator)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.click(*RegularSporadicUpgradeLocators.TMNL_PURPOSE)
        locator = self.get_select_locator(RegularSporadicUpgradeLocators.TMNL_PURPOSE_VALUE, index)
        self.click(*locator)

    # 升级版本号
    def inputSel_upgrade_version_no(self, index):
        self.click(*RegularSporadicUpgradeLocators.UPGRADE_VERSION_NO)
        locator = self.get_select_locator(RegularSporadicUpgradeLocators.UPGRADE_VERSION_NO_VALUE, index)
        self.click(*locator)

    # 起始终端地址
    def inputStr_tmnl_addr_start(self, content):
        self.input(content, *RegularSporadicUpgradeLocators.TMNL_ADDR_START)

    # 结束终端地址
    def inputStr_tmnl_addr_end(self, content):
        self.input(content, *RegularSporadicUpgradeLocators.TMNL_ADDR_END)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content, *RegularSporadicUpgradeLocators.TMNL_ASSET_NO)

    # 查询按钮
    def btn_search(self):
        self.click(*RegularSporadicUpgradeLocators.BTN_SEARCH)
