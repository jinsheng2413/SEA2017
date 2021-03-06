# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: periodUsePowerAnalyse_page.py
@time: 2019-02-19 14:45:34
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→数据分析→电量分析→时段用电分析
class periodUsePowerAnalysePage(Page):
    # 统计类型
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option)

    # 统计月份
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
