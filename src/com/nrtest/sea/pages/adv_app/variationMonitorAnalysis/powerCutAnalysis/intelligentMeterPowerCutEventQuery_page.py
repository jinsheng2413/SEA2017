# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: intelligentMeterPowerCutEventQuery_page.py
@time: 2018/11/5 14:42
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.intelligentMeterPowerCutEventQuery_locators import *


# 高级应用→配变监测分析→停电分析→智能表停电事件查询：智能表停电统计
class IntelligentMeterPowerCutEventQueryPage(Page):
    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()

# 高级应用→配变监测分析→停电分析→智能表停电事件查询→智能表停电明细
class IntelligentMeterPowerCutEventQueryDetailPage(Page):
    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index, is_multi_elements=True, is_multi_tab=True)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 事件正确性
    def inputSel_event_correctness(self, index):
        self.selectDropDown(index)

    # 停电时长
    def inputStr_power_cut_start(self, content):
        self.input(content, *IntelligentMeterPowerCutEventQueryDetailLocators.QRY_POWER_CUT_START)

    def inputStr_power_cut_end(self, content):
        self.input(content)

    # 电表厂家
    def inputSel_meter_factory(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
