# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysCoverageQuery_page.py
@time: 2018/11/8 10:34
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.reportMan.stateGridReport.sysCoverageQuery_locators import \
    SysCoverageQueryLocators


# 统计查询--》报表管理--》国网报表--》系统采集覆盖情况

class SysCoverageQueryPage(Page):

    # 查询日期

    def inputStr_dateS(self, value):
        self.input(value, *SysCoverageQueryLocators.QRY_DATE)

    # 统计口径
    def inputSel_statWay(self, index):
        self.click(*SysCoverageQueryLocators.QRY_STAT_WAY)
        locator = self.get_select_locator(SysCoverageQueryLocators.QRY_STAT_WAY_VALUE, index)
        self.click(*locator)

    # 用户类型

    def inputSel_userType(self, index):
        self.click(*SysCoverageQueryLocators.QRY_USER_TYPE)
        locator = self.get_select_locator(SysCoverageQueryLocators.QRY_USER_TYPE_VALUE, index)
        self.click(*locator)

    # 查询
    def btn_qry(self):
        self.click(*SysCoverageQueryLocators.BTN_QRY)
