# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: userDefind_page.py
@time: 2019/3/13 13:58
@desc:
"""

from com.nrtest.pbs.locators.sys_man.sysMan_locators import SysMan_locators
from com.nrtest.common.base_page import Page


# 系统管理--用户定义

class UserDefindPage(Page):
    # 输入框
    def input_name(self, value):
        self.input(value, *SysMan_locators.INPUT_NAME3)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
