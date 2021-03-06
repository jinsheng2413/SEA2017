# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: powerCurveAnalyse_page.py
@time: 2019-02-19 10:33:03
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→数据分析→电量分析→电量曲线统计:电量统计
class PowerStatPage(Page):
    # 统计类型
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option)

    # 统计月份
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 同比月份
    def inputDt_year_date(self, value):
        self.inputDate(value)

    # 环比月份
    def inputDt_link_date(self, value):
        self.inputDate(value)

    # 月份类型
    def inputChk_date_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 统计查询→数据分析→电量分析→电量曲线统计:电量明细
class PowerDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 行业
    def inputSel_trade(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 受电容量
    def inputSel_ele_capacity(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
