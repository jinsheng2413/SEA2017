# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: collocateDataQuery_page.py
@time: 2018-08-15 16:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→配变数据查询:基本档案
from com.nrtest.sea.locators.stat_rey.synthQuery.publicDataQuery_locators import PublicDataQueryLocators


class CollcateDataQueryDocPage(Page):

    # 配变表号
    def inputSel_meter_asset_no(self, value):
        self.selectDropDown(value)

    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→配变数据查询:数据展示
class CollcateDataQueryDataPage(Page):

    # 配变表号
    def inputSel_meter_asset_no(self, value):
        self.selectDropDown(value)

    def btn_search(self):
        self.btn_query(is_multi_tab=True, idx=1)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 一二次测量值
    def inputSel_meas_value(self, option):
        self.specialDropdown(option, PublicDataQueryLocators.MEAS_VALUE)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value, is_multi_tab=True)

    def btn_qry(self):
        self.btn_query(True, idx=2)
