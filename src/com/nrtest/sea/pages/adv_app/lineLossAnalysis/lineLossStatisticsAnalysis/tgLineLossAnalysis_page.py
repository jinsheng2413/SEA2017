# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossAnalysis_page.py
@time: 2018/10/30 13:59
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.tgLineLossAnalysis_locators import \
    TgLineLossAnalysisLocators


# 高级应用→线损分析→线损统计分析→台区线损分析
class TgLineLossAnalysisPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content, *TgLineLossAnalysisLocators.QRY_TG_NO)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content, *TgLineLossAnalysisLocators.QRY_TG_NAME)

    # 安装率
    def inputSel_installation_rate(self, index):
        self.click(*TgLineLossAnalysisLocators.QRY_INSTALLATION_RATE)
        locator = self.get_select_locator(
            TgLineLossAnalysisLocators.QRY_INSTALLATION_RATE_VALUE, index)
        self.click(*locator)

    def inputStr_installation_rate(self, content):
        self.input(
            content, *TgLineLossAnalysisLocators.QRY_INSTALLATION_RATE_INPUT)

    # 抄读成功率
    def inputSel_read_success_rate(self, index):
        self.click(*TgLineLossAnalysisLocators.QRY_READ_SUCCESS_RATE)
        locator = self.get_select_locator(
            TgLineLossAnalysisLocators.QRY_READ_SUCCESS_RATE_VALUE, index)
        self.click(*locator)

    def inputStr_read_success_rate(self, content):
        self.input(
            content, *TgLineLossAnalysisLocators.QRY_READ_SUCCESS_RATE_INPUT)

    # 线损率
    def inputSel_line_loss_rate(self, index):
        self.click(*TgLineLossAnalysisLocators.QRY_LINE_LOSS_RATE)
        locator = self.get_select_locator(
            TgLineLossAnalysisLocators.QRY_LINE_LOSS_RATE_VALUE, index)
        self.click(*locator)

    def inputStr_line_loss_rate(self, content):
        self.input(content, *TgLineLossAnalysisLocators.QRY_LINE_LOSS_RATE_INPUT)

    # 查询按钮
    def btn_search(self):
        self.click(*TgLineLossAnalysisLocators.BTN_SEARCH)
