# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: stateGridReportQuery_page.py
@time: 2018/11/8 11:38
@desc:
"""
from com.nrtest.common.base_page import Page


# 统计查询--》报表管理--》国网报表--》国网报表新

class StateGridReportQueryPage(Page):
    # 报表类型
    def inputSel_reportType(self, option):
        # self.click(StateGridReportQueryLocators.QRY_REPORT_TYPE)
        # locator = self.get_select_locator(StateGridReportQueryLocators.QRY_REPORT_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(option)

    # 查询方式
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 查询日期

    def inputStr_date(self, value):
        self.inputDate(value)  #, *StateGridReportQueryLocators.QRY_DATE)

    # 查询
    def btn_qry(self):
        # self.click(StateGridReportQueryLocators.BTN_QRY)
        self.btn_query()
