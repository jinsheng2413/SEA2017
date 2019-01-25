# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: elePricePara_pages.py
@time: 2018/8/15 0015 14:36
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→费控管理→本地费控→电价参数下发
class ElePricePages(Page):
    # 工单编号
    def inputStr_app_no(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 任务类型
    def inputSel_task_type(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 执行状态
    def inputSel_execute_status(self, option):
        self.clean_label(option)
        self.selectDropDown(option)


    # 接收时间
    def inputDt_receive_time(self, value):
        self.clean_label(value)
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
