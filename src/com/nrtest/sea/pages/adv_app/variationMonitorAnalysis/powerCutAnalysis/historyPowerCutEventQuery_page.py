# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: historyPowerCutEventQuery_page.py
@time: 2018/11/7 14:15
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.variationMonitorAnalysis.powerCutAnalysis.historyPowerCutEventQuery_locators import \
    IntelligentMeterPowerCutEventQueryLocators


# 高级应用→配变监测分析→停电分析→历史停电事件查询
class HistoryPowerCutEventQueryPage(Page):
    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index)

    # 查询日期
    def inputDt_date(self, content):
        # self.exec_script(HistoryPowerCutEventQueryLocators.DATE_JS)
        # self.input(content, *HistoryPowerCutEventQueryLocators.QRY_DATE)
        self.inputDate(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(HistoryPowerCutEventQueryLocators.QRY_CONS_TYPE)
        # locator = self.get_select_locator(HistoryPowerCutEventQueryLocators.QRY_CONS_TYPE_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        # self.click(HistoryPowerCutEventQueryLocators.BTN_SEARCH)
        self.btn_query()

# 高级应用→配变监测分析→停电分析→历史停电事件查询→终端停电事件查询
class TmnlPowerCutEventQueryPage(Page):
    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(TmnlPowerCutEventQueryLocators.QRY_CONS_TYPE)
        # locator = self.get_select_locator(TmnlPowerCutEventQueryLocators.QRY_CONS_TYPE_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # self.click(TmnlPowerCutEventQueryLocators.QRY_TMNL_TYPE)
        # locator = self.get_select_locator(TmnlPowerCutEventQueryLocators.QRY_TMNL_TYPE_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index)

    # 日期
    def inputDt_date(self, content):
        # self.exec_script(TmnlPowerCutEventQueryLocators.DATE_JS)
        # self.input(content, *TmnlPowerCutEventQueryLocators.QRY_DATE)
        self.inputDate(content)

    # 停复电标识
    def inputSel_power_cut_identifying(self, index):
        # self.click(TmnlPowerCutEventQueryLocators.QRY_POWER_CUT_IDENTIFYING)
        # locator = self.get_select_locator(TmnlPowerCutEventQueryLocators.QRY_POWER_CUT_IDENTIFYING_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(TmnlPowerCutEventQueryLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(TmnlPowerCutEventQueryLocators.QRY_TMNL_FACTORY_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index)

    # 是否有效
    def inputSel_whether_valid(self, index):
        # self.click(TmnlPowerCutEventQueryLocators.QRY_WHETHER_VALID)
        # locator = self.get_select_locator(TmnlPowerCutEventQueryLocators.QRY_WHETHER_VALID_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询按钮
    def btn_search(self):
        # self.click(TmnlPowerCutEventQueryLocators.BTN_SEARCH)
        self.btn_query(True)

# 高级应用→配变监测分析→停电分析→历史停电事件查询→智能表停电事件查询
class IntelligentMeterPowerCutEventQueryDetailPage(Page):
    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(IntelligentMeterPowerCutEventQueryLocators.QRY_CONS_TYPE)
        # locator = self.get_select_locator(IntelligentMeterPowerCutEventQueryLocators.QRY_CONS_TYPE_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_date(self, content):
        # self.exec_script(IntelligentMeterPowerCutEventQueryLocators.DATE_JS)
        # self.input(content, *IntelligentMeterPowerCutEventQueryLocators.QRY_DATE)
        self.inputDate(content)

    # 事件正确性
    def inputSel_event_correctness(self, index):
        # self.click(IntelligentMeterPowerCutEventQueryLocators.QRY_EVENT_CORRECTNESS)
        # locator = self.get_select_locator(IntelligentMeterPowerCutEventQueryLocators.QRY_EVENT_CORRECTNESS_VALUE,
        #                                   index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index)

    # 停电时长
    def inputStr_power_cut_start(self, content):
        self.input(content, *IntelligentMeterPowerCutEventQueryLocators.QRY_POWER_CUT_START)

    def inputStr_power_cut_end(self, content):
        self.input(content)  #, *IntelligentMeterPowerCutEventQueryLocators.QRY_POWER_CUT_END)

    # 电表厂家
    def inputSel_meter_factory(self, index):
        # self.click(IntelligentMeterPowerCutEventQueryLocators.QRY_METER_FACTORY)
        # locator = self.get_select_locator(IntelligentMeterPowerCutEventQueryLocators.QRY_METER_FACTORY_VALUE,
        #                                   index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index)

    # 是否有效
    def inputSel_whether_valid(self, index):
        # self.click(IntelligentMeterPowerCutEventQueryLocators.QRY_WHETHER_VALID)
        # locator = self.get_select_locator(IntelligentMeterPowerCutEventQueryLocators.QRY_WHETHER_VALID_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询按钮
    def btn_search(self):
        # self.click(IntelligentMeterPowerCutEventQueryLocators.BTN_SEARCH)
        self.btn_query(True)
