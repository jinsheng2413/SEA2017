# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: paperManage_page.py
@time: 2019/3/13 11:40
@desc:
"""
from com.nrtest.common.base_page import Page
# 系统管理--页面管理
from com.nrtest.pbs.locators.sys_man.sysMan_locators import SysMan_locators


class PaperManagePage(Page):
    # 输入框
    def input_name(self, value):
        self.input(value, *SysMan_locators.INPUT_NAME2)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
