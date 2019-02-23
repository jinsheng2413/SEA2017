# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: realTimeReadMeterQrygw_page.py
@time: 2019-02-20 11:06:35
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表数据查询(国网):抄表明细
class RealTimeReadMeterQrygwPage(Page):
    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 数据类型
    def inputSel_data_type(self, option):
        self.selectDropDown(option)

    # 电能表抄读状态
    def inputSel_meter_read_status(self, option):
        self.selectDropDown(option)

    # 终端运行状态
    def inputSel_tmnl_run_status(self, option):
        self.selectDropDown(option)

    # 示值类型
    def inputChk_value_type(self, option):
        self.clickRadioBox(option)

    # 采集情况
    def inputChk_read_status(self, options):
        self.clickCheckBox_new(options)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 统计查询→综合查询→抄表数据查询(国网):抄表失败统计
class RealTimeReadMeterQrygwFailStatPage(Page):
    # 示值类型
    def inputChk_value_type(self, option):
        self.clickRadioBox(option, is_multi_elements=True, is_multi_tab=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→抄表数据查询(国网):抄表失败明细
class RealTimeReadMeterQryGwFaildetailPage(Page):
    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.curr_input(value, is_multi_elements=True, is_multi_tab=True)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.curr_input(value, is_multi_elements=True, is_multi_tab=True)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options, is_multi_elements=True, is_multi_tab=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 终端生产厂家
    def inputSel_tmnl_factory(self, option):
        self.selectDropDown(option)

    # 反向采集结果
    def inputSel_data_type(self, option):
        self.selectDropDown(option)

    # 电能表抄读状态
    def inputSel_meter_read_status(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 终端运行状态
    def inputSel_tmnl_run_status(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 示值类型
    def inputChk_value_type(self, option):
        self.clickRadioBox(option, is_multi_elements=True, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
