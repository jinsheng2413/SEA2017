# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlPowerCutEventQuery_page.py
@time: 2018/11/5 10:29
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→停电分析→终端停电事件查询
class TmnlPowerCutEventQueryPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(*TmnlPowerCutEventQueryLocators.QRY_CONS_TYPE)
        # locator = self.get_select_locator(
        #     TmnlPowerCutEventQueryLocators.QRY_CONS_TYPE_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, True, True)

    # 月份
    def inputDt_date(self, content):
        # self.exec_script(TmnlPowerCutEventQueryLocators.DATE_JS)
        # self.input(content, *TmnlPowerCutEventQueryLocators.QRY_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(*TmnlPowerCutEventQueryLocators.BTN_SEARCH)
        self.btn_query()

    # 统计类型
    def inputChk_stat_type(self, content):
        self.clickRadioBox(content)

# 高级应用→配变监测分析→停电分析→终端停电事件查询→月终端停电明细
class TmnlPowerCutEventQueryMonthPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(*TmnlPowerCutEventQueryMonthLocators.QRY_CONS_TYPE)
        # locator = self.get_select_locator(
        #     TmnlPowerCutEventQueryMonthLocators.QRY_CONS_TYPE_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 月份
    def inputDt_date(self, content):
        # self.exec_script(TmnlPowerCutEventQueryMonthLocators.DATE_JS)
        # self.input(content, *TmnlPowerCutEventQueryMonthLocators.QRY_DATE)
        self.inputDate(content)

    # 停电次数
    def inputStr_power_cut_time(self, content):
        self.input(content)  #, *TmnlPowerCutEventQueryMonthLocators.QRY_POWER_CUT_TIME)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(*TmnlPowerCutEventQueryMonthLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     TmnlPowerCutEventQueryMonthLocators.QRY_TMNL_FACTORY_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        # self.click(*TmnlPowerCutEventQueryMonthLocators.BTN_SEARCH)
        self.btn_query(True)

# 高级应用→配变监测分析→停电分析→终端停电事件查询→日终端停电明细
class TmnlPowerCutEventQueryDayPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(*TmnlPowerCutEventQueryDayLocators.QRY_CONS_TYPE)
        # locator = self.get_select_locator(
        #     TmnlPowerCutEventQueryDayLocators.QRY_CONS_TYPE_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_date(self, content):
        # self.exec_script(TmnlPowerCutEventQueryDayLocators.DATE_JS)
        # self.input(content, *TmnlPowerCutEventQueryDayLocators.QRY_DATE)
        self.inputDate(content)

    # 停复电标识
    def inputSel_power_cut_identifying(self, index):
        # self.click(*TmnlPowerCutEventQueryDayLocators.QRY_POWER_CUT_IDENTIFYING)
        # locator = self.get_select_locator(
        #     TmnlPowerCutEventQueryDayLocators.QRY_POWER_CUT_IDENTIFYING_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        # self.click(*TmnlPowerCutEventQueryDayLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     TmnlPowerCutEventQueryDayLocators.QRY_TMNL_FACTORY_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        # self.click(*TmnlPowerCutEventQueryDayLocators.BTN_SEARCH)
        self.btn_query(True)
