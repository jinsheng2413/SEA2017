# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEffectStatistics_page.py
@time: 2018/9/29 14:16
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeEffectStatistics_locators import \
    UpgradeEffectStatisticsLocators


# 基本应用→终端管理→软件升级→升级效果统计
class UpgradeEffectStatisticsPage(Page):
    # 集中计划升级
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.click(*UpgradeEffectStatisticsLocators.TMNL_FACTORY)
        locator = self.get_select_locator(UpgradeEffectStatisticsLocators.TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        self.click(*UpgradeEffectStatisticsLocators.UPGRADE_PURPOSE)
        locator = self.get_select_locator(UpgradeEffectStatisticsLocators.UPGRADE_PURPOSE_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*UpgradeEffectStatisticsLocators.BTN_SEARCH)

    # 终端升级明细
    def inputSel_detail_tmnl_factory(self, index):
        self.click(*UpgradeEffectStatisticsLocators.DETAIL_TMNL_FACTORY)
        locator = self.get_select_locator(UpgradeEffectStatisticsLocators.DETAIL_TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 升级目的
    def inputSel_detail_upgrade_purpose(self, index):
        self.click(*UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_PURPOSE)
        locator = self.get_select_locator(UpgradeEffectStatisticsLocators.DETAIL_UPGRADE_PURPOSE_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_detail_search(self):
        self.click(*UpgradeEffectStatisticsLocators.BTN_DETAIL_SEARCH)
