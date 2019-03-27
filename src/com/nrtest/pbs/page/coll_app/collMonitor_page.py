# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: collMonitor_page.py
@time: 2019-03-06 14:38:37
@desc:
"""
from com.nrtest.common.base_page import Page


# 采集运维→采集监视
class CollMonitorPage(Page):
    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 数据类型
    def inputChk_data_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
