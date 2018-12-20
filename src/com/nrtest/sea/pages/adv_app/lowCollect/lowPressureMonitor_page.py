# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: lowPressureMonitor_page.py
@time: 2018-11-01 11:03
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lowCollect.lowPressureMonitor_locators import LowPressureMonitor_Locators


class LowPressureMonitor_Page(Page):
    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value, *LowPressureMonitor_Locators.QRY_TG_NAME)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *LowPressureMonitor_Locators.QRY_TMNL_ADDR)

    # 用户定义类别
    def inputSel_cons_define_type(self, index):
        self.click(*LowPressureMonitor_Locators.QRY_CONS_DEFINE_TYPE)
        locator = self.get_select_locator(
            LowPressureMonitor_Locators.QRY_CONS_DEFINE_TYPE_VALUE, index)
        self.click(*locator)

    # 查询
    def btn_qry(self):
        self.click(*LowPressureMonitor_Locators.BTN_QUERY)
