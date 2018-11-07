# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: validPowerCutEventQuery_page.py
@time: 2018/11/2 16:19
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.validPowerCutEventQuery_locators import \
    ValidPowerCutDetailLocators, ValidPowerCutEventQueryLocators


# 高级应用→配变监测分析→停电分析→有效停电事件查询
class ValidPowerCutEventQueryPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(*ValidPowerCutEventQueryLocators.QRY_CONS_TYPE)
        locator = self.get_select_locator(
            ValidPowerCutEventQueryLocators.QRY_CONS_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(ValidPowerCutEventQueryLocators.DATE_JS)
        self.input(content, *ValidPowerCutEventQueryLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*ValidPowerCutEventQueryLocators.BTN_SEARCH)


# 高级应用→配变监测分析→停电分析→有效停电事件查询→有效停电明细
class ValidPowerCutDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(*ValidPowerCutDetailLocators.QRY_CONS_TYPE)
        locator = self.get_select_locator(
            ValidPowerCutDetailLocators.QRY_CONS_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.click(*ValidPowerCutDetailLocators.QRY_TMNL_TYPE)
        locator = self.get_select_locator(
            ValidPowerCutDetailLocators.QRY_TMNL_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 日期
    def inputDt_date(self, content):
        self.exec_script(ValidPowerCutDetailLocators.DATE_JS)
        self.input(content, *ValidPowerCutDetailLocators.QRY_DATE)

    # 当前是否停电
    def inputSel_whether_power_cut(self, index):
        self.click(*ValidPowerCutDetailLocators.QRY_WHETHER_POWER_CUT)
        locator = self.get_select_locator(
            ValidPowerCutDetailLocators.QRY_WHETHER_POWER_CUT_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 是否有效停电
    def inputSel_whether_power_cut_valid(self, index):
        self.click(*ValidPowerCutDetailLocators.QRY_WHETHER_POWER_CUT_VALID)
        locator = self.get_select_locator(
            ValidPowerCutDetailLocators.QRY_WHETHER_POWER_CUT_VALID_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 是否补全
    def inputSel_whether_complement(self, index):
        self.click(*ValidPowerCutDetailLocators.QRY_COMPLEMENT)
        locator = self.get_select_locator(
            ValidPowerCutDetailLocators.QRY_COMPLEMENT_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.click(*ValidPowerCutDetailLocators.QRY_TMNL_FACTORY)
        locator = self.get_select_locator(
            ValidPowerCutDetailLocators.QRY_TMNL_FACTORY_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 停电时长
    def inputStr_power_cut_start(self, content):
        self.input(content, *ValidPowerCutDetailLocators.QRY_POWER_CUT_START)

    def inputStr_power_cut_end(self, content):
        self.input(content, *ValidPowerCutDetailLocators.QRY_POWER_CUT_END)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *ValidPowerCutDetailLocators.QRY_TMNL_ADDR)

    # 查询按钮
    def btn_search(self):
        self.click(*ValidPowerCutDetailLocators.BTN_SEARCH)
