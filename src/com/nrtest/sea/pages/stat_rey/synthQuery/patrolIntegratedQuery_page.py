# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: patrolIntegratedQuery_page.py
@time: 2018/10/19 16:03
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.patrolIntegratedQuery_locators import PatrolIntegratedQueryLocators


# 统计查询→综合查询→巡检仪综合查询
class PatrolIntegratedQueryPage(Page):
    # 巡检仪运行指标
    # 日期
    def inputDt_date(self, content):
        self.exec_script(PatrolIntegratedQueryLocators.DATE_JS)
        self.input(content, *PatrolIntegratedQueryLocators.DATE)

    # 查询按钮
    def btn_search(self):
        self.click(PatrolIntegratedQueryLocators.BTN_SEARCH)

    # 巡检仪运行指标明细
    # 日期
    def inputDt_detail_date(self, content):
        self.exec_script(PatrolIntegratedQueryLocators.DETAIL_DATE_JS)
        self.input(content, *PatrolIntegratedQueryLocators.DETAIL_DATE)

    # 指标
    def inputSel_detail_index(self, index):
        self.click(PatrolIntegratedQueryLocators.DETAIL_INDEX)
        locator = self.get_select_locator(
            PatrolIntegratedQueryLocators.DETAIL_INDEX_VALUE, index)
        self.click(locator)

    # 终端地址
    def inputStr_detail_tmnl_addr(self, content):
        self.input(content, *PatrolIntegratedQueryLocators.DETAIL_TMNL_ADDR)

    # 查询按钮
    def btn_detail_search(self):
        self.click(PatrolIntegratedQueryLocators.BTN_DETAIL_SEARCH)
