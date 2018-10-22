# -*- coding:utf-8 -*-

'''
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/30 8:42
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.transformerMonitor.powerFactorCount.powerFactorCountDetail_locators import \
    PowerFactorCountDetailLocators

class PowerFactorCountDetailPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputRSel_cons_type(self, name):
        self.click(*PowerFactorCountDetailLocators.CONS_TYPE_SEL)
        locator = self.get_select_locator(PowerFactorCountDetailLocators.CONS_TYPE, name)
        self.click(*locator)

    # 无功补偿情况--打开并选择
    def inputRSel_power_quality_type(self, name):
        self.click(*PowerFactorCountDetailLocators.POWER_QUALITY_TYPE_SEL)
        locator = self.get_select_locator(PowerFactorCountDetailLocators.POWER_QUALITY_TYPE, name)
        self.click(*locator)

    # 查询日期
    def inputStr_query_date(self, value):
        self.input(value, *PowerFactorCountDetailLocators.QUERY_DATE)

    # 点击查询
    def btn_query(self):
        self.click(*PowerFactorCountDetailLocators.BTN_QUERY)
