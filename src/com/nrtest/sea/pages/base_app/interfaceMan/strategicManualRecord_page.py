# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: strategicManualRecord_page.py
@time: 2018-11-08 10:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→接口管理→关口人工补录
class StrategicManualRecordPage(Page):
    # 采集点名
    def inputStr_gatherpoint_name(self, value):
        self.input(value)

    # 电表名称
    def inputStr_meter_name(self, value):
        self.input(value)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
