# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: logStatAnalysis_page.py
@time: 2018/11/21 0021 14:07
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.logMan.logStatAnalysis_locators import *


# 系统管理--》日志管理--》日志统计分析
class LogStatAnalysis_fial_Page(Page):
    # 
    def inputStr_date(self, value):
        self.input(value, *LogStatAnalysis_fail_Locators.QRY_DATE)

        # 查询

    def btn_qry(self):
        self.click(*LogStatAnalysis_fail_Locators.BTN_QRY)


# 系统管理--》日志管理--》日志统计分析
class LogStatAnalysis_list_Page(Page):
    # 查询日期
    def inputStr_queryDate(self, value):
        self.input(value, *LogStatAnalysis_list_Locators.QRY_QUERY_DATE)

    # 结束时间
    def inputStr_TO(self, value):
        self.input(value, *LogStatAnalysis_list_Locators.QRY_TO)

        # 查询

    def btn_qry(self):
        self.click(*LogStatAnalysis_list_Locators.BTN_QRY)


# 系统管理--》日志管理--》日志统计分析
class LogStatAnalysis_man_Page(Page):
    # 查询日期
    def inputStr_queryDate(self, value):
        self.input(value, *LogStatAnalysis_man_Locators.QRY_QUERY_DATE)

    # 结束时间
    def inputStr_TO(self, value):
        self.input(value, *LogStatAnalysis_man_Locators.QRY_TO)

    # 查询
    def btn_qry(self):
        self.click(*LogStatAnalysis_man_Locators.BTN_QRY)
