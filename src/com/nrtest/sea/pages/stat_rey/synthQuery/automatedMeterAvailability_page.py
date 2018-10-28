# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: automatedMeterAvailability_page.py
@time: 2018/10/19 10:54
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.automatedMeterAvailability_locators import \
    AutomatedMeterAvailabilityLocators


# 统计查询→综合查询→自动化抄表可用率
class AutomatedMeterAvailabilityPage(Page):
    # 全项采集成功率
    # 表计类型
    def inputSel_meter_type(self, index):
        self.click(*AutomatedMeterAvailabilityLocators.METER_TYPE)
        locator = self.get_select_locator(AutomatedMeterAvailabilityLocators.METER_TYPE_VALUE, index)
        self.click(*locator)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(AutomatedMeterAvailabilityLocators.DATE_JS)
        self.input(content, *AutomatedMeterAvailabilityLocators.DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*AutomatedMeterAvailabilityLocators.BTN_SEARCH)

    # 全项采集失败明细
    # 表计类型
    def inputSel_failed_meter_type(self, index):
        self.click(*AutomatedMeterAvailabilityLocators.FAILED_METER_TYPE)
        locator = self.get_select_locator(AutomatedMeterAvailabilityLocators.FAILED_METER_TYPE_VALUE, index)
        self.click(*locator)

    # 终端地址
    def inputStr_failed_tmnl_addr(self, content):
        self.input(content, *AutomatedMeterAvailabilityLocators.FAILED_TMNL_ADDR)

    # 查询日期
    def inputDt_failed_date(self, content):
        self.exec_script(AutomatedMeterAvailabilityLocators.FAILED_DATE_JS)
        self.input(content, *AutomatedMeterAvailabilityLocators.FAILED_DATE)

    # 查询按钮
    def failed_btn_search(self):
        self.click(*AutomatedMeterAvailabilityLocators.FAILED_BTN_SEARCH)
