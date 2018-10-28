# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.allCollectSuccessRate_locators import AllCollectSuccessRateLocators


class AllCollectSuccessRatePage(Page):
    # 电能表抄读状态
    def inputStr_meterReadState(self, name):
        self.click(*AllCollectSuccessRateLocators.QRY_METER_READ_STATE)
        locator = self.get_select_locator(AllCollectSuccessRateLocators.QRY_METER_READ_STATE_VALUE, name)
        self.click(*locator)

    # 终端运行状态
    def inputStr_Tmnl_runState(self, name):
        self.click(*AllCollectSuccessRateLocators.QRY_TMNL_RUN_STATE)
        locator = self.get_select_locator(AllCollectSuccessRateLocators.QRY_TMNL_RUN_STATE_VALUE, name)
        self.click(*locator)

    # 用户编号
    def inputStr_userNo(self, value):
        self.input(value, *AllCollectSuccessRateLocators.QRY_USER_NO)

    # 用户类型
    def inputStr_userType(self, name):
        self.input(name, *AllCollectSuccessRateLocators.QRY_USERTYPE)

    # 表资产号
    def inputStr_surfaceAssetNo(self, value):
        self.input(value, *AllCollectSuccessRateLocators.QRY_SURFACE_ASSERT_NO)

        # 查询

    def btn_qry(self):
        self.click(*AllCollectSuccessRateLocators.BTN_QRY)
