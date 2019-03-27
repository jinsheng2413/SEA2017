# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: departManage_page.py
@time: 2019/3/13 11:23
@desc:
"""

# 系统管理--部门管理
from com.nrtest.pbs.locators.sys_man.sysMan_locators import SysMan_locators
from com.nrtest.common.base_page import Page


class DepartManagePage(Page):
    # 输入框
    def input_name(self, value):
        self.input(value, *SysMan_locators.INPUT_NAME1)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
