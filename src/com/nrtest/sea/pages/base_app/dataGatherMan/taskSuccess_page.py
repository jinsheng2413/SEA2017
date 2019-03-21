# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: ReadCompleteRate_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量检查(new)→采集任务成功率

class TaskSuccessPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 任务名称
    def inputSel_task_name(self, value):
        self.selectDropDown(value)

    # 查询
    def btn_query(self):
        self.btn_query(True)
