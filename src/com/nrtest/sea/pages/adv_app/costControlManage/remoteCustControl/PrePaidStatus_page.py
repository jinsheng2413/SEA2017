# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→费控管理→远程费控→远程费控执行统计:按指令执行统计
class PrePaidStatusByActionPage(Page):
    # 控制类别
    def inputSel_ctrl_type(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 高级应用→费控管理→远程费控→远程费控执行统计:按用户执行统计
class PrePaidStatusByUserPage(Page):
    # 控制类别
    def inputSel_ctrl_type(self, name):
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
