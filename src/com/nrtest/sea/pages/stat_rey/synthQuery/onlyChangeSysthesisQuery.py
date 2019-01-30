# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: onlyChangeSysthesisQuery.py
@time: 2019/1/30 0030 8:51
@desc:
"""
from com.nrtest.common.base_page import Page


class LoadCountPage(Page):
    # 数据类型
    def inputCHR_dataType(self, value):
        self.dateType = s = value.split(';;')[1]
        self.clickRadioBox(value, is_multi_tab=True, is_multi_elements=True)

    def inputDT_monthDay(self, value):
        self.inputDate(value)

    def inputDT_yearDay(self, value):
        self.inputDate(value)

    # 日期
    def inputDT_displayDate(self, value):
        self.inputDate(value)

    def inputCHR_quantityType(self, value):
        self.clickRadioBox(value, is_multi_tab=True, is_multi_elements=True)

    # 曲线类型
    def inputCHR_power_type(self, value):
        self.clickCheckBox_new(value)

    # 曲线类型
    def inputCHR_max_min(self, value):
        self.clickCheckBox_new(value)

    # 曲线间隔
    def inputStr_curveBetween(self, value):
        self.selectDropDown(value)

    def btn_qry(self):
        self.btn_query(True)
