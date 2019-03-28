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
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 查询时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 是否选终端在线
    def inputChk_tmnl_online(self, item):
        self.clickSingleCheckBox(item)

    # 查询
    def btn_qry(self):
        self.btn_query()
