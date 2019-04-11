# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: phaseIdent_page.py
@time: 2019-04-11 15:24:48
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC芯片管理→相位识别:相位统计
class PhaseIdentStatPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→档案管理→HPLC芯片管理→相位识别:相位明细
class PhaseIdentDetailPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 规约
    def inputSel_tmnl_protocol(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
