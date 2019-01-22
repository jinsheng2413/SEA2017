# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→定制任务管理:任务查询

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
        self.curr_input(value, is_multi_elements=True, is_multi_tab=True)

    # 任务编号
    def inputStr_task_no(self, value):
        self.input(value)

    # 任务类型
    def inputSel_task_type(self, name):
        self.selectDropDown(name)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 基本应用→数据采集管理→定制任务管理:执行结果分析
class GatherTaskCompile_result_Page(Page):

    # 任务名称
    def inputStr_task_name(self, value):
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 任务编号
    def inputStr_task_no(self, value):
        self.selectDropDown(value)

    # 开始时间
    def inputDT_startTime(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDT_endTime(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
