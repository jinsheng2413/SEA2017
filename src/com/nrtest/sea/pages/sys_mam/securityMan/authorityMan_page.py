# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: authorityMan_page.py
@time: 2018/11/23 14:34
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.securityMan.authorityMan_locators import AuthorityManLocators


# 系统管理→权限密码管理→权限管理
class AuthorityManPage(Page):
    # 工号
    def inputStr_staff_no(self, content):
        self.input(content, *AuthorityManLocators.QRY_STAFF_NO)

    # 用户名
    def inputStr_user_name(self, content):
        self.input(content, *AuthorityManLocators.QRY_USER_NAME)

    # 当前状态
    def inputSel_cur_status(self, index):
        self.click(*AuthorityManLocators.QRY_CUR_STATUS)
        locator = self.get_select_locator(AuthorityManLocators.QRY_CUR_STATUS_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*AuthorityManLocators.BTN_SEARCH)
