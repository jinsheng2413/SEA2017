# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: lowPressureQuery_page.py
@time: 2018-11-01 16:16
@desc:
"""

from com.nrtest.common.base_page import Page


class LowPressureQuery_Page(Page):
    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 日期
    def inputDt_query_date(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
