# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: loseCountPowerMan_page.py
@time: 2018/11/2 0002 8:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用-->线损分析→线损模型维护→线损计算模型管理
class LoseCountPowerManPage(Page):
    # 台区编码
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区运行状态
    def inputSel_run_status(self, name):
        self.selectDropDown(name)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 责任人工号
    def inputStr_responsibilier_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
