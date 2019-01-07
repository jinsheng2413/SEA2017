# -*- coding: utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: meterClockMan_pages.py
@time: 2018/11/2 0002 11:07
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理-电能表管理-电能表状态查询
class MeterClockManPage(Page):

    # 事件类型
    def inputSel_eventtype(self, option):
        # self.click(MeterClockManLocators.QRY_EVENTTYPE)
        # locator = self.get_select_locator(
        #     MeterClockManLocators.QRY_EVENTTYPE_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)


    # 终端厂家
    def inputSel_tmnlfactory(self, option):
        # self.click(MeterClockManLocators.QRY_TMNLFACORY)
        # locator = self.get_select_locator(
        #     MeterClockManLocators.QRY_TMNLFACORY_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 电表厂家
    def inputSel_meterfactory(self, option):
        # self.click(MeterClockManLocators.QRY_METERFACTORY)
        # locator = self.get_select_locator(
        #     MeterClockManLocators.QRY_METERFACTORY_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 终端地址
    def inputStr_tmnladdr(self, content):
        # self.input(value, *MeterClockManLocators.QRY_TMNLADDR)
        self.input(content)


    # 用户编号
    def inputStr_userno(self, content):
        # self.input(value, *MeterClockManLocators.QRY_USERNO)
        self.input(content)

    # 电表资产号
    def inputStr_meterno(self, content):
        # self.input(value, *MeterClockManLocators.QRY_METERNO)
        self.input(content)

    # 日期
    def inputDt_date(self, content):
        # self.input(value, *MeterClockManLocators.QRY_DATE)
        self.inputDate(content)

    # 查询
    def btn_qry(self):
        # self.click(MeterClockManLocators.BTN_QRY)
        self.btn_query()
