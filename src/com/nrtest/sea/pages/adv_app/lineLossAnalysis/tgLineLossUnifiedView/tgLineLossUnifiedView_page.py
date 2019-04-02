# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossUnifiedView_page.py
@time: 2018/11/1 13:55
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→线损管理→台区线损统一视图→台区线损统一视图
class TgLineLossUnifiedViewPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

    # TAB页名称
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 日线损
    # 查询日期，开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search_day(self):
        self.btn_query(True, idx=2)

    # 月线损
    # 查询按钮
    def btn_search_month(self):
        self.btn_query(True, idx=2)
