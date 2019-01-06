# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: manualEdit_page.py
@time: 2018-11-07 15:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.interfaceMan.manaualEdit_locators import ManualEdit_Locators


class ManualEditPage(Page):

    # 抄表段号
    def inputStr_meter_reading_paragraph(self, value):
        self.input(value, *ManualEdit_Locators.QRY_METER_READING_PARAGRAPH)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *ManualEdit_Locators.QRY_CONS_NO)

    # 处理类型
    def inputSel_process_type(self, option):
        # self.click(ManualEdit_Locators.QRY_PROCESS_TYPE)
        # locator = self.get_select_locator(ManualEdit_Locators.QRY_PROCESS_TYPE_VALUE, option)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(option)

    def inputDt_date(self, value):
        # self.input(value, *ManualEdit_Locators.QRY_DATE)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(ManualEdit_Locators.BTN_QRY)
        self.btn_query()
