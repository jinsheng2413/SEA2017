# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: dataCollectMon_page.py
@time: 2019-02-15 15:08:45
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集数据甄别分析→数据采集监测
class DataCollectMonPage(Page):
    # 月份
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 业务系统
    def inputSel_business_system(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
