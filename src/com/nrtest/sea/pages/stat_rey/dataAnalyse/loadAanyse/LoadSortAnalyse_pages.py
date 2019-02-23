# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: LoadSortAnalyse_pages.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class LoadSortAnalysePage(Page):
    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectDropDown(options)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 排名数量
    def inputStr_ranking_number(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()