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
class MeterDataQueryPage(Page):
    # 数据类型
    def inputChk_data_type(self, options):
        self.clickRadioBox(options)

    # 抄表段号
    def inputStr_mr_sect_no(self, content):
        self.input(content)  # , *MeterDataQueryLocators.MR_SECT_NO)

    # 电表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content)  #, *MeterDataQueryLocators.METER_ASSET_NO)

    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(MeterDataQueryLocators.CONS_TYPE)
        # locator = self.get_select_locator(
        #     MeterDataQueryLocators.CONS_TYPE_VALUE, index)
        # self.click(locator)
        self.selectCheckBox(index)

    # 相位
    def inputSel_phase_code(self, index):
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(MeterDataQueryLocators.DATE_JS)
        # self.input(content, *MeterDataQueryLocators.DATE)
        self.inputDate(content)

    # 数据类别
    def inputSel_data_type(self, index):
        self.selectDropDown(index)

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
        # self.click(MeterDataQueryLocators.BTN_SEARCH)
        self.btn_query(True)


# 统计查询→综合查询→抄表数据查询:抄表失败统计
class MeterDataQueryCountPage(Page):
    # 日冻结曲线类型
    def inputChk_day_freeze_curve_type(self, option):
        self.clickRadioBox(option)

    # 日冻结示值
    def inputChk_day_reeze_show_value(self, option):
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

    # 日冻结示值
    def inputChk_day_reeze_show_value(self, option):
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
