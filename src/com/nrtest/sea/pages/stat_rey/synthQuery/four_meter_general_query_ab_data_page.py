# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: four_meter_general_query_ab_data_page.py
@time: 2019/3/15 17:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→多表合一综合查询:异常数据明细
class FourMeterGeneralQueryAbDataPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 异常类型
    def inputSel_abnormal_type(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
