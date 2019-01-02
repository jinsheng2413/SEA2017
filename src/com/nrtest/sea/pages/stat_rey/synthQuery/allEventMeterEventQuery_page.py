# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: allEventMeterEventQuery_page.py
@time: 2018/9/30 14:33
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.allEventMeterEventQuery_locators import AllEventMeterEventQueryLocators


# 统计查询→综合查询→全事件电表事件查询
class AllEventMeterEventQueryPage(Page):
    # 电表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content, *AllEventMeterEventQueryLocators.METER_ASSET_NO)

    # 事件等级
    def inputSel_event_level(self, index):
        self.click(AllEventMeterEventQueryLocators.EVENT_LEVEL)
        locator = self.get_select_locator(
            AllEventMeterEventQueryLocators.EVENT_LEVEL_VALUE, index)
        self.click(locator)

    # 事件类型
    def inputSel_event_type(self, index):
        self.click(AllEventMeterEventQueryLocators.EVENT_TYPE)
        locator = self.get_select_locator(
            AllEventMeterEventQueryLocators.EVENT_TYPE_VALUE, index)
        self.click(locator)

    # 采集开始时间
    def inputDt_start_date(self, content):
        self.exec_script(AllEventMeterEventQueryLocators.START_DATE_JS)
        self.input(content, *AllEventMeterEventQueryLocators.START_DATE)

    # 采集结束时间
    def inputDt_end_date(self, content):
        self.exec_script(AllEventMeterEventQueryLocators.END_DATE_JS)
        self.input(content, *AllEventMeterEventQueryLocators.END_DATE)

    # 查询按钮
    def btn_search(self):
        self.click(AllEventMeterEventQueryLocators.BTN_SEARCH)
