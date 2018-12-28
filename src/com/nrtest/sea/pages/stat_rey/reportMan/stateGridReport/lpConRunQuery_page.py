# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: lpConRunQuery_page.py
@time: 2018/11/7 13:41
@desc:
"""
from com.nrtest.common.base_page import Page


# 统计查询--》报表管理--》国网报表--》低压用户运行指标

class IpConRunQueryPage(Page):

    # 查询月份

    def inputStr_date(self, value):
        self.inputDate(value)  # , *IpConRunQueryLocators.QRY_DATE)

    # 统计口径
    def inputSel_statWay(self, option):
        # self.click(*IpConRunQueryLocators.QRY_STAT_WAY)
        # locator = self.get_select_locator(IpConRunQueryLocators.QRY_STAT_WAY_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(*IpConRunQueryLocators.BTN_QRY)
        self.btn_query()
