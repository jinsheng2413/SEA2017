# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: allEventDistributionRateStatistics_page.py
@time: 2018/10/18 9:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→全事件配置率统计
class AllEventDistributionRateStatisticsPage(Page):
    # 全事件配置率统计
    # 时间
    def inputDt_date(self, content):
        # self.exec_script(AllEventDistributionRateStatisticsLocators.DATE_JS)
        # self.input(content, *AllEventDistributionRateStatisticsLocators.DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(AllEventDistributionRateStatisticsLocators.BTN_SEARCH)
        self.btn_query()

    # 全事件未配置明细
    # 时间
    def inputDt_date_tab(self, content):
        # self.exec_script(
        #     AllEventDistributionRateStatisticsLocators.DATE_TAB_JS)
        # self.input(content, *AllEventDistributionRateStatisticsLocators.DATE_TAB)
        self.inputDate(content)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        # self.click(AllEventDistributionRateStatisticsLocators.TMNL_TYPE)
        # locator = self.get_select_locator(
        #     AllEventDistributionRateStatisticsLocators.TMNL_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 查询按钮
    def btn_search_tab(self):
        # self.click(AllEventDistributionRateStatisticsLocators.BTN_SEARCH_TAB)
        self.btn_query(True)
