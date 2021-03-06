# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesQuery_pages.py
@time: 2018/8/31 0031 9:28
@desc:
"""
from com.nrtest.common.base_page import Page


# 基本应用→档案管理→档案查询
class ArchivesQueryPages(Page):
    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectCheckBox(option)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()

