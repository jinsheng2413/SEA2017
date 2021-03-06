# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: logStatAnalysis_page.py
@time: 2018/11/21 0021 14:07
@desc:
"""
from com.nrtest.common.base_page import Page


# 系统管理→日志管理→日志统计分析
# 月统计登录失败top50
class LogStatAnalysis_fial_Page(Page):

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()


# 用户权限变更列表
class LogStatAnalysis_list_Page(Page):

    # 查询开始日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 管理员重置用户密码列表
class LogStatAnalysis_man_Page(Page):

    # 查询开始日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
