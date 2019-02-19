# -*- coding: utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: workQuery_page.py
@time: 2018/10/31 15:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→工单查询→工单查询
class WorkCountPage(Page):

    # 日期
    def inputDt_query_date(self, value):
        self.clean_label(value)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()

class WorkQueryPage(Page):

    # 异常编号
    def inputStr_abnormal_no(self, value):
        self.input(value)

    # 异常状态
    def inputSel_abnormal_status(self, options):

        self.selectDropDown(options)

    # 日期
    def inputDt_query_date(self, value):
        self.clean_label(value)
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
