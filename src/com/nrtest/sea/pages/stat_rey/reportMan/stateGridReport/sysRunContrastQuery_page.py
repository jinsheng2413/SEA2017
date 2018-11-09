# -*- coding:utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysRunContrastQuery_page.py
@time: 2018/11/6 15:24
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.reportMan.stateGridReport.sysRunContrastQuery_locators import \
    SysRunContrastQueryLocators


# 统计查询--》报表管理--》国网报表--》采集系统运行指标
class SysRunContrastQueryPage(Page):
    def inputStr_date(self, value):
        self.input(value, *SysRunContrastQueryLocators.QRY_DATE)

    # 统计口径

    def inputSel_statWay(self, index):
        self.click(*SysRunContrastQueryLocators.QRY_STAT_WAY)
        locator = self.get_select_locator(SysRunContrastQueryLocators.QRY_STAT_WAY_VALUE, index)
        self.click(*locator)
    # 查询
    def btn_qry(self):
        self.click(*SysRunContrastQueryLocators.BTN_QRY)