# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: TerminalVersion_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class TerminalVersionPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *TerminalVersionLocators.QRY_CONS_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)  # , *TerminalVersionLocators.QRY_TMNL_ADDR)

    # 查询时间
    def inputDt_query_date(self, value):
        # self.input(value, *TerminalVersionLocators.QRY_DATE)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(TerminalVersionLocators.BTN_QRY)
        self.btn_query()
