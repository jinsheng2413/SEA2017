# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: onlyChangeSysthesisQuery.py
@time: 2019/1/30 0030 8:51
@desc:
"""
from com.nrtest.common.base_page import Page


# 统计查询--综合查询--专公变综合查询:负荷统计
class LoadCountPage(Page):
    # 数据类型
    def inputChk_data_type(self, value):
        self.dateType = s = value.split(';;')[1]
        self.clickRadioBox(value, is_multi_tab=True, is_multi_elements=True)

    def inputDt_month_day(self, value):
        self.inputDate(value)

    def inputDt_year_day(self, value):
        self.inputDate(value)

    # 日期
    def inputDt_display_date(self, value):
        self.inputDate(value)

    def inputChk_quantity_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True, is_multi_elements=True)

    # 曲线类型
    def inputChk_power_type(self, value):
        self.clickCheckBox_new(value)

    # 曲线类型
    def inputCHR_max_min(self, value):
        self.clickCheckBox_new(value)

    # 曲线间隔
    def inputStr_curve_between(self, value):
        self.selectDropDown(value)

    def btn_qry(self):
        self.btn_query(True)


# 统计查询--综合查询--专公变综合查询:电量曲线图
class EleMapPage(Page):
    # 数据类型
    def inputChk_data_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_collect_time(self, value):
        self.inputDate(value)

    # 做功类型
    def inputChk_have_power_type(self, value):
        self.clickCheckBox_new(value, is_multi_tab=True)

    # 电量获取方式
    def inputChk_ele_get_type(self, value):
        self.clickRadioBox(value)

    def btn_qry(self):
        self.btn_query(True)
