# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: dataRepair_page.py
@time: 2018-10-31 15:11
@desc:
"""

from com.nrtest.common.base_page import Page


class DataRepair_1Page(Page):
    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectDropDown(options)
    # 数据类型
    def inputSel_data_type(self, options):
        self.selectDropDown(options)
    # 开始时间

    def inputDt_start_date(self, value):
        self.input(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 第二个tab页
class DataRepair_2Page(Page):
    # 数据类型
    def inputSel_data_type(self, options):
        self.selectDropDown(options,is_multi_tab=True,is_multi_elements=True)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectDropDown(options,is_multi_tab=True,is_multi_elements=True)

    # 查询日期

    def inputDt_query_date(self, value):
        self.curr_input(value, True, True)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 电表局编号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)