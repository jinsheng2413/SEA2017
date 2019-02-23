# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: terminalOnlineSpied_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→终端版本召测
class TerminalOnlineSpiedPage(Page):
    # 终端厂商
    def inputStr_tmnl_factory(self, value):
        self.selectCheckBox(value)

    # 终端地址
    def inputSel_terminal_addr(self, value):
        self.input(value)

    # 终端状态
    def inputStr_tmnl_status(self, value):
        self.selectCheckBox(value)

    # 终端规约
    def inputStr_tmnl_protocol(self, value):
        self.selectCheckBox(value)

    # 终端类型
    def inputStr_tmnl_type(self, value):
        self.selectCheckBox(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
