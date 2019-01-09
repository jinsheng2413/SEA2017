# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserMoneyCheck_Page.py
@time: 2018/8/9 0009 13:55
@desc:
"""
from com.nrtest.common.base_page import Page


class BalanceCount_page(Page):
    # 数据日期查询
    def inputStr_data_date(self, value):
        print(value)
        self.clean_label(value)
        self.inputDate(value)  # , *BalanceCountLocator.QRY_DATA_DATE)

    # 查询按钮
    def btn_qry(self):
        # self.click(BalanceCountLocator.BTN_QRY)
        self.btn_query(True)




class BalanceCheck_page(Page):
    # 工单编号
    def inputStr_work_order(self, value):
        self.input(value)  #, *BalanceCheckLocator.QRY_WORK_ORDER)

    # 用户编号
    def inputStr_user_order(self, value):
        self.input(value)  #, *BalanceCheckLocator.QRY_USER_ORDER)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)  #, *BalanceCheckLocator.QRY_TERMINAL_ADDR)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)  #, *BalanceCheckLocator.QRY_METER_ADDR)

    # 抄表段号
    def inputStr_meter_reading_number(self, value):
        self.input(value)  #, *BalanceCheckLocator.QRY_METER_READING_NUMBER)

    # 用户名称
    def inputStr_user_name(self, value):
        self.input(value)  #, *BalanceCheckLocator.QRY_USER_NAME)

    # 电表局编号
    def inputStr_ele_meter_bureea_order(self, value):
        self.input(value)  #, *BalanceCheckLocator.QRY_ELE_METER_BUREEA_ORDER)

    # 接收时间
    def inputStr_receive_date(self, value):
        self.clean_label(value)
        self.inputDate(value)  #, *BalanceCheckLocator.QRY_RECEIVE_DATE)

    # (末)
    def inputDt_end_date(self, value):
        self.inputDate(value)  #, *BalanceCheckLocator.QRY_END_DATE)

    # 执行状态
    def inputRSel_execute_state(self, option):
        # self.click(BalanceCheckLocator.QRY_EXECUTE_STATE)
        # locator = self.get_select_locator(
        #     BalanceCheckLocator.QRY_EXECUTE_STATE_VALUE, num)
        # self.click(locator)
        self.clean_label(option)
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(BalanceCheckLocator.BTN_QRY)
        self.btn_query(True)
