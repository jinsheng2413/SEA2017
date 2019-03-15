# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tqydb_dy_page.py
@time: 2019-03-15 09:39:14
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→线损统计→台区同期月优秀达标查询(壹)
class TqydbDyPage(Page):
    # 日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 至日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
