# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sectDataQuery_page.py
@time: 2018/9/29 16:09
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→抄表段数据查询
class SectDataQueryPage(Page):
    # 抄表段编号
    def inputStr_mr_sect_no(self, content):
        self.input(content)  # , *SectDataQueryLocators.MR_SECT_NO)

    # 查询按钮
    def btn_search(self):
        # self.click(SectDataQueryLocators.BTN_SEARCH)
        self.btn_query()

    # 数据展示
    # 查询日期，开始
    def inputDt_start_date(self, index):
        self.inputDate(index)

    # 查询日期，结束
    def inputDt_end_date(self, index):
        self.inputDate(index)

    # 查询按钮
    def btn_tab_search(self):
        # self.click(SectDataQueryLocators.BTN_TAB_SEARCH)
        self.btn_query(True)