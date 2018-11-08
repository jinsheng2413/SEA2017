# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.clock.localBroadChkClock_locators import LocalBroadChkClockLocators


# 运行管理→时钟管理→本地广播校时设置
class LocalBroadChkClockPage(Page):
    # 节点名称
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *LocalBroadChkClockLocators.TMNL_ADDR)

    # 终端类型--打开并选择
    def inputRSel_tmnl_type(self, name):
        self.click(*LocalBroadChkClockLocators.TMNL_TYPE_SEL)
        locator = self.get_select_locator(
            LocalBroadChkClockLocators.TMNL_TYPE, name)
        self.click(*locator)

    # 终端厂家--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*LocalBroadChkClockLocators.TMNL_FAC_SEL)
        locator = self.get_select_locator(
            LocalBroadChkClockLocators.TMNL_FAC, name)
        self.click(*locator)

    # 终端规约--打开并选择
    def inputRSel_tmnl_protocol(self, name):
        self.click(*LocalBroadChkClockLocators.TMNL_PROTOCOL_SEL)
        locator = self.get_select_locator(
            LocalBroadChkClockLocators.TMNL_PROTOCOL, name)
        self.click(*locator)

    # 设置状态--打开并选择
    def inputRSel_set_status(self, name):
        self.click(*LocalBroadChkClockLocators.SET_STATUS_SEL)
        locator = self.get_select_locator(
            LocalBroadChkClockLocators.SET_STATUS, name)
        self.click(*locator)

    # 点击查询
    def btn_query(self):
        self.click(*LocalBroadChkClockLocators.BTN_QUERY)
