# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→资料维护→线路资料维护
class LineDocManagePage(Page):

    # 变电站
    def inputSel_subs(self, name):
        self.selectDropDown(name)

    # 负责人
    def inputSel_master(self, name):
        self.selectDropDown(name)

    # 线路名称
    def inputStr_line_name(self, value):
        self.input(value)

    # 无负责人
    def Chk_no_master(self, value):
        self.clickSingleCheckBox(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
