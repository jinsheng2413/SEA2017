# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: sysDictMan_page.py
@time: 2018/9/13 10:23
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysConfigMan.sysDictMan_locators import SysDictManLocators


class SysDictManPage(Page):

    # 分类名称
    def inputStr_catalog_name(self, value):
        self.input(value, *SysDictManLocators.CATALOG_NAME)

    # 生效日期
    def inputStr_start_date(self, value):
        self.input(value, *SysDictManLocators.START_DATE)

    # 失效日期
    def inputStr_end_date(self, value):
        self.input(value, *SysDictManLocators.END_DATE)

    # 维护类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*SysDictManLocators.EDIT_TYPE_SEL)
        locator = self.get_select_locator(SysDictManLocators.EDIT_TYPE, name)
        self.click(*locator)

    # 维护人员
    def inputStr_editor(self, value):
        self.input(value, *SysDictManLocators.EDITOR)

    # 维护类型--打开并选择
    def inputRSel_data_source(self, name):
        self.click(*SysDictManLocators.DATA_SOURCE_SEL)
        locator = self.get_select_locator(SysDictManLocators.DATA_SOURCE, name)
        self.click(*locator)

    # 点击查询
    def btn_query(self):
        self.click(*SysDictManLocators.BTN_QUERY)
