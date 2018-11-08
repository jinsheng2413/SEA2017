# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.interfaceMan.interfaceMonitor_locators import InterfaceMonitor_Locators


class InterfaceMonitorPage(Page):

    # 接口类型
    def inputSel_interfaceType(self, name):
        self.click(*InterfaceMonitor_Locators.QRY_INTERFACE_TYPE)
        locator = self.get_select_locator(
            InterfaceMonitor_Locators.QRY_INTERFACE_TYPE_VALUE, name)
        print(locator)
        self.click(*locator)

    # 接收时间
    def inputStr_start_time(self, value):
        self.input(value, *InterfaceMonitor_Locators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *InterfaceMonitor_Locators.QRY_END_TIME)

    # 查询
    def btn_qry(self):
        self.click(*InterfaceMonitor_Locators.BTN_QRY)
