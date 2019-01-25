# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→费控管理→本地费控→低压用户购电参数下发
class LowUserBuyEleParaGiveOut_page(Page):
    # 工单编号
    def inputStr_app_no(self, value):
        self.clean_label(value)
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 执行状态
    def inputSel_execute_status(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 接收时间
    def inputDt_start_time(self, value):
        self.clean_label(value)
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
