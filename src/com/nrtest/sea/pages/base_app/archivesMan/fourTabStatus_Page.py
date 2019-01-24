# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class FourTabStatusPage(Page):

    # 用户状态
    def inputSel_cons_status(self, name):
        self.selectDropDown(name)

    # 查询
    def btn_qry(self):
        self.btn_query()
