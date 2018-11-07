# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossStatisticsQuery_page.py
@time: 2018/10/31 14:44
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossStatisticsQuery_locators import \
    LineLossStatisticsQueryLocators


# 高级应用→线损分析→线损统计分析→线损统计查询
class LineLossStatisticsQueryPage(Page):
    # 线损分类
    def inputSel_line_loss_type(self, index):
        self.click(*LineLossStatisticsQueryLocators.QRY_LINE_LOSS_TYPE)
        locator = self.get_select_locator(LineLossStatisticsQueryLocators.QRY_LINE_LOSS_TYPE_VALUE, index)
        self.click(*locator)

    # 线损率
    def inputSel_line_loss_rate(self, index):
        self.click(*LineLossStatisticsQueryLocators.QRY_LINE_LOSS_RATE)
        locator = self.get_select_locator(LineLossStatisticsQueryLocators.QRY_LINE_LOSS_RATE_VALUE, index)
        self.click(*locator)

    def inputStr_line_loss_rate(self, content):
        self.input(content, *LineLossStatisticsQueryLocators.QRY_LINE_LOSS_RATE_INPUT)

    # 日期
    def inputDt_date(self, content):
        self.exec_script(LineLossStatisticsQueryLocators.DATE_JS)
        self.input(content, *LineLossStatisticsQueryLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*LineLossStatisticsQueryLocators.BTN_SEARCH)
