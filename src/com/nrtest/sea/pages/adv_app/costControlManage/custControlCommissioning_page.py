# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: custControlCommissioning_page.py
@time: 2018/8/23 0023 10:57
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.costControlManage.custControlCommissioning_locators import \
    CustControlCommissioning_locators


class CustControlCommissioning_page(Page):
    # 营销单号
    def inputStr_mark_sigle(self, value):
        self.input(value, *CustControlCommissioning_locators.QRY_MARKETINF_SINGLE_NUM)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value, *CustControlCommissioning_locators.QRY_TERMIAL_ADDR)

    # 用户编号
    def inputStr_user_num(self, value):
        self.input(value, *CustControlCommissioning_locators.QRY_USER_NUM)

    # 用户名称
    def inputStr_user_name(self, value):
        self.input(value, *CustControlCommissioning_locators.QRY_USER_NAME)

    # 开始时间
    def inputStr_start_date(self, value):
        self.input(value, *CustControlCommissioning_locators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_date(self, value):
        self.input(value, *CustControlCommissioning_locators.QRY_END_TIME)

    # 按
    def inputRSel_buy_ele_date(self, index):
        self.click(*CustControlCommissioning_locators.SELR_ARRANGE)
        locator = self.get_select_locator(CustControlCommissioning_locators.SELR_ARRANGE_VALUE, index)
        self.click(*locator)

    # 下发状态
    def inputSel_provide_state(self, index):
        print('-------------')
        self.click(*CustControlCommissioning_locators.QRY_PROVIDE_STATE)
        locator = self.get_select_locator(CustControlCommissioning_locators.QRY_PROVIDE_STATE_VALUE, index)
        self.click(*locator)

    # 点击查询按钮
    def btn_qry(self):
        self.click(*CustControlCommissioning_locators.BTN_QRY)

    # 总加组
    def btn_all_class(self):
        self.click(*CustControlCommissioning_locators.TAB_ONE_ALL_CLASS)
