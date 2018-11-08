# -*- coding: utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: allMeasureDataCountQuery_page.py
@time: 2018/11/2 11:13
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.allMeasureDataCountQuery.allMeasureDataCountQuery_locators import \
    AllMeasureDataCountQueryLocators


# 统计查询--》全量数据统计查询--》全量数据统计查询
class AllMeasureDataCountQueryPage(Page):
    # 日期
    def inputStr_date(self, value):
        self.input(value, *AllMeasureDataCountQueryLocators.QRY_DATE)

    # 查询
    def btn_qry(self):
        self.click(*AllMeasureDataCountQueryLocators.BTN_QRY)

    # 重置
    def btn_re(self):
        self.click(*AllMeasureDataCountQueryLocators.BTN_RE)
