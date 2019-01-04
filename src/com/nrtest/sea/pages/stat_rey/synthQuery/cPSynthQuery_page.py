# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: cPSynthQuery_page.py
@time: 2018/10/20 14:04
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集点综合查询
class CPSynthQueryPage(Page):
    # 终端状态
    def inputSel_tmnl_status(self, index):
        # self.click(CPSynthQueryLocators.TMNL_STATUS)
        # locator = self.get_select_locator(
        #     CPSynthQueryLocators.TMNL_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 用户范围
    def inputSel_cons_range(self, index):
        # self.click(CPSynthQueryLocators.CONS_RANGE)
        # locator = self.get_select_locator(
        #     CPSynthQueryLocators.CONS_RANGE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 停电标志
    def inputSel_power_out_sign(self, index):
        self.selectDropDown(index)

    # 终端投运日期
    def inputChk_tmnl_comm_date(self, index):
        self.clickSingleCheckBox(index)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 终端用途
    def inputChk_tmnl_way(self, value):
        self.clickRadioBox(value)

    # 接线方式
    def inputSel_line_way(self, value):
        self.selectDropDown(value)

    # 查询按钮
    def btn_search(self):
        # self.click(CPSynthQueryLocators.BTN_SEARCH)
        self.btn_query()
