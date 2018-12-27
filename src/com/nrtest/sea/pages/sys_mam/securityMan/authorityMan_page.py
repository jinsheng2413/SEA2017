# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: authorityMan_page.py
@time: 2018/11/23 14:34
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→权限密码管理→权限管理
class AuthorityManPage(Page):
    # 工号
    def inputStr_staff_no(self, content):
        # #self.input(content, *AuthorityManLocators.QRY_STAFF_NO)

        self.input(content)
        # self.curr_input(content,is_multi_tab=True,is_multi_elements=True)

    # 用户名
    def inputStr_user_name(self, content):
        # self.input(content, *AuthorityManLocators.QRY_USER_NAME)
        self.input(content)

    # 当前状态
    def inputSel_cur_status(self, option):
        # self.click(*AuthorityManLocators.QRY_CUR_STATUS)
        ## locator = self.get_select_locator(AuthorityManLocators.QRY_CUR_STATUS_VALUE, option)
        ## #self.click(*locator)
        # self.selectDropDown(is_multi_tab=True,is_multi_elements=True)
        # self.selectCheckBox(is_multi_tab=True,is_multi_elements=True)
        self.selectDropDown(option)

    #
    # 查询按钮
    def btn_search(self):
        # self.click(*AuthorityManLocators.BTN_SEARCH)
        self.btn_query()
