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
        # self.click(*MetClockMonthStaticLocators.MET_TYPE_SEL)
        # locator = self.get_select_locator(
        #     MetClockMonthStaticLocators.MET_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 电能表厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        # self.click(*MetClockMonthStaticLocators.MET_FAC_SEL)
        # locator = self.get_select_locator(
        #     MetClockMonthStaticLocators.MET_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *MetClockMonthStaticLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*MetClockMonthStaticLocators.BTN_QUERY)
        self.btn_query()


# 电表时钟日统计
class MetClockDayStaticPage(Page):

    # 电表类别--打开并选择
    def inputSel_tmnl_type(self, item):
        # self.click(*MetClockDayStaticLocators.MET_TYPE_SEL)
        # locator = self.get_select_locator(
        #     MetClockDayStaticLocators.MET_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 电能表厂商--打开并选择
    def inputSel_tmnl_fac(self, item):
        # self.click(*MetClockDayStaticLocators.MET_FAC_SEL)
        # locator = self.get_select_locator(
        #     MetClockDayStaticLocators.MET_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)


    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *MetClockDayStaticLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*MetClockDayStaticLocators.BTN_QUERY)
        self.btn_query()

# 电表时钟明细
class MetClockDetailPage(Page):

    # 电能表厂商--打开并选择
    def inputSel_met_fac(self, item):
        # self.click(*MetClockDetailLocators.MET_FAC_SEL)
        # locator = self.get_select_locator(MetClockDetailLocators.MET_FAC, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 电表类别
    def inputRSel_met_type(self, item):
        # self.click(*MetClockDetailLocators.MET_TYPE_SEL)
        # locator = self.get_select_locator(
        #     MetClockDetailLocators.MET_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 电能表资产号
    def inputStr_met_asset_no(self, value):
        # self.input(value, *MetClockDetailLocators.MET_ASSET_NO)
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        # self.input(value, *MetClockDetailLocators.CONS_NO)
        self.input(value)

    # 偏差范围--打开并选择
    def inputSel_offset_range(self, item):
        # self.click(*MetClockDetailLocators.OFFSET_RANGE_SEL)
        # locator = self.get_select_locator(
        #     MetClockDetailLocators.OFFSET_RANGE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        # self.input(value, *MetClockDetailLocators.TMNL_ADDR)
        self.input(value)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *MetClockDetailLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*MetClockDetailLocators.BTN_QUERY)
        self.btn_query()


# 自动对时策略配置
class AutoCheckPolicyPage(Page):

    # 间隔周期--打开并选择
    def inputSel_interval_cycle(self, item):
        # self.click(*AutoCheckPolicyLocators.INTERVAL_CYCLE_SEL)
        # locator = self.get_select_locator(
        #     AutoCheckPolicyLocators.INTERVAL_CYCLE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 周期内自动对时次数--打开并选择
    def inputSel_auto_times(self, item):
        # self.click(*AutoCheckPolicyLocators.AUTO_TIMES_SEL)
        # locator = self.get_select_locator(
        #     AutoCheckPolicyLocators.AUTO_TIMES, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *AutoCheckPolicyLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*AutoCheckPolicyLocators.BTN_QUERY)
        self.btn_query()
