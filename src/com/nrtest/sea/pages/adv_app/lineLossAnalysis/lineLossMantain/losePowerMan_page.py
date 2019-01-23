# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: losePowerMan_page.py
@time: 2018/10/31 0031 13:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用-->线损分析→线损模型维护→线损模型设计
class LosePowerManPage(Page):
    # 考核单位状态
    def inputSel_assess_unit_state(self, name):
        self.selectDropDown(name)

    # 组合标志
    def inputSel_combination_sign(self, name):
        self.clean_label(name)
        self.selectDropDown(name)


    # 台区状态
    def inputSel_tg_status(self, name):
        self.selectDropDown(name)

    # 考核单位名称
    def inputStr_assess_unit_name(self, value):
        self.input(value)

    # 考核单位分类
    def inputSel_assess_unit_classficcation(self, name):
        self.selectDropDown(name)

    # 点击复选框
    def inputChk_uncover(self, name):
        self.clickSingleCheckBox(name)

    # 查询
    def btn_qry(self):
        self.btn_query()
