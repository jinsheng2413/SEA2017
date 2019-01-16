# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesAnalysisOfAnomaly_locators.py
@time: 2018/8/29 0029 15:56
@desc:
"""
from com.nrtest.common.base_page import Page


# 基本应用→档案管理→档案异常分析：档案异常统计
class ArchivesAnalysisOfAnomaly_count_pages(Page):

    # 用户类型
    def inputSel_cons_sort(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 日期
    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 【操作区】
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→档案管理→档案异常分析：档案异常明细
class ArchivesAnalysisOfAnomaly_detail_pages(Page):

    # 确定
    def btn_qry(self):
        self.btn_query(True)

    # 用户类型
    def inputSel_cons_sort(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 日期
    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 档案类型
    def inputRSel_archives_type(self, index):
        self.selectDropDown(index)
