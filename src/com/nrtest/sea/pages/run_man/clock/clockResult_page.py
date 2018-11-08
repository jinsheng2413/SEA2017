# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/11/1 13:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.clock.clockResult_locators import ClockResultDetailLocators
from com.nrtest.sea.locators.run_man.clock.clockResult_locators import ClockResultStaticLocators


# 运行管理→时钟管理→对时结果分析
# 对时结果分析
class ClockResultStaticPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 终端厂商--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*ClockResultStaticLocators.TMNL_FAC_SEL)
        locator = self.get_select_locator(
            ClockResultStaticLocators.TMNL_FAC, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *ClockResultStaticLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*ClockResultStaticLocators.BTN_QUERY)


# 对时结果明细
class ClockResultDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 类别--打开并选择
    def inputRSel_clock_model(self, name):
        self.click(*ClockResultDetailLocators.CLOCK_MODEL_SEL)
        locator = self.get_select_locator(
            ClockResultDetailLocators.CLOCK_MODEL, name)
        self.click(*locator)

    # 电表资产号
    def inputStr_met_asset_no(self, value):
        self.input(value, *ClockResultDetailLocators.MET_ASSET_NO)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value, *ClockResultDetailLocators.TMNL_ASSET_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *ClockResultDetailLocators.TMNL_ADDR)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *ClockResultDetailLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*ClockResultDetailLocators.BTN_QUERY)
