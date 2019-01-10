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

    # 日期类型
    def inputChk_data_method(self, option):
        self.clickRadioBox(option)

    # 时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 账号状态
    def inputSel_account_status(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
