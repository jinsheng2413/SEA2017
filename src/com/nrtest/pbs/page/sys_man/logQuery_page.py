# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: logQuery_page.py
@time: 2019/3/13 14:14
@desc:
"""
from com.nrtest.common.base_page import Page


# 系统管理--日志查询
class LogQueryPage(Page):

    # 日志类型
    def inputSel_log_type(self, option):
        self.selectDropDown(option, is_line=True)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value, is_line=True)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value, is_line=True)

    # 操作用户
    def inputSel_oper_user(self, option):
        self.selectDropDown(option, is_line=True)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
