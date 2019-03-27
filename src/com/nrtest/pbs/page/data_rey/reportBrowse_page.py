# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: reportBrowse_page.py
@time: 2019-03-12 16:34:42
@desc:
"""
# 数据管理--报表浏览

from com.nrtest.common.base_page import Page


class ReportBrowsePage(Page):
    # 时间方案
    def inputChk_time_type(self, option):
        self.clickTabPage(option, is_by_js=True)

    # 结束
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 开始
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 生成报表
    def inputChk_generate_list(self, option):
        self.clickTabPage(option, is_by_js=True)

    # 导出报表
    def inputChk_export_list(self, option):
        self.clickTabPage(option, is_by_js=True)
