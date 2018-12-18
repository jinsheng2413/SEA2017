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
        self.input(content)  # ,*ConsDataQueryLocators.QRY_CONS_NO)

    # 查询按钮
    def btn_search(self):
        # self.click(*ConsDataQueryLocators.BTN_SEARCH)
        self.btn_query()
