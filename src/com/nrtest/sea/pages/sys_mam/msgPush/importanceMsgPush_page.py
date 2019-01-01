# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: importanceMsgPush_page.py
@time: 2018/11/27 10:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→信息定制→推送信息定制→重要信息推出
class ImportanceMsgPushPage(Page):
    # 角色名称
    def inputStr_role_name(self, content):
        # self.input(content, *ImportanceMsgPushLocators.QRY_ROLE_NAME)
        self.input(content)


    # 查询按钮
    def btn_search(self):
        # self.click(ImportanceMsgPushLocators.BTN_SEARCH)
        self.btn_query()
