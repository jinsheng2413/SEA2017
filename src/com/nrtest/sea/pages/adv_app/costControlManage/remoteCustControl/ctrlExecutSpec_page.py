# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: ctrlExecutSpec_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→费控管理→远程费控→专变用户远程费控执行
class CtrlExecutSpecPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 控制类型
    def inputSel_ctrl_type(self, options):
        self.selectDropDown(options)

    # 执行状态
    def inputSel_execute_status(self, options):
        self.selectDropDown(options)

    # 时间区间
    def inputChk_dt_interal(self, option):
        self.clickRadioBox(option)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 工单号
    def inputStr_app_no(self, value):
        self.input(value)

    # 查询

    def btn_qry(self):
        self.btn_query()
