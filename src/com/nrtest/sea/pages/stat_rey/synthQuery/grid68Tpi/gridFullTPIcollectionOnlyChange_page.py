# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: grid_full_tpi_collection_onlychange_page.py
@time: 2019-02-12 11:25:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→国网68项指标→国网指标全量采集专变:专变抄表成功率统计
class GridFullTpiCollectionOnlychange_count_Page(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.clean_label(value)
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 统计查询→综合查询→国网68项指标→国网指标全量采集专变:专变抄表失败明细
class GridFullTpiCollectionOnlychange_detail_Page(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.clean_label(value)
        self.inputDate(value, is_multi_tab=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
