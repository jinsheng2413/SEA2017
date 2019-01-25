# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineLossAnalysis_page.py
@time: 2018/10/30 16:21
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损统计分析→线路线损分析
class LineLossAnalysisPage(Page):
    # 线路编号
    def inputStr_line_no(self, content):
        self.input(content)

    # 线路名称
    def inputStr_line_name(self, content):
        self.input(content)

    # 查询日期
    def inputDt_query_date(self, content):
        self.input(content)

    # 按时间统计类型
    def inputDt_stat_date_type(self, name):
        self.clickDt_Tab(name)

    # 组合单元
    def inputChk_composition_unit(self, name):
        self.clickSingleCheckBox(name)

    # 线损类型
    def inputSChk_line_loss_type(self, name):
        self.clickRadioBox(name)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
