# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dataTableAnalysis_page.py
@time: 2018/11/20 0020 14:21
@desc:
"""
from com.nrtest.sea.locators.sys_mam.dataClearing.DataStructureComparison_locators import \
    DataStructureComparisonLocators

from com.nrtest.common.base_page import Page


# 系统管理-->数据清理管理-->数模结构对照
class DataStructureComparisonPage(Page):
    # 核查日期
    def inputStr_examineDate(self, value):
        self.input(value, *DataStructureComparisonLocators.QRY_EXAMINE_DATE)

    # 表名称
    def inputStr_listName(self, value):
        self.input(value, *DataStructureComparisonLocators.QRY_LIST_NAME)

    # 数据组
    def inputSel_dataGroup(self, name):
        self.click(*DataStructureComparisonLocators.QRY_DATA_GROUP)
        locator = self.get_select_locator(DataStructureComparisonLocators.QRY_DATA_GROUP_VALUE, name)
        self.click(*locator)

        # 查询

    def btn_qry(self):
        self.click(*DataStructureComparisonLocators.BTN_QRY)
