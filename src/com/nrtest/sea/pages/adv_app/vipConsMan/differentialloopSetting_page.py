# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: differentialloopSetting_page.py
@time: 2018-11-06 10:50
@desc:
"""

from com.nrtest.common.base_page import Page


class DifferentialloopSetting_Page(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 选择指定行
    def inputRow_select_row(self, row_item):
        self.select_row(row_item)

    # 查询
    def btn_qry(self):
        self.btn_query()
