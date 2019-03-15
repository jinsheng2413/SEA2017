# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tq_xl_rxs_page.py
@time: 2019-03-15 09:57:02
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→线损统计→线路日线损查询
class TqXlRxsPage(Page):
    # 选择人员
    def inputSel_select_person(self, option):
        self.selectDropDown(option)

    # 线路名称
    def inputStr_line_name(self, value):
        self.input(value)

    # 日期
    def inputDt_start_date(self, value):
        self.clean_label(value)
        self.inputDate(value)

    # 至
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
