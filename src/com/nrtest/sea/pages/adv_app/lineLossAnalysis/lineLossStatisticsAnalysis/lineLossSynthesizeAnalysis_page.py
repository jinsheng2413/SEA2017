# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossSynthesizeAnalysis_page.py
@time: 2018/10/31 14:02
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损统计分析→线损综合分析
class LineLossSynthesizeAnalysisPage(Page):
    # 线损类别
    def inputSel_line_loss_type(self, index):
        # self.click(*LineLossSynthesizeAnalysisLocators.QRY_LINE_LOSS_TYPE)
        # locator = locator = self.get_select_locator(
        #     LineLossSynthesizeAnalysisLocators.QRY_LINE_LOSS_TYPE_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(index)

    # 查询日期
    def inputDt_date(self, content):
        # self.exec_script(LineLossSynthesizeAnalysisLocators.DATE_JS)
        ###self.input(content, *LineLossSynthesizeAnalysisLocators.QRY_DATE)
        self.inputDate(content)

    # 按日期统计类型
    def inputDTTAB_statDateType(self, name):
        self.clickDt_Tab(name)

    # 查询按钮
    def btn_search(self):
        # self.click(*LineLossSynthesizeAnalysisLocators.BTN_SEARCH)
        self.btn_query()
