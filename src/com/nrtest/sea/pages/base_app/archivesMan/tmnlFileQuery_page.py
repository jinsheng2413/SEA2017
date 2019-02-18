# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: tmnlFileQuery_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→巡检仪档案管理
class TmnlFileQueryPage(Page):
    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
