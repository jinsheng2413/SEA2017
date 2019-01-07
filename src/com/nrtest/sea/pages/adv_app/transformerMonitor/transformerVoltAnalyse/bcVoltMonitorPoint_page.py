# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page

# 高级应用--》配变监测分析--》电压质量分析--》B/C类电压监测点
# B/C类电压监测点查询
class BcVoltMonitorPointQueryPage(Page):

    # 监测点类型--打开并选择
    def inputSel_monitor_point_type(self, item):
        self.selectDropDown(item)

    # 监测点名称
    def inputStr_monitor_point_name(self, value):
        self.input(value)

    # 查询日期
    def inputStr_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# B/C类电压监测点数据
class BcVoltMonitorPointDataPage(Page):

    # 监测点类型--打开并选择
    def inputSel_monitor_point_type(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 监测点名称
    def inputStr_monitor_point_name(self, value):
        self.curr_input(value,is_multi_tab=True,is_multi_elements=True)

    # 查询日期
    def inputStr_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
