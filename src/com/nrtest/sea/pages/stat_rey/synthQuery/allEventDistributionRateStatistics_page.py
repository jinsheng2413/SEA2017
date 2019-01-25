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
    def inputDt_query_date(self, content):
        self.clean_label(content)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


class AllEventDistributionRateDetailPage(Page):
    # 全事件未配置明细
    # 时间
    def inputDt_query_date(self, content):
        self.clean_label(content)
        self.inputDate(content)

    # 终端类型
    def inputSel_tmnl_type(self, index):
        self.selectDropDown(index)

    # 查询按钮
    def btn_search_tab(self):
        self.btn_query(True)
