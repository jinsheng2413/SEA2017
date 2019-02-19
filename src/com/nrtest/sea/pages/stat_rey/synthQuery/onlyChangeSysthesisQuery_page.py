# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: onlyChangeSysthesisQuery_page.py
@time: 2019/1/30 0030 8:51
@desc:
"""
from com.nrtest.common.base_page import Page

# 统计查询--综合查询--专公变综合查询:负荷统计

# 统计查询--综合查询--专公变综合查询：负荷统计
from com.nrtest.sea.locators.stat_rey.synthQuery.onlyChangeSysthesisQuery_locators import LoadDayDataLocators


class LoadCountPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 电能表
    def inputSel_meter(self, option):
        self.selectDropDown(option)

    # 数据类型
    def inputChk_data_type(self, option):
        self.clickRadioBox(option, True, True)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 瞬时量
    def inputChk_quantity_type(self, option):
        self.clickRadioBox(option)

    # 有功
    def inputChk_power_type(self, options):
        self.clickCheckBox_new(options)

    # 积分曲线
    def inputChk_integral_curve(self, option):
        self.clickSingleCheckBox(option)

    # 曲线间隔
    def inputSel_curve_period(self, option):
        self.selectDropDown(option)

    # 最大最小值分类
    def inputChk_max_min_type(self, options):
        self.clickCheckBox_new(options)

    def btn_qry(self):
        self.btn_query(True)


# 统计查询--综合查询--专公变综合查询:电量曲线图
class EleMapPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 电能表
    def inputSel_meter(self, option):
        self.selectDropDown(option)

    # 数据类型
    def inputChk_data_type(self, option):
        self.clickRadioBox(option, True, True)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 正反功率值分类
    def inputChk_power_type(self, options):
        self.clickCheckBox_new(options)

    # 电量获取方式
    def inputChk_ele_get_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→专公变综合查询:日抄表数据
class DayReadDataPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 显示方式
    def inputChk_display_type(self, option):
        self.clickRadioBox(option)

    # 从
    def inputDt_from_date(self, value):
        self.inputDate(value)

    # 到
    def inputDt_to_date(self, value):
        self.inputDate(value)

    # 是否显示所有终端信息
    def inputChk_disp_all(self, options):
        self.clickSingleCheckBox(options, True, True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


from com.nrtest.common.base_page import Page


# 统计查询→综合查询→专公变综合查询:负荷日数据
class LoadDayDataPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 电能表
    def inputSel_meter(self, option):
        self.selectDropDown(option)

    # 数据类型
    def inputChk_data_type(self, option):
        self.clickRadioBox(option, True, True)

    # 时段类型
    def inputChk_time_type(self, option):
        self.clickRadioBox(option, True, True)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 日期从
    def inputDt_from_date(self, value):
        self.inputDate(value)

    # 到
    def inputDt_to_date(self, value):
        self.inputDate(value)

    # 一二次侧
    def inputSel_ps_side(self, option):
        self.specialDropdown(option, LoadDayDataLocators.PS_SIDE)

    # PQUI
    def inputChk_pqui(self, options):
        self.clickCheckBox_new(options)

    # 功率电流平衡度
    def inputChk_pi_balance_type(self, options):
        self.clickCheckBox_new(options)
    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→专公变综合查询:实时抄表数据
class SynthqueryDataPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 查询日期从
    def inputDt_from_date(self, value):
        self.inputDate(value)

    # 电能表
    def inputSel_meter(self, option):
        self.selectDropDown(option)

    # 到
    def inputDt_to_date(self, value):
        self.inputDate(value)

    # 是否显示正向有功电能量
    def inputChk_disp_all(self, options):
        self.clickCheckBox_new(options)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→专公变综合查询:终端事件
class TmnlEventPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 电能表
    def inputSel_meter(self, option):
        self.selectDropDown(option)

    # 从
    def inputDt_from_date(self, value):
        self.inputDate(value)

    # 到
    def inputDt_to_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→专公变综合查询:采集点信息/用户档案
class TgQueryCpPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 电能表
    def inputSel_meter(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)

# 统计查询→综合查询→专公变综合查询:变压器负载率监控
class TransformerLoadRateMonitoringPage(Page):
    # 终端地址
    def inputSel_tmnl_addr(self, option):
        self.selectDropDown(option)

    # 电能表
    def inputSel_meter(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
