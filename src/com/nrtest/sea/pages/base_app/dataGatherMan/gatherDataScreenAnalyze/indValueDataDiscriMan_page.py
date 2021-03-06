# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: indValueDataDiscriMan_page.py
@time: 2019-02-15 11:29:29
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集数据甄别分析→示值类数据甄别管理
class IndValueDataDiscriManPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 用户分类
    def inputSel_cons_type(self, option):
        self.selectDropDown(option)

    # 终端编号
    def inputStr_tmnl_no(self, value):
        self.input(value)

    # 终端名称
    def inputStr_tmnl_name(self, value):
        self.input(value)

    # 终端类型
    def inputSel_tmnl_type(self, option):
        self.selectDropDown(option)

    # 起始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 终止日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 抄表例日
    def inputStr_meter_day(self, value):
        self.input(value)

    # 电能表编号
    def inputStr_meter_no(self, value):
        self.input(value)

    # 电能表资产编号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 甄别标志
    def inputSel_screen_sign(self, value):
        self.selectDropDown(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
