# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: manualEditQH_page.py
@time: 2018-11-07 16:34
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.interfaceMan.manualEditQH_locators import ManualEditQH_Locators


class ManualEditQHPage(Page):

    # 抄表段号
    def inputStr_meter_reading_paragraph(self, value):
        self.input(value, *ManualEditQH_Locators.QRY_METER_READING_PARAGRAPH)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value, *ManualEditQH_Locators.QRY_CONS_NO)

    # 数据来源
    def inputSel_data_from(self, index):
        self.click(ManualEditQH_Locators.QRY_DATA_FROM)
        locator = self.get_select_locator(ManualEditQH_Locators.QRY_DATA_FROM_VALUE, index)
        self.click(locator)
        self.delDropdownBoxHtml()

    def inputStr_date(self, value):
        self.input(value, *ManualEditQH_Locators.QRY_DATE)

    # 查询
    def btn_qry(self):
        self.click(ManualEditQH_Locators.BTN_QRY)
