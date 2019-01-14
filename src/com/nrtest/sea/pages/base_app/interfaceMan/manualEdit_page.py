# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: manualEdit_page.py
@time: 2018-11-07 15:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用--接口管理--人工补录
class ManualEditPage(Page):

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 处理类型
    def inputSel_process_type(self, option):
        self.selectDropDown(option)

    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(ManualEdit_Locators.BTN_QRY)
        self.btn_query()
