# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→费控管理→本地费控→电价参数管理::费率电价

class EleParaMan_rate_Page(Page):
    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)

    # 是否已生成参数
    def inputSel_ComeIntoPara(self, name):
        self.selectDropDown(name)


    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value, is_multi_tab=True)

    # 费率来源
    def inputChk_task_from(self, options):
        self.clickCheckBox_new(options)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 高级应用→费控管理→本地费控→电价参数管理::阶梯电价
class EleParaMan_step_Page(Page):
    # 开始时间
    def inputDt_start_time(self, value):
        self.inputDate(value)
        # 是否已生成参数

    def inputSel_ComeIntoPara(self, name):
        self.selectDropDown(name)

    # 结束时间
    def inputDt_end_time(self, value):
        self.inputDate(value)

    # 任务来源
    def inputChk_task_from(self, options):
        self.clickCheckBox_new(options)

    def btn_qry(self):
        self.btn_query(True)
