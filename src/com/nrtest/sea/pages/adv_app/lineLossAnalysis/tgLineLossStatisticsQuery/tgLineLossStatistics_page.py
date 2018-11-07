# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossStatistics_page.py
@time: 2018/11/1 16:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossStatistics_locators import \
    TgLineLossStatisticsLocators


# 高级应用→线损分析→台区线损统计查询→台区线损统计
class TgLineLossStatisticsPage(Page):
    # 线损维度
    def inputSel_line_loss_dimension(self, index):
        self.click(*TgLineLossStatisticsLocators.QRY_LINE_LOSS_DIMENSION)
        locator = self.get_select_locator(TgLineLossStatisticsLocators.QRY_LINE_LOSS_DIMENSION_VALUE, index)
        self.click(*locator)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(TgLineLossStatisticsLocators.DATE_JS)
        self.input(content, *TgLineLossStatisticsLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*TgLineLossStatisticsLocators.BTN_SEARCH)
