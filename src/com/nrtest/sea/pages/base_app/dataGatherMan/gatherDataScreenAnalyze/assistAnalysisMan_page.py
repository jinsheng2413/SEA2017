# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: assistAnalysisMan_page.py
@time: 2019-02-15 14:24:49
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集数据甄别分析→辅助分析管理
class AssistAnalysisManPage(Page):
    # 采集点编号
    def inputStr_cp_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
