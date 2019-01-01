# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: securityControl_page.py
@time: 2018/10/26 15:41
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→智能锁具→权限控制
class SecurityControlPage(Page):
    # 供电单位，查询按钮
    def btn_cons_search(self):
        # self.click(SecurityControlLocators.BTN_CONS_SEARCH)
        self.btn_query()

    # 锁封编号
    def inputStr_lock_no(self, content):
        self.input(content)  # , *SecurityControlLocators.LOCK_NO)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  #, *SecurityControlLocators.CONS_NO)

    # 查询按钮
    def btn_search(self):
        # self.click(SecurityControlLocators.BTN_SEARCH)
        self.btn_query()
