# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.costControlManage.lowUserBuyEleParaGiveOut_locators import \
    LowUserBuyEleParaGiveOutLocators


class LowUserBuyEleParaGiveOut_page(Page):
    # 工单编号
    def inputStr_work_num(self, value):
        self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_EMPLOYEE_NUM)

    # 用户编号
    def inputStr_user_num(self, value):
        self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_USER_NUM)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_TERMINAL_ADDR)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_METER_ADDR)

    # 抄表段号
    def inputStr_meter_reading_num(self, value):
        self.input(
            value, *LowUserBuyEleParaGiveOutLocators.QRY_METER_READING_NUMBER)

    # 执行状态
    def inputSel_execute_state(self, index):
        self.click(*LowUserBuyEleParaGiveOutLocators.QRY_EXECUTE_STATE)
        locator = self.get_select_locator(
            LowUserBuyEleParaGiveOutLocators.QRY_EXECUTE_STATE_VALUE, index)
        # print(locator)
        self.click(*locator)

    # 接收时间
    def inputStr_receive_time(self, value):
        self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_RECEIVE_DATE)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_END_TIME)

    # 查询
    def btn_qry(self):
        self.click(*LowUserBuyEleParaGiveOutLocators.BTN_QRY)
