# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: areaLineLossAnalysis_page.py
@time: 2018/10/31 10:05
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损管理→线损统计分析→区域线损分析
class AreaLineLossAnalysisPage(Page):
    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 按日期类型选择
    def inputChk_qry_date_type(self, tab_name):
        self.clickDt_Tab(tab_name)

    # 季度选择
    def inputChk_quarter_sel(self, value):
        self.clickRadioBox(value)

    # 电量供应类型
    def inputChk_ele_type(self, name):
        self.clickRadioBox(name)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()
