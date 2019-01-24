# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: costControlManage_page.py
@time: 2018/8/2 0002 18:53
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→费控管理→本地费控→专变用户费控管理
class CostControlManagePage(Page):

    # 营销单号
    def inputStr_app_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)

    # 业务类型
    def inputSel_business_type(self, index):
        self.selectDropDown(index)

    # 参数下发状态
    def inputSel_para_status(self, index):
        self.selectDropDown(index)

    # 购电日期
    def inputSel_buy_ele_date(self, index):
        self.selectDropDown(index)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 点击查询按钮
    def btn_qry(self):
        self.btn_query()
