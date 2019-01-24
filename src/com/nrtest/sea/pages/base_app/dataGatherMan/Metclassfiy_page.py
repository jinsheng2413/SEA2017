# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→电能表分级归类管理
class MetclassfiyPage(Page):

    # 模板名称
    def inputStr_templet_name(self, value):
        self.input(value)

    # 电能表类型
    def inputSel_meter_type(self, option):
        self.selectDropDown(option)

    # 操作
    def inputStr_perform(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
