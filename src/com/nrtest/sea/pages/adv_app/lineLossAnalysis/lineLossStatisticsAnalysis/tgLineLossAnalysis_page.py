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
        ###self.input(content, *TgLineLossAnalysisLocators.QRY_TG_NO)

        self.input(content)


    # 台区名称
    def inputStr_tg_name(self, content):
        ###self.input(content, *TgLineLossAnalysisLocators.QRY_TG_NAME)

        self.input(content)


    # 安装率
    def inputSel_install_rate(self, index):
        self.click(TgLineLossAnalysisLocators.QRY_INSTALL_RATE)
        locator = locator = self.get_select_locator(
            TgLineLossAnalysisLocators.QRY_INSTALL_RATE_VALUE, index)
        self.click(locator)
        # self.selectDropDown(index)

    def inputStr_installation_rate(self, content):
        # self.input(
        # content, *TgLineLossAnalysisLocators.QRY_INSTALL_RATE_INPUT)
        self.input(content)
    # 抄读成功率
    def inputSel_read_success_rate(self, index):
        self.click(TgLineLossAnalysisLocators.QRY_READ_SUCCESS_RATE)
        locator = locator = self.get_select_locator(
            TgLineLossAnalysisLocators.QRY_READ_SUCCESS_RATE_VALUE, index)
        self.click(locator)
        # self.selectDropDown(index)

    def inputStr_read_success_rate(self, content):
        # self.input(
        # content, *TgLineLossAnalysisLocators.QRY_READ_SUCCESS_RATE_INPUT)
        self.input(content)

    # 线损率
    def inputSel_line_loss_rate(self, index):
        self.click(TgLineLossAnalysisLocators.QRY_LINE_LOSS_RATE)
        locator = locator = self.get_select_locator(
            TgLineLossAnalysisLocators.QRY_LINE_LOSS_RATE_VALUE, index)
        self.click(locator)
        # self.selectDropDown(index)

    def inputStr_line_loss_rate(self, content):
        ###self.input(content, *TgLineLossAnalysisLocators.QRY_LINE_LOSS_RATE_INPUT)

        # self.input(content)
        self.input(content)

        # 运算类型

    def inputChk_line_loss_type(self, value):
        self.clickRadioBox(value)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

    # 日期选择类型
    def inputDt_by_date_type(self, tab_name):
        self.clickDt_Tab(tab_name)

    # 查询时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 可算类型
    def inputChk_tg_type(self, value):
        self.clickRadioBox(value)
