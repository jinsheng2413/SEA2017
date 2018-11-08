# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: availableCapacityAnalyse_page.py
@time: 2018/9/27 15:43
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.transformerMonitor.transformerLoadAnalyse.availableCapacityAnalyse_locators import \
    AvailableCapacityAnalyseLocators


class AvailableCapacityAnalysePage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *AvailableCapacityAnalyseLocators.QUERY_DATE)

    # 负载率
    def inputStr_load_rate(self, value):
        self.input(value, *AvailableCapacityAnalyseLocators.LOAD_RATE)

    # 点击查询
    def btn_query(self):
        self.click(*AvailableCapacityAnalyseLocators.BTN_QUERY)
