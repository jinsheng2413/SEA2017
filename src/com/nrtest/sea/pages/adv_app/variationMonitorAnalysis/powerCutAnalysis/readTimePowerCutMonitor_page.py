# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: readTimePowerCutMonitor_page.py
@time: 2018/11/7 10:05
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→停电分析→实时停电监测
class ReadTimePowerCutMonitorPage(Page):
    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

# 高级应用→配变监测分析→停电分析→实时停电监测→实时停电明细
class ReadTimePowerCutDetailPage(Page):
    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index)

    # 信息推送
    def inputSel_information_push(self, index):
        self.selectDropDown(index)

    # 停电范围
    def inputSel_power_cut_scope(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)
