# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: tTmnlCheckClock_page.py
@time: 2018/11/2 16:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.clock.remoteBroadChkClock_locators import RemoteBroadChkClockLocators


# 运行管理→时钟管理→远程广播校时设置
class RemoteBroadChkClockPage(Page):

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *RemoteBroadChkClockLocators.TMNL_ADDR)

    # 终端类型--打开并选择
    def inputRSel_tmnl_type(self, name):
        self.click(*RemoteBroadChkClockLocators.TMNL_TYPE_SEL)
        locator = self.get_select_locator(
            RemoteBroadChkClockLocators.TMNL_TYPE, name)
        self.click(*locator)

    # 终端厂家--打开并选择
    def inputRSel_tmnl_fac(self, name):
        self.click(*RemoteBroadChkClockLocators.TMNL_FAC_SEL)
        locator = self.get_select_locator(
            RemoteBroadChkClockLocators.TMNL_FAC, name)
        self.click(*locator)

    # 终端规约--打开并选择
    def inputRSel_tmnl_protocol(self, name):
        self.click(*RemoteBroadChkClockLocators.TMNL_PROTOCOL_SEL)
        locator = self.get_select_locator(
            RemoteBroadChkClockLocators.TMNL_PROTOCOL, name)
        self.click(*locator)

    # 设置状态--打开并选择
    def inputRSel_set_status(self, name):
        self.click(*RemoteBroadChkClockLocators.SET_STATUS_SEL)
        locator = self.get_select_locator(
            RemoteBroadChkClockLocators.SET_STATUS, name)
        self.click(*locator)

    # 点击查询
    def btn_query(self):
        self.click(*RemoteBroadChkClockLocators.BTN_QUERY)
