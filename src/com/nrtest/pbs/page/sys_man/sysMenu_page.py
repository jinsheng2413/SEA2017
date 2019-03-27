# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: sysMenu_page.py
@time: 2019/3/13 10:39
@desc:
"""
# 系统管理--系统菜单

from com.nrtest.common.base_page import Page
from com.nrtest.pbs.locators.sys_man.sysMan_locators import SysMan_locators


class SysMenuPage(Page):

    # 输入框
    def inputStr_input_name(self, value):
        self.input(value, *SysMan_locators.INPUT_NAME)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
