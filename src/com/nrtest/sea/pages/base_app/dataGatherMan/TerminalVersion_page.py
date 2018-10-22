# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.terminalVersion_locators import TerminalVersionLocators


class TerminalVersionPage(Page):
    # 用户编号
    def inputStr_userNo(self, value):
        self.input(value, *TerminalVersionLocators.QRY_USER_NO)

    # 终端地址
    def inputStr_tmnlAddr(self, value):
        self.input(value, *TerminalVersionLocators.QRY_TMNL_ADDR)

    # 查询时间
    def inputStr_queryTime(self, value):
        self.input(value, *TerminalVersionLocators.QRY_DATE)


        # 查询
    def btn_qry(self):
            self.click(*TerminalVersionLocators.BTN_QRY)