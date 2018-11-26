# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: coreFunctionAudit_page.py
@time: 2018/11/21 0021 9:56
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysUseStat.coreFunctionAudit_locators import CoreFunctionAuditLocators


# 系统管理→系统使用情况统计→系统使用情况统计
class CoreFunctionAuditPage(Page):
    # 操作员
    def inputStr_performer(self, value):
        self.input(value, *CoreFunctionAuditLocators.QRY_PERFORMER)

    # 访问时间
    def inputStr_visitTime(self, value):
        self.input(value, *CoreFunctionAuditLocators.QRY_VISIST_DATE)

    # 到
    def inputStr_TO(self, value):
        self.input(value, *CoreFunctionAuditLocators.QRY_TO)

    # 结束时间
    def inputStr_enDtime(self, value):
        self.input(value, *CoreFunctionAuditLocators.QRY_TO)

        # 查询

    def btn_qry(self):
        self.click(*CoreFunctionAuditLocators.BTN_QRY)
