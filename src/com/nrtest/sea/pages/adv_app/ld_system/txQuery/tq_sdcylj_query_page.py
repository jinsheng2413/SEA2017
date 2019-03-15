# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tq_sdcylj_query_page.py
@time: 2019-03-15 11:21:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→查询管理→台区售电侧月累计查询
class TqSdcyljQueryPage(Page):
    # 月份
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 至
    def inputDt_to(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
