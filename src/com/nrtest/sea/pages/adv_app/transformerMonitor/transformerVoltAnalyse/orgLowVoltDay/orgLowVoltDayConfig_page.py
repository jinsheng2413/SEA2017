# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page


class OrgLowVoltDayConfigPage(Page):
    # 供电单位
    def inputStr_org_no(self, value):
        self.openLeftTree(value)

    # 是否电压监测--打开并选择
    def inputSel_volt_monitor(self, item):
        # self.click(*OrgLowVoltDayConfigLocators.IS_VOLT_MONITOR_SEL)
        # locator = self.get_select_locator(
        #     OrgLowVoltDayConfigLocators.IS_VOLT_MONITOR, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 点击查询
    def btn_qry(self):
        # self.click(*OrgLowVoltDayConfigLocators.BTN_QUERY)
        self.btn_query()
