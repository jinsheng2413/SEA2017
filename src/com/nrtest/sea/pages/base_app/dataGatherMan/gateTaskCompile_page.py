# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: gateTaskCompile_page.py
@time: 2019-02-15 16:03:04
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→关口采集任务编制:任务模板
class GateTaskCompileTempPage(Page):
    # 任务名称
    def inputStr_task_name(self, value):
        self.input(value)

    # 任务项
    def inputChk_task_item(self, options):
        self.clickCheckBox_new(options)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 基本应用→数据采集管理→关口采集任务编制:任务查询
class GateTaskCompileQryPage(Page):
    # 采集点名称
    def inputStr_cp_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
