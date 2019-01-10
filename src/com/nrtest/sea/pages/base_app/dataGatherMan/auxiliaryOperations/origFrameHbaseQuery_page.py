# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: origFrameHbaseQuery_page.py
@time: 2018/11/9 0009 15:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理-->采集运维平台-->辅助运维--》报文查询
class OrigFrameHbaseQueryPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)  # , *OrigFrameHbaseQueryLocators.QRY_TMNL_ADDR)

    # 报文类型
    def inputSel_messageType(self, name):
        # self.click(OrigFrameHbaseQueryLocators.QRY_MESSAGE_TYPE)
        # locator = self.get_select_locator(OrigFrameHbaseQueryLocators.QRY_MESSAGE_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(name)

    # 查询时间
    def inputStr_query_time(self, value):
        self.input(value)  # , *OrigFrameHbaseQueryLocators.QRY_QUERY_TIME)

    # 从
    def inputDt_from(self, value):
        # self.input(value, *OrigFrameHbaseQueryLocators.QRY_FROM)
        self.inputDate(value)
     # 到
    def inputDt_to(self, value):
        # self.input(value, *OrigFrameHbaseQueryLocators.QRY_TO)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(OrigFrameHbaseQueryLocators.BTN_QRY)
        self.btn_query()
