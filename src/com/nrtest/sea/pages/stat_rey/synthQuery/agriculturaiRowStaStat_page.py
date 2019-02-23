# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: agriculturaiRowStaStat_page.py
@time: 2019-02-13 16:08:50
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→农排用户统计:农排用户信息接入统计
class AgriculturaiRowStaPage(Page):
    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 统计查询→综合查询→农排用户统计:农排用户接入明细
class AgriculturaiRowStaDetailPage(Page):
    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 电表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端状态
    def inputSel_tmnl_status(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
