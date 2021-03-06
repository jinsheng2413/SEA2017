# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: InterfaceMonitor_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→接口管理→接口管理
class InterfaceMonitorPage(Page):

    # 接口类型
    def inputSel_interface_type(self, name):
        self.clean_label(name)
        self.selectDropDown(name)

    # 接收时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)
    # 查询
    def btn_qry(self):
        self.btn_query()
