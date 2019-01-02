# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeEditionApprove_page.py
@time: 2018/9/27 15:45
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeEditionApprove_locators import \
    UpgradeEditionApproveLocators


# 基本应用→终端管理→软件升级→升级版本审批
class UpgradeEditionApprovePage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(UpgradeEditionApproveLocators.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     UpgradeEditionApproveLocators.TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # self.click(UpgradeEditionApproveLocators.TMNL_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeEditionApproveLocators.TMNL_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        # self.click(UpgradeEditionApproveLocators.TMNL_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeEditionApproveLocators.TMNL_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 申请状态
    def inputSel_apply_status(self, index):
        # self.click(UpgradeEditionApproveLocators.APPLY_STATUS)
        # locator = self.get_select_locator(
        #     UpgradeEditionApproveLocators.APPLY_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 申请开始日期
    def inputDt_start_date(self, content):
        self.exec_script(UpgradeEditionApproveLocators.START_DATE_JS)
        self.input(content, *UpgradeEditionApproveLocators.START_DATE)

    # 申请结束日期
    def inputDt_end_date(self, content):
        self.exec_script(UpgradeEditionApproveLocators.END_DATE_JS)
        self.input(content, *UpgradeEditionApproveLocators.END_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(UpgradeEditionApproveLocators.BTN_SEARCH)
