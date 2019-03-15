# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tq_sdc_xs_page.py
@time: 2019-03-15 11:24:41
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→查询管理→台区售电侧月线损电量查询
class TqSdcXsPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 售电类型
    def inputSel_sale_type(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
