# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: curVoltQuery_page.py
@time: 2019-02-13 09:08:36
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→低压固定时间点电压电流监测→低电压监测→电压电流查询
class CurVoltQueryPage(Page):
    # 接线方式
    def inputSel_wiring_type(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 用户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_met_asset_no(self, value):
        self.input(value)

    # 数据类型
    def inputChk_data_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
