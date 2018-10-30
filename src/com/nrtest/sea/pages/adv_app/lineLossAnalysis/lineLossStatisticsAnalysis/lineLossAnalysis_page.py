# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossAnalysis_page.py
@time: 2018/10/30 16:21
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossStatisticsAnalysis.lineLossAnalysis_locators import \
    LineLossAnalysisLocators


# 高级应用→线损分析→线损统计分析→线路线损分析
class LineLossAnalysisPage(Page):
    # 线路编号
    def inputStr_line_no(self, content):
        self.input(content, *LineLossAnalysisLocators.QRY_LINE_NO)

    # 线路名称
    def inputStr_line_name(self, content):
        self.input(content, *LineLossAnalysisLocators.QRY_LINE_NAME)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(LineLossAnalysisLocators.DATE_JS)
        self.input(content, *LineLossAnalysisLocators.QRY_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*LineLossAnalysisLocators.BTN_SEARCH)
