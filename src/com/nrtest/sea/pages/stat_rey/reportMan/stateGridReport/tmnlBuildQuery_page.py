# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tmnlBuildQuery_page.py
@time: 2018/11/8 9:12
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.reportMan.stateGridReport.tmnlBuildQuery_locators import TmnlBuildQueryLocators


# 统计查询--》报表管理--》国网报表--》智能电能表及终端设备建设情况

class TmnlBuildQueryPage(Page):

    # 查询日期

    def inputStr_dateS(self, value):
        self.input(value, *TmnlBuildQueryLocators.QRY_DATE_S)

    def inputStr_dateE(self, value):
        self.input(value, *TmnlBuildQueryLocators.QRY_DATE_E)

    # 终端类型
    def inputSel_tmnlType(self, index):
        self.click(*TmnlBuildQueryLocators.QRY_TMNL_TYPE)
        locator = self.get_select_locator(TmnlBuildQueryLocators.QRY_TMNL_TYPE_VALUE, index)
        self.click(*locator)

    # 终端厂商
    def inputSel_tmnlFac(self, index):
        self.click(*TmnlBuildQueryLocators.QRY_TMNL_FAC)
        locator = self.get_select_locator(TmnlBuildQueryLocators.QRY_TMNL_FAC_VALUE, index)
        self.click(*locator)

    # 统计口径
    def inputSel_statWay(self, index):
        self.click(*TmnlBuildQueryLocators.QRY_STAT_WAY)
        locator = self.get_select_locator(TmnlBuildQueryLocators.QRY_STAT_WAY_VALUE, index)
        self.click(*locator)

    # 查询
    def btn_qry(self):
        self.click(*TmnlBuildQueryLocators.BTN_QRY)
