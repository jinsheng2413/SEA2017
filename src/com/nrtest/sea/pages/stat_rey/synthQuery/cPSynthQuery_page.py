# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: cPSynthQuery_page.py
@time: 2018/10/20 14:04
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.cPSynthQuery_locators import CPSynthQueryLocators


# 统计查询→综合查询→采集点综合查询
class CPSynthQueryPage(Page):
    # 终端状态
    def inputSel_tmnl_status(self, index):
        self.click(*CPSynthQueryLocators.TMNL_STATUS)
        locator = self.get_select_locator(CPSynthQueryLocators.TMNL_STATUS_VALUE, index)
        self.click(locator)

    # 用户范围
    def inputSel_cons_range(self, index):
        self.click(*CPSynthQueryLocators.CONS_RANGE)
        locator = self.get_select_locator(CPSynthQueryLocators.CONS_RANGE_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(*CPSynthQueryLocators.BTN_SEARCH)
