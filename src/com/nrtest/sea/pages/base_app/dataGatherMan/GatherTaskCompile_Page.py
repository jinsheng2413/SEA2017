# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→定制任务管理

class GatherTaskCompilePage(Page):
    # 任务状态
    def inputSel_task_state(self, name):
        self.selectDropDown(name)

    # 终端类型
    def inputRSel_tmnl_type(self, name):
        self.selectDropDown(name)

    # 采集点名称
    def inputStr_collection_point_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 任务名称
    def inputStr_task_name(self, value):
        self.input(value)

    # 任务编号
    def inputStr_task_no(self, value):
        self.input(value)

    # 任务类型
    def inputSel_task_type(self, name):
        self.selectDropDown(name)

    # 查询
    def btn_qry(self):
        self.btn_query()
