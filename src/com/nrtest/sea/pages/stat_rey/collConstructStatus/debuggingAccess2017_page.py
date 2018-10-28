# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: debuggingAccess2017_page.py
@time: 2018/10/25 16:49
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.collConstructStatus.debuggingAccess2017_locators import \
    DebuggingAccess2017Locators


# 统计查询→综合查询→采集建设情况→调试接入情况2017
class DebuggingAccess2017Page(Page):
    # 页面元素
    # 管理方式
    def inputSel_manage_style(self, index):
        self.click(*DebuggingAccess2017Locators.MANAGE_STYLE)
        locator = self.get_select_locator(DebuggingAccess2017Locators.MANAGE_STYLE_VALUE, index)
        self.click(*locator)

    # 装接方式
    def inputCSel_assembling_way(self, index):
        if index is 'c':
            self._find_element(*DebuggingAccess2017Locators.ASSEMBLING_WAY)
        else:
            self.click(*DebuggingAccess2017Locators.ASSEMBLING_WAY)
            locator = self.get_select_locator(DebuggingAccess2017Locators.ASSEMBLING_WAY_VALUE, index)
            self.click(*locator)
            self.click(*DebuggingAccess2017Locators.ASSEMBLING_WAY)

    # 日期
    def inputDt_date(self, content):
        self.exec_script(DebuggingAccess2017Locators.DATE_JS)
        self.input(content, *DebuggingAccess2017Locators.DATE)

    # 查询按钮
    def btn_search(self):
        self.click(*DebuggingAccess2017Locators.BTN_SEARCH)
