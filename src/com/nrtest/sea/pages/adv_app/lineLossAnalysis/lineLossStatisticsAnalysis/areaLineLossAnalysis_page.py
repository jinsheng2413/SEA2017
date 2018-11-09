# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: areaLineLossAnalysis_page.py
@time: 2018/10/31 10:05
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.areaLineLossAnalysis_locators import \
    AreaLineLossAnalysisLocators


# 高级应用→线损分析→线损统计分析→区域线损分析
class AreaLineLossAnalysisPage(Page):
    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(AreaLineLossAnalysisLocators.DATE_JS)
        self.input(content, *AreaLineLossAnalysisLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*AreaLineLossAnalysisLocators.BTN_SEARCH)