# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.terminalPassword__locators import TerminalPasswordLocators


class TerminalPasswordPage(Page):
    # 日期
    def inputStr_date(self, value):
        self.input(value, *TerminalPasswordLocators.QRY_DATE)

        # 查询

    def btn_qry(self):
        self.click(*TerminalPasswordLocators.BTN_QRY)
