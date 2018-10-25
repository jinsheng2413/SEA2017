# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: debuggingAccess_page.py
@time: 2018-10-24 16:10
@desc:
'''

from com.nrtest.sea.locators.stat_rey.collConstructStatus.debuggingAccess_locators import DebuggingAccessLocators
from com.nrtest.common.base_page import Page


#统计查询→综合查询→采集建设情况→调试接入情况
class DebuggingAccessPage(Page):
# 页面元素
    # 管理方式
    def inputSel_manage_style(self,index):
        self.click(*DebuggingAccessLocators.MANAGE_STYLE)
        locator = self.get_select_locator(DebuggingAccessLocators.MANAGE_STYLE_VALUE, index)
        self.click(*locator)
    # 装接方式
    def inputCSel_assembling_way(self,index):
        if index is 'c':
            self._find_element(*DebuggingAccessLocators.ASSEMBLING_WAY)
        else:
            self.click(*DebuggingAccessLocators.ASSEMBLING_WAY)
            locator = self.get_select_locator(DebuggingAccessLocators.ASSEMBLING_WAY_VALUE,index)
            self.click(*locator)
            self.click(*DebuggingAccessLocators.ASSEMBLING_WAY)
    # 日期
    def inputDt_date(self,content):
        self.exec_script(DebuggingAccessLocators.DATE_JS)
        self.input(content,*DebuggingAccessLocators.DATE)
    # 查询按钮
    def btn_search(self):
        self.click(*DebuggingAccessLocators.BTN_SEARCH)
