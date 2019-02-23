# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: fourTabStatus_Page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→多表合一运行状态
class FourTabStatusPage(Page):

    # 用户状态
    def inputSel_cons_status(self, name):
        self.selectDropDown(name)

    def inputChk_cons_tab(self, tab_name):
        self.clickTabPage(tab_name)



    # 查询
    def btn_qry(self):
        self.btn_query()
