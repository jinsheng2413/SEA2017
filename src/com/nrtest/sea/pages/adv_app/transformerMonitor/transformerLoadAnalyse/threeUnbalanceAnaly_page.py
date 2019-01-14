# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/24 20:42
@desc:
"""

from com.nrtest.common.base_page import Page

# 高级应用--》配变负载分析--》三相不平衡分析
# 三相不平衡统计
class ThreeUnbalanceAnalyStaticPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# 三相不平衡明细
class ThreeUnbalanceAnalyDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item,True,1,True)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)