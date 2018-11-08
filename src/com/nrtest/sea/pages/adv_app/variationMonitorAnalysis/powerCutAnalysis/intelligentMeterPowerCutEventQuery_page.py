# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: intelligentMeterPowerCutEventQuery_page.py
@time: 2018/11/5 14:42
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.intelligentMeterPowerCutEventQuery_locators import *


# 高级应用→配变监测分析→停电分析→智能表停电事件查询
class IntelligentMeterPowerCutEventQueryPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(*IntelligentMeterPowerCutEventQueryLocators.QRY_CONS_TYPE)
        locator = self.get_select_locator(
            IntelligentMeterPowerCutEventQueryLocators.QRY_CONS_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(IntelligentMeterPowerCutEventQueryLocators.DATE_JS)
        self.input(content, *IntelligentMeterPowerCutEventQueryLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*IntelligentMeterPowerCutEventQueryLocators.BTN_SEARCH)


# 高级应用→配变监测分析→停电分析→智能表停电事件查询→智能表停电明细
class IntelligentMeterPowerCutEventQueryDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(
            *IntelligentMeterPowerCutEventQueryDetailLocators.QRY_CONS_TYPE)
        locator = self.get_select_locator(
            IntelligentMeterPowerCutEventQueryDetailLocators.QRY_CONS_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(
            IntelligentMeterPowerCutEventQueryDetailLocators.DATE_JS)
        self.input(
            content, *IntelligentMeterPowerCutEventQueryDetailLocators.QRY_DATE)

    # 事件正确性
    def inputSel_event_correctness(self, index):
        self.click(
            *IntelligentMeterPowerCutEventQueryDetailLocators.QRY_EVENT_CORRECTNESS)
        locator = self.get_select_locator(IntelligentMeterPowerCutEventQueryDetailLocators.QRY_EVENT_CORRECTNESS_VALUE,
                                          index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 停电时长
    def inputStr_power_cut_start(self, content):
        self.input(
            content, *IntelligentMeterPowerCutEventQueryDetailLocators.QRY_POWER_CUT_START)

    def inputStr_power_cut_end(self, content):
        self.input(
            content, *IntelligentMeterPowerCutEventQueryDetailLocators.QRY_POWER_CUT_END)

    # 电表厂家
    def inputSel_meter_factory(self, index):
        self.click(
            *IntelligentMeterPowerCutEventQueryDetailLocators.QRY_METER_FACTORY)
        locator = self.get_select_locator(IntelligentMeterPowerCutEventQueryDetailLocators.QRY_METER_FACTORY_VALUE,
                                          index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 查询按钮
    def btn_search(self):
        self.click(*IntelligentMeterPowerCutEventQueryDetailLocators.BTN_SEARCH)
