# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysEnterLog_page.py
@time: 2018/11/29 13:57
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.logMan.sysEnterLog_locators import SysEnterLogLocators


# 系统管理→日志管理→系统登录日志
class SysEnterLogPage(Page):
    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.exec_script(SysEnterLogLocators.START_DATE_JS)
        self.input(content, *SysEnterLogLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(SysEnterLogLocators.END_DATE_JS)
        self.input(content, *SysEnterLogLocators.QRY_END_DATE)

    # 操作人员
    def inputStr_operator(self, content):
        self.input(content, *SysEnterLogLocators.QRY_OPERATOR)

    # 查询按钮
    def btn_search(self):
        self.click(*SysEnterLogLocators.BTN_SEARCH)
