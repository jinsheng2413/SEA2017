# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: gisPanoramaDisplay_page.py
@time: 2019-02-19 08:53:09
@desc:
"""

from com.nrtest.common.base_page import Page

# 统计查询→数据分析→电量分析→电量数据查询
class GisPanoramaDisplayPage(Page):
    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 逐日显示
    def inputSel_day_display(self, option):
        self.selectDropDown(option)

    # 用户类型
    def inputSel_cons_type(self, option):
        self.selectDropDown(option)

    # 查询方式
    def inputChk_query_type(self, option):
        self.clickRadioBox(option)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
