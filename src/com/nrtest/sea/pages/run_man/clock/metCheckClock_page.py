# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.clock.metCheckClock_locators import AutoCheckPolicyLocators
from com.nrtest.sea.locators.run_man.clock.metCheckClock_locators import MetClockDayStaticLocators
from com.nrtest.sea.locators.run_man.clock.metCheckClock_locators import MetClockDetailLocators
from com.nrtest.sea.locators.run_man.clock.metCheckClock_locators import MetClockMonthStaticLocators


# 运行管理→时钟管理→电能表对时
# 电表时钟月统计
class MetClockMonthStaticPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 电表类别--打开并选择
    def inputRSel_tmnl_type(self, name):
        self.click(*MetClockMonthStaticLocators.MET_TYPE_SEL)
        locator = self.get_select_locator(MetClockMonthStaticLocators.MET_TYPE, name)
        self.click(*locator)

    # 电能表厂商--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*MetClockMonthStaticLocators.MET_FAC_SEL)
        locator = self.get_select_locator(MetClockMonthStaticLocators.MET_FAC, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *MetClockMonthStaticLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*MetClockMonthStaticLocators.BTN_QUERY)


# 电表时钟日统计
class MetClockDayStaticPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 电表类别--打开并选择
    def inputRSel_tmnl_type(self, name):
        self.click(*MetClockDayStaticLocators.MET_TYPE_SEL)
        locator = self.get_select_locator(MetClockDayStaticLocators.MET_TYPE, name)
        self.click(*locator)

    # 电能表厂商--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*MetClockDayStaticLocators.MET_FAC_SEL)
        locator = self.get_select_locator(MetClockDayStaticLocators.MET_FAC, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *MetClockDayStaticLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*MetClockDayStaticLocators.BTN_QUERY)


# 电表时钟明细
class MetClockDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 电能表厂商--打开并选择
    def inputRSel_met_fac(self, name):
        self.click(*MetClockDetailLocators.MET_FAC_SEL)
        locator = self.get_select_locator(MetClockDetailLocators.MET_FAC, name)
        self.click(*locator)

    # 电表类别
    def inputRSel_met_type(self, name):
        self.click(*MetClockDetailLocators.MET_TYPE_SEL)
        locator = self.get_select_locator(MetClockDetailLocators.MET_TYPE, name)
        self.click(*locator)

    # 电能表资产号
    def inputStr_met_asset_no(self, value):
        self.input(value, *MetClockDetailLocators.MET_ASSET_NO)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value, *MetClockDetailLocators.CONS_NO)

    # 偏差范围--打开并选择
    def inputRSel_offset_range(self, name):
        self.click(*MetClockDetailLocators.OFFSET_RANGE_SEL)
        locator = self.get_select_locator(MetClockDetailLocators.OFFSET_RANGE, name)
        self.click(*locator)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *MetClockDetailLocators.TMNL_ADDR)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *MetClockDetailLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*MetClockDetailLocators.BTN_QUERY)


# 自动对时策略配置
class AutoCheckPolicyPage(Page):
    # 节点
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 间隔周期--打开并选择
    def inputRSel_interval_cycle(self, name):
        self.click(*AutoCheckPolicyLocators.INTERVAL_CYCLE_SEL)
        locator = self.get_select_locator(AutoCheckPolicyLocators.INTERVAL_CYCLE, name)
        self.click(*locator)

    # 周期内自动对时次数--打开并选择
    def inputRSel_auto_times(self, name):
        self.click(*AutoCheckPolicyLocators.AUTO_TIMES_SEL)
        locator = self.get_select_locator(AutoCheckPolicyLocators.AUTO_TIMES, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *AutoCheckPolicyLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*AutoCheckPolicyLocators.BTN_QUERY)
