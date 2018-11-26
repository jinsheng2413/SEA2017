# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dataTableAnalysis_page.py
@time: 2018/11/20 0020 14:21
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.dataClearing.dataStrategyManagenment_locators import \
    DataStrategyManagenmentLocators


# 系统管理-->数据清理管理-->历史数据策略管理
class DataStrategyManagenmentPage(Page):
    # 存储周期
    def inputSel_storageCycle(self, name):
        self.click(*DataStrategyManagenmentLocators.QRY_STORAGE_CYCLE)
        locator = self.get_select_locator(DataStrategyManagenmentLocators.QRY_STORAGE_CYCLE_VALUE, name)
        self.click(*locator)

    # 表名称
    def inputStr_listName(self, value):
        self.input(value, *DataStrategyManagenmentLocators.QRY_LIST_NAME)

    # 数据组
    def inputSel_dataGroup(self, name):
        self.click(*DataStrategyManagenmentLocators.QRY_DATA_GROUP)
        locator = self.get_select_locator(DataStrategyManagenmentLocators.QRY_DATA_GROUP_VALUE, name)
        self.click(*locator)

        # 查询

    def btn_qry(self):
        self.click(*DataStrategyManagenmentLocators.BTN_QRY)
