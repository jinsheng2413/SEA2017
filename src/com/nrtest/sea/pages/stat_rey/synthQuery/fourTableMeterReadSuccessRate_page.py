# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: fourTableMeterReadSuccessRate_page.py
@time: 2018/10/20 11:04
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.fourTableMeterReadSuccessRate_locators import \
    FourTableMeterReadSuccessRateLocators


# 统计查询→综合查询→自动化抄表可用率
class FourTableMeterReadSuccessRatePage(Page):
    # 全项采集成功率
    # 表计类型
    def inputSel_meter_type(self, index):
        self.click(*FourTableMeterReadSuccessRateLocators.METER_TYPE)
        locator = self.get_select_locator(FourTableMeterReadSuccessRateLocators.METER_TYPE_VALUE, index)
        self.click(*locator)

    # 查询日期
    def inputDt_date(self, content):
        self.exec_script(FourTableMeterReadSuccessRateLocators.DATE_JS)
        self.input(content, *FourTableMeterReadSuccessRateLocators.DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*FourTableMeterReadSuccessRateLocators.BTN_SEARCH)

    # 四表合一抄表失败明细
    # 表计类型
    def inputSel_failed_meter_type(self, index):
        self.click(*FourTableMeterReadSuccessRateLocators.FAILED_METER_TYPE)
        locator = self.get_select_locator(FourTableMeterReadSuccessRateLocators.FAILED_METER_TYPE_VALUE, index)
        self.click(*locator)

    # 终端地址
    def inputStr_failed_tmnl_addr(self, content):
        self.input(content, *FourTableMeterReadSuccessRateLocators.FAILED_TMNL_ADDR)

    # 查询日期
    def inputDt_failed_date(self, content):
        self.exec_script(FourTableMeterReadSuccessRateLocators.FAILED_DATE_JS)
        self.input(content, *FourTableMeterReadSuccessRateLocators.FAILED_DATE)

    # 查询按钮
    def failed_btn_search(self):
        self.click(*FourTableMeterReadSuccessRateLocators.FAILED_BTN_SEARCH)
