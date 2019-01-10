# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.meterStateArrLocators import MeterStateArrLocators


class MeterStateArrPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *MeterStateArrLocators.QRY_TMNLADDR)

    # 终端状态
    def inputSel_tmnlStatus(self, name):
        self.click(MeterStateArrLocators.QRY_TMNL_STATUS)
        locator = self.get_select_locator(
            MeterStateArrLocators.QRY_TMNL_STATUS_VALUE, name)
        self.click(locator)

    # 终端类型
    def inputSel_tmnlType(self, name):
        self.click(MeterStateArrLocators.QRY_TMNLTYPE)
        locator = self.get_select_locator(
            MeterStateArrLocators.QRY_TMNLTYPE_VALUE, name)
        self.click(locator)

    # # 筛选条件
    # def inputSel_screenCondition(self, name):
    #     self.click(MeterStateArrLocators.QRY_SCREEN_CONDITION)
    #     locator = self.get_select_locator(MeterStateArrLocators.QRY_SCREEN_CONDITION_VALUE, name)
    #     self.click(locator)

    # #筛选条件输入框
    # def inputStr_screenConditionInput(self,value):
    #     self.input(value, *MeterStateArrLocators.QRY_SCREEN_CONDITION_INPUT)

    # # 电能表状态
    # def inputSel_meterStatus(self, name):
    #     self.click(MeterStateArrLocators.QRY_METER_STATUS)
    #     locator = self.get_select_locator(MeterStateArrLocators.QRY_METER_STATUS_VALUE, name)
    #     self.click(locator)

    # 查询
    def btn_tmnl_qry(self):
        self.click(MeterStateArrLocators.BTN_TMNL_QRY)

        # 查询

    def btn_meter_qry(self):
        self.click(MeterStateArrLocators.BTN_METER_QRY)
