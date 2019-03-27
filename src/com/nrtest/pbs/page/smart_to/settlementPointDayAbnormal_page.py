# -*- coding: utf-8 -*-

"""
@author:郭春彪
@license: (C) Copyright 2019, Nari.
@file: puiu.py
@time: 2019-03-15 09:44
@desc:
"""
from com.nrtest.common.base_page import Page


# 智能研判-->结算点日异常
class SettlementPointDayAbnormal_page(Page):

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)
