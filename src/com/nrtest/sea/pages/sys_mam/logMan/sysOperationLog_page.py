# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysOperationLog_page.py
@time: 2018/11/29 15:04
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.logMan.sysOperationLog_locators import SysOperationLogLocators, \
    UserOperationLogLocators


# 系统管理→日志管理→系统操作日志
class SysOperationLogPage(Page):
    # 操作模块
    def inputSel_operation_tem(self, index):
        self.click(*SysOperationLogLocators.QRY_OPERATION_TEM)
        locator = self.get_select_locator(SysOperationLogLocators.QRY_OPERATION_TEM_VALUE, index)
        self.click(*locator)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *SysOperationLogLocators.QRY_TMNL_ADDR)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.exec_script(SysOperationLogLocators.START_DATE_JS)
        self.input(content, *SysOperationLogLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(SysOperationLogLocators.END_DATE_JS)
        self.input(content, *SysOperationLogLocators.QRY_END_DATE)

    # 操作人员
    def inputStr_operator(self, content):
        self.input(content, *SysOperationLogLocators.QRY_OPERATOR)

    # 查询按钮
    def btn_search(self):
        self.click(*SysOperationLogLocators.BTN_SEARCH)


# 系统管理→日志管理→系统操作日志→用户操作日志
class UserOperationLogPage(Page):
    # 操作模块
    def inputSel_operation_tem(self, index):
        self.click(*UserOperationLogLocators.QRY_OPERATION_TEM)
        locator = self.get_select_locator(UserOperationLogLocators.QRY_OPERATION_TEM_VALUE, index)
        self.click(*locator)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.exec_script(UserOperationLogLocators.START_DATE_JS)
        self.input(content, *UserOperationLogLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(UserOperationLogLocators.END_DATE_JS)
        self.input(content, *UserOperationLogLocators.QRY_END_DATE)

    # 操作人员
    def inputStr_operator(self, content):
        self.input(content, *UserOperationLogLocators.QRY_OPERATOR)

    # 查询按钮
    def btn_search(self):
        self.click(*UserOperationLogLocators.BTN_SEARCH)
