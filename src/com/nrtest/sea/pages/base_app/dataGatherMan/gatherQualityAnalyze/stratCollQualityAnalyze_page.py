# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: stratCollQualityAnalyze_page.py
@time: 2019-02-14 14:40:53
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量分析→关口采集质量分析:采集成功率
class StratCollQualityAnalyzePage(Page):
    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→数据采集管理→采集质量分析→关口采集质量分析:采集失败列表明细
class StratCollQualityAnalyzeDetailPage(Page):
    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)

    # 电表名称
    def inputStr_meter_name(self, value):
        self.input(value)

    # 采集名称
    def inputStr_gather_name(self, value):
        self.input(value)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
