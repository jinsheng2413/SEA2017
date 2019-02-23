# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gridFullTPIcollectionLowThreePhase_page.py
@time: 2019-02-12 11:25:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→国网68项指标→国网指标全量采集低压三相
class GridFullTpiCollectionLowThreePhasePage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.clean_label(value)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
