# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: databaseUpgradeStat_page.py
@time: 2018/11/15 15:44
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysConfigMan.databaseUpgradeStat_locators import DatabaseUpgradeStatLocators


# 系统管理→系统配置管理→数据库升级情况
class DatabaseUpgradeStatPage(Page):
    # 升级日期
    def inputDt_date(self, content):
        # self.input(content, *DatabaseUpgradeStatLocators.QRY_DATE)
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.click(*DatabaseUpgradeStatLocators.BTN_SEARCH)
