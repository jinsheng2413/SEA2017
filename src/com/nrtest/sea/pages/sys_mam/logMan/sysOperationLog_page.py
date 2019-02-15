# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysOperationLog_page.py
@time: 2018/11/29 15:04
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→日志管理→系统操作日志
# 终端操作日志
class SysOperationLogPage(Page):
    # 操作模块
    def inputSel_operation_module(self, options):
        self.selectDropDown(options)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 操作人员
    def inputStr_operator(self, content):
        self.input(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)


# 用户操作日志
class UserOperationLogPage(Page):
    # 操作模块
    def inputSel_operation_module(self, options):
        self.selectDropDown(options,is_multi_tab=True,is_multi_elements=True)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 操作人员
    def inputStr_operator(self, content):
        self.input(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)
