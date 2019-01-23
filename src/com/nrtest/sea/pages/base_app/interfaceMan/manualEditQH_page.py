# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: manualEditQH_page.py
@time: 2018-11-07 16:34
@desc:
"""

from com.nrtest.common.base_page import Page


class ManualEditQHPage(Page):

    # 抄表段号
    def inputStr_meter_reading_paragraph(self, value):
        self.input(value)  # , *ManualEditQH_Locators.QRY_METER_READING_PARAGRAPH)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *ManualEditQH_Locators.QRY_CONS_NO)

    # 数据来源
    def inputSel_data_src(self, option):
        # self.click(ManualEditQH_Locators.QRY_DATA_SRC)
        # locator = self.get_select_locator(ManualEditQH_Locators.QRY_DATA_SRC_VALUE, option)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(option)

    def inputDt_query_date(self, value):
        # self.input(value, *ManualEditQH_Locators.QRY_DATE)
        self.inputDate(value)

    def inputChk_powerEmpty(self, name):
        self.clickSingleCheckBox(name)

    # 查询
    def btn_qry(self):
        # self.click(ManualEditQH_Locators.BTN_QRY)
        self.btn_query()
