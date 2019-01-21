# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossStatistics_page.py
@time: 2018/11/1 16:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→台区线损统计查询→台区线损统计
class TgLineLossStatisticsPage(Page):
    # 线损维度
    def inputSel_line_loss_dimension(self, index):
        self.selectDropDown(index)

    # 开始时间
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束世间
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
