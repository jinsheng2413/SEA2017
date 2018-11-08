# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlEventSendingFunction_page.py
@time: 2018/11/7 15:34
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.tmnlEventSendingFunction_locators import *


# 高级应用→配变监测分析→停电分析→终端是否具备停上电事件上送功能
class TmnlEventSendingFunctionPage(Page):
    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(TmnlEventSendingFunctionLocators.DATE_JS)
        self.input(content, *TmnlEventSendingFunctionLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*TmnlEventSendingFunctionLocators.BTN_SEARCH)


# 高级应用→配变监测分析→停电分析→终端是否具备停上电事件上送功能→终端是否具备停上电事件上送功能明细
class TmnlEventSendingFunctionDeatilPage(Page):
    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(TmnlEventSendingFunctionDeatilLocators.DATE_JS)
        self.input(content, *TmnlEventSendingFunctionDeatilLocators.QRY_DATE)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.click(*TmnlEventSendingFunctionDeatilLocators.QRY_TMNL_TYPE)
        locator = self.get_select_locator(TmnlEventSendingFunctionDeatilLocators.QRY_TMNL_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.click(*TmnlEventSendingFunctionDeatilLocators.QRY_TMNL_FACTORY)
        locator = self.get_select_locator(TmnlEventSendingFunctionDeatilLocators.QRY_TMNL_FACTORY_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 终端规约
    def inputSel_tmnl_protocol(self, index):
        self.click(*TmnlEventSendingFunctionDeatilLocators.QRY_TMNL_PROTOCOL)
        locator = self.get_select_locator(TmnlEventSendingFunctionDeatilLocators.QRY_TMNL_PROTOCOL_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 是否具备停上电事件上送功能
    def inputSel_sending_function(self, index):
        self.click(*TmnlEventSendingFunctionDeatilLocators.QRY_SENDING_FUNCTION)
        locator = self.get_select_locator(TmnlEventSendingFunctionDeatilLocators.QRY_SENDING_FUNCTION_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 查询按钮
    def btn_search(self):
        self.click(*TmnlEventSendingFunctionDeatilLocators.BTN_SEARCH)
