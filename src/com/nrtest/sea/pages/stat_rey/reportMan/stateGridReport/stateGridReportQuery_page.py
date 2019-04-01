# -*- coding:utf-8 -*-
"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: stateGridReportQuery_page.py
@time: 2018/11/8 11:38
@desc:
"""
from com.nrtest.common.base_page import Page


# 统计查询→报表管理→国网报表→国网报表新

class StateGridReportQueryPage(Page):
    # 报表类型
    def inputSel_report_type(self, option):
        self.selectDropDown(option)

    # 查询方式
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 切换tab页
    def inputChk_tab_name(self, option):
        self.clickTabPage(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
