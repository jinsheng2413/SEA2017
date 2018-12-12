# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class CtrlExecutPage(Page):
    # 用户编号
    def inputStr_userNo(self, value):
        self.input(value)  # , *CtrlExecutLocators.QRY_USER_NO)

    # 用户名称
    def inputStr_userName(self, value):
        self.input(value)  #, *CtrlExecutLocators.QRY_USER_NAME)

    # 终端地址
    def inputStr_tmnlAddr(self, value):
        self.input(value)  #, *CtrlExecutLocators.QRY_TMNL_ADDR)

    # 抄表段号
    def inputStr_sectNo(self, value):
        self.input(value)  #, *CtrlExecutLocators.QRY_SECT_NO)

    # 工单号
    def inputStr_workOrder(self, value):
        self.input(value)  #, *CtrlExecutLocators.QRY_WORRK_ORDER)

    # 开始时间
    def inputStr_startTime(self, value):
        self.input(value)  #, *CtrlExecutLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_ENDTIme(self, value):
        self.input(value)  #, *CtrlExecutLocators.QRY_END_TIME)

    # 控制类型
    def inputSel_controlType(self, name):
        # self.click(*CtrlExecutLocators.QRY_CONTROL_TYPE)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_CONTROL_TYPE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 执行状态
    def inputSel_exeStatus(self, name):
        # self.click(*CtrlExecutLocators.QRY_EXE_STATUS)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_EXE_STATUS_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 数据来源
    def inputSel_dataCome(self, name):
        # self.click(*CtrlExecutLocators.QRY_DATA_COME)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_DATA_COME_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 确认状态
    def inputSel_confirmStatus(self, name):
        # self.click(*CtrlExecutLocators.QRY_CONFIRM_STATUS)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_CONFIRM_STATUS_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 执行结果状态
    def inputSel_exeResultStatus(self, name):
        # self.click(*CtrlExecutLocators.QRY_EXE_STATUS_RESULT)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_EXE_STATUS_RESULT_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name)

    # 查询

    def btn_qry(self):
        # self.click(*CtrlExecutLocators.BTN_QRY)
        self.btn_query()
