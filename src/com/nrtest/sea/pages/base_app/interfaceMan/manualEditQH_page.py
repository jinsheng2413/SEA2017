# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: manualEditQH_page.py
@time: 2018-11-07 16:34
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→接口管理→人工补录（青海）
class ManualEditQHPage(Page):

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 数据来源
    def inputSel_data_from(self, option):
        self.selectDropDown(option)

    def inputDt_query_date(self, value):
        self.inputDate(value)

    def inputChk_power_empty(self, name):
        self.clickSingleCheckBox(name)

    # 查询
    def btn_qry(self):
        self.btn_query()
