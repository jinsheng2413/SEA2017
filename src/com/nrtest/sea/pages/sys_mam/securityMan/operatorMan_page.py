# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: operatorMan_page.py
@time: 2018/11/23 10:16
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→权限密码管理→操作员管理
class OperatorManPage(Page):
    # 工号
    def inputStr_staff_no(self, content):
        self.input(content)

    # 用户名
    def inputStr_staff_name(self, content):
        self.input(content)

    # 当前状态
    def inputSel_cur_status(self, option):
        self.selectDropDown(option)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
