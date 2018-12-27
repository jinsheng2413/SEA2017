# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: roleMan_page.py
@time: 2018/11/23 11:34
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.securityMan.roleMan_locators import RoleMAnLocators


# 系统管理→权限密码管理→角色管理
class RoleMAnPage(Page):
    # 角色名称
    def inputStr_role_name(self, content):
        # self.input(content, *RoleMAnLocators.QRY_ROLE_NAME)

        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.click(*RoleMAnLocators.BTN_SEARCH)
