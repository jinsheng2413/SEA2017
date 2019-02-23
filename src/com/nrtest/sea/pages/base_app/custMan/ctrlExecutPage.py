# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: ctrlExecutPage.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→费控管理→远程费控→低压用户远程费控执行
class CtrlExecutPage(Page):
    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 抄表段号
    def inputStr_mr_sect_no(self, value):
        self.input(value)

    # 工单号
    def inputStr_app_no(self, value):
        self.input(value)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 控制类型
    def inputSel_ctrl_type(self, options):
        self.selectDropDown(options)

    # 执行状态
    def inputSel_execute_status(self, options):
        self.selectDropDown(options)

    # 数据来源
    def inputSel_data_src(self, options):
        self.selectDropDown(options)

    # 确认状态
    def inputSel_confirm_status(self, options):
        self.selectDropDown(options)

    # 执行结果状态
    def inputSel_exe_result_status(self, options):
        self.selectDropDown(options)

    # 时间区间
    def inputChk_dt_interal(self, option):
        self.clickRadioBox(option)

    # 查询

    def btn_qry(self):
        self.btn_query()
