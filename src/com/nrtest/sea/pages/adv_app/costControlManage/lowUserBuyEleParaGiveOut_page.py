# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""
from com.nrtest.common.base_page import Page


class LowUserBuyEleParaGiveOut_page(Page):
    # 工单编号
    def inputStr_app_no(self, value):
        self.input(value)  # , *LowUserBuyEleParaGiveOutLocators.QRY_EMPLOYEE_NUM)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *LowUserBuyEleParaGiveOutLocators.QRY_USER_NUM)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)  # , *LowUserBuyEleParaGiveOutLocators.QRY_TERMINAL_ADDR)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)  # , *LowUserBuyEleParaGiveOutLocators.QRY_METER_ADDR)

    # 抄表段号
    def inputStr_sect_no(self, value):
        self.input(value)  # , *LowUserBuyEleParaGiveOutLocators.QRY_METER_READING_NUMBER)

    # 执行状态
    def inputSel_execute_status(self, option):
        # self.click(LowUserBuyEleParaGiveOutLocators.QRY_EXECUTE_STATE)
        # locator = self.get_select_locator(
        #     LowUserBuyEleParaGiveOutLocators.QRY_EXECUTE_STATE_VALUE, option)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(option)

    # 接收时间
    def inputDt_start_time(self, value):
        # self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_RECEIVE_DATE)
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        # self.input(value, *LowUserBuyEleParaGiveOutLocators.QRY_END_TIME)
        self.inputDate(value)
    # 查询
    def btn_qry(self):
        # self.click(LowUserBuyEleParaGiveOutLocators.BTN_QRY)
        self.btn_query()
