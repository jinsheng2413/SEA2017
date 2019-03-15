# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: four_meter_general_query_col_fail_page.py
@time: 2019/3/15 17:24
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→多表合一综合查询:抄表失败列表
class FourMeterGeneralQueryColFailPage(Page):
    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 用户类型
    def inputSel_cons_sort(self, options):
        self.selectCheckBox(options)

    # 反向采集结果
    def inputSel_data_type(self, option):
        self.selectDropDown(option)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
