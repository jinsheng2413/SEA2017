# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class PrePaidStatusByActionPage(Page):
    # 控制类别
    def inputSel_controlType(self, name):
        # self.click(PrePaidStatus_Locators.QRY_CONTROL_TYPE_ONE)
        # locator = self.get_select_locator(
        # PrePaidStatus_Locators.QRY_CONTROL_TYPE_VALUE_ONE, name)
        # print(locator)
        # self.click(locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 开始时间
    def inputDt_start_time(self, value):
        # self.input(value, *PrePaidStatus_Locators.QRY_START_TIME_ONE)
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        # self.input(value, *PrePaidStatus_Locators.QRY_END_TIME_ONE)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(PrePaidStatus_Locators.BTN_QRY_ONE)
        self.btn_query(True)


class PrePaidStatusByUserPage(Page):
    # 控制类别
    def inputSel_controlType(self, name):
        # self.click(PrePaidStatus_Locators.QRY_CONTROL_TYPE_TWO)
        # locator = self.get_select_locator(
        # PrePaidStatus_Locators.QRY_CONTROL_TYPE_VALUE_TWO, name)
        # print(locator)
        # self.click(locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 开始时间
    def inputDt_start_time(self, value):
        # self.input(value, *PrePaidStatus_Locators.QRY_START_TIME_TWO)
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        # self.input(value, *PrePaidStatus_Locators.QRY_END_TIME_TWO)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(PrePaidStatus_Locators.BTN_QRY_TWO)
        self.btn_query(True)
