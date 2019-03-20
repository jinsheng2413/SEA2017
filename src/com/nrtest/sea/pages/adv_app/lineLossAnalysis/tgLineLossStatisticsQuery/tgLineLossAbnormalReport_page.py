# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossAbnormalReport_page.py
@time: 2018/11/2 11:06
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→台区线损统计查询→台区线损异常报表
class TgLineLossAbnormalReportPage(Page):
    # 线损维度
    def inputSel_line_loss_dimension(self, index):
        self.selectDropDown(index)

    # 责任人工号
    def inputStr_emp_no(self, content):
        self.input(content)

    # 查询日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
