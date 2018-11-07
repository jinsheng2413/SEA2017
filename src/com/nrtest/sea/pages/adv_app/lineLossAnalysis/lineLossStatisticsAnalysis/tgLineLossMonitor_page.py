# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossMonitor_page.py
@time: 2018/10/31 15:49
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.tgLineLossMonitor_locators import \
    TgLineLossMonitorLocators


# 高级应用→线损分析→线损统计分析→台区线损监测
class TgLineLossMonitorPage(Page):
    # 指标类型
    def inputSel_pointer_type(self, index):
        self.click(*TgLineLossMonitorLocators.QRY_POINTER_TYPE)
        locator = self.get_select_locator(
            TgLineLossMonitorLocators.QRY_POINTER_TYPE_VALUE, index)
        self.click(*locator)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(TgLineLossMonitorLocators.DATE_JS)
        self.input(content, *TgLineLossMonitorLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*TgLineLossMonitorLocators.BTN_SEARCH)
