# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: vipConsStealAnal_page.py
@time: 2018-11-05 14:22
@desc:
"""

from com.nrtest.common.base_page import Page


class VipConsStealAnal_Page(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *VipConsStealAnal_locators.QRY_CONS_NO)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)  #, *VipConsStealAnal_locators.QRY_CONS_NAME)

    def inputChk_type(self, para):
        options = [para['CONS_NORMAL'], para['CONS_UNNORMAL']]
        for option in options:
            self.clickSingleCheckBox(option)

    # 查询
    def btn_qry(self):
        #self.click(*VipConsStealAnal_locators.BTN_QUERY)
        self.btn_query()
