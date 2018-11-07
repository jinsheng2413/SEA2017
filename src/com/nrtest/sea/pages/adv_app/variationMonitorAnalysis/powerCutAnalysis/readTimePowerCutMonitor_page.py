# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: readTimePowerCutMonitor_page.py
@time: 2018/11/7 10:05
@desc:
"""
from com.nrtest.common.base_page import Page
from src.com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.readTimePowerCutMonitor_locators import *


# 高级应用→配变监测分析→停电分析→实时停电监测
class ReadTimePowerCutMonitorPage(Page):
    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(ReadTimePowerCutMonitorLocators.DATE_JS)
        self.input(content, *ReadTimePowerCutMonitorLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*ReadTimePowerCutMonitorLocators.BTN_SEARCH)


# 高级应用→配变监测分析→停电分析→实时停电监测→实时停电明细
class ReadTimePowerCutDetailPage(Page):
    # 日期
    def inputDt_date(self, content):
        self.exec_script(ReadTimePowerCutDetailLocators.DATE_JS)
        self.input(content, *ReadTimePowerCutDetailLocators.QRY_DATE)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(*ReadTimePowerCutDetailLocators.QRY_CONS_TYPE)
        locator = self.get_select_locator(ReadTimePowerCutDetailLocators.QRY_CONS_TYPE_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 信息推送
    def inputSel_information_push(self, index):
        self.click(*ReadTimePowerCutDetailLocators.QRY_INFORMATION_PUSH)
        locator = self.get_select_locator(ReadTimePowerCutDetailLocators.QRY_INFORMATION_PUSH_VALUE, index)
        self.click(*locator)
        self.delDropdownBoxHtml()

    # 查询按钮
    def btn_search(self):
        self.click(*ReadTimePowerCutDetailLocators.BTN_SEARCH)
