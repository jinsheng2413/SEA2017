# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: chip_archives_query_page.py
@time: 2019-04-11 17:12:21
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC芯片管理→芯片档案查询功能
class ChipArchivesQueryPage(Page):
    # 设备类型
    def inputSel_equip_type(self, option):
        self.selectDropDown(option)

    # 芯片ID号
    def inputStr_chipid(self, value):
        self.input(value)

    # 所属终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 规约
    def inputSel_protocal_code(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
