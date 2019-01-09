# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用-->台线系统--》资料维护--》专变考核点资料维护
class CheckPointDataRtuPage(Page):
    # 电表正反向
    def inputSel_meter_fr(self, name):
        self.selectDropDown(name)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 抄表段号
    def inputSel_read_no(self, name):
        self.selectDropDown(name)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
