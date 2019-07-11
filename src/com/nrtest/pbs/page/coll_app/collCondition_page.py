# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: collCondition_page.py
@time: 2019-07-08 16:37
@desc:
"""

from com.nrtest.common.base_page import Page


# 采集运维→采集工况
class CollConditionPage(Page):
    # 数据中断时间超过
    def inputSel_time_out(self, value):
        self.selectDropDown(value)

    # 电压等级
    def inputSel_vol_level(self, value):
        self.inputDate(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()