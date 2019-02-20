# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: coreFunctionAudit_page.py
@time: 2018/11/21 0021 9:56
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统使用情况统计→系统使用情况统计
class CoreFunctionAuditPage(Page):
    # 操作员
    def inputStr_operator(self, value):
        self.input(value)

    # 访问时间
    def inputDt_visit_time(self, value):
        self.inputDate(value)

    # 到
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()