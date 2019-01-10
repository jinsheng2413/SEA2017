# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: dataRepair_page.py
@time: 2018-10-31 15:11
@desc:
"""

from com.nrtest.common.base_page import Page


class DataRepair_1Page(Page):
    # 用户类型
    def inputSel_cons_sort(self, options):
        # self.click(DataRepair_1Locators.QRY_CONS_SORT)
        # locator = self.get_select_locator(
        #     DataRepair_1Locators.QRY_CONS_SORT_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)
    # 数据类型
    def inputSel_data_type(self, options):
        # self.click(DataRepair_1Locators.QRY_DATA_TYPE)
        # locator = self.get_select_locator(
        #     DataRepair_1Locators.QRY_DATA_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)
    # 开始时间

    def inputDt_start_date(self, value):
        self.input(value)#, *DataRepair_1Locators.QRY_START_DATE)

    # 结束时间
    def inputDt_end_date(self, value):
        self.input(value)#, *DataRepair_1Locators.QRY_END_DATE)

    # 查询
    def btn_qry(self):
        # self.click(DataRepair_1Locators.BTN_QUERY)
        self.btn_query()


# 第二个tab页
class DataRepair_2Page(Page):
    # 数据类型
    def inputSel_data_type(self, options):
        # self.click(DataRepair_2Locators.QRY_DATA_TYPE)
        # locator = self.get_select_locator(
        #     DataRepair_2Locators.QRY_DATA_TYPE_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options,is_multi_tab=True,is_multi_elements=True)

    # 用户类型
    def inputSel_cons_sort(self, options):
        # self.click(DataRepair_2Locators.QRY_CONS_SORT)
        # locator = self.get_select_locator(
        #     DataRepair_2Locators.QRY_CONS_SORT_VALUE, index)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options,is_multi_tab=True,is_multi_elements=True)

    # 查询日期

    def inputDt_query_date(self, value):
        self.curr_input(value,True,True)#, *DataRepair_2Locators.QRY_DATE)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)#, *DataRepair_2Locators.QRY_CONS_NO)

    # 终端资产号
    def inputStr_tmnl_asst_no(self, value):
        self.input(value)#, *DataRepair_2Locators.QRY_TMNL_ASST_NO)

    # 电表局编号
    def inputStr_meter_no(self, value):
        self.input(value)#, *DataRepair_2Locators.QRY_METER_NO)

    # 查询
    def btn_qry(self):
        # self.click(DataRepair_2Locators.BTN_QUERY)
        self.btn_query(True)