# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tq_rxslxbyx_query_page.py
@time: 2019-03-15 11:15:52
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→查询管理→台区日线损连续不优秀查询
class TqRxslxbyxQueryPage(Page):
    # 月份
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 线损电量
    def inputStr_line_loss(self, value):
        self.input(value)

    # 至
    def inputStr_to(self, value):
        self.input(value)

    # 连续天数
    def inputSel_consecutive_days(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
