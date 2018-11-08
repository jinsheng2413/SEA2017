# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: specialUserBalanceQuery_page.py
@time: 2018/8/19 0019 9:04
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.costControlManage.specialUserBalanceQuery_locators import \
    SpecialUserBalanceQuery_locators


class SpecialUserBalanceQueryPage(Page):
    # 用户编号
    def inputStr_user_num(self, value):
        self.input(value, *SpecialUserBalanceQuery_locators.QRY_USER_NUM)

    # 用户名称
    def inputStr_User_name(self, value):
        self.input(value, *SpecialUserBalanceQuery_locators.QRY_USER_NAME)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value, *SpecialUserBalanceQuery_locators.QRY_TERMINAL_ADDR)

    #   #越限类型
    # def inputSel_more_cata(self,index):
    #     self.click(*SpecialUserBalanceQuery_locators.QRY_MORE_BOARD_CATA)
    #     locator = self.get_select_locator(SpecialUserBalanceQuery_locators.QRY_MORE_BOARD_CATA_VALUE, index)
    #     # print(locator)
    #     self.click(*locator)

    # 召测日期
    def inputStr_call_test_date(self, value):
        self.input(value, *SpecialUserBalanceQuery_locators.QRY_CALL_TEST_DATE)

    def btn_qry(self):
        self.click(*SpecialUserBalanceQuery_locators.BTN_QRY)
