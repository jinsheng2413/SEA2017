# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesManage_locators.py
@time: 2018/8/29 0029 13:51
@desc:
"""
from com.nrtest.common.base_page import Page


# 基本应用→档案管理→档案同步
class ArchivesManage_pages(Page):

    # 用户类型
    def inputSel_cons_sort(self, option):
        self.selectDropDown(option)

    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    def btn_qry(self):
        self.btn_query()
