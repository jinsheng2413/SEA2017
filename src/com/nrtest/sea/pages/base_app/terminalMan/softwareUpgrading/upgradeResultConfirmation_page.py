# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: upgradeResultConfirmation_page.py
@time: 2018/9/29 10:00
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→软件升级→升级结果确认
class UpgradeResultConfirmationPage(Page):
    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(UpgradeResultConfirmationLocator.TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     UpgradeResultConfirmationLocator.TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # self.click(UpgradeResultConfirmationLocator.TMNL_TYPE)
        # locator = self.get_select_locator(
        #     UpgradeResultConfirmationLocator.TMNL_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端用途
    def inputSel_tmnl_purpose(self, index):
        # self.click(UpgradeResultConfirmationLocator.TMNL_PURPOSE)
        # locator = self.get_select_locator(
        #     UpgradeResultConfirmationLocator.TMNL_PURPOSE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 确认开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(UpgradeResultConfirmationLocator.START_DATE_JS)
        # self.input(content, *UpgradeResultConfirmationLocator.START_DATE)
        self.inputDate(content)

    # 确认结束日期
    def inputDt_end_date(self, content):
        # self.exec_script(UpgradeResultConfirmationLocator.END_DATE_JS)
        # self.input(content, *UpgradeResultConfirmationLocator.END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(UpgradeResultConfirmationLocator.BTN_SEARCH)
        self.btn_query()
