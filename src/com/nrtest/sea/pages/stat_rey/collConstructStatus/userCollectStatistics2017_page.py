# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userCollectStatistics2017_page.py
@time: 2018/10/24 14:12
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计2017
class UserCollectStatistics2017Page(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(UserCollectStatistics2017Locators.CONS_TYPE)
        # locator = self.get_select_locator(
        #     UserCollectStatistics2017Locators.CONS_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 统计月份
    def inputDt_query_date(self, content):
        # self.exec_script(UserCollectStatistics2017Locators.DATE_JS)
        # self.input(content, *UserCollectStatistics2017Locators.DATE)
        self.inputDate(content)

    # 统计口径
    def inputSel_stat_scope(self, index):
        # self.click(UserCollectStatistics2017Locators.STAT_SCOPE)
        # locator = self.get_select_locator(
        #     UserCollectStatistics2017Locators.STAT_SCOPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search(self):
        # self.click(UserCollectStatistics2017Locators.BTN_SEARCH)
        self.btn_query()
