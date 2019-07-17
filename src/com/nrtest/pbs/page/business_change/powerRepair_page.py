# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: powerRepair_page.py
@time: 2019-07-08 10:07
@desc:
"""

from com.nrtest.common.base_page import Page


# 业务变更→电量追补
class PowerRepairPage(Page):
    # 区域
    def inputSel_query_area(self, value):
        self.selectDropDown(value)

    # 时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()