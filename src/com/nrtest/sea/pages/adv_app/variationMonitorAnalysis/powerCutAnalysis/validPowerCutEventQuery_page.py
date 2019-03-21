# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: validPowerCutEventQuery_page.py
@time: 2018/11/2 16:19
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.validPowerCutEventQuery_locators import \
    ValidPowerCutDetailLocators


# 高级应用→配变监测分析→停电分析→有效停电事件查询:有效停电事件查询
class ValidPowerCutEventQueryPage(Page):
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

# 高级应用→配变监测分析→停电分析→有效停电事件查询→有效停电明细
class ValidPowerCutDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 当前是否停电
    def inputSel_whether_power_cut(self, index):
        self.selectDropDown(index)

    # 是否有效停电
    def inputSel_whether_power_cut_valid(self, index):
        self.selectDropDown(index)

    # 是否补全
    def inputSel_whether_complement(self, index):
        self.selectDropDown(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 停电时长
    def inputStr_power_cut_start(self, content):
        self.input(content, *ValidPowerCutDetailLocators.QRY_POWER_CUT_START)

    def inputStr_power_cut_end(self, content):
        self.input(content, *ValidPowerCutDetailLocators.QRY_POWER_CUT_END)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
