# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class CtrlExecutSpecPage(Page):
    # 控制类别
    def inputSel_controlType(self, name):
        # self.click(CtrlExecutSpecLocators.QRY_CONTROL_TYPE)
        # locator = self.get_select_locator(
        # CtrlExecutSpecLocators.QRY_CONTROL_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 工单号
    def inputStr_workOrder(self, value):
        # self.input(value, *CtrlExecutSpecLocators.QRY_WORK_ORDER)
        self.input(value)

    # 结束时间
    def inputDt_endTime(self, value):
        # self.input(value, *CtrlExecutSpecLocators.QRY_END_TIME)
        self.inputDate(value)

    # 开始时间
    def inputDt_startTime(self, value):
        # self.input(value, *CtrlExecutSpecLocators.QRY_START_TIME)
        self.inputDate(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        # self.input(value, *CtrlExecutSpecLocators.QRY_TMNL_ADDR)
        self.input(value)

    # 用户名称
    def inputStr_userName(self, value):
        # self.input(value, *CtrlExecutSpecLocators.QRY_USER_NAME)
        self.input(value)

    # 用户编号
    def inputStr_userNo(self, value):
        # self.input(value, *CtrlExecutSpecLocators.QRY_USER_NO)
        self.input(value)

    # 执行状态
    def inputSel_exeStatus(self, name):
        # self.click(CtrlExecutSpecLocators.QRY_EXE_STATUS)
        # locator = self.get_select_locator(
        # CtrlExecutSpecLocators.QRY_EXE_STATUS_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 查询
    def btn_qry(self):
        # self.click(CtrlExecutSpecLocators.BTN_QRY)
        self.btn_query()
