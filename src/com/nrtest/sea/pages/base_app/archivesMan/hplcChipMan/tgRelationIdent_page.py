# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgRelationIdent_page.py
@time: 2019-04-11 14:38:39
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC芯片管理→台户关系识别:台户关系统计
class TgRelationIdentStatPage(Page):
    # 异常类型
    def inputSel_anomaly_type(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→档案管理→HPLC芯片管理→台户关系识别:台户关系明细
class TgRelationIdentDetailPage(Page):
    # 异常类型
    def inputSel_anomaly_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 规约
    def inputSel_tmnl_protocol(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
