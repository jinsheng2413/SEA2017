# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: partialPressureLineLossAnalysis_page.py
@time: 2018/10/30 17:24
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损统计分析→分压线损分析
class PartialPressureLineLossAnalysisPage(Page):
    # 电压等级
    def inputSel_volt_code(self, index):
        self.selectCheckBox(index)

    # 按日期类型选择
    def inputChk_date_type_sel(self, tab_name):
        self.clickDt_Tab(tab_name)

    # 季度选择
    def inputChk_quarter_sel(self, value):
        self.clickRadioBox(value)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
