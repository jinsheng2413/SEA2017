# -*- coding:utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: sysRunContrastQuery_page.py
@time: 2018/11/6 15:24
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→报表管理→国网报表→采集系统运行指标
class SysRunContrastQueryPage(Page):

    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 统计口径

    def inputSel_stat_scope(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
