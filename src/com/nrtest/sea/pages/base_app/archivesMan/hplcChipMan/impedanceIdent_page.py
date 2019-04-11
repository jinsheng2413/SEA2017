# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: impedance_ident_page.py
@time: 2019-04-11 16:42:44
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC芯片管理→阻抗识别
class ImpedanceIdentPage(Page):
    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 电表地址
    def inputStr_comm_addr(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
