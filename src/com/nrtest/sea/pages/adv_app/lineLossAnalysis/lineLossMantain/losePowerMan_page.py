# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: losePowerMan_page.py
@time: 2018/10/31 0031 13:27
@desc:
"""

from com.nrtest.common.base_page import Page

# 高级应用→线损管理→线损模型维护→线损模型设计
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossMantain.losePowerMan_locators import LosePowerManLocators


class LosePowerManPage(Page):
    # 考核单元名称
    def inputStr_chkunit_name(self, value):
        self.input(value)

    # 考核单元分类
    def inputSel_chkunit_type(self, option):
        self.selectDropDown(option)

    # 组合标志
    def inputSel_combination_flag(self, option):
        self.clean_label(option)
        self.selectDropDown(option)

    # 考核单元状态
    def inputSel_chkunit_status(self, option):
        self.selectDropDown(option)

    # 台区编号
    def inputStr_tg_no(self, value):
        loc = self.format_xpath(LosePowerManLocators.QRY_NO, value.split(';')[0])
        self.specialInput(loc, value)

    # 台区状态
    def inputSel_tg_status(self, option):
        self.selectDropDown(option)

    # 线路编号
    def inputStr_line_no(self, value):
        loc = self.format_xpath(LosePowerManLocators.QRY_NO, value.split(';')[0])
        self.specialInput(loc, value)

    # 未覆盖
    def inputChk_uncover(self, options):
        self.clickSingleCheckBox(options)

    # 查询
    def btn_qry(self):
        self.btn_query()
