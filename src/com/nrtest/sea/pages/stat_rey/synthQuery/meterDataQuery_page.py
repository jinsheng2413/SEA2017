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
        self.clickRadioBox(option, is_multi_elements=True, is_multi_tab=True)

    # 抄表段号
    def inputStr_mr_sect_no(self, content):
        self.curr_input(content, is_multi_tab=True, is_multi_elements=True)

    # 电表资产号
    def inputStr_meter_asset_no(self, content):
        self.curr_input(content, is_multi_elements=True, is_multi_tab=True)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index, is_multi_tab=True, is_multi_elements=True)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 数据类别
    def inputSel_data_sort(self, option):
        self.selectDropDown(option)

    # 农排用户选择
    def inputSel_user_select(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 计量点状态
    def inputSel_sto_point_status(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 采集情况
    def inputChk_read_status(self, index):
        self.clickCheckBox_new(index, is_multi_tab=True)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→抄表数据查询:抄表失败统计
class MeterDataQueryCountPage(Page):
    # 日冻结曲线类型
    def inputChk_day_freeze_curve_type(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 相位
    def inputSel_phase_code(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→抄表数据查询:抄表失败明细
class MeterDataQueryFailDetailPage(Page):
    # 规约类型
    def inputChk_protocol_type(self, value):
        self.selectCheckBox(value)

    # 日冻结曲线类型
    def inputChk_day_freeze_curve_type(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.curr_input(value, is_multi_elements=True, is_multi_tab=True)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.curr_input(value, is_multi_elements=True, is_multi_tab=True)

    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectCheckBox(option, is_multi_tab=True, is_multi_elements=True)

    # 相位
    def inputSel_phase_code(self, option, line=0):
        if line == 1 or line == 2:
            return 0
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 农排用户选择
    def inputSel_user_select(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 用户类别
    def inputSel_cons_sort(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnl_manufacturer(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 反相采集结果
    def inputSel_recerse_collection_result(self, option, line=0):
        if line == 2 or line == 3:
            return 0
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 计量点状态
    def inputSel_sto_point_status(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 日冻结需量和示值曲线
    def inputChk_day_freezing_demand_value_curve(self, value):
        self.clickRadioBox(value, is_multi_elements=True, is_multi_tab=True)

    # 日冻结电能示值
    def inputChk_day_freezing_ele_value(self, value):
        self.clickRadioBox(value, is_multi_elements=True, is_multi_tab=True)

    # 正反是否有功
    def inputChk_power_type(self, value, line=0):
        if line == 2 or line == 3:
            return 0
        self.clickRadioBox(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
