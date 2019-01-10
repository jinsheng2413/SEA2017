# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class CollectSuccessRateStatPage(Page):
    # 查询时间
    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 查询方式
    def inputChk_query_type(self, name):
        self.clickRadioBox(name)

    # 查询
    def btn_qry(self):
        self.btn_query()
