# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: ReadCompleteRate_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量检查(new)→后台任务查询

class BackgroundTaskQueryPage(Page):
    # 任务来源
    def inputSel_task_from(self, value):
        self.selectDropDown(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 任务当前状态
    def inputSel_task_status(self, value):
        self.selectDropDown(value)

    # 任务时间从
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 到
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_query(self):
        self.btn_query(True)
