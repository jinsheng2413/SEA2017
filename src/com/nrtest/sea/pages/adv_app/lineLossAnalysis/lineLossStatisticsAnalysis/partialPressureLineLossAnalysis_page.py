# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: partialPressureLineLossAnalysis_page.py
@time: 2018/10/30 17:24
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.partialPressureLineLossAnalysis_locators import \
    PartialPressureLineLossAnalysisLocators


# 高级应用→线损分析→线损统计分析→分压线损分析
class PartialPressureLineLossAnalysisPage(Page):
    # 电压等级
    def inputSel_voltage_level(self, index):
        if index == 'c':
            self._find_element(*PartialPressureLineLossAnalysisLocators.QRY_VOLTAGE_LEVEL)
        else:
            self.click(*PartialPressureLineLossAnalysisLocators.QRY_VOLTAGE_LEVEL)
            locator = self.get_select_locator(PartialPressureLineLossAnalysisLocators.QRY_VOLTAGE_LEVEL_VALUE, index)
            self.click(*locator)
            self.click(*PartialPressureLineLossAnalysisLocators.QRY_VOLTAGE_LEVEL)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(PartialPressureLineLossAnalysisLocators.DATE_JS)
        self.input(content, *PartialPressureLineLossAnalysisLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*PartialPressureLineLossAnalysisLocators.BTN_SEARCH)
