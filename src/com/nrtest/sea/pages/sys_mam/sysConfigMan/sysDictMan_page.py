# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: sysDictMan_page.py
@time: 2018/9/13 10:23
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→数据字典管理
class SysDictManPage(Page):

    # 分类名称
    def inputStr_catalog_name(self, content):
        self.input(content)

    # 生效日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 失效日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 维护类型--打开并选择
    def inputRSel_cons_type(self, option):
        self.selectDropDown(option)

    # 维护人员
    def inputStr_editor(self, content):
        self.input(content)

    # 维护类型--打开并选择
    def inputRSel_data_source(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_search(self):
        self.btn_query()
