# -*- coding: utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: allMeasureDataCountQuery_page.py
@time: 2018/11/2 11:13
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→全量数据统计查询→全量数据统计查询
class AllMeasureDataCountQueryPage(Page):

    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 用户类型--打开并选择
    def inputSel_cons_type(self, options):
        self.selectDropDown(options)

    # 数据项
    def inputSel_protocol_item(self, options):
        self.selectDropDown(options)

    # 统计维度
    def inputSel_stat_mode(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
