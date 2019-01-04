# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterSuccessRateQuery_page.py
@time: 2018/10/10 14:48
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表成功率查询（河北）
class MeterSuccessRateQueryPage(Page):
    # 按地区、厂家统计
    # 日期
    def inputDt_factory_date(self, content):
        # self.exec_script(MeterSuccessRateQueryLocators.FACTORY_DATE_JS)
        # self.input(content, *MeterSuccessRateQueryLocators.FACTORY_DATE)
        self.inputDate(content)

    # 用户类型
    def inputSel_factory_cons_type(self, index):
        # if index == 'c':
        #     self._find_element(MeterSuccessRateQueryLocators.FACTORY_CONS_TYPE)
        # else:
        #     self.click(MeterSuccessRateQueryLocators.FACTORY_CONS_TYPE)
        #     locator = self.get_select_locator(
        #         MeterSuccessRateQueryLocators.FACTORY_CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(MeterSuccessRateQueryLocators.FACTORY_CONS_TYPE)
        self.selectCheckBox(index)

    # 终端类型
    def inputSel_factory_tmnl_type(self, index):
        # if index == 'c':
        #     self._find_element(MeterSuccessRateQueryLocators.FACTORY_TMNL_TYPE)
        # else:
        #     self.click(MeterSuccessRateQueryLocators.FACTORY_TMNL_TYPE)
        #     locator = self.get_select_locator(
        #         MeterSuccessRateQueryLocators.FACTORY_TMNL_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(MeterSuccessRateQueryLocators.FACTORY_TMNL_TYPE)
        self.label_clean(index)
        self.selectCheckBox(index)

    # 通信方式
    def inputSel_comm_way(self, index):
        self.selectCheckBox(index)

    # 规约类型
    def inputSel_protocol_type(self, index):
        self.selectCheckBox(index)

    # 用户范围
    def inputSel_cons_range(self, index):
        self.selectDropDown(index)

    # 统计类型
    def inputSel_stat_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def factory_btn_search(self):
        # self.click(MeterSuccessRateQueryLocators.FACTORY_BTN_SEARCH)
        self.btn_query()
