# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.costControlManage.remoteCustControl.PrePaidStatus_locators import \
    PrePaidStatus_Locators


class PrePaidStatusPage(Page):
    # 控制类别
    def inputRSel_controlType_one(self, name):
        self.click(*PrePaidStatus_Locators.QRY_CONTROL_TYPE_ONE)
        locator = self.get_select_locator(PrePaidStatus_Locators.QRY_CONTROL_TYPE_VALUE_ONE, name)
        print(locator)
        self.click(*locator)

    def inputRSel_controlType_Two(self, name):
        self.click(*PrePaidStatus_Locators.QRY_CONTROL_TYPE_TWO)
        locator = self.get_select_locator(PrePaidStatus_Locators.QRY_CONTROL_TYPE_VALUE_TWO, name)
        print(locator)
        self.click(*locator)


    # 开始时间
    def inputStr_start_timeOne(self, value):
        self.input(value, *PrePaidStatus_Locators.QRY_START_TIME_ONE)

    def inputStr_start_timeTwo(self, value):
        self.input(value, *PrePaidStatus_Locators.QRY_START_TIME_TWO)

    # 结束时间
    def inputStr_end_timeOne(self, value):
        self.input(value, *PrePaidStatus_Locators.QRY_END_TIME_ONE)

    def inputStr_end_timeTwo(self, value):
        self.input(value, *PrePaidStatus_Locators.QRY_END_TIME_TWO)

    # 查询
    def btn_qryOne(self):
            self.click(*PrePaidStatus_Locators.BTN_QRY_ONE)

    def btn_qryTwo(self):
            self.click(*PrePaidStatus_Locators.BTN_QRY_TWO)