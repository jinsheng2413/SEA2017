# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: readCompleteRateCT_page.py
@time: 2019-02-15 09:34:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→巡检仪采集完整率:采集完整率
class ReadCompleteRateCtPage(Page):
    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→数据采集管理→巡检仪采集完整率:采集完整率明细
class ReadCompleteRateCtDetailPage(Page):
    # 日期时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
