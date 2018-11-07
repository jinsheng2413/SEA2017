# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossAbnormalReport_page.py
@time: 2018/11/2 11:06
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.tgLineLossStatisticsQuery.tgLineLossAbnormalReport_locators import \
    TgLineLossAbnormalReportLocators


# 高级应用→线损分析→台区线损统计查询→台区线损异常报表
class TgLineLossAbnormalReportPage(Page):
    # 线损维度
    def inputSel_line_loss_dimension(self, index):
        self.click(*TgLineLossAbnormalReportLocators.QRY_LINE_LOSS_DIMENSION)
        locator = self.get_select_locator(
            TgLineLossAbnormalReportLocators.QRY_LINE_LOSS_DIMENSION_VALUE, index)
        self.click(*locator)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(TgLineLossAbnormalReportLocators.DATE_JS)
        self.input(content, *TgLineLossAbnormalReportLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*TgLineLossAbnormalReportLocators.BTN_SEARCH)
