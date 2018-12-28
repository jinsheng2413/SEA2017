# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeTaskExecution_page.py
@time: 2018/9/28 14:22
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeTaskExecution_locators import \
    UpgradeTaskExecutionLocators


# 基本应用→终端管理→软件升级→升级任务执行
class UpgradeTaskExecutionPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(*UpgradeTaskExecutionLocators.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     UpgradeTaskExecutionLocators.TMNL_FACTORY_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # self.click(*UpgradeTaskExecutionLocators.TMNL_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeTaskExecutionLocators.TMNL_TYPE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        # self.click(*UpgradeTaskExecutionLocators.TMNL_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeTaskExecutionLocators.TMNL_PURPOSE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 开始时间
    def inputDt_start_date(self, content):
        self.exec_script(UpgradeTaskExecutionLocators.START_DATE_JS)
        self.input(content, *UpgradeTaskExecutionLocators.START_DATE)

    # 结束时间
    def inputDt_end_date(self, content):
        self.exec_script(UpgradeTaskExecutionLocators.END_DATE_JS)
        self.input(content, *UpgradeTaskExecutionLocators.END_DATE)

    # 批次号
    def inputStr_batch_no(self, content):
        self.input(content, *UpgradeTaskExecutionLocators.BATCH_NO)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        # self.click(*UpgradeTaskExecutionLocators.UPGRADE_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeTaskExecutionLocators.UPGRADE_PURPOSE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 升级类型
    def inputSel_upgrade_type(self, index):
        # self.click(*UpgradeTaskExecutionLocators.UPGRADE_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeTaskExecutionLocators.UPGRADE_TYPE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 执行状态
    def inputSel_execution_state(self, index):
        # self.click(*UpgradeTaskExecutionLocators.EXECUTION_STATE)
        # locator = self.get_select_locator(
        #     UpgradeTaskExecutionLocators.EXECUTION_STATE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.click(*UpgradeTaskExecutionLocators.BTN_SEARCH)
