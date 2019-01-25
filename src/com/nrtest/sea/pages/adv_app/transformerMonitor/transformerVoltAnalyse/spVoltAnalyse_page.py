# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→电压质量分析→专/公变电压质量分析
# 专/公变电压质量分析
class SpVoltAnalyseStaticPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item)

    # 日期类型
    def inputChk_date_type(self, option):
        self.clickRadioBox(option, True, True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# 专/公变电压质量明细
class SpVoltAnalyseDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 日期类型
    def inputChk_date_type(self, option):
        self.clickRadioBox(option, True, True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)