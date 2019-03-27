# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: balanceBrowse_page.py
@time: 2019-03-15 10:04
@desc:
"""

from com.nrtest.common.base_page import Page


# 线损分析→母平浏览:母平汇总
class BalanceBrowseCollectPage(Page):
    # 区域
    def inputSel_area(self, value):
        self.selectDropDown(value)

    # 时间方案
    def inputChk_date_type(self, value):
        self.clickTabPage(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)


# 线损分析→母平浏览:母平查询
class BalanceBrowseQueryPage(Page):
    # 电压
    def inputSel_voltage(self, value):
        self.selectDropDown(value)

    # 类型
    def inputSel_type(self, value):
        self.selectDropDown(value)

    # 损耗率
    def inputSel_attrition_rate(self, value):
        self.selectDropDown(value)

    # 时间类型
    def inputChk_date_type(self, value):
        self.clickTabPage(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
