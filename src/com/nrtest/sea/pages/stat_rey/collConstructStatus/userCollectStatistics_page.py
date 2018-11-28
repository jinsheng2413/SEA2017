# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userCollectStatistics_page.py
@time: 2018/10/24 14:12
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.collConstructStatus.userCollectStatistics_locators import \
    UserCollectStatisticsLocators


# 统计查询→综合查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计
class UserCollectStatisticsPage(Page):
    # 用户类型
    def inputCSel_cons_type(self, value):
            self.click(*UserCollectStatisticsLocators.CONS_TYPE)
            self.selectCheckBox(value,flag=UserCollectStatisticsLocators.CONS_TYPE_ONLY)#用于标识那个下拉框
            self.click(*UserCollectStatisticsLocators.CONS_TYPE)

    # 统计月份
    def inputDt_date(self, content):
        self.exec_script(UserCollectStatisticsLocators.DATE_JS)
        self.input(content, *UserCollectStatisticsLocators.DATE)

    # 统计口径
    def inputSel_statistics_caliber(self, index):
        self.click(*UserCollectStatisticsLocators.STATISTICS_CALIBER)
        locator = self.get_select_locator(
            UserCollectStatisticsLocators.STATISTICS_CALIBER_VALUE, index)
        self.click(*locator)

    # 查询按钮
    def btn_search(self):
        self.click(*UserCollectStatisticsLocators.BTN_SEARCH)
