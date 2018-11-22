# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: historicalDataMonitoring_page.py
@time: 2018/11/20 0020 11:31
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.dataClearing.historicalDataMonitoring_locators import \
    HistoricalDataMonitoringLocators


# 系统管理-->数据清理管理-->历史数据监控
class HistoricalDataMonitoringPage(Page):
    # 数据来源
    def inputSel_data_from(self, name):
        self.click(*HistoricalDataMonitoringLocators.QRY_DATA_FROM)
        locator = self.get_select_locator(HistoricalDataMonitoringLocators.QRY_DATA_FROM_VALUE, name)
        self.click(*locator)

    # 表名称
    def inputStr_listName(self, value):
        self.input(value, *HistoricalDataMonitoringLocators.QRY_LIST_NAME)

    # 数据组
    def inputSel_dataGroup(self, name):
        self.click(*HistoricalDataMonitoringLocators.QRY_DATA_GROUP)
        locator = self.get_select_locator(HistoricalDataMonitoringLocators.QRY_DATA_GROUP_VALUE, name)
        self.click(*locator)

    # 接收时间
    def inputStr_Start_time(self, value):
        self.input(value, *HistoricalDataMonitoringLocators.QRY_START_DATE)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *HistoricalDataMonitoringLocators.QRY_END_DATE)

        # 查询

    def btn_qry(self):
        self.click(*HistoricalDataMonitoringLocators.BTN_QRY)
