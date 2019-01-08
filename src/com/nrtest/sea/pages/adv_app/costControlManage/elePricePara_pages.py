# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: elePricePara_pages.py
@time: 2018/8/15 0015 14:36
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用--》费控管理--》本地费控--》电价参数下发
class ElePricePages(Page):
    # 工单编号
    def inputStr_work_No(self, value):
        self.input(value)  #, *ElePricePara_locators.QRY_EMPLOYEE_NUM)

    # 用户编号
    def inputStr_user_No(self, value):
        self.input(value)  #, *ElePricePara_locators.QRY_USER_NUM)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)  #, *ElePricePara_locators.QRY_TERMINAL_ADDR)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)  #, *ElePricePara_locators.QRY_METER_ADDR)

    # 抄表段号
    def inputStr_meter_reading_num(self, value):
        self.input(value)  #, *ElePricePara_locators.QRY_METER_READING_NUMBER)

    # 任务类型
    def inputSel_task_cata(self, index):
        # self.click(ElePricePara_locators.QRY_TASK_CATA)
        # locator = self.get_select_locator(
        #     ElePricePara_locators.QRY_TASK_CATA_VALUE, index)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(index)

    # 执行状态
    def inputSel_execute_state(self, index):
        # self.click(ElePricePara_locators.QRY_EXECUTE_STATE)
        # locator = self.get_select_locator(
        #     ElePricePara_locators.QRY_EXECUTE_STATE_VALUE, index)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(index)


    # 接收时间
    def inputStr_receive_time(self, value):
        self.input(value)  #, *ElePricePara_locators.QRY_RECEIVE_DATE)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value)  #, *ElePricePara_locators.QRY_END_TIME)

    # 查询
    def btn_qry(self):
        # self.click(ElePricePara_locators.BTN_QRY)
        self.btn_query()
