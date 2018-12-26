# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.transformerMonitor.transformerVoltAnalyse.bcVoltMonitorPoint.bcVoltMonitorPointQuery_locators import \
    BcVoltMonitorPointQueryLocators


class BcVoltMonitorPointQueryPage(Page):
    # 供电单位
    # def inputStr_org_no(self, value):
    #     self.openLeftTree(value)

    # 监测点类型--打开并选择
    def inputSel_monitor_point_type(self, item):
        # self.click(*BcVoltMonitorPointQueryLocators.MONITOR_POINT_TYPE_SEL)
        # locator = self.get_select_locator(
        #     BcVoltMonitorPointQueryLocators.MONITOR_POINT_TYPE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 监测点名称
    def inputStr_monitor_point_name(self, value):
        # self.input(value, *BcVoltMonitorPointQueryLocators.MONITOR_POINT_NAME)
        self.input(value)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *BcVoltMonitorPointQueryLocators.QUERY_DATE)
        self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(*BcVoltMonitorPointQueryLocators.BTN_QUERY)
        self.btn_query()