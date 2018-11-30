# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysUpgradeLog_page.py
@time: 2018/11/30 10:56
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.logMan.sysUpgradeLog_locators import SysUpgradeLogLocators


# 系统管理→日志管理→系统升级日志
class SysUpgradeLogPage(Page):
    # 版本类型
    def inputSel_version_type(self, index):
        self.click(*SysUpgradeLogLocators.QRY_VERSION_TYPE)
        locator = self.get_select_locator(SysUpgradeLogLocators.QRY_VERSION_TYPE_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*SysUpgradeLogLocators.BTN_SEARCH)
