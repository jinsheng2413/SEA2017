# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: centralizePlanUpgrade_page.py
@time: 2018/9/29 10:49
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.centralizePlanUpgrade_locators import \
    CentralizePlanUpgradeLocators


# 基本应用→终端管理→软件升级→集中计划升级
class CentralizePlanUpgradePage(Page):
    # 集中计划升级
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.click(*CentralizePlanUpgradeLocators.TMNL_FACTORY)
        locator = self.get_select_locator(CentralizePlanUpgradeLocators.TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        self.click(*CentralizePlanUpgradeLocators.UPGRADE_PURPOSE)
        locator = self.get_select_locator(CentralizePlanUpgradeLocators.UPGRADE_PURPOSE_VALUE, index)
        self.click(*locator)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.click(*CentralizePlanUpgradeLocators.TMNL_PURPOSE)
        locator = self.get_select_locator(CentralizePlanUpgradeLocators.TMNL_PURPOSE_VALUE, index)
        self.click(*locator)

    # 开始时间
    def inputDt_start_date(self, content):
        self.exec_script(CentralizePlanUpgradeLocators.START_DATE_JS)
        self.input(content, *CentralizePlanUpgradeLocators.START_DATE)

    # 结束时间
    def inputDt_end_date(self, content):
        self.exec_script(CentralizePlanUpgradeLocators.END_DATE_JS)
        self.input(content, *CentralizePlanUpgradeLocators.END_DATE)

    # 批次号
    def inputStr_batch_no(self, content):
        self.input(content, *CentralizePlanUpgradeLocators.BATCH_NO)

    # 查询按钮
    def btn_search(self):
        self.click(*CentralizePlanUpgradeLocators.BTN_SEARCH)

    # 制定计划
    # 终端厂家
    def inputSel_tab_tmnl_factory(self, index):
        self.click(*CentralizePlanUpgradeLocators.TAB_TMNL_FACTORY)
        locator = self.get_select_locator(CentralizePlanUpgradeLocators.TAB_TMNL_FACTORY_VALUE, index)
        self.click(*locator)

    # 终端类型
    def inputSel_tab_tmnl_type(self, index):
        self.click(*CentralizePlanUpgradeLocators.TAB_TMNL_TYPE)
        locator = self.get_select_locator(CentralizePlanUpgradeLocators.TAB_TMNL_TYPE_VALUE, index)
        self.click(*locator)

    # 终端用途
    def inputSel_tab_tmnl_purpose(self, index):
        self.click(*CentralizePlanUpgradeLocators.TAB_TMNL_PURPOSE)
        locator = self.get_select_locator(CentralizePlanUpgradeLocators.TAB_TMNL_PURPOSE_VALUE, index)
        self.click(*locator)

    # 升级版本号
    def inputSel_tab_upgrade_version_no(self, index):
        self.click(*CentralizePlanUpgradeLocators.TAB_UPGRADE_VERSION_NO)
        locator = self.get_select_locator(CentralizePlanUpgradeLocators.TAB_UPGRADE_VERSION_NO_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_tab_search(self):
        self.click(*CentralizePlanUpgradeLocators.TAB_BTN_SEARCH)
