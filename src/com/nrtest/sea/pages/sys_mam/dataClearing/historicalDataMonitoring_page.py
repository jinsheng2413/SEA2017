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
    def inputSel_data_from(self, options):
        self.selectDropDown(options)

    # 表名称
    def inputSel_list_name(self, value):
        self.input(value)

    # 数据组
    def inputSel_data_group(self, options):
        self.selectDropDown(options)

    # 接收时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
