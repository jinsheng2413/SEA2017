# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossAnalysisJibei_page.py
@time: 2018/10/31 16:23
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.tgLineLossAnalysisJibei_locators import \
    TgLineLossAnalysisJibeiLocators


# 高级应用→线损分析→线损统计分析→台区线损分析（冀北）
class TgLineLossAnalysisJibeiPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content, *TgLineLossAnalysisJibeiLocators.QRY_TG_NO)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content, *TgLineLossAnalysisJibeiLocators.QRY_TG_NAME)

    # 安装率
    def inputSel_installation_rate(self, index):
        self.click(TgLineLossAnalysisJibeiLocators.QRY_INSTALLATION_RATE)
        locator = self.get_select_locator(
            TgLineLossAnalysisJibeiLocators.QRY_INSTALLATION_RATE_VALUE, index)
        self.click(locator)

    def inputStr_installation_rate(self, content):
        self.input(
            content, *TgLineLossAnalysisJibeiLocators.QRY_INSTALLATION_RATE_INPUT)

    # 抄读成功率
    def inputSel_read_success_rate(self, index):
        self.click(TgLineLossAnalysisJibeiLocators.QRY_READ_SUCCESS_RATE)
        locator = self.get_select_locator(
            TgLineLossAnalysisJibeiLocators.QRY_READ_SUCCESS_RATE_VALUE, index)
        self.click(locator)

    def inputStr_read_success_rate(self, content):
        self.input(
            content, *TgLineLossAnalysisJibeiLocators.QRY_READ_SUCCESS_RATE_INPUT)

    # 线损率
    def inputSel_line_loss_rate(self, index):
        self.click(TgLineLossAnalysisJibeiLocators.QRY_LINE_LOSS_RATE)
        locator = self.get_select_locator(
            TgLineLossAnalysisJibeiLocators.QRY_LINE_LOSS_RATE_VALUE, index)
        self.click(locator)

    def inputStr_line_loss_rate(self, content):
        self.input(
            content, *TgLineLossAnalysisJibeiLocators.QRY_LINE_LOSS_RATE_INPUT)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(TgLineLossAnalysisJibeiLocators.DATE_JS)
        self.input(content, *TgLineLossAnalysisJibeiLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(TgLineLossAnalysisJibeiLocators.BTN_SEARCH)
