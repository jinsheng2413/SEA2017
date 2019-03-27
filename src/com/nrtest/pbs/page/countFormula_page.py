# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: countFormula_page.py
@time: 2019/3/5 0005 15:17
@desc:
"""
from com.nrtest.common.base_page import Page


class CountFormula_page(Page):
    # 计算公式
    def inputStr_formula_name(self, value):
        self.input(value)

    # 公式别名
    def inputStr_formula_alias(self, value):
        self.curr_input(value)

    # 计算时间间隔
    def inoutSel_conputer_Interval(self, value):
        self.selectDropDown(value)

    # 所属对象
    def inputStr_object(self, value):
        self.curr_input(value, is_multi_elements=True)

    # 分时时标
    def inputStr_minute_scale(self, value):
        self.inputDate(value)

    # 开始时
    def inputStr_day_time(self, value):
        self.inputDate(value)

    # 开始时
    def inputStr_month_time(self, value):
        self.inputDate(value)

    # 公式类型
    def inoutSel_formula_type(self, value):
        self.selectDropDown(value)

    def btn_qry(self):
        self.btn_query(is_multi_tab=True, btn_name='确认')
