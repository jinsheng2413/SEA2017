# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: accountsAudit_page.py
@time: 2018/11/21 0021 10:35
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysUseStat.accountsAudit_locators import AccountsAuditLocators


# 系统管理→系统使用情况统计→账号审计
class AccountsAuditPage(Page):
    # 时间
    def inputStr_date(self, value):
        self.input(value, *AccountsAuditLocators.QRY_DATE)


    # 账号状态
    def inputStr_accountStatus(self, value):
        self.click(*AccountsAuditLocators.QRY_ACCOUNT_STATUS)
        locator = self.get_select_locator(AccountsAuditLocators.QRY_ACCOUNT_STATUS_VALUE,value)
        self.click(*locator)

        # 查询
    def btn_qry(self):
            self.click(*AccountsAuditLocators.BTN_QRY)