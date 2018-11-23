# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: operatorMan_page.py
@time: 2018/11/23 10:16
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.securityMan.operatorMan_locators import OperatorManLocators


# 系统管理→权限密码管理→操作员管理
class OperatorManPage(Page):
    # 工号
    def inputStr_staff_no(self, content):
        self.input(content, *OperatorManLocators.QRY_STAFF_NO)

    # 用户名
    def inputStr_user_name(self, content):
        self.input(content, *OperatorManLocators.QRY_USER_NAME)

    # 当前状态
    def inputSel_cur_status(self, index):
        self.click(*OperatorManLocators.QRY_CUR_STATUS)
        locator = self.get_select_locator(OperatorManLocators.QRY_CUR_STATUS_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*OperatorManLocators.BTN_SEARCH)
