# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: failListJX_page.py
@time: 2019/01/28 14:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→专公变明细查询(江西)
class failListJxPage(Page):
    # 查询日期
    def inputDt_query_date(self, index):
        self.inputDate(index)

    # Tab页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
