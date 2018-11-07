# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: specTranRunQuery_page.py
@time: 2018/11/7 10:47
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.reportMan.stateGridReport.specTranRunQuery_locators import \
    SpecTranRunQueryLocators


# 统计查询--》报表管理--》国网报表--》专变用户运行指标

class SpecTranRunQueryPage(Page):

    # 查询月份

    def inputStr_date(self, value):
        self.input(value, *SpecTranRunQueryLocators.QRY_DATE)

    # 异常状态
    def inputSel_statWay(self, index):
        self.click(*SpecTranRunQueryLocators.QRY_STAT_WAY)
        locator = self.get_select_locator(SpecTranRunQueryLocators.QRY_STAT_WAY_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 查询
    def btn_qry(self):
        self.click(*SpecTranRunQueryLocators.BTN_QRY)
