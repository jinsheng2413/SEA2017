# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterDataQuery_page.py
@time: 2018/10/9 16:45
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表数据查询:抄表明细
class MeterDataQueryDetailPage(Page):
    # 日冻结曲线类型
    def inputChk_day_freeze_curve_type(self, option):
        self.clickRadioBox(option)
    # 抄表段号
    def inputStr_mr_sect_no(self, content):
        self.input(content)

    # 电表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 数据类别
    def inputSel_data_sort(self, option):
        self.selectDropDown(option)

    # 电能表抄读状态
    def inputSel_meter_read_status(self, index):
        self.selectDropDown(index)

    # 终端运行状态
    def inputSel_tmnl_run_status(self, index):
        self.selectDropDown(index)

    # 农排用户选择
    def inputSel_user_select(self, index):
        self.selectDropDown(index)

    # 用户类别
    def inputSel_cons_sort(self, index):
        self.selectDropDown(index)

    # 采集情况
    def inputChk_read_status(self, index):
        self.clickCheckBox_new(index)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)

# 统计查询→综合查询→抄表数据查询:抄表失败统计
class MeterDataQueryCountPage(Page):
    # 日冻结曲线类型
    def inputChk_day_freeze_curve_type(self, option):
        self.clickRadioBox(option)

    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 相位
    def inputSel_phase_code(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→抄表数据查询:抄表失败明细
class MeterDataQueryFailDetailPage(Page):
    # 日冻结曲线类型
    def inputChk_day_freeze_curve_type(self, option):
        self.clickRadioBox(option)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option)

    # 相位
    def inputSel_phase_code(self, option):
        self.selectDropDown(option)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 到
    def inputDt_to_date(self, value):
        self.inputDate(value)

    # 数据类别
    def inputChk_data_sort(self, option):
        self.clickRadioBox(option)

    # 电能表抄读状态
    def inputSel_meter_read_status(self, option):
        self.selectDropDown(option)

    # 终端运行状态
    def inputSel_tmnl_run_status(self, option):
        self.selectDropDown(option)

    # 农排用户选择
    def inputSel_user_select(self, option):
        self.selectDropDown(option)

    # 用户类别
    def inputSel_cons_sort(self, option):
        self.selectDropDown(option)

    # 终端厂家
    def inputSel_tmnl_manufacturer(self, option):
        self.selectDropDown(option)

    # 反相采集结果
    def inputSel_recerse_collection_result(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
