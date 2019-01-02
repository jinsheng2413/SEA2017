# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page


class BcVoltMonitorPointDataPage(Page):
    # 供电单位
    # def inputStr_org_no(self, value):
    #     self.openLeftTree(value)

    # 监测点类型--打开并选择
    def inputSel_monitor_point_type(self, item):
        # self.click(BcVoltMonitorPointDataLocators.MONITOR_POINT_TYPE_SEL)
        # locator = self.get_select_locator(
        #     BcVoltMonitorPointDataLocators.MONITOR_POINT_TYPE, name)
        # self.click(locator)
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 监测点名称
    def inputStr_monitor_point_name(self, value):
        # self.input(value, *BcVoltMonitorPointDataLocators.MONITOR_POINT_NAME)
        self.curr_input(value,is_multi_tab=True,is_multi_elements=True)

    # 查询日期
    def inputStr_query_date(self, value):
        # self.input(value, *BcVoltMonitorPointDataLocators.QUERY_DATE)
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        # self.click(BcVoltMonitorPointDataLocators.BTN_QUERY)
        self.btn_query(True)
