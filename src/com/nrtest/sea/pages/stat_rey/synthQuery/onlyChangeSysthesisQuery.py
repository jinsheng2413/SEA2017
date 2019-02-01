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
from com.nrtest.sea.locators.other.base_g_locators import BaseTabLocators


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


# 统计查询→综合查询→专公变综合查询:日抄表数据
class DayReadDataPage(Page):
    # 显示方式
    def inputChk_display_type(self, option):
        self.clickRadioBox(option)

    # 从
    def inputDt_from_date(self, value):
        self.inputDate(value)

    # 到
    def inputDt_from_to(self, value):
        self.inputDate(value)

    # 是否显示所有终端信息
    def inputChk_display_all_tmnl_info(self, option):
        self.clickSingleCheckBox(option, is_multi_tab=True)

    # 用户编号
    def inputStr_tree_cons_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


from com.nrtest.common.base_page import Page


# 统计查询→综合查询→专公变综合查询:负荷日数据
class LoadDayDataPage(Page):


    # 数据类型
    def inputChk_data_type(self, option):
        self.clickRadioBox(option)

    # 时段类型
    def inputChk_time_type(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_day_date(self, value):
        self.inputDate(value)

    # 日期从
    def inputDt_date_from(self, value):
        self.inputDate(value)

    # 到
    def inputDt_date_to(self, value):
        self.inputDate(value)

    # 电量平衡类型
    def inputChk_ele_type(self, options):
        self.clickCheckBox_new(options)

    # 做功方式
    def inputChk_alphabet_power_type(self, options):
        self.clickCheckBox_new(options)

    # 充值次数
    def inputSel_time_value(self, value):
        self.click(BaseTabLocators.RECHARGE_TIME)
        locator = self.get_select_locator(BaseTabLocators.RECHARGE_TIME_VALUE, value)
        self.click(locator)




    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→专公变综合查询:实时抄表数据
class SynthqueryDataPage(Page):

    # 查询日期从
    def inputDt_query_time_from(self, value):
        self.inputDate(value)

    # 到
    def inputDt_query_time_to(self, value):
        self.inputDate(value)

    # 是否显示正向有功电能量
    def inputChk_or_power(self, options):
        self.clickCheckBox_new(options)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
