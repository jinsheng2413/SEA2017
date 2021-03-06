# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: realtimeData_page.py
@time: 2019-02-14 14:20:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→实时数据查询
class RealtimeDataPage(Page):
    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 菜单名称
    def inputChk_tab_name(self, option):
        self.clickTabPage(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
