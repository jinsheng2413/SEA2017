# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: regularSporadicUpgradeApprove_page.py
@time: 2018/9/28 9:27
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.regularSporadicUpgradeApprove_locators import \
    RegularSporadicUpgradeApproveLocator


# 基本应用→终端管理→软件升级→常规零星升级审批
class RegularSporadicUpgradeApprovePage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(RegularSporadicUpgradeApproveLocator.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     RegularSporadicUpgradeApproveLocator.TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 申请状态
    def inputSel_apply_status(self, index):
        # self.click(RegularSporadicUpgradeApproveLocator.APPLY_STATUS)
        # locator = self.get_select_locator(
        #     RegularSporadicUpgradeApproveLocator.APPLY_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        # self.click(RegularSporadicUpgradeApproveLocator.TMNL_PURPOSE)
        # locator = self.get_select_locator(
        #     RegularSporadicUpgradeApproveLocator.TMNL_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 申请开始日期
    def inputDt_start_date(self, content):
        self.exec_script(RegularSporadicUpgradeApproveLocator.START_DATE_JS)
        self.input(content, *RegularSporadicUpgradeApproveLocator.START_DATE)

    # 申请结束日期
    def inputDt_end_date(self, content):
        self.exec_script(RegularSporadicUpgradeApproveLocator.END_DATE_JS)
        self.input(content, *RegularSporadicUpgradeApproveLocator.END_DATE)

    # 批次号
    def inputStr_batch_no(self, content):
        self.input(content, *RegularSporadicUpgradeApproveLocator.BATCH_NO)

    # 查询按钮
    def btn_search(self):
        self.click(RegularSporadicUpgradeApproveLocator.BTN_SEARCH)
