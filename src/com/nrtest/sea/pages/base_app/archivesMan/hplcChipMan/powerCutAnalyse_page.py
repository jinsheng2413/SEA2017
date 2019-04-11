# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: powerCutAnalyse_page.py
@time: 2019-04-11 12:27:45
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC芯片管理→停上电分析:停电统计
class PowerCutAnalyseStatPage(Page):
    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 统计维度
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→档案管理→HPLC芯片管理→停上电分析:停电明细
class PowerCutAnalyseDetailPage(Page):
    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询维度
    def inputChk_qry_type(self, option):
        self.clickRadioBox(option)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)

    # 规约
    def inputSel_tmnl_protocol(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
