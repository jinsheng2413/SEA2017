# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: multipleTableDataQuery_page.py
@time: 2018/10/10 16:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→多表合一抄表数据查询
# 用户抄表数据
class MultipleTableDataQueryPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  # , *MultipleTableDataQueryLocators.CONS_CONS_NO)

    # 开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(MultipleTableDataQueryLocators.CONS_START_DATE_JS)
        # self.input(content, *MultipleTableDataQueryLocators.CONS_START_DATE)
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        # self.exec_script(MultipleTableDataQueryLocators.CONS_END_DATE_JS)
        # self.input(content, *MultipleTableDataQueryLocators.CONS_END_DATE)
        self.inputDate(content)

    # 用户状态
    def inputSel_cons_status(self, index):
        # self.click(MultipleTableDataQueryLocators.CONS_CONS_STATUS)
        # locator = self.get_select_locator(
        #     MultipleTableDataQueryLocators.CONS_CONS_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        # self.click(MultipleTableDataQueryLocators.BTN_SEARCH)
        self.btn_query()


# 终端抄表数据
class MultipleTableDataQueryTmnlPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, index):
        self.input(index)

    # 用户状态
    def inputSel_cons_status(self, index):
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputDt_query_date(self, index):
        self.inputDate(index)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
