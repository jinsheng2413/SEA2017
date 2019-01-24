# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: automatedMeterAvailability_page.py
@time: 2018/10/19 10:54
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→自动化抄表可用率:全项采集成功率
class AutomatedMeterAvailabilityPage(Page):
    # 表计类型
    def inputSel_meter_type(self, index):
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 统计查询→综合查询→自动化抄表可用率:全项采集失败明细
class AutomatedMeterAvailabilityDetailPage(Page):
    # 表计类型
    def inputSel_meter_type(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 查询日期
    def inputDt_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
