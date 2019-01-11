# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class TerminalOnlineSpiedPage(Page):
    # 终端厂商
    def inputStr_TmnlManufactory(self, value):
        self.selectCheckBox(value)  # , *TerminalOnlineSpiedLocators.QRY_TMNL_MANUFACTURER)

    # 终端地址
    def inputSel_TmnlAddr(self, value):
        self.input(value)  # , *TerminalOnlineSpiedLocators.QRY_TMNL_ADDR)

    # 终端状态
    def inputStr_TmnlState(self, value):
        self.selectCheckBox(value)  # , *TerminalOnlineSpiedLocators.QRY_TMNL_STATE)

    # 终端规约
    def inputStr_TmnlProtocol(self, value):
        self.selectCheckBox(value)  # , *TerminalOnlineSpiedLocators.QRY_TMNL_PROTOCOL)

    # 终端类型
    def inputStr_TmnlType(self, value):
        self.selectCheckBox(value)  # , *TerminalOnlineSpiedLocators.QRY_TMNL_TYPE)

    # 查询
    def btn_qry(self):
        # self.click(TerminalOnlineSpiedLocators.BTN_QRY)
        self.btn_query()
