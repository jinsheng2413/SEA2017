# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlPowerCutEventQuery_page.py
@time: 2018/11/5 10:29
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→停电分析→终端停电事件查询
class TmnlPowerCutEventQueryPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index, True, True)

    # 月份
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()

    # 统计类型
    def inputChk_stat_type(self, content):
        self.clickRadioBox(content)

# 高级应用→配变监测分析→停电分析→终端停电事件查询→月终端停电明细
class TmnlPowerCutEventQueryMonthPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 月份
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 停电次数
    def inputStr_power_cut_time(self, content):
        self.input(content)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)

# 高级应用→配变监测分析→停电分析→终端停电事件查询→日终端停电明细
class TmnlPowerCutEventQueryDayPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 停复电标识
    def inputSel_power_cut_identifying(self, index):
        self.selectDropDown(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
