# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: localBroadChkClock_page.py
@time: 2018/10/30 13:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→时钟管理→本地广播校时设置
class LocalBroadChkClockPage(Page):

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端类型--打开并选择
    def inputSel_tmnl_type(self, item):
        self.selectDropDown(item)

    # 终端厂家--打开并选择
    def inputSel_tmnl_factory(self, item):
        self.selectDropDown(item)

    # 终端规约--打开并选择
    def inputSel_tmnl_protocol(self, item):
        self.selectDropDown(item)

    # 设置状态--打开并选择
    def inputSel_set_status(self, item):
        self.selectDropDown(item)

    # 点击查询
    def btn_qry(self):
        self.btn_query()
