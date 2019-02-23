# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: lowPressureMonitor_page.py
@time: 2018-11-01 11:03
@desc:
"""

from com.nrtest.common.base_page import Page


class LowPressureMonitor_Page(Page):
    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 用户定义类别
    def inputSel_cons_define_type(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()