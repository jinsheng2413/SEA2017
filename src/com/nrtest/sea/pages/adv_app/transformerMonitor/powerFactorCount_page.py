# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/30 8:42
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用--》配变监测分析--》功率因数越限统计
# 功率因数越限统计
class PowerFactorCountStaticPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()


# 功率因数越限明细
class PowerFactorCountDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item, is_multi_tab=True, is_multi_elements=True)

    # 无功补偿情况--打开并选择
    def inputSel_power_quality_type(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
