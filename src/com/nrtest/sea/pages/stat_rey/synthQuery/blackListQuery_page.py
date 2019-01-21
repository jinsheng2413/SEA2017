# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: blackListQuery_page.py
@time: 2018/10/20 14:59
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→黑名单查询
class BlackListQueryPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  # , *BlackListQueryLocators.CONS_NO)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(BlackListQueryLocators.DATE_JS)
        # self.input(content, *BlackListQueryLocators.DATE)
        self.inputDate(content)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *BlackListQueryLocators.TMNL_ADDR)

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
        # self.click(BlackListQueryLocators.BTN_SEARCH)
        self.btn_query()
