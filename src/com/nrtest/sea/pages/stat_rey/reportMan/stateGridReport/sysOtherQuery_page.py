# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysOtherQuery_page.py
@time: 2018/11/8 11:07
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.reportMan.stateGridReport.sysOtherQuery_locators import SysOtherQueryLocators


# 统计查询--》报表管理--》国网报表--》系统其他运行指标

class SysOtherQueryPage(Page):

    # 查询日期

    def inputStr_dateS(self, value):
        self.input(value, *SysOtherQueryLocators.QRY_DATE)

    # 统计口径
    def inputSel_statWay(self, index):
        self.click(*SysOtherQueryLocators.QRY_STAT_WAY)
        locator = self.get_select_locator(SysOtherQueryLocators.QRY_STAT_WAY_VALUE, index)
        self.click(*locator)

    # 查询
    def btn_qry(self):
        self.click(*SysOtherQueryLocators.BTN_QRY)