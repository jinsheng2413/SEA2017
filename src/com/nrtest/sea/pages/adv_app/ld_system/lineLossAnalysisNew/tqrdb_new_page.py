# -*- coding: utf-8 -*-

"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: tqrdb_new_page.py
@time: 2019-03-14 16:13:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→台线系统→线损统计(新)→台区日优秀达标查询新
class TqrdbNewPage(Page):
    # 选择人员
    def inputSel_select_person(self, option):
        self.selectDropDown(option)

    # 日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 至日期

    def inputDt_end_date(self, value):
        self.clean_label(value)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
