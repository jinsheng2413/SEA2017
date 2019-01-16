# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: checkResultStat_page.py
@time: 2018/11/19 0019 10:34
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→档案核查管理→核查结果统计查询
class CheckResultStatPage(Page):

    # 异常类型
    def inputSel_except_type(self, options):
        self.selectCheckBox(options)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 任务类型
    def inputSel_task_type(self, options):
        self.selectCheckBox(options)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
