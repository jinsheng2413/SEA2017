# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: handworkEnterPlanValue_page.py
@time: 2019-03-13 14:37
@desc:
"""

from com.nrtest.common.base_page import Page


# 业务变更→手工录入计划值
class HandworkEnterPlanValuePage(Page):
    # 时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 提交按钮
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
