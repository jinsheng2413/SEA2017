# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用--》费控管理--》远程费控--》低压用户远程费控执行
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
        self.inputDate(value)  # , *CtrlExecutLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_ENDTIme(self, value):
        self.inputDate(value)  #, *CtrlExecutLocators.QRY_END_TIME)

    # 控制类型
    def inputSel_controlType(self, options):
        # self.click(CtrlExecutLocators.QRY_CONTROL_TYPE)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_CONTROL_TYPE_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 执行状态
    def inputSel_exeStatus(self, options):
        # self.click(CtrlExecutLocators.QRY_EXE_STATUS)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_EXE_STATUS_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 数据来源
    def inputSel_dataCome(self, options):
        # self.click(CtrlExecutLocators.QRY_DATA_COME)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_DATA_COME_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 确认状态
    def inputSel_confirmStatus(self, options):
        # self.click(CtrlExecutLocators.QRY_CONFIRM_STATUS)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_CONFIRM_STATUS_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 执行结果状态
    def inputSel_exeResultStatus(self, options):
        # self.click(CtrlExecutLocators.QRY_EXE_STATUS_RESULT)
        # locator = self.get_select_locator(
        #     CtrlExecutLocators.QRY_EXE_STATUS_RESULT_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 查询

    def btn_qry(self):
        # self.click(CtrlExecutLocators.BTN_QRY)
        self.btn_query()
