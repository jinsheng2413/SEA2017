# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tmnlEventSendingFunction_page.py
@time: 2018/11/7 15:34
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→停电分析→终端是否具备停上电事件上送功能
class TmnlEventSendingFunctionPage(Page):
    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

# 高级应用→配变监测分析→停电分析→终端是否具备停上电事件上送功能→终端是否具备停上电事件上送功能明细
class TmnlEventSendingFunctionDeatilPage(Page):
    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 终端厂家
    def inputSel_tmnl_factory(self, index):
        self.selectDropDown(index)

    # 终端规约
    def inputSel_tmnl_protocol(self, index):
        self.selectDropDown(index)

    # 是否具备停上电事件上送功能
    def inputSel_sending_function(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
