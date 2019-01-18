# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: fourTableMeterReadSuccessRate_page.py
@time: 2018/10/20 11:04
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→四表合一抄表成功率
# 四表合一抄表成功率
class FourTableMeterReadSuccessRatePage(Page):
    # 表计类型
    def inputSel_meter_type(self, index):
        # self.click(FourTableMeterReadSuccessRateLocators.METER_TYPE)
        # locator = self.get_select_locator(
        #     FourTableMeterReadSuccessRateLocators.METER_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(FourTableMeterReadSuccessRateLocators.DATE_JS)
        # self.input(content, *FourTableMeterReadSuccessRateLocators.DATE)
        self.inputDate(content)

    # 仪表厂家
    def inputSel_meter_factory(self, value):
        self.selectDropDown(value)

    # 终端厂家
    def inputSel_tmnl_factory(self, value):
        self.selectDropDown(value)

    # 查询按钮
    def btn_search(self):
        # self.click(FourTableMeterReadSuccessRateLocators.BTN_SEARCH)
        self.btn_query()


# 四表合一抄表失败明细
class FourTableMeterReadFailedDetailPage(Page):
    # 表计类型
    def inputSel_meter_type(self, index):
        # self.click(FourTableMeterReadSuccessRateLocators.FAILED_METER_TYPE)
        # locator = self.get_select_locator(
        #     FourTableMeterReadSuccessRateLocators.FAILED_METER_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *FourTableMeterReadSuccessRateLocators.FAILED_TMNL_ADDR)

    # 查询日期
    def inputDt_query_date(self, content):
        # self.exec_script(FourTableMeterReadSuccessRateLocators.FAILED_DATE_JS)
        # self.input(content, *FourTableMeterReadSuccessRateLocators.FAILED_DATE)
        self.inputDate(content)

    # 仪表厂家
    def inputSel_meter_factory(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 终端厂家
    def inputSel_tmnl_factory(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        # self.click(FourTableMeterReadSuccessRateLocators.FAILED_BTN_SEARCH)
        self.btn_query(True)
