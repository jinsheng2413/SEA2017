# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: specialUserBalanceQuery_page.py
@time: 2018/8/19 0019 9:04
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→费控管理→本地费控→专变用户余额查看
class SpecialUserBalanceQueryPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 越限类型
    def inputSel_over_type(self, index):
        self.selectDropDown(index)

    # 召测日期
    def inputDt_call_date(self, value):
        self.inputDate(value)

    def btn_qry(self):
        self.btn_query()
