# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sectfailedAppQuery_page.py
@time: 2018/10/29 11:19
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→工单处理→抄表失败工单查询
class SectfailedAppQueryPage(Page):
    # 时间范围
    def inputChk_date_range(self, content):
        self.clickRadioBox(content)

    # 开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 抄表段号
    def inputStr_mr_sect_no(self, content):
        self.input(content)

    # 抄表管理员工号
    def inputStr_sect_manager_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
