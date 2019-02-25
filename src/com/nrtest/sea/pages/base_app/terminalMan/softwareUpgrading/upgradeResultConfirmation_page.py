# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeResultConfirmation_page.py
@time: 2018/9/29 10:00
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.terminalMan.softwareUpgrading.upgradeResultConfirmation_locators import \
    UpgradeResultConfirmationLocator

# 基本应用→终端管理→软件升级→升级结果确认
class UpgradeResultConfirmationPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        self.selectDropDown(index)

    # 升级版本号
    def inputSel_upgrade_version_no(self, index):
        self.click(UpgradeResultConfirmationLocator.UPGRADE_VERSION_NO)
        self.selectDropDown(index)

    # 升级目的
    def inputSel_upgrade_purpose(self, index):
        self.selectDropDown(index)

    # 确认状态
    def inputSel_confirm_status(self, index):
        self.selectDropDown(index)

    # 升级状态
    def inputSel_upgrade_status(self, index):
        self.selectDropDown(index)

    # 升级号
    def inputChk_upgrade_no(self, index):
        self.clickSingleCheckBox(index, locator=UpgradeResultConfirmationLocator.UPGRADE_NO)

    # 批次号
    def inputStr_batch_no(self, index):
        self.input(index)

    # 前置下发状态
    def inputSel_preposition_down_status(self, index):
        self.selectDropDown(index)

    # 确认开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 确认结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
