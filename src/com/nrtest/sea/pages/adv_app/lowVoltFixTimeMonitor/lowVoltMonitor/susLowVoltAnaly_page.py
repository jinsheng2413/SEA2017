# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: susLowVoltAnaly_page.py
@time: 2019-02-13 15:11:12
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→低压固定时间点电压电流监测→低电压监测→疑似低电压分析:疑似低电压用户统计
class SusLowVoltAnalyStaticPage(Page):
    # 接线方式
    def inputSel_wiring_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 月份
    def inputDt_query_date(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 低压天数
    def inputStr_low_volt_days(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 高级应用→低压固定时间点电压电流监测→低电压监测→疑似低电压分析:疑似低电压用户明细
class SusLowVoltAnalyDetailPage(Page):
    # 接线方式
    def inputSel_wiring_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 月份
    def inputDt_query_date(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 低压天数
    def inputStr_low_volt_days(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
