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
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 按日期类型选择
    def inputChk_qry_date_type(self, tab_name):
        self.clickDt_Tab(tab_name)

    # 季度选择
    def inputChk_quarter_sel(self, value):
        self.clickRadioBox(value)

    # TAB页选择
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()
