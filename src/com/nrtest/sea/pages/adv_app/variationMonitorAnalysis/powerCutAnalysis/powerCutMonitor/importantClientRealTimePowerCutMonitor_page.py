# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: importantClientRealTimePowerCutMonitor_page.py
@time: 2018/11/6 10:43
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→停电分析→停电监测→重要客户实时停电监测→重要客户历史停电查询
class ImportantClientRealTimePowerCutMonitorPage(Page):
    # 电压等级
    def inputSel_volt_level(self, index):
        # self.click(*ImportantClientRealTimePowerCutMonitorLocators.QRY_VOLT_LEVEL)
        # locator = self.get_select_locator(
        #     ImportantClientRealTimePowerCutMonitorLocators.QRY_VOLT_LEVEL_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(index, is_multi_elements=True, is_multi_tab=True)

    # 停电开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(
        #     ImportantClientRealTimePowerCutMonitorLocators.START_DATE_JS)
        # self.input(
        #     content, *ImportantClientRealTimePowerCutMonitorLocators.QRY_START_DATE)
        self.inputDate(content)

    # 停电结束日期
    def inputDt_end_date(self, content):
        # self.exec_script(
        #     ImportantClientRealTimePowerCutMonitorLocators.END_DATE_JS)
        # self.input(
        #     content, *ImportantClientRealTimePowerCutMonitorLocators.QRY_END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(*ImportantClientRealTimePowerCutMonitorLocators.BTN_SEARCH)
        self.btn_query(True)
