# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: preventingElectricityStolen_page.py
@time: 2019-02-20 13:05:23
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→双回路对比分析
class PreventingElectricityStolenPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 选择要显示点数
    def inputChk_display_num(self, option):
        self.clickRadioBox(option)

    # 统计日期从
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
