# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.clock.tTmnlCheckClock_locators import AutoCheckPolicyLocators
from com.nrtest.sea.locators.run_man.clock.tTmnlCheckClock_locators import TmnlClockDetailLocators
from com.nrtest.sea.locators.run_man.clock.tTmnlCheckClock_locators import TmnlClockStaticLocators


# 运行管理→时钟管理→终端对时
# 终端对时统计
class TmnlClockStaticPage(Page):



    # 终端类型--打开并选择
    def inputRSel_tmnl_type(self, name):
        self.click(*TmnlClockStaticLocators.TMNL_TYPE_SEL)
        locator = self.get_select_locator(
            TmnlClockStaticLocators.TMNL_TYPE, name)
        self.click(*locator)

    # 终端厂商--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*TmnlClockStaticLocators.TMNL_FAC_SEL)
        locator = self.get_select_locator(
            TmnlClockStaticLocators.TMNL_FAC, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *TmnlClockStaticLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*TmnlClockStaticLocators.BTN_QUERY)


# 终端时钟明细
class TmnlClockDetailPage(Page):


    # 偏差范围--打开并选择
    def inputRSel_offset_range(self, name):
        self.click(*TmnlClockDetailLocators.OFFSET_RANGE_SEL)
        locator = self.get_select_locator(
            TmnlClockDetailLocators.OFFSET_RANGE, name)
        self.click(*locator)

    # 终端类型--打开并选择
    def inputRSel_tmnl_type(self, name):
        self.click(*TmnlClockDetailLocators.TMNL_TYPE_SEL)
        locator = self.get_select_locator(
            TmnlClockDetailLocators.TMNL_TYPE, name)
        self.click(*locator)

    # 终端型号
    def inputStr_tmnl_model(self, value):
        self.input(value, *TmnlClockDetailLocators.TMNL_MODEL)

    # 终端厂商--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*TmnlClockDetailLocators.TMNL_FAC_SEL)
        locator = self.get_select_locator(
            TmnlClockDetailLocators.TMNL_FAC, name)
        self.click(*locator)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *TmnlClockDetailLocators.TMNL_ADDR)

    # 是否在线--打开并选择
    def inputRSel_is_online(self, name):
        self.click(*TmnlClockDetailLocators.IS_ONLINE_SEL)
        locator = self.get_select_locator(
            TmnlClockDetailLocators.IS_ONLINE, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *TmnlClockDetailLocators.QUERY_DATE)

    # 对时结果-打开并选择
    def inputRSel_call_status(self, name):
        self.click(*TmnlClockDetailLocators.CALL_STATUS_SEL)
        locator = self.get_select_locator(
            TmnlClockDetailLocators.CALL_STATUS, name)
        self.click(*locator)

    # 点击查询
    def btn_query(self):
        self.click(*TmnlClockDetailLocators.BTN_QUERY)

# 自动对时策略配置


class AutoCheckPolicyPage(Page):


    # 间隔周期--打开并选择
    def inputRSel_interval_cycle(self, name):
        self.click(*AutoCheckPolicyLocators.INTERVAL_CYCLE_SEL)
        locator = self.get_select_locator(
            AutoCheckPolicyLocators.INTERVAL_CYCLE, name)
        self.click(*locator)

    # 周期内自动对时次数--打开并选择
    def inputRSel_auto_times(self, name):
        self.click(*AutoCheckPolicyLocators.AUTO_TIMES_SEL)
        locator = self.get_select_locator(
            AutoCheckPolicyLocators.AUTO_TIMES, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *AutoCheckPolicyLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*AutoCheckPolicyLocators.BTN_QUERY)
