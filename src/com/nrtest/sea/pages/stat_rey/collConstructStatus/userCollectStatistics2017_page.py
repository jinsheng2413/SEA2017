# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userCollectStatistics_page.py
@time: 2018/10/24 14:12
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.collConstructStatus.userCollectStatistics2017_locators import \
    UserCollectStatistics2017Locators


# 统计查询→综合查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计2017
class UserCollectStatistics2017Page(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.click(UserCollectStatistics2017Locators.CONS_TYPE)
        locator = self.get_select_locator(
            UserCollectStatistics2017Locators.CONS_TYPE_VALUE, index)
        self.click(locator)

    # 统计月份
    def inputDt_date(self, content):
        self.exec_script(UserCollectStatistics2017Locators.DATE_JS)
        self.input(content, *UserCollectStatistics2017Locators.DATE)

    # 统计口径
    def inputSel_statistics_caliber(self, index):
        self.click(UserCollectStatistics2017Locators.STATISTICS_CALIBER)
        locator = self.get_select_locator(
            UserCollectStatistics2017Locators.STATISTICS_CALIBER_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search(self):
        self.click(UserCollectStatistics2017Locators.BTN_SEARCH)
