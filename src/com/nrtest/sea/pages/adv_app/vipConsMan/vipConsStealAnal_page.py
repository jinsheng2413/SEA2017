# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: vipConsStealAnal_page.py
@time: 2018-11-05 14:22
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→重点用户窃电分析
class VipConsStealAnal_Page(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 类型
    def inputChk_use_elec_type(self, options):
        self.clickCheckBox_new(options)

    # 查询
    def btn_qry(self):
        # self.click(VipConsStealAnal_locators.BTN_QUERY)
        self.btn_query()
