# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserMoneyCheck_page.py
@time: 2018/8/15 0015 14:36
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→费控管理→本地费控→低压用户余额查看:余额统计
class BalanceCount_page(Page):

    # 日期时间
    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 高级应用→费控管理→本地费控→低压用户余额查看:余额查看
class BalanceCheck_page(Page):

    # 工单编号
    def inputStr_app_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 接收时间
    def inputDt_receive_date(self, value):
        self.inputDate(value)

    # 执行状态
    def inputSel_execute_status(self, value):
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

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 电表局编号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
