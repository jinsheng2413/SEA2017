# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: menuUseStat_page.py
@time: 2018/11/30 11:25
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysUseStat.menuUseStat_locators import *


# 系统管理→系统使用情况统计→菜单使用情况统计
# 菜单使用统计
class MenuUseStatPage(Page):
    # 菜单
    def inputSel_menu(self, options):
        self.selectDropDown(options)

    # 操作员
    def inputStr_operator(self, content):
        self.input(content)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)


# 系统管理→系统使用情况统计→菜单使用情况统计
# 菜单使用明细
class MenuUseDetailPage(Page):
    # 菜单
    def inputSel_menu(self, options):
        self.selectDropDown(options,is_multi_tab=True,is_multi_elements=True)

    # 操作员
    def inputStr_operator(self, content):
        self.curr_input(content,is_multi_tab=True,is_multi_elements=True)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)
