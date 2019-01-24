# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→电能表状态维护
class MeterStateArrPage(Page):
    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 终端状态
    def inputSel_tmnl_status(self, name):
        self.selectDropDown(name)

    # 终端类型
    def inputSel_tmnl_type(self, name):
        self.selectDropDown(name)

    # 包含下级单位
    def inputChk_contain_org(self, name):
        self.clickSingleCheckBox(name)

    # 查询
    def btn_qry(self):
        self.btn_query()
