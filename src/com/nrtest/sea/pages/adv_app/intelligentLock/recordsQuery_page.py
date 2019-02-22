# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: recordsQuery_page.py
@time: 2018/10/26 16:43
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→智能锁具→记录查询
class RecordsQueryPage(Page):
    # 开关锁操作日志
    # 操作员名称
    def inputStr_staff_name(self, content):
        self.input(content)

    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 用户名称
    def inputStr_cons_name(self, content):
        self.input(content)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectDropDown(index)

    # 操作行为
    def inputSel_operant_hehavior(self, index):
        self.selectDropDown(index)

    # 操作结果
    def inputSel_operant_result(self, index):
        self.selectDropDown(index)

    # 电子钥匙编号
    def inputStr_key_no(self, content):
        self.input(content)

    # 锁封编号
    def inputStr_lock_no(self, content):
        self.input(content)

    # 开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()


# 资产管理记录查询
class RecordsQueryStaffPage(Page):
    # 操作员名称
    def inputStr_staff_name(self, content):
        self.curr_input(content, True, True)

    # 电子钥匙编号
    def inputStr_key_no(self, content):
        self.curr_input(content, True, True)

    # 锁封编号
    def inputStr_lock_no(self, content):
        self.curr_input(content, True, True)

    # 锁封用户编号
    def inputStr_lock_user_no(self, content):
        self.curr_input(content, True, True)

    # 开始日期
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query(True)
