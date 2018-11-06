# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: vipConsStealAnal_page.py
@time: 2018-11-05 14:22
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.vipConsStealAnal_locators import VipConsStealAnal_locators


class VipConsStealAnal_Page(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value, *VipConsStealAnal_locators.QRY_CONS_NO)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value, *VipConsStealAnal_locators.QRY_CONS_NAME)

    # 查询
    def btn_qry(self):
        self.click(*VipConsStealAnal_locators.BTN_QUERY)
