# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: differentialloopSetting_page.py
@time: 2018-11-06 10:50
@desc:
"""

from com.nrtest.common.base_page import Page


class DifferentialloopSetting_Page(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *DifferentialloopSetting_locators.QRY_CONS_NO)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)  #, *DifferentialloopSetting_locators.QRY_CONS_NAME)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)  #, *DifferentialloopSetting_locators.QRY_TMNL_ADDR)

    # 终端资产号
    def inputStr_tmnl_asst_no(self, value):
        self.input(value)  #, *DifferentialloopSetting_locators.QRY_TMNL_ASST_NO)

    # 查询
    def btn_qry(self):
        # self.click(*DifferentialloopSetting_locators.BTN_QUERY)
        self.btn_query()
