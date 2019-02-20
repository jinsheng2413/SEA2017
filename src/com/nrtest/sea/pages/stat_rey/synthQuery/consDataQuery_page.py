# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: consDataQuery_page.py
@time: 2018/12/13 9:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→用户数据查询
class ConsDataQueryPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


class ConsDataQueryDisplayPage(Page):

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()

    # tab页选择
    def inputChk_tab_name(self, tab_name):
        self.clickTabPage(tab_name)

    # 查询方式（实时或冻结）
    def inputChk_query_type(self, value):
        self.clickRadioBox(value, is_multi_tab=True, is_multi_elements=True)

    # 电表
    def inputSel_meter(self, value):
        self.selectDropDown(value)

    # 查询日期
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 至
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 第二个查询按钮
    def btn_search_tab(self):
        self.btn_query(True, idx=2)
