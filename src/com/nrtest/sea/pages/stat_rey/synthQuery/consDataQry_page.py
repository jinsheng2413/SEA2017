# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: consDataQry_page.py
@time: 2019-02-18 11:12:42
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→用户数据:基本档案
class ConsdataqryFilePage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→用户数据:数据展示
class ConsdataqryDisplayPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # TAB页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 曲线类型
    def inputChk_curve_type(self, option):
        self.clickRadioBox(option)

    # 电表
    def inputSel_meter_no(self, option):
        self.selectDropDown(option)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 开始日期
    def inputDt_stat_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 日期类型
    def inputChk_date_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
