# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→数据召测→批量巡测
class BatchFetchPage(Page):

    # 任务名称
    def inputStr_task_name(self, value):
        self.input(value)

    # 有效性
    def inputSel_effectiveness(self, name):
        self.selectDropDown(name)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 操作人
    def inputStr_operator(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
