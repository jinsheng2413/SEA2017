# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: whiteListQuery_page.py
@time: 2018/10/19 14:42
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→白名单查询
class WhiteListQueryPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  # , *WhiteListQueryLocators.CONS_NO)

    # 开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(WhiteListQueryLocators.START_DATE_JS)
        # self.input(content, *WhiteListQueryLocators.START_DATE)
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        # self.exec_script(WhiteListQueryLocators.END_DATE_JS)
        # self.input(content, *WhiteListQueryLocators.END_DATE)
        self.inputDate(content)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *WhiteListQueryLocators.TMNL_ADDR)

    # 电能表资产号
    def inputStr_meter_asset_no(self, index):
        self.input(index)

    # 开户卡号
    def inputStr_open_card_no(self, index):
        self.input(index)

    # 白名单卡号
    def inputStr_white_card_no(self, index):
        self.input(index)

    # 查询按钮
    def btn_search(self):
        # self.click(WhiteListQueryLocators.BTN_SEARCH)
        self.btn_query()