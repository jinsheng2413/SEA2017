# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.transformerMonitor.transformerVoltAnalyse.orgLowVoltDay.orgLowVoltDayDetail_locators import \
    OrgLowVoltDayDetailLocators


class OrgLowVoltDayDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 开始日期
    def inputStr_start_date(self, value):
        # self.input(value, *OrgLowVoltDayDetailLocators.START_DATE)
        self.input(value)

    # 结束日期
    def inputStr_end_date(self, value):
        # self.input(value, *OrgLowVoltDayDetailLocators.END_DATE)
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        # self.input(value, *OrgLowVoltDayDetailLocators.TG_NAME)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*OrgLowVoltDayDetailLocators.BTN_QUERY)
        self.btn_query()
