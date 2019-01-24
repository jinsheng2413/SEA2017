# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: aeeseementResultStatistics_page.py
@time: 2018/11/1 10:18
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损指标考核→考核结果统计
class AeeseementResultStatisticsPage(Page):
    # 责任人
    def inputSel_charge_person(self, index):
        self.selectDropDown(index)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 按日期类型选择
    def inputChk_date_type_sel(self, tab_name):
        self.clickDt_Tab(tab_name)

    # 季度选择
    def inputChk_quarter_sel(self, value):
        self.clickRadioBox(value)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

    # TAB页选择
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)
