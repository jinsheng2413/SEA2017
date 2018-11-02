# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: meterClockMan_pages.py
@time: 2018/11/2 0002 11:07
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.meterMan.meterClockMan_locators import MeterClockManLocators


# 运行管理-电能表管理-电能表状态查询
class MeterClockManPage(Page):

    # 事件类型
    def inputSel_eventtype(self, index):
        self.click(*MeterClockManLocators.QRY_EVENTTYPE)
        locator = self.get_select_locator(MeterClockManLocators.QRY_EVENTTYPE_VALUE, index)
        self.click(*locator)

    # 终端厂家
    def inputSel_tmnlfactory(self, index):
        self.click(*MeterClockManLocators.QRY_TMNLFACORY)
        locator = self.get_select_locator(MeterClockManLocators.QRY_TMNLFACORY_VALUE, index)
        self.click(*locator)

    # 电表厂家
    def inputSel_meterfactory(self, index):
        self.click(*MeterClockManLocators.QRY_METERFACTORY)
        locator = self.get_select_locator(MeterClockManLocators.QRY_METERFACTORY_VALUE, index)
        self.click(*locator)

    # 终端地址
    def inputStr_tmnladdr(self, value):
        self.input(value, *MeterClockManLocators.QRY_TMNLADDR)

    # 用户编号
    def inputStr_userno(self, value):
        self.input(value, *MeterClockManLocators.QRY_USERNO)

    # 电表资产号
    def inputStr_meterno(self, value):
        self.input(value, *MeterClockManLocators.QRY_METERNO)

    # 日期
    def inputStr_date(self, value):
        self.input(value, *MeterClockManLocators.QRY_DATE)

    # 查询
    def btn_qry(self):
        self.click(*MeterClockManLocators.BTN_QRY)
