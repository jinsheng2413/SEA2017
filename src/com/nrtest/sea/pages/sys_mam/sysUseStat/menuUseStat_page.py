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
class MenuUseStatPage(Page):
    # 菜单
    def inputSel_menu(self, index):
        self.click(*MenuUseStatLocators.QRY_MENU)
        locator = self.get_select_locator(MenuUseStatLocators.QRY_MENU_VALUE, index)
        self.click(*locator)

    # 操作员
    def inputStr_operator(self, content):
        self.input(content, *MenuUseStatLocators.QRY_OPERATOR)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.exec_script(MenuUseStatLocators.START_DATE_JS)
        self.input(content, *MenuUseStatLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(MenuUseStatLocators.END_DATE_JS)
        self.input(content, *MenuUseStatLocators.QRY_END_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*MenuUseStatLocators.BTN_SEARCH)


# 系统管理→系统使用情况统计→菜单使用情况统计→菜单使用明细
class MenuUseDetailPage(Page):
    # 菜单
    def inputSel_menu(self, index):
        self.click(*MenuUseDetailLocators.QRY_MENU)
        locator = self.get_select_locator(MenuUseDetailLocators.QRY_MENU_VALUE, index)
        self.click(*locator)

    # 操作员
    def inputStr_operator(self, content):
        self.input(content, *MenuUseDetailLocators.QRY_OPERATOR)

    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.exec_script(MenuUseDetailLocators.START_DATE_JS)
        self.input(content, *MenuUseDetailLocators.QRY_START_DATE)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.exec_script(MenuUseDetailLocators.END_DATE_JS)
        self.input(content, *MenuUseDetailLocators.QRY_END_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*MenuUseDetailLocators.BTN_SEARCH)
