# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: custControlCommissioning_page.py
@time: 2018/8/23 0023 10:57
@desc:
"""
from com.nrtest.common.base_page import Page


class CustControlCommissioning_page(Page):
    # 营销单号
    def inputStr_app_no(self, value):
        # self.input(value, *CustControlCommissioning_locators.QRY_MARKETINF_SINGLE_NUM)
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)  # , *CustControlCommissioning_locators.QRY_TERMIAL_ADDR)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *CustControlCommissioning_locators.QRY_USER_NUM)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)  # , *CustControlCommissioning_locators.QRY_USER_NAME)

    # 开始时间
    def inputDt_start_date(self, value):
        # self.input(value, *CustControlCommissioning_locators.QRY_START_TIME)
        self.inputDate(value)
    # 结束时间
    def inputDt_end_date(self, value):
        # self.input(value, *CustControlCommissioning_locators.QRY_END_TIME)
        self.inputDate(value)

    # 按
    def inputSel_debug_dt(self, option):
        # self.click(CustControlCommissioning_locators.SELR_ARRANGE)
        # locator = self.get_select_locator(
        #     CustControlCommissioning_locators.SELR_ARRANGE_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 下发状态
    def inputSel_send_status(self, option):
        # print('-------------')
        # self.click(CustControlCommissioning_locators.QRY_PROVIDE_STATE)
        # locator = self.get_select_locator(
        #     CustControlCommissioning_locators.QRY_PROVIDE_STATE_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 点击查询按钮
    def btn_qry(self):
        # self.click(CustControlCommissioning_locators.BTN_QRY)
        self.btn_query()

    # 总加组
    def btn_all_class(self):
        # self.click(CustControlCommissioning_locators.TAB_ONE_ALL_CLASS)
        self.btn_query()
