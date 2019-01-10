# -*- coding: utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: meterClockMan_pages.py
@time: 2018/11/2 0002 11:07
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理-电能表管理-电能表状态查询
class MeterClockManPage(Page):

    # 事件类型
    def inputSel_event_type(self, option):
        self.selectDropDown(option)


    # 终端厂家
    def inputSel_tmnl_factory(self, option):
        self.selectDropDown(option)

    # 电表厂家
    def inputSel_meter_factory(self, option):
        self.selectDropDown(option)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)


    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 电表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content)

    # 日期
    def inputDt_query_date_range(self, content):
        self.inputDate(content)

    # 查询
    def btn_qry(self):
        self.btn_query()
