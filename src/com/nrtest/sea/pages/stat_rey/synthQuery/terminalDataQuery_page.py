# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: terminalDataQuery_page.py
@time: 2018/8/13 0002 14:00
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→终端数据查询
class TerminalDataQueryPage(Page):
    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content)  # , *TerminalDataQueryLocators.QRY_TMNL_ASSET_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *TerminalDataQueryLocators.QRY_TMNL_ADDR)

    # 查询按钮
    def btn_search(self):
        # self.click(TerminalDataQueryLocators.BTN_SEARCH)
        self.btn_query()
