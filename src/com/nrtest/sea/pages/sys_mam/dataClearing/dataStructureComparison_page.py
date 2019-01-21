# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dataTableAnalysis_page.py
@time: 2018/11/20 0020 14:21
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→数据清理管理→数模结构对照
class DataStructureComparisonPage(Page):

    # 核查日期
    def inputDt_examine_date(self, value):
        self.inputDate(value)

    # 表名称
    def inputSel_table_name(self, value):
        self.input(value)

    # 数据组
    def inputSel_data_group(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
