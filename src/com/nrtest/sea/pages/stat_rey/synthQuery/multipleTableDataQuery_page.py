# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: multipleTableDataQuery_page.py
@time: 2018/10/10 16:01
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.multipleTableDataQuery_locators import MultipleTableDataQueryLocators


# 统计查询→综合查询→多表合一抄表数据查询
class MultipleTableDataQueryPage(Page):
    # 用户抄表数据
    # 用户编号
    def inputStr_cons_cons_no(self, content):
        self.input(content, *MultipleTableDataQueryLocators.CONS_CONS_NO)

    # 开始日期
    def inputDt_cons_start_date(self, content):
        self.exec_script(MultipleTableDataQueryLocators.CONS_START_DATE_JS)
        self.input(content, *MultipleTableDataQueryLocators.CONS_START_DATE)

    # 结束日期
    def inputDt_cons_end_date(self, content):
        self.exec_script(MultipleTableDataQueryLocators.CONS_END_DATE_JS)
        self.input(content, *MultipleTableDataQueryLocators.CONS_END_DATE)

    # 用户状态
    def inputSel_cons_cons_status(self, index):
        self.click(MultipleTableDataQueryLocators.CONS_CONS_STATUS)
        locator = self.get_select_locator(
            MultipleTableDataQueryLocators.CONS_CONS_STATUS_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(MultipleTableDataQueryLocators.BTN_SEARCH)
