# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: TerminalOnlineMonitor_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class TerminalOnlineMonitorPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        # self.input(value, *TerminalOnlineMonitorLocators.QRY_DATE)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(TerminalOnlineMonitorLocators.BTN_QRY)
        self.btn_query()
