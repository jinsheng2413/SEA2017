# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.transformerMonitor.transformerVoltAnalyse.orgLowVoltDay.orgLowVoltDayStatic_locators import \
    OrgLowVoltDayStaticLocators


class OrgLowVoltDayStaticPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 开始日期
    def inputStr_start_date(self, value):
        self.input(value, *OrgLowVoltDayStaticLocators.START_DATE)

    # 结束日期
    def inputStr_end_date(self, value):
        self.input(value, *OrgLowVoltDayStaticLocators.END_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*OrgLowVoltDayStaticLocators.BTN_QUERY)
