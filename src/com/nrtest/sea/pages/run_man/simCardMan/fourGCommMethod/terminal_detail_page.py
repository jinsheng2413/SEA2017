# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: terminal_detail_page.py
@time: 2019-02-14 10:36:41
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→SIM卡管理→4G通信方式→终端接入明细:01
class TerminalDetailPage(Page):
    # 采集方式
    def inputSel_coll_mode(self, option):
        self.selectDropDown(option)

    # 终端状态
    def inputSel_tmnl_status(self, option):
        self.selectDropDown(option)

    # 线路编号
    def inputStr_line_no(self, value):
        self.input(value)

    # 运营商
    def inputSel_operator(self, option):
        self.selectDropDown(option)

    # 当前状态
    def inputSel_cur_status(self, option):
        self.selectDropDown(option)

    # 终端逻辑地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端规约
    def inputStr_tmnl_protocol(self, value):
        self.selectDropDown(value)

    # 终端厂家
    def inputSel_tmnl_factory(self, option):
        self.selectDropDown(option)

    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option)

    # 终端类型
    def inputSel_tmnl_type(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
