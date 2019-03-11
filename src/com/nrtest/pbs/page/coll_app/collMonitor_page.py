# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: coll_monitor_page.py
@time: 2019-03-06 14:38:37
@desc:
"""
from com.nrtest.pbs.locators.coll_app.collApp_locators import CollOperMain_locators
from com.nrtest.pbs.tree.tree_page import TreePBSPage


# 采集运维→采集监视
class CollMonitorPage(TreePBSPage):
    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 数据类型
    def inputChk_data_type(self, option):
        self.clickRadioBox(option)

    # 查询
    def btn_qry(self):
        self.click(CollOperMain_locators.BTN_SEARCH)
