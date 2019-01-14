# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: availableCapacityAnalyse_page.py
@time: 2018/9/27 15:43
@desc:
"""

from com.nrtest.common.base_page import Page

# 高级应用--》配变负载分析--》报装可用容量分析
class AvailableCapacityAnalysePage(Page):

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 负载率
    def inputStr_load_rate(self, value):
        self.input(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()
