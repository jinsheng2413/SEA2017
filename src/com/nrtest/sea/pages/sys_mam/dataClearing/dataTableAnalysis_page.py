# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dataTableAnalysis_page.py
@time: 2018/11/20 0020 14:21
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.dataClearing.dataTableAnalysis_locators import DataTableAnalysisLocators


# 系统管理-->数据清理管理-->数据表分析
class DataTableAnalysisPage(Page):
    # 核查日期
    def inputStr_examineDate(self, value):
         self.input(value)

    # 表名称
    def inputStr_listName(self, value):
        self.input(value)

    # 数据组
    def inputSel_dataGroup(self, options):
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
