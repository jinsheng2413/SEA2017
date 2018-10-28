# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: batchDataQuery_page.py
@time: 2018/9/29 18:10
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.batchDataQuery_locators import BatchDataQueryLocators


# 统计查询→综合查询→批量数据查询
class BatchDataQueryPage(Page):
    # 日期
    def inputDt_date(self, content):
        self.exec_script(BatchDataQueryLocators.DATE_JS)
        self.input(content, *BatchDataQueryLocators.DATE)

    # 终端资产号
    def inputStr_tmnl_asset_no(self, content):
        self.input(content, *BatchDataQueryLocators.TMNL_ASSET_NO)

    # 用户类型
    def inputCSel_cons_type(self, index):
        if index is 'c':
            self._find_element(*BatchDataQueryLocators.CONS_TYPE)
        else:
            self.click(*BatchDataQueryLocators.CONS_TYPE)
            locator = self.get_select_locator(BatchDataQueryLocators.CONS_TYPE_VALUE, index)
            self.click(*locator)
            self.click(*BatchDataQueryLocators.CONS_TYPE)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content, *BatchDataQueryLocators.TMNL_ADDR)

    # 查询按钮
    def btn_search(self):
        self.click(*BatchDataQueryLocators.BTN_SEARCH)
