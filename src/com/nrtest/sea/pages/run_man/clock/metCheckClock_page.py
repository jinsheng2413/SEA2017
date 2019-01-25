# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→时钟管理→电能表对时
# 电表时钟月统计
class MetClockMonthStaticPage(Page):

    # 电表类别--打开并选择
    def inputSel_tmnl_type(self, item):
        self.selectDropDown(item)

    # 电能表厂商--打开并选择
    def inputSel_module_factory(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# 电表时钟日统计
class MetClockDayStaticPage(Page):

    # 统计类型
    def inputChk_stat_mode(self, option):
        self.clickRadioBox(option)

    # 电表类别--打开并选择
    def inputSel_met_type(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 电能表厂商--打开并选择
    def inputSel_meter_factory(self, item):
        self.selectDropDown(item, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)

# 电表时钟明细
class MetClockDetailPage(Page):

    # 电能表厂商--打开并选择
    def inputSel_meter_factory(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 电表类别
    def inputSel_met_type(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 电能表资产号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 偏差范围--打开并选择
    def inputSel_offset_range(self, item):
        self.selectDropDown(item)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)

# 自动对时策略配置
class AutoCheckPolicyPage(Page):

    # 间隔周期--打开并选择
    def inputSel_interval_cycle(self, item):
        self.selectDropDown(item)

    # 周期内自动对时次数--打开并选择
    def inputSel_auto_times(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
