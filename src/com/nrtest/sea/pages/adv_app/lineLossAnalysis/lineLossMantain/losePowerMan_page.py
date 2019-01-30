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
    # 考核单元名称
    def inputStr_chkunit_name(self, value):
        self.input(value)

    # 考核单元分类
    def inputSel_chkunit_type(self, option):
        self.selectDropDown(option)

    # 组合标志
    def inputSel_combination_flag(self, option):
        self.selectDropDown(option)

    # 考核单元状态
    def inputSel_chkunit_status(self, option):
        self.selectDropDown(option)

    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区状态
    def inputSel_tg_status(self, option):
        self.selectDropDown(option)

    # 线路编号
    def inputStr_line_no(self, value):
        self.input(value)

    # 未覆盖
    def inputChk_uncover(self, options):
        self.clickSingleCheckBox(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
    #
    # # 考核单位状态
    # def inputSel_chkunit_status(self, name):
    #     self.selectDropDown(name)
    #
    # # 组合标志
    # def inputSel_combination_sign(self, name):
    #     self.clean_label(name)
    #     self.selectDropDown(name)
    #
    #
    # # 台区状态
    # def inputSel_tg_status(self, name):
    #     self.selectDropDown(name)
    #
    # # 考核单位名称
    # def inputStr_chkunit_name(self, value):
    #     self.input(value)
    #
    # # 考核单位分类
    # def inputSel_chkunit_type(self, name):
    #     self.selectDropDown(name)
    #
    # # 点击复选框
    # def inputChk_uncover(self, name):
    #     self.clickSingleCheckBox(name)
    #
    # # 查询
    # def btn_qry(self):
    #     self.btn_query()
