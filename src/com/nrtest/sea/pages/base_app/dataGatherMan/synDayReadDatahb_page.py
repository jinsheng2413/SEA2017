# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: synDayReadDatahb_page.py
@time: 2019-02-14 16:15:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→数据发布(河北)
class SynDayReadDatahbPage(Page):
    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
