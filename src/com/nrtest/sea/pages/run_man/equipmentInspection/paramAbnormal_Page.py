# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: param_abnormal_page.py
@time: 2019-02-15 13:18:09
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→设备巡检→参数档案异常反校:反校汇总信息
class ParamAbnormal_collect_Page(Page):
    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 设备类型
    def inputSel_device_type(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 异常类型
    def inputSel_except_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 运行管理→设备巡检→参数档案异常反校:反校明细信息
class ParamAbnormal_detail_Page(Page):
    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 设备类型
    def inputSel_device_type(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 异常类型
    def inputSel_except_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 终端资产编号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
