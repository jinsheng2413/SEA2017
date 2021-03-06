# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: indexDetail_page.py
@time: 2018/11/2 15:00
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损管理→同期线损→指标明细
class IndexDetailPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.clean_label(content)
        self.curr_input(content, is_multi_tab=True)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.clean_label(content)
        self.curr_input(content, is_multi_tab=True)

    # 时间选择
    def inputDt_query_date(self, content):
        self.clean_label(content)
        self.inputDate(content, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)


# 高级应用→线损管理→个性化指标展示→指标明细：指标统计
class IndexDetailStatPage(Page):
    # 工号
    def inputStr_staff_no(self, name):
        self.clean_label(name)
        self.curr_input(name, is_multi_tab=True)

    # 时间选择
    def inputDt_query_date(self, content):
        self.clean_label(content)
        self.inputDate(content, is_multi_tab=True)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
