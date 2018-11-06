# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: suspecteAreaPowerCutMonitor_page.py
@time: 2018/11/6 14:11
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.powerCutMonitor.suspecteAreaPowerCutMonitor_locators import *


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测
class SuspecteAreaPowerCutMonitorPage(Page):
    # 停电日期
    def inputDt_date(self, content):
        self.exec_script(SuspecteAreaPowerCutMonitorLocators.DATE_JS)
        self.input(content, *SuspecteAreaPowerCutMonitorLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*SuspecteAreaPowerCutMonitorLocators.BTN_SEARCH)


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测→疑似停电线路查询
class SuspectePowerCutLineQueryPage(Page):
    # 是否恢复停电
    def inputSel_whether_recover_power_cut(self, index):
        self.click(*SuspectePowerCutLineQueryLocators.QRY_WHETHER_RECOVER_POWER_CUT)
        locator = self.get_select_locator(SuspectePowerCutLineQueryLocators.QRY_WHETHER_RECOVER_POWER_CUT_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 停电日期
    def inputDt_date(self, content):
        self.exec_script(SuspectePowerCutLineQueryLocators.DATE_JS)
        self.input(content, *SuspectePowerCutLineQueryLocators.QRY_DATE)

    # 停电时长
    def inputStr_power_cut_start(self, content):
        self.input(content, *SuspectePowerCutLineQueryLocators.QRY_POWER_CUT_START)

    def inputStr_power_cut_end(self, content):
        self.input(content, *SuspectePowerCutLineQueryLocators.QRY_POWER_CUT_END)

    # 查询按钮
    def btn_search(self):
        self.click(*SuspectePowerCutLineQueryLocators.BTN_SEARCH)


# 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测→疑似停电对象查询
class SuspectePowerCutObjectQueryPage(Page):
    # 是否线路停电
    def inputSel_whether_line_power_cut(self, index):
        self.click(*SuspectePowerCutObjectQueryLocators.QRY_WHETHER_LINE_POWER_CUT)
        locator = self.get_select_locator(SuspectePowerCutObjectQueryLocators.QRY_WHETHER_LINE_POWER_CUT_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 对象类型
    def inputSel_object_type(self, index):
        self.click(*SuspectePowerCutObjectQueryLocators.QRY_OBJECT_TYPE)
        locator = self.get_select_locator(SuspectePowerCutObjectQueryLocators.QRY_OBJECT_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 停电日期
    def inputDt_date(self, content):
        self.exec_script(SuspectePowerCutObjectQueryLocators.DATE_JS)
        self.input(content, *SuspectePowerCutObjectQueryLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*SuspectePowerCutObjectQueryLocators.BTN_SEARCH)
