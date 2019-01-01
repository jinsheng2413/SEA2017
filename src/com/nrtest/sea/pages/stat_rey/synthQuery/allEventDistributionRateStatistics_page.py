# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: allEventDistributionRateStatistics_page.py
@time: 2018/10/18 9:40
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.allEventDistributionRateStatistics_locators import \
    AllEventDistributionRateStatisticsLocators


# 统计查询→综合查询→全事件配置率统计
class AllEventDistributionRateStatisticsPage(Page):
    # 全事件配置率统计
    # 时间
    def inputDt_date(self, content):
        self.exec_script(AllEventDistributionRateStatisticsLocators.DATE_JS)
        self.input(content, *AllEventDistributionRateStatisticsLocators.DATE)

    # 查询按钮
    def btn_search(self):
        self.click(AllEventDistributionRateStatisticsLocators.BTN_SEARCH)

    # 全事件未配置明细
    # 时间
    def inputDt_date_tab(self, content):
        self.exec_script(
            AllEventDistributionRateStatisticsLocators.DATE_TAB_JS)
        self.input(content, *AllEventDistributionRateStatisticsLocators.DATE_TAB)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.click(AllEventDistributionRateStatisticsLocators.TMNL_TYPE)
        locator = self.get_select_locator(
            AllEventDistributionRateStatisticsLocators.TMNL_TYPE_VALUE, index)
        self.click(locator)

    # 查询按钮
    def btn_search_tab(self):
        self.click(AllEventDistributionRateStatisticsLocators.BTN_SEARCH_TAB)
