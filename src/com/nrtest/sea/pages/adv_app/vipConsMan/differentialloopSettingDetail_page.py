# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: differentialloopSettingDetail_page.py
@time: 2018-11-07 13:57
@desc:
"""

from com.nrtest.common.base_page import Page


class DifferentialloopSettingDetail_Page(Page):
    # 用户名称
    def inputStr_cons_name(self, value):
        self.clean_label(value)
        self.input(value)

    # 选择指定行
    def inputRow_select_row(self, row_item):
        self.select_row(row_item)

    # 查询
    def btn_qry(self):
        self.btn_query()
